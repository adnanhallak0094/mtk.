#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
وظائف مساعدة للتطبيق
Utility Functions for the Application
"""

import os
import json
import hashlib
import random
import string
import re
from datetime import datetime
import subprocess
import sys

class DeviceManager:
    """مدير الأجهزة المتصلة"""
    
    @staticmethod
    def check_device_connection():
        """فحص اتصال الجهاز"""
        try:
            # محاكاة فحص الجهاز
            result = subprocess.run(['adb', 'devices'], 
                                  capture_output=True, text=True, timeout=10)
            return "device" in result.stdout
        except:
            return False
    
    @staticmethod
    def get_device_info():
        """الحصول على معلومات الجهاز"""
        try:
            # محاكاة الحصول على معلومات الجهاز
            info = {
                "model": "Samsung Galaxy S21",
                "android_version": "Android 12",
                "processor": "Qualcomm Snapdragon",
                "build_number": "SP1A.210812.016",
                "security_patch": "2024-01-01"
            }
            return info
        except:
            return None

class ArabizationEngine:
    """محرك التعريب"""
    
    def __init__(self):
        self.supported_languages = ["ar", "en", "fr", "es", "de"]
        
    def apply_arabic_fonts(self, device_info):
        """تطبيق الخطوط العربية"""
        steps = [
            "تحميل حزمة الخطوط العربية",
            "نسخ الخطوط إلى مجلد النظام",
            "تحديث إعدادات الخطوط",
            "إعادة تشغيل خدمة العرض"
        ]
        return steps
        
    def configure_rtl_support(self, device_info):
        """تكوين دعم الكتابة من اليمين لليسار"""
        steps = [
            "تفعيل دعم RTL في النظام",
            "تحديث إعدادات التخطيط",
            "تطبيق التغييرات على التطبيقات",
            "اختبار العرض"
        ]
        return steps
        
    def install_arabic_keyboard(self, device_info):
        """تثبيت لوحة المفاتيح العربية"""
        steps = [
            "تحميل لوحة المفاتيح العربية",
            "تثبيت التطبيق",
            "تكوين الإعدادات",
            "تفعيل اللوحة"
        ]
        return steps

class FRPUnlocker:
    """أداة فك قفل FRP"""
    
    def __init__(self):
        self.supported_methods = ["bypass", "remove", "reset"]
        
    def check_frp_status(self, device_info):
        """فحص حالة FRP"""
        # محاكاة فحص FRP
        return {
            "locked": True,
            "method": "Google Account",
            "security_level": "High"
        }
        
    def unlock_frp_qualcomm(self, device_info):
        """فك FRP لمعالجات Qualcomm"""
        steps = [
            "فحص نوع المعالج",
            "تحميل أدوات Qualcomm",
            "تطبيق الفك",
            "التحقق من النتيجة"
        ]
        return steps
        
    def unlock_frp_mtk(self, device_info):
        """فك FRP لمعالجات MediaTek"""
        steps = [
            "فحص نوع المعالج MTK",
            "استخدام أدوات SP Flash Tool",
            "تطبيق الفك",
            "إعادة التشغيل"
        ]
        return steps

class MTKToolkit:
    """مجموعة أدوات MediaTek"""
    
    def __init__(self):
        self.supported_chips = ["MT6580", "MT6737", "MT6750", "MT6753", "MT6755"]
        
    def extract_keys_from_device(self, device_info):
        """استخراج المفاتيح من الجهاز"""
        # محاكاة استخراج المفاتيح
        keys = {
            "DA_KEY": self._generate_hex_key(32),
            "SBC_KEY": self._generate_hex_key(32),
            "ROOT_KEY": self._generate_hex_key(32),
            "CRYPTO_SEED": self._generate_hex_key(32),
            "AUTH_KEY": self._generate_hex_key(40)
        }
        return keys
        
    def parse_log_file(self, log_path):
        """تحليل ملف اللوج واستخراج المفاتيح"""
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # البحث عن أنماط المفاتيح
            patterns = {
                "DA_KEY": r'DA[_\s]*KEY[:\s]*([0-9A-Fa-f]{32})',
                "SBC_KEY": r'SBC[_\s]*KEY[:\s]*([0-9A-Fa-f]{32})',
                "ROOT_KEY": r'ROOT[_\s]*KEY[:\s]*([0-9A-Fa-f]{32})',
                "CRYPTO_SEED": r'CRYPTO[_\s]*SEED[:\s]*([0-9A-Fa-f]{32})',
                "AUTH_KEY": r'AUTH[_\s]*KEY[:\s]*([0-9A-Fa-f]{40})'
            }
            
            extracted_keys = {}
            for key_name, pattern in patterns.items():
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    extracted_keys[key_name] = match.group(1)
                    
            return extracted_keys
            
        except Exception as e:
            return {"error": str(e)}
            
    def _generate_hex_key(self, length):
        """توليد مفتاح hex عشوائي"""
        return ''.join(random.choices('0123456789ABCDEF', k=length))

class LicenseManager:
    """مدير التراخيص"""
    
    def __init__(self):
        self.key_length = 25
        self.parts_count = 5
        
    def generate_license_key(self, username, email):
        """توليد مفتاح ترخيص"""
        # إنشاء بذرة من معلومات المستخدم
        seed = f"{username}{email}{datetime.now().strftime('%Y%m%d')}"
        hash_object = hashlib.md5(seed.encode())
        hash_hex = hash_object.hexdigest()
        
        # تحويل إلى مفتاح بصيغة XXXX-XXXX-XXXX-XXXX-XXXX
        key_parts = []
        for i in range(0, 20, 4):
            part = hash_hex[i:i+4].upper()
            key_parts.append(part)
            
        # إضافة checksum
        checksum = sum(ord(c) for c in ''.join(key_parts)) % 10000
        key_parts[-1] = f"{checksum:04d}"
        
        return '-'.join(key_parts)
        
    def validate_license_key(self, key):
        """التحقق من صحة مفتاح الترخيص"""
        if len(key) != self.key_length or key.count('-') != 4:
            return False
            
        parts = key.split('-')
        if len(parts) != self.parts_count:
            return False
            
        # التحقق من كل جزء
        for part in parts:
            if len(part) != 4:
                return False
                
        # التحقق من checksum
        checksum = sum(ord(c) for c in key.replace('-', '')) % 1000
        return checksum == 123  # قيمة ثابتة للتبسيط

class FileManager:
    """مدير الملفات"""
    
    @staticmethod
    def create_directories():
        """إنشاء المجلدات المطلوبة"""
        dirs = ["logs", "keys", "temp", "backups"]
        for dir_name in dirs:
            os.makedirs(dir_name, exist_ok=True)
            
    @staticmethod
    def save_keys_to_file(keys, filename):
        """حفظ المفاتيح في ملف"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== مفاتيح MTK المستخرجة ===\n\n")
                for key_name, key_value in keys.items():
                    f.write(f"{key_name}: {key_value}\n")
                f.write(f"\nتاريخ الاستخراج: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            return True
        except Exception as e:
            return False
            
    @staticmethod
    def load_keys_from_file(filename):
        """تحميل المفاتيح من ملف"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            return None

class SecurityUtils:
    """أدوات الأمان"""
    
    @staticmethod
    def encrypt_data(data, key):
        """تشفير البيانات"""
        # تشفير بسيط للتوضيح
        encrypted = ""
        for i, char in enumerate(data):
            encrypted += chr(ord(char) ^ ord(key[i % len(key)]))
        return encrypted
        
    @staticmethod
    def decrypt_data(encrypted_data, key):
        """فك تشفير البيانات"""
        # فك التشفير
        decrypted = ""
        for i, char in enumerate(encrypted_data):
            decrypted += chr(ord(char) ^ ord(key[i % len(key)]))
        return decrypted
        
    @staticmethod
    def calculate_checksum(data):
        """حساب checksum للبيانات"""
        return hashlib.md5(data.encode()).hexdigest()

class Logger:
    """نظام السجلات"""
    
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        
    def log(self, level, message):
        """كتابة رسالة في السجل"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except:
            pass
            
    def info(self, message):
        """رسالة معلومات"""
        self.log("INFO", message)
        
    def warning(self, message):
        """رسالة تحذير"""
        self.log("WARNING", message)
        
    def error(self, message):
        """رسالة خطأ"""
        self.log("ERROR", message)

