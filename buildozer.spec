[app]
title = Mis Notas Honor
package.name = notaspro
package.domain = org.tuusuario
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# CONFIGURACIÓN CORREGIDA
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
# Eliminamos la línea android.sdk que daba WARNING
android.build_tools_version = 33.0.0
android.archs = arm64-v8a
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 0
