[app]

# (str) Title of your application
title = porikol

# (str) Package name
package.name = porikol

# (str) Package domain (needed for android packaging)
package.domain = org.porikol

# (str) Source code where the main.py lives
source.dir = .

# (str) Entry point of your application (указываем ваш файл porikol.py)
source.main_filename = porikol.py

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact
bin_dir = bin

# -----------------------------------------------------------------------------
# Android specific settings

# Стабильная комбинация для GitHub Actions
android.api = 31
android.minapi = 21
android.accept_sdk_licenses = True

# НДК и архитектура под простое приложение
android.ndk = 27.3.13750724
android.archs = arm64-v8a
android.androidx = True