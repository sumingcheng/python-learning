# upload.py
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import base64
import time
import json

with open('env.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)

# 配置信息
config = CosConfig(
    Region='ap-shanghai',
    SecretId=data.SecretId,
    SecretKey=data.SecretKey,
)
client = CosS3Client(config)


def upload_image(base64_str, filename):
    # 解码 Base64 图片
    decoded_image = base64.b64decode(base64_str)

    time_file = f'SD_Photo_Output/{str(int(time.time()))}-{filename}'

    # 上传图片
    try:
        response = client.put_object(
            Bucket='mikacat-ai-1302339726',
            Body=decoded_image,
            Key=time_file,
            EnableMD5=False,
        )
        # 如果没有抛出异常，打印成功消息
        print('对象存储上传成功.')
    except Exception as e:
        # 如果抛出异常，打印错误消息
        print(f'对象存储上传异常: {e}')

    url = f'mikacat-ai-1302339726.cos.ap-shanghai.myqcloud.com/{time_file}'
    return url


# 将图片转换为Base64编码
with open("gogogo.png", "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')

res = upload_image(base64_string, 'git.png')
print(res)
