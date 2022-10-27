# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: ocr_web.py
import os, web, base64, json
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from paddleocr import PaddleOCR, draw_ocr
ocr_japan = PaddleOCR(use_angle_cls=True, use_gpu=False, lang='japan')
ocr_chinese = PaddleOCR(use_angle_cls=True, use_gpu=False, lang='ch')
ocr_en = PaddleOCR(use_angle_cls=True, use_gpu=False, lang='en')
ocr_korean = PaddleOCR(use_angle_cls=True, use_gpu=False, lang='korean')
urls = ('/(.*)', 'hello')
app = web.application(urls, globals())

class hello:

    def GET(self, name):
        web_test_get = web.input()
        return web_test_get.name

    def POST(img, lan):
        i = web.input()
        if not 'img' not in str(i.keys()):
            if 'lan' not in str(i.keys()):
                return json.dumps({'RetCode':0,  'Message':'参数缺失'}, sort_keys=True, indent=4, ensure_ascii=False, separators=(',',
                                                                                                                              ': '))
            image_base64 = i.img
            lan = i.lan
            if lan == 'ch':
                ocr = ocr_chinese
        elif lan == 'japan':
            ocr = ocr_japan
        else:
            if lan == 'en':
                ocr = ocr_en
            else:
                if lan == 'korean':
                    ocr = ocr_korean
                else:
                    return json.dumps({'RetCode':0,  'Message':'不正确的lan参数，中文为ch，英文为en，日文为japan，韩文为korean'}, sort_keys=True, indent=4, ensure_ascii=False, separators=(',',
                                                                                                                                                                      ': '))
        try:
            image_dat = base64.b64decode(image_base64)
        except:
            return json.dumps({'RetCode':0,  'Message':'未能成功解析图片base64编码'}, sort_keys=True, indent=4,
              ensure_ascii=False,
              separators=(',', ': '))
        else:
            with open('temp.png', 'wb') as (f):
                f.write(image_dat)
            result = ocr.ocr('temp.png', cls=True)
            results = []
            for line in result:
                re_ep = str(line)
                epc = re_ep.split("('")[1].split("', 0.")[0]
                results.append(epc)
            else:
                dic_re = {}
                dic_re['RetCode'] = 0
                dic_re['Message'] = 'Success'
                Result_dic = {}
                words_arr = []
                for ite_index, ite in enumerate(results):
                    words_arr.append(ite)
                #else:
                    dic_re['Result'] = {'Words': words_arr}
                    data2 = json.dumps(dic_re, sort_keys=True, indent=4, ensure_ascii=False, separators=(',',
                                                                                                         ': '))
                    return result


class MyApplication(web.application):

    def run(self, port=8080, *middleware):
        func = (self.wsgifunc)(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


if __name__ == '__main__':
    app = MyApplication(urls, globals())
    app.run(port=5689)
# okay decompiling ocr_web.pyc
#pip install paddleocr
#pip install web.py
#pip install --upgrade google-api-python-client
#pip3 install paddlepaddle paddleocr