# Quick Workspace Launcher

> 对我个人而言的 Python 期末课程设计。

一个基于 Python 开发的轻量级命令行启动器，用于统一管理常用软件、文件夹和网页，并支持一键启动。

项目采用 **JSON** 作为数据存储，无需数据库，适合作为日常开发工具或 Python 课程设计。

---

## ✨ Features

- Add launcher items
- List all items
- Edit existing items
- Delete items
- Launch a specified item
- Launch all items with one command
- Automatically detect URL or local application

---

## 📂 Project Structure

```text
.
├── launcher.py      # Main program
├── items.json       # Data file (generated automatically)
└── README.md
```

---

## 🚀 Usage

### Add an item

```bash
python launcher.py add "Visual Studio" "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
```

Add a website:

```bash
python launcher.py add "GitHub" "https://github.com"
```

Specify the type manually:

```bash
python launcher.py add "GitHub" "https://github.com" --type url
```

---

### List all items

```bash
python launcher.py list
```

Example:

```text
Visual Studio | app | C:\Program Files\Microsoft Visual Studio\...
GitHub | url | https://github.com
```

---

### Edit an item

Change the path:

```bash
python launcher.py edit "Visual Studio" --path "D:\VS\devenv.exe"
```

Rename an item:

```bash
python launcher.py edit "Visual Studio" --rename "VS2022"
```

Change the type:

```bash
python launcher.py edit "GitHub" --type url
```

---

### Delete an item

```bash
python launcher.py del "GitHub"
```

---

### Launch a specified item

```bash
python launcher.py run "Visual Studio"
```

---

### Launch all items

```bash
python launcher.py run-all
```

---

## 📄 Data Format

All launcher items are stored in `items.json`.

Example:

```json
{
    "GitHub": {
        "type": "url",
        "path": "https://github.com"
    },
    "Visual Studio": {
        "type": "app",
        "path": "C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\Common7\\IDE\\devenv.exe"
    }
}
```

---

## 🛠 Technologies

- Python
- argparse
- json
- os
- webbrowser

---

## 📄 License

MIT License
