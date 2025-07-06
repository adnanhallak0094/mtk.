#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف بناء التطبيق التنفيذي
Build Executable Script
"""

import os
import sys
import subprocess
import shutil

def install_pyinstaller():
    """تثبيت PyInstaller"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("تم تثبيت PyInstaller بنجاح")
        return True
    except subprocess.CalledProcessError:
        print("فشل في تثبيت PyInstaller")
        return False

def create_spec_file():
    """إنشاء ملف المواصفات"""
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['advanced_main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config.py', '.'),
        ('utils.py', '.'),
        ('README.md', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ArabicPhoneTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'
)
'''
    
    with open('ArabicPhoneTool.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("تم إنشاء ملف المواصفات")

def build_executable():
    """بناء الملف التنفيذي"""
    try:
        # إنشاء ملف المواصفات
        create_spec_file()
        
        # بناء التطبيق
        subprocess.check_call([
            "pyinstaller", 
            "--onefile", 
            "--windowed",
            "--name=ArabicPhoneTool",
            "--distpath=dist",
            "--workpath=build",
            "advanced_main.py"
        ])
        
        print("تم بناء الملف التنفيذي بنجاح!")
        print("الملف التنفيذي موجود في مجلد: dist/")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"فشل في بناء الملف التنفيذي: {e}")
        return False

def create_installer_script():
    """إنشاء سكريبت التثبيت"""
    installer_content = '''@echo off
echo ===================================
echo تثبيت أداة تعريب الهواتف الذكية
echo أبو محمود السوري
echo ===================================
echo.

echo جاري إنشاء مجلد التثبيت...
if not exist "C:\\ArabicPhoneTool" mkdir "C:\\ArabicPhoneTool"

echo جاري نسخ الملفات...
copy "ArabicPhoneTool.exe" "C:\\ArabicPhoneTool\\"
copy "README.md" "C:\\ArabicPhoneTool\\"

echo جاري إنشاء اختصار على سطح المكتب...
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = "%USERPROFILE%\\Desktop\\أداة تعريب الهواتف.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "C:\\ArabicPhoneTool\\ArabicPhoneTool.exe" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript CreateShortcut.vbs
del CreateShortcut.vbs

echo.
echo تم التثبيت بنجاح!
echo يمكنك الآن تشغيل البرنامج من سطح المكتب
echo.
pause
'''
    
    with open('install.bat', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    
    print("تم إنشاء سكريبت التثبيت")

def main():
    """الدالة الرئيسية"""
    print("=== بناء تطبيق تعريب الهواتف الذكية ===")
    print("أبو محمود السوري")
    print()
    
    # التحقق من وجود الملفات المطلوبة
    required_files = ['advanced_main.py', 'config.py', 'utils.py']
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"خطأ: الملف المطلوب غير موجود: {file}")
            return
    
    # تثبيت PyInstaller
    print("1. تثبيت PyInstaller...")
    if not install_pyinstaller():
        return
    
    # بناء الملف التنفيذي
    print("2. بناء الملف التنفيذي...")
    if not build_executable():
        return
    
    # إنشاء سكريبت التثبيت
    print("3. إنشاء سكريبت التثبيت...")
    create_installer_script()
    
    print()
    print("=== تم الانتهاء بنجاح! ===")
    print("الملفات المنشأة:")
    print("- dist/ArabicPhoneTool.exe (الملف التنفيذي)")
    print("- install.bat (سكريبت التثبيت)")
    print()
    print("لتوزيع التطبيق:")
    print("1. انسخ الملف التنفيذي وسكريبت التثبيت")
    print("2. شغل install.bat كمدير")
    print("3. سيتم تثبيت التطبيق في C:\\ArabicPhoneTool")

if __name__ == "__main__":
    main()

