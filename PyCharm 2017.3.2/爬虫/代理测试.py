import requests
import pymysql
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

list_ip =[
    'http://1.197.203.11:9999',
    'http://175.42.128.246:9999',
    'http://175.42.122.188:9999',
    'http://175.44.109.246:9999',
    'http://123.163.121.90:9999',
    'http://175.42.122.152:9999',
    'http://123.149.136.203:9999',
    'http://175.42.129.34:9999',
    'http://115.218.215.20:9000',
    'http://61.130.181.231:20195',
    'http://120.198.76.45:41443',
    'http://123.55.101.73:9999',
    'http://123.101.231.18.73:9999',
    'http://125.110.69.229:9000',
    'http://110.243.25.64:9999',
    'http://183.166.138.203:9999',
    'http://125.108.104.192:9000',
    'http://118.113.246.122:9000',
    'http://110.243.25.64:9999',
    'http://125.108.98.146:9000',
    'http://36.248.132.176:9999',
    'http://123.149.141.45:9999',
    'http://175.44.109.35:9999',
    'http://175.42.129.94:9999',
    'http://123.55.106.188:9999',
    'http://123.55.106.158:9999',
    'http://125.110.83.60:9000',
    'http://60.168.80.255:1133',
    'http://171.35.223.85:9999',
    'http://115.218.211.41:9000',
    'http://125.108.88.40:9000'
]
# for i in list_ip:
response = requests.get('https://www.baidu.com',proxies={'http':'http://163.125.158.248:8888'},headers=headers)
# response = requests.get('https://www.baidu.com',proxies={'http':i},headers=headers)
print(response)

# con = pymysql.connect(host='localhost', user='root', password='123456', database='pachong', port=3306,
#                       charset='utf8')
# # 创建游标
# cur = con.cursor()

# for i in list_ip:
#     cur.execute('insert into ip value(0,%s)',[i])
#     # 提交
#     con.commit()
#

# ce = cur.execute('select ip_port from ip')
# print(cur.fetchone())
#
# cur.close()
# con.close()
# di = ('http://1.198.73.130:9999',)
# print(''.join(list(di)))