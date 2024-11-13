import requests
# 请求头
headers = {
    # 用户身份信息

    'cookie' : 'SINAGLOBAL=6106999949683.298.1720859058565; SCF=Ar85hp8WEeP8ZzZ6ooo-rY4AhuEQ-y1jycJjvvtQEmxGthV0hv3AGAXc4tH2mLTcfYwfRvx0f8Vos9VgCCHRlKQ.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhvMyXZR6Ka4CBR04wKBwiT5JpX5KMhUgL.Fo2f1hz01hzRSoM2dJLoIpjLxK-LBo5L12qLxKBLBo.LBKqLxK.L1-BL1--t; UOR=,,www.bilibili.com; ULV=1731239059646:5:2:1:1751567089880.6367.1731239059644:1730819601422; XSRF-TOKEN=-ANBjv61Bdd-E82acvKCyRG8; ALF=1734017503; SUB=_2A25KNwSPDeRhGedL41AS-CzEzTuIHXVpTRhHrDV8PUJbkNAbLVXnkW1NVJIQ25JNYCmFUXjmSDi_U4y6Lm73YbJG; WBPSESS=H5FBZFu4iVsdM7yQwgSmd59nIuk_rX3lgie7rfPxlQmbf6sQB6GD0H5ghEJe01tif_fSt8GCMhqv12by7mMhPvB7t6MdqBSlhtqFCX4zKN9eC7cxyu100F5voI_kijZlpD494_ogKA9RQIW-kThWvQ==',
    # 防盗链
    'referer' : 'https://weibo.com/6603105502/OFA88dIP6',
    # 浏览器基本信息
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
url = 'https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id=5099103363270568&is_show_bulletin=2&is_mix=0&count=10&uid=6603105502&fetch_level=0&locale=zh-CN'
# 1.发送请求
response = requests.get(url=url,headers=headers)
# 2.打印网页数据
# 定义一个json_data来存储 response.json()的数据
json_data = response.json()
# 定义一个data_list取出所有data中的数据
data_list = json_data['data']
# 定义一个data数据，让它便利data_list里面的对象
# 这里怎么理解呢，data_list看作一个数组，我让data等于数组的第一个数
# 然后执行操作，执行完之后返回for，我们再另data等于数组的第二个数执行操作
# 循环往复
for data in data_list:
    # 这里 data 代表着 data_list的第一个数也就是 ['data'][0]
    text_raw = data['text_raw']
    print(text_raw)