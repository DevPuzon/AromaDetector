import json
import serial

data = open('.\AromaTrainModel\AromaTrainModel\AromaTrainModel.json','r').read()
modelArray = json.loads(data)


annScorings = []
analyzeDatas =[]
def analyze():
    global analyzeDatas 
    for model in modelArray :
        sensorDatas = model['sensorDatas']
        imq135 = []
        imq3 = []
        imq5 = []
        imq138 = []
        imq2 = [] 
        sensorDataCount = 0  
        
        for sensorData in sensorDatas:
            if True :
                imq135.append(sensorData['mq135'])
                imq3.append(sensorData['mq3'])
                imq5.append(sensorData['mq5'])
                imq138.append(sensorData['mq138'])
                imq2.append(sensorData['mq2'])
                sensorDataCount = sensorDataCount + 1
                
        analyzeDatas.append({'aroma':model['aroma'],
                         'mq135min':min(imq135),'mq135max':max(imq135),
                         'mq3min':min(imq3),'mq3max':max(imq3),
                         'mq5min':min(imq5),'mq5max':max(imq5),
                         'mq138min':min(imq138),'mq138max':max(imq138),
                         'mq2min':min(imq2),'mq2max':max(imq2)})
        
    print("analyze")
    print(analyzeDatas)

def checkingData(valMq135, valMq3, valMq5, valMq138, valMq2): 
    global annScorings
    global analyzeDatas 
    for analyzeData in analyzeDatas : 
        imq135 = 0
        imq3 = 0
        imq5 = 0
        imq138 = 0
        imq2 = 0
        
#        if analyzeData['mq135min'] <= valMq135 and analyzeData['mq135max'] >= valMq135 :
#            imq135 = imq135 +0.1;
#            
#        if analyzeData['mq3min'] <= valMq3 and analyzeData['mq3max'] >= valMq3 :
#            imq3 =  imq3 +0.1;
#            
#        if analyzeData['mq5min'] <= valMq5 and analyzeData['mq5max'] >= valMq5 :
#            imq5 =  imq5+0.1;
#            
#        if analyzeData['mq138min'] <= valMq138 and analyzeData['mq138max'] >= valMq138 :
#            imq138 =  imq138+0.1;
#            
#        if analyzeData['mq2min'] <= valMq2 and analyzeData['mq2max'] >= valMq2 :
#            imq2 = imq2+0.1;
         
        percent4 = 0.2
        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent4) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent4) < valMq135:
            imq135 = imq135 - 0.2; 
            
        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent4) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent4) < valMq3:
            imq3 = imq3 - 0.2; 
        
        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent4) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent4) < valMq5:
            imq5 =imq5 - 0.2;  
        
        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent4) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent4) < valMq138:
            imq138 = imq138 -0.2; 
        
        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent4) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent4) < valMq2:
            imq2 = imq2 - 0.2;  
            
        percent3 = 0.5
        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent3) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent3) < valMq135:
            imq135 = imq135 - 0.5; 
            
        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent3) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent3) < valMq3:
            imq3 = imq3 - 0.5; 
        
        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent3) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent3) < valMq5:
            imq5 =imq5 - 0.5;  
        
        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent3) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent3) < valMq138:
            imq138 = imq138 -0.5; 
        
        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent3) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent3) < valMq2:
            imq2 = imq2 - 0.5;  
            
        percent2 = 0.8
        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent2) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent2) < valMq135:
            imq135 = imq135 - 0.8; 
            
        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent2) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent2) < valMq3:
            imq3 = imq3 - 0.8; 
        
        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent2) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent2) < valMq5:
            imq5 =imq5 - 0.8;  
        
        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent2) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent2) < valMq138:
            imq138 = imq138 - 0.8; 
        
        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent2) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent2) < valMq2:
            imq2 = imq2 - 0.8;  
            
        percent1 = 1
        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent1) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent1) < valMq135:
            imq135 = imq135 - percent1; 
            
        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent1) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent1) < valMq3:
            imq3 = imq3 - percent1; 
        
        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent1) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent1) < valMq5:
            imq5 =imq5 - percent1;  
        
        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent1) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent1) < valMq138:
            imq138 = imq138 - percent1; 
        
        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent1) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent1) < valMq2:
            imq2 = imq2 - percent1;  
            
        percent = 1.3
        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent) < valMq135:
            imq135 = imq135 - percent; 
            
        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent) < valMq3:
            imq3 = imq3 - percent; 
        
        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent) < valMq5:
            imq5 = imq5 - percent;  
        
        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent) < valMq138:
            imq138 = imq138 - percent; 
        
        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent) < valMq2:
            imq2 = imq2 - percent;  
            
