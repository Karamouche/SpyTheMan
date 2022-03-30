#define servo1 2
//#define servo2 3
//#define servo3 12

int poservo1 = 80;
//int poservo2 = 40;
//int poservo3 = 180;

#include <Servo.h>
Servo monServo1;
//Servo monServo2;
//Servo monServo3;

void setup() {
	Serial.begin(9600);
	monServo1.attach(servo1); monServo1.write(poservo1);
	//monServo2.attach(servo2); monServo2.write(poservo2);
	//monServo3.attach(servo3); monServo3.write(poservo3);
	delay(10);
	}
void loop(){
	if (Serial.available(){
		byte nr = Serial.read();
		Serial.print("The following char was received:");
		Serial.println(nr, DEC);
	switch (nr){
		case 1:
			digitalWrite(borneIN1, HIGH); digitalWrite(borneIN2, LOW);
			digitalWrite(borneIN3, LOW); digitalWrite(borneIN4, HIGH);
			analogWrite(borneENA, 250); analogWrite(borneENB, 250);
			monservo3.write(280);
			break;
		case up:
			poservo1++;
			monservo1.write(poservo1);
			delay(10);
			break;
		case down:
			poservo1--;
			monservo1.write(poservo1);
			delay(10);
			break;
		case right:
			poservo2++;
			monservo2.write(poservo2);
			delay(10);
			break;
		case left:
			poservo2--;
			monservo2.write(poservo2);
			delay(10);
			break;
		default:
			break;
		}

