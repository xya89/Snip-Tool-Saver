# 📸 Screenshot Saver – Streamlit App

A lightweight Streamlit web app to quickly **paste screenshots from clipboard** (e.g., from `Win + Shift + S`) and **save them as PNG files**.

## 🚀 How to Use

1. **Take a Screenshot**  
   Press `Win + Shift + S` to use the Snipping Tool on Windows. Your screenshot will be copied to the clipboard.

2. **Paste & Save**  
   Run this app. Click **"📋 Paste from Clipboard"** to fetch the image. If successful, the image will display along with a **Download** button.

## 🛠️ Setup

Install dependencies if you haven’t already:

```bash
pip install streamlit pillow
```

Then run the app:

```bash
streamlit run app.py
```

Note: This app works on Windows only, since ImageGrab.grabclipboard() relies on the Windows clipboard.

## 📁 Output
- The image is displayed in the app.

- A PNG download button is provided, with filenames like:
```bash
screenshot_20250514_134522.png
```

## 📌 Requirements
- Python 3.7+

- Windows OS

- Modules: streamlit, Pillow