# 🔐 Secret Steganography App

A Python-based web application that lets users **hide and extract secret messages inside images** using the **Least Significant Bit (LSB)** steganography technique. Built with a clean **Streamlit** interface and deployable both locally and online.

> 💼 This project demonstrates key skills in Python, image processing, UI design, and deploying data apps — making it a great portfolio addition for internships and developer roles.

---

## 🧰 Tech Stack

| Layer         | Tools / Libraries                          |
|---------------|---------------------------------------------|
| 🧠 Core Logic | Python, NumPy, Pillow (PIL)                 |
| 🖼️ Image Work | LSB Steganography, Pixel Manipulation       |
| 🧪 UI / Web   | Streamlit (for fast frontend + backend)     |
| 🔁 Data       | ByteStream (for image download), PNG format |
| 💻 Deployment | Local Machine or Streamlit Cloud            |
| 📂 Dev Tools  | Git, GitHub, Virtual Environments           |

---

## 🚀 Run This Project Locally

```bash
# 1. Clone the repository
git clone https://github.com/sainivaibhav742/secret_steganography_app.git
cd secret_steganography_app

# 2. Set up virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
