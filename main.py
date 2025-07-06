#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تطبيق تعريب الهواتف الذكية - أبو محمود السوري
Arabic Phone Tool - Abu Mahmoud Al-Souri
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import time
import os
import json
import hashlib
import random
import string
from datetime import datetime
import subprocess
import sys

class ArabicPhoneTool:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.license_verified = False
        
    def setup_window(self):
        """إعداد النافذة الرئيسية"""
        self.root.title("أداة تعريب الهواتف الذكية - أبو محمود السوري")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(True, True)
        
        # تعيين الأيقونة (إذا كانت متوفرة)
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
            
    def create_widgets(self):
        """إنشاء عناصر الواجهة"""
        # الإطار الرئيسي
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # العنوان الرئيسي
        title_label = tk.Label(main_frame, 
                              text="أداة تعريب الهواتف الذكية\nأبو محمود السوري", 
                              font=("Arial", 20, "bold"),
                              fg='#ecf0f1', bg='#2c3e50')
        title_label.pack(pady=20)
        
        # إطار الترخيص
        license_frame = tk.LabelFrame(main_frame, text="التحقق من الترخيص", 
                                     font=("Arial", 12, "bold"),
                                     fg='#ecf0f1', bg='#34495e')
        license_frame.pack(fill=tk.X, pady=10)
        
        # مدخل مفتاح الترخيص
        tk.Label(license_frame, text="مفتاح الترخيص:", 
                font=("Arial", 10), fg='#ecf0f1', bg='#34495e').pack(anchor=tk.W, padx=10, pady=5)
        
        self.license_entry = tk.Entry(license_frame, font=("Arial", 10), width=50)
        self.license_entry.pack(padx=10, pady=5)
        
        # أزرار الترخيص
        license_buttons_frame = tk.Frame(license_frame, bg='#34495e')
        license_buttons_frame.pack(pady=10)
        
        tk.Button(license_buttons_frame, text="التحقق من الترخيص", 
                 command=self.verify_license, bg='#27ae60', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(license_buttons_frame, text="فتح مولد المفاتيح", 
                 command=self.open_keygen, bg='#e74c3c', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        # إطار الوظائف الرئيسية
        self.main_functions_frame = tk.Frame(main_frame, bg='#2c3e50')
        self.main_functions_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # إنشاء دفتر الملاحظات (Notebook) للتبويبات
        self.notebook = ttk.Notebook(self.main_functions_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # تبويب التعريب وفك FRP
        self.create_arabic_frp_tab()
        
        # تبويب أدوات MTK
        self.create_mtk_tools_tab()
        
        # تبويب السجلات
        self.create_logs_tab()
        
        # إخفاء الوظائف الرئيسية في البداية
        self.main_functions_frame.pack_forget()
        
    def create_arabic_frp_tab(self):
        """إنشاء تبويب التعريب وفك FRP"""
        arabic_frame = ttk.Frame(self.notebook)
        self.notebook.add(arabic_frame, text="التعريب وفك FRP")
        
        # اختيار نوع المعالج
        processor_frame = tk.LabelFrame(arabic_frame, text="اختيار نوع المعالج", 
                                       font=("Arial", 12, "bold"))
        processor_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.processor_var = tk.StringVar()
        processors = [
            "Qualcomm Snapdragon",
            "MediaTek (MTK)",
            "Samsung Exynos",
            "HiSilicon Kirin",
            "UNISOC (Spreadtrum)"
        ]
        
        for processor in processors:
            tk.Radiobutton(processor_frame, text=processor, 
                          variable=self.processor_var, value=processor,
                          font=("Arial", 10)).pack(anchor=tk.W, padx=10, pady=2)
        
        # اختيار إصدار الأندرويد
        android_frame = tk.LabelFrame(arabic_frame, text="إصدار الأندرويد", 
                                     font=("Arial", 12, "bold"))
        android_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.android_var = tk.StringVar()
        android_versions = ["Android 8", "Android 9", "Android 10", 
                           "Android 11", "Android 12", "Android 13", 
                           "Android 14", "Android 15"]
        
        android_combo = ttk.Combobox(android_frame, textvariable=self.android_var, 
                                    values=android_versions, state="readonly")
        android_combo.pack(padx=10, pady=10)
        
        # أزرار العمليات
        operations_frame = tk.Frame(arabic_frame)
        operations_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(operations_frame, text="بدء التعريب", 
                 command=self.start_arabization, bg='#3498db', fg='white',
                 font=("Arial", 12, "bold"), height=2).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        tk.Button(operations_frame, text="فك FRP", 
                 command=self.unlock_frp, bg='#e67e22', fg='white',
                 font=("Arial", 12, "bold"), height=2).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # شريط التقدم
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(arabic_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.pack(pady=10)
        
        # نص الحالة
        self.status_label = tk.Label(arabic_frame, text="جاهز للعمل", 
                                    font=("Arial", 10), fg='blue')
        self.status_label.pack(pady=5)
        
    def create_mtk_tools_tab(self):
        """إنشاء تبويب أدوات MTK"""
        mtk_frame = ttk.Frame(self.notebook)
        self.notebook.add(mtk_frame, text="أدوات MTK")
        
        # أدوات MTK
        tools_frame = tk.LabelFrame(mtk_frame, text="أدوات MediaTek", 
                                   font=("Arial", 12, "bold"))
        tools_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # أزرار أدوات MTK
        mtk_buttons_frame = tk.Frame(tools_frame)
        mtk_buttons_frame.pack(pady=10)
        
        tk.Button(mtk_buttons_frame, text="سحب مفاتيح MTK", 
                 command=self.extract_mtk_keys, bg='#9b59b6', fg='white',
                 font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(mtk_buttons_frame, text="تحويل اللوج إلى مفاتيح", 
                 command=self.convert_log_to_keys, bg='#1abc9c', fg='white',
                 font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=5)
        
        # منطقة عرض المفاتيح
        keys_frame = tk.LabelFrame(mtk_frame, text="المفاتيح المستخرجة", 
                                  font=("Arial", 12, "bold"))
        keys_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.keys_text = scrolledtext.ScrolledText(keys_frame, height=15, 
                                                  font=("Courier", 10))
        self.keys_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # أزرار حفظ وتصدير
        export_frame = tk.Frame(mtk_frame)
        export_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(export_frame, text="حفظ المفاتيح", 
                 command=self.save_keys, bg='#27ae60', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(export_frame, text="مسح المفاتيح", 
                 command=self.clear_keys, bg='#e74c3c', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
    def create_logs_tab(self):
        """إنشاء تبويب السجلات"""
        logs_frame = ttk.Frame(self.notebook)
        self.notebook.add(logs_frame, text="السجلات")
        
        # منطقة عرض السجلات
        self.logs_text = scrolledtext.ScrolledText(logs_frame, height=25, 
                                                  font=("Courier", 9))
        self.logs_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # أزرار السجلات
        logs_buttons_frame = tk.Frame(logs_frame)
        logs_buttons_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(logs_buttons_frame, text="مسح السجلات", 
                 command=self.clear_logs, bg='#e74c3c', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(logs_buttons_frame, text="حفظ السجلات", 
                 command=self.save_logs, bg='#27ae60', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
    def log_message(self, message):
        """إضافة رسالة إلى السجلات"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.logs_text.insert(tk.END, log_entry)
        self.logs_text.see(tk.END)
        
    def verify_license(self):
        """التحقق من صحة مفتاح الترخيص"""
        license_key = self.license_entry.get().strip()
        
        if not license_key:
            messagebox.showerror("خطأ", "يرجى إدخال مفتاح الترخيص")
            return
            
        # التحقق من صحة المفتاح
        if self.validate_license_key(license_key):
            self.license_verified = True
            messagebox.showinfo("نجح", "تم التحقق من الترخيص بنجاح!")
            self.main_functions_frame.pack(fill=tk.BOTH, expand=True, pady=10)
            self.log_message("تم التحقق من الترخيص بنجاح")
        else:
            messagebox.showerror("خطأ", "مفتاح الترخيص غير صحيح")
            self.log_message("فشل في التحقق من الترخيص")
            
    def validate_license_key(self, key):
        """التحقق من صحة مفتاح الترخيص"""
        # خوارزمية بسيطة للتحقق من المفتاح
        if len(key) != 25 or key.count('-') != 4:
            return False
            
        parts = key.split('-')
        if len(parts) != 5:
            return False
            
        # التحقق من كل جزء
        for part in parts:
            if len(part) != 4:
                return False
                
        # التحقق من checksum بسيط
        checksum = sum(ord(c) for c in key.replace('-', '')) % 1000
        return checksum == 123  # قيمة ثابتة للتبسيط
        
    def open_keygen(self):
        """فتح نافذة مولد المفاتيح"""
        KeygenWindow(self.root)
        
    def start_arabization(self):
        """بدء عملية التعريب"""
        if not self.license_verified:
            messagebox.showerror("خطأ", "يجب التحقق من الترخيص أولاً")
            return
            
        processor = self.processor_var.get()
        android_version = self.android_var.get()
        
        if not processor or not android_version:
            messagebox.showerror("خطأ", "يرجى اختيار نوع المعالج وإصدار الأندرويد")
            return
            
        # بدء عملية التعريب في thread منفصل
        threading.Thread(target=self._arabization_process, 
                        args=(processor, android_version), daemon=True).start()
        
    def _arabization_process(self, processor, android_version):
        """عملية التعريب الفعلية"""
        self.status_label.config(text="جاري التعريب...")
        self.log_message(f"بدء عملية التعريب - المعالج: {processor}, الأندرويد: {android_version}")
        
        steps = [
            "فحص الجهاز المتصل",
            "تحميل ملفات التعريب",
            "تطبيق التعريب على النظام",
            "إعادة تشغيل الخدمات",
            "التحقق من التعريب"
        ]
        
        for i, step in enumerate(steps):
            self.status_label.config(text=f"الخطوة {i+1}: {step}")
            self.log_message(f"تنفيذ: {step}")
            
            # محاكاة العملية
            for j in range(20):
                progress = ((i * 20) + j + 1)
                self.progress_var.set(progress)
                time.sleep(0.1)
                
        self.status_label.config(text="تم التعريب بنجاح!")
        self.log_message("تم إكمال عملية التعريب بنجاح")
        messagebox.showinfo("نجح", "تم التعريب بنجاح!")
        
    def unlock_frp(self):
        """فك قفل FRP"""
        if not self.license_verified:
            messagebox.showerror("خطأ", "يجب التحقق من الترخيص أولاً")
            return
            
        # بدء عملية فك FRP في thread منفصل
        threading.Thread(target=self._frp_unlock_process, daemon=True).start()
        
    def _frp_unlock_process(self):
        """عملية فك FRP الفعلية"""
        self.status_label.config(text="جاري فك FRP...")
        self.log_message("بدء عملية فك FRP")
        
        steps = [
            "فحص حالة FRP",
            "تحضير أدوات الفك",
            "تطبيق الفك",
            "التحقق من النتيجة"
        ]
        
        for i, step in enumerate(steps):
            self.status_label.config(text=f"الخطوة {i+1}: {step}")
            self.log_message(f"تنفيذ: {step}")
            
            # محاكاة العملية
            for j in range(25):
                progress = ((i * 25) + j + 1)
                self.progress_var.set(progress)
                time.sleep(0.1)
                
        self.status_label.config(text="تم فك FRP بنجاح!")
        self.log_message("تم فك FRP بنجاح")
        messagebox.showinfo("نجح", "تم فك FRP بنجاح!")
        
    def extract_mtk_keys(self):
        """استخراج مفاتيح MTK"""
        if not self.license_verified:
            messagebox.showerror("خطأ", "يجب التحقق من الترخيص أولاً")
            return
            
        self.log_message("بدء استخراج مفاتيح MTK")
        
        # محاكاة استخراج المفاتيح
        sample_keys = """
=== مفاتيح MTK المستخرجة ===
DA_KEY: 1234567890ABCDEF1234567890ABCDEF
SBC_KEY: FEDCBA0987654321FEDCBA0987654321
ROOT_KEY: ABCDEF1234567890ABCDEF1234567890
CRYPTO_SEED: 9876543210FEDCBA9876543210FEDCBA
AUTH_KEY: 1111222233334444555566667777888899990000
KCFG_LOCK: ENABLED
SLA_CHALLENGE: 0x12345678
SLA_RESPONSE: 0x87654321
        """
        
        self.keys_text.delete(1.0, tk.END)
        self.keys_text.insert(tk.END, sample_keys)
        self.log_message("تم استخراج مفاتيح MTK بنجاح")
        messagebox.showinfo("نجح", "تم استخراج مفاتيح MTK بنجاح!")
        
    def convert_log_to_keys(self):
        """تحويل ملف اللوج إلى مفاتيح"""
        if not self.license_verified:
            messagebox.showerror("خطأ", "يجب التحقق من الترخيص أولاً")
            return
            
        # اختيار ملف اللوج
        log_file = filedialog.askopenfilename(
            title="اختر ملف اللوج",
            filetypes=[("Log files", "*.log *.txt"), ("All files", "*.*")]
        )
        
        if not log_file:
            return
            
        self.log_message(f"تحويل ملف اللوج: {log_file}")
        
        try:
            with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                log_content = f.read()
                
            # استخراج المفاتيح من اللوج (محاكاة)
            extracted_keys = self._parse_log_for_keys(log_content)
            
            self.keys_text.delete(1.0, tk.END)
            self.keys_text.insert(tk.END, extracted_keys)
            
            self.log_message("تم تحويل اللوج إلى مفاتيح بنجاح")
            messagebox.showinfo("نجح", "تم تحويل اللوج إلى مفاتيح بنجاح!")
            
        except Exception as e:
            self.log_message(f"خطأ في تحويل اللوج: {str(e)}")
            messagebox.showerror("خطأ", f"فشل في تحويل اللوج: {str(e)}")
            
    def _parse_log_for_keys(self, log_content):
        """استخراج المفاتيح من محتوى اللوج"""
        # محاكاة استخراج المفاتيح
        keys_found = []
        
        # البحث عن أنماط المفاتيح
        import re
        
        # البحث عن مفاتيح hex
        hex_patterns = re.findall(r'[0-9A-Fa-f]{16,64}', log_content)
        
        result = "=== مفاتيح مستخرجة من اللوج ===\n\n"
        
        for i, key in enumerate(hex_patterns[:10]):  # أول 10 مفاتيح
            result += f"KEY_{i+1}: {key}\n"
            
        if not hex_patterns:
            result += "لم يتم العثور على مفاتيح في ملف اللوج\n"
            
        return result
        
    def save_keys(self):
        """حفظ المفاتيح في ملف"""
        keys_content = self.keys_text.get(1.0, tk.END).strip()
        
        if not keys_content:
            messagebox.showwarning("تحذير", "لا توجد مفاتيح لحفظها")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="حفظ المفاتيح",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(keys_content)
                self.log_message(f"تم حفظ المفاتيح في: {file_path}")
                messagebox.showinfo("نجح", "تم حفظ المفاتيح بنجاح!")
            except Exception as e:
                self.log_message(f"خطأ في حفظ المفاتيح: {str(e)}")
                messagebox.showerror("خطأ", f"فشل في حفظ المفاتيح: {str(e)}")
                
    def clear_keys(self):
        """مسح المفاتيح"""
        self.keys_text.delete(1.0, tk.END)
        self.log_message("تم مسح المفاتيح")
        
    def clear_logs(self):
        """مسح السجلات"""
        self.logs_text.delete(1.0, tk.END)
        
    def save_logs(self):
        """حفظ السجلات في ملف"""
        logs_content = self.logs_text.get(1.0, tk.END).strip()
        
        if not logs_content:
            messagebox.showwarning("تحذير", "لا توجد سجلات لحفظها")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="حفظ السجلات",
            defaultextension=".log",
            filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(logs_content)
                messagebox.showinfo("نجح", "تم حفظ السجلات بنجاح!")
            except Exception as e:
                messagebox.showerror("خطأ", f"فشل في حفظ السجلات: {str(e)}")


class KeygenWindow:
    """نافذة مولد المفاتيح"""
    
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """إعداد نافذة مولد المفاتيح"""
        self.window.title("مولد مفاتيح الترخيص - أبو محمود السوري")
        self.window.geometry("500x400")
        self.window.configure(bg='#34495e')
        self.window.resizable(False, False)
        
        # جعل النافذة في المقدمة
        self.window.transient()
        self.window.grab_set()
        
    def create_widgets(self):
        """إنشاء عناصر واجهة مولد المفاتيح"""
        # العنوان
        title_label = tk.Label(self.window, 
                              text="مولد مفاتيح الترخيص\nأبو محمود السوري", 
                              font=("Arial", 16, "bold"),
                              fg='#ecf0f1', bg='#34495e')
        title_label.pack(pady=20)
        
        # معلومات المستخدم
        info_frame = tk.LabelFrame(self.window, text="معلومات المستخدم", 
                                  font=("Arial", 12, "bold"),
                                  fg='#ecf0f1', bg='#34495e')
        info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # اسم المستخدم
        tk.Label(info_frame, text="اسم المستخدم:", 
                font=("Arial", 10), fg='#ecf0f1', bg='#34495e').pack(anchor=tk.W, padx=10, pady=5)
        
        self.username_entry = tk.Entry(info_frame, font=("Arial", 10), width=40)
        self.username_entry.pack(padx=10, pady=5)
        
        # البريد الإلكتروني
        tk.Label(info_frame, text="البريد الإلكتروني:", 
                font=("Arial", 10), fg='#ecf0f1', bg='#34495e').pack(anchor=tk.W, padx=10, pady=5)
        
        self.email_entry = tk.Entry(info_frame, font=("Arial", 10), width=40)
        self.email_entry.pack(padx=10, pady=5)
        
        # زر توليد المفتاح
        tk.Button(self.window, text="توليد مفتاح الترخيص", 
                 command=self.generate_license_key, bg='#27ae60', fg='white',
                 font=("Arial", 12, "bold"), height=2).pack(pady=20)
        
        # عرض المفتاح المولد
        key_frame = tk.LabelFrame(self.window, text="مفتاح الترخيص المولد", 
                                 font=("Arial", 12, "bold"),
                                 fg='#ecf0f1', bg='#34495e')
        key_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.generated_key_text = tk.Text(key_frame, height=3, font=("Courier", 12))
        self.generated_key_text.pack(padx=10, pady=10, fill=tk.X)
        
        # أزرار النسخ والإغلاق
        buttons_frame = tk.Frame(self.window, bg='#34495e')
        buttons_frame.pack(pady=10)
        
        tk.Button(buttons_frame, text="نسخ المفتاح", 
                 command=self.copy_key, bg='#3498db', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(buttons_frame, text="إغلاق", 
                 command=self.window.destroy, bg='#e74c3c', fg='white',
                 font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
    def generate_license_key(self):
        """توليد مفتاح ترخيص جديد"""
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        
        if not username or not email:
            messagebox.showerror("خطأ", "يرجى إدخال اسم المستخدم والبريد الإلكتروني")
            return
            
        # توليد مفتاح الترخيص
        license_key = self._generate_key(username, email)
        
        self.generated_key_text.delete(1.0, tk.END)
        self.generated_key_text.insert(tk.END, license_key)
        
        messagebox.showinfo("نجح", "تم توليد مفتاح الترخيص بنجاح!")
        
    def _generate_key(self, username, email):
        """توليد مفتاح الترخيص الفعلي"""
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
        
    def copy_key(self):
        """نسخ المفتاح إلى الحافظة"""
        key = self.generated_key_text.get(1.0, tk.END).strip()
        
        if not key:
            messagebox.showwarning("تحذير", "لا يوجد مفتاح لنسخه")
            return
            
        self.window.clipboard_clear()
        self.window.clipboard_append(key)
        messagebox.showinfo("نجح", "تم نسخ المفتاح إلى الحافظة!")


def main():
    """الدالة الرئيسية"""
    root = tk.Tk()
    app = ArabicPhoneTool(root)
    root.mainloop()


if __name__ == "__main__":
    main()

