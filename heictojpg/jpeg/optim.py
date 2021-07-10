from PIL import Image
from io import BytesIO
import os


jpegdir = './' # JPEG形式の写真があるディレクトリ



# コンフィグ
COMPRESS_QUALITY = 20 # 圧縮のクオリティ

# JPEG形式とPNG形式の画像ファイルを用意
files = os.listdir(jpegdir)
files = [i for i in files if 'jpeg' in i]

#############################
#     JPEG形式の圧縮処理     #
#############################
# ファイル名を取得
for jpeg_imgefile in files:
	file_name = os.path.splitext(os.path.basename(jpeg_imgefile))[0]
	with open(jpeg_imgefile, 'rb') as inputfile:
	    # バイナリモードファイルをPILイメージで取得
	    im = Image.open(inputfile)
	    # JPEG形式の圧縮を実行
	    im_io = BytesIO()
	    im.save(im_io, 'JPEG', quality = COMPRESS_QUALITY)
	with open('comp_' + file_name + '.jpg', mode='wb') as outputfile:
	    # 出力ファイル(comp_png_image.png)に書き込み
	    outputfile.write(im_io.getvalue())