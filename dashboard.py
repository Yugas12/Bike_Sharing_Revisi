import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
# Menggunakan path relatif
file_path = os.path.join(os.path.dirname(__file__), "data_terbaru.csv")
df = pd.read_csv(file_path)

# Konversi tanggal ke format datetime
df["dteday"] = pd.to_datetime(df["dteday"])

# Sidebar filter
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [df["dteday"].min(), df["dteday"].max()])
if isinstance(date_range, list) and len(date_range) == 2:
    df_filtered = df[(df["dteday"] >= pd.Timestamp(date_range[0])) & (df["dteday"] <= pd.Timestamp(date_range[1]))]
else:
    df_filtered = df

# Dashboard Title
st.title("Dashboard Peminjaman Sepeda")

# Grafik 1: Tren Jumlah Peminjaman Sepeda Sepanjang Tahun
st.subheader("Tren Jumlah Peminjaman Sepeda")
plt.figure(figsize=(12, 5))
sns.lineplot(x=df_filtered["dteday"], y=df_filtered["cnt_y"], marker='o', color='b')
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Peminjaman Sepeda")
plt.xticks(rotation=45)
st.pyplot(plt)

# Grafik 2: Hubungan Suhu dan Peminjaman Sepeda 
st.subheader("Hubungan Suhu dan Peminjaman Sepeda")
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df_filtered["temp_y"], y=df_filtered["cnt_y"], marker='o', color='b')
plt.xlabel("Suhu (normalized)")
plt.ylabel("Jumlah Peminjaman Sepeda")
st.pyplot(plt)


st.write("Dashboard ini memungkinkan eksplorasi tren peminjaman sepeda berdasarkan tanggal serta melihat korelasi antara suhu dan jumlah peminjaman.")
