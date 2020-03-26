#include "src/Bossy.h"

Bossy bossy;

void setup() {
  Serial.begin(9600);
}

void loop() {
  //int value = bossy.readValue(LEFT_JOYSTICK_UPPER_X);
  //int value = bossy.readState(LEFT_BUTTON_UPPER);

  print_on_pot_reading_change("p0: ", POT_LEFT);
  print_on_pot_reading_change("p1: ", POT_LEFT_CENTER);
  print_on_pot_reading_change("p2: ", POT_CENTER);
  print_on_pot_reading_change("p3: ", POT_RIGHT_CENTER);
  print_on_pot_reading_change("p4: ", POT_RIGHT);
  
  print_on_button_state_change("b-UL: ", LEFT_BUTTON_UPPER);
  print_on_button_state_change("b-LL: ", LEFT_BUTTON_LOWER);
  print_on_button_state_change("b-UR: ", RIGHT_BUTTON_UPPER);
  print_on_button_state_change("b-LR: ", RIGHT_BUTTON_LOWER);

  print_on_button_state_change("jb-UL: ", LEFT_JOYSTICK_UPPER_BUTTON);
  print_on_button_state_change("jb-LL: ", LEFT_JOYSTICK_LOWER_BUTTON);
  print_on_button_state_change("jb-UR: ", RIGHT_JOYSTICK_UPPER_BUTTON);
  print_on_button_state_change("jb-LR: ", RIGHT_JOYSTICK_LOWER_BUTTON);

  print_on_scale_change("jx-UL: ", LEFT_JOYSTICK_UPPER_X);
  print_on_scale_change("jx-LL: ", LEFT_JOYSTICK_LOWER_X);
  print_on_scale_change("jx-UR: ", RIGHT_JOYSTICK_UPPER_X);
  print_on_scale_change("jx-LR: ", RIGHT_JOYSTICK_LOWER_X);

  print_on_scale_change("jy-UL: ", LEFT_JOYSTICK_UPPER_Y);
  print_on_scale_change("jy-LL: ", LEFT_JOYSTICK_LOWER_Y);
  print_on_scale_change("jy-UR: ", RIGHT_JOYSTICK_UPPER_Y);
  print_on_scale_change("jy-LR: ", RIGHT_JOYSTICK_LOWER_Y);

  print_on_scale_change("sw-UL: ", LEFT_SWITCH_UPPER);
  print_on_scale_change("sw-LL: ", LEFT_SWITCH_LOWER);
  print_on_scale_change("sw-UR: ", RIGHT_SWITCH_UPPER);
  print_on_scale_change("sw-RL: ", RIGHT_SWITCH_LOWER);
}

void print_on_button_state_change(String prefix, int input_id) {
  if (bossy.hasChangedState(input_id)) {
    Serial.print(prefix);    
    bossy.savedState(input_id)==PUSHED ? 
      Serial.println("pressed") : Serial.println("not_pressed");
  }
}

void print_on_pot_reading_change(String prefix, int input_id) {
  if (bossy.hasChangedReading(input_id)) {
    Serial.print(prefix);
    Serial.print(bossy.savedReading(input_id));
    Serial.print(" ");
    Serial.println(bossy.savedReadingLowRes(input_id));
  }
}

void print_on_scale_change(String prefix, int input_id) {
  if (bossy.hasChangedState(input_id)) {
    Serial.print(prefix);
    Serial.println(bossy.savedState(input_id));
  }
}
