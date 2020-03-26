#include "src/Bossy.h"

Bossy bossy;

void setup() {
  Serial.begin(9600);
}

void loop() {

  //int p1 = bossy.readValue(LEFT_BUTTON_UPPER);
  
  print_button_when_changed_state("upperleft b", LEFT_BUTTON_UPPER);
  print_button_when_changed_state("lowerleft b", LEFT_BUTTON_LOWER);
  print_button_when_changed_state("upperright b", RIGHT_BUTTON_UPPER);
  print_button_when_changed_state("lowerright b", RIGHT_BUTTON_LOWER);

  print_button_when_changed_state("upperleft jb", LEFT_JOYSTICK_UPPER_BUTTON);
  print_button_when_changed_state("lowerleft jb", LEFT_JOYSTICK_LOWER_BUTTON);
  print_button_when_changed_state("upperright jb", RIGHT_JOYSTICK_UPPER_BUTTON);
  print_button_when_changed_state("lowerright jb", RIGHT_JOYSTICK_LOWER_BUTTON);

  print_scale_reading_when_changed_state("upperleft sw", LEFT_SWITCH_UPPER);
  print_scale_reading_when_changed_state("lowerleft sw", LEFT_SWITCH_LOWER);
  print_scale_reading_when_changed_state("upperright sw", RIGHT_SWITCH_UPPER);
  print_scale_reading_when_changed_state("lowerright sw", RIGHT_SWITCH_LOWER);

  print_scale_reading_when_changed_state("upperleft jx", LEFT_JOYSTICK_UPPER_X);
  print_scale_reading_when_changed_state("lowerleft jx", LEFT_JOYSTICK_LOWER_X);
  print_scale_reading_when_changed_state("upperright jx", RIGHT_JOYSTICK_UPPER_X);
  print_scale_reading_when_changed_state("lowerright jx", RIGHT_JOYSTICK_LOWER_X);

  print_scale_reading_when_changed_state("upperleft jy", LEFT_JOYSTICK_UPPER_Y);
  print_scale_reading_when_changed_state("lowerleft jy", LEFT_JOYSTICK_LOWER_Y);
  print_scale_reading_when_changed_state("upperright jy", RIGHT_JOYSTICK_UPPER_Y);
  print_scale_reading_when_changed_state("lowerright jy", RIGHT_JOYSTICK_LOWER_Y);

  //print_pot_when_changed_reading("pot 1", POT_LEFT);
  print_pot_when_changed_reading("pot 1", POT_LEFT_CENTER);
  print_pot_when_changed_reading("pot 2", POT_CENTER);
  print_pot_when_changed_reading("pot 3", POT_RIGHT_CENTER);
  print_pot_when_changed_reading("pot 4", POT_RIGHT);
}

void print_button_when_changed_state(String input_name, int input_id) {
  
  if (bossy.hasChangedState(input_id)) {
    
    Serial.print(input_name);
    Serial.print(": ");
    
    bossy.savedState(input_id)==PUSHED ? 
      Serial.println("pressed") : Serial.println("neutral");
  }
}

void print_pot_when_changed_reading(String input_name, int input_id) {
  
  if (bossy.hasChangedReading(input_id)) {
    Serial.print(input_name);
    Serial.print(": ");
    Serial.print(bossy.savedReading(input_id));
    Serial.print(" ");
    Serial.print(bossy.savedReadingLowRes(input_id));
    Serial.println();

  }
}

void print_scale_reading_when_changed_state(String input_name, int input_id) {
  if (bossy.hasChangedState(input_id)) {
    Serial.print(input_name);
    Serial.print(": ");
    Serial.print(bossy.savedState(input_id));
    Serial.println(" ");
  }
}
