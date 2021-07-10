import os
import subprocess

heicdir = './heic/' # HEIC形式の写真があるディレクトリ
jpegdir = './jpeg/' # JPEG形式の写真があるディレクトリ
files = os.listdir(heicdir)
i = 1

for f in files:
        cmd = 'sips --setProperty format jpeg ' + heicdir + f + ' --out ' + jpegdir + 'photo-' + str(i) + '.jpeg'
        subprocess.call(cmd, shell=True)
        i+=1
