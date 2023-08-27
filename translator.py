from utils.AuthV3Util import addAuthParams
import json
import requests
from filter import TextFilter
import random
import hashlib
import os

# 您的应用ID
APP_KEY = os.environ.get("app_key")
# 您的应用密钥
APP_SECRET = os.environ.get("app_secret")

class YoudaoTranslator(object):
    def __init__(self, app_key=APP_KEY, app_secret=APP_SECRET):
        self.app_key = app_key
        self.app_secret = app_secret
        self.text_filter = TextFilter()

    def filter_translation(self, translation_result):
        translation_result['Standard Translation'] = [self.text_filter.filter_text(text) for text in
                                                      translation_result['Standard Translation']]
        translation_result['Web Translation'] = [self.text_filter.filter_text(text) for text in
                                                 translation_result['Web Translation']]
        return translation_result

    def handle_error(self, response_content):
        if response_content.get("errorCode") != "0":
            return {"error": "Translation failed", "details": response_content}
        return None

    def translate(self, q):
        lang_from = 'zh-CHS'
        lang_to = 'en'
        data = {'q': q, 'from': lang_from, 'to': lang_to}
        addAuthParams(self.app_key, self.app_secret, data)
        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        try:
            res = doCall('https://openapi.youdao.com/api', header, data, 'post')
            response_content = json.loads(res.content.decode('utf-8'))

            error_response = self.handle_error(response_content)
            if error_response:
                return error_response

            # 以下部分用于生成 Alfred 需要的数据格式
            alfred_items = []

            standard_translation = response_content.get("translation", [])
            if standard_translation:
                alfred_items.append({
                    "type": "default",
                    "title": standard_translation[0],
                    "subtitle": f"标准翻译=>{q}",
                    "arg": standard_translation[0]
                })

            web_translation = response_content.get("web", [])
            for item in web_translation:
                values = item.get("value", [])
                for value in values:
                    alfred_items.append({
                        "type": "default",
                        "title": value,
                        "subtitle": f"网络翻译=>{item['key']}",
                        "arg": value
                    })

            result = {"items": alfred_items}
            return result

        except Exception as e:
            return {
                "error": "API Call Failed",
                "details": str(e)
            }


def addAuthParams(appKey, appSecret, data):
    salt = str(random.randint(1, 65536))
    sign_str = appKey + data['q'] + salt + appSecret
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    data['appKey'] = appKey
    data['salt'] = salt
    data['sign'] = sign

def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, headers=header, data=params)


def main():
    pass


if __name__ == "__main__":
    main()