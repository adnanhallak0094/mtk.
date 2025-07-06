#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف إعدادات التطبيق
Application Configuration File
"""

# معلومات التطبيق
APP_NAME = "أداة تعريب الهواتف الذكية"
APP_VERSION = "1.0.0"
APP_AUTHOR = "أبو محمود السوري"
APP_EMAIL = "support@abu-mahmoud-syrian.com"

# إعدادات الواجهة
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
WINDOW_BG_COLOR = "#2c3e50"
FRAME_BG_COLOR = "#34495e"
TEXT_COLOR = "#ecf0f1"

# ألوان الأزرار
BUTTON_COLORS = {
    "primary": "#3498db",
    "success": "#27ae60", 
    "warning": "#e67e22",
    "danger": "#e74c3c",
    "info": "#9b59b6",
    "secondary": "#1abc9c"
}

# أنواع المعالجات المدعومة
SUPPORTED_PROCESSORS = [
    "Qualcomm Snapdragon",
    "MediaTek (MTK)",
    "Samsung Exynos", 
    "HiSilicon Kirin",
    "UNISOC (Spreadtrum)"
]

# إصدارات الأندرويد المدعومة
SUPPORTED_ANDROID_VERSIONS = [
    "Android 8",
    "Android 9", 
    "Android 10",
    "Android 11",
    "Android 12",
    "Android 13",
    "Android 14",
    "Android 15"
]

# إعدادات الترخيص
LICENSE_KEY_LENGTH = 25
LICENSE_KEY_PARTS = 5
LICENSE_CHECKSUM_MOD = 1000
LICENSE_VALID_CHECKSUM = 123

# مسارات الملفات
LOGS_DIR = "logs"
KEYS_DIR = "keys"
TEMP_DIR = "temp"

# إعدادات MTK
MTK_SUPPORTED_KEYS = [
    "DA_KEY",
    "SBC_KEY", 
    "ROOT_KEY",
    "CRYPTO_SEED",
    "AUTH_KEY",
    "KCFG_LOCK",
    "SLA_CHALLENGE",
    "SLA_RESPONSE"
]

# رسائل الحالة
STATUS_MESSAGES = {
    "ready": "جاهز للعمل",
    "arabizing": "جاري التعريب...",
    "frp_unlocking": "جاري فك FRP...",
    "extracting_keys": "جاري استخراج المفاتيح...",
    "converting_log": "جاري تحويل اللوج...",
    "success": "تمت العملية بنجاح!",
    "error": "حدث خطأ أثناء العملية"
}

# إعدادات الأمان
SECURITY_SETTINGS = {
    "enable_logging": True,
    "encrypt_keys": True,
    "backup_data": True,
    "verify_checksums": True
}

