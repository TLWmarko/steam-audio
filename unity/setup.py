#
# Copyright (c) Valve Corporation. All rights reserved.
#

import os
import shutil
import urllib2
import zipfile

version = "2.0-beta.12"

def download_file(url):
    remote_file = urllib2.urlopen(url)
    with open(os.path.basename(url), "wb") as local_file:
        while True:
            data = remote_file.read(1024)
            if not data:
                break
            local_file.write(data)

print "Downloading Steam Audio SDK v" + version + "..."
url = "https://github.com/ValveSoftware/steam-audio/releases/download/v" + version + "/steamaudio_api_" + version + ".zip"
download_file(url)

print "Extracting steamaudio_api_" + version + ".zip..."
with zipfile.ZipFile(os.path.basename(url), "r") as zip:
	zip.extractall()

print "Copying files..."
shutil.copy("steamaudio_api/bin/Windows/x86/phonon.dll", "src/project/SteamAudioUnity/Assets/Plugins/x86")
shutil.copy("steamaudio_api/bin/Windows/x64/phonon.dll", "src/project/SteamAudioUnity/Assets/Plugins/x86_64")
shutil.copy("steamaudio_api/lib/Linux/x86/libphonon.so", "src/project/SteamAudioUnity/Assets/Plugins/x86")
shutil.copy("steamaudio_api/lib/Linux/x64/libphonon.so", "src/project/SteamAudioUnity/Assets/Plugins/x86_64")
try:
	shutil.rmtree("src/project/SteamAudioUnity/Assets/Plugins/phonon.bundle")
except:
	pass
shutil.copytree("steamaudio_api/bin/OSX/phonon.bundle",  "src/project/SteamAudioUnity/Assets/Plugins/phonon.bundle")
shutil.copy("steamaudio_api/lib/Android/libphonon.so",   "src/project/SteamAudioUnity/Assets/Plugins/android")

print "Cleaning up..."
shutil.rmtree("steamaudio_api")