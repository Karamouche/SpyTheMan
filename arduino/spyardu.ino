#define servo1 10
#define servo2 11
#define servo3 12
#define borneIN1 2
#define borneIN2 3
#define borneIN3 4
#define borneIN4 5


int poservo1 = 80;
int poservo2 = 40;
int poservo3 = 180;

#include <Servo.h>
Servo Serv1;//Servo  Horizontal
Servo Serv2; //Servo Vertical
Servo Serv3; //Servo chargeur

void setup() {
	Serial.begin(9600);
	Serv1.attach(servo1); Serv1.write(poservo1);
	Serv2.attach(servo2); Serv2.write(poservo2);
	Serv3.attach(servo3); Serv3.write(poservo3);
	delay(10);
	pinMode(borneIN1, OUTPUT); pinMode(borneIN2, OUTPUT); //Moteur 1
	pinMode(borneIN3, OUTPUT); pinMode(borneIN4, OUTPUT); //Moteur 2
	}
void loop(){
	if (Serial.available(){
		byte nr = Serial.read();
		Serial.print("Syst send:");
		Serial.println(nr, DEC);
	switch (nr){
		case shoot://Le  programme a déjà aligné le système et la cible et ordonne de tirer
			digitalWrite(borneIN1, HIGH);
			digitalWrite(borneIN2, LOW);
			digitalWrite(borneIN3, LOW);
			digitalWrite(borneIN4, HIGH);
			delay(10) //On attend que les moteurs soit à  la bonne vitesse
			servo3.write(280); //On envoie la munition
			break;
		case up: // Le programme ordonne de monter
			poservo1++;
			servo1.write(poservo1);
			delay(10);
			break;
		case down: // Le programme ordonne de descendre
			poservo1--;
			servo1.write(poservo1);
			delay(10);
			break;
		case right: // Le programme ordonne d'orienter vers la droite
			poservo2++;
			servo2.write(poservo2);
			delay(10);
			break;
		case left: // Le programme ordonne d'orienter vers la gauche
			poservo2--;
			servo2.write(poservo2);
			delay(10);
			break;
		default: // cas par défaut, si le programme principal n'envoie rien on arrive ici
			break;
		}
