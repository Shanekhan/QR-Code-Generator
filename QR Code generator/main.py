import qrcode

data = input("Enter the url:").strip()
filename = input("Enter the file name:").strip() + ".png"

qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"QR code save as {filename}")