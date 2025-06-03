# 🧠 SmartLeadProfiler

A lightweight AI-powered lead scoring and profiling tool built in 5 hours for Caprae Capital’s AI-Readiness Challenge.

## 🔍 Features
- Input: Company domain
- Scrapes website title
- Uses Hunter.io API to enrich email data
- Assigns lead score based on quality
- Clean Streamlit UI

## ⚙️ Tech Stack
- Python, Streamlit, Hunter.io API, BeautifulSoup

## 🚀 How to Run
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add `.env` file with your API key:
   ```
   HUNTER_API_KEY=your_key
   ```
4. Run app:
   ```bash
   streamlit run app.py
   ```

## 📄 Report
See `SmartLeadProfiler_Report.pdf` in this repo for full breakdown.

## 👤 Author
Mohith