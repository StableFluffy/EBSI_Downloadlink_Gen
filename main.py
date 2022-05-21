import requests
import re

URL = "https://www.ebsi.co.kr/ebs/xip/xipc/previousPaperListAjax.ajax"
PAGES = 4

c_header = {
    'referer' : 'https://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs?targetCd=D300',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' 
}

def req_eng(pagecount):


    c_data = {
        'targetCd': 'D100',
        'monthList': '03,02,04,05,06,07,09,10,11,12',
        'subjList': '3',
        'sort': 'recent',
        #'paperId',
        #'paperNo',
        #'lvl',
        'beginYear': '2016',
        'endYear': '2022',
        'subj': '3',
        'currentPage': pagecount
    }

    r = requests.post(URL, headers = c_header, data = c_data)
    t_v = r.text

    hits = re.findall(r"goDownLoadP.+?pdf", t_v)
    for hit in hits:
        print("https://wdown.ebsi.co.kr/W61001/01exam" + hit.split("'")[1])

for i in range(PAGES):
    req_eng(i + 1)
