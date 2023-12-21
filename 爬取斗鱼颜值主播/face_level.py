# @ Time    : 2019/2/28 14:46
# @ Author  : JuRan
from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID = '15648537'
API_KEY = 'sq3nrjYPjoxGKpsATXy6OGqm'
SECRET_KEY = 'IhFs8fRGy9fKqoGbv65jBsc0fUX8DDAM'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face(filepath):

    with open(filepath, "rb") as f:
        data = base64.b64encode(f.read())

    # image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"
    # 将字节转换成字符串
    image = data.decode()

    imageType = "BASE64"
    options = {}
    options["face_field"] = "beauty"

    """ 调用人脸检测 """
    result = client.detect(image, imageType,options)
    # print(result)
    try:
        if result['result']:
            # print(result['result']['face_list'][0]['beauty'])
            return str(result['result']['face_list'][0]['beauty']) + "分"
        else:
            return None
    except Exception as e:
        pass


beauty = face('./image/刚刚好女孩.png')
print(beauty)