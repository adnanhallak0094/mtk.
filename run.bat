@echo off
chcp 65001 >nul
title أداة تعريب الهواتف الذكية - أبو محمود السوري

echo ===================================================
echo           أداة تعريب الهواتف الذكية
echo                أبو محمود السوري
echo ===================================================
echo.

echo جاري فحص متطلبات النظام...

:: فحص Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo خطأ: Python غير مثبت على النظام
    echo يرجى تثبيت Python 3.6 أو أحدث من python.org
    pause
    exit /b 1
)

echo ✓ Python مثبت

:: فحص tkinter
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo خطأ: tkinter غير متوفر
    echo يرجى إعادة تثبيت Python مع tkinter
    pause
    exit /b 1
)

echo ✓ tkinter متوفر

:: فحص الملفات المطلوبة
if not exist "advanced_main.py" (
    echo خطأ: الملف الرئيسي غير موجود
    pause
    exit /b 1
)

echo ✓ الملفات المطلوبة موجودة

:: إنشاء المجلدات المطلوبة
if not exist "logs" mkdir logs
if not exist "keys" mkdir keys
if not exist "temp" mkdir temp
if not exist "backups" mkdir backups

echo ✓ تم إنشاء المجلدات المطلوبة

echo.
echo جاري تشغيل التطبيق...
echo.

:: تشغيل التطبيق
python advanced_main.py

if %errorlevel% neq 0 (
    echo.
    echo حدث خطأ أثناء تشغيل التطبيق
    echo يرجى مراجعة ملف السجل للتفاصيل
    pause
)

echo.
echo تم إغلاق التطبيق
pause

