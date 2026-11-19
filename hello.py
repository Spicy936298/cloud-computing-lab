#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hello.py
云计算课程 - Git/GitHub 课后作业示例程序
更新版本：新增带姓名的个性化问候与实验信息展示
"""

def greet(name):
    """返回一个个性化的欢迎信息"""
    return "Hello, {}! 欢迎来到 Cloud Computing Lab!".format(name)

def show_lab_info():
    """展示当前实验的基本信息"""
    info = {
        "课程": "云计算",
        "实验": "创建个人项目仓库并完成开发流程",
        "仓库": "cloud-computing-lab",
        "分支": "main",
    }
    print("=== 实验信息 ===")
    for key, value in info.items():
        print("  {}: {}".format(key, value))
    print("================")

def main():
    print(greet("Spicy936298"))
    print(greet("Cloud Learner"))
    show_lab_info()

if __name__ == "__main__":
    main()
