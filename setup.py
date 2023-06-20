import sys
import os
from cx_Freeze import setup, Executable

# Đường dẫn tới file script.py
script = r"E:\TOOL\craw data\main.py"

# Các thư viện được sử dụng trong chương trình
includes = ["PyQt6","sys","selenium","time","MySQLdb","os","urllib.parse",]


# Cấu hình cho cx_Freeze
options = {
    'build_exe': {
        'includes': includes,
    }
}
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Sử dụng Win32GUI để ẩn cửa sổ terminal trên Windows

# Thiết lập thông tin chương trình
setup(
    name="MyProgram",
    version="1.0",
    description="Description ssss",
    options=options,
    executables=[Executable(script,base=base)]
)
