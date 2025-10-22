import os
import sys
from PyQt6.QtGui import QFontDatabase


class FontLoader:
    def __init__(self):
        """بارگذاری خودکار تمام فونت‌ها از فولدر fonts"""
        self.base_path = self.get_base_path()
        self.fonts_dir = os.path.join(self.base_path, "fonts")
        self.font_ids = []

    def get_base_path(self):
        """بررسی مسیر درست در حالت عادی و حالت PyInstaller"""
        try:
            if hasattr(sys, '_MEIPASS'):
                return sys._MEIPASS
            else:
                # مسیر دایرکتوری اصلی پروژه (که شامل app/ و fonts/ است)
                return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        except Exception as e:
            print(f"❌ خطا در تشخیص مسیر پایه: {e}")
            return os.path.abspath(".")

    def load_all_fonts(self):
        """تمام فونت‌های موجود در فولدر fonts را بارگذاری می‌کند"""
        if not os.path.exists(self.fonts_dir):
            print(f"⚠ پوشه فونت یافت نشد: {self.fonts_dir}")
            return

        for filename in os.listdir(self.fonts_dir):
            if filename.lower().endswith((".ttf", ".otf")):
                font_path = os.path.join(self.fonts_dir, filename)
                font_id = QFontDatabase.addApplicationFont(font_path)
                if font_id != -1:
                    self.font_ids.append(font_id)
                   # print(f"✅ فونت بارگذاری شد: {filename}")
                else:
                    print(f"⚠ فونت بارگذاری نشد: {filename}")

    def get_font_families(self):
        """نام خانواده فونت‌های بارگذاری شده را برمی‌گرداند"""
        families = []
        for fid in self.font_ids:
            families.extend(QFontDatabase.applicationFontFamilies(fid))
        return families