from tornado.httpclient import AsyncHTTPClient


async def asynchronous_fetch(url):
    http_clinet = AsyncHTTPClient()
    response = await http_clinet.fetch(url)
    return response.body


print(asynchronous_fetch("http://www.baidu.com"))
