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

  // Pulling down enable pin to ground enables the multiplexer
  digitalWrite(PIN_ENABLE_LEFT_MUX, HIGH);
  digitalWrite(PIN_ENABLE_RIGHT_MUX, HIGH);

  // set all readings to zero
  for (uint8_t input_id = 0; input_id < NUMBER_OF_CHANNELS; input_id++) {
    _readings[input_id] = 0;
    _states[input_id] = NEUTRAL;
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
  const uint8_t i = _constrain(input_id);
  return max(_readings[i] / 4, 255);
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
  return old_reading != _readings[i] ? true: false;
}

void Bossy::_update(const uint8_t input_id) {
  _updateReading(input_id);
  _updateState(input_id);
}

void Bossy::_updateState(const uint8_t input_id) {
  const uint16_t reading = _readings[input_id];
  const bool input_type = INPUT_TYPE[input_id];

  // update if a button input
  if (_isButton(input_id)) {
    const uint16_t MIN_THRESH = 100;
    const uint16_t MAX_THRESH = 900;

    if (input_type == NORMAL) {
      _states[input_id] = reading > MAX_THRESH ? PUSHED : NEUTRAL;
    } else {
      _states[input_id] = reading < MIN_THRESH ? PUSHED : NEUTRAL;
    }
    return;
  }

  // update if a non-button input
  // 0, 200, 400, 600, 800
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
  if (input_id >= MUX_LEFT_MIN && input_id <= MUX_LEFT_MAX) {
    _enableLeftMux();
  } else {
    _enableRightMux();
  }

  // read the appropriate channel of that multiplexer
  const uint8_t channel = INPUT_CHANNEL[input_id];
  uint16_t value = _readMux(channel);

  if (_isButton(input_id)) {
    // THERE ARE BETTER WAYS TO DEBOUNCE A BUTTON but this is good enough
    _delay_ms(10);
    uint16_t new_value = _readMux(channel);
    // if the new value is not same as the value before throw these values away
    if (new_value != value) {
      value = _readings[input_id];
    }
  }

  // finally update the value
  _readings[input_id] = value;
}

void Bossy::_enableLeftMux(void) {
  digitalWrite(PIN_ENABLE_LEFT_MUX, LOW);
  digitalWrite(PIN_ENABLE_RIGHT_MUX, HIGH);
}

void Bossy::_enableRightMux(void) {
  digitalWrite(PIN_ENABLE_LEFT_MUX, LOW);
  digitalWrite(PIN_ENABLE_RIGHT_MUX, HIGH);
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

  //loop through the 4 control pins
  for(int i = 0; i < 4; i ++){
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  return analogRead(PIN_SIGNAL);
}

uint8_t Bossy::_constrain(const uint8_t input_id) {
  return min(max(0, input_id), NUMBER_OF_CHANNELS - 1);
}

bool Bossy::_isButton(const uint8_t input_id) {
  for (uint8_t i = 0; i < NUMBER_OF_BOOLEAN_INPUTS; i++) {
    if(BOOLEAN_INPUTS[i]==input_id) { return true; }
  }
  return false;
}
