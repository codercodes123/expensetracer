# Git Commands to Create and Push Repository

## Step 1: Initialize Git Repository
```bash
git init
```

## Step 2: Add All Files
```bash
git add .
```

## Step 3: Create Initial Commit
```bash
git commit -m "🚀 AI for Bharat Week 2: Lazy Expense Tracker - Built with Kiro in 2 hours!"
```

## Step 4: Create GitHub Repository
Go to https://github.com/new and create a new repository named `lazy-expense-tracker`
- Make it Public
- Don't initialize with README (we already have one)

## Step 5: Add Remote Origin
```bash
git remote add origin https://github.com/YOUR_USERNAME/lazy-expense-tracker.git
```

## Step 6: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## All Commands in One Block (Copy-Paste Ready)
```bash
git init
git add .
git commit -m "🚀 AI for Bharat Week 2: Lazy Expense Tracker - Built with Kiro in 2 hours!"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/lazy-expense-tracker.git
git push -u origin main
```

## After Screenshots
Once you add screenshots, run:
```bash
git add screenshots/
git commit -m "📸 Add screenshots for documentation"
git push
```

---

**Remember to replace `YOUR_USERNAME` with your actual GitHub username!**
