# 💰 Smart Expense Tracker AI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Groq-AI-green?style=for-the-badge" alt="Groq AI">
</p>

## 🚀 Overview

**Smart Expense Tracker AI** is an intelligent personal finance dashboard built with Python and Streamlit. It helps you track expenses, analyze spending patterns, get AI-powered financial insights, and monitor stock prices — all in one sleek web app.

## ✨ Features

- 💵 **Add Expenses** — Log your daily expenses with title, amount, category, and date
- 📊 **View Expenses** — Browse all recorded transactions in a clean table view
- 📈 **Analytics** — Visualize spending patterns with interactive bar charts by category
- 🤖 **AI Insights** — Get smart financial advice powered by Groq AI (Llama 3.3)
- 📉 **Finance Tracker** — Monitor real-time stock prices with historical charts

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web UI Framework |
| **SQLite** | Lightweight database |
| **Pandas** | Data manipulation & analysis |
| **Matplotlib** | Data visualization |
| **yFinance** | Stock market data fetching |
| **Groq API** | AI-powered insights (Llama 3.3) |

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ritik-hub2024/-Smart-Expense-Tracker-AI.git
   cd -Smart-Expense-Tracker-AI
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv-new
   venv-new\Scripts\activate  # Windows
   # OR
   source venv-new/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API Key**
   ```bash
   # Windows PowerShell
   $env:GROQ_API_KEY="your_groq_api_key_here"
   
   # OR create a .env file
   echo GROQ_API_KEY=your_groq_api_key_here > .env
   ```

5. **Run the app**
   ```bash
   python -m streamlit run app2.py
   ```

## 📸 Screenshots

| Add Expense | Analytics Dashboard | AI Insights |
|-------------|---------------------|-------------|
| Log your spending with title, amount, category & date | Interactive bar charts by category | AI-generated financial advice |

## 🏗️ Project Structure

```
Smart-Expense-Tracker-AI/
├── app2.py              # Main Streamlit application
├── db.py                # SQLite database connection & setup
├── expense.py           # Expense data model
├── utils.py             # CRUD operations for expenses
├── analytics.py         # Data analysis with Pandas
├── ai_insights.py       # Groq AI integration
├── finance_api.py       # Stock data via yFinance
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
└── .gitignore           # Ignored files (venv, db, etc.)
```

## 🔐 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes | Your Groq API key for AI insights |

> Get your free API key at [console.groq.com](https://console.groq.com/keys)

## 🎯 Future Enhancements

- [ ] Budget setting & alerts
- [ ] Export data to CSV/Excel
- [ ] Monthly/yearly spending reports
- [ ] Dark mode theme
- [ ] Multi-currency support

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ by <strong>Ritik</strong>
</p>

