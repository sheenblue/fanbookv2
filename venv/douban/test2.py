import requests

url = "https://notetocard.com/"

payload={}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.2.1842135751.1654778166; Hm_lvt_a6854964b4affe369e0c033fe896b517=1659253725; Hm_lpvt_a6854964b4affe369e0c033fe896b517=1659253725; JSESSIONID=6E8C2DC93F94E900D00144B81CE19B91',
  'If-Modified-Since': 'Sat, 30 Jul 2022 11:11:32 GMT',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response)
