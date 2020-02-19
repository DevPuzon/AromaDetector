
int mq135 = A0;
int mq3 = A1;
int mq5 = A2;
int mq138 = A3;
int mq2 = A4;


void setup() {
  Serial.begin(9600);           //  setup serial
}

void loop() {
  String imq135 = String(analogRead(mq135));
  String imq3 = String(analogRead(mq3)); 
  String imq5 = String(analogRead(mq5));
  String imq138 = String(analogRead(mq138));
  String imq2 = String(analogRead(mq2)); 

  String jsonData = imq135+","+imq3+","+imq5+","+imq138+","+imq2+",)";
  Serial.println(jsonData);  
  delay(800);
}
