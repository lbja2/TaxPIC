import os
from PIL import Image
import base64
import  json
import requests

def img_recongnizer(imageBase64):
    # imageBase64 = '''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'''
    host = 'http://vercode.market.alicloudapi.com'
    path = '/vercode/info'
    appcode = '338569b87b304ea28b16321693100354'
    bodys = {}
    codeType = '5006'
    url = host + path

    bodys['codeType'] = codeType
    bodys['imageBase64'] = imageBase64
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Authorization': ('APPCODE ' + appcode)}
    response = requests.post(url, data=bodys, headers = headers)
    # 根据API的要求，定义相对应的Content-Type
    content = json.loads(response.text)
    # if (content):
    # print(content)
    return content

def pic2base64(pic_name):
    with open(pic_name,'rb') as f:
        base64_code = base64.b64encode(f.read())
    return base64_code

if __name__ == '__main__':

    img_name = '12.png'
    folder = 'D:\\'
    imgPath = os.path.join(folder, img_name)
    img = Image.open(imgPath)
    imgArray = img.load()

    x, y = img.size

    for i in range(y):
        for j in range(x):
            if (imgArray[j, i][0] < 100 and imgArray[j, i][1] < 100 and imgArray[j, i][2] > 200 and (
                    imgArray[j, i][0] + imgArray[j, i][1]) < imgArray[j, i][2]):
                img.putpixel((j, i), (255, 255, 255, 255))
            else:
                pass

    img.save(os.path.join(folder, 'test.png'))

    ImgBase64 = pic2base64(os.path.join(folder, 'test.png'))
    result = img_recongnizer(ImgBase64)

    print(result)
