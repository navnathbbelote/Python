import qrcode as qr
img = qr.make("Hello QR")
img.save("navqrcode.png")
