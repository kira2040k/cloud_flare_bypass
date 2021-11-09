using System;
using System.Net;
using System.Net.Http;
using System.Threading;

namespace cloud_flare_bypass
{
    class Program
    {
        public static class Globals
        {
            public static String domain = "www.youtube.com";
        }
            static void Main(string[] args)
        {
            try
            {
                Globals.domain = args[0];
                Console.WriteLine("scan runing...");
            }
            catch (IndexOutOfRangeException) {
               
                    Console.WriteLine("add domain arg");
                    System.Environment.Exit(1);

                
            }
            var watch = new System.Diagnostics.Stopwatch();

            watch.Start();

            int part1 = 0;
            int part2 = 0;
            int part3 = 0;
            int part4 = 0;
            for (int i= 0; i < 4294967296; i++) {
            //for (int i = 0; i < 300000; i++)
            //{
                part1 = part1 + 1;
                if (part1 == 254)
                {
                    part2 = part2 + 1;
                    part1 = 0;
                }
                if (part2 == 254)
                {
                    part3 = part3 + 1;
                    part2 = 0;
                }
                if (part3 == 254)
                {
                    part4 = part4 + 1;
                    part3 = 0;
                }
                Thread newThread = new Thread(Program.DoWork);
                newThread.Start(part4 + "." + part3 + "." + part2 + "." + part1);
                //newThread.Start("142.250.72.100");
                
                if (i % 100000 == 0) {
                    Console.WriteLine("ip was scanned: "+i);
                }
               
            }
            Console.WriteLine("Finish. " + Globals.domain);

        }

        
        /*
        public static async void DoWork(object data)
        {
            HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.Add("Host",Globals.domain);
            try
            {
                HttpResponseMessage response = await client.GetAsync("https://" + data);
                if (response.StatusCode.ToString() == "OK" || response.StatusCode.ToString() == "NotFound")
                {
                    Console.WriteLine("found " + Globals.domain + " ip -> " + data);
                }
            }
            catch (HttpRequestException) { }
        }
        */
       
        public static void DoWork(object data)
        {
            try
            {
                var webRequest = System.Net.WebRequest.Create("https://" + data);
                webRequest.Proxy = null;
                webRequest.Method = "GET";
                webRequest.Timeout = 5000;
                webRequest.Headers.Add("Host", Globals.domain);
                HttpWebResponse response = (HttpWebResponse)webRequest.GetResponse();
                if (response.StatusCode != HttpStatusCode.BadGateway)
                {
                    Console.WriteLine("found " + data);
                }
                response.Close();

            }
            catch (WebException e) { }
            catch (OperationCanceledException) { }
            return;
        }
        
    }
}
