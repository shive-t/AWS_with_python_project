import pyqrcode
qr = input("enter link/variable to be converted to QRCode:\n")
link = pyqrcode.create(qr)
link.png('code.png', scale=10)
