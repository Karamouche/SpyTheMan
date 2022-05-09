//#define servo1 
//#define servo2
//#define servo3
#define borneIN1 2
#define borneIN2 3
#define borneIN3 4
#define borneIN4 5

int poservo1 = 80;
//int poservo2 = 40;
//int poservo3 = 180;

#include <Servo.h>
Servo Servo1;//Servo  Horizontal
//Servo Servo2; //Servo Vertical
//Servo Servo3; //Servo chargeur

void setup() {
	Serial.begin(9600);
	Servo1.attach(servo1); Servo1.write(poservo1);
	//Servo2.attach(servo2); Servo2.write(poservo2);
	//Servo3.attach(servo3); Servo3.write(poservo3);
	delay(10);
//	pinMode(borneIN1, OUTPUT); pinMode(borneIN2, OUTPUT); //Moteur 1
//	pinMode(borneIN3, OUTPUT); pinMode(borneIN4, OUTPUT); //Moteur 2
//	pinMode(borneENA, OUTPUT); pinMode(borneENB, OUTPUT);
	}
void loop(){
	if (Serial.available()){
		byte message  = Serial.read();
		Serial.print("Syst send:");
		Serial.println(message, DEC);
		}
	if (message ==  0){		//Le  programme a déjà aligné le système et la cible et ordonne de tirer
		digitalWrite(borneIN1, HIGH);
		digitalWrite(borneIN2, LOW);
		digitalWrite(borneIN3, LOW);
		digitalWrite(borneIN4, HIGH);
		analogWrite(borneENA, 250);
		analogWrite(borneENB, 250); //On allume les moteurs
		delay(10) //On attend que les moteurs soit à  la bonne vitesse
		servo3.write(280); //On envoie la munition
		}
	else if (message == 1){		 // Le programme ordonne de monter
		poservo1++;
		servo1.write(poservo1);
		delay(10);
		}
	else if (message == 2){			 // Le programme ordonne de descendre
		poservo1--;
		servo1.write(poservo1);
		delay(10);
	else if (message == 3){			 // Le programme ordonne d'orienter vers la droite
		poservo2++;
		servo2.write(poservo2);
		delay(10);
	else if (message == 4){ // Le programme ordonne d'orienter vers la gauche
		poservo2--;
		servo2.write(poservo2);
		delay(10);
	
	}
}

