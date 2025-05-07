# NYC Rodent Inspection Analysis Project

This repository contains an end-to-end pipeline to process, analyze, and visualize the NYC Rodent Inspection dataset.

## Structure
- `data/raw/`: source CSV & GeoJSON files
- `data/processed/`: cleaned Parquet
- `notebooks/`: Jupyter notebooks
- `src/etl/`: PySpark ETL script
- `src/analysis/`: Pattern analysis module
- `src/app/`: Streamlit dashboard
- `dashboards/`: Tableau workbook (.twbx)

## Setup & Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. ETL:
    python src/etl/process_rodent_data.py \
    --input data/raw/rodent_inspections.csv \
    --output data/processed/rodent_inspections.parquet

3. Notebooks:
    jupyter notebooks/

4. Dashboard:
    streamlit run src/app/streamlit_app.py



## ✅ What’s Done

- **Data Ingestion**  
  - Reads CSV from `data/raw/rodent_inspections.csv` with an explicit `StructType` schema.
- **Date Parsing**  
  - Converts the `INSPECTION_DATE` and `APPROVED_DATE` strings into Spark `TimestampType` columns.
- **Data Cleaning**  
  - Filters out records with missing timestamps or zero latitude/longitude.
  - Deduplicates on `JOB_TICKET_OR_WORK_ORDER_ID` + timestamp.
- **Partitioning & Write**  
  - Adds `year` and `month` columns.
  - Writes cleaned data out as partitioned Parquet by `year` & `BOROUGH`.
- **Windows Compatibility**  
  - Sets `HADOOP_HOME` → points to your local `winutils.exe`.
  - Disables native permissions checks:
    ```python
    .config("spark.hadoop.fs.permissions","false")
    .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version","1")
    ```

## 🚧 What Needs to Be Done

- **Disk/Memory Tuning**  
  - Adjust `spark.local.dir` or increase available disk for spill files.
  - Tweak executor memory / partition sizes.
- **Schema Validation**  
  - Auto-detect schema mismatches or evolving CSV formats.
- **Error Handling & Logging**  
  - Add `try/except` blocks and structured logs.
- **Packaging & Deployment**  
  - Containerize in Docker, publish to Airflow or other scheduler.
- **Unit & Integration Tests**  
  - PyTest or Spark-testing-base for critical transformations.

## 🛠️ Prerequisites

1. **Java 8+**  
2. **Python 3.7+**  
3. **Apache Spark 3.x** (pyspark)  
4. **Hadoop WinUtils** (for Windows)  
   - Download matching version, unzip to e.g. `D:\hadoop\bin\winutils.exe`  
   - Grant admin rights so `winutils.exe` can create native directories.

## 🚀 How To Run

1. **Set environment variables** (in your shell or at top of script):
   ```bash
   export HADOOP_HOME="D:\hadoop"
   export PATH="$HADOOP_HOME\bin:$PATH"


## Install Python dependencies:
pip install pyspark

## Run the ETL script:
python src/etl/process_rodent_data.py \
  --input  data/raw/rodent_inspections.csv \
  --output data/processed/rodent_inspections.parquet
### ----------