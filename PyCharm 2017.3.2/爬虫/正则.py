import re

# ret = re.match('baidu','baidu.com')
# print(ret)
#
# # 显示匹配字符
# print(ret.group())

# ret = re.match('.','1561')
# print(ret.group())
#
# ret = re.match('a','abcdc123')
# print(ret.group())

# ret = re.match('秦时明月','秦时明月，汉时关。万里长征人未还。')
# print(ret.group())
#
# ret = re.match('\d*','123')
# print(ret.group())
# *代表0个或多个
# +代表1个或多个

# match = re.match('[a-zA-Z][a-z]*[\d]+', 'asd123')
# print(match.group())
#
# ？可有可无
# match = re.match('[1-9]?[0-9]', '09')
# print(match.group())

# {}匹配个数
# match = re.match('\w{8,20}','13654as1cd55s1')
# match = re.match('\w{8,20}','13654as1cd55s1')
# match = re.match('\w{8,20}','13654as1cd55s1')
# print(match.group())

# $以...结尾
# match = re.match('[\w]{4,20}@126\.com$','as567@126.com')
# print(match.group())

# match = re.match('\D','@@globle')
# print(match.group())

# ^以....开头
# match = re.match('[\d]{1,3}','666')
# print(match.group())
#
# match = re.match('[1]?[\d]?[\d]','123')
# print(match.group())

# match = re.match('[1-9]?[0-9]$|100','100')
# print(match.group())

match = re.match('[\w]{4,20}@(163|126|qq)\.com$','12366@qq.com')
print(match.group())
print(match.group(1))

match = re.findall('[\w]{4,20}@(163|126|qq)\.com$','156312@126.com')
print(match)