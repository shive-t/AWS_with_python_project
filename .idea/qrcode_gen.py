#!/usr/bin/python3
import pyqrcode
import boto3
import random
num=random.randint(0,1000)
filename="code"+str(num)+".png"
qr = input("enter link/variable to be converted to QRCode:\n")
link = pyqrcode.create(qr)
link.png(filename, scale=10)
s3 = boto3.resource('s3')
response = s3.meta.client.upload_file(filename, 'qrcode-storage',filename)
