# 📨 WhatsApp Bulk Sender

Automated WhatsApp message sender using Selenium and WhatsApp Web. Reads phone numbers from a CSV file, sends a predefined message to each contact, and delivers a delivery summary report to the first number.

---

## 📋 Requirements

- Python 3.7+
- Google Chrome browser
- Active WhatsApp account

### Python Dependencies

Install all required packages:

```bash
pip install selenium webdriver-manager pandas tqdm
```

---

## 📁 Project Structure

```
project/
├── main.py          # Main script
├── nomor.csv        # CSV file containing phone numbers
└── README.md
```

---

## 📄 CSV Format

Prepare a file named `nomor.csv` with the following structure:

```csv
nomor
812345678
856789012
877654321
```

> **Note:** Numbers should be in local Indonesian format (starting with `0` or without country code). The script will automatically prepend `62` (Indonesia country code).

---

## ⚙️ Configuration

Open `main.py` and edit the `pesan` variable to set your message:

```python
pesan = """
Your message goes here.
"""
```

---

## 🚀 How to Use

1. **Prepare your CSV file** — ensure `nomor.csv` is in the same directory as the script.

2. **Run the script:**

   ```bash
   python main.py
   ```

3. **Scan the QR Code** — WhatsApp Web will open in Chrome. Scan the QR code with your phone.

4. **Press ENTER** — once logged in, press `ENTER` in the terminal to start sending.

5. **Wait for completion** — the script will iterate through all numbers automatically.

6. **View the summary** — after all messages are sent, a delivery report will be printed in the terminal and sent to the **first number** in the CSV.

---

## 🛑 Stopping Mid-Run

Press `Ctrl+C` at any time to interrupt the process. A delivery summary will be printed to the terminal before the program exits.

---

## 📊 Delivery Report

At the end of the session, the script generates a report similar to:

```
REKAP PENGIRIMAN

Berhasil: 3 nomor
 - 6281234567
 - 6285678901
 - 6287765432

Gagal: 1 nomor
 - 6289999999
```

This report is also sent automatically to the first number in the CSV list.

---

## ⚠️ Notes & Limitations

- This tool uses **WhatsApp Web via browser automation** and is not an official API integration.
- Numbers not registered on WhatsApp will be marked as **failed**.
- A random delay of **1–2 seconds** is added between each message to reduce the risk of being flagged.
- Avoid sending to very large lists in a single session to minimize the chance of your account being restricted by WhatsApp.
- Debug HTML files (`debug_<nomor>.html`) may be created for failed numbers to help with troubleshooting.

---

## 🐛 Troubleshooting

| Issue | Solution |
|---|---|
| Chrome doesn't open | Make sure Google Chrome is installed |
| QR code not loading | Check your internet connection |
| Messages not sending | Ensure the send button XPath is up to date with current WhatsApp Web version |
| Number marked as failed | The number may not be registered on WhatsApp |

---

## 📜 License

This project is intended for **personal and educational use only**. Always comply with [WhatsApp's Terms of Service](https://www.whatsapp.com/legal/terms-of-service) when using automation tools.
S
