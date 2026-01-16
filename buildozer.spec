[app]
title = Card Radar
package.name = cardradar
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

android.permissions = CAMERA
orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a

# نترك هذه القيم فارغة ليختار السيرفر أفضل نسخة تلقائياً
android.api = 31
android.minapi = 21
android.ndk_path = 
android.sdk_path = 

[buildozer]
log_level = 2
warn_on_root = 1
