#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف إعداد التطبيق
Setup Script for Arabic Phone Tool
"""

from setuptools import setup, find_packages
import os

# قراءة ملف README
def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

# قراءة متطلبات التطبيق
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="arabic-phone-tool",
    version="1.0.0",
    author="أبو محمود السوري",
    author_email="support@abu-mahmoud-syrian.com",
    description="أداة شاملة لتعريب الهواتف الذكية وفك قفل FRP مع أدوات MTK متقدمة",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/abu-mahmoud-syrian/arabic-phone-tool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Hardware",
        "Topic :: Utilities",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pyinstaller>=4.0",
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
        "build": [
            "pyinstaller>=4.0",
            "auto-py-to-exe>=2.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "arabic-phone-tool=advanced_main:main",
        ],
        "gui_scripts": [
            "arabic-phone-tool-gui=advanced_main:main",
        ]
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "*.ico"],
    },
    data_files=[
        ("", ["README.md", "LICENSE"]),
        ("config", ["config.py"]),
        ("utils", ["utils.py"]),
    ],
    zip_safe=False,
    keywords=[
        "android", "arabic", "localization", "frp", "unlock", 
        "mtk", "mediatek", "phone", "smartphone", "tool",
        "أندرويد", "تعريب", "فك", "قفل", "هاتف", "أداة"
    ],
    project_urls={
        "Bug Reports": "https://github.com/abu-mahmoud-syrian/arabic-phone-tool/issues",
        "Source": "https://github.com/abu-mahmoud-syrian/arabic-phone-tool",
        "Documentation": "https://github.com/abu-mahmoud-syrian/arabic-phone-tool/wiki",
        "Funding": "https://github.com/sponsors/abu-mahmoud-syrian",
    },
)

