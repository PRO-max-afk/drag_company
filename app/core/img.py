import os
import sys

class AssetManager:
    """مدیریت مسیر و بارگذاری فایل‌های تصویری از پوشه assets"""

    def __init__(self):
        self.base_path = self.get_base_path()
        self.assets_dir = os.path.join(self.base_path, "assets")

    def get_base_path(self):
        """بررسی مسیر درست برای حالت اجرا و حالت build (PyInstaller)"""
        try:
            if hasattr(sys, "_MEIPASS"):
                # حالت بسته‌شده توسط PyInstaller
                return sys._MEIPASS
            else:
                # مسیر پروژه در حالت عادی
                return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        except Exception as e:
            print(f"❌ خطا در تشخیص مسیر پایه: {e}")
            return os.path.abspath(".")

    def get_asset_path(self, filename: str) -> str | None:
        """دریافت مسیر مطلق فایل داخل پوشه assets"""
        try:
            image_path = os.path.join(self.assets_dir, filename)

            if os.path.exists(image_path):
                return image_path
            else:
                print(f"⚠ فایل یافت نشد: {image_path}")
                return None
        except Exception as e:
            print(f"❌ خطا در دریافت مسیر تصویر: {e}")
            return None

    def list_assets(self) -> list[str]:
        """لیست تمام فایل‌های موجود در پوشه assets"""
        try:
            if not os.path.exists(self.assets_dir):
                print(f"⚠ پوشه assets یافت نشد: {self.assets_dir}")
                return []

            files = [
                f for f in os.listdir(self.assets_dir)
                if os.path.isfile(os.path.join(self.assets_dir, f))
            ]
            return files
        except Exception as e:
            print(f"❌ خطا در فهرست‌گیری فایل‌ها: {e}")
            return []

