import argparse
import json
import os
import sys
import webbrowser

DATA_FILE = "items.json"


def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def guess_type(path):
    return "url" if path.startswith(("http://", "https://")) else "app"


# ---- 增 ----
def cmd_add(args):
    data = load()
    if args.name in data:
        sys.exit(f"已存在: {args.name}")
    data[args.name] = {
        "type": args.type or guess_type(args.path),
        "path": args.path,
    }
    save(data)
    print(f"已添加: {args.name}")


# ---- 查 ----
def cmd_list(args):
    data = load()
    if not data:
        print("暂无条目")
        return
    for name, item in data.items():
        print(f"{name} | {item['type']} | {item['path']}")


# ---- 删 ----
def cmd_del(args):
    data = load()
    if args.name not in data:
        sys.exit(f"不存在: {args.name}")
    del data[args.name]
    save(data)
    print(f"已删除: {args.name}")


# ---- 改 ----
def cmd_edit(args):
    data = load()
    if args.name not in data:
        sys.exit(f"不存在: {args.name}")
    item = data[args.name]
    if args.path:
        item["path"] = args.path
    if args.type:
        item["type"] = args.type
    if args.rename:
        data[args.rename] = data.pop(args.name)
    save(data)
    print("已修改")


# ---- 启动 ----
def cmd_run(args):
    data = load()
    if args.name not in data:
        sys.exit(f"不存在: {args.name}")
    item = data[args.name]
    if item["type"] == "url":
        webbrowser.open(item["path"])
    else:
        os.startfile(item["path"])  # 仅 Windows
    print(f"启动: {args.name}")


# ---- 启动全部 ----
def cmd_run_all(args):
    data = load()
    if not data:
        print("暂无条目")
        return
    for name, item in data.items():
        try:
            if item["type"] == "url":
                webbrowser.open(item["path"])
            else:
                os.startfile(item["path"])
            print(f"启动: {name}")
        except Exception as e:
            print(f"失败: {name} -> {e}")


def build_parser():
    p = argparse.ArgumentParser(description="简易启动器")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="增")
    a.add_argument("name")
    a.add_argument("path")
    a.add_argument("--type", choices=["app", "url"])
    a.set_defaults(func=cmd_add)

    sub.add_parser("list", help="查").set_defaults(func=cmd_list)
    sub.add_parser("run-all", help="启动全部").set_defaults(func=cmd_run_all)

    d = sub.add_parser("del", help="删")
    d.add_argument("name")
    d.set_defaults(func=cmd_del)

    e = sub.add_parser("edit", help="改")
    e.add_argument("name")
    e.add_argument("--rename")
    e.add_argument("--path")
    e.add_argument("--type", choices=["app", "url"])
    e.set_defaults(func=cmd_edit)

    r = sub.add_parser("run", help="启动")
    r.add_argument("name")
    r.set_defaults(func=cmd_run)

    return p


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()