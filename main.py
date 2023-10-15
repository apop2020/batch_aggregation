from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import *
from pyspark.sql.functions import  col, window, concat,lit,avg
from pyspark.sql import SparkSession
import os

window_time = os.getenv("window_time", default="1 day")

if __name__=="__main__":
    spark =  SparkSession.builder\
        .appName("batchaggregationcodingchallange")\
        .config("dfs.client.read.shortcircuit.skip.checksum", "true")\
        .getOrCreate()
    
    print(f"starting summary window_time={window_time}")
    df = spark.read.parquet('/data/in/*.parquet')
    df = df.withColumn("TimeBucket",window("Timestamp",window_time))
    df = df.withColumn("TimeBucket",concat(col("TimeBucket").start, lit(" to "), col("TimeBucket").end))
    final_df :DataFrame = df.groupBy("Metric","TimeBucket")\
        .agg(avg("Value").alias("Value_avg"))
    final_df.show(1)
    final_df = final_df.coalesce(1)

    # spark config options to avoid generating crc and metadata files when outputting
    spark.conf.set("spark.sql.parquet.mergeSchema", "false")
    spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")
    spark.conf.set("spark.sql.sources.commitProtocolClass", "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol")
    
    final_df.write.mode("append").csv("/data/out/summary.csv")
    final_df.write.mode("append").parquet("/data/out/summary.parquet")