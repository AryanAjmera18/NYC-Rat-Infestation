from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum as _sum, when, col

def spark_session():
    return SparkSession.builder.appName("RodentPatternAnalysis").enableHiveSupport().getOrCreate()

def temporal_trends(table="rodent_inspections"):
    df = spark_session().table(table)
    return (df.groupBy("year","month")
              .agg(
                count("*").alias("total_inspections"),
                _sum(when(col("RESULT").contains("Rat"),1).otherwise(0)).alias("rat_signs")
              ).orderBy("year","month"))

def borough_hotspots(table="rodent_inspections"):
    df = spark_session().table(table)
    return (df.groupBy("BOROUGH")
              .agg(
                count("*").alias("inspections"),
                _sum(when(col("RESULT").contains("Rat"),1).otherwise(0)).alias("rat_signs")
              ).orderBy(col("rat_signs").desc()))