#        percent5 = 2.5
#        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent5) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent5) < valMq135:
#            imq135 = imq135 - percent5; 
#            
#        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent5) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent5) < valMq3:
#            imq3 = imq3 - percent5; 
#        
#        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent5) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent5) < valMq5:
#            imq5 = imq5 - percent5;  
#        
#        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent5) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent5) < valMq138:
#            imq138 = imq138 - percent5; 
#        
#        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent5) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent5) < valMq2:
#            imq2 = imq2 - percent5;   
#        
#        percent4 = 2.8
#        if analyzeData['mq135min'] - (analyzeData['mq135min'] * percent4) > valMq135 or analyzeData['mq135max'] + (analyzeData['mq135max'] * percent4) < valMq135:
#            imq135 = imq135 - percent4; 
#            
#        if analyzeData['mq3min'] - (analyzeData['mq3min'] * percent4) > valMq3 or analyzeData['mq3max'] + (analyzeData['mq3max'] * percent4) < valMq3:
#            imq3 = imq3 - percent4; 
#        
#        if analyzeData['mq5min'] - (analyzeData['mq5min'] * percent4) > valMq5 or analyzeData['mq5max'] + (analyzeData['mq5max'] * percent4) < valMq5:
#            imq5 = imq5 - percent4;  
#        
#        if analyzeData['mq138min'] - (analyzeData['mq138min'] * percent4) > valMq138 or analyzeData['mq138max'] + (analyzeData['mq138max'] * percent4) < valMq138:
#            imq138 = imq138 - percent4; 
#        
#        if analyzeData['mq2min'] - (analyzeData['mq2min'] * percent4) > valMq2 or analyzeData['mq2max'] + (analyzeData['mq2max'] * percent4) < valMq2:
#            imq2 = imq2 - percent4;  
            
            
        annScorings.append({'aroma':analyzeData['aroma'],
                            'mq135':imq135,
                            'mq3':imq3,
                            'mq5':imq5,
                            'mq138':imq138,
                            'mq2':imq2})  
    
def getResult():
    modelScores = []
    global annScorings  
    for annScoring in annScorings:
        isSetScore = False
        modelCount = 0
        origScore = 0 
        for modelScore in modelScores:
            if modelScore['aroma'] == annScoring['aroma']:
                origScore = modelScore['score']
                
                origScore = annScoring['mq135'] + origScore
                origScore = annScoring['mq3'] + origScore
                origScore = annScoring['mq5'] + origScore
                origScore = annScoring['mq138'] + origScore
                origScore = annScoring['mq2'] + origScore
                modelScores[modelCount]['score'] = origScore
                isSetScore = True
            modelCount = modelCount + 1
            
        if len(modelScores) == None or not isSetScore:
            origScore = annScoring['mq135'] + origScore
            origScore = annScoring['mq3'] + origScore
            origScore = annScoring['mq5'] + origScore
            origScore = annScoring['mq138'] + origScore
            origScore = annScoring['mq2'] + origScore
            modelScores.append({ 'aroma':annScoring['aroma'],'score':origScore})
    
    print("modelScores")
    print(modelScores)
    sortedScores = getLowerNumber(modelScores)
    print("sortedScores")
    print(sortedScores)
    sortedScoreI = 0
    for sortedScore in sortedScores: 
        print(str(sortedScoreI+1)+"-----")
        print(sortedScores[sortedScoreI]) 
        sortedScoreI =sortedScoreI+1


def getLowerNumber(modelScores):
    repmodelScores = modelScores
    scores = []
    for modelScore in modelScores:
        scores.append(modelScore['score'])
    scores.sort(reverse = True) 
    
    ret = [] 
    for score in scores:
        for modelScore in repmodelScores:
            if modelScore['score'] == score:
                ret.append({'aroma':modelScore['aroma'],
                            'score':score})
                repmodelScores.remove(modelScore) 
    return ret 

 #In arduino, Serial.begin(baud_rate) 
 #CONNECTION ARDUINO TO RPI
serial_port = 'com11';
baud_rate = 9600;
ser = serial.Serial(serial_port, baud_rate)

analyze() 
validCount = 0
while validCount < 30: #TIME VALIDATION
    arduinodata = ser.readline();
    arduinodata = arduinodata.decode("utf-8")
    print("----------")
    print(arduinodata)
    datas = arduinodata.split(',')
    if len(datas) == 6 : 
        valMq135 = datas[0]
        valMq3 = datas[1]
        valMq5 =  datas[2]
        valMq138 = datas[3]
        valMq2 = datas[4]
#        if valMq135 < 110 and valMq3 < 110 and valMq3 < 110 and valMq138 < 110 and valMq2 < 110 : 
        if validCount > 20: #TIME WHERE THE PROCESS START 
            checkingData(int(valMq135), int(valMq3),
                         int(valMq5),int(valMq138), int(valMq2))
        validCount = validCount + 1
#        else :
#            validCount = 10000
#            print('----- SENSOR IS NOT STABLE PLEASE RESTART THE DEVICE ----- ')
getResult()





#datas = modelArray[0]['sensorDatas'] 
###jsonDatas = json.loads(datas) 
#for data in datas: 
#    checkingData(data['mq135'], data['mq3'], data['mq5'], data['mq138'], data['mq2'])

