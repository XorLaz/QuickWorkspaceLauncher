Quick Workspace Launcher

对我个人而言的期末Python小作业。

一个基于 Python 开发的轻量级命令行启动器，用于统一管理常用软件、文件夹和网页，并支持一键启动。
项目采用 JSON 作为数据存储，无需数据库，适合作为日常开发工具或 Python 课程设计。

________________________________________
功能
添加启动项
查看所有启动项
修改启动项
删除启动项
启动指定项目
一键启动全部项目
自动识别 URL 与本地程序
________________________________________


使用方法
添加启动项
python launcher.py add "Visual Studio" "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
添加网页：
python launcher.py add "GitHub" "https://github.com"
也可以手动指定类型：
python launcher.py add "GitHub" "https://github.com" --type url

________________________________________

查看所有项目
python launcher.py list
示例：
Visual Studio | app | C:\Program Files\Microsoft Visual Studio\...
GitHub | url | https://github.com

________________________________________

修改项目
修改路径：
python launcher.py edit "Visual Studio" --path "D:\VS\devenv.exe"
修改名称：
python launcher.py edit "Visual Studio" --rename "VS2022"
修改类型：
python launcher.py edit "GitHub" --type url

________________________________________

删除项目

python launcher.py del "GitHub"

________________________________________

启动指定项目
python launcher.py run "Visual Studio"

________________________________________

一键启动全部项目
python launcher.py run-all

________________________________________


数据格式
所有数据保存在 items.json 中，例如：
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


________________________________________
技术实现
•	Python
•	argparse
•	json
•	os
•	webbrowser
________________________________________
License
MIT License
