# Python_OCR_API
Based on PaddleOCR

1. 不仅仅支持本地OCR服务，还可以部署于外网服务器或者云服务器

2. 支持的语言：中文、英文、日文、韩文

3. 环境安装：
pip install paddleocr
pip install web.py
pip install --upgrade google-api-python-client
pip install paddlepaddle
其它缺什么装什么
if you are installing the CPU version of Paddle, use pip install paddlepaddle==2.0.0rc1
The machine does not support avx, you can try: pip install paddlepaddle-gpu==2.0.2 -f https://paddlepaddle.org.cn/whl/stable/noavx.html

https://stackoverflow.com/questions/71348433/modulenotfounderror-no-module-named-paddle-fluid-core-noavx

4. 建议本地post时不要用http://0.0.0.0:5689，替换为http://127.0.0.1:5689，如部署服务器或其它机器，改为http://本机ip:5689即可。

5. 使用代码实例: 开启服务后，我们仅需将图片的base64编码post给指定url即可。post时需要传入两个参数。详细见req.py
 
