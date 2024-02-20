
#command prompt -> pip install qrcode
#command prompt -> pip install Pillow (image)
import qrcode


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
#ERROR_CORRECT_L-About 7% or less errors can be corrected.
#ERROR_CORRECT_M-(default)-About 15% or less errors can be corrected.
#ERROR_CORRECT_Q-About 25% or less errors can be corrected.
#ERROR_CORRECT_H-About 30% or less errors can be corrected.

data="https://github.com/KarmaFaber"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="#0077B5", black_color="white")
img.save("created_QR_code_01.png")