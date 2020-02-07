using Microsoft.Office.Interop.Excel;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Ports;
using System.Linq;
using System.Text;
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
            _serialPort.PortName = Console.ReadLine(); // NAME of Prot example COM8
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

        private static void SerialHandler(object sender, SerialDataReceivedEventArgs e)
        {
            if (isStart)
            {
                string incomingByte;
                incomingByte = _serialPort.ReadExisting();
                data += incomingByte;

                String[] datas = data.Split(',');
                Console.WriteLine(datas[0]);
                Console.WriteLine(datas[1]);
                Console.WriteLine(datas[2]);
                Console.WriteLine(datas[3]);
                Console.WriteLine(datas[4]);
                SensorData sensorData =
                    new SensorData(datas[0], datas[1],
                    datas[2],
                    datas[3],
                    datas[4]);
                Console.WriteLine(data);
                Console.WriteLine(JsonConvert.SerializeObject(sensorData)); 
                if (count < 100)
                {
                    sensorDatas.Add(sensorData);
                }
                else
                {
                    isStart = false;
                    saveData();
                    Console.WriteLine("Do you want to train again? y or n ");
                    String again = Console.ReadLine();
                    if (again == "y")
                    {
                        init();
                    }
                    else
                    {
                        Environment.Exit(-1);
                    }
                }
                count++;
            }
        }

        private static void saveData()
        {
            Application app = new Application();
            aromaModels.Add(new AromaModel(aromaTitle, sensorDatas));

            String saveText = JsonConvert.SerializeObject(aromaModels);
            System.IO.File.WriteAllText(filePath, saveText);

            Workbook workbook = app.Workbooks.Open(excelPath);
            Worksheet sheet = workbook.Worksheets[aromaModels.Count];
            sheet.Name = aromaTitle;
             

            //A Title 
            sheet.Cells[1, 1] = "Aroma";
            //B MQ135
            sheet.Cells[1, 2] = "MQ135";
            //C MQ3
            sheet.Cells[1, 3] = "MQ3";
            //D MQ5
            sheet.Cells[1, 4] = "MQ5";
            //E MQ138
            sheet.Cells[1, 5] = "MQ138";
            //F MQ2
            sheet.Cells[1, 6] = "MQ2";

            for (var ii = 0; ii < sensorDatas.Count; ii++)
            {
                SensorData sensorData = sensorDatas[ii];
                //A Title 
                sheet.Cells[ii + 2, 1] = aromaTitle;
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
            aromaModels.Clear();
        }

        private static void init()
        {
            Console.WriteLine("Aroma type :");
            aromaTitle = Console.ReadLine();
            isStart = true;
            count = 0;
            Console.ReadLine();
        }

        //private static String filePath = "./AromaTrainModel.json";
        //private static String excelPath = "./AromaTrainExcel.xlsx"; 
        private static String filePath = @"D:\DriveD\Project\Github\..Net\AromaTrainModel\AromaTrainModel\AromaTrainModel/AromaTrainModel.json";
        private static String excelPath = @"D:\DriveD\Project\Github\..Net\AromaTrainModel\AromaTrainModel\AromaTrainModel/AromaTrainExcel.xlsx";
        
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
