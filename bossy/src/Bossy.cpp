#include "Arduino.h"
#include "Bossy.h"

Bossy::Bossy(void) {
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);

  pinMode(PIN_ENABLE_LEFT_MUX, OUTPUT);
  pinMode(PIN_ENABLE_RIGHT_MUX, OUTPUT);

  digitalWrite(s0, LOW);
  digitalWrite(s1, LOW);
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);

  // pulling down enable pin to ground enables the multiplexer
  digitalWrite(PIN_ENABLE_LEFT_MUX, HIGH);
  digitalWrite(PIN_ENABLE_RIGHT_MUX, HIGH);

  // set all readings to a random number, nonsense number
  for (uint8_t input_id = 0; input_id < NUMBER_OF_CHANNELS; input_id++) {
    _update(input_id);
  }
}

uint16_t Bossy::savedReading(const uint8_t input_id) {
  const uint8_t i = _constrain(input_id);
  return _readings[i];
}

uint16_t Bossy::savedState(const uint8_t input_id) {
  const uint8_t i = _constrain(input_id);
  return _states[i];
}

uint8_t Bossy::savedReadingLowRes(const uint8_t input_id){
  // convert reading from range 0-1023 to 0-255
  const uint8_t i = _constrain(input_id);
  return min(_readings[i] / 4, 255);
}

uint16_t Bossy::readValue(const uint8_t input_id) {
  const uint8_t i = _constrain(input_id);
  _update(i);
  return _readings[i];
}

uint8_t Bossy::readState(const uint8_t input_id) {
  const uint8_t i = _constrain(input_id);
  _update(i);
  return _states[i];
}

bool Bossy::hasChangedState(const uint8_t input_id) {
  const uint8_t i = _constrain(input_id);
  const uint16_t old_state = _states[i];
  _update(i);
  return old_state != _states[i] ? true: false;
}

bool Bossy::hasChangedReading(const uint8_t input_id) {
  const uint8_t i = _constrain(input_id);
  const uint16_t old_reading = _readings[i];
  _update(i);
  const uint16_t new_reading = _readings[i];

  // remove noise, especially of potentiometer
  const uint16_t TOL = 2;
  if (old_reading > new_reading) {
    return old_reading - new_reading > TOL;
  }
  return new_reading - old_reading > TOL;
}

void Bossy::_update(const uint8_t input_id) {
  
  //temporarily makeshift function for joystick buttons without pullup resistors
  if (_isBrokenButton(input_id)) {
    _updateBrokenButton(input_id);
    return;
  }

  _updateReading(input_id);
  _updateState(input_id);
}

void Bossy::_updateState(const uint8_t input_id) {
  const uint16_t reading = _readings[input_id];
  const bool input_type = INPUT_TYPE[input_id];

  if (input_type == NORMAL) {
    if (reading < 200) { _states[input_id] = SCALE_0; return; }
    if (reading < 400) { _states[input_id] = SCALE_1; return; }
    if (reading < 600) { _states[input_id] = SCALE_2; return; }
    if (reading < 800) { _states[input_id] = SCALE_3; return; }
    _states[input_id] = SCALE_4; return;
  } else {
    if (reading > 800) { _states[input_id] = SCALE_0; return; }
    if (reading > 600) { _states[input_id] = SCALE_1; return; }
    if (reading > 400) { _states[input_id] = SCALE_2; return; }
    if (reading > 200) { _states[input_id] = SCALE_3; return; }
    _states[input_id] = SCALE_4; return;
  }
}

void Bossy::_updateReading(const uint8_t input_id) {

  // check and enable multiplexer we are suppose to read from
  const bool is_left_mux = input_id >= MUX_LEFT_MIN && input_id <= MUX_LEFT_MAX;
  is_left_mux ? _enableLeftMux() : _enableRightMux();

  //debounce if it's a button else just save the reading
  if (_isButton(input_id)) {
    _saveDebouncedReading(input_id);
    return;
  }
  const uint8_t channel = INPUT_CHANNEL[input_id];
  _readings[input_id] = _readMux(channel);
}

void Bossy::_enableLeftMux(void) {
  digitalWrite(PIN_ENABLE_LEFT_MUX, LOW);
  digitalWrite(PIN_ENABLE_RIGHT_MUX, HIGH);
}

void Bossy::_enableRightMux(void) {
  digitalWrite(PIN_ENABLE_LEFT_MUX, HIGH);
  digitalWrite(PIN_ENABLE_RIGHT_MUX, LOW);
}

uint16_t Bossy::_readMux(const uint8_t channel) {
  const uint8_t controlPin[] = {s0, s1, s2, s3};

  const uint8_t muxChannel[16][4]= {
    {0, 0, 0, 0}, //channel 0
    {1, 0, 0, 0}, //channel 1
    {0, 1, 0, 0}, //channel 2
    {1, 1, 0, 0}, //channel 3
    {0, 0, 1, 0}, //channel 4
    {1, 0, 1, 0}, //channel 5
    {0, 1, 1, 0}, //channel 6
    {1, 1, 1, 0}, //channel 7
    {0, 0, 0, 1}, //channel 8
    {1, 0, 0, 1}, //channel 9
    {0, 1, 0, 1}, //channel 10
    {1, 1, 0, 1}, //channel 11
    {0, 0, 1, 1}, //channel 12
    {1, 0, 1, 1}, //channel 13
    {0, 1, 1, 1}, //channel 14
    {1, 1, 1, 1}  //channel 15
  };

  //Send the appropriate signals
  for(int i = 0; i < 4; i ++){
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  return analogRead(PIN_SIGNAL);
}

bool Bossy::_isButton(const uint8_t input_id) {
  for (uint8_t i = 0; i < NUMBER_OF_BOOLEAN_INPUTS; i++) {
    if (BOOLEAN_INPUTS[i] == input_id) { return true; }
  }
  return false;
}

void Bossy::_saveDebouncedReading(const uint8_t input_id) {
  const uint8_t channel = INPUT_CHANNEL[input_id];
  const uint16_t reading = _readMux(channel);
  // if current reading is not the same as the saved reading
  // the state might have changed, double check if this is the case
  if (reading != _readings[input_id]) {
    _delay_ms(5);
    const uint16_t second_reading = _readMux(channel);
    if (second_reading == reading) {
      _readings[input_id] = reading;
    }
  }
}

uint8_t Bossy::_constrain(const uint8_t input_id) {
  // input id can only be within 0-24
  return min(max(0, input_id), NUMBER_OF_CHANNELS - 1);
}

bool Bossy::_isBrokenButton(const uint8_t input_id) {
  for (uint8_t i = 0; i < 4; i++) {
    if (BROKEN_BUTTONS[i]==input_id) { return true; }
  }
  return false;
}

void Bossy::_updateBrokenButton(const uint8_t input_id) {

  const bool is_left_mux = input_id >= MUX_LEFT_MIN && input_id <= MUX_LEFT_MAX;
  is_left_mux ? _enableLeftMux() : _enableRightMux();
  
  const uint8_t channel = INPUT_CHANNEL[input_id];
  uint16_t reading = _readMux(channel);
  reading = reading == 0 ? 0 : 1023;
  
  // if current reading is not the same as the saved reading
  // the state might have changd, double check if this is the case
  if (reading != _readings[input_id]) {

    _delay_ms(50);
    uint16_t second_reading = _readMux(channel);
    second_reading = second_reading == 0 ? 0 : 1023;

    if (second_reading == reading) {
      _readings[input_id] = reading;
    }
  }

  _states[input_id] = _readings[input_id] == 0 ? PUSHED : NOT_PUSHED;
}

