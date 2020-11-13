# coding=utf-8
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '85.0.4183.83 Safari/537.36'
}

bookname = input('输入书名：')

# url = 'https://www.biquge5200.cc/modules/article/search.php?'

# ret = requests.get(url=url,params={'searchkey':bookname},headers=headers).text
# print(ret)
#
# print(ret)

html = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/小说.py"
输入书名：大主宰
<!doctype html>
<html>
<head>
<title>笔趣阁_书友最值得收藏的网络小说阅读网</title>
<meta name="keywords" content=",好看的,2014排行榜" />
<meta name="description" content="笔趣阁是广大书友最值得收藏的网络小说阅读网，笔趣阁网站收录了当前最火热的网络小说，笔趣阁5200免费提供高质量的小说最新章节，是广大网络小说爱好者必备的小说阅读网。" />
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta content="always" name="referrer"/>
<link rel="stylesheet" type="text/css" href="//www.biquge5200.cc/images/biquge.css"/>
<script src="//apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>
<script src="//apps.bdimg.com/libs/jquery.cookie/1.4.1/jquery.cookie.min.js" type="text/javascript"></script>
<script type="text/javascript" src="//www.biquge5200.cc/images/bqg.js?v=200302"></script>
<style>p{font-size:13px;line-height:2}</style>
</head>
<body>
<div id="wrapper">
		<script>login();</script>
		<div class="header">
			<div class="header_logo">
				<a href="//www.biquge5200.cc">笔趣阁</a>
			</div>
			<script>bqg_panel();</script>
		</div>
		<div class="nav">
			<ul>
				<li><a href="//www.biquge5200.cc/">首页</a></li>
				<li><a rel="nofollow" href="/home/">我的书架</a></li>
				<li><a href="//www.biquge5200.cc/xuanhuanxiaoshuo/">玄幻小说</a></li>
				<li><a href="//www.biquge5200.cc/xiuzhenxiaoshuo/">修真小说</a></li>
				<li><a href="//www.biquge5200.cc/dushixiaoshuo/">都市小说</a></li>
				<li><a href="//www.biquge5200.cc/chuanyuexiaoshuo/">穿越小说</a></li>
				<li><a href="//www.biquge5200.cc/wangyouxiaoshuo/">网游小说</a></li>
				<li><a href="//www.biquge5200.cc/kehuanxiaoshuo/">科幻小说</a></li>
				<li><a href="//www.biquge5200.cc/yanqingxiaoshuo/">言情小说</a></li>
				<li><a href="//www.biquge5200.cc/tongrenxiaoshuo/">同人小说</a></li>
			</ul>
		</div>
		
        <div id="main"><div id="hotcontent"><script type="text/javascript">list();</script>
   
     
<table class="grid" width="100%" align="center">
<caption>搜索结果</caption>
  <tr align="center">
    <th width="20%">文章名称</th>
    <th width="40%">最新章节</th>
    <th width="15%">作者</th>
	<th width="9%">字数</th>
    <th width="10%">更新</th>
    <th width="6%">状态</th>
  </tr>
  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/57_57544/">大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/57_57544/140224011.html" target="_blank"> 第十三章公平交易!</a></td>
    <td class="odd">寂寞香烟</td>
	<td class="even">54K</td>
    <td class="odd" align="center">2017-02-16</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/0_7/">大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/0_7/167373115.html" target="_blank"> 第一千三十二章 七阳截天杖</a></td>
    <td class="odd">天蚕土豆</td>
	<td class="even">8569K</td>
    <td class="odd" align="center">2019-07-05</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/13_13898/">主宰大宇宙</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/13_13898/5960411.html" target="_blank"> 第二百三十五章 时间奥义</a></td>
    <td class="odd">中原大飞</td>
	<td class="even">1387K</td>
    <td class="odd" align="center">2016-01-30</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/30_30184/">大主宰外传</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/30_30184/11841827.html" target="_blank"> 爱你如痴如醉。</a></td>
    <td class="odd">老茶坊</td>
	<td class="even">30K</td>
    <td class="odd" align="center">2016-01-30</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/7_7046/">傲世大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/7_7046/6354116.html" target="_blank"> 第二百九十三章 扫灭天穹</a></td>
    <td class="odd">丰居</td>
	<td class="even">1738K</td>
    <td class="odd" align="center">2016-01-30</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/48_48249/">魔道大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/48_48249/19249110.html" target="_blank"> 上架感言</a></td>
    <td class="odd">花无语</td>
	<td class="even">199K</td>
    <td class="odd" align="center">2016-10-01</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/3_3874/">隋唐大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/3_3874/139127592.html" target="_blank"> 099归程（六）</a></td>
    <td class="odd">最爱吃菜花</td>
	<td class="even">3617K</td>
    <td class="odd" align="center">2016-12-24</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/53_53432/">大宇宙主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/53_53432/139520444.html" target="_blank"> 第144章 华夏震动 （创世《宇宙大至尊》）</a></td>
    <td class="odd">宇宙神火</td>
	<td class="even">188K</td>
    <td class="odd" align="center">2017-01-09</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/40_40427/">星河大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/40_40427/141916116.html" target="_blank"> 问路的人</a></td>
    <td class="odd">凡尘以荒.CS</td>
	<td class="even">55K</td>
    <td class="odd" align="center">2017-03-14</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/66_66754/">异世大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/66_66754/143212946.html" target="_blank"> 通告通告</a></td>
    <td class="odd">凝沧海</td>
	<td class="even">125K</td>
    <td class="odd" align="center">2017-03-20</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/43_43604/">异世大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/43_43604/146575294.html" target="_blank"> 通告通告</a></td>
    <td class="odd">逆沧海.CS</td>
	<td class="even">125K</td>
    <td class="odd" align="center">2017-06-02</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/38_38767/">星河大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/38_38767/146603394.html" target="_blank"> 问路的人</a></td>
    <td class="odd">凡尘以荒</td>
	<td class="even">2K</td>
    <td class="odd" align="center">2017-06-02</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/78_78829/">文娱大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/78_78829/148668725.html" target="_blank"> 新书已发</a></td>
    <td class="odd">羽林都督</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2017-09-11</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/83_83674/">九州大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/83_83674/151404933.html" target="_blank"> 今天无更</a></td>
    <td class="odd">绿色植物油</td>
	<td class="even">148K</td>
    <td class="odd" align="center">2018-01-12</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/53_53777/">命运大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/53_53777/153341633.html" target="_blank"> 第两百二十章 云深不知处</a></td>
    <td class="odd">谷长城</td>
	<td class="even">800K</td>
    <td class="odd" align="center">2018-03-31</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/77_77628/">武林大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/77_77628/155644251.html" target="_blank"> 第五百二十二章·天道融武书结局（大结局）</a></td>
    <td class="odd">修之名</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2018-08-31</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/46_46871/">命运大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/46_46871/155695627.html" target="_blank"> 第两百二十章 云深不知处 新</a></td>
    <td class="odd">高卧南阳</td>
	<td class="even">443K</td>
    <td class="odd" align="center">2018-09-07</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/40_40832/">命运大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/40_40832/155711685.html" target="_blank"> 第两百二十章 云深不知处 新</a></td>
    <td class="odd">沈子国主.CS</td>
	<td class="even">242K</td>
    <td class="odd" align="center">2018-09-07</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/35_35334/">命运大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/35_35334/155713627.html" target="_blank"> 第两百二十章 云深不知处 新</a></td>
    <td class="odd">沈子国主</td>
	<td class="even">115K</td>
    <td class="odd" align="center">2018-09-07</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/57_57287/">次元大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/57_57287/158000307.html" target="_blank"> 嗯，耗时很久，开了新的号写了新书。</a></td>
    <td class="odd">逍墨白</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2018-09-19</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/111_111648/">都市大主宰系统</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/111_111648/162008196.html" target="_blank"> 第169章 奇果</a></td>
    <td class="odd">风火江南</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2019-01-16</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/120_120667/">万道大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/120_120667/167681520.html" target="_blank"> 第802章 与坤家对赌！</a></td>
    <td class="odd">清十依</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2019-07-17</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/116_116991/">太古大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/116_116991/167686268.html" target="_blank"> 第三百五十三章 连续</a></td>
    <td class="odd">青蓝西瓜</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2019-07-17</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/97_97979/">这个大佬是主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/97_97979/155455972.html" target="_blank"> 第十七章.网络时刻</a></td>
    <td class="odd">长弓水圣</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2018-08-14</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/103_103476/">三国之大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/103_103476/158688940.html" target="_blank"> 第一百四十二章 南华慈宗</a></td>
    <td class="odd">曾经的名字</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2018-10-02</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/85_85470/">大主宰之归零</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/85_85470/162605163.html" target="_blank"> 第十九章 战争前奏 新</a></td>
    <td class="odd">寻爱橘子</td>
	<td class="even">49K</td>
    <td class="odd" align="center">2019-02-14</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/118_118091/">我真是大主宰</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/118_118091/165088569.html" target="_blank"> 新书已发布。</a></td>
    <td class="odd">任九天</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2019-04-23</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/68_68925/">万界大主宰系统</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/68_68925/152015510.html" target="_blank"> 452 玄冰阁</a></td>
    <td class="odd">本微末凡尘</td>
	<td class="even">167K</td>
    <td class="odd" align="center">2020-08-16</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/90_90816/">穿越大主宰之任我遨游</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/90_90816/153241944.html" target="_blank"> 章节变动 ，再解释一遍！</a></td>
    <td class="odd">君笑仙尘</td>
	<td class="even">67K</td>
    <td class="odd" align="center">2018-03-28</td>
    <td class="even" align="center">连载中</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/98_98391/">大主宰之牧尘穿越以后</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/98_98391/155529102.html" target="_blank"> 第三十三章 谁才是大主宰</a></td>
    <td class="odd">睡树上的青蛙</td>
	<td class="even">67K</td>
    <td class="odd" align="center">2018-08-21</td>
    <td class="even" align="center">此书已完成</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/86_86838/">大主宰之慕白逆袭</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/86_86838/167298339.html" target="_blank"> 第四百八十二章 极限斗罗之陨</a></td>
    <td class="odd">陆书宇</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2019-07-02</td>
    <td class="even" align="center">连载</td>
  </tr>

  <tr>
    <td class="odd"><a href="https://www.biquge5200.cc/134_134372/">从大主宰开始打卡</a></td>
    <td class="even"><a href="https://www.biquge5200.cc/134_134372/172660061.html" target="_blank"> 第219章 结局</a></td>
    <td class="odd">秋老虎123</td>
	<td class="even">0K</td>
    <td class="odd" align="center">2020-06-16</td>
    <td class="even" align="center">连载</td>
  </tr>

</table>
        </div>

		</div>
<div class="footer">
			<div class="footer_link"></div>
			<div class="footer_cont">
				<script>footer();right();dl();</script>
			</div>
		</div>
	</div>
<script charset="gbk" src="//www.baidu.com/js/opensug.js"></script>
<script type="text/javascript">
	var params = {
	"XOffset":0, //提示框位置横向偏移量,单位px
	"YOffset":0, //提示框位置纵向偏移量,单位px
	"width":204, //提示框宽度，单位px
	"fontColor":"#000", //提示框文字颜色
	"fontColorHI":"#FFF",	//提示框高亮选择时文字颜色
	"fontSize":"14px",		//文字大小
	"fontFamily":"宋体",	//文字字体
	"borderColor":"gray", 	//提示框的边框颜色
	"bgcolorHI":"#03c",		//提示框高亮选择的颜色
	"sugSubmit":false		//在选择提示词条是是否提交表单
	};
 	BaiduSuggestion.bind("wd",params,search);
</script>

</div>
</body>
</html>

Process finished with exit code 0

