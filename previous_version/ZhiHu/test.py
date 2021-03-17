__author__= "姜维洋"

import requests
url = "https://zhuanlan.zhihu.com/p/151864354"
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Cache-Control': 'max-age=0',
# 'Cookie': 'SESSIONID=wzsiUD5XnUjXfCDqmUpGB2fcoCjbTbMPiyRN1YqKQgz; JOID=U1gcAU3Kqef8cKkhLMmvOaM7p6k1jui7vgTKT36pn9mcQMhBbVqB4KB2oSMjH1qME86ZRRrZUEfyxS9Ze0mSZDM=; osd=V18SAUPOrun8fq0mIsmhPaQ1p6cxiea7sADNQX6nm96SQMZFalSB7qRxryMtG12CE8CdQhTZXkP1yy9Xf06cZD0=; _zap=b150dafc-e5e7-4331-96eb-a6973d6d13cb; d_c0="ABBQXggifRGPTlyFqHZBn8AbRaDFbOBy5gE=|1593235305"; _ga=GA1.2.1413905039.1593235307; _xsrf=86d5fd94-478e-4755-9d6b-1730f62f237b; _gid=GA1.2.810732245.1594364879; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1594105242,1594364878,1594365701,1594367083; capsion_ticket="2|1:0|10:1594370129|14:capsion_ticket|44:NjRlMjc4NzY0ZWNkNGZhODllYTMzM2U1OTI3ODlkMDk=|8a9c26c43d7beb1458502fb5ef12157ccbaf02038a8c409beadc3bf2ea19c30d"; z_c0="2|1:0|10:1594370161|4:z_c0|92:Mi4xR2twN0NnQUFBQUFBRUZCZUNDSjlFU1lBQUFCZ0FsVk5jWGIxWHdCcmdQTHlrV1VobzNFWkJoZ1lXSEZfR2JjY1N3|b5d82546d25afd95466404bbc91fd76559bca65d22322def264dc743c0311199"; unlock_ticket="ADDnDYj-yQ0mAAAAYAJVTXkvCF_ZmFy7ZWemRLm1k9QbUMAhPK-WSA=="; tst=r; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1594370711; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1594370710|1594370709',
# 'Cookie': 'KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1594370710|1594370709',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-site',
'Sec-Fetch-User': '?1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
resp = requests.get(url=url,headers=headers)
print(resp.url)
print(resp.content.decode("utf-8","ignore"))

