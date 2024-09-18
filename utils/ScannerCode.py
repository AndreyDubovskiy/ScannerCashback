from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image

def get_code_from_bytes_image(bytes_image):
    try:
        img = Image.open(BytesIO(bytes_image))
        tmp = decode(img)
        for i in tmp:
            print(i.data)
            print("str", str(i.data, 'utf-8'))
            return str(i.data, 'utf-8')
        return None
    except:
        return None