# 💰 Real-Time Bank SMS Expense Tracker

> **AI for Bharat Week 2: Lazy Automation** | Built with Kiro Agent in under 2 hours!

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![AI for Bharat](https://img.shields.io/badge/AI%20for%20Bharat-Week%202-orange.svg)](https://community.aws/ai-for-bharat)

## 🎯 The Problem

Every day, I receive multiple bank SMS notifications from Bank of Maharashtra (MAHABK):
- UPI payments
- Online purchases  
- Salary credits
- Money transfers

**The painful reality:** I was manually copy-pasting these SMS into Excel to track my expenses. This took 15-20 minutes daily and I often forgot to do it!

## 💡 The Solution

A **zero-manual-work** expense tracking system:

```
📱 Bank SMS → 📲 MacroDroid → 📄 expenses_raw.txt → ☁️ Google Drive → 🐍 Python → 📊 Live Dashboard
```

**Result:** Real-time expense tracking with ZERO manual effort!

## ✨ Features

- 🔴 **Real-time monitoring** - Watch transactions as they happen
- 📊 **Beautiful dashboard** - Color-coded credits/debits with emojis
- 📈 **Live totals** - Instant calculation of received/spent/net balance
- 🕐 **Recent transactions** - Top 5 most recent with timestamps
- 📱 **MacroDroid integration** - Automatic SMS capture
- ☁️ **Google Drive sync** - Access from any device

## 📸 Screenshots

### MacroDroid Macro Setup
![MacroDroid Setup](screenshots/macrodroid_setup.png)
*MacroDroid automatically captures MAHABK SMS and writes to file*

### Raw Expenses File
![Expenses Raw](screenshots/expenses_raw.png)
*expenses_raw.txt with captured bank SMS*

### Real-Time Watcher (main.py)
![Live Dashboard](screenshots/live_dashboard.png)
*Live dashboard showing real-time transaction updates*

### Expense Summary (expense_summary.py)
![Summary Report](screenshots/summary_report.png)
*Detailed expense summary with statistics*

### Kiro Agent Chat
![Kiro Chat](screenshots/kiro_chat.png)
*This entire project was built with Kiro's help!*

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/lazy-expense-tracker.git
cd lazy-expense-tracker
```

### 2. Run the Real-Time Watcher
```bash
python main.py
```

### 3. Run the Summary Report
```bash
python expense_summary.py
```

## 📱 MacroDroid Setup

1. **Install MacroDroid** from Play Store
2. **Create new macro** with these settings:

**Trigger:**
- SMS Received
- Content contains: "MAHABK"

**Actions:**
- Write to File
- File: `/storage/emulated/0/expenses_raw.txt`
- Content: `[date] [hour]:[minute]:[second],[sender],[sms_body]`
- Append: Yes

**Constraints:**
- None (run always)

3. **Sync with Google Drive** for cloud access

## 📁 Project Structure

```
lazy-expense-tracker/
├── main.py              # Real-time transaction watcher
├── expense_summary.py   # Detailed summary generator
├── expenses_raw.txt     # Sample transaction data
├── requirements.txt     # Dependencies (standard library only!)
├── README.md           # This file
├── .kiro/
│   └── kiro_chat.md    # Kiro conversation log
└── screenshots/        # Screenshot placeholders
    ├── macrodroid_setup.png
    ├── expenses_raw.png
    ├── live_dashboard.png
    ├── summary_report.png
    └── kiro_chat.png
```

## 📊 Sample Output

```
╔══════════════════════════════════════════════════════════════════════════╗
║   💰  R E A L - T I M E   E X P E N S E   T R A C K E R  💰             ║
║              🏦  Bank of Maharashtra Live Monitor  🏦                    ║
╚══════════════════════════════════════════════════════════════════════════╝

  ● LIVE Watching for new transactions...

  ┌─────────────────────────────┐  ┌─────────────────────────────┐
  │  📥 TOTAL RECEIVED          │  │  📤 TOTAL SPENT             │
  │         ₹19,000.00          │  │          ₹7,901.00          │
  │  4 transactions             │  │  16 transactions            │
  └─────────────────────────────┘  └─────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │  📈 NET BALANCE:  +₹11,099.00  (PROFIT)                         │
  └─────────────────────────────────────────────────────────────────┘
```

## 🛠️ Built With

- **Python 3.7+** - Core language (standard library only!)
- **MacroDroid** - Android automation for SMS capture
- **Google Drive** - Cloud sync
- **Kiro Agent** - AI-powered development assistant

## ⚡ How Kiro Accelerated Development

This entire project was built in **under 2 hours** with Kiro's help:

1. ✅ Regex patterns for parsing bank SMS amounts
2. ✅ Transaction type detection (debit/credit)
3. ✅ Beautiful terminal UI with colors and emojis
4. ✅ Real-time file watching logic
5. ✅ Summary statistics and reporting
6. ✅ Error handling for malformed data
7. ✅ Complete documentation and README

**Without Kiro:** This would have taken 6-8 hours of manual coding and debugging.

## 📈 My Real Data Summary

From December 1-7, 2025:
- **Total Received:** ₹19,000.00
- **Total Spent:** ₹7,901.00  
- **Net Balance:** +₹11,099.00 (Profit! 🎉)
- **Transactions:** 20 total (4 credits, 16 debits)

## 🏆 AI for Bharat Week 2 Submission

This project is my submission for **Week 2: Lazy Automation** of the AI for Bharat hackathon.

**Theme:** Automate a repetitive task using AI tools
**Solution:** Zero-manual-work expense tracking from bank SMS

## 📝 License

MIT License - feel free to use and modify!

## 🙏 Acknowledgments

- **AWS Builder Center** for hosting AI for Bharat
- **Kiro Agent** for accelerating development
- **Bank of Maharashtra** for consistent SMS format 😄

---

**Built with ❤️ and Kiro for AI for Bharat Week 2**

*This project was generated in seconds using Kiro Agent, accelerating my development for the AWS Builder Center blog post.*
