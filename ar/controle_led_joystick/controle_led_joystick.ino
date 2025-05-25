String comando = "";

const int ledCima = 2;
const int ledBaixo = 3;
const int ledEsquerda = 4;
const int ledDireita = 5;

int buzzer = 8;

void setup() {
  Serial.begin(9600);
  pinMode(ledCima, OUTPUT);
  pinMode(ledBaixo, OUTPUT);
  pinMode(ledEsquerda, OUTPUT);
  pinMode(ledDireita, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "START") {
      tone(buzzer, 1600);
      delay(200);
      noTone(buzzer);
      tone(buzzer, 2200);
      delay(250);
      noTone(buzzer);
    }

    // Desliga todos antes de acender o próximo
    digitalWrite(ledCima, LOW);
    digitalWrite(ledBaixo, LOW);
    digitalWrite(ledEsquerda, LOW);
    digitalWrite(ledDireita, LOW);

    if (comando == "CIMA") {
      digitalWrite(ledCima, HIGH);
    } else if (comando == "BAIXO") {
      digitalWrite(ledBaixo, HIGH);
    } else if (comando == "ESQUERDA") {
      digitalWrite(ledEsquerda, HIGH);
    } else if (comando == "DIREITA") {
      digitalWrite(ledDireita, HIGH);
    } else if (comando == "ZERO") {
      digitalWrite(ledCima, LOW);
      digitalWrite(ledBaixo, LOW);
      digitalWrite(ledEsquerda, LOW);
      digitalWrite(ledDireita, LOW);
    }

    if (comando == "END") {
      tone(buzzer, 900);
      delay(160);
      noTone(buzzer);
      tone(buzzer, 300);
      delay(320);
      noTone(buzzer);
    }
  }
}