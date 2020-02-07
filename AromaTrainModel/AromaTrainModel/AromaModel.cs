using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AromaTrainModel
{
    public class AromaModel
    {
        public String aroma { get; set; }
        public List<SensorData> sensorDatas{get;set; }

        public AromaModel(String aroma,List<SensorData> sensorDatas)
        {
            this.aroma = aroma;
            this.sensorDatas = sensorDatas;
        }

    }
    public class SensorData
    {
        public String mq135 { get; set; }
        public String mq3 { get; set; }
        public String mq5 { get; set; }
        public String mq138 { get; set; }
        public String mq2 { get; set; }
        public SensorData() { }
        public SensorData(String mq135, String mq3, String mq5, String mq138, String mq2)
        {
            this.mq135 = mq135;
            this.mq3 = mq3;
            this.mq5 = mq5;
            this.mq138 = mq138;
            this.mq2 = mq2;
        }
    }
}
