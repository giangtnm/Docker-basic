Run normal Apriori by this command:

java -cp <path to normal-apriori.jar> MainTestApriori_saveToFile <path to input file> <path to output file> <support>

Run parallel Apriori by thi command:

spark-submit --class vn.edu.uit.ParallelApriori --master mesos://<ip of master>:7077 --conf  'spark.locality.wait=0' --deploy-mode cluster <path to paralle-apriori.jar> <path to input file> <path to output file> <support> <num of CPU>