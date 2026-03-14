[app]

title = Colour Catching
package.name = colourcatching
package.domain = org.colourcatching

source.dir = .
source.include_exts = py,png,jpg,jpeg,ogg,wav,mp3,ttf,json

version = 1.0

requirements = python3==3.10.12,kivy==2.3.0,hostpython3==3.10.12,pyjnius==1.5.0,pygame

orientation = landscape

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
