using Microsoft.Office.Interop.Excel;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.IO.Ports;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Threading.Tasks;

namespace AromaTrainModel
{
    class Program
    {
        private static SerialPort _serialPort;
        private static String aromaTitle;
        private static bool isStart = false;
        private static int count = 0;
        private static List<AromaModel> aromaModels = new List<AromaModel>();
        private static string data;
        private static List<SensorData> sensorDatas = new List<SensorData>();
        static void Main(string[] args)
        {
            filePath = Path.GetFullPath(filePath);
            excelPath = Path.GetFullPath(excelPath);
            aromaModels = getExistingModel();
            initSerilPort();
            init();
        }

        private static void initSerilPort()
        {
            Console.WriteLine("Port Name :"); 
            _serialPort = new SerialPort();
            _serialPort.PortName = "com11"; // NAME of Prot example COM8
            _serialPort.Parity = Parity.None;
            _serialPort.StopBits = StopBits.One;
            _serialPort.DataBits = 8;
            _serialPort.Handshake = Handshake.None;
            _serialPort.RtsEnable = true;
            _serialPort.DtrEnable = true;    // Data-terminal-ready 
            _serialPort.Encoding = Encoding.Default;
            _serialPort.BaudRate = 9600;
            _serialPort.Open();
            _serialPort.DataReceived += new SerialDataReceivedEventHandler(SerialHandler);
        }
         private static bool iscalibrate= true;
        private static void SerialHandler(object sender, SerialDataReceivedEventArgs e)
        { 
            string incomingByte;
            incomingByte = _serialPort.ReadExisting();
            data += incomingByte; 
            Thread.Sleep(1000);
            Console.WriteLine(data);
            if (isStart)
            {
                if (iscalibrate)
                {
                    Console.WriteLine("Calebrating.........");
                    iscalibrate = false;
                }
                Debug.WriteLine(count);
                if (count > 30)
                {
                    String getdata = data.Replace(System.Environment.NewLine, "");
                    culculation(getdata);
                    Console.WriteLine(JsonConvert.SerializeObject(getdata));
                    isStart = false;
                    saveData();
                    //Console.WriteLine("Do you want to train again? y or n ");
                    //String again = Console.ReadLine();

                    //if (again.Equals("y"))
                    //{
                    //    init();
                    //}
                    //else
                    //{
                    //    //Environment.Exit(-1);
                    //    init();
                    //}

                    init();
                    iscalibrate = true;
                } 
                count++; 
            }
            else
            {
                data = "";
            }
        }

        private static void culculation(string getdata)
        {
            String[] getdatas = getdata.Split(')');
            for(var i = 0; i < getdatas.Length - 1;i++)
            {
                try
                {
                    String[] datas = getdatas[i].Split(','); 
                    Console.WriteLine("mq135 : " + datas[0]);
                    Console.WriteLine(" | mq3 : " + datas[1]);
                    Console.WriteLine(" | mq5 : " + datas[2]);
                    Console.WriteLine(" | mq138 : " + datas[3]);
                    Console.WriteLine(" | mq2 : " + datas[4]);
                    SensorData sensorData = new SensorData(int.Parse(datas[0]), int.Parse(datas[1]),
                       int.Parse(datas[2]),
                       int.Parse(datas[3]),
                       int.Parse(datas[4]));
                    sensorDatas.Add(sensorData);
                    Console.WriteLine("Json " + JsonConvert.SerializeObject(sensorData) + " || count : " + i.ToString());
                }
                catch(Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
        }

        private static void saveData()
        {
            int itemIndex =12;

            Application app = new Application();
            aromaModels.Add(new AromaModel(aromaTitle, sensorDatas));
            //aromaModels[itemIndex-1] = new AromaModel(aromaTitle, sensorDatas);

            Workbook workbook = app.Workbooks.Open(excelPath);
            Debug.WriteLine((aromaModels.Count - 1).ToString());
            Worksheet sheet = workbook.Worksheets[aromaModels.Count-1];
            //Worksheet sheet = workbook.Worksheets[itemIndex];
            sheet.Name = aromaTitle; 

            //A Title 
            sheet.Cells[1, 1] = "test";
            //B MQ135
            sheet.Cells[1, 2] = "mq135";
            //C MQ3
            sheet.Cells[1, 3] = "mq3";
            //D MQ5
            sheet.Cells[1, 4] = "mq5";
            //E MQ138
            sheet.Cells[1, 5] = "mq138";
            //F MQ2
            sheet.Cells[1, 6] = "mq2";

            for (var ii = 0; ii < sensorDatas.Count; ii++)
            {
                SensorData sensorData = sensorDatas[ii];
                //A Title 
                sheet.Cells[ii + 2, 1] = "test "+(ii+1).ToString();
                //B MQ135
                sheet.Cells[ii + 2,2] = sensorData.mq135;
                //C MQ3
                sheet.Cells[ii + 2,3] = sensorData.mq3;
                //D MQ5
                sheet.Cells[ii + 2,4] = sensorData.mq5;
                //E MQ138
                sheet.Cells[ii + 2,5] = sensorData.mq138;
                //F MQ2
                sheet.Cells[ii + 2 ,6] = sensorData.mq2;
            }

            workbook.Save();
            workbook.Close();

            String saveText = JsonConvert.SerializeObject(aromaModels);
            System.IO.File.WriteAllText(filePath, saveText);
            sensorDatas.Clear();
        }

        private static void init()
        {
            Console.WriteLine("Aroma type :");
            aromaTitle = Console.ReadLine();
            isStart = true;
            count = 0;
            Console.ReadKey();
        }

        //private static String filePath = "./AromaTrainModel.json";
        //private static String excelPath = "./AromaTrainExcel.xlsx"; 
        private static String filePath = @"D:\DriveD\Project\Github\..Net\AromaTrainModel\AromaTrainModel\AromaTrainModel\AromaTrainModel36aroma.json";
        private static String excelPath = @"D:\DriveD\Project\Github\..Net\AromaTrainModel\AromaTrainModel\AromaTrainModel\AromaTrainExcel36aroma.xlsx";
        
        private static List<AromaModel> getExistingModel()
        {
            List<AromaModel> aromaModels = new List<AromaModel>();
            string text = System.IO.File.ReadAllText(filePath);

            aromaModels = JsonConvert.DeserializeObject<List<AromaModel>>(text);
            if (String.IsNullOrEmpty(text))
            {
                Console.WriteLine("No Existing Data");
                return new List<AromaModel>();
            }
            Console.WriteLine(JsonConvert.SerializeObject(aromaModels));
            return aromaModels;
        }
    }
}
