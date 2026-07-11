# 📋 Markdown Table Generator

A simple Python CLI tool that converts CSV files into Markdown tables.

## ✨ Features

- Read CSV files
- Generate GitHub-friendly Markdown tables
- Save output to `output.md`
- Lightweight and beginner-friendly

## 📦 Requirements

- Python 3.x

## ▶️ Run

```bash
python main.py
```

## 📌 Example

Input (`sample.csv`):

```csv
Name,Age,Role
Aliya,20,AI Engineer
Rahul,22,Backend Developer
```

Output (`output.md`):

```markdown
| Name | Age | Role |
| --- | --- | --- |
| Aliya | 20 | AI Engineer |
| Rahul | 22 | Backend Developer |
```

## 🛠 Built With

- Python
- csv (standard library)
