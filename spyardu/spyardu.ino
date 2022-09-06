#include <Servo.h>
#define servot 10
#define servoh 11
#define servov 12
#define borneIN1 2
#define borneIN2 3
#define borneIN3 4
#define borneIN4 5
#define dep 2


int poservoT = 180;
int poservoH = 90;
int poservoV = 90;


Servo ServH;//Servo  Horizontal
Servo ServV; //Servo Vertical
Servo ServT; //Servo chargeur

void setup() {
	Serial.begin(9600);
	ServH.attach(servoh); ServH.write(poservoH);
	ServV.attach(servov); ServV.write(poservoV);
	ServT.attach(servot); ServT.write(poservoT);
	delay(10);
	pinMode(borneIN1, OUTPUT); pinMode(borneIN2, OUTPUT); //Moteur 1
	pinMode(borneIN3, OUTPUT); pinMode(borneIN4, OUTPUT); //Moteur 2

	}
void loop(){
	while (Serial.available()){
		byte nr = Serial.read();
		Serial.print("Syst send:");
		Serial.println(nr);
	switch (nr){
		case 49://Le  programme a déjà aligné le système et la cible et ordonne de tirer
			digitalWrite(borneIN1, LOW);
			digitalWrite(borneIN2, HIGH);
			digitalWrite(borneIN3, LOW);
			digitalWrite(borneIN4, HIGH);
			delay(2000); //On attend que les moteurs soit à  la bonne vitesse
			ServT.write(0); //On envoie la munition 180 = 
      delay(1000);
      ServT.write(180);
      delay(600);
      poservoV = 90;
      poservoH = 90;
      delay(50);
      ServV.write(poservoV);
      ServH.write(poservoH);
      digitalWrite(borneIN1, LOW);
      digitalWrite(borneIN2, LOW);
      digitalWrite(borneIN3, LOW);
      digitalWrite(borneIN4, LOW);  
			break;
		case 50: // Le programme ordonne de monter
      if(poservoV <= 180-dep){
			poservoV = poservoV+dep;
      delay(50);
      ServV.write(poservoV);
      }
			break;
		case 51: // Le programme ordonne de descendre
      if(poservoV >= dep){
      poservoV = poservoV-dep;
			delay(50);
     ServV.write(poservoV);
      }
			break;
		case 52: // Le programme ordonne d'orienter vers la droite
      if(poservoH <= 180-dep){
			poservoH = poservoH+dep;
      delay(50);
      ServH.write(poservoH);
      }
			break;
      
		case 53: // Le programme ordonne d'orienter vers la gauche
      if(poservoH >= dep){
      poservoH = poservoH-dep;
      delay(50);
      ServH.write(poservoH);
      }
			break;
		default: // cas par défaut, si le programme principal n'envoie rien on arrive ici
			break;
		}
	}
}
