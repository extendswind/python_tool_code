import qrcode


def simpleGenerate():
    img = qrcode.make('Some data here')
    with open("simple1.png", 'wb') as f:
         img.save(f)


def generate(qrString):
     qr = qrcode.QRCode(
         version=1,
         error_correction=qrcode.constants.ERROR_CORRECT_L,
         box_size=20,
         border=1,
     )
     qr.add_data(qrString)
     qr.make(fit=True)
     img = qr.make_image()
     qrFile = qrString + '.png'
     # img = qrcode.make(str)
     with open(qrFile, 'wb') as f:
         img.save(f)
     return qrFile

if __name__ == '__main__':
    simpleGenerate()
    generate("test")
