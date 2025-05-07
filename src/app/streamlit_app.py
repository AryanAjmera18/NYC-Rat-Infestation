import streamlit as st
from pyspark.sql import SparkSession
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

@st.cache_data
def load_data(path):
    spark = SparkSession.builder.appName("RodentDashboard").getOrCreate()
    df = (
        spark.read
        .option("basePath", path)
        .parquet(f"{path}/*/*")  # Ensure all partitions are read
        .select("LATITUDE", "LONGITUDE", "year", "BOROUGH", "RESULT", "month")
        .filter("LATITUDE IS NOT NULL AND LONGITUDE IS NOT NULL")
    )
    df_pd = df.toPandas()
    spark.stop()
    return df_pd

st.title("NYC Rodent Inspection Dashboard")

# Load full data
df = load_data("data/processed/rodent_inspections.parquet")
# Filter years in range 2009–2025
df = df[(df["year"] >= 2009) & (df["year"] <= 2025)]

# Populate filters from unfiltered data
available_years = sorted(df["year"].dropna().unique())
available_boros = sorted(df["BOROUGH"].dropna().unique())
available_results = sorted(df["RESULT"].dropna().unique())

# Sidebar filters
year = st.sidebar.selectbox("Year", available_years)
boros = st.sidebar.multiselect("Borough", available_boros, default=available_boros)
res = st.sidebar.multiselect("Result", available_results, default=available_results)

# Filter the data
data = df[
    (df["year"] == year)
    & df["BOROUGH"].isin(boros)
    & df["RESULT"].isin(res)
]

# Handle no data case
if data.empty:
    st.warning("⚠️ No records found for the selected filters.")
    st.stop()

# Metrics
st.metric("Inspections", f"{len(data):,}")

# Heatmap
m = folium.Map([40.7128, -74.0060], zoom_start=11)
HeatMap(data[["LATITUDE", "LONGITUDE"]].dropna().values.tolist(), radius=7).add_to(m)
st.subheader("Hotspots")
st_folium(m, width=700)

# Monthly bar chart
st.subheader("Monthly Inspections")
monthly = data["month"].value_counts().sort_index()
st.bar_chart(monthly)
