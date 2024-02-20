#command prompt -> pip install qrcode
#command prompt -> pip install Pillow (image)
import qrcode
from PIL import Image


# QR variable
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)


# variable where we read URL
data="https://github.com/KarmaFaber"
qr.add_data(data)
qr.make(fit=True)

# variable imagen
img=qr.make_image(fill_color="#1D1A39", black_color="white").convert('RGB')


# Logo image path
imagenLogo=r'D:\Programación_2024\Python_2024\QR_Python\ver_1.0\logo_GH.png'
logo=Image.open(imagenLogo)


# Calculate logo position
qr_img_size=img.size
logo_position = ((qr_img_size[0] - logo.size[0]) // 2, (qr_img_size[0] - logo.size[0]) // 2)

# Paste the logo onto the QR code
img.paste(logo, logo_position)

# Save the final image
img.save('prueba_1.png')