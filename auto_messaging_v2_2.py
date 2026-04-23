# Import library yang diperlukan
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse
import random
import pandas as pd
from tqdm import tqdm

# Baca nomor dari file CSV dan tambahkan kode negara 62
df = pd.read_csv("nomor.csv")

nomor_list = []
print("Mengonversi nomor dari CSV...")
for n in tqdm(df['nomor'].astype(str), desc="Memproses nomor"):
    nomor_list.append("62" + n.lstrip("0"))

nomor_pertama = nomor_list[0]

# Pesan yang akan dikirim
pesan = """
tes
"""

encoded_pesan = urllib.parse.quote(pesan)

berhasil_dikirim = []
gagal_dikirim = []

# Konfigurasi WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

input("Silakan scan QR code dan tekan ENTER jika sudah login...")

# Fungsi menutup popup Fresh Look
def tutup_popup_fresh_look():
    try:
        tombol_popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()[contains(., "Continue") or contains(., "Lanjut")]]'))
        )
        tombol_popup.click()
        print("Popup 'Fresh Look' berhasil ditutup")
        time.sleep(2)
    except Exception:
        print("ℹ Tidak ada popup Fresh Look yang muncul atau gagal ditutup")

# Fungsi membuat pesan rekap
def buat_pesan_rekap():
    rekap_pesan = f"REKAP PENGIRIMAN\n\nBerhasil: {len(berhasil_dikirim)} nomor\n"
    for b in berhasil_dikirim:
        rekap_pesan += f" - {b}\n"
    rekap_pesan += f"\nGagal: {len(gagal_dikirim)} nomor\n"
    for g in gagal_dikirim:
        rekap_pesan += f" - {g}\n"
    return rekap_pesan


# Buka nomor pertama (tanpa kirim pesan)
url = f"https://web.whatsapp.com/send?phone={nomor_pertama}&text={encoded_pesan}"
driver.get(url)
print(f"Membuka nomor pertama ({nomor_pertama}) tanpa mengirim pesan...")
time.sleep(2)
tutup_popup_fresh_look()

# Iterasi ke nomor berikutnya (pakai progress bar)
try:
    for i, nomor in enumerate(tqdm(nomor_list[1:], desc="Mengirim pesan ke nomor")):
        url = f"https://web.whatsapp.com/send?phone={nomor}&text={encoded_pesan}"
        driver.get(url)

        try:
            invalid_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//div[contains(text(), "Phone number shared via url is invalid") or contains(text(), "Nomor telepon yang dibagikan via tautan tidak valid")]'
                ))
            )
            gagal_dikirim.append(nomor)
            continue
        except:
            pass

        try:
            message_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@role="textbox"][@data-tab]'))
            )

            try:
                send_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[(@aria-label="Send" or @aria-label="Kirim") and .//span[@data-icon="wds-ic-send-filled"]]'))
                )
                send_button.click()
                berhasil_dikirim.append(nomor)
            except:
                gagal_dikirim.append(nomor)

            time.sleep(random.randint(1,2))

        except Exception:
            gagal_dikirim.append(nomor)
            # Cek apakah driver masih aktif sebelum akses page_source
            try:
                if driver.service.process.poll() is None:
                    with open(f"debug_{nomor}.html", "w", encoding="utf-8") as f:
                        f.write(driver.page_source)
            except:
                pass

except KeyboardInterrupt:
    print("\nInterupsi diterima! Mencetak rekap di terminal...\n")
    rekap_terminal = buat_pesan_rekap()
    print(rekap_terminal)
    try:
        driver.quit()
    except:
        pass
    exit()

# =========================
# Kirim rekap (Normal)
# =========================
rekap_terminal = buat_pesan_rekap()
print("\nMencetak rekap ke terminal:\n")
print(rekap_terminal)

rekap_encoded = urllib.parse.quote(rekap_terminal)
print(f"\nMengirim rekap ke nomor pertama: {nomor_pertama}")
driver.get(f"https://web.whatsapp.com/send?phone={nomor_pertama}&text={rekap_encoded}")

try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@role="textbox"][@data-tab]'))
    )
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[(@aria-label="Send" or @aria-label="Kirim") and .//span[@data-icon="wds-ic-send-filled"]]'))
    )
    send_button.click()
    print("Rekap berhasil dikirim ke nomor pertama")
    time.sleep(5)
except Exception as e:
    print(f"Gagal mengirim rekap: {e}")

time.sleep(3)
driver.quit()
