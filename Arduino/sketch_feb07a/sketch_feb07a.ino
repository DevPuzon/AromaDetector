 
int mq135 = A0;
int mq3 = A1;
int mq5 = A2;
int mq138 = A3;
int mq2 = A4;     
#define         RL_VALUE                     (10)    
#define         RO_CLEAN_AIR_FACTOR          (9.21)  
#define         CALIBARAION_SAMPLE_TIMES     (50)    
#define         CALIBRATION_SAMPLE_INTERVAL  (500)   
#define         READ_SAMPLE_INTERVAL         (50)    
#define         READ_SAMPLE_TIMES            (5)   
#define         GAS_H2                      (0) 
float           H2Curve[3]  =  {2.3, 0.93,-1.44};    
float           Romq135           =  10;         
float           Romq3           =  10;              
float           Romq5          =  10;              
float           Romq138           =  10;           
float           Romq2           =  10;                     

String mq3_ppm;//ppm 
void setup() {  
  Serial.begin(9600);  
  initmq3(); 
}

void initmq3(){               
//  Romq135 = MQCalibration(mq135);                
//  Romq3 = MQCalibration(mq3);                  
//  Romq5 = MQCalibration(mq5);                  
//  Romq138 = MQCalibration(mq138);                  
//  Romq2 = MQCalibration(mq2); 
   
  Romq135 = 2.23;                
  Romq3 = 1.80;                  
  Romq5 = 2.39;                  
  Romq138 =2.95;                  
  Romq2 = 0.35 ; 
}
 
void loop() {    
  
  String imq135 = getmq(mq135,Romq135);
  String imq3 =  getmq(mq3,Romq3);
  String imq5 =  getmq(mq5,Romq5);
  String imq138 = getmq(mq138,Romq5);
  String imq2 =  getmq(mq2,Romq2);
  
  String jsonData = imq135+","+imq3+","+imq5+","+imq138+","+imq2+",)";
  Serial.println(jsonData);  
}
 
String getmq(int pin,float ro){
   String ret =String( MQGetGasPercentage(MQRead(pin)/ro,GAS_H2));//ppm
   mq3_ppm = String(ret);//ppm  
   return ret;
}




////////////////////////////////////////////////////////////////////////////////////////////////-------------------------------
float MQResistanceCalculation(int raw_adc) {
  return ( ((float)RL_VALUE*(1023-raw_adc)/raw_adc));
} 

float MQCalibration(int mq_pin) {
  int i;
  float val=0; 
  for (i=0;i<CALIBARAION_SAMPLE_TIMES;i++) {           
    val += MQResistanceCalculation(analogRead(mq_pin));
    delay(CALIBRATION_SAMPLE_INTERVAL);
  }
  val = val/CALIBARAION_SAMPLE_TIMES;                  
  val = val/RO_CLEAN_AIR_FACTOR;                      
  return val; 
}

float MQRead(int mq_pin) {
  int i;
  float rs=0;
 
  for (i=0;i<READ_SAMPLE_TIMES;i++) {
    rs += MQResistanceCalculation(analogRead(mq_pin));
    delay(READ_SAMPLE_INTERVAL);
  }
 
  rs = rs/READ_SAMPLE_TIMES;
 
  return rs;  
}

int MQGetGasPercentage(float rs_ro_ratio, int gas_id) {
  if ( gas_id == GAS_H2) {
     return MQGetPercentage(rs_ro_ratio,H2Curve);
  }  
  return 0;
} 

int  MQGetPercentage(float rs_ro_ratio, float *pcurve) {
  return (pow(10,( ((log(rs_ro_ratio)-pcurve[1])/pcurve[2]) + pcurve[0])));
}




//
//int mq135 = A0;
//int mq3 = A1;
//int mq5 = A2;
//int mq138 = A3;
//int mq2 = A4;
//
//
//void setup() {
//  Serial.begin(9600);           //  setup serial
//}
//
//void loop() {
//  String imq135 = String(analogRead(mq135));
//  String imq3 = String(analogRead(mq3)); 
//  String imq5 = String(analogRead(mq5));
//  String imq138 = String(analogRead(mq138));
//  String imq2 = String(analogRead(mq2)); 
//
//  String jsonData = imq135+","+imq3+","+imq5+","+imq138+","+imq2+",)";
//  Serial.println(jsonData);  
//  delay(800);
//}
// 
