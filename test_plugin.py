#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试插件主类是否能被正确导入
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # 测试直接导入
    from main import HelpTypst
    print("✓ 直接导入 HelpTypst 成功")
    print(f"  类名: {HelpTypst.__name__}")
    print(f"  模块: {HelpTypst.__module__}")
    print(f"  父类: {HelpTypst.__base__.__name__}")
except Exception as e:
    print(f"✗ 直接导入 HelpTypst 失败: {e}")

try:
    # 测试从包导入
    from astrbot_plugin_help_typst import HelpTypst
    print("\n✓ 从包导入 HelpTypst 成功")
    print(f"  类名: {HelpTypst.__name__}")
    print(f"  模块: {HelpTypst.__module__}")
except Exception as e:
    print(f"\n✗ 从包导入 HelpTypst 失败: {e}")

try:
    # 测试动态导入
    import importlib
    module = importlib.import_module("main")
    print("\n✓ 动态导入 main 模块成功")
    
    # 查找所有继承自 Star 的类
    from astrbot.api.star import Star
    star_classes = [cls for name, cls in module.__dict__.items() 
                   if isinstance(cls, type) and issubclass(cls, Star) and cls != Star]
    print(f"  找到 {len(star_classes)} 个 Star 子类:")
    for cls in star_classes:
        print(f"    - {cls.__name__}")
except Exception as e:
    print(f"\n✗ 动态导入测试失败: {e}")