'''
html_doc = etree.HTML(html)
a = html_doc.xpath("//td/a/@href")[2]
# ret = requests.get(a,headers).text
# print(ret)
html1 = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/小说.py"
<!doctype html>
<html>
<head>
<title>大主宰无弹窗_大主宰最新章节列表_大主宰5200_笔趣阁</title>
<meta name="keywords" content="大主宰,大主宰最新章节,大主宰无弹窗" />
<meta name="description" content="大主宰无弹窗最新章节由网友提供，《大主宰》情节跌宕起伏、扣人心弦，是一本情节与文笔俱佳的玄幻小说，笔趣阁5200免费提供大主宰最新清爽干净的文字章节在线阅读。" />
<meta http-equiv="Content-Type" content="text/html; charset=gbk" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<meta http-equiv="Cache-Control" content="no-transform" />
<meta content="always" name="referrer"/>
<link rel="stylesheet" type="text/css" href="//www.biquge5200.cc/images/biquge.css"/>
<script src="//apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>
<script src="//apps.bdimg.com/libs/jquery.cookie/1.4.1/jquery.cookie.min.js" type="text/javascript"></script>
<script type="text/javascript" src="//www.biquge5200.cc/images/bqg.js?v=200302"></script>
<style>p{font-size:13px;line-height:2}</style>
<meta http-equiv="mobile-agent" content="format=html5; url=https://m.biquge5200.cc/info-7/" />
<meta http-equiv="mobile-agent" content="format=xhtml; url=https://m.biquge5200.cc/info-7/" />
<script language="javascript" type="text/javascript">var bookid = "7"; var booktitle = "大主宰";var novelId="7";var refId="24027";</script>
<script type="text/javascript">uaredirect("https://m.biquge5200.cc/info-7/");</script>
<meta property="og:type" content="novel"/>
<meta property="og:title" content="大主宰"/>
<meta property="og:description" content="其实接下来的新书，在斗破完结时便已经是有了构想，只不过却并未立即开始写，因为那个世界太过的宏伟浩大，所以，我再写了一本武动，来作为其基石。斗破大结局时，萧炎所去的新世界，与林动最终去往的神秘世界，是相同的，因为那个神秘的大世界，便是我们新书开始的地方。当初并不太认为自己有驾驭那个世界的能力，而现在，终归是可以开始了。"/>
<meta property="og:image" content="http://r.m.biquge5200.cc/files/article/image/0/7/7s.jpg"/>
<meta property="og:novel:category" content="玄幻小说"/>
<meta property="og:novel:author" content="天蚕土豆"/>
<meta property="og:novel:book_name" content="大主宰"/>
<meta property="og:novel:read_url" content="https://www.biquge5200.cc/0_7/"/>
<meta property="og:novel:status" content="连载中"/>
<meta property="og:novel:author_link" content="//www.biquge5200.cc/modules/article/search.php?searchkey=辰东"/>
<meta property="og:novel:update_time" content="2016-01-28 18:31"/>
<meta property="og:novel:latest_chapter_url" content="https://www.biquge5200.cc/0_7/167373115.htm"/>
<meta property="og:novel:latest_chapter_name" content="第一千三十二章 七阳截天杖"/>
</head>
<body>
<div id="wrapper">
		<script>login();</script>
		<div class="header">
			<div class="header_logo">
				<a href="//www.biquge5200.cc">笔趣阁</a>
			</div>
			<script>bqg_panel();</script>
		</div>
		<div class="nav">
			<ul>
				<li><a href="//www.biquge5200.cc/">首页</a></li>
				<li><a rel="nofollow" href="/home/">我的书架</a></li>
				<li><a href="//www.biquge5200.cc/xuanhuanxiaoshuo/">玄幻小说</a></li>
				<li><a href="//www.biquge5200.cc/xiuzhenxiaoshuo/">修真小说</a></li>
				<li><a href="//www.biquge5200.cc/dushixiaoshuo/">都市小说</a></li>
				<li><a href="//www.biquge5200.cc/chuanyuexiaoshuo/">穿越小说</a></li>
				<li><a href="//www.biquge5200.cc/wangyouxiaoshuo/">网游小说</a></li>
				<li><a href="//www.biquge5200.cc/kehuanxiaoshuo/">科幻小说</a></li>
				<li><a href="//www.biquge5200.cc/yanqingxiaoshuo/">言情小说</a></li>
				<li><a href="//www.biquge5200.cc/tongrenxiaoshuo/">同人小说</a></li>
			</ul>
		</div>
<div class="dahengfu"><script>list();</script></div>
<div class="box_con">
			<div class="con_top">
				<div id="bdshare" class="bdshare_b" style="line-height: 12px;"><img src="http://bdimg.share.baidu.com/static/images/type-button-7.jpg" /><a class="shareCount"></a></div>
				<a href="/">笔趣阁</a> &gt; <a href="/xuanhuanxiaoshuo/">玄幻小说</a>  &gt; 大主宰最新章节列表
			</div>
			<div id="maininfo">
				<div id="info">
					<h1>大主宰</h1>
					<p style="width:200px">作&nbsp;&nbsp;&nbsp;&nbsp;者：天蚕土豆</p>
					<p style="width:500px">动作：<a href="javascript:download('大主宰');">TXT下载</a>, <a href="javascript:pl('7', '2046');">加入书架</a>,  <a href="javascript:nu('7');">更新提醒</a>,  <a href="javascript:tj('1', '7');">投推荐票</a>,  <a href="#footer">直达底部</a></p>
					<p>最后更新：2019-07-05</p>
				</div>
				<div id="intro">
					<p>其实接下来的新书，在斗破完结时便已经是有了构想，只不过却并未立即开始写，因为那个世界太过的宏伟浩大，所以，我再写了一本武动，来作为其基石。斗破大结局时，萧炎所去的新世界，与林动最终去往的神秘世界，是相同的，因为那个神秘的大世界，便是我们新书开始的地方。当初并不太认为自己有驾驭那个世界的能力，而现在，终归是可以开始了。</p>
				</div>
			</div>
			<div id="sidebar">
				<div id="fmimg"><img alt="" src="http://r.m.biquge5200.cc/files/article/image/0/7/7s.jpg" width="120" height="150"><span class="b"></span></div>
			</div> 
			<div id="listtj">&nbsp;推荐阅读：
				<a href='/97_97123/' style='font-weight:bold'>三寸人间</a>
				<a href='/76_76490/' >牧神记</a>
				<a href='/86_86700/' style='font-weight:bold'>伏天氏</a>
				<a href='/78_78387/' >汉乡</a>
				<a href='/0_111/' >武炼巅峰</a>
				<a href='/79_79883/' style='font-weight:bold'>元尊</a>
				<a href='/79_79875/' >飞剑问道</a>
				<a href='/8_8165/' style='font-weight:bold'>至尊剑皇</a>
				<a href='/121_121229/' >前任无双</a>
				<a href='/130_130510/' >超品命师</a>
				<a href='/51_51253/' style='font-weight:bold'>透视小医神</a>
				<a href='/0_554/' style='font-weight:bold'>混沌剑神</a>
			</div>
		</div>
		<div style="width:910px;margin:0px auto;" id="cstad"><table id="cstad"><tr>
			<td id="adt1"><script type="text/javascript">cad1();</script></td>
			<td id="adt2"><script type="text/javascript">cad2();</script></td>
			<td id="adt3"><script type="text/javascript">cad3();</script></td>
			</tr></table>
		</div>
        <script>dingbu();</script>    
		<div class="box_con">
			<div id="list">
				<dl>
					<dt><b>《大主宰》最新章节</b>（提示：已启用缓存技术，最新章节可能会延时显示，登录书架即可实时查看。）</dt><dd><a href='https://www.biquge5200.cc/0_7/167373115.html' >第一千三十二章 七阳截天杖</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373113.html' >第一千三十章  激战</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373111.html' >第一千零五章 牧尘出手</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373106.html' >第九百三十四章 强大的灵傀</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373102.html' >第九百三十一章 秘藏中心</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373100.html' >第八百九十章 咫尺之遥</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373096.html' >第七百四十二章 龙争虎斗</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167373092.html' >第四百六十一章 强势镇压</a></dd><dd><a href='https://www.biquge5200.cc/0_7/167372433.html' >千言万语，汇成一句感谢。</a></dd>
								<dt>《大主宰》正文</dt>
                    
                        <dd><a href="https://www.biquge5200.cc/0_7/2046.html">武动乾坤结局感言以及新书</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2047.html">第一章 北灵院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2048.html">第二章 被踢出灵路的少年</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2049.html">第三章 牧域</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2050.html">第四章 大浮屠诀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2051.html">第五章 大千世界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2052.html">第六章 灵力增幅</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2053.html">第七章 慕元</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2054.html">第八章 柳阳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2055.html">第九章 对恃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2056.html">第十章 院试</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2057.html">第十一章 谭青山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2058.html">第十二章 出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2059.html">第十三章 战柳阳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2060.html">第十四章 灵动境中期</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2061.html">第十五章 破灵珠</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2062.html">第十六章 天届</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2063.html">第十七章 三级聚灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2064.html">第十八章 筑基</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2065.html">第十九章 森罗死印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2066.html">第二十章 成印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2067.html">第二十一章 训练场风波</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2068.html">第二十二章 死印之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2069.html">第二十三章 森罗死印的真正力量</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2070.html">第二十四章 约定</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2071.html">第二十五章 灵兽精魄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2072.html">第二十六章 老练的猎手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2073.html">第二十七章 抢劫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2074.html">第二十八章 合作</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2075.html">第二十九章 玉灵树</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2076.html">第三十章 山谷猎猿（求收藏！）</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2077.html">第三十一章 驱虎吞狼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2078.html">第三十二章 分赃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2079.html">第三十三章 回营【求收藏，求推荐！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2081.html">第三十四章 柳暝（第三章，求收藏！）</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2082.html">第三十五章 第二道森罗死印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2083.html">第三十六章 麻烦</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2084.html">第三十七章 下套</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2085.html">第三十八章 反杀【求收藏！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2086.html">第三十九章 芥子镯</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2087.html">第四十章 成绩</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2089.html">第四十一章 作弊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2090.html">第四十二章 堵截</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2091.html">第四十三章 雨中人纪宗【求收藏！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2092.html">第四十四章 破阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2093.html">第四十五章 九幽雀【求收藏！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2094.html">第四十六章 封印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2095.html">第四十七章 灵阵【求收藏！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2096.html">第四十七章 天赋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2097.html">第四十九章 行动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2098.html">第五十章 黑冥渊【求收藏，求推荐！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2099.html">第五十一章 噬灵蜂</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2100.html">第五十二章 灵虫笛</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2101.html">第五十三章 对碰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2102.html">第五十四章 黑毒沼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2103.html">第五十五章 办法【求收藏！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2104.html">第五十六章 狠手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2105.html">第五十七章 借势</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2106.html">第五十八章 引蜂【求收藏！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2107.html">第五十九章 抵达</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2108.html">第六十章 怪岩</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2109.html">第六十一章 神秘黑蛋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2110.html">第六十二章 异变</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2111.html">第六十三章 黑神雷云</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2112.html">第六十四章 进化</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2113.html">第六十五章 自爆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2114.html">第六十六章 体内的变故</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2115.html">我的第四本书要上架了，请大家内详。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2116.html">第六十七章 一页黑纸镇灵雀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2117.html">第六十八章 火炎灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2118.html">热血尚在否？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2119.html">第六十九章 二级聚灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2120.html">第七十章 参与</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2121.html">第七十一章 联合布阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2122.html">第七十二章 心阵状态</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2123.html">第七十三章 种子名额</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2124.html">第七十四章 陈帆，霍云</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2125.html">第七十五章 灵诀室第三层</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2126.html">第七十六章 两部灵诀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2127.html">第七十七章 苦训</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2128.html">第七十八章 化形</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2129.html">第七十九章 成效</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2130.html">第八十章 神魄境的陪练</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2131.html">第八十一章 名额争夺战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2132.html">第八十二章 完虐</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2133.html">第八十三章 名额之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2134.html">第八十四章 龙争虎斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2135.html">第八十五章 底牌层出</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2136.html">第八十六章 胜负</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2137.html">第八十七章 挑选灵院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2138.html">第八十八章 结果</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2139.html">第八十九章 谈判失败</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2140.html">第九十章 邙阴山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2141.html">第九十一章 说服</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2142.html">第九十二章 联手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2143.html">第九十三章 血拼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2144.html">第九十四章 九天雷灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2145.html">第九十五章 黑色卷轴</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2146.html">第九十六章 压制与突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2147.html">第九十七章 灵轮境后期</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2148.html">第九十八章 不安的平静</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2150.html">第九十九章 九域大会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2151.html">第一百章 柳惊山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2152.html">第一百零一章 融天境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2153.html">第一百零二章 交易</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2154.html">第一百零三章 借用力量</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2155.html">第一百零四章 大战柳惊山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2156.html">第一百零五章 三级灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2157.html">第一百零六章 妖莲屠灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2158.html">第一百零七章 斩杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2159.html">第一百零八章 落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2160.html">第一百零九章 恢复</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2161.html">第一百一十章 离开【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2162.html">第一百一十一章 北苍界【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2163.html">第一百一十二章 黑裙少女【第四更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2164.html">第一百一十三章 被盯上</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2165.html">第一百一十四章 杀鸡儆猴</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2166.html">第一百一十五章 第三道森罗死印【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2167.html">第一百一十六章 笋儿【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2168.html">第一百一十七章 三人行【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2169.html">第一百一十八章 叶轻灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2170.html">第一百一十九章 葛海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2171.html">第一百二十章 血祸者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2172.html">战！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2173.html">第一百二十一章 曾经，现在，依旧强大</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2174.html">第一百二十二章 条件</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2175.html">第一百二十三章 夺宝【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2176.html">第一百二十四章 金轮裂灵阵【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2177.html">第一百二十五章 神魄阴阳芝【第四更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2178.html">第一百二十六章 神魄境！【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2179.html">第一百二十七章 碾压【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2180.html">第一百二十八章 战利品【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2181.html">第一百二十九章 消息传开</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2183.html">第一百三十章 龙象阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2184.html">第一百三十一章 楚麒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2185.html">第一百三十二章 碧眼金晶兽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2186.html">再战吧！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2187.html">第一百三十三章 金刚浮屠手【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2188.html">第一百三十四章 冰玄灵蛟【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2189.html">第一百三十五章 阵容【三百票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2191.html">第一百三十六章 万人斩冰蛟【六百票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2192.html">第一百三十七章 地心炎龙蜥【九百票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2193.html">我们同样也累，但没人会放弃。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2194.html">第一百三十八章 夺取【一千两百票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2195.html">第一百三十九章 大追杀【1500票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2196.html">第一百四十章 体内变故</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2197.html">第一百四十一章 血脉链接</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2199.html">第一百四十二章 相见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2200.html">第一百四十三章 解决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2201.html">第一百四十四章 龙象阵之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2202.html">第一百四十五章 旧敌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2203.html">第一百四十六章 聚集点</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2204.html">第一百四十七章 石家兄弟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2206.html">第一百四十八章 战石惊天【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2207.html">第一百四十九章 黑炎【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2208.html">第一百五十章 北苍殿【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2209.html">第一百五十一章 最后的挑战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2210.html">第一百五十二章 安然</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2212.html">第一百五十二章 安然【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2213.html">第一百五十三章 新生的反扑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2214.html">第一百五十四章 灵雀镇冰鹰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2215.html">第一百五十五章 北苍灵院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2217.html">第一百五十六章 杨弘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2218.html">第一百五十七章 论灵值的重要性</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2219.html">第一百五十八章 灵值殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2220.html">第一百五十九章 冲击神魄榜【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2221.html">第一百六十章 神魄榜第三【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2222.html">第一百六十一章 神魄丹 【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2224.html">第一百六十二章 陌轮</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2225.html">第一百六十三章 雷域突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2226.html">第一百六十四章 吾来掌玄黄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2227.html">第一百六十五章 浮屠塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2228.html">第一百六十六章 封堵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2229.html">第一百六十七章 陌轮</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2230.html">第一百六十八章 浮屠塔之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2232.html">第一百六十九章 社团【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2233.html">第一百七十章 作弊【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2234.html">第一百七十一章 洛神会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2235.html">第一百七十二章 切磋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2236.html">第一百七十三章 天榜第二，李玄通</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2237.html">第一百七十四章 对恃【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2238.html">第一百七十五章 新生大会【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2239.html">第一百七十六章 北灵山【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2240.html">第一百七十七章 冲击山顶【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2241.html">第一百七十八章 石台【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2242.html">第一百七十九章 山巅</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2243.html">第一百八十章 杨弘真正的力量</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2244.html">第一百八十一章 牧尘战杨弘【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2245.html">第一百八十二章 大炎魔之阵【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2246.html">第一百八十三章 九幽现【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2247.html">第一百八十四章 血脉链接的力量【第四更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2248.html">第一百八十五章 黑塔镇虎蛟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2249.html">第一百八十六章 谁是新生第一？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2250.html">第一百八十七章 交谈【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2251.html">第一百八十八章 灵力融合【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2252.html">第一百八十九章 第一</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2253.html">第一百九十章 苏萱，鹤妖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2254.html">第一百九十一章 灵诀殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2255.html">第一百九十二章 挑选灵诀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2256.html">第一百九十三章 四神星宿经</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2257.html">第一百九十四章 镇守者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2258.html">第一百九十五章 取巧</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2260.html">第一百九十六章 六级聚灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2261.html">第一百九十七章 湖底潜修</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2262.html">第一百九十八章 苏灵儿【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2263.html">第一百九十五章 新老神魄第一的交手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2264.html">第两百章 手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2265.html">第两百零一章 突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2266.html">第两百零二章 融天境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2268.html">第两百零三章 霍风</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2269.html">第两百零四章 交锋【第四更!】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2270.html">第两百零五章 天灵莲【第五更!】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2271.html">第两百零六章 徐青青【第一更!】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2272.html">第两百零七章 九级浮屠塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2273.html">第两百零八章 夺取灵莲子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2274.html">第两百零九章 天榜高手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2275.html">第两百一十章 修炼神诀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2276.html">第两百一十一章 感悟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2277.html">第两百一十二章 两巴掌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2278.html">请读者们看看。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2279.html">第两百一十三章 两强【第四更!】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2280.html">第两百一十四章 邀战【第一更!】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2281.html">第两百一十五章 灵斗场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2282.html">第两百一十六章 三招之约</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2283.html">第两百一十七章 新生第一vs天榜第二【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2284.html">第两百一十八章 四神星宿经vs天玄神诀【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2285.html">第两百一十九章 换我来进攻【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2286.html">第两百二十章 妖莲再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2287.html">第两百二十一章 洛神族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2288.html">第两百二十二章 西天界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2289.html">第两百二十四章 炎帝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2290.html">第两百二十五章 天级任务</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2291.html">第两百二十六章 灵藏</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2292.html">第两百二十七章 北苍大陆【第一更】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2293.html">第两百二十八章 白龙城【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2294.html">第三更正在写之中。、</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2295.html">第两百二十九章 灵阵子【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2297.html">第两百三十章 白龙玉柱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2298.html">第两百三十一章 竞争</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2299.html">第两百三十二章 白轩【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2300.html">第两百三十三章 白龙之丘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2301.html">第两百三十四章 夜袭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2302.html">第两百三十五章 反杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2303.html">第两百三十六章 一个不留</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2304.html">第两百三十七章 龙魔宫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2305.html">第两百三十八章 狮虎团</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2306.html">第两百三十九章 灵藏出世</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2307.html">第两百四十章 火炎灵莲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2308.html">第两百四十一章 遭遇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2309.html">第两百四十二章 火灵仙莲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2310.html">第两百四十三章 炼化莲子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2311.html">第两百四十四章 突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2312.html">第两百四十五章 龙蛟灵环</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2313.html">第两百四十六章 双龙镇压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2314.html">第两百四十七章 交换</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2315.html">第两百四十八章 石像守卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2316.html">第两百四十九章 黑色盆地</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2317.html">第两百五十章 石像之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2318.html">第两百五十一章 逼出</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2319.html">第两百五十二章 至尊现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2320.html">第两百五十三章 黑龙与白龙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2321.html">第两百五十四章 重水灵珠</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2322.html">第两百五十五章 黑色魔柱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2323.html">第两百五十六章 白轩的真正实力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2324.html">第两百五十七章 空间破碎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2325.html">第两百二十八章 太古凶器</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2326.html">第两百五十九章 镇压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2327.html">第两百六十章 不会死</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2328.html">第两百六十一章 凶煞之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2329.html">第两百六十二章 惨烈 血斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2330.html">第两百六十三章 援兵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2331.html">第两百六十四章 沈苍生</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2333.html">第两百六十五章 归院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2334.html">第两百六十六章 交接任务</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2335.html">第两百六十七章 车轮</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2336.html">第两百六十八章 准备</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2337.html">第两百六十九章 登门【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2338.html">第两百七十章 十道灵阵【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2339.html">第两百七十一章 灵阵围妖门【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2340.html">第两百七十二章 接阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2342.html">第两百七十三章 十阵之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2343.html">第两百七十四章 隐藏</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2344.html">第两百七十五章 再入雷域</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2345.html">第两百七十六章 雷域第七层</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2346.html">第两百七十七章 破解封印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2347.html">第两百七十八章 域外邪族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2348.html">第两百七十九章 准化天境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2349.html">第两百八十章 龙腾术</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2350.html">第两百八十一章 第八层</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2352.html">第两百八十二章 秃头老人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2353.html">第两百八十三章 一招</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2354.html">第两百八十四章 一万三千颗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2355.html">第两百八十五章 精血到手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2356.html">第两百八十六章 黑神雷劫再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2357.html">第两百八十七章 渡劫成功</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2358.html">第两百八十八章 沉睡</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2359.html">第两百八十九章 沸腾</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2360.html">第两百九十章 太苍院长</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2361.html">第两百九十一章 开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2362.html">第两百九十二章 灵光界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2363.html">第两百九十三章 聚集点</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2364.html">第两百九十四章 联手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2365.html">第两百九十五章 剿灭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2366.html">第两百九十六章 独自吃下</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2367.html">第两百九十七章 王家三兄弟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2368.html">第两百九十八章 代价</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2369.html">第两百九十九章 战三王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2370.html">第三百章 雷神体之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2371.html">第三百零一章 极度危险级别</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2372.html">第三百零二章 黑会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2373.html">第三百零三章 营地</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2374.html">第三百零四章 锻器神石</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2375.html">第三百零五章 慕风扬</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2376.html">第三百零六章 抵达</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2377.html">第三百零七章 云集</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2379.html">第三百零八章 灵王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2380.html">第三百零九章 围剿灵王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2381.html">第三百一十章 地底</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2382.html">第三百一十一章 夺取灵晶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2383.html">第三百一十二章 灵王追杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2384.html">第三百一十三章 心眼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2385.html">第三百一十四章 双莲之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2386.html">第三百一十五章 斩杀灵王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2387.html">第三百一十六章 震动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2388.html">第三百一十七章 突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2390.html">第三百一十八章 灵光山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2391.html">第三百一十九章 第三个位置</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2392.html">第三百二十章 激战鹤妖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2393.html">第三百二十一章 鹤神降</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2394.html">第三百二十二章 踢出狩猎场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2395.html">第三百二十三章 压力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2396.html">第三百二十四章 最后一战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2397.html">第三百二十五章 三大将</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2399.html">第三百二十六章 战古天炎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2400.html">第三百二十七章 双阵齐出</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2401.html">第三百二十八章 催动黑神雷</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2402.html">第三百二十九章 血斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2403.html">第三百三十章 胜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2404.html">第三百三十一章 落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2405.html">第三百三十二章 休整</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2406.html">第三百三十三章 新天榜第三</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2408.html">第三百三十四章 刑殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2409.html">第三百三十五章 雷毒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2410.html">第三百三十六章 雷神丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2411.html">第三百三十七章 完整版本的雷神体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2412.html">第三百三十八章 黑神雷毒指</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2413.html">第三百三十九章 潜入雷海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2414.html">第三百四十章 到手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2415.html">第三百四十一章 接受灵光灌顶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2417.html">第三百四十二章 交流会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2418.html">第三百四十三章 柳狰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2419.html">第三百四十四章 一剑之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2420.html">第三百四十五章 血弑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2421.html">第三百四十六章 出现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2422.html">第三百四十七章 朱雀神印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2423.html">第三百四十八章 血神甲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2425.html">第三百四十九章 一拳碎甲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2426.html">第三百五十章</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2427.html">第三百五十一章 灵溪</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2428.html">第三百五十二章 指点</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2429.html">第三百五十三章 破阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2430.html">第三百五十四章 神秘的灵溪</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2431.html">第三百五十五章 灵阵屋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2432.html">第三百五十六章 生死压迫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2433.html">第三百五十七章 画卷</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2434.html">第三百五十八章 关系</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2435.html">第三百五十九章 血鸣钟 【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2436.html">第三百六十章 救援</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2437.html">第三百六十一章 西荒境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2438.html">第三百六十二章 赤鱼与矛将</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2439.html">第三百六十三章 凶悍的情侣档</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2440.html">第三百六十四章 救人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2441.html">第三百六十五章 寻火</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2442.html">第三百六十六章 解毒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2443.html">第三百六十七章 汇聚</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2444.html">第三百六十八章 短兵接触</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2445.html">第三百六十九章 西荒城</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2446.html">第三百七十章 四人对决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2447.html">第三百七十一章 对阵吴甲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2448.html">第三百七十二章 九重山岳阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2449.html">第三百七十三章 心眼破阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2450.html">第三百七十四章 强悍的魔龙子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2451.html">第三百七十五章 底牌层出</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2452.html">第三百七十六章 神鼎炼天阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2453.html">第三百七十七章 化龙血诀 【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2454.html">第三百七十八章 再借凶煞</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2455.html">第三百七十九章 看谁更凶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2456.html">第三百八十章 魔柱之威【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2457.html">第三百八十一章 三大至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2458.html">第三百八十二章 至尊小三难【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2459.html">第三百八十三章 龙魔烙印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2460.html">第三百八十四章 至尊之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2461.html">第三百八十五章 办法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2462.html">第三百八十六章 静姨</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2463.html">第三百八十七章 记忆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2464.html">第三百八十八章 迷茫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2465.html">第三百八十九章 偷灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2466.html">第三百九十章 学长的骄傲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2467.html">第三百九十一章 通天之境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2468.html">第三百九十二章 刑灵战偶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2469.html">第三百九十三章 魔柱再现【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2470.html">第三百九十四章 院长之话</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2471.html">第三百九十五章 北苍门</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2472.html">第三百九十六章 动身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2473.html">第三百九十七章 圣灵城</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2474.html">第三百九十八章 龙蛇混杂</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2475.html">第三百九十九章 魔刑天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2476.html">第四百章 准备</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2477.html">第四百零一章 圣灵山开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2478.html">第四百零二章 来自神秘黑纸的颤动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2479.html">第四百零三章 风暴夺宝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2480.html">第四百零四章 吴峒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2481.html">曾经斗魂，今安在？！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2482.html">第四百零五章 毒指</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2483.html">第四百零六章 断臂</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2484.html">第四百零七章 天至尊之骨</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2485.html">第四百零八章 天至尊精血 【第1000票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2486.html">第四百零九章 至尊法身【第1500票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2487.html">第四百一十章 万古不朽身【第2000票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2488.html">第四百一十一章 九天梯【第2500票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2489.html">还有13更！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2490.html">第四百一十二章 登台【拜求月票！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2491.html">第四百一十三章 资格</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2492.html">第四百一十四章 斗柳影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2493.html">第四百一十五章 震慑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2494.html">第四百一十六章 霸道的魔刑天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2495.html">第四百一十七章 战魔刑天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2496.html">第四百一十八章 倾尽手段【第4000票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2497.html">千言万语，汇成一句感谢。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2498.html">第四百一十九章 魔符【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2499.html">大主宰活动，有美女妹纸唱歌哦~</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2500.html">第四百二十章 孰胜孰败【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2501.html">第四百二十一章 抹杀【第4500票加更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2502.html">拉保底月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2503.html">第四百二十二章 动荡</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2504.html">喝酒喝坏了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2505.html">第四百二十三章 震动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2506.html">第四百二十四章 无量老祖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2507.html">第四百二十五章 完成洗礼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2508.html">第四百二十六章 危机</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2509.html">第四百二十七章 魔柱之力，神剑之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2510.html">第四百二十八章 那道身影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2511.html">第四百二十九章 欺我孩儿【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2512.html">第四百三十章 静姨</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2513.html">第四百三十一章 可怕的实力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2514.html">第四百三十二章 惊退落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2515.html">第四百三十三章 再度分离</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2516.html">第四百三十四章 幽暗空间</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2517.html">第四百三十五章 灭龙魔宫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2518.html">第四百三十六章 灵院大赛的准备</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2519.html">第四百三十七章 四大院的新人【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2520.html">第四百三十八章 北苍门开启 【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2521.html">第四百三十九章 特训【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2522.html">第四百四十章 苦修【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2523.html">第四百四十一章 厚积薄发【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2524.html">第四百四十二章 四纹雷体【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2525.html">第四百四十三章 第一阶段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2526.html">第四百四十四章 心事</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2527.html">第四百四十五章 喜欢 【第一更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2528.html">第四百四十六章 修炼大浮屠诀阴卷【第二更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2529.html">第四百四十七章 再做突破【第三更！】</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2530.html">第四百四十八章 闲暇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2531.html">第四百四十九章 新生入院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2532.html">第四百五十章 有何不敢</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2533.html">第四百五十一章 新老霸主交替</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2534.html">第四百五十二章 故友相见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2535.html">第四百五十三章 规则</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2536.html">第四百五十四章 灵院大赛，开启！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2537.html">第四百五十五章 风云汇聚</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2538.html">第四百五十六章 破碎的遗迹大陆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2539.html">第四百五十七章 排名</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2540.html">第四百五十八章 挑选目标</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2541.html">第四百五十九章 老对头</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2542.html">第四百六十章 邱北海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2543.html">第四百六十一章 强势镇压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2544.html">新年活动。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2545.html">第四百六十二章 雷神之手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2546.html">第四百六十三章 虎口</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2547.html">第四百六十四章 情报</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2548.html">第四百六十五章 遗迹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2549.html">第四百六十六章 四院齐聚</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2550.html">第四百六十七章 唐媚儿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2551.html">第四百六十八章 资格</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2552.html">第四百六十九章 黑暗森林</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2553.html">第四百七十章 魔树</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2554.html">第四百七十一章 补充毒指</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2555.html">第四百七十二章 解救</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2556.html">第四百七十三章 合作</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2557.html">第四百七十四章 仙灵树</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2558.html">第四百七十五章 宫殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2559.html">第四百七十六章 取宝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2560.html">第四百七十七章 木灵院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2561.html">第四百七十八章 主殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2562.html">请假过年。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2563.html">第四百七十九章 万木之界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2564.html">第四百八十章 震慑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2565.html">第四百八十一章 战夏侯</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2566.html">第四百八十二章 星辰大法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2567.html">第四百八十三章 雷威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2568.html">第四百八十四章 恩怨</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2569.html">第四百八十五章 盯上</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2570.html">第四百八十六章 木神卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2571.html">第四百八十七章 联手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2572.html">第四百八十八章 洛神剑莲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2573.html">第四百九十章 扛走</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2574.html">第四百九十一章 战利品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2575.html">第四百九十二章 收获</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2576.html">第四百九十三章 渡肉身难</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2577.html">第四百九十四章 苦难</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2578.html">明日恢复更新，以及以后更新情况。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2580.html">第四百九十五章 来袭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2581.html">第四百九十六章 出关</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2582.html">第四百九十七章 温清璇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2583.html">第四百九十八章 双美</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2584.html">第四百九十九章 血祸者与灵冠者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2585.html">第五百章 合作</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2586.html">第五百零一章 情敌？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2587.html">第五百零二章 血神族再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2588.html">第五百零三章 血天都</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2589.html">第五百零四章 交易镇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2590.html">第五百零五章 灵丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2591.html">第五百零六章 小千剑灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2592.html">第五百零七章 到手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2593.html">第五百零八章 木神山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2594.html">第五百零九章 王钟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2595.html">第五百一十章 武盈盈</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2596.html">第五百一十一章 色胚</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2597.html">第五百一十二章 木神山开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2598.html">第五百一十三章 灵宝山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2599.html">第五百一十四章 陷阱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2600.html">第五百一十五章 规则</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2601.html">第五百一十六章 锐气</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2602.html">第五百一十七章 三重神魄难</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2603.html">第五百一十八章 斗战偶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2604.html">第五百一十九章 天木神轮</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2605.html">第五百二十章 收获</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2606.html">第五百二十一章 盆满钵满</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2607.html">第五百二十二章 藏灵院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2608.html">第五百二十三章 潜行</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2610.html">第五百二十四章 闯入</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2611.html">第五百二十五章秦风</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2612.html">第五百二十六章 你完了</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2613.html">第五百二十七章 玉盘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2614.html">第五百二十八章 温清璇之怒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2616.html">第五百二十九章 院灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2617.html">第五百三十章 继承者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2618.html">第五百三十一章 开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2619.html">第五百三十二章 至尊灵液</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2620.html">第五百三十三章 各施手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2621.html">第五百三十四章 聚灵碗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2622.html">第五百三十五章 暴力震慑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2623.html">第五百三十六章 血影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2624.html">第五百三十七章 木神院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2625.html">第五百三十八章 登山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2626.html">第五百三十九章 雷海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2627.html">第五百四十章 神木罡雷</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2628.html">第五百四十一章 肉身渡雷</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2629.html">第五百四十二章 十件宝贝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2630.html">天府三周年。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2631.html">第五百四十三章 争夺玄龟印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2632.html">第五百四十四章 棘手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2633.html">第五百四十五章 两女</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2634.html">第五百四十六章 两女之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2635.html">第五百四十七章 自爆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2636.html">第五百四十八章 小千灵剑阵之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2637.html">第五百四十九章 凑齐木神碑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2638.html">第五百五十章 分别</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2639.html">第五百五十一章 木神经</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2640.html">第五百五十二章 白热化的灵院大赛</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2641.html">第五百五十三章 再度出关</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2642.html">第五百五十四章 萧皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2643.html">第五百五十五章 应邀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2644.html">第五百五十六章 赌约</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2645.html">第五百五十七章 斗阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2646.html">第五百五十八章 以阵斗阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2647.html">第五百五十九章 顾此失彼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2648.html">第五百六十章 救美</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2649.html">第五百六十一章 破阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2650.html">第五百六十二章 后手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2652.html">第五百六十三章 姬玄的试探</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2653.html">第五百六十四章</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2654.html">第五百六十五章 木神经之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2655.html">第五百六十六章 碾压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2656.html">第五百六十七章 分数</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2657.html">第五百六十八章 回忆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2658.html">第五百六十九章 拔牙行动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2659.html">第五百七十章 围剿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2660.html">第五百七十一章 吕天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2661.html">第五百七十二章 玄龟力场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2663.html">第五百七十三章 雷神体VS白骨神体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2664.html">第五百七十四章 大丰收</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2665.html">第五百七十五章 针对</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2666.html">第五百七十六章 暴风来临</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2667.html">第五百七十七章 反击</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2668.html">第五百七十八章 追逃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2669.html">第五百七十九章 惨烈</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2670.html">第五百八十章 双王见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2671.html">第五百八十一章 出牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2672.html">第五百八十二章 阵容对峙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2673.html">第五百八十三章 惊天对碰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2674.html">第五百八十四章 三重神魄难vs七纹雷体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2675.html">第五百八十五章 反击</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2676.html">第五百八十六章 隐藏底牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2677.html">第五百八十七章 暂时落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2678.html">第五百八十八章 深不可测的姬玄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2679.html">第五百八十九章 争夺第一</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2680.html">第五百九十章 兵分两路</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2681.html">第五百九十一章 排名飙升的代价</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2682.html">请假一天。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2683.html">第五百九十二章 龙虎鼎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2684.html">第五百九十三章 闯过去</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2685.html">第五百九十四章 神魄难</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2686.html">第五百九十五章 洛王展威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2687.html">第五百九十六章 渡难成功</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2688.html">第五百九十七章 燃烧院牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2689.html">第五百九十八章 分库</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2690.html">第五百九十九章 决战赛开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2691.html">第六百章 半年后的北苍灵院</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2692.html">第六百零一章 战界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2693.html">第六百零二章 黄金战梯</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2694.html">第六百零四章 前三</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2695.html">第六百零五章 决战赛</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2696.html">第六百零六章 八强对战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2697.html">第六百零七章 战柳青云</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2698.html">第六百零八章 风神影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2699.html">第六百零九章 队长之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2700.html">第六百一十章 黑塔炼灵影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2701.html">第六百一十一章</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2702.html">第六百一十二章 三强出线</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2703.html">第六百一十三章 血魔兽与战神猿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2704.html">第六百一十四章 审判之镜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2705.html">第六百一十五章 审判海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2706.html">第六百一十六章 损失惨重</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2707.html">第六百一十七章 超级漩涡</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2708.html">第六百一十八章 四强</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2709.html">第六百一十九章 四强开战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2710.html">第六百二十章 洛璃战血天河</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2711.html">第六百二十一章 温清璇的底牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2712.html">第六百二十二章 洛神剑的真正形态</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2713.html">第六百二十三章 变故</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2714.html">第六百二十四章 银发化青丝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2715.html">第六百二十五章 洛河之灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2716.html">第六百二十六章 真正的底牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2717.html">第六百二十七章 至尊海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2718.html">第六百二十八章 牧尘现身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2719.html">第六百二十九章 牧尘的至尊海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2720.html">第六百三十章 至尊之拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2721.html">第六百三十一章 姬玄最后的底牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2722.html">歪歪端午活动。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2723.html">第六百三十二章 九幽再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2724.html">第六百三十三章 九幽之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2725.html">第六百三十四章 九幽冥雀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2726.html">第六百三十五章 曼荼罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2727.html">第六百三十六章 斩草除根</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2728.html">第六百三十七章 冠军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2729.html">第六百三十八章 落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2730.html">第六百三十九章 离别之前</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2731.html">第六百四十章 洛天神</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2732.html">第六百四十一章 交谈</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2733.html">第六百四十二章 分离</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2734.html">第六百四十三章 原始法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2735.html">第六百四十四章 晋升至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2736.html">第六百四十五章 借镜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2737.html">第六百四十五章 争执</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2738.html">第六百四十七章 探测不朽图录</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2739.html">第六百四十七章 上古天宫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2740.html">第六百四十八章 离开</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2741.html">第六百四十九章 离开</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2742.html">第六百四十九章 灵力的灵性</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2743.html">第六百五十章 漫长的赶路</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2744.html">第六百五十一章 商之大陆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2745.html">第六百五十二章 商城</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2746.html">第六百五十三章 林静</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2748.html">第六百五十四章 拍卖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2749.html">第六百五十五章 大日虚空果</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2750.html">第六百五十六章 争夺</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2751.html">第六百五十七章 不灭神叶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2752.html">第六百五十八章 九龙九象术</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2753.html">第六百五十九章 截杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2754.html">第六百六十章 大千世界第一战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2755.html">第六百六十一章 战柳冥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2756.html">第六百六十二章 三莲形态</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2757.html">第六百六十三章 变故</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2758.html">第六百六十四章 神秘的白衣女子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2759.html">第六百六十五章 武境主母，绫清竹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2760.html">第六百六十六章 柳天道</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2761.html">第六百六十七章 大罗天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2762.html">第六百六十八章 九幽宫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2763.html">第六百六十九章 四大统领</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2764.html">第六百七十章 诸王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2765.html">第六百七十一章 九王会议</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2766.html">第六百七十二章 资格</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2767.html">第六百七十三章 震慑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2768.html">第六百七十四章 打死</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2769.html">第六百七十五章 修炼大日不灭身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2770.html">第六百七十六章 九阳为体，大日淬身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2771.html">第六百七十七章 法身成！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2772.html">第六百七十八章 九幽卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2773.html">第六百七十九章 统率九幽卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2774.html">第六百八十章 诚服</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2776.html">第六百七十九章 诡异的九龙九象术</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2777.html">第六百八十章 金池峰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2778.html">第六百八十一章 大罗金池之争</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2779.html">第六百八十二章 登顶之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2780.html">第六百八十三章 战四至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2781.html">第六百八十四章 雷霆手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2782.html">第六百八十五章 大罗金台</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2783.html">第六百八十六章 气魄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2784.html">第六百八十七章 挑战曹锋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2785.html">第六百八十八章 新老统领之斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2786.html">第六百八十九章 血影法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2787.html">第六百九十章 大日不灭身之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2788.html">第六百九十一章 摧枯拉朽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2789.html">第六百九十二章 登顶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2790.html">第六百九十三章 进入大罗金池</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2791.html">第六百九十四章 两千丈</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2792.html">第六百九十五章 池底之人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2793.html">第六百九十六章 曼荼罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2794.html">第六百九十七章 金池落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2795.html">第六百九十八章 大狩猎战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2797.html">第六百九十九章 靠拳头</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2798.html">第七百章 两个选择</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2799.html">第七百零一章 金身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2800.html">第七百零二章 罢免</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2801.html">第七百零三章 九幽战意</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2802.html">第七百零四章 摧枯拉朽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2803.html">第七百零五章 赌斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2805.html">第七百零六章 战阵师</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2806.html">第七百零七章 残破竹简</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2807.html">第七百零八章 感悟战意</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2808.html">第七百零九章 两卫之斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2810.html">第七百一十章 战意比拼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2811.html">第七百一十一章 血祭战意</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16701.html">第七百一十二章 获胜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/78460.html">第七百一十三章 征伐之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/105007.html">第七百一十四章 至天丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/134240.html">第七百一十五章 二品至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/175905.html">第七百一十六章 镇压诅咒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/225709.html">第七百一十七章 九阳之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/241797.html">第七百一十八章 战端启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/268959.html">第七百一十九章 横扫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/275228.html">第七百二十章 雷魔宗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/307370.html">卡壳，今天请假一天。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/317292.html">第七百二十一章 雷魔战意</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/346222.html">第七百二十二章 干扰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/390176.html">第七百二十三章 二品对三品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/407546.html">第七百二十四章 雷魔劫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/427884.html">第七百二十五章 胜利</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/455123.html">第七百二十六章 心魔雷莲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/458782.html">第七百二十七章 雷魔渊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/465625.html">第七百二十八章 探寻</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/471857.html">第七百二十九章 无上心魔经</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/499111.html">第七百三十章 镇魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/512169.html">第七百三十一章 残破石碑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/527750.html">第七百三十二章 右手不死,左手心魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/534350.html">第七百三十三章 淬炼九幽卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/535846.html">第七百三十四章 心魔种子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/544341.html">第七百三十五章 三千剑侍</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/555782.html">第七百三十六章 决战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/564107.html">第七百三十七章 巨头</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/564108.html">八点中秋活动。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/570024.html">第七百三十八章 一场赌斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/589447.html">第七百三十九章 八品至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/592495.html">第七百四十章 深不可测的睡皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/595148.html">第七百四十一章 尸骨娃娃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/603249.html">第七百四十二章 龙争虎斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/606961.html">第七百四十三章 罗汉法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/616026.html">第七百四十四章 血修罗之手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/622354.html">第七百四十五章 以命相搏</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/624488.html">第七百四十六章 败露</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/635797.html">第七百四十七章 大罗域主的真身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/640559.html">第七百四十八章 对峙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/649616.html">第七百四十九章 训练</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/662641.html">第七百五十章 大罗天军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/669261.html">第七百五十一章 灵炎髓</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/683277.html">感冒了，请假一天。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/685920.html">第七百五十二章 地狱模式</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/685921.html">第七百五十三章 岩浆苦修</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/700540.html">第七百五十四章 大猎杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/705827.html">第七百五十五章 身份的转变</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/728283.html">第七百五十六章 火魅儿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/737411.html">第七百五十七章 鹬蚌相争</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/755930.html">第七百五十八章 果决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/762264.html">第七百五十九章 完成修炼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/767669.html">第七百六十章 九九炎龙阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/769602.html">第七百六十一章 燃天符</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/794519.html">第七百六十二章 上古炎龙精血</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/795101.html">第七百六十三章 小心魔状态</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/805249.html">第七百六十四章 龙凤录</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/805922.html">第七百六十五章 曼陀罗灭天光</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/806311.html">第七百六十六章 动身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/808444.html">第七百六十七章 深山之遇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/808861.html">第七百六十八章 少女与青年</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/811840.html">第七百六十九章 同行</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/812616.html">第七百七十章 龙凤阁</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/815361.html">第七百七十一章 雷霆手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/816447.html">第七百七十二章 苏碧月与红鱼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/817193.html">第七百七十三章 龙凤池</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/827661.html">第七百七十四章 白衣男子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/837658.html">第七百七十五章 虫海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/840343.html">第七百七十六章 白骨山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/842855.html">第七百七十七章 登顶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/843460.html">第七百七十八章 两大强者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/843846.html">第七百七十九章 战柳炎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/846203.html">第七百八十章 焚天之羽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/850274.html">第七百八十一章 天阳黄金印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/854184.html">第七百八十二章 夺食</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/857750.html">第七百八十三章 幽冥皇子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/861487.html">第七百八十四章 伪龙体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/866592.html">第七百八十五章 龙凤神果</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/868391.html">第七百八十六章 金甲守护者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/873131.html">第七百八十七章 一指吞天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/874435.html">第七百八十八章 龙凤金甲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/875857.html">第七百八十九章 炼化</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/882001.html">第七百九十章 龙凤体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/889171.html">第七百九十一章 八座龙凤池</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/890586.html">第七百九十二章 众强云集</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/896737.html">第七百九十三章 龙凤台现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/898156.html">第七百九十四章 登台</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/904687.html">第七百九十五章 争夺开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/907714.html">第七百九十六章 锐气尽显</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/909211.html">第七百九十七章 一炷香</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/911262.html">第七百九十八章 再战柳炎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/926510.html">第七百九十九章 龙凤体之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/927751.html">第八百章 败柳炎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/929820.html">第八百零一章 幽冥皇子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/932112.html">第八百零二章 两处战场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/933698.html">第八百零三章 各显神通</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/933860.html">第八百零四章 最终对决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/938685.html">第八百零五章 胜！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/939452.html">第八百零六章 传承归属</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/941999.html">第八百零七章 龙凤梯</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/942778.html">第八百零八章 龙凤血浴</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/944618.html">第八百零九章 龙凤真经</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/947271.html">第八百一十章 三尊巨头</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/948787.html">第八百一十一章 帝焱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/950137.html">第八百一十二章 炎帝之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/952007.html">第八百一十三章 封王祭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/952853.html">第八百一十四 洛璃的消息</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/954227.html">第八百一十五章 夺王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/956153.html">第八百一十六章 双雄会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/960826.html">第八百一十七章 秦钟斗邱太阴</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/965274.html">剧情有点卡，今天无更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/969838.html">第八百一十八章 五品至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/969839.html">第八百一十九章 登台夺王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/973965.html">第八百二十章 突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/974529.html">第八百二十一章 激战邱太阴</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/977111.html">第八百二十二章 牧尘的底牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/977718.html">第八百二十三章 险胜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/979795.html">第八百二十四章 封王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/981616.html">第八百二十五章 备战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/983245.html">第八百二十六章 灵神液</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/988417.html">第八百二十七章 神血淬体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/989228.html">第八百二十八章 人形神兽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/994694.html">第八百二十九章 陨落源丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/997170.html">第八百三十章 大狩猎战开启!</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/999117.html">第八百三十一章 拉开战幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1004312.html">第八百三十二章 三级遗迹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1005608.html">第八百三十三章 龙蛇宗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1006987.html">第八百三十四章 蛇卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1019569.html">第八百三十五章 战意之间的差距</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1020100.html">第八百三十六章 战意之灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1021640.html">第八百三十七章 以命博命</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1023349.html">第八百三十八章 提炼陨落源丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1024552.html">今天无更，请大家不要等，抱歉。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1033385.html">第八百三十九章 灰袍人影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1033386.html">第八百四十章 萧青云</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1033387.html">第八百四十一章 求救</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1033388.html">第八百四十二章 千里救援</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1036948.html">第八百四十三章 徐霸</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1038347.html">第八百四十四章 天鳄军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1038455.html">第八百四十四章 五百出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1051531.html">第八百四十五章 黑马对霸主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1051532.html">第八百四十六章 周天神经</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1051535.html">第八百四十八章 远古星辰法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1051536.html">第八百四十七章 各显神通</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1056390.html">第八百四十九章 开三阳！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1058947.html">第八百五十章 两败</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1061810.html">第八百五十一章 援军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1081012.html">第八百五十二章 局势逆转</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1083295.html">第八百五十三章 痛打落水狗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1085966.html">第八百五十四章 千里追杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1087804.html">第八百五十五章 招打手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1088575.html">第八百五十六章 各方动静</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1089704.html">第八百五十七章 修炼战意</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1092918.html">第八百五十八章 血鹰战意之灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1093534.html">第八百五十九章 伪战意之灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1095328.html">第八百六十章 死亡遗迹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1096319.html">第八百六十一章 詹台琉璃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1097051.html">第八百六十二章 萧天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1097880.html">第八百六十三章 玄天部</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1098919.html">第八百六十四章 借军一用</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1108979.html">第八百六十五章 进入</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1110864.html">第八百六十六章 腐朽军队</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1126824.html">第八百六十七章 五王出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1128532.html">第八百六十八章 大军云集</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1130458.html">第八百六十九章 破阵之法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1133527.html">第八百七十章 庞大联军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1138298.html">第八百七十一章 詹台琉璃的能力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1141427.html">第八百七十二章 四灵战阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1143131.html">第八百七十三章 五军！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1144866.html">第八百七十四章 被坑的萧天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1147874.html">第八百七十五章 玄武阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1150228.html">第八百七十六章 五灵齐出</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1151641.html">第八百七十七章 惨烈</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1160040.html">第八百七十八章 聚五灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1161742.html">第八百七十九章 破阵！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1171807.html">第八百八十章 脆弱的合作</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1174516.html">第八百八十一章 天阵皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1188787.html">第八百八十二章 相信</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1201058.html">第八百八十三章 联手破邪</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1204352.html">第八百八十四章 天阵皇本尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1217316.html">千唤万唤始出来,大主宰手游正式公测!</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1218896.html">第八百八十五章 意念之法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1219452.html">第八百八十六章 九劫雷狱观想法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1220574.html">第六百八十七章 九劫战帝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1228051.html">第八百八十八章 围攻</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1230824.html">第八百八十九章 杀神归来</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1232525.html">第八百九十章 咫尺之遥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1234299.html">第八百九十一章 人质</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1235446.html">第八百九十二章 摧枯拉朽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1236121.html">第八百九十三章 敲诈</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1242013.html">第八百九十四章 收获</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1245288.html">更新在写，不过可能要12点。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1245291.html">第八百九十五章 冲刺五品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1249161.html">今天更新要耽搁一下，明天两章补上。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1250029.html">第八百九十六章 触手可及</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1251151.html">第八百九十七章 观想雷狱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1252909.html">第八百九十八章 精进的意念</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1258882.html">第八百九十九章 闭关结束</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1265340.html">第九百章 万纹战阵师</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1268402.html">第九百零一章 动荡的陨落战场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1275157.html">第九百零二章 林冥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1280140.html">第九百零三章 诸王汇合</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1284543.html">第九百零四章 被擒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1292034.html">第九百零五章 群雄会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1310287.html">第九百零六章 各方云集</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1314260.html">第九百零七章 群雄对峙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1321332.html">第九百零八章 玩更大</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1325619.html">第九百零九章 战阵师之间的对决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1342817.html">第九百一十章 吞魔之法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1345291.html">第九百一十一章 霸道</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1351016.html">第九百一十二章 九劫雷龙纹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1352995.html">第九百一十三章 回归</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1358258.html">第九百一十四章 暴涨的意念</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1360118.html">第九百一十五章 烂摊子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1361972.html">第九百一十六章 冥火老人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1369784.html">第九百一十七章 接引</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1372165.html">今天无更，明天补上。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1373445.html">第九百一十八章 破碎空间</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1374696.html">第九百一十九章 融化符文</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1379240.html">第九百二十章 寻宝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1380980.html">第九百二十一章 奇怪之物</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1383917.html">第九百二十二章 进入地至尊秘藏</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1384675.html">第九百二十三章 上古天宫，十大凶兽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1387658.html">第九百二十四章 修罗王vs吞天魔蛟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1401009.html">第九百二十五章 惨败</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1425663.html">第九百二十六章 九幽出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1450349.html">今天刚回家，明天补上更新</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1452500.html">第九百二十七章 最后一场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1452825.html">第九百二十八章 十凶兽，天龙虎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1455376.html">第九百二十九章 燃烧血脉</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1484000.html">第九百三十章 破阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1484615.html">第九百三十一章 秘藏中心</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1510841.html">第九百三十二章 七大地至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1513154.html">第九百三十三章 第四殿主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1517062.html">第九百三十四章 强大的灵傀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1541504.html">第九百三十五章 混战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1545191.html">第九百三十六章 三强对碰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1547981.html">第九百三十七章 后手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1557051.html">第九百三十八章 三座至尊法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1569738.html">第九百三十九章 五阳枪</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1586764.html">第九百四十章 震慑群雄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1591700.html">第九百四十一章 南阁主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1601175.html">第九百四十二章 战意神盘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1604002.html">第九百四十三章 陶罐</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1621200.html">第九百四十四章 鲁莽的神阁之主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1629217.html">第九百四十五章 灵神液成形!</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1637546.html">第九百四十六章 完美级灵神液</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1639119.html">第九百四十七章 隐忧</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1643692.html">第九百四十八章 半步上位地至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1664169.html">第九百四十九章 神阁之主的后招</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1668912.html">第九百五十章 危局</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1673884.html">第九百五十一章 第四殿主现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1679141.html">第九百五十二章 星辰镇魔塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1693259.html">第九百五十三章 陨落</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1698094.html">第九百五十四章 不朽金身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1701480.html">第九百五十五章 投资</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1705285.html">第九百五十六章 瓜分神阁</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1706883.html">第九百五十七章 壮大的九幽宫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1709886.html">第九百五十八章 天雀长老</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1712349.html">第九百五十九章 柳青</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1713861.html">第九百六十章 九幽炎雀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1716494.html">第九百六十一章 激斗柳青</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1720275.html">第九百六十二章 真凤威压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1720276.html">第九百六十三章 神兽之原</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1725819.html">第九百六十四章 四个名额</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1731917.html">第九百六十五章 两月准备</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1735418.html">第九百六十六章 六品至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1741581.html">第九百六十七章 天品灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1753154.html">第九百六十八章 九幽界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1757289.html">第九百六十九章 两个选择</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1773570.html">第九百七十章 肉身之撼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1775827.html">第九百七十一章 天罗阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1775828.html">高考季，祝福我的读者。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1778105.html">第九百七十二章 双重灵阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1779644.html">第九百七十三章 名额到手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1780923.html">第九百七十四章 墨锋墨铃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1784427.html">第九百七十五章 进入神兽之原</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1787238.html">第九百七十六章 血灵泥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1787239.html">第九百七十七章 巨无霸</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1792815.html">第九百七十八章 雷鸦族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1794415.html">第九百七十九章 血灵泥胎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1803873.html">第九百八十章 炼化</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1808756.html">第九百八十一章 肉身精进</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1818917.html">第九百八十二章 远古炼体塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1823681.html">第九百八十三章 天鹏族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1829133.html">第九百八十四章 群雄云集</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1833006.html">第九百八十五章 十座接引台</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1838485.html">第九百八十六章 天山神印</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1841651.html">第九百八十七章 天品灵阵之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1844009.html">第九百八十八章 进入</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1847621.html">第九百八十九章 塔内</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1850913.html">第九百九十章 赤光锻身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1854330.html">第九百九十一章 反追而上</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1861752.html">第九百九十二章 炼体塔第二层</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1865367.html">第九百九十三章 厚积薄发</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1898604.html">第九百九十四章 发力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1901340.html">第九百九十五章 残酷淘汰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1905866.html">第九百九十六章 真龙拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1913144.html">第九百九十七章 龙拳之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1922085.html">第九百九十八章 必占其一</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1926656.html">第九百九十九章 五道名额</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1929789.html">第一千章 雷髓洗礼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1931082.html">第一千零一章 收获</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1932483.html">第一千零二章 黑色石碑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1934128.html">第一千零三章 点燃青铜灯</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1934992.html">第一千零四章 七盏</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1936611.html">第一千零五章 牧尘出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1937893.html">第一千零六章 九灯齐燃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1944231.html">第一千零七章 偷袭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1946353.html">第一千零八章 拿钱消灾</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1966446.html">第一千零九章 血战王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1967152.html">第一千一十章 突破！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1975916.html">第一千一十一章 吐出来？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1976591.html">第一千一十二章 一拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1980279.html">第一千一十三章 试拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1981232.html">第一千一十四章 上古多宝兽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1982784.html">第一千一十五章 赶路</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1990873.html">第一千一十六章 自由交易点</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1996378.html">第一千一十七章 凤炎精</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/1998084.html">第一千一十八章 赤红舞</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2000259.html">第一千一十九章 保定了</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2000524.html">状态不佳，今天可能无更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2001376.html">第一千二十章 再来三颗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2002906.html">第一千二十一章 牛角,雷心</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2005035.html">第一千二十二章 万兽墓</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2005948.html">第一千二十三章 天狼族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2007184.html">第一千二十四章 金裂</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2013047.html">今日无更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2016080.html">第一千二十五章 暗算</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2023154.html">第一千二十六章 失效</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2025338.html">第一千二十七章 诛神阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2027873.html">第一千二十六章 草芥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2031498.html">第一千二十九章 金擎天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2035518.html">第一千三十章 激战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2042991.html">第一千三十一章 狮皇三吞</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2044965.html">第一千三十二章 七阳截天杖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2047837.html">第一千三十三章 败后赔款</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2052569.html">第一千三十四章 多宝湖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2058590.html">第一千三十五章 取宝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2066630.html">第一千三十六章 灭生瞳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2070891.html">第一千三十七章 盆满钵满</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2073797.html">第一千三十八章 神秘之地</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2088049.html">第一千三十九章 神墓园</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2092904.html">第一千四十章 群雄聚</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2098816.html">第一千四十一章 白冥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2105216.html">第一千四十二章 资格</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2105217.html">第一千三十三章 猎杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2105218.html">第一千三十四章 八品兽灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2113994.html">第一千三十五章 围猎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2119311.html">第一千三十六章 灵阵围杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2124909.html">第一千三十七章 灭生瞳之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2131394.html">第一千三十八章 九转青莲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2139107.html">第一千三十九章 闯谷</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2142769.html">第一千四十章 毁灭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2148194.html">第一千四十一章 七品至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2151263.html">第一千四十二章 内域</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2156815.html">第一千四十三章 三道传承精血</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2159301.html">第一千四十四章 战白冥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2163265.html">第一千四十五章 龙争虎斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2166179.html">第一千四十六章 灭生瞳vs寒凰灵扇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2169500.html">第一千四十七章 凰血祭灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2182995.html">第一千四十八章 血扇逞威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2196787.html">第一千四十九章 魔拳之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2224157.html">第一千五十章 近在咫尺</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2230528.html">第一千五十一章 传承精血</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2232893.html">第一千五十二章 魔变</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2233693.html">第一千五十三章 三兽尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2235922.html">第一千五十四章 天兽军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2240608.html">第一千五十五章 兽矛斩魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2246213.html">第一千五十六章 大造化</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2248632.html">第一千五十七章 神海苦修</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2253862.html">第一千五十八章 落幕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2258276.html">第一千五十九章 震动的九幽雀族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2272757.html">第一千六十章 天宫初现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2281289.html">第一千六十一章 实力精进</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2288183.html">第一千六十二章 半步九品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2293457.html">第一千六十三章 归来</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2298781.html">第一千六十四章 大罗天域的局势</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2299652.html">第一千六十五章 肃清</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2303862.html">第一千六十六章 新诸王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2305100.html">第一千六十七章 新皇争夺</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2307200.html">第一千六十八章 强势而来</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2311486.html">第一千六十九章 不灭火神罩</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2321077.html">第一千七十章 龙臂之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2327894.html">第一千七十一章 战九品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2330144.html">第一千七十二章 一拳夺皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2334643.html">第一千七十三章 遗迹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2338272.html">第一千七十四章 上古天宫的实力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2342635.html">第一千七十五章 迦楼罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2826725.html">[15] 第一千七十六章 西城</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2835644.html">第一千七十七章 夏弘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2840084.html">第一千七十八章 令牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2860149.html">第一千七十九章 拍卖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2860150.html">第一千八十章 九龙弑仙阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/2958416.html">第一千八十一章 争夺</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3019958.html">第一千八十二章 神秘女孩</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3116586.html">第一千八十三章 林静再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3143437.html">第一千八十四章 观摩龙阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3222254.html">第一千八十五章 借头</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3408190.html">第一千八十六章 扬威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3489707.html">第一千八十七章 挖坑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3595000.html">第一千八十八章 战夏弘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3695612.html">第一千八十九章 九凶天兽身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3763102.html">第一千九十章 开八阳！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3803035.html">第一千零九十二章 八阳天轮，攻防一体</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3809172.html">第一千九十二章 冰灵偶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3829674.html">第一千九十三章 收获颇丰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3852692.html">第一千九十四章 强者榜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3867710.html">第一千九十五章 传奇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3899148.html">第一千九十六章 一朵花</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/3953235.html">第一千九十七章 兵符</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/4622017.html">第一千九十八章 进入天宫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/4810547.html">第一千九十九章 空间暗斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/4989063.html">第一千一百章 登龙门</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5084464.html">第一千一百零一章 苏轻吟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5139704.html">第一千一百零二章 初次交锋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5249429.html">第一千一百零三章 金蛟弟子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5344687.html">第一千一百零四章 三位金龙弟子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5431141.html">第一千一百零五章 挑战权限</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5492409.html">第一千一百零六章 周天星辰阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5512250.html">第一千一百零七章 突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5577355.html">第一千一百零八章 车轮战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5626831.html">第一千一百零九章 第四位金龙弟子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5672081.html">第一千一百一十章 前往内域</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5694296.html">第一千一百一十一章 九府</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5717352.html">第一千一百一十二章 破阵而进</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5777315.html">第一千一百一十三章 风府之主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5790244.html">第一千一百一十四章 林静的手笔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5804189.html">第一千一百一十五章 圣物反噬</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5806108.html">第一千一百一十六章 与我有缘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5817497.html">第一千一百一十七章 祝焱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5827892.html">第一千一百一十八章 初次交锋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5835853.html">第一千一百一十九章 收获颇丰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5855247.html">第一千一百二十章 龙岛</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5868861.html">第一千一百二十一章 两女争锋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5880649.html">第一千一百二十一章 九幽的机缘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5906619.html">第一千一百二十二章 再见萧潇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5916425.html">第一千一百二十三章 吞天蟒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5930277.html">第一千一百二十四章 冤家路窄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5953189.html">第一千一百二十五章 气势碾压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5976345.html">第一千一百二十六章 初遇迦楼罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/5998359.html">第一千一百二十七章 恩怨</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6115031.html">第一千一百二十八章 天河开启</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6230845.html">第一千一百二十九章 天河之灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6253583.html">第一千一百三十章 捕获</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6266329.html">第一千一百三十一章 收获颇丰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6284376.html">第一千一百三十二章 战夏禹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6300663.html">第一千一百三十三章 大天王法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6305569.html">第一千一百三十四章 激战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6318977.html">第一千一百三十九章 山河玺</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6320709.html">第一千一百四十章 魔拳之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6335371.html">第一千一百四十一章 夏禹陨落</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6347459.html">第一千一百四十二章 第一百颗天河之晶？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/6354920.html">第一千一百四十三章 接锅</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12328274.html">第一千一百四十三章 接锅</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12381655.html">第一千一百四十四章 感应</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12507185.html">第一千一百四十五章 斗法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12509877.html">第一千一百四十六章 完美洗礼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12555476.html">第一千一百四十七章 实力精进</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12599232.html">第一千一百四十八章 不圆满？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12648422.html">第一千一百四十九章 奇特的藏经楼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12669938.html">第一千一百五十章  第二殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12723589.html">第一千一百五十一章 凰虫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12792253.html">第一千一百五十二章 合作</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/12933568.html">第一千一百五十三章 恢复屠灵卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13226626.html">第一千一百五十四章 战纹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13272814.html">第一千一百五十五章 收服屠灵卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13340871.html">第一千一百五十六章 冤家路窄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13376578.html">第一千一百五十七章 左长老</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13434167.html">第一千一百五十八章 初战地至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13491772.html">第一千一百五十九章 至尊法相</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13543760.html">第一千一百六十章 破阵之法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13616735.html">第一千一百六十一章 一掌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13646589.html">第一千一百六十二章 藏经楼现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13701033.html">第一千一百六十三章 寻找不朽金身！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13733568.html">第一千一百六十四章 战迦楼罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13787054.html">第一千一百六十五章 激战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13819225.html">第一千一百六十六章 圣物之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13862335.html">第一千一百六十七章 大日不灭身之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13908444.html">第一千一百六十八章 十阳神魔手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13930495.html">第一千一百六十九章 最终胜者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13947999.html">第一千一百七十章 不朽金身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13969810.html">第一千一百七十一章 天帝陵园</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/13994875.html">第一千一百七十二章 顶尖强者降临</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14025209.html">第一千一百七十三章 大圆满</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14077410.html">第一千一百七十四章 大圆满的曼荼罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14134470.html">第一千一百七十五章 变故</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14183171.html">第一千一百七十六章 魔帝？天帝？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14207032.html">第一千一百七十七章 魔帝复苏</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14235011.html">第一千一百七十八章 炎帝，萧炎</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14283613.html">第一千一百七十九章 佛怒火连</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14329946.html">第一千一百八十章 王见王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14376045.html">第一千一百八十一章 武祖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14438086.html">第一千一百八十二章 清理</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14488939.html">第一千一百八十三章 归属</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14533282.html">第一千一百八十四章 天帝赐机缘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14577067.html">第一千一百八十五章 这，就是地至尊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14599182.html">第一千一百八十六章 灵劫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14605234.html">第一千一百八十七章 展手段，渡灵劫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14643120.html">第一千一百八十八章 突破！地至尊！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14690434.html">第一千一百八十九章 天帝之教</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14749935.html">第一千一百九十章 浮屠古族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14800160.html">第一千一百九十一章 新建势力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14825480.html">第一千一百九十二章 以谁为尊？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14889837.html">第一千一百九十三章 登首资格</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14889918.html">第一千一百九十四章 灵阵展威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14941391.html">第一千一百九十五章 牧府</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/14984328.html">第一千一百九十六章 洛神</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15038452.html">第一千一百九十七章 创立牧府！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15060696.html">第一千一百九十八章 小西天界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15085682.html">第一千一百九十九章 那个女孩</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15109861.html">第一千两百章 洛神祭</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15145614.html">第一千两百零一章 洛神花</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15184416.html">第一千两百零二章 你的骑士</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15200437.html">第一千两百零三章 相见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15207742.html">第一千两百零四章 宰给你看</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15222776.html">第一千两百零五章 何谓恐怖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15251949.html">第一千两百零六章 黄泉血海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15267504.html">第一千两百零七章 也该绝望了</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15286863.html">第一千两百零八章 陨落</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15315002.html">第一千两百零九章 战绩</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15342462.html">第一千两百一十章 不会？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15365976.html">第一千两百一十一章 冬老</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15423279.html">第一千一百一十二章 大千世界第一美人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15454157.html">第一千两百一十三章 圣女？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15487108.html">第一千两百一十五章 战皇降临</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15515007.html">第一千两百一十五章 炎帝再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15540564.html">第一千两百一十六章 炎帝vs战皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15562794.html">第一千两百一十七章 渊源</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15580064.html">第一千两百一十八章 大陆之子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15610776.html">第一千两百一十九章 牧皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15635302.html">第一千两百二十章 洛璃的手腕</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15662156.html">第一千两百二十一章 四大圣子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15688852.html">第一千两百二十二章 古老之地</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15704035.html">第一千两百二十三章 祖气</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15721527.html">第一千两百二十四章 截杀与援手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15755311.html">第一千两百二十五章 强大的水晶浮屠塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15809005.html">第一千两百二十六章 争夺将至</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15840879.html">第一千两百二十七章 夺冠热门</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15868373.html">第一千两百二十八章 八千万一拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15893061.html">第一千两百二十九章 一拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15916170.html">第一千两百三十章 投了</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15949901.html">第一千两百三十一章 争夺战来临</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/15964601.html">第一千两百三十二章 战皇的福利</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16026828.html">第一千两百三十三章 三灵战阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16070579.html">第一千两百三十四章 火袍男子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16105418.html">第一千两百三十五章 首战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16143888.html">第一千两百三十六章 扬名</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16178683.html">第一千两百三十七章 鬼大师</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16226714.html">第一千两百三十八章 ??够了吗？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16268824.html">第一千两百三十九章 伏魔卫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16325817.html">第一千两百四十章 玄武战灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16379986.html">第一千两百四十一章 血灵子之死</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16400606.html">第一千两百四十二章 战阵到手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16431159.html">第一千两百四十三章 横扫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16465196.html">第一千两百四十四章 柳星辰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16501406.html">第一千两百四十五章 琅琊剑仙，霸刀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16524542.html">第一千两百四十六章 决战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16562866.html">第一千两百四十七章 灵战子之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16587588.html">第一千两百四十八章 巅峰对决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16636125.html">第一千两百四十九章 上古战帝法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16636130.html">一千二百五十章 不朽金身vs战帝法身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16636187.html">更新发重复了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16662144.html">今天的第一千两百五十章已经发布了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16684411.html">第一千两百五十一章 妖孽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16699309.html">第一千两百五十二章 现世！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16725023.html">第一千两百五十三章 绝世神通显威能</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16758069.html">第一千两百五十四章 最后的赢家</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16805697.html">第一千两百五十五章 两个女人的战场</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16876159.html">第一千两百五十六章 两女争锋</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16923036.html">第一千两百五十七章 洛璃显威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16948595.html">第一千两百五十八章 洛璃夺魁</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/16994397.html">第一千两百五十九章 洗礼分配</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17031386.html">第一千两百六十章 争夺份额</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17057102.html">第一千两百六十一章 一剑</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17095130.html">第一千两百六十二章 大陆洗礼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17141646.html">第一千两百六十三章 轰动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17177417.html">第一千两百六十四章 龙象</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17209229.html">第一千两百六十五章 晋级，上位地至尊！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17262090.html">第一千两百六十六章 少主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17270260.html">大主宰今天书友活动~</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17313902.html">第一千两百六十七章 自投罗网</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17363747.html">第一千两百六十八章 温存</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17390898.html">第一千两百六十九章 三大地至尊大圆满</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17433582.html">第一千两百七十章 夺阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17470552.html">第一千两百七十一章 大战大圆满</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17480132.html">第一千两百七十二章 杀心</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17531598.html">第一千两百七十三章 末日天狮</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17566582.html">第一千两百七十四章 红色葫芦</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17619247.html">第一千两百七十五章 赤炎老仙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17643251.html">第一千两百七十六章 八部浮屠</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17660078.html">第一千两百七十七章 母子再见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17733901.html">第一千两百七十八章 圣渊之秘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17856333.html">第一千两百七十九章 两卷阵图</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17879950.html">第一千两百八十章 圣渊大陆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17915309.html">第一千两百八十一章 大千宫，诛魔王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17949324.html">第一千两百八十二章 熟人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/17949325.html">第一千两百八十三章 再遇温清璇</a></dd>
                        
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/18024792.html">第一千两百八十四章 浮屠古族来到</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18076536.html">第一千两百八十五章 清萱长老</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18083321.html">第一千两百八十六章 夜见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18119261.html">第一千两百八十七章 高阶宗师境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18206987.html">第一千两百八十八章 进入上古圣渊</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18229283.html">第一千两百八十九章 化灵风</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18253786.html">第一千两百九十章 收服</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18277789.html">第一千两百九十一章 董山</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/18310329.html">第一千两百九十二章 灵蝶丹仙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18320101.html">第一千两百九十三章 武通</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18344633.html">第一千两百九十四章 丹兽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18362407.html">第一千两百九十五章 夺丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18405199.html">第一千两百九十六章 底牌齐出</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18442770.html">第一千两百九十七章 溶洞大战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18468042.html">第一千两百九十八章 投炉</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18489379.html">第一千两百九十九章 玄龙军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18509434.html">第一千三百章 玄龙空间</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18536591.html">第一千三百零一章 选择</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18563129.html">第一千三百零二章 战意之斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18600721.html">第一千三百零三章 再点兵！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18637189.html">第一千三百零四章 玄龙战灵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18647833.html">第一千三百零五章 尸魔族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18661389.html">第一千三百零六章 尸天幽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18697260.html">第一千三百零七章 无底洞</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18706786.html">第一千三百零八章 升华丹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18730643.html">第一千三百零九章 境界突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18760084.html">第一千三百一十章 交易区</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18788090.html">第一千三百一十一章 墨心少主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18815143.html">第一千三百一十二章 显威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18846681.html">第一千三百一十三章 冲突</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18881258.html">第一千三百一十四章 秦不败</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18914619.html">第一千三百一十五章 四圣塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18941339.html">第一千三百一十六章 炎魔族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18968691.html">第一千三百一十七章 炎魔族统领</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/18989282.html">第一千三百一十八章 大战炎魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19031498.html">第一千三百一十九章 清衍静的消息</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19094745.html">第一千三百二十章 墨心与玄罗的实力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19105316.html">第一千三百二十一章 尸天幽再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19126981.html">第一千三百二十二章 再战魔帝尸骸</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19164981.html">第一千三百二十三章 化灵风显威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19182707.html">第一千三百二十四章 尸神三叩首</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19219433.html">第一千三百二十五章 尸神技</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19249193.html">第一千三百二十六章 不朽金莲</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19289744.html">第一千三百二十七章 血僵天魔帝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19307676.html">第一千三百二十八章 浮屠战血僵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19350666.html">第一千三百二十八章 新的诛魔王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19387255.html">第一千三百二十九章 震动</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19422579.html">第一千三百三十章 传承归属</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19455107.html">第一千三百三十一章 八部浮屠传承！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19497370.html">第一千三百三十二章 唤醒之法</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19525737.html">第一千三百三十三章 太灵通天光</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19540623.html">番外，冰灵族篇一。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19540625.html">冰灵族番外篇二</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19540644.html">冰灵篇3</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19550150.html">第一千三百三十四章 半步大圆满</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19569341.html">第一千三百三十六章 阻扰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19588937.html">第一千三百三十七章 一群天至尊的对峙</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19606840.html">第一千三百三十八章 第二位诛魔王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19621210.html">第一千三百三十九章 诛魔点</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19632338.html">第一千三百四十章 分离</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19656818.html">第一千三百四十一章 紫云宗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19724620.html">第一千三百四十二章 牧府之主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/19778269.html">第一千三百四十三章 镇服</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20083995.html">第一千三百四十四章 北域争霸</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20103557.html">第一千三百四十五章 欣欣向荣的牧府</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20158315.html">第一千三百四十六章 和藏经楼的交易</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20200982.html">第一千三百四十七章 大会来临</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20224898.html">第一千三百四十八章 北域原</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20313886.html">第一千三百四十九章 雷霆手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20474769.html">第一千三百五十章 逞凶威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20491722.html">第一千三百五十一章 三大霸主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20502248.html">第一千三百五十二章 大战紫云真君</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20545869.html">第一千三百五十三章 金箭之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20574650.html">第一千三百五十四章 强势</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20595270.html">第一千三百五十五章 牧主战三霸</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20628485.html">第一千三百五十六章 临阵突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20648965.html">第一千三百五十七章 八部浮屠显威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20677500.html">第一千三百五十八章 划分地盘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20693288.html">第一千三百五十九章 新晋霸主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20744204.html">第一千三百六十章 牧府扬威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20799383.html">第一千三百六十章 天至尊之路</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20820884.html">第一千三百六十一章 白龙机缘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20843786.html">第一千三百六十二章 空间节点</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20891949.html">第一千三百六十三章 下位面</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20920906.html">第一千三百六十四章 血魔将</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/20964870.html">第一千三百六十五章 白衣女王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/21040249.html">第一千三百六十六章 血魔王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138463907.html">第一千三百六十七章 摧枯拉朽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138524524.html">第一千三百六十八章 镇魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138553112.html">第一千三百六十九章 请求</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138580665.html">第一千三百七十章 血魔山</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138626847.html">第一千三百七十一章 圣龙宗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138663225.html">第一千三百七十二章 尽除</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138700250.html">第一千三百七十三章 大战将起</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138722442.html">第一千三百七十四章 以一敌三战血魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138750349.html">第一千三百七十五章 催化</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138771036.html">第一千三百七十六章 血皇出世</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138786694.html">第一千三百七十七章 魔帝之威</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138826489.html">第一千三百七十八章 牧主战血皇</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138847189.html">第一千三百七十九章 一气化三清，三合之境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138858273.html">第一千三百八十章 最后的手段</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138880680.html">第一千三百八十一章 机缘所在</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138907398.html">第一千三百八十二章 天障</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138936352.html">第一千三百八十三章 天尊劫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/138989589.html">第一千三百八十四章 年少出北灵，今朝登天门</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139023929.html">第一千三百八十五章 天至尊之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139039975.html">第一千三百八十六章 黑尸天魔帝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139061249.html">第一千三百八十七章 武祖斗尸帝</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139088474.html">第一千三百八十八章 位面之主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139134815.html">第一千三百八十九章 玄天老祖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139163519.html">第一千三百九十章 强势归来</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139196858.html">第一千三百九十一章 灵脉之秘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139224079.html">第一千三百九十二章 强势镇压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139257324.html">第一千三百九十三章 强硬</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139275742.html">第一千三百九十四章 威慑四方</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139303165.html">第一千三百九十五章 收服玄天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139332376.html">第一千三百九十六章 神脉</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139351052.html">第一千三百九十七章 今朝现世</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139403631.html">第一千三百九十八章 灵脉殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139445730.html">第一千三百九十九章 神脉震玄天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139480938.html">第一千四百章 浮屠城</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139492012.html">第一千四百零一章 摩诃幽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139542797.html">第一千四百零二章 浮屠界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139586024.html">第一千四百零三章 清脉之势</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139620933.html">第一千四百零四章 席位之争</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139683287.html">第一千四百零五章 浮屠玄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139720202.html">第一千四百零六章 三脉之首</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139742794.html">第一千四百零七章 清脉之败</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139757422.html">第一千四百零八章 家母，清衍静</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139796686.html">第一千四百零九章 新清脉脉首</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139805209.html">第一千四百一十章 一人战玄脉</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139807553.html">第一千四百一十一章 一招一个</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139812029.html">第一千四百一十二章 再斗黑光</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139821969.html">第一千四百一十三章 暴打</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139863144.html">第一千四百一十四章 仙品出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139886481.html">第一千四百一十五章 激战仙品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139906275.html">第一千四百一十六章 神脉对决</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139927972.html">第一千四百一十七章 神光震古族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139941815.html">第一千四百一十八章 再起斗执</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139968628.html">第一千四百一十九章 一人战浮屠</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/139989934.html">第一千四百二十章 一人敌族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140023900.html">第一千四百二十一章 浮屠玄出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140043493.html">第一千四百二十二章 清衍静现身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140049821.html">第一千四百二十三章 圣品之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140073203.html">第一千四百二十四章 新任大长老</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140097856.html">第一千四百二十五章 变天的浮屠古族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140122143.html">第一千四百二十六章 见面礼</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140151901.html">第一千四百二十七章 晋级的圣浮屠塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140170510.html">第一千四百二十八章 百灵大陆</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140189132.html">第一千四百二十九章 百灵王</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140213841.html">第一千四百三十章 你真的是一个废物</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140233654.html">第一千四百三十一章 去搬救兵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140249824.html">第一千四百三十二章 夫妻相见</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140281967.html">第一千四百三十三章 柳百花</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140302275.html">第一千四百三十四章 秦北玄</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140327246.html">第一千四百三十五章 背景</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140344728.html">第一千四百三十六章 处置</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140365125.html">第一千四百三十七章 远距离传送阵</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140380539.html">第一千四百三十八章 不死血脉启争端</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140413338.html">第一千四百三十九章 九幽有难</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140431934.html">第一千四百四十章 缘由</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140459042.html">第一千四百四十一章 欺压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140480237.html">第一千四百四十二章 针锋相对</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140508911.html">第一千四百四十三章 血精</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140537643.html">第一千四百四十四章 镇压</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140577291.html">第一千四百四十五章 莫名来者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140608162.html">第一千四百四十六章 合作</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140623899.html">第一千四百四十七章 埋伏截杀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140656118.html">第一千四百四十八章 三英战凰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/140690120.html">第一千四百四十九章 准圣血精</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/141356559.html">第一千四百四十九章 黄雀在后</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/142890135.html">第一千四百五十章 天骄之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143143836.html">第一千四百五十一章 龙凰斗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143168199.html">第一千四百五十二章 九转入圣诀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143191733.html">第一千四百五十三章 三合境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143209856.html">第一千四百五十四章 胜负</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143218750.html">第一千四百五十五章 准圣血精入手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143441521.html">第一千四百五十六章 进化，上古不死鸟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143468600.html">第一千四百五十七章 真龙与真凤</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143493035.html">第一千四百五十八章 牧府局势</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143516276.html">第一千四百五十九章 天罗盟</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143553848.html">第一千四百六十章 霸主之争</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143593805.html">第一千四百六十一章 天罗对牧府</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143638711.html">第一千四百六十二章 以一敌五</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143674095.html">第一千四百六十三章 五千万战纹</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143696475.html">第一千四百六十四章 显峥嵘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143721029.html">第一千四百六十五章 赔偿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143764311.html">第一千四百六十六章 山洞闭关</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143801280.html">第一千四百六十七章 热门</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143831080.html">第一千四百六十八章 万古城</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143842588.html">第一千四百六十九章 条件</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143862569.html">第一千四百七十章 万古塔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143897437.html">第一千四百七十一章 万古之争</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143904998.html">第一千四百七十二章 秦东海</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143938691.html">第一千四百七十三章 战释罗</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143944025.html">第一千四百七十四章 圣佛手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143975729.html">第一千四百七十五章 三灵再现</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/143982484.html">第一千四百七十六章 六千八百万</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/143994006.html">第一千四百七十七章 最后一层</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144041931.html">第一千四百七十八章 突破</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144047096.html">第一千四百七十九章 摩诃无量劫</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144097875.html">第一千四百八十章 万古不朽身现世</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144132894.html">第一千四百八十一章 神秘的暗金之影</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144140034.html">第一千四百八十二章 刀圣陨</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144152853.html">第一千四百八十三章 自爆不朽金身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144177647.html">第一千四百八十四章 紫金世界</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144198632.html">第一千四百八十五章 掌控与唤醒</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144218399.html">第一千四百八十六章 再临世间</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144237654.html">第一千四百八十七章 真品与赝品</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144295849.html">第一千四百八十八章 万古新主</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144308860.html">第一千四百八十九章 肉身不朽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144360998.html">第一千四百九十章 五年苦修，铸就不朽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144388800.html">第一千四百九十一章 现身</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144400233.html">第一千四百九十二章 黑天古族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144422718.html">第一千四百九十三章 再见洛璃</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144440385.html">第一千四百九十三章 对决摩诃天</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144479870.html">第一千四百九十五章 圣品之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144521284.html">第一千四百九十六章 现世之战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144540479.html">第一千四百九十七章 摩诃阴阳瓶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144563512.html">第一千四百九十八章 古塔镇玉瓶</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144590154.html">第一千四百九十九章 送贴</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144603476.html">第一千五百章 大千盟约</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144632162.html">第一千五百零一章 万魔殿</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144656097.html">第一千五百零二章 安宁</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144687738.html">第一千五百零三章 魔迹现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144728404.html">第一千五百零四章 北荒之丘</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144741689.html">第一千五百零五章 群雄聚</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144771174.html">第一千五百零六章 遗命</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144787966.html">第一千五百零七章 诸尊炼魔神</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144808830.html">第一千五百零八章 援军</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144946540.html">第一千五百零九章 那个人</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/144967215.html">第一千五百一十一章 心魔种子</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146319398.html">第一千五百一十章 邪灵族</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146344331.html">第一千五百一十一章 姜崖</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146361058.html">第一千五百一十二章 人法合一</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146652600.html">第一千五百一十三章 一拳</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146683665.html">第一千五百一十四章 血祀</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146704832.html">第一千五百一十五章 邪神出世</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146724903.html">第一千五百一十六章 他们，来了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146751925.html">第一千五百一十七章 世界意志</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146768400.html">第一千五百一十八章 苍穹榜</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146787875.html">第一千五百一十九章 一帝一祖战邪神（上）</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146804119.html">第一千五百二十章 一帝一祖战邪神（中）</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146822785.html">第一千五百二十一章 一帝一祖战邪神（下）</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146842415.html">第一千五百二十二章 九目邪神</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146885144.html">第一千五百二十三章 第三者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146915332.html">第一千五百二十四章 大帝遗泽</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146934068.html">第一千五百二十六章 接收传承</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146954804.html">第一千五百二十七章 扫荡与苦修</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146974613.html">第一千五百二十八章 三神境</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/146993830.html">第一千五百二十九章 魔踪与八目</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147031483.html">第一千五百三十章 战争来临</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147053605.html">第一千五百三十一章 刀与剑，血与火</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147074180.html">第一千五百三十二章 魔灾</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147093033.html">第一千五百三十三章 北苍乱</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147098542.html">第一千五百三十五章 灵院难</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147110302.html">第一千五百三十五章 黑尸再现</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147117837.html">第一千五百三十六章 可曾问过</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147132678.html">第一千五百三十七章 再战黑尸</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147149523.html">第一千五百三十八章 弹指灭魔</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147159297.html">第一千五百三十九章 再见时，已君临大千</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/147194428.html">第一千五百四十一章</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147220916.html">第一千五百四十二章 有我之名</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/147248253.html">第一千五百四十三章 第三位榜上者</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147276672.html">第一千五百四十四章 再战天邪神</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147290837.html">第一千五百四十五章 最强之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147309295.html">第一千五百四十六章 十目</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147324739.html">第一千五百四十七章 最后的底牌</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147326926.html">第一千五百四十八章 大主宰</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147348090.html">第一千五百四十九章 最后一战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147368351.html">第一千五百五十章 生灵之力</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/147370713.html">第一千五百五十一章 邪神陨落（大结局）</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167372369.html">热血尚在否？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372370.html">五更，求月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372371.html">三天十一更，求月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372372.html">马上就新的一周了，求推荐票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372373.html">三章已更，可能求票？</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372374.html">三章已更，求月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372375.html">求推荐票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372376.html">三章，求月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372377.html">第九十九章 九域大会</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372378.html">新的一周，求推荐票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372379.html">四更！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372380.html">战！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372381.html">今儿四更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372382.html">四章已更，求月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372383.html">三更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372384.html">再战吧！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372385.html">我们同样也累，但没人会放弃。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372386.html">七更！！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372387.html">最后一天，求月票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372388.html">感谢大家。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372389.html">三章已更，求声票！</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167372391.html">急求月票。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372392.html">新的一周，求推荐票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372393.html">今天请假一下，欠两章更新。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372394.html">刚到家，今天一更，欠五更了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372395.html">新的一周，拜求推荐票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372396.html">尝试四更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372397.html">第一百八十二章 大炎魔之阵【第二更！】</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167372399.html">四章。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372400.html">白天回老家过中秋节了，刚刚赶回来</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372401.html">三章！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372402.html">明天开始补欠更新。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372403.html">双倍月票来了，兄弟姐妹们，热血起来吧！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372404.html">干！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372405.html">五章已更！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372406.html">最后的22小时！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372407.html">请读者们看看。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372408.html">四章！</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167372410.html">第三更正在写之中。、</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372411.html">求推荐票！！！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372412.html">三章！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372413.html">新的一周，求一声票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372414.html">今日一更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372415.html">求声月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372416.html">最后24小时！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372417.html">新的一月！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372418.html">三章已更！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372419.html">求月票！！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372420.html">三章！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372421.html">请假一天。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372422.html">月底了，求一声月票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372423.html">大家别等了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372424.html">还欠三更，今日必须五更才行了。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372425.html">求月票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372426.html">五章已更。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372427.html">第二天，求月票！！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372428.html">求票！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372429.html">补欠更新还玩，今日两百票，加一更！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372430.html">三章已更！</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167372431.html">月中，求声月票！</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167372433.html">千言万语，汇成一句感谢。</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167373092.html">第四百六十一章 强势镇压</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167373096.html">第七百四十二章 龙争虎斗</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167373100.html">第八百九十章 咫尺之遥</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167373102.html">第九百三十一章 秘藏中心</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167373106.html">第九百三十四章 强大的灵傀</a></dd>
                        
                        <dd><a href="https://www.biquge5200.cc/0_7/167373111.html">第一千零五章 牧尘出手</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167373113.html">第一千三十章  激战</a></dd>
                        <dd><a href="https://www.biquge5200.cc/0_7/167373115.html">第一千三十二章 七阳截天杖</a></dd>
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
				</dl>
			</div>
		</div>
        
        <div class="dahengfu"><script type="text/javascript">bottom();</script></div>
        
		<div id="footer" name="footer">
			<div class="footer_link">&nbsp;新书推荐：<a href='/2_2599/' >全职法师</a>
				<a href='/9_9365/' style='font-weight:bold'>盖世帝尊</a>
				<a href='/46_46254/' >斗战狂潮</a>
				<a href='/53_53081/' >都市超级医圣</a>
				<a href='/0_494/' style='font-weight:bold'>超级兵王</a>
				<a href='/0_491/' >俗人回档</a>
				<a href='/44_44186/' style='font-weight:bold'>人皇纪</a>
				<a href='/2_2691/' >寒门崛起</a>
				<a href='/0_419/' >无敌天下</a>
				  </div>
			<div class="footer_cont">
				<p>《大主宰》情节跌宕起伏、扣人心弦，是一本情节与文笔俱佳的，笔趣阁转载收集大主宰最新章节。</p>
				<script>footer();right();dl();</script>
			</div>
		</div>
	</div>
	<script type="text/javascript">ac("1", "7");</script>
</body></html>

Process finished with exit code 0

'''
html1_doc = etree.HTML(html1)
# //dd/a/@href
http = html1_doc.xpath("//dd/a/@href")
# print(len(http))
for i in range(1,10):
    response = requests.get(http[i],headers)
    html = response.text
    # html_str = '''
    # # D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/小说.py"
    # # 1680
    # #
    # # <!doctype html>
    # # <html>
    # # <head>
    # # <title>第一千零五章 牧尘出手_大主宰_笔趣阁</title>
    # # <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
    # # <meta name="keywords" content="大主宰, 第一千零五章 牧尘出手" />
    # # <meta name="description" content="笔趣阁提供了天蚕土豆创作的玄幻小说《大主宰》干净清爽无错字的文字章节： 第一千零五章 牧尘出手在线阅读。" />
    # # <meta http-equiv="Cache-Control" content="no-siteapp" /><meta http-equiv="Cache-Control" content="no-transform" />
    # # <meta http-equiv="mobile-agent" content="format=html5; url=https://m.biquge5200.cc/wapbook-7-167373111/" />
    # # <meta http-equiv="mobile-agent" content="format=xhtml; url=https://m.biquge5200.cc/wapbook-7-167373111/" />
    # # <link rel="stylesheet" type="text/css" href="//www.biquge5200.cc/images/biquge.css"/>
    # # <script src="//apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js" type="text/javascript"></script>
    # # <script src="//apps.bdimg.com/libs/jquery.cookie/1.4.1/jquery.cookie.min.js" type="text/javascript"></script>
    # # <script type="text/javascript">var novelId="7";var chapterId = "167373111";var refId="24027";var preview_page = "https://www.biquge5200.cc/0_7/167373106.html";var next_page = "https://www.biquge5200.cc/0_7/167373113.html";var index_page = "https://www.biquge5200.cc/0_7/";var article_id = "7";	var chapter_id = "167373111";	function jumpPage() {var event = document.all ? window.event : arguments[0];if (event.keyCode == 37) document.location = preview_page;if (event.keyCode == 39) document.location = next_page;if (event.keyCode == 13) document.location = index_page;}document.onkeydown=jumpPage;</script>
    # # <script type="text/javascript" src="//www.biquge5200.cc/images/bqg.js?v=200302"></script>
    # # <script type="text/javascript">uaredirect("https://m.biquge5200.cc/wapbook-7-167373111/");</script>
    # # </head>
    # # <body>
    # # <div id="wrapper">
    # #         <script>login();</script>
    # #         <div class="header">
    # #             <div class="header_logo">
    # #                 <a href="//www.biquge5200.cc">笔趣阁</a>
    # #             </div>
    # #             <script>bqg_panel();</script>
    # #         </div>
    # #         <div class="nav">
    # #             <ul>
    # #                 <li><a href="//www.biquge5200.cc/">首页</a></li>
    # #                 <li><a rel="nofollow" href="/home/">我的书架</a></li>
    # #                 <li><a href="//www.biquge5200.cc/xuanhuanxiaoshuo/">玄幻小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/xiuzhenxiaoshuo/">修真小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/dushixiaoshuo/">都市小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/chuanyuexiaoshuo/">穿越小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/wangyouxiaoshuo/">网游小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/kehuanxiaoshuo/">科幻小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/yanqingxiaoshuo/">言情小说</a></li>
    # #                 <li><a href="//www.biquge5200.cc/tongrenxiaoshuo/">同人小说</a></li>
    # #             </ul>
    # #         </div>
    # # <div class="content_read">
    # #                         <script>list();</script>
    # #                         <script>dingbu();</script>
    # #                     <div class="box_con">
    # #                 <div class="con_top">
    # #                     <script>textselect();</script>
    # #                     <a href="/">笔趣阁</a> &gt; <a href="/xuanhuanxiaoshuo/">玄幻小说</a> &gt; <a href="https://www.biquge5200.cc/0_7/">大主宰</a> &gt;  第一千零五章 牧尘出手
    # #                 </div>
    # #                 <div class="bookname">
    # #                     <h1> 第一千零五章 牧尘出手</h1>
    # #                     <div class="bottem1">
    # #                          <script type="text/javascript">list3();</script>
    # #                         <a href="javascript:tj('1','7');">投推荐票</a> <a href="https://www.biquge5200.cc/0_7/167373106.html">上一章</a> &larr; <a href="https://www.biquge5200.cc/0_7/">章节目录</a> &rarr; <a href="https://www.biquge5200.cc/0_7/167373113.html">下一章</a> <a href="javascript:pl('7','167373111');">加入书签</a>
    # #                        <script type="text/javascript">list2();</script>
    # #                     </div>
    # #
    # #                     <script>gonggao();</script>
    # #                     <div class="lm">&nbsp;热门推荐：
    # #                         <a href='/97_97123/' style='font-weight:bold'>三寸人间</a>
    # #                         <a href='/76_76490/' >牧神记</a>
    # #                         <a href='/86_86700/' style='font-weight:bold'>伏天氏</a>
    # #                         <a href='/78_78387/' >汉乡</a>
    # #                         <a href='/0_111/' >武炼巅峰</a>
    # #                         <a href='/79_79883/' style='font-weight:bold'>元尊</a>
    # #                         <a href='/79_79875/' >飞剑问道</a>
    # #                         <a href='/8_8165/' style='font-weight:bold'>至尊剑皇</a>
    # #                         <a href='/57_57491/' >道君</a>
    # #                         <a href='/84_84888/' >超品巫师</a>
    # #                         <a href='/51_51253/' style='font-weight:bold'>透视小医神</a>
    # #                         <a href='/0_554/' style='font-weight:bold'>混沌剑神</a>
    # #                     </div>
    # #                 </div>
    # #                 <div class="kongwei"><span></span></div>
    # #                 <div style="width:910px;margin:0px auto;" id="ctad">
    # #                     <table id="adt1"><tr>
    # #                     <td id="adt1"><script type="text/javascript">cad1();</script></td>
    # #                     <td id="adt2"><script type="text/javascript">cad2();</script></td>
    # #                     <td id="adt3"><script type="text/javascript">cad3();</script></td>
    # #                     </tr></table>
    # #                 </div>
    # #                 <div id="content"><p>　　黑色石碑之前，牧尘静立，他凝视着石碑表面那无数道印痕，隐约间，仿佛是能够感受到那无数强者曾经站在这里，凝聚着所有的肉身力量，挥出最强的一击。</p><p>　　据说在那远古时期，曾经有着强者将九盏青铜灯尽数的点燃，这让得牧尘实在是有些惊叹，当然，他也知晓，能够将九盏青铜灯点燃的人，其本身实力，必然应该是远超了他们，甚至极有可能，其本身就是八品甚至九品至尊的强者。</p><p>　　再加上远古时期这神兽之原对于肉身的各种淬炼之力，也是导致神兽之原中的诸多强者都是肉身极为的强悍，要说他们能够做到点燃九盏青铜灯，牧尘并不怀疑。</p><p>　　而且，自从神兽之原破碎后，那些进入神兽之原寻找机缘的各族天骄们，能够在炼体塔第四层点燃九盏青铜灯的人，更是屈指可数。</p><p>　　而那些人，无一不是在那一辈之中显赫之极的妖孽人物，即便是各族的天骄，也是在他们的光芒下格外的黯淡。</p><p>　　而对于点燃九盏灯，牧尘也清楚其难度有多可怕，即便是强如那韩山，倾尽所有的力量，也仅仅只能勉强点燃第七盏灯，这距离九盏，还有着不小的距离。</p><p>　　所以，对于自己最终能够取得什么样的成绩，牧尘现在也无法估量，但不管如何，这一次，他必然是会全力以赴！</p><p>　　为了能够在这炼体塔内，将龙凤真经突破到第二层！</p><p>　　呼。</p><p>　　牧尘心中念头渐渐的平复下来，他深吸一口气，手掌也是在那所有的视线注视下，紧紧的握拢了起来。</p><p>　　淡淡的金光，开始在此时自牧尘的体内散发出来，他的皮肤，竟是被渲染得犹如黄金所铸，这种金色，伴随着时间的推移。愈发的暗沉内敛，犹如一尊岁月久远的黄金之像。</p><p>　　他催动着龙凤体，渐渐的将体内的所有力量，都是从血肉深处开始抽动出来。这一次，他要将龙凤体的力量，施展到最极限！</p><p>　　在那不远处，宗腾，韩山。墨锋三人望着此时的牧尘，双目都是微微一眯，因为他们能够察觉到，站在那里的牧尘，此时有着一种无可撼动的沉重之感散发出来。</p><p>　　感觉上，就犹如是一座矗立天地的巍峨山岳一般。</p><p>　　随着龙凤体逐渐的运转到极致，牧尘双臂上，那盘踞的真龙真凤之纹，也是在此时微微的颤动着，紧接着。那龙吟凤鸣之声，便是从其体内传出，震荡着血肉，令得牧尘体内的力量，在此时开始以一种惊人的速度出现增幅。</p><p>　　龙吟凤鸣越来越嘹亮，越来越急促，牧尘浑身的血肉，都是在那震荡间变得渐渐的沸腾起来，特别是在双臂处的真龙真凤之纹，更是在此时变得滚烫。犹如烙铁一般。</p><p>　　牧尘的双目，愈发的金光璀璨，他的呼吸变得粗重起来，因为体内的力量。在此时凝聚到了一种相当可怕的程度，这股力量，比之前重创陆隋的时候，还要来得更强！</p><p>　　韩山三人望着那不断喷薄着金光的身影，眼神也是渐渐的凝重起来，那种金光。并非是灵力所化，而同样是牧尘体内的气血凝聚到极致的表现，只不过让得他们有些惊异的是，牧尘的这种气血之光颇为的奇异，而且似乎还蕴藏着一种令他们感到有些压迫的波动。</p><p>　　“没想到凭借着六品至尊的实力，就能够凝聚出如此可怕的气势…”韩山目光锐利的盯着牧尘，虽说他并未小觑过牧尘，但也并未料到，后者的能力会是如此的出众，他有着预感，恐怕牧尘这一次的出手，最起码都将会超越宗腾，墨锋，甚至…说不定还会追赶上他！</p><p>　　这个人类，不简单。</p><p>　　而对于韩山他们的凝重视线，此时的牧尘已是无法察觉，伴随着体内血肉愈发的沸腾，他发现外界的动静仿佛是被屏蔽，整个世界，似乎都唯有他一人。</p><p>　　这种状态，让得牧尘将浑身精气神都是凝聚到了巅峰。</p><p>　　犹如实质般的金光，自牧尘的双目中喷薄而出，他体内的力量，已是彻彻底底的达到了巅峰，甚至，体内的血肉，骨骼，都是在发出隐隐的刺痛感。</p><p>　　那是极限的表现。</p><p>　　既然已到极限，那就出手吧！</p><p>　　牧尘神色古井无波，仿佛无我无他，他右手紧握，然后平平的一拳轰出。</p><p>　　轰出的刹那，真龙以及真凤之纹尽数的游动而来，最后竟是同时盘踞在了牧尘右臂之上，紫金光芒散发，金色的龙爪凤爪，伸展开来，将牧尘的拳头尽数的覆盖。</p><p>　　吼！</p><p>　　一拳轰出的刹那，那嘹亮的龙吟凤鸣声，终是无法被牧尘的身体所遮掩，直接是传荡而出，最后轰然在这座古老的广场中响彻起来。</p><p>　　而韩山，墨锋，宗腾三人的身体，则是在此时猛的一僵，他们察觉到一股可怕的威压，正在疯狂的从牧尘体内席卷出来。</p><p>　　那种威压，令得他们血脉都是在为之颤抖。</p><p>　　那是一种血脉压制！</p><p>　　但这种压制让得三人都是难以置信，因为他们本身的血脉便属于高等血脉，在灵兽界中算得上是顶尖，然而眼下，竟然因为牧尘体内传出的威压，产生了血脉压制？</p><p>　　那是唯有源自超级神兽的超级血脉，才有可能办到的啊！</p><p>　　而就在三人震惊之间，牧尘的那缠绕着真龙真凤，犹如黄金所铸般的拳头，已是轰爆了空间，最后携带着层层黄金涟漪，重重的轰在了那黑色石碑之上。</p><p>　　轰！</p><p>　　轰击的瞬间，韩山他们能够清晰的感觉到整个古老广场都是在此时震动了一下，甚至，连那素来稳如磐石的黑色石碑，仿佛也是微微的颤了一颤。</p><p>　　韩山他们的目光死死的盯着牧尘拳头与黑色石碑的碰撞之点，然后瞳孔都是猛的一缩。</p><p>　　那里金光涟漪冲击开来，牧尘的拳头瞬间崩裂，鲜血溅射出来，甚至隐隐间都是显出了白骨，这表明牧尘的这一拳之强悍，竟是连他的肉身都是有些无法承受。那种反震力道，直接震碎了他的拳头。</p><p>　　不过，即便是拳头鲜血溅射，森森白骨显露。但牧尘却并没有任何要收手的迹象，反而是一声低喝，体内所有的力量，都是在在此时顺着拳头疯狂的涌了出去。</p><p>　　金色涟漪，一波波的从牧尘拳头之下荡漾开来。席卷了整个石碑表面。</p><p>　　他脚下的古老地面，也是在此时悄然的裂开一道小小的裂纹。</p><p>　　嗡嗡！</p><p>　　恐怖的力量冲击之下，韩山他们顿时见到，在那石碑之上，青铜灯之中立即有着火苗出现，旋即噗噗噗的点燃声音不断的响起。</p><p>　　一盏盏青铜灯迅速的被点燃！</p><p>　　短短一息，六盏青铜灯，同时被点燃！</p><p>　　而在第六盏青铜点燃后，那第七盏青铜灯中，火星也是开始迅速的涌现。最后在那一道道震惊的目光中凝聚起来，噗的一声，便是燃烧而起。</p><p>　　“竟然点燃第七盏青铜灯了！”炼体塔内，惊呼声响彻起来，所有强者都是一脸的难以置信，因为牧尘点燃第七盏青铜灯的速度，竟然比韩山还快！</p><p>　　韩山的神色同样是在此时一变，旋即他死死的盯着那第八盏青铜灯，虽然那里一片漆黑，但他却是隐隐的感觉到。牧尘这次的力量，似乎还没完。</p><p>　　而也就是在韩山这般死盯之下，那第八盏的漆黑持续了数息，而后终于是有着一点火星出现…</p><p>　　墨锋与宗腾也是见到那一点火星。当即都是忍不住的吸了一口凉气，牧尘此次的力量，竟然还能够在第八盏青铜灯内出现火星？！</p><p>　　这可是之前韩山都未曾办到的事情啊！</p><p>　　滴答。</p><p>　　鲜血不断的从牧尘拳头上滴落下来，白骨隐现，但他却是纹丝不动，那犹如黄金般的拳头之下。金光涟漪依旧在冲击开来，疯狂的冲入那黑色石碑之中。</p><p>　　嗤嗤！</p><p>　　第八盏青铜灯内，原本微弱的火星，也就是在此时，出现了第二点火星…第三点火星…</p><p>　　一点点火星在韩山他们逐渐睁大的眼睛中凝现出来，最后终于是汇聚到了极致，噗的一声，化为火焰，熊熊燃烧起来。</p><p>　　第八盏青铜灯，点燃！</p><p>　　韩山他们的神色在此时显得有些滞涩，他们怔怔的望着那燃烧起来的第八盏青铜灯，再看了看那石碑前如磐石般的年轻身影，内心的震动，不言而喻。</p><p>　　谁能想到，牧尘竟然能够将第八盏青铜灯都是点燃！</p><p>　　他那一拳的力量，究竟该有多恐怖？！</p><p>　　那等力量，恐怕就算是他们，都得动用所用的力量来应对吧？</p><p>　　炼体塔内塔外，都是在那燃烧起来的第八盏青铜灯下，变得安静下来…</p><p>　　不过，也就是在他们都是因为震惊而有些失语时，那黑色石碑之前，牧尘那被渲染成金色的眸子盯着石碑，拳头上传来的剧痛几乎被他忽略，他的脑海也是因为那种极限般的力量，从而变得有些空空荡荡。</p><p>　　但不知道为何，他的本能却是告诉他，这还并没有结束！</p><p>　　他能够隐隐的感觉到，他之前那一拳轰进黑色石碑的力量，他还能够将它们控制，犹如一种极为奇特的暗劲。</p><p>　　它们如果爆发，还将会造成一段更为惊人的破坏力。</p><p>　　说不定，便是能够将那第九盏青铜灯也是点燃！</p><p>　　金光自牧尘的双目中喷射而出，旋即他再没有任何的犹豫，拳头狠狠的按在石碑碑面上，然后沙哑的声音，从其喉咙间低低的传出来。</p><p>　　“给我爆！”</p><p>　　好若书吧,看书之家！唯一网址:</p>
    # #                                   </div>
    # #                 <script>bdshare();</script>
    # #                 <div style="width:910px;margin:0px auto;" id="cbad"><table id="ctad2"><tr>
    # #                     <td id="adt4"><script type="text/javascript">cad4();</script></td>
    # #                     <td id="adt5"><script type="text/javascript">cad5();</script></td>
    # #                     <td id="adt6"><script type="text/javascript">cad6();</script></td>
    # #                     </tr></table>
    # #                 </div>
    # #                 <div class="bottem2">
    # #                     <a href="javascript:;" onclick="showpop('/modules/article/uservote.php?id=9&ajax_request=1');">投推荐票</a> <a href="https://www.biquge5200.cc/0_7/167373106.html">上一章</a> &larr; <a href="https://www.biquge5200.cc/0_7/">章节目录</a> &rarr; <a href="https://www.biquge5200.cc/0_7/167373113.html">下一章</a> <a href="javascript:pl('7','167373111');">加入书签</a>
    # #                 </div>
    # #             </div>
    # #         </div>
    # #         <div class="footer">
    # #             <div class="footer_link">&nbsp;新书推荐：<a href='/2_2599/' >全职法师</a>
    # #                 <a href='/9_9365/' style='font-weight:bold'>盖世帝尊</a>
    # #                 <a href='/46_46254/' >斗战狂潮</a>
    # #                 <a href='/53_53081/' >都市超级医圣</a>
    # #                 <a href='/0_494/' style='font-weight:bold'>超级兵王</a>
    # #                 <a href='/0_491/' >俗人回档</a>
    # #                 <a href='/44_44186/' style='font-weight:bold'>人皇纪</a>
    # #                 <a href='/2_2691/' >寒门崛起</a>
    # #                 <a href='/0_419/' >无敌天下</a>
    # #             </div>
    # #             <div class="footer_cont">
    # #                 <script>footer();right();dl();</script>
    # #                 <!--<script>mark();</script>-->
    # #                 <div class="reader_mark1"><a href="javascript:;" onclick="pl(article_id, chapter_id);"></a></div>
    # #                 <div class="reader_mark0"><a href="javascript:;" onclick="tj('1', article_id);"></a></div>
    # #             </div>
    # #         </div>
    # #     </div>
    # #     <script type="text/javascript">ac("1", "7");</script>
    # # </body>
    # # </html>
    # #
    # #
    # # Process finished with exit code 0
    # #
    # # '''
    bookdoc = etree.HTML(html)
    a = ''.join(bookdoc.xpath("//div[@id='content']/p/text()"))
    with open(bookname+'.txt','a+',encoding='utf-8') as f:
        f.write(a)


# requests.get()


