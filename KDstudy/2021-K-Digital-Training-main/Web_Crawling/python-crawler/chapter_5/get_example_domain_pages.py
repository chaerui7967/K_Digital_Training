import time

import requests

PAGE_URL_LIST = [
    'http://example.com/1.page',
    'http://example.com/2.page',
    'http://example.com/3.page',
]

for page_url in PAGE_URL_LIST:
    res = requests.get(page_url, timeout=30)
    print(
        "페이지 URL: " + page_url + ", " + \
        "HTTP 상태: " + str(res.status_code) + ", " + \
        "처리 시간(초): " + str(res.elapsed.total_seconds())
    )
    time.sleep(1)
