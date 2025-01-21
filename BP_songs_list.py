'''
#找到歌词：

import requests
import json
# 引用requests,json模块

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers = {
    'referer':'https://y.qq.com/portal/search.html',
    # 请求来源
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 标记了请求从什么设备，什么浏览器上发出
    }

for x in range(5):

    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.lyric_next',
    'searchid':'94267071827046963',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'sem':'1',
    't':'7',
    'p':str(x+1),
    'n':'10',
    'w':'周杰伦',
    'g_tk':'1714057807',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'  
    }

    res = requests.get(url, headers = headers, params = params)
    #下载该网页，赋值给res
    jsonres = json.loads(res.text)
    #使用json来解析res.text
    list_lyric = jsonres['data']['lyric']['list']
    #一层一层地取字典，获取歌词的列表

    for lyric in list_lyric:
    #lyric是一个列表，x是它里面的元素
        print(lyric['content'])
    #以content为键，查找歌词
'''

'''
import requests

# 使用headers是一种习惯
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 建立一个空列表，以待写入数据
articlelist=[]
# 设置offset的起始值为第一页的值：10
offset=10

while True:
    # 封装参数
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'10',
        'sort_by':'voteups',
        }
    # 发送请求，并把响应内容赋值到变量res里面
    res=requests.get(url,headers=headers,params=params)
    # 确认这个response对象状态正确 
    print(res.status_code)
    # 如果响应成功，继续
    if int(res.status_code) == 200:
        # 用json()方法去解析response对象
        articles=res.json()
        # 定位数据
        data=articles['data']
    
        for i in data:
            # 把数据封装成列表
            list1=[i['title'],i['url'],i['excerpt']]
            articlelist.append(list1) 
        # 在while循环内部，offset的值每次增加20
        offset=offset+20 
        if offset>30:
            break
        # 如果offset大于30，即爬了两页，就停止
        # ——————另一种思路实现———————————————— 
        # 如果键is_end所对应的值是True，就结束while循环。
        #if articles['paging']['is_end'] == True:
            #break
        # ————————————————————————————————————
#打印看看
print(articlelist)
'''

'''
#完整爬虫（获取数据 提取数据 解析数据 储存数据）：

import requests
import openpyxl

wb = openpyxl.Workbook()  
#创建工作簿  （对象）
sheet = wb.active 
#获取工作簿的活动表   （工作表）
sheet.title = 'restaurants' 
#工作表重命名

sheet['A1'] = '歌曲名'     #加表头，给A1单元格赋值
sheet['B1'] = '所属专辑'   #加表头，给B1单元格赋值
sheet['C1'] = '播放时长'   #加表头，给C1单元格赋值
sheet['D1'] = '播放链接'   #加表头，给D1单元格赋值

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': 'BLACKPINK',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(url, params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        name = music['name']
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name']
        # 查找专辑名，把专辑名赋给album
        time = music['interval']
        # 查找播放时长，把时长赋值给time
        link = 'https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html\n\n'
        # 查找播放链接，把链接赋值给link
        sheet.append([name,album,time,link])
        # 把name、album、time和link写成列表，用append函数多行写入Excel
        print('歌曲名：' + name + '\n' + '所属专辑:' + album +'\n' + '播放时长:' + str(time) + '\n' + '播放链接:'+ link)
        
wb.save('BLACKPINK.xlsx')            
#最后保存并命名这个Excel文件
'''
