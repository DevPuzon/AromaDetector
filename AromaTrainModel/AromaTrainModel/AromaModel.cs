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
        public int mq135 { get; set; }
        public int mq3 { get; set; }
        public int mq5 { get; set; }
        public int mq138 { get; set; }
        public int mq2 { get; set; }
        public SensorData() { }
        public SensorData(int mq135, int mq3, int mq5, int mq138, int mq2)
        {
            this.mq135 = mq135;
            this.mq3 = mq3;
            this.mq5 = mq5;
            this.mq138 = mq138;
            this.mq2 = mq2;
        }
    }
}
