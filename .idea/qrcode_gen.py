import pyqrcode
qr = input("enter link/variable to be converted to QRCode:\n")
url = pyqrcode.create(qr)
print(url.terminal(quiet_zone=1))