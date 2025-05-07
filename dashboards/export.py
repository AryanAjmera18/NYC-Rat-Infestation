from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ExportSubsetParquet")
    .getOrCreate()
)

# Load with partition discovery
df = spark.read.option("basePath", "data/processed").parquet("data/processed/rodent_inspections.parquet")

# Make sure Spark discovers partitioned columns
df.printSchema()

# Filter to years 2009–2025
df_filtered = df.filter((df["year"] >= 2009) & (df["year"] <= 2025))

# Optional: remove rows with null boroughs
df_filtered = df_filtered.filter(df_filtered["BOROUGH"].isNotNull())

# Save filtered version to a new path for Tableau
df_filtered.write.mode("overwrite").parquet("data/processed/rodent_subset.parquet")

spark.stop()
print("✅ Subset saved to data/processed/rodent_subset.parquet")
