import streamlit as st
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from groq import Groq

# Fungsi untuk menentukan selector
def class_filter(media_name):
    if media_name == "kompas":
        return "hlTitle", "h1"
    elif media_name == "detik":
        return "media__title", "h2"
    elif media_name == "tribun":
        return "hltitle", "div"


# Fungsi scraping berita
def scrape_news(name, url):
    class_name, element_selector = class_filter(name)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headline_element = soup.find(element_selector, class_=class_name)
    return headline_element.text.strip() if headline_element else "Tidak ditemukan."


# Halaman Utama
def main_page():
    st.title("Aplikasi Berita🎉")
    st.write("Selamat datang!")

    st.subheader("Berita Tebaru")
    kompas = scrape_news("kompas", "https://www.kompas.com/")
    detik = scrape_news("detik", "https://news.detik.com/")
    tribun = scrape_news("tribun", "https://www.tribunnews.com/")

    st.write(f"**Kompas**: {kompas}")
    st.write(f"**Detik**: {detik}")
    st.write(f"**Tribun**: {tribun}")


# Halaman Cek Usia
def usia_page():
    st.title("Cek Usia dan Fakta Teknologi")
    tahun_lahir = st.number_input("Masukkan Tahun Lahir Anda", min_value=1900, max_value=datetime.now().year, step=1)

    if st.button("Cek Usia"):
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        st.write(f"**Usia Anda adalah**: {usia} tahun")


# Halaman Cafe
def cafe_page():
    st.title("Halaman baru")
    st.write("Halaman ini masih dalam pengembangan.")
    
# Menampilkan halaman sesuai menu
menu = st.sidebar.selectbox("Pilih Halaman", ["Halaman Berita", "Cek Usia", "baru"])

if menu == "Halaman Berita":
    main_page()
elif menu == "Cek Usia":
    usia_page()
elif menu == "baru":
    cafe_page()
