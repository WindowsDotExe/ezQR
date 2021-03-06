# This is a very simple QR code generator program.
# A QR code is generated in the current director with the information provided.-

import qrcode
from PIL import Image

def generate():
    '''
    Generates a QR code based on text (str) input.
    .jpg image created in directory of execution.
    '''
    url = input('Enter text to generate a QR code: ')
    file = input('Enter the file for the QR code or press enter for default ("qr.jpg"): ')

    if file == '':  # Enter key was pressed; default filename
        file = 'qr.jpg'

    try:    
        img = qrcode.make(url)
        img.save(file)
        img.show(Image.open(file))  # Comment this line out if you don't want the file to automatically open
        print('QR code successfully generated (' + file + ').')

    except qrcode.exceptions.DataOverflowError:
        print('ERROR: You have entered too many characters.')

    except:
        print('An unknown error occured.')


generate()