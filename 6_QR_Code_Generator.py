import qrcode
data = "https://chatgpt.com/"
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)
qr.add_data(data)
qr.make(fit=False)
img = qr.make_image(fill_color="red", back_color="black")
img.save("chatgpt_qr.png")
img.show()