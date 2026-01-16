[app]
title = Card Radar
package.name = cardradar
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# الصلاحيات اللازمة
android.permissions = CAMERA

orientation = portrait
fullscreen = 1

# تحديد المعمارية المناسبة لأغلب الجوالات
android.archs = armeabi-v7a

# (إضافة مهمة) تحديد إصدارات أدوات الأندرويد
android.api = 31
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
