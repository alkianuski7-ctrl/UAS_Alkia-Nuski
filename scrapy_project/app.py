import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Books Scraping",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Hasil Web Scraping Buku")
st.write("Data diambil menggunakan Scrapy dari website Books to Scrape.")

# Membaca file CSV
df = pd.read_csv("books.csv")

# Menampilkan jumlah data
st.metric("Jumlah Buku", len(df))

# Menampilkan tabel
st.subheader("Data Buku")
st.dataframe(df, use_container_width=True)

# Filter harga
st.subheader("Pencarian Judul Buku")

keyword = st.text_input("Masukkan Judul Buku")

if keyword:
    hasil = df[df["Title"].str.contains(keyword, case=False, na=False)]
    st.dataframe(hasil, use_container_width=True)