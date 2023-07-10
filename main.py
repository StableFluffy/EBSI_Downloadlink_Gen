from lxml import etree
import requests
import re

URL = "https://www.ebsi.co.kr/ebs/xip/xipc/previousPaperListAjax.ajax"
STARTPAGE = 1
PAGES = 14

print("[")

c_header = {
    'referer' : 'https://www.ebsi.co.kr/ebs/    xip/xipc/previousPaperList.ebs?targetCd=D100',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36' 
}

def req(pagecount):

    c_data = {
        'targetCd': 'D300',
        'monthList': '03,02,04,05,06,07,09,10,11,12',
        'sort': 'recent',
        'pageSize': '50',
        'beginYear': '2016',
        'endYear': '2023',
        'subjList': '1',
        'currentPage': pagecount
    }

    r = requests.post(URL, headers = c_header, data = c_data)
    t_v = r.text
    #print(t_v)
    tree = etree.HTML(t_v)
    t_path = (tree.xpath('//*[@id="pagingForm"]/div[2]/ul/li'))
    print(len(t_path))
    for btn_data in t_path:
        parsed = ((etree.HTML(etree.tostring(btn_data, method='html', encoding='unicode'))).xpath('/html/body/li/div[3]/div[1]')[0])
        parsed_str = (etree.tostring(parsed, method='html', encoding='unicode'))
        try:

            print(((re.findall(r"goDownLoadP.+?;", parsed_str)[0])[12:-2]).split(',')[0][1:-1])
            print(((re.findall(r"goDownLoadJ.+?;", parsed_str)[0])[12:-2]).split(',')[0][1:-1])
        except:
            None

    
    hits_n = re.findall(r"paperOn.+?;", t_v)
    #print(hits_n)
    hits_a = re.findall(r"goDownLoadP.+?pdf", t_v)

    hits_b = re.findall(r"goDownLoadH.+?pdf", t_v)
    #for c in range(len(hits_n)):
    #    print("{")
    #    print('"ym" : "' + (hits_a[c].split("'")[1])[1:7] + '",')
    #    print('"fullname" : "' + hits_n[c].split(",")[1] + '",')
    #    print('"munlink" : "' + hits_a[c].split("'")[1] + '",')
    #    print('"hsjlink" : "' + hits_b[c].split("'")[1] + '"')
    #    print("},")
    #for hit in hits_n:
    #    print(hit.split(",")[1])
    #hits_a = re.findall(r"goDownLoadP.+?pdf", t_v)
    #for hit in hits_a:
    #    print(hit.split("'")[1])
    #hits_b = re.findall(r"goDownLoadH.+?pdf", t_v)
    #for hit in hits_b:
    #    print(hit.split("'")[1])

for i in range(PAGES - STARTPAGE + 1):
    req(i + STARTPAGE)

print("]")
