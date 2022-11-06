import pyqrcode
import boto3
import random
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%m%d%Y%H%M%S")
filename="code"+date_time+".png"
qr = input("enter link/variable to be converted to QRCode:\n")
link = pyqrcode.create(qr)
link.png(filename, scale=10)
s3 = boto3.resource('s3')
response = s3.meta.client.upload_file(filename, 'qrcode-storage',filename)
