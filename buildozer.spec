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
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET, CAMERA

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact
bin_dir = bin

# -----------------------------------------------------------------------------
# Android specific settings

# Версия Android SDK, под которую собирается приложение
android.api = 33

# Минимальная поддерживаемая версия Android
android.minapi = 24

# Фиксируем стабильную версию NDK
android.ndk = 27.3.13750724

# (list) The android arch to build for
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.androidx = True