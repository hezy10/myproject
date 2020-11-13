# coding=utf-8
import re
import requests
from lxml import etree
import pymysql
con = pymysql.connect(host='localhost',user='root',password='123456',database='pachong',charset='utf8')
cur = con.cursor()

url = 'https://www.qk365.com/room/81686'
# ret = requests.get(url).text
html = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/青客2.py"
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="applicable-device" content="pc" />
	<meta http-equiv="Cache-Control" content="no-transform " />
	<title>【浦东新区】 2号线 创新中路 唐镇 培元新苑 朝南_上海培元新苑_青客时尚租房网</title>
<meta name="keywords" content="浦东新区唐镇租房,培元新苑租房,青客,时尚租房,上海租房">
<meta name="description"
	content="青客时尚租房,上海知名租房基地,提供浦东新区 唐镇 培元新苑房源信息,2号线 创新中路 唐镇 培元新苑拎包即住,青客让租房变得简单，咨询热线：400-8198-365。"><link rel="Shortcut Icon" href="https://www.qk365.com/favicon.ico?version=20191206" type="image/x-icon" />
	<link rel="alternate" media="only screen and (max-width: 640px)" href="https://i.qk365.com/sh/easy/81686" />
	<link href="https://www.qk365.com/css/grab.css?version=20171229" rel="stylesheet" type="text/css" />
	<link rel="stylesheet" href="https://www.qk365.com/css/slider/jquery.slider.css" type="text/css" />
	<link rel="stylesheet" href="https://g.alicdn.com/de/prismplayer/2.7.2/skins/default/aliplayer-min.css" type="text/css" />
</head>
<body>
<input type="hidden" id="romIdHidden" value="81686"/>
<input type="hidden" id="cucIdHidden" value="24224"/>
<input type="hidden" id="cutIdHidden" value=""/>
<input type="hidden" id="cucLongitude" value="121.676166"/>
<input type="hidden" id="cucLatitude" value="31.21619"/>
<input type="hidden" value="0" id="romState" />
<input type="hidden" id="prcName" value="浦东新区"/>
<input type="hidden" id="romAddressRough" value=""/>
<input type="hidden" id="lineid" value=""/>
<input type="hidden" id="cucSubWay" value="创新中路"/>
<input type="hidden" id="romAdminId" name="romAdminId" value="17861"/>
<input type="hidden" id="videoUrl" value="http://qk365-nct-out-001.oss-cn-hangzhou.aliyuncs.com/Act-ss-mp4-ld/e11d5ddf53b449a1a2c5d60a8f698d71/A0081439A0.mp4"/>
<input type="hidden" id="coupon_type" value=""/>
<input type="hidden" id="couponType"/>
<input type="hidden" id="is_img_code" value="0"/>
<input type="hidden" id="is_new_user" value="0"/>
<input type="hidden" id="issend" value="0"/>
<input type="hidden" id="cucVillage" value="培元新苑"/>
<!-- 头部 -->
<meta name="renderer" content="webkit" />
<link href="https://www.qk365.com/css/reset.css?v=20191205" rel="stylesheet" type="text/css">
<link href="https://www.qk365.com/css/style.css?v=20200901" rel="stylesheet" type="text/css">
<link href="https://www.qk365.com/css/head
.css?v=20191204" rel="stylesheet" type="text/css">
<link href="https://www.qk365.com/css/footer.css?v=20191204" rel="stylesheet" type="text/css">
<link href="https://www.qk365.com/css/user.css?version=20191205" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="https://www.qk365.com/css/packet.css?version=20180124" type="text/css">

<script type="text/javascript">
	function checkMobile() {
		return navigator.userAgent
						.match(/iphone|android|phone|mobile|wap|netfront|x11|java|opera mobi|opera mini|ucweb|windows ce|symbian|symbianos|series|webos|sony|blackberry|dopod|nokia|samsung|palmsource|xda|pieplus|meizu|midp|cldc|motorola|foma|docomo|up.browser|up.link|blazer|helio|hosin|huawei|novarra|coolpad|webos|techfaith|palmsource|alcatel|amoi|ktouch|nexian|ericsson|philips|sagem|wellcom|bunjalloo|maui|smartphone|iemobile|spice|bird|zte-|longcos|pantech|gionee|portalmmm|jig browser|hiptop|benq|haier|^lct|320x320|240x320|176x220/i) != null;
	}
	(function() {
		cur_url = document.URL;
		if (checkMobile()) {
			if (cur_url=="https://www.qk365.com/"||cur_url=="https://www.qk365.com") {
				window.location.href = "https://i.qk365.com/";
			} else if (cur_url=="https://sz.qk365.com/"||cur_url=="https://sz.qk365.com") {
				window.location.href = "https://i.qk365.com/su";
			} else if (cur_url=="https://hz.qk365.com/"||cur_url=="https://hz.qk365.com") {
				window.location.href = "https://i.qk365.com/hz";
			} else if (cur_url=="https://bj.qk365.com/"||cur_url=="https://bj.qk365.com") {
				window.location.href = "https://i.qk365.com/bj";
			} else if (cur_url=="https://jx.qk365.com/"||cur_url=="https://jx.qk365.com") {
				window.location.href = "https://i.qk365.com/jx";
			} else if (cur_url=="https://nj.qk365.com/"||cur_url=="https://nj.qk365.com") {
				window.location.href = "https://i.qk365.com/nj";
			} else if (cur_url=="https://wh.qk365.com/"||cur_url=="https://wh.qk365.com") {
				window.location.href = "https://i.qk365.com/wh";
			}
		}
	})();
</script>

<div class="headNav">
    <div class="headLeft">
        <a class="logo" title="上海租房" href="https://www.qk365.com/">
        	<img src="https://www.qk365.com/images/2019-11-29-img/logo.png" alt="上海租房" />
        </a>
        <div class="popup">上海</div>
				<div class="popupHide">
				<a href="https://www.qk365.com" title="上海租房" onclick="this.href=getCityChangeUrl('https://www.qk365.com');">上海</a>
				<a href="https://sz.qk365.com" title="苏州租房" onclick="this.href=getCityChangeUrl('https://sz.qk365.com');">苏州</a>
				<a href="https://hz.qk365.com" title="杭州租房" onclick="this.href=getCityChangeUrl('https://hz.qk365.com');">杭州</a>
				<a href="https://bj.qk365.com" title="北京租房" onclick="this.href=getCityChangeUrl('https://bj.qk365.com');">北京</a>
				<a href="https://jx.qk365.com" title="嘉兴租房" onclick="this.href=getCityChangeUrl('https://jx.qk365.com');">嘉兴</a>
				<a href="https://nj.qk365.com" title="南京租房" onclick="this.href=getCityChangeUrl('https://nj.qk365.com');">南京</a>
				<a href="https://wh.qk365.com" title="武汉租房" onclick="this.href=getCityChangeUrl('https://wh.qk365.com');">武汉</a>
				<a href="https://tj.qk365.com" title="天津租房" onclick="this.href=getCityChangeUrl('https://tj.qk365.com');">天津</a>
				</div>
		</div>
    
    <div class="headRight">
        <div class="phone">
			<p class="ph1">&nbsp;看房热线：8:00~22:00</p>
			<p class="ph2">400-8198-365</p>
		</div>

        <ul class="subnav">
            <li>
                <button class="subnav-top">房屋出租</button>
                <div class="dropnav">
                    <a href="https://www.qk365.com/list" title="上海轻松找房">轻松找房</a>
                    <a href="https://www.qk365.com/xiaoqu" title="上海小区租房">小区租房</a>
                    <a href="https://www.qk365.com/todaySpecial" title="上海今日特惠">今日特惠</a>
                    <a href="https://www.qk365.com/bus" title="上海公交沿线租房">公交找房</a>
                </div>
            </li>
            <li>
                <a href="https://www.qk365.com/map" target="_blank" class="subnav-top" title="上海租房地图找房">地图找房</a>
            </li>
            <li>
                <a href="https://www.qk365.com/fwtg" target="_blank" rel="nofollow" class="subnav-top" title="上海租房房屋托管">房屋托管</a>
            </li>
            <li>
                <button class="subnav-top">商务合作</button>
                <div class="dropnav">
                    <a href="https://www.qk365.com/supplier/index" rel="nofollow" title="上海租房商务合作">商务合作</a>
                    <a href="https://www.qk365.com/to/jsp_government" rel="nofollow" title="上海政府视窗">政府视窗</a>
                </div>
            </li>
            <li>
                <button class="subnav-top">青客快讯</button>
                <div class="dropnav">
                    <a href="https://www.qk365.com/qkkx/index.html" title="上海租房">快讯首页</a>
                    <a href="https://www.qk365.com/qkkx/zfgl/index.html" title="上海租房找房攻略">找房攻略</a>
                    <a href="https://www.qk365.com/qkkx/hydt/index.html" title="上海租房行业动态">行业动态</a>
                    <a href="https://www.qk365.com/qkkx/ssrd/index.html" title="上海租房时事热点">时事热点</a>
                    <a href="https://www.qk365.com/qkkx/sqgl/index.html" title="上海租房省钱攻略">省钱攻略</a>
                    <a href="https://www.qk365.com/qkkx/bmxx/index.html" title="上海租房便民信息">便民信息</a>
                    <a href="https://www.qk365.com/qkkx/zzhd/index.html" title="上海租房组织活动">组织活动</a>
                    <a href="https://www.qk365.com/mail.do" rel="nofollow" title="鸡毛信">鸡毛信</a>
                    </div>
            </li>
            <li>
                <button class="subnav-top">移动青客</button>
                <div class="dropnav">
                    <a href="https://www.qk365.com/qkkx/zthd/2019/7627932.html">下载APP</a>
                    <a href="https://i.qk365.com/sh">手机官网</a>
						</div>
            </li>
            
            <li class="" id="noLogin">
                <a href="https://www.qk365.com/security/register" id="loginli" class="subnav-top" rel="nofollow">注册登录<em></em></a>
            </li>
            <li class="userico" id="loginIn" style="display: none">
                <a href="javascript:;" class="subnav-top pepSnapLogin"><i></i>注册登录</a>
                <div class="dropnav">
                    <a href="javascript:;" id="topMyData">我的资料</a>
					<a href="https://www.qk365.com/security/reservation.do">我的预约</a>
					<a href="https://www.qk365.com/security/subscribe.do">我的订阅</a>
					<a href="https://www.qk365.com/security/userCouponsActivities.do">我的优惠券</a>
					<a href="https://www.qk365.com/security/collection.do">我的收藏</a>
					<a href="javascript:;" id="logout">退出</a>
                </div>
            </li>
        </ul>
        <div class="clearfix"></div>
    </div>
</div>
<div class="house_cur">
	<div class="w1200 clearfix">
		<div class="easyCurve">
			<span>您当前的位置：</span>
			<div id="topnanv">
				<div id="anvlfteb">
					<div class="posbox">
							<a title="上海租房" href="https://www.qk365.com">上海租房</a>
								</div>
					<em>></em>
						<div class="posbox">
							<a title="轻松找房" href="https://www.qk365.com/list">轻松找房</a>
								</div>
					<em>></em>
						<div class="posbox">
							<a title="浦东新区租房" href="https://www.qk365.com/list/a14">浦东新区租房</a>
								</div>
					<em>></em>
						<div class="posbox">
							<a title="唐镇租房" href="https://www.qk365.com/list/a14-k177">唐镇租房</a>
								</div>
					<em>></em>
						<div class="posbox">
							<a title="培元新苑租房" href="https://www.qk365.com/xiaoqu/v27081">培元新苑租房</a>
								</div>
					<em>></em>
						<div class="posbox">
							房间详情</div>
					<em>&gt;</em>
					<div class="posbox poscolor">房间编号：A0081438B</div>
				</div>
				<div id="seledbox" class="posiabox">
					<div class="area areaCur">
								<a title="苏州租房" href="https://sz.qk365.com" target="_blank">苏州租房</a>
								<a title="杭州租房" href="https://hz.qk365.com" target="_blank">杭州租房</a>
								<a title="北京租房" href="https://bj.qk365.com" target="_blank">北京租房</a>
								<a title="嘉兴租房" href="https://jx.qk365.com" target="_blank">嘉兴租房</a>
								<a title="南京租房" href="https://nj.qk365.com" target="_blank">南京租房</a>
								<a title="武汉租房" href="https://wh.qk365.com" target="_blank">武汉租房</a>
								<a title="天津租房" href="https://tj.qk365.com" target="_blank">天津租房</a>
								</div>
						<div class="area">
								<a title="小区找房" href="https://www.qk365.com/xiaoqu" target="_blank">小区找房</a>
								<a title="地图找房" href="https://www.qk365.com/map" target="_blank">地图找房</a>
								<a title="今日特惠" href="https://www.qk365.com/todaySpecial" target="_blank">今日特惠</a>
								<a title="公交沿线租房" href="https://www.qk365.com/bus/" target="_blank">公交沿线租房</a>
								</div>
						<div class="area">
								<a title="黄浦区租房" href="https://www.qk365.com/list/a3" target="_blank">黄浦区租房</a>
								<a title="徐汇区租房" href="https://www.qk365.com/list/a4" target="_blank">徐汇区租房</a>
								<a title="长宁区租房" href="https://www.qk365.com/list/a5" target="_blank">长宁区租房</a>
								<a title="静安区租房" href="https://www.qk365.com/list/a6" target="_blank">静安区租房</a>
								<a title="普陀区租房" href="https://www.qk365.com/list/a7" target="_blank">普陀区租房</a>
								<a title="闸北区租房" href="https://www.qk365.com/list/a8" target="_blank">闸北区租房</a>
								<a title="虹口区租房" href="https://www.qk365.com/list/a9" target="_blank">虹口区租房</a>
								<a title="杨浦区租房" href="https://www.qk365.com/list/a10" target="_blank">杨浦区租房</a>
								<a title="闵行区租房" href="https://www.qk365.com/list/a11" target="_blank">闵行区租房</a>
								<a title="宝山区租房" href="https://www.qk365.com/list/a12" target="_blank">宝山区租房</a>
								<a title="嘉定区租房" href="https://www.qk365.com/list/a13" target="_blank">嘉定区租房</a>
								<a title="金山区租房" href="https://www.qk365.com/list/a15" target="_blank">金山区租房</a>
								<a title="松江区租房" href="https://www.qk365.com/list/a16" target="_blank">松江区租房</a>
								<a title="青浦区租房" href="https://www.qk365.com/list/a17" target="_blank">青浦区租房</a>
								<a title="奉贤区租房" href="https://www.qk365.com/list/a18" target="_blank">奉贤区租房</a>
								<a title="崇明区租房" href="https://www.qk365.com/list/a19" target="_blank">崇明区租房</a>
								<a title="卢湾区租房" href="https://www.qk365.com/list/a26" target="_blank">卢湾区租房</a>
								<a title="上海花桥租房" href="https://sz.qk365.com/list/a37-k353" target="_blank">上海花桥租房</a>
								</div>
						<div class="area">
								<a title="八佰伴租房" href="https://www.qk365.com/list/a14-k153" target="_blank">八佰伴租房</a>
								<a title="北蔡租房" href="https://www.qk365.com/list/a14-k154" target="_blank">北蔡租房</a>
								<a title="曹路租房" href="https://www.qk365.com/list/a14-k156" target="_blank">曹路租房</a>
								<a title="川沙租房" href="https://www.qk365.com/list/a14-k157" target="_blank">川沙租房</a>
								<a title="航头租房" href="https://www.qk365.com/list/a14-k159" target="_blank">航头租房</a>
								<a title="花木租房" href="https://www.qk365.com/list/a14-k160" target="_blank">花木租房</a>
								<a title="惠南镇租房" href="https://www.qk365.com/list/a14-k161" target="_blank">惠南镇租房</a>
								<a title="金杨地区租房" href="https://www.qk365.com/list/a14-k163" target="_blank">金杨地区租房</a>
								<a title="康桥/周浦租房" href="https://www.qk365.com/list/a14-k164" target="_blank">康桥/周浦租房</a>
								<a title="陆家嘴租房" href="https://www.qk365.com/list/a14-k168" target="_blank">陆家嘴租房</a>
								<a title="三林地区租房" href="https://www.qk365.com/list/a14-k173" target="_blank">三林地区租房</a>
								<a title="外高桥租房" href="https://www.qk365.com/list/a14-k179" target="_blank">外高桥租房</a>
								<a title="新场租房" href="https://www.qk365.com/list/a14-k181" target="_blank">新场租房</a>
								<a title="源深体育中心租房" href="https://www.qk365.com/list/a14-k184" target="_blank">源深体育中心租房</a>
								<a title="张江租房" href="https://www.qk365.com/list/a14-k185" target="_blank">张江租房</a>
								<a title="王港租房" href="https://www.qk365.com/list/a14-k367" target="_blank">王港租房</a>
								<a title="御桥租房" href="https://www.qk365.com/list/a14-k588" target="_blank">御桥租房</a>
								<a title="高行租房" href="https://www.qk365.com/list/a14-k589" target="_blank">高行租房</a>
								<a title="周浦万达租房" href="https://www.qk365.com/list/a14-k2314" target="_blank">周浦万达租房</a>
								<a title="周浦租房" href="https://www.qk365.com/list/a14-k5609" target="_blank">周浦租房</a>
								<a title="江镇租房" href="https://www.qk365.com/list/a14-k5612" target="_blank">江镇租房</a>
								<a title="浦东周边租房" href="https://www.qk365.com/list/a14-k5625" target="_blank">浦东周边租房</a>
								</div>
						<div class="area">
								<a title="保利金色唐城租房" href="https://www.qk365.com/xiaoqu/v1392" target="_blank">保利金色唐城租房</a>
								<a title="保利御樽苑租房" href="https://www.qk365.com/xiaoqu/v1404" target="_blank">保利御樽苑租房</a>
								<a title="华昌小区租房" href="https://www.qk365.com/xiaoqu/v2414" target="_blank">华昌小区租房</a>
								<a title="东唐苑租房" href="https://www.qk365.com/xiaoqu/v1483" target="_blank">东唐苑租房</a>
								<a title="庆利苑租房" href="https://www.qk365.com/xiaoqu/v24049" target="_blank">庆利苑租房</a>
								<a title="金唐公寓租房" href="https://www.qk365.com/xiaoqu/v1692" target="_blank">金唐公寓租房</a>
								<a title="唐丰苑租房" href="https://www.qk365.com/xiaoqu/v2026" target="_blank">唐丰苑租房</a>
								<a title="毕加索小镇租房" href="https://www.qk365.com/xiaoqu/v1406" target="_blank">毕加索小镇租房</a>
								<a title="齐友佳苑租房" href="https://www.qk365.com/xiaoqu/v1900" target="_blank">齐友佳苑租房</a>
								<a title="金融家租房" href="https://www.qk365.com/xiaoqu/v5266" target="_blank">金融家租房</a>
								<a title="金利公寓租房" href="https://www.qk365.com/xiaoqu/v1681" target="_blank">金利公寓租房</a>
								<a title="瀚盛家园租房" href="https://www.qk365.com/xiaoqu/v1548" target="_blank">瀚盛家园租房</a>
								<a title="创新佳苑租房" href="https://www.qk365.com/xiaoqu/v1443" target="_blank">创新佳苑租房</a>
								<a title="绿波城租房" href="https://www.qk365.com/xiaoqu/v1803" target="_blank">绿波城租房</a>
								<a title="齐爱佳苑租房" href="https://www.qk365.com/xiaoqu/v1899" target="_blank">齐爱佳苑租房</a>
								</div>
						<div class="area">
								</div>
						</div>
			</div>
			<span class="curveLast"></span>
			<div class="clear"></div>
		</div>
		<div class="houShare">
			<div class="Rshare"><em class="fL">分享到：</em>
				<a href="http://v.t.sina.com.cn/share/share.php?url=http%3A%2F%2FWWW.baidu.com&title=青客公寓就是家" target="_blank"  class="houSina" rel="nofollow">&nbsp;</a>
				<!-- <a href="http://share.v.t.qq.com/index.php?c=share&a=index&url=http%3A%2F%2Fshare.baidu.com%2F%230-tqq-1-88853-89b7933b38b0586d98eb9d131fa70b46&title=青客公寓就是家&appkey=801cf76d3cfc44ada52ec13114e84a96" target="_blank" class="houWeibo" rel="nofollow">&nbsp;</a> -->
				<a href="http://connect.qq.com/widget/shareqq/index.html?url=http%3A%2F%2Fshare.baidu.com%2Fcode%230-sqq-1-14275-9737f6f9e09dfaf5d3fd14d775bfee85&title=青客公寓就是家&desc=青客公寓就是家&summary=&site=baidu" target="_blank"  class="houQQ" rel="nofollow">&nbsp;</a>
				<a href="javascript:void(0)" class="houWeixin" >
					<div class="hweiBox hide">
						<span class="HweixinCon"><img alt="上海租房" src="https://www.qk365.com/images/weixin02.jpg?v=20190222"  /></span>
						<em class="tips_03"></em>
					</div>
				</a>
				<a href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=http%3A%2F%2Fshare.baidu.com%2F%230-qzone-1-68471-d020d2d2a4e8d1a374a433f596ad1440&title=青客公寓就是家&desc=&summary=&site=" target="_blank" class="houQzone" rel="nofollow">&nbsp;</a>
			</div>
		</div>
	</div>
</div>
<div class="houseWrap">
	<div class="houseimgBox">
		<div class="houseScrollbox" id="box1">
			<ul class="houseboxList">
				<li type_data="0">
					<a href="javascript:void(0)"><img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B0/CgoKaFxGSc-AKLGPAABksKGFeYI466.jpg" width="75px" height="44px" onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/></a>
					<p class="housemaskBox"></p></li>
				<li type_data="1">
					<a href="javascript:void(0)"><img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B0/CgoKaFxGSdCAUfwCAABFGUQM1Zk163.jpg" width="75px" height="44px" onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/></a>
					<p class="housemaskBox"></p></li>
				<li type_data="2">
					<a >
								<img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B1/CgoKZ1xGSc6AUgzyAABlJ9GDHQw336.jpg" width="75px" height="44px" id="fengmian"
								onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
								<div id='J_prismPlayer' class='prism-player'>
							</div>
							</a>
							<div class="playBig" id="playBig">
								<img alt="上海培元新苑租房图" src="https://www.qk365.com/images/play03.png" id="play_pic">
							</div>
						<p class="housemaskBox"></p></li>
				<li type_data="3">
					<a href="javascript:void(0)"><img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B0/CgoKaFxGSdKAGS54AABM0cAcDJo932.jpg" width="75px" height="44px" onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/></a>
					<p class="housemaskBox"></p></li>
				<li type_data="4">
					<a href="javascript:void(0)"><img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B0/CgoKaFxGSdOAYUSaAACY829Cd7g977.jpg" width="75px" height="44px" onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/></a>
					<p class="housemaskBox"></p></li>
				<li type_data="5">
					<a href="javascript:void(0)"><img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/DC/CgoKZ1xGUU-ALM6YAACy3Q5t3pQ347.jpg" width="75px" height="44px" onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/></a>
					<p class="housemaskBox"></p></li>
				<li type_data="6">
					<a href="javascript:void(0)"><img alt="上海培元新苑租房图" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/DC/CgoKZ1xGUU6ANkYuAACfKzYzyLQ942.jpg" width="75px" height="44px" onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/></a>
					<p class="housemaskBox"></p></li>
				</ul>
		</div>
		<a href="javascript:void(0)" class="housGol" id="hougol1"></a>
		<a href="javascript:void(0)" class="housGor" id="hougor1"></a>
	</div>
	</div>

<div class="w1200 houseInfo clearfix">
	<!-- 修改start -->
	<div class="HouInfoL">
		<h1 class="houInfoTit">
			【浦东新区】地铁2号线 创新中路站 培元新苑 精装白领公寓 朝南主卧出租 配备齐全</h1>
		
		<div class="houExpenses">
			<em>近地铁</em>
				<em>优选</em>
					<em>主卧</em>
					<em>0中介费</em>
			<em>立即可租</em>
			<p class="houBtn">
				<a id="collectLink"><label id="collect" ></label></a>
			</p>
			<div class="rob-snap" style="display:none" id="rob-snap"></div>
			
			<form action="" id="collection">
				<input type="hidden" name="collectionRoom.encodedUserId" id="encodedUserId" value=""/>
				<input type="hidden" name="collectionRoom.colRomId" value="81686"/>
				<input type="hidden" name="collectionRoom.colRomTitle" value="【浦东新区】地铁2号线 创新中路站 培元新苑 精装白领公寓 朝南主卧出租 配备齐全"/>
				<input name="currStrategy" id="currStrategy" type="hidden"value="" />
			</form>
		</div>
		<dl class="houSurvey clearfix">
		   <div class="survey-left fL">
		   		<dd><span>原　　价：</span>3230元/月</dd>
				<dd><span>面　　积：</span>以现场勘察为准</dd>
				<dd><span>朝　　向：</span>
				<em>朝南</em>
				</dd>
				<dd><span>楼　　层：</span>7 / 17层</dd>
				<dd><span>小区名称：</span><a title="培元新苑租房" href="https://www.qk365.com/xiaoqu/v27081"
				target="_blank">培元新苑</a></dd>
			</div>
			
			<div class="survey-right fR">
				<dd><span>房间编号：</span>A0081438B</dd>
				<dd><span>地　　铁：</span>
				<a title="2号线租房" href="https://www.qk365.com/list/s2" target="_blank">2号线</a>
					<a title="创新中路租房" href="https://www.qk365.com/list/s2-e2025" target="_blank">创新中路</a>&nbsp;
				<a title="2号线租房" href="https://www.qk365.com/list/s2" target="_blank">2号线</a>
					<a title="唐镇租房" href="https://www.qk365.com/list/s2-e2024" target="_blank">唐镇</a>&nbsp;
				<a title="2号线租房" href="https://www.qk365.com/list/s2" target="_blank">2号线</a>
					<a title="华夏东路租房" href="https://www.qk365.com/list/s2-e2026" target="_blank">华夏东路</a>&nbsp;
				</dd>
				<dd class="clearfix"><span>公　　交：</span>
					<div class="bus-line">
					<p>
							<a title="机口村租房" href="https://www.qk365.com/bus/10382262" target="_blank">机口村</a>
							<i>，</i>
							<a title="浦东17路租房" href="https://www.qk365.com/bus/line-21510/" target="_blank" >浦东17路</a>
							</p>
					<p>
							<a title="顾唐路齐爱路租房" href="https://www.qk365.com/bus/10480504" target="_blank">顾唐路齐爱路</a>
							<i>，</i>
							<a title="1099路租房" href="https://www.qk365.com/bus/line-20529/" target="_blank" >1099路</a>
							</p>
					</div>
				</dd>
				<dd><span>所在区域：</span>
				<a title="浦东新区租房" href="https://www.qk365.com/list/a14" target="_blank">浦东新区</a>&nbsp;&nbsp;
				<a title="唐镇租房" href="https://www.qk365.com/list/a14-k177" target="_blank">唐镇</a>
				</dd>
			</div>
		</dl>
		<ul class="houSet clearfix">
			<p>房屋配置：具体配置以现场实际情况为准</p>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKZ13511WAKCQkAAALQeaaADU811.jpg?version=20191205"></i>
						<em>床</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKaF3514SAAwIHAAAKQeiK7s0643.jpg?version=20191205"></i>
						<em>宽带</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKaF3514SAbehVAAAKr8yAAPM791.jpg?version=20191205"></i>
						<em>冰箱</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKZ13514OAXFMpAAAL63rB5DY484.jpg?version=20191205"></i>
						<em>洗衣机</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKaF3514SABMv5AAALxL_ait8570.jpg?version=20191205"></i>
						<em>空调</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKaF3514SAN_NHAAALJxIxdS8304.jpg?version=20191205"></i>
						<em>热水器</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKZ13514OAUAUVAAAK7_G53t8960.jpg?version=20191205"></i>
						<em>微波炉</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/48/CgoKZ1351_6ATRfJAAAMEGfKJeI453.jpg?version=20191205"></i>
						<em>智能锁</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKZ13514SAANX8AAAK8Eq_Rbc742.jpg?version=20191205"></i>
						<em>床头柜</em>
					</li>
				<li>
						<i><img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/46/CgoKaF3514OAR0R9AAALEPc8v48866.jpg?version=20191205"></i>
						<em>衣柜</em>
					</li>
				</ul>
	</div>
	<div class="HouInfoR">
		<div class="houPrice"> <!--VIP价显示-->
			<div class="price_txt">
				<em>￥</em>
				<h4>2415</h4>
				<i>元/月起</i>
			</div>
			<!-- <p class="price_sm">具体可享受的优惠请咨询服务中心</p> -->
		</div>
		<!--   特价显示-->
		<!-- 双十一、跨年感恩节 广告位 start -->
		<a style="display:none" onclick="activityViewCount(1,'房间详情页广告入口','PC电商');" class="rob-advert" href="https://www.qk365.com/special/rentingSeason?roomDetail" target="_blank">
			<img src="https://www.qk365.com/img/rentingSeason.jpg?version=20180329" />
		</a>
		<!-- 双十一、跨年感恩节 广告位 end -->
		<a class="rob-advert" href="javascript:;" target="_blank">
				<img src="https://oss-wuxi.qk365.com/qingkepic/M00/27/CD/CgoKZ1zT2iqAMYdjAAA-IU5boLg426.png">
			</a>
		<dl class="houTopInfo clearfix">
			<dt><a href="/security/reservation.do?romId=81686&forward=/security/reservation.do?romId=81686"><div class="houTopIcon01"><span>预约看房<em>Reservation</em></span></div></a></dt>
			<dd><a href="javascript:void (0);"><div class="houTopIcon02"><span class="look_wdsy">我的室友<em>My roommate</em></span></div></a></dd>
		</dl>
		<div class="sharePhone">
			<div class="houPhone">400-8198-365</div>
			<p class="houShareText"><em style="margin: 0 40px;">20人浏览</em> | <em style="margin: 0 40px;">16人已预约看房</em>
			</p>
		</div>
		<div class="ljdf">
		    <div class="ljdf-btn" id="ljdf-btn"></div>
		    <div class="flip-wx">
				<div class="flip-box">
					<div class="wx-pic" id="qrcode"></div><br>
					<p>使用手机青客app或微信扫码订房</p>
				</div>
			</div>
		</div>
	</div>
	<!-- 修改over -->
</div>
<!-- 新增弹窗开始 -->
<div class="tk">
	<div class="tk_content">
		<h1>
		    <span>可租通知</span>
			<img id="tk_close" alt="上海租房" src="https://www.qk365.com/images/dlet.png">
		</h1>
		<p class="p1">请如实填写，我们会尽快联系您</p>
		<p class="p2">
			<span class="redb">*</span>
			<span class="black18">您的姓名</span>
			<input type="text" name="tk_userName" id="tk_userName" value="">
		</p>
        <p class="p2">
            <span class="redb">*</span>
            <span class="black18">图形验证码</span>
            <input type="text" name="tk_captcha" id="tk_captcha" value="" style="margin-left: 2px;">
            <img src="https://www.qk365.com/security/captcha.do" id="captchaImg"  style="display: block;float: none;margin-left: 108px;margin-top: 20px;cursor: pointer;">
        </p>
		<p class="p2">
			<span class="redb">*</span>
			<span class="black18">手机号码</span>
			<input type="text" name="tk_phoneNumber" id="tk_phoneNumber" value="">
			<button type="button" id="smsSend" style="cursor: pointer;" onclick="sendSmCode(this,'tk_phoneNumber','commonsm');">发送验证码</button>
		</p>
		<p class="p2">
			<span class="redb">*</span>
			<span class="black18">验证码</span>
			<input class="iup" type="text" name="tk_code" id="tk_code">
		</p>
		<p class="p2">
			<span class="black18">&nbsp;&nbsp;备注</span>
			<textarea  cols="20" id="tk_remarks"></textarea>
		</p>
		<button type="submit" onclick="submit()">提交</button>
	</div>
</div>

<div class="houseMain clearfix">
	<div class="w1200">
		<div class="HouInfoL">
			<ul class="houseMainList">
				<li class="cur"><span>基本信息</span></li>
				<li><span>周边配套</span></li>
				<li><span>扫码关注</span></li>
			</ul>
			<div class="houseMainPanle">
				<div class="houmCon">
				<div class="houmSide">
					<!-- 增加over -->
					<p>青客，中国公共租赁住房提供商，成熟运作模式，服务范围覆盖上海、苏州、杭州、南京、北京、武汉、嘉兴七大城市，管辖近10万余间客房，覆盖各城市地铁沿线。三大认证，锁定靠谱室友；网上缴费，轻松生活；智能门锁，保证安全；Wifi覆盖，时尚方便；标配齐全，拎包即住；非中介，0手续费，租房咨询热线 ：400-8198-365。</p>
					<div class="houmTab">
						<table cellpadding="0" cellspacing="0" border="0" width="100%">
							<thead>
							<tr>
								<th class="houLine">房间</th>
								<th>租金</th>
								<th>状态</th>
								<th>可租日期</th>
								<th>室友</th>
								<th>窗户</th>
								<th>阳台</th>
								<th>独立卫生间</th>
							</tr>
							</thead>
							<tbody>
							<tr>
									<td class="houLetter houLine">
								     <a  href="https://www.qk365.com/room/81686">B房间</a>
								</td>

									<td>3230元/月</td>
									<td class="houRent houRent_dz">
											<em><a href="https://www.qk365.com/room/81686">待租</a></em>
										</td>
									<td class="houRent_dz">随时可租</td>
										<td class="houPerson">
									</td>
									<td><img  src="https://www.qk365.com/images/chum-icon4.png?version=20191205" />
										</td>

									<td></td>
									<td></td>
								</tr>
							<tr>
									<td class="houLetter houLine">
								     <a  href="https://www.qk365.com/room/81687">A房间</a>
								</td>

									<td>3346元/月</td>
									<td class="houRent">
											<em><a href="https://www.qk365.com/room/81687">已租</a></em>
										</td>
									<td>2021-08-01</td>
										<td class="houPerson">
									<img  src="https://www.qk365.com/images/icon_11.png?version=20191205" />
									</td>
									<td></td>

									<td><img  src="https://www.qk365.com/images/chum-icon4.png?version=20191205"  />
									</td>
									<td></td>
								</tr>
							<tr>
									<td class="houLetter houLine">
								     <a  href="https://www.qk365.com/room/81688">C房间</a>
								</td>

									<td>2676元/月</td>
									<td class="houRent houRent_dz">
											<em><a href="https://www.qk365.com/room/81688">待租</a></em>
										</td>
									<td class="houRent_dz">随时可租</td>
										<td class="houPerson">
									</td>
									<td><img  src="https://www.qk365.com/images/chum-icon4.png?version=20191205" />
										</td>

									<td></td>
									<td></td>
								</tr>
							</tbody>
						</table>
						</div>
				</div>
				<div class="houmSide hide">
					<dl class="rimList">
						<dd class="margin_t0"><span class="rimIcon rimIcon01">购物</span><span class="rimInfo">家乐福超市 唐镇地铁购物广场 联华超市 华联超市</span></dd>
						<dd><span class="rimIcon rimIcon02">休闲</span><span class="rimInfo">家乐福超市 唐镇地铁购物广场 联华超市 华联超市</span></dd>
						<dd><span class="rimIcon rimIcon03">医院</span><span class="rimInfo">曙光医院 张江卫生院 江浦门诊</span></dd>
						<dd><span class="rimIcon rimIcon04">交通</span><span class="rimInfo"></span></dd>
					</dl>
				</div>

				<div class="houmSide hide">
					<span class="weiBox">
						<img alt="上海租房" src="https://www.qk365.com/images/weixin01.jpg"/>
						<h3 class="weiTit">青客APP</h3>
						<p class="weiCon">让您的租房过程化繁为简，一步到位，扫码立即下载</p>
					</span>
					<span class="weiBox">
						<img alt="上海租房" src="https://www.qk365.com/images/weixin02.jpg?v=20190222" />
						<h3 class="weiTit">青客微信</h3>
						<p class="weiCon">衣食住行、热点资讯、房源信息，扫码应有尽有</p>
					</span>
					<span class="weiBox weixXCX">
						<img alt="上海租房" src="https://www.qk365.com//images/code-qkzf.jpg">
						<h3 class="weiTit">微信小程序</h3>
						<p class="weiCon">地铁边、租得起、有管家的青客公寓，微信扫码立即找房</p>
					  </span>
				</div>
			</div>
				<div class="houTreaty">
				<div class="">
					<h3 class="treatyTit">地理位置</h3>
					<div class="f_more_map" style="width:100%;">
						<ul class="fmap_top" id="fmap_top">
							<li class="on" id="bt1" style="cursor:pointer">餐饮</li>
							<li id="bt2" style="cursor:pointer">超市</li>
							<li id="bt3" style="cursor:pointer">影院</li>
							<li id="bt4" style="cursor:pointer">酒店</li>
							<li id="bt5" style="cursor:pointer">地铁站</li>
							<li id="bt6" style="cursor:pointer">学校</li>
							<li id="bt7" style="cursor:pointer">银行</li>
							<li id="bt8" style="cursor:pointer">医院</li>
							<li id="bt9" style="cursor:pointer">景点</li>
							<li id="bt10" style="cursor:pointer">加油站</li>
						</ul>
						<div id="_map" class="_map"></div>
						<div class="mapOperate">
							<div class="mapOp1 clearfix">
								<p class="op_go op_active" onclick="roomDetailMap.switchPosition('end')">到这里去</p>
								<p class="op_from" onclick="roomDetailMap.switchPosition('start')">从这里出发</p>
								<p class="op_site" onclick="roomDetailMap.houseLocation()">定位当前房源</p>
							</div>
							<div class="mapOp2 clearfix">
								<input type="text" placeholder="请输入有效的地址名称" id="suggestId" maxlength="50">
								<p id="busMap" >公交</p>
								<p id="walkMap" >步行</p>
								<p id="driveMap" >驾车</p>
							</div>
						</div>
					</div>
				</div>
				<h3 class="treatyTit">租房公约</h3>
				<div class="houtreaCon">
					<p>各位青年才俊：</p>
					<br />
					<p>欢迎入住人才公寓，为了让家更美好，让我们共同营造一个安全、舒适、愉快的居住环境。请庄严的承诺：“我，我们是好人！我们到过的地方，见过的人，在我们离开以后会比我们来之前更美好！”</p>
					<br />
					<h3>一、好人的承诺</h3>
					<br />
					<p>1、好人是可爱的，任何时候先给周围的人一个微笑。因为我们是好人，所以一定要多做好事，哪怕很小的好事，同时绝不给周围的人添麻烦。</p>
					<p>2、好人是守法的，盗窃公用区域电力是违法犯罪行为，好人绝不违法。</p>
					<p>3、好人是高素质的，绝对不在公寓门厅、过道等公共部位放置私人物品。</p>
					<p>4、好人是讲卫生的，公寓保洁员每周打扫一次公共区域，平时请大家自行保持整洁的环境，顺手带走公共区域的垃圾，个人的生活垃圾只放在房间内的垃圾桶里，并及时扔进小区的垃圾箱。</p>
					<p>5、好人是受邻居爱戴的，为保持安静的环境，请大家在走廊、电梯厅内不要大声喧哗，音响、电视、电脑等发声设备请调到适当的音量，以免影响其他邻居的休息。</p>
					<br />
					<h3>二、好人勇于承担责任</h3>
					<br />
					<p>1、好人不给别人找麻烦，请大家保管好自己的门卡，离开房间哪怕是上洗手间、洗澡、串门请带好自己的门卡。万一没带门卡进不了门，你可以通过青客公寓APP自助开门，也可拨打4008198365热线，我们每月将为您提供3次免费的临时密码紧急开门服务，之后每次享受开门服务需支付50元服务费。各位千万记住，避免类似情况发生，因为大家都很麻烦。</p>
					<p>2、好人不会让下水道堵塞，淋浴时一定拉好浴帘，以防水溢出。如有毛发堵塞下水地漏口，随手清理。</p>
					<p>3、好人保持马桶清洁通畅，绝不把报纸、卫生巾、避孕套、塑料袋丢入马桶以免堵塞，使用洗衣机洗衣服前一定把口袋内的纸张、硬币等取出，以免堵塞洗衣机下水口或者损坏洗衣机。如因前述原因损坏洗衣机、堵塞马桶或者下水道的，请悄悄地自费修理。如向管理方报修，对于人为原因造成的损害由入住人员均摊修理费用。</p>
					<p>4、好人自力更生，请经常留意个人账户上电和水的余量，当少于50度时立即自助购电。购电到供电有若干小时时间差，尽请谅解。你也可到服务中心自助购电，服务中心购电及时到账。公寓的修理工作是自助式的，如果遇到家具和设备损坏需要报修的，管理方提供3种报修方式：青客公寓（最快）、QQ报修（中等）、电话报修（奇慢无比）。QQ报修时间是上午9点至下午9点。4008198365电话报修时电信运营方收取相应市话费，并且电话排队等待较长。强烈推荐使用青客公寓APP免费报修。人为损坏的维修费用见价格表。</p>
					<p>5、好人及时支付自己的账单，入住前请先登陆青客公寓APP。房租、电费、水费、宽带费、修理费、我们会在系统里开列账单收取，你垫付的修理费我们会在系统上向你退还。青客公寓APP可以使用支付宝、微信、青客宝支付账单。</p>
					<p>6、好人一生平安，务必随时更新你的个人信息，尤其是你的手机和电子邮箱如有变化请第一时间在青客公寓APP上进行修改。否则管家送你的礼物和惊喜就不能及时送达了。祝好人生活愉快！</p>
				
				</div>
			</div>
			</div>
			<p class="houAll"><span class="HouDown">查看全部</span></p>
		</div>
		<div class="HouInfoR">
			<div class="hinfoRborder">
				<p class="stewardPhoto">
					<a title="上海租房房管员朱晓杰1" href="https://www.qk365.com/roomAdmin/17861">
						<img alt="上海租房房管员朱晓杰1" src="https://www.qk365.com/images/houseHead.jpg?version=20191205"/>
						</a>
				</p>
				<p class="stewPhotName">
					<a title="上海租房房管员朱晓杰1" style="color: #333333;"
					   href="https://www.qk365.com/roomAdmin/17861">
						房管员：朱晓杰1</a>
				</p>
				<p class="stewPhotinfo">房源数量：<em>25间</em> 服务青客：<em>36人</em> 近30天出房：<em>8间</em></p>
				<!--新增房屋备案编码开始-->
				<!--新增房屋备案编码结束-->
				<p class="stewTel">400 8198 365</p>
			</div>
			<p class="serviceAim"><em>服务宗旨</em>由衷欢迎您与您的家人朋友入住我们的公寓，
				我们将竭诚为您服务！</p>
			<div class="hinfoRborder clearfix">
				<h3 class="AimTit">青客向您保证</h3>
				<div class="AimTopCon clearfix">
<span class="aCon02">保洁承诺</span>
					<span class="aCon03">维修承诺</span>
				</div>
				<p class="aimSubText">青客服务全程保障您的权益，租客认证、一客一锁解决您在租房过程中各种担忧，专人保洁、专业维修免除您在居住期间的后顾之忧。通过投诉全公示、400热线等确保您的权益得到落实。</p>
				<ul class="aimList">
					<li>
						<p><em class="num_01 fL">ONE</em><span class="fR aimLine"></span></p>
						<div class="aimText">租客认证 凡有意向入住青客的租客，需要提供相关证明，通过我们的租客认证。</div>
					</li>
					<li>
						<p><em class="num_02 fL">TWO</em><span class="fR aimLine"></span></p>
						<div class="aimText">一客一锁 每间房间都设置不同的密码锁，电子控制。</div>
					</li>
					<li>
						<p><em class="num_03 fL">THREE</em><span class="fR aimLine"></span></p>
						<div class="aimText">专人保洁 为了给青客客户创造品质的租住生活，每周2次公共区域保洁。</div>
					</li>
					<li>
						<p><em class="num_04 fL">FOUR</em><span class="fR aimLine"></span></p>
						<div class="aimText">专业维修 青客针对房屋主体，电路，灯具等提供24小时内响应，48小时上门，三个工作日完成的维修服务</div>
					</li>
				</ul>
			</div>
		</div>
	</div>
</div>

<div id="sidebarRig">
	<ul>
		<li>
			<span class="sidebarBox">
                <div class="sideFadeIn">
                    <div id="SideBox01">
                        <div class="tit">
                            <img src="https://www.qk365.com/images/index/sidebar1.png" />
                            <h3>关注青客</h3>
                        </div>
                        <div class="scan scan0">
                            <p><img src="https://www.qk365.com/images/Side/wxImg02.png" /></p>
                            <p>扫描二维码</p>
                            <p>下载APP</p>
                        </div>
                    </div>
                </div>
                <img src="https://www.qk365.com/images/index/sidebar1.png" width="53" height="45" class="sideFadeOut" />
            </span>
        </li>
        <li>
            <span class="sidebarBox">
                <div class="sideFadeIn">
                    <div id="SideBox02">
                        <a class="tit" href="https://www.qk365.com/fwtg" target="_blank">
                            <img src="https://www.qk365.com/images/index/sidebar2.png" />
                            <h3>房屋托管</h3>
                        </a>
                    </div>
                </div>
                <img src="https://www.qk365.com/images/index/sidebar2.png" width="53" height="45" class="sideFadeOut" />
            </span>
        </li>
        <li>
            <span class="sidebarBox">
                <div>
                    <div id="SideBox03">
                        <a class="tit" target="_blank" href="javascript:;" onclick="onKST();">
                            <img src="https://www.qk365.com/images/index/sidebar3.png" />
                            <h3>在线咨询</h3>
                        </a>
                    </div>
                </div>
            </span>
        </li>
        <li>
            <span class="sidebarBox">
                <div class="sideFadeIn">
                    <div id="SideBox04">
                        <div class="tit">
                            <span><img src="https://www.qk365.com/images/index/sidebar4.png" /></span>
                            <h3>租客需求</h3>
                        </div>
                        <div class="text">
                            <textarea name="mydiyue" id="mydiyue" onclick="changeShowList(this)">求租火车站附近房源</textarea>
                        </div>
                        <div class="submit">
                            <form id="mail">
                                <input type="submit" onclick="diyue_center('https://www.qk365.com/security/subscribe.do');" value="确认" />
                            </form>
                        </div>
                    </div>
                </div>
                <img src="https://www.qk365.com/images/index/sidebar4.png"  class="sideFadeOut" />
            </span>
        </li>
        <li id="sidebarTop">
            <span class="sidebarBox" id="top_btn">
                <div class="sideFadeIn" >
                    <img src="https://www.qk365.com/images/index/top-arrow2.png"/>
                    <h3>TOP</h3>
                </div>
                <img src="https://www.qk365.com/images/index/top-arrow2.png"  class="sideFadeOut" />
            </span>
        </li>
    </ul>
</div><script>
	var cityName = "上海";
	var basePath = "https://www.qk365.com/";
	var detailURL = "room/"
	var currPage = 1;
	var totalPageNumber = parseInt((49) / 4 + 1);
	function changeBatches(obj) {
		if (currPage >= totalPageNumber) {
			return
		}
		var _src = $(obj).find("img").attr("src");
		$(obj).find("img").attr("src",basePath+"images/change.gif");

		currPage = ++currPage;
		var endRecord = currPage * 4;
		var indexRecord = endRecord - 4;
		var roomsHtml = "";
		
			var count = 1
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82223">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/97/CgoKZ1xG0nCATYRPAABrxbWA12k081.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82223">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3313.28元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1840';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 2
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81661">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/FA/CgoKZ1xGVpWABcEpAACO5Wzg2i0153.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81661">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2670.73元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：1938';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 3
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81720">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/24/CgoKaFxGvnqALbAnAACgxRb1-_s716.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81720">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2785.26元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 4
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81985">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/1F/CgoKZ1xGMROAbTAUAABw4xSTJP8070.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/81985">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3240.67元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 5
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/89988">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/EF/CgoKaFxGtR-AVVJ4AAB69AXwfRc860.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="青客，中国公共租赁住房提供商，成熟运作模式，服务范围覆盖上海、苏州、杭州、南京、北京、武汉、嘉兴七大城市，管辖近10万余间客房，覆盖各城市地铁沿线。新客首次入住可享受三天免费退房。三大认证，锁定靠谱室友；网上缴费，轻松生活；智能门锁，保证安全；Wifi覆盖，时尚方便；标配齐全" href="https://www.qk365.com/room/89988">';
							roomsHtml +='<span class="loveTit"> 青客，中国公共租赁住房提供......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2773.23元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1585';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 6
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82070">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/BA/CgoKZ1xGe46AKTDPAABvXC-yM-8936.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82070">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3343.51元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1915';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 7
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82358">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/FD/CgoKZ1xGVwqAESLqAABr6PhPPjc063.JPG" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82358">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3243.97元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1835';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 8
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/83643">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/BC/CgoKaFxGe_2AIBwEAABvQZ8tA9Y663.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/83643">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3234.93元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 9
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81558">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/24/CgoKZ1xGXdGAdaleAAB8iguWlkI615.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="真实房源、真实价格管家陪同带看；房租月付减轻住房压力，轻松租房入住无忧；每周保洁阿姨打扫、管家服务、免费维修家电家具。" href="https://www.qk365.com/room/81558">';
							roomsHtml +='<span class="loveTit"> 真实房源、真实价格管家陪同......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2798.85元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1469';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 10
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82074">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A3/DB/CgoKZ1xHP_qAIW_rAABh9I_g5nI466.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82074">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2695.03元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1600';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 11
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82790">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B0/CgoKZ1xGSbOAc0KjAABY-yUiCEg130.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82790">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2672.9元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1552';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 12
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81158">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/A9/CgoKaFxGHM-AcRjLAABqOBtTpeY179.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81158">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3165.05元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1800';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 13
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/83650">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/22/CgoKaFxGviSAGWWEAABj2OS3O7U256.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="欢迎入住人才公寓，为了让家更美好，让我们共同营造一个安全、舒适、愉快的居住环境。请庄严的承诺：“我，我们是好人！我们到过的地方，见过的人，在我们离开以后会比我们来之前更美好！”" href="https://www.qk365.com/room/83650">';
							roomsHtml +='<span class="loveTit"> 欢迎入住人才公寓，为了让家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3209.6元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 14
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81710">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/AB/F5/CgoKZ1xI00KAbcGOAABrqA7gyts826.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/81710">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3076.03元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1850';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 15
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82027">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/03/CgoKaFxGuL-ACnjLAABZSnVf57c421.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/82027">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3168.57元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 16
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/84128">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/C6/CgoKaFxGIdKAIKcsAAB4ulOiO68250.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/84128">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3001.02元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2395';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 17
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82861">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/C1/CgoKaFxGTNeAGITdAABlhyyV93Y245.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="便捷的交通，专业的客服，贴心的售后，房间定时保洁，不收取中介费；宜家的装修风格，配套齐全，幽静的环境，绿化面积大；品牌家电，专业的维修与售后。" href="https://www.qk365.com/room/82861">';
							roomsHtml +='<span class="loveTit"> 便捷的交通，专业的客服，贴......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3232.41元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2545';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 18
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82570">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/03/CgoKZ1xGuKSAHtL_AABx63d0_rY051.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82570">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3344.11元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1940';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 19
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/84289">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/EF/CgoKaFxGtQeAPyv9AAB9_AdlAP0920.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/84289">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2563.77元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1510';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 20
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81682">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/8C/CgoKaFxGQ4yAHd4PAAB9ch3SI4Y318.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="小区周边生活设施全，公交站、超市、便利店、菜市场；无任何隐藏费用；水、电、网络、家具和电器全都配置齐全，让您拎包即可入住。" href="https://www.qk365.com/room/81682">';
							roomsHtml +='<span class="loveTit"> 小区周边生活设施全，公交站......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2680.59元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：1938';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 21
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/94652">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/EF/CgoKaFxGtRKAcS44AAB9Ga6FenY289.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="便捷的交通，专业的客服，贴心的售后，房间定时保洁，不收取中介费；宜家的装修风格，配套齐全，幽静的环境，绿化面积大；品牌家电，专业的维修与售后。" href="https://www.qk365.com/room/94652">';
							roomsHtml +='<span class="loveTit"> 便捷的交通，专业的客服，贴......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2824.07元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1615';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 22
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82472">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/96/CgoKZ1xGGV2ACdyNAACPP4_q03E921.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82472">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2818.73元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 23
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81750">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B1/CgoKaFxGSfaAP9edAABbtl5POng140.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/81750">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3080.52元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2395';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 24
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/92759">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/24/CgoKZ1xGvlCAd3FAAACXVoAEyvk932.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/92759">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2774.24元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 25
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82355">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/01/CgoKaFxGV_CAfPMtAABgDrkWq7w227.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82355">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3165.42元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 26
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/83638">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/B5/CgoKaFxGHteAH9ZlAACDcCHWLDU849.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/83638">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2866.47元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 27
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/84449">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/AB/CgoKZ1xGHSOAY8o2AABt2UzZKdc360.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/84449">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3274.87元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2515';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 28
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82316">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/8B/CgoKaFxGQ4CARmVeAAB1f1V6iYw151.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82316">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2598.71元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：1938';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 29
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81587">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/32/CgoKZ1xGNHqAAiL4AABxjCXmzfc575.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/81587">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3078.45元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2395';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 30
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/83972">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/32/CgoKZ1xGNHyAU1A7AABxjCXmzfc078.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/83972">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3079.26元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2395';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 31
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/83988">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/AB/80/CgoKaFxIvfaAfQDgAABxlOhcncU131.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="房间装修时尚清爽大方，干净整洁，酒店式管理；家电齐全，靠谱室友，房间配备齐全，拎包入住；出门就是地铁口，多路公交四通八达交通方便，好房不等人，欢迎您的来电！" href="https://www.qk365.com/room/83988">';
							roomsHtml +='<span class="loveTit"> 房间装修时尚清爽大方，干净......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3229.81元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2475';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 32
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81688">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B1/CgoKZ1xGSdCAIbLeAABkgYm_WuM099.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/81688">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2675.71元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：1938';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 33
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/85595">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/30/CgoKaFxGYByAOoHZAABuf68puMI927.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="青客，中国公共租赁住房提供商，成熟运作模式，服务范围覆盖上海、苏州、杭州、南京、北京、武汉、嘉兴七大城市，管辖近10万余间客房，覆盖各城市地铁沿线。新客首次入住可享受三天免费退房。" href="https://www.qk365.com/room/85595">';
							roomsHtml +='<span class="loveTit"> 青客，中国公共租赁住房提供......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3217.03元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：1870';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 34
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/85738">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/CA/CgoKZ1xGTjmAOqLWAACK_eWVxko920.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="真实房源、真实价格管家陪同带看；房租月付减轻住房压力，轻松租房入住无忧；每周保洁阿姨打扫、管家服务、免费维修家电家具。" href="https://www.qk365.com/room/85738">';
							roomsHtml +='<span class="loveTit"> 真实房源、真实价格管家陪同......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2759.46元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 35
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/95485">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/04/CgoKZ1xGuNiACnhFAABluQBfVX4490.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/95485">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3336.93元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='特价：2033';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 36
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82071">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/96/CgoKaFxG0maAXKjLAAB1f1V6iYw223.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82071">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2674.35元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：1938';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 37
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81718">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/24/CgoKaFxGvn2APUCsAABqf__4uDE815.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81718">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3147.98元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 38
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82580">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/00/CgoKZ1xGuBCAHoJIAABj4_-eV3s626.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82580">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2617.11元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：1938';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 39
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81572">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/72/CgoKaFxGP0KAPLMXAABynfLfaRk825.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81572">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3078.76元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2395';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 40
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82287">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/02/CgoKZ1xGuJCAE-wVAABeW_YeYd8093.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82287">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3156.1元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 41
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82512">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/F4/CgoKZ1xGKWuAdnzHAAB3WxVj6xw409.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82512">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3071.32元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2395';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 42
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/85128">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/AB/F4/CgoKZ1xI0zSAGPOgAABwbJXtS1s039.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/85128">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2864.28元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 43
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82601">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/81/CgoKZ1xGb-iAGJcwAAByGDLh2-E702.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82601">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3233.92元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 44
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82602">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/81/CgoKZ1xGb-uAP0fiAAB6GCzg4SY076.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82602">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3384.03元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2545';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 45
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82613">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/FF/CgoKaFxGV4GATKj7AACTvo2HvuE427.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82613">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2802.46元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 46
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/82490">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/13/CgoKZ1xGLueAEHHFAABm5qs68TU131.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82490">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2696.32元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2047';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 47
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/84287">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B0/CgoKaFxGScqAFnHJAABrBgqgHH4268.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/84287">';
							roomsHtml +='<span class="loveTit"> 非中介，精装地铁房，有管家......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3089.02元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 48
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/84448">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9D/AB/CgoKZ1xGHSGAT6V6AABvQZ8tA9Y512.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/84448">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">3163.04元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2415';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 49
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81764">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/F7/CgoKaFxGVkiAXJK4AAB8se5eaz0336.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81764">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2799.86元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2091';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
			var count = 50
			if (count > indexRecord && count <= endRecord) {
				roomsHtml +='<li>';
				roomsHtml +='<a title="上海培元新苑租房" href="https://www.qk365.com/room/81999">';
					
						roomsHtml +='<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9F/7F/CgoKaFxGb5GAK6YuAABe2JxWY8U005.jpg" title="上海培元新苑租房"';
						
							roomsHtml +='alt="上海培元新苑租房"';
						
						roomsHtml +='onerror="this.src=\'https://www.qk365.com/images/pic_01.jpg\'"/> ';
					
							roomsHtml +='</a>';
							roomsHtml +='<a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81999">';
							roomsHtml +='<span class="loveTit"> 我们的住房服务给您一个温暖......';
							
							roomsHtml +='</span></a>';
							//roomsHtml +='<em class="loveMoney">2686.37元/月</em>';
							roomsHtml +='<em class="loveMoney">';
                        	
									roomsHtml +='VIP价：2082';
								
							roomsHtml +='元/月</em>';
							
							
									roomsHtml +='<a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>';
								
				roomsHtml +="</li>";
			}
		
		if (currPage == totalPageNumber) {
			currPage = 0;
		}
		$("#interestRoomsUl").html(roomsHtml);
	}
</script>
<!-- 猜你喜欢 -->
<div class="houseLoveBox">
    <div class="houseLove">
        <ul class="houseLoveList">
            <li class="cur houseLove-cnxh"><span>猜你喜欢</span><div class="houseChange" onclick="changeBatches(this)">换一批 <img src="https://www.qk365.com/images/change.png" /></div></li>
            <li class="houseLove-jqck"><span>近期查看</span></li>
        </ul>
        <div class="houseLoveCon clearfix">
            <div class="houseLoveSide">
                <ul class="houseConList clearfix" id="interestRoomsUl">
                    <li>
                                <a title="上海培元新苑租房" href="https://www.qk365.com/room/82223">
                                    <img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/97/CgoKZ1xG0nCATYRPAABrxbWA12k081.jpg"  title="上海培元新苑租房"
                                             alt="上海培元新苑租房" onerror="this.src='https://www.qk365.com/images/pic_01.jpg'"/>
                                    </a>
                                <a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/82223">
									<span class="loveTit"> 非中介，精装地铁房，有管家......</span>
                                </a>
                                <em class="loveMoney">
                                	
											特价：1840元/月
                                </em>
                                <a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">
		                                    培元新苑</a>
								   </li>
                    <li>
                                <a title="上海培元新苑租房" href="https://www.qk365.com/room/81661">
                                    <img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/FA/CgoKZ1xGVpWABcEpAACO5Wzg2i0153.jpg"  title="上海培元新苑租房"
                                             alt="上海培元新苑租房" onerror="this.src='https://www.qk365.com/images/pic_01.jpg'"/>
                                    </a>
                                <a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81661">
									<span class="loveTit"> 我们的住房服务给您一个温暖......</span>
                                </a>
                                <em class="loveMoney">
                                	
											VIP价：1938元/月
                                </em>
                                <a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">
		                                    培元新苑</a>
								   </li>
                    <li>
                                <a title="上海培元新苑租房" href="https://www.qk365.com/room/81720">
                                    <img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/24/CgoKaFxGvnqALbAnAACgxRb1-_s716.jpg"  title="上海培元新苑租房"
                                             alt="上海培元新苑租房" onerror="this.src='https://www.qk365.com/images/pic_01.jpg'"/>
                                    </a>
                                <a title="我们的住房服务给您一个温暖的家，为了每一位住客能住的舒心，我们免费安排每周2-3次专业保洁，并24小时的工程部、维修部和客服部服务。" href="https://www.qk365.com/room/81720">
									<span class="loveTit"> 我们的住房服务给您一个温暖......</span>
                                </a>
                                <em class="loveMoney">
                                	
											VIP价：2091元/月
                                </em>
                                <a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">
		                                    培元新苑</a>
								   </li>
                    <li>
                                <a title="上海培元新苑租房" href="https://www.qk365.com/room/81985">
                                    <img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/1F/CgoKZ1xGMROAbTAUAABw4xSTJP8070.jpg"  title="上海培元新苑租房"
                                             alt="上海培元新苑租房" onerror="this.src='https://www.qk365.com/images/pic_01.jpg'"/>
                                    </a>
                                <a title="非中介，精装地铁房，有管家的青年社区，配贴心小管家性价比高，网上缴费，轻松生活，智能门锁保证安全；小区绿化率高，周边配套完善，随时看房，随时入住。" href="https://www.qk365.com/room/81985">
									<span class="loveTit"> 非中介，精装地铁房，有管家......</span>
                                </a>
                                <em class="loveMoney">
                                	
											VIP价：2415元/月
                                </em>
                                <a title="上海培元新苑租房" class="loveSubtext" href="https://www.qk365.com/xiaoqu/v27081">
		                                    培元新苑</a>
								   </li>
                    </ul>
            </div>
            <div class="houseLoveSide clearfix hide">
                <ul class="houseConList clearfix">
                    </ul>
                <div align="center">
                        <p style="font-size: 25px; color: #666666; padding: 100px;">暂无查看记录</p>
                    </div>
                </ul>
            </div>
        </div>
    </div>
</div><script src="https://www.qk365.com/js/jquery-1.11.0.min.js"></script>
<script type="text/javascript">
	var titleindex = '1';
	if(titleindex==''){
		titleindex = 0;
	}
	$(document).ready(function(){
		$("#titleindex"+titleindex).addClass("active");
		});
	var basePathUrl = 'https://www.qk365.com/';
	var eliveBasePath = 'http://www.qk365.com/';
	var cmsPathUrl = 'http://www.qk365.com/news/';
	var htmlPath = 'http://www.qk365.com/news/';
	$(function(){ initfunction(); });
</script>
	<!-- 视频播放  -->
<script src="https://g.alicdn.com/de/prismplayer/2.7.2/json/json.min.js"></script>
<script src="https://g.alicdn.com/de/prismplayer/2.7.2/aliplayer-min.js"></script>
<script src="https://www.qk365.com/js/roomdetail/qkplayer.js"></script>
<script src="https://www.qk365.com/js/roomdetail/roomdetail.js?v=20200901"></script>
<script src="https://www.qk365.com/js/qrcode.js"></script>
<script src="https://www.qk365.com/js/homepage/autoFill.js"></script>
<script src="https://www.qk365.com/js/homepage/homepage.js"></script>
<script src="https://www.qk365.com/js/public/public.js?v=20181025"></script>
		
<script src="https://www.qk365.com/js/jquery.nicescroll.min.js"></script>
<script src="https://www.qk365.com/js/jquery-migrate-1.2.1.min.js"></script>
<script src="https://www.qk365.com/js/jquery-ui-1.10.4.custom.js"></script>
<script src="https://www.qk365.com/js/jquery.weather.js"></script>
<script src="https://www.qk365.com/js/common/tab.js"></script>
<script src="https://www.qk365.com/js/jquery.form.js"></script>
<script src="https://www.qk365.com/js/select.js?v=20181019"></script>
<script src="https://www.qk365.com/js/init_bill.js?v=20190528"></script>

<script src="https://www.qk365.com/js/roomdetail/map.js?v=20190807"></script>
<script src="https://www.qk365.com/js/roomdetail/findrooms.js?v=20181119"></script>
<script src="https://www.qk365.com/js/dubbo11/coupon.js?v=20180601"></script>
<script src="https://www.qk365.com/js/hide-box.js"></script>

<script src="https://www.qk365.com/js/activityViewCount.js"></script>
<script type="text/javascript" src="https://www.qk365.com/js/houseView360.js?v=20171225"></script>
<script type="text/javascript" src="https://www.qk365.com/js/slider/jquery.slider.min.js"></script>
<script type="text/javascript" src="https://www.qk365.com/js/common/math.uuid.js"></script>
<script type="text/javascript" src="https://www.qk365.com/js/rentingseason/registerdiv.js?v=20180205"></script>
<script type="text/javascript" src="https://www.qk365.com/js/rentingseason/roomdetaillabel.js?v=20180202"></script>
<script type="text/javascript" src="https://www.qk365.com/js/jquery.qrcode.min.js"></script>
<script src="https://www.qk365.com/js/roomdetail/fjxq.js?v=20190909"></script>
<!-- flowLay -->
<div class="flowLay">
    <div class="flowList">
        <span class="flowIcon01"><em>挑选房屋</em></span>
        <div class="flowIcon02"><span><em>支付定金或者预定看房</em></span></div>
        <div class="flowIcon03"><span><em>了解入住须知</em></span></div>
        <div class="flowIcon04"><span><em>签约付款</em></span></div>
        <span class="flowIcon05"><em>开始入住</em></span>
    </div>
</div>
<!-- footer -->
<div class="footer">
    <div class="w1170">
        <div class="w1170Tab">
            <div class="w1170TabMenu clearfix">
                <ul>
                    <li>上海热门区县租房<i></i></li>
						<li>上海热门小区租房<i></i></li>
					<li>相关城市租房<i></i></li>
					</ul>
                <div class="phone">
                    <p class="SerSubTit">服务热线</p>
                    <p class="serPhone pB20">400-8198-365</p>
                </div>
</div>
            <div class="w1170TabBox">
                <div class="tabBox1">
                    <div class="fotLink">
                    	<a title="崇明租房" href="https://www.qk365.com/list/a19" target="_blank"> 崇明租房</a>
								
									|
								<a title="长宁租房" href="https://www.qk365.com/list/a5" target="_blank"> 长宁租房</a>
								
									|
								<a title="杨浦租房" href="https://www.qk365.com/list/a10" target="_blank"> 杨浦租房</a>
								
									|
								<a title="浦东租房" href="https://www.qk365.com/list/a14" target="_blank"> 浦东租房</a>
								
									|
								<a title="徐汇租房" href="https://www.qk365.com/list/a4" target="_blank"> 徐汇租房</a>
								
									|
								<a title="松江租房" href="https://www.qk365.com/list/a16" target="_blank"> 松江租房</a>
								
									|
								<a title="青浦租房" href="https://www.qk365.com/list/a17" target="_blank"> 青浦租房</a>
								
									|
								<a title="上海周边租房" href="https://sz.qk365.com/list/a37" target="_blank"> 上海周边租房</a>
								
									|
								<a title="虹口租房" href="https://www.qk365.com/list/a9" target="_blank"> 虹口租房</a>
								
									|
								<a title="黄浦租房" href="https://www.qk365.com/list/a3" target="_blank"> 黄浦租房</a>
								
									|
								<a title="闵行租房" href="https://www.qk365.com/list/a11" target="_blank"> 闵行租房</a>
								
									|
								<a title="金山租房" href="https://www.qk365.com/list/a15" target="_blank"> 金山租房</a>
								
									|
								<a title="普陀租房" href="https://www.qk365.com/list/a7" target="_blank"> 普陀租房</a>
								
									|
								<a title="卢湾租房" href="https://www.qk365.com/list/a26" target="_blank"> 卢湾租房</a>
								
									|
								<a title="嘉定租房" href="https://www.qk365.com/list/a13" target="_blank"> 嘉定租房</a>
								
									|
								<a title="闸北租房" href="https://www.qk365.com/list/a8" target="_blank"> 闸北租房</a>
								
									|
								<a title="静安租房" href="https://www.qk365.com/list/a6" target="_blank"> 静安租房</a>
								
									|
								<a title="奉贤租房" href="https://www.qk365.com/list/a18" target="_blank"> 奉贤租房</a>
								</div>
                </div>
                <div class="tabBox2">
                    <div class="fotLink">
                    	<a title="松江登云苑租房" href="https://www.qk365.com/xiaoqu/v2878" target="_blank">松江登云苑租房</a>
								
								 |
								<a title="旭辉城租房" href="https://www.qk365.com/xiaoqu/v2889" target="_blank">旭辉城租房</a>
								
								 |
								<a title="崧泽绿地租房" href="https://www.qk365.com/xiaoqu/v2013" target="_blank">崧泽绿地租房</a>
								
								 |
								<a title="沁富佳苑租房" href="https://www.qk365.com/xiaoqu/v1909" target="_blank">沁富佳苑租房</a>
								
								 |
								<a title="宝山佳境苑租房" href="https://www.qk365.com/xiaoqu/v2554" target="_blank">宝山佳境苑租房</a>
								
								 |
								<a title="德宁苑租房" href="https://www.qk365.com/xiaoqu/v2523" target="_blank">德宁苑租房</a>
								
								 |
								<a title="唐家苑租房" href="https://www.qk365.com/list/i%E5%94%90%E5%AE%B6%E8%8B%91-h%E5%94%90%E5%AE%B6%E8%8B%91" target="_blank">唐家苑租房</a>
								
								 |
								<a title="金海华城永华苑租房" href="https://www.qk365.com/xiaoqu/v2825" target="_blank">金海华城永华苑租房</a>
								
								 |
								<a title="张江樟盛苑租房" href="https://www.qk365.com/xiaoqu/v2535" target="_blank">张江樟盛苑租房</a>
								
								 |
								<a title="登云苑租房" href="https://www.qk365.com/xiaoqu/v2878" target="_blank">登云苑租房</a>
								
								 |
								<a title="塘泾南苑租房" href="https://www.qk365.com/xiaoqu/v2441" target="_blank">塘泾南苑租房</a>
								
								 |
								<a title="馨香三期灯辉公寓租房" href="https://www.qk365.com/xiaoqu/v6862" target="_blank">馨香三期灯辉公寓租房</a>
								</div>
                </div>
                <div class="tabBox3">
                    <div class="fotLink">
                    	<a title="上海租房" href="https://www.qk365.com/list" target="_blank">上海租房</a>
							
								|
							<a title="苏州租房" href="https://sz.qk365.com/" target="_blank">苏州租房</a>
							
								|
							<a title="杭州租房" href="https://hz.qk365.com/" target="_blank">杭州租房</a>
							
								|
							<a title="北京租房" href="https://bj.qk365.com/" target="_blank">北京租房</a>
							
								|
							<a title="南京租房" href="https://nj.qk365.com/" target="_blank">南京租房</a>
							
								|
							<a title="武汉租房" href="https://wh.qk365.com/" target="_blank">武汉租房</a>
							</div>
                </div>
                </div>

            <!-- service -->
            <div class="service clearfix">
                <div class="w1170">
                    <div class="QcoL5 fL">
                        <ul class="serviceList">
                            <li>
                                <p>关于青客</p>
								<a title="青客公司简介" href="https://www.qk365.com/qkkx/about/2018/1.html?gsjj" rel="nofollow">公司简介</a>
								<a title="青客上海网站地图" href="https://www.qk365.com/qkkx/about/2018/5.html?wzdh">网站地图</a>
				                <a title="联系青客上海租房" href="https://www.qk365.com/qkkx/about/2018/3.html?lxwm" rel="nofollow">联系我们</a>
								<a title="加入青客" href="https://www.qk365.com/qkkx/about/2018/2.html?qkzp" rel="nofollow">加入我们</a>
								<a title="上海租房小区专题" href="https://www.qk365.com/xiaoqu/xqjh">小区专题</a>
								<a title="隐私政策" href="https://www.qk365.com/qkkx/about/2019/7628049.html?yszc">隐私政策</a>
								</li>
                            <li>
                                <p>新手指南</p>
                                <a title="青客上海租房注册方式" href="https://www.qk365.com/qkkx/service/2018/8.html?zcfs" target="_blank" rel="nofollow">注册方式</a>
								<a title="青客上海租房租房流程" href="https://www.qk365.com/qkkx/service/2018/10.html?zflc" target="_blank" rel="nofollow">租房流程</a>
<a title="青客上海租房在线报修" href="https://www.qk365.com/qkkx/service/2018/13.html?zxbx" target="_blank" rel="nofollow">在线报修</a>
                            </li>
                            <li>
                                <p>租期服务</p>
                                <a title="青客上海租房400服务" href="https://www.qk365.com/qkkx/service/2018/21.html?400fw" target="_blank" rel="nofollow">400服务</a>
								<a title="青客上海租房保洁服务" href="https://www.qk365.com/qkkx/service/2018/22.html?bjfw" target="_blank" rel="nofollow">保洁服务</a>
								<a title="青客上海租房维修服务" href="https://www.qk365.com/qkkx/service/2018/23.html?wxfw" target="_blank" rel="nofollow">维修服务</a>
								<a title="青客上海租房宽带服务" href="https://www.qk365.com/qkkx/service/2018/24.html?kdfw" target="_blank" rel="nofollow">宽带服务</a>
                            </li>
                            <li>
                                <p>会员专区</p>
                                <a title="青客上海租房会员介绍" href="https://www.qk365.com/qkkx/service/2018/34.html?hyjs" target="_blank" rel="nofollow">会员介绍</a>
								<a title="青客上海租房会员积分" href="https://www.qk365.com/qkkx/service/2018/40.html?hyjf" target="_blank" rel="nofollow">会员积分</a>
								<a title="青客上海租房门店支付" href="https://www.qk365.com/qkkx/service/2018/33.html?mdzf" target="_blank" rel="nofollow">门店支付</a>
								<a title="青客上海租房ATM支付" href="https://www.qk365.com/qkkx/service/2018/36.html?atmzf" target="_blank" rel="nofollow">ATM支付</a>
								<a title="青客上海租房APP支付" href="https://www.qk365.com/qkkx/service/2018/37.html?appzf" target="_blank" rel="nofollow">APP支付</a>
                            </li>
                        </ul>
                    </div>
                    <div class="QcoL5 fL">
                        <ul class="serviceR clearfix">
                           <li>
                               <img class="sicon" src="https://www.qk365.com/images/2019-11-29-img/applet-qkgy.png"></img>
                               <img class="sicon1" src="https://www.qk365.com/images/2019-11-29-img/applet-qkgyClick.png"></img>
                               <div class="scode"><img src="https://www.qk365.com/images/index/code-qkgy.jpg" alt="青客公寓APP"></div>
                               <p>青客公寓APP</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://www.qk365.com/images/2019-11-29-img/applet-qkfw.png"></img>
                               <img class="sicon1" src="https://www.qk365.com/images/2019-11-29-img/applet-qkfwClick.png"></img>
                               <div class="scode"><img src="https://www.qk365.com/images/index/code-qkfw.jpg?v=20191225" alt="青客服务号"></div>
                               <p>青客服务号</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://www.qk365.com/images/2019-11-29-img/applet-qkzf.png"></img>
                               <img class="sicon1" src="https://www.qk365.com/images/2019-11-29-img/applet-qkzfClick.png"></img>
                               <div class="scode"><img src="https://www.qk365.com/images/index/code-qkzf.jpg?v=20191225" alt="青客找房小程序"></div>
                               <p>青客找房小程序</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://www.qk365.com/images/2019-11-29-img/applet-zfb.png"></img>
                               <img class="sicon1" src="https://www.qk365.com/images/2019-11-29-img/applet-zfbClick.png"></img>
                               <div class="scode"><img src="https://www.qk365.com/images/index/code-zfb.jpg?v=20191225" alt="支付宝小程序"></div>
                               <p>支付宝小程序</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://www.qk365.com/images/2019-11-29-img/applet-bd.png"></img>
                               <img class="sicon1" src="https://www.qk365.com/images/2019-11-29-img/applet-bdClick.png"></img>
                               <div class="scode"><img src="https://www.qk365.com/images/index/code-bd.jpg" alt="百度小程序"></div>
                               <p>百度小程序</p>
                           </li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <p class="description">青客<a href="https://www.qk365.com/" title="上海租房网">上海租房网</a>提供优质<a href="https://www.qk365.com/list" title="房屋出租">房屋出租</a>信息，海量直租房、经纪人租房信息，帮您轻松在上海<a href="https://www.qk365.com/" title="租房">租房</a>。包括<a href="https://www.qk365.com/" title="白领公寓">白领公寓</a>、<a href="https://www.qk365.com/" title="合租公寓">合租公寓</a>、<a href="https://www.qk365.com/" title="单身公寓">单身公寓</a>、
						<a href="https://www.qk365.com/" title="时尚租房">时尚租房</a>、<a href="https://www.qk365.com/" title="上海合租">上海合租</a>等信息，您还可以选择青客
						<a href="https://i.qk365.com/sh" title="上海租房移动端">上海租房移动端</a>，更方便、更快捷。</p>
            	<div class="alphabet">
            	<div>
					<p class="alphabet-tit">商圈索引：</p>
                    <ul class="alphabet-tabs">
                    	<li class="selected">A</li>
                    	<li >B</li>
                    	<li >C</li>
                    	<li >D</li>
                    	<li >F</li>
                    	<li >G</li>
                    	<li >H</li>
                    	<li >J</li>
                    	<li >K</li>
                    	<li >L</li>
                    	<li >M</li>
                    	<li >N</li>
                    	<li >P</li>
                    	<li >Q</li>
                    	<li >S</li>
                    	<li >T</li>
                    	<li >W</li>
                    	<li >X</li>
                    	<li >Y</li>
                    	<li >Z</li>
                    	</ul>
				</div>
                <ul class="alphabet-item">
                	<li style="display: list-item;">
                			<a href="https://www.qk365.com/list/a13-k140" title="安亭租房">安亭租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a11-k96" title="北桥租房">北桥租房</a>
                			<a href="https://www.qk365.com/list/a12-k124" title="宝山城区租房">宝山城区租房</a>
                			<a href="https://www.qk365.com/list/a13-k141" title="博乐广场租房">博乐广场租房</a>
                			<a href="https://www.qk365.com/list/a14-k153" title="八佰伴租房">八佰伴租房</a>
                			<a href="https://www.qk365.com/list/a14-k154" title="北蔡租房">北蔡租房</a>
                			<a href="https://www.qk365.com/list/a18-k229" title="百联南桥购物中心租房">百联南桥购物中心租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a3-k1" title="城隍庙租房">城隍庙租房</a>
                			<a href="https://www.qk365.com/list/a11-k97" title="春申租房">春申租房</a>
                			<a href="https://www.qk365.com/list/a11-k98" title="春申地区租房">春申地区租房</a>
                			<a href="https://www.qk365.com/list/a14-k156" title="曹路租房">曹路租房</a>
                			<a href="https://www.qk365.com/list/a14-k157" title="川沙租房">川沙租房</a>
                			<a href="https://www.qk365.com/list/a17-k227" title="重固镇租房">重固镇租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a12-k586" title="大场镇租房">大场镇租房</a>
                			<a href="https://www.qk365.com/list/a15-k195" title="石化租房">石化租房</a>
                			<a href="https://www.qk365.com/list/a16-k368" title="洞泾租房">洞泾租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a16-k201" title="飞航广场租房">飞航广场租房</a>
                			<a href="https://www.qk365.com/list/a18-k230" title="奉城租房">奉城租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a5-k38" title="古北租房">古北租房</a>
                			<a href="https://www.qk365.com/list/a11-k99" title="古美罗阳租房">古美罗阳租房</a>
                			<a href="https://www.qk365.com/list/a12-k125" title="高境租房">高境租房</a>
                			<a href="https://www.qk365.com/list/a12-k126" title="共富租房">共富租房</a>
                			<a href="https://www.qk365.com/list/a12-k127" title="顾村租房">顾村租房</a>
                			<a href="https://www.qk365.com/list/a14-k589" title="高行租房">高行租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a4-k23" title="华东理工租房">华东理工租房</a>
                			<a href="https://www.qk365.com/list/a4-k24" title="华泾租房">华泾租房</a>
                			<a href="https://www.qk365.com/list/a10-k87" title="黄兴公园租房">黄兴公园租房</a>
                			<a href="https://www.qk365.com/list/a11-k104" title="华漕/虹桥镇租房">华漕/虹桥镇租房</a>
                			<a href="https://www.qk365.com/list/a13-k143" title="黄渡镇租房">黄渡镇租房</a>
                			<a href="https://www.qk365.com/list/a14-k159" title="航头租房">航头租房</a>
                			<a href="https://www.qk365.com/list/a14-k160" title="花木租房">花木租房</a>
                			<a href="https://www.qk365.com/list/a14-k161" title="惠南镇租房">惠南镇租房</a>
                			<a href="https://www.qk365.com/list/a17-k223" title="华新镇租房">华新镇租房</a>
                			<a href="https://www.qk365.com/list/a18-k231" title="海湾旅游区租房">海湾旅游区租房</a>
                			<a href="https://www.qk365.com/list/a18-k232" title="环城东路租房">环城东路租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a6-k2316" title="静安周边租房">静安周边租房</a>
                			<a href="https://www.qk365.com/list/a11-k103" title="虹桥镇租房">虹桥镇租房</a>
                			<a href="https://www.qk365.com/list/a11-k105" title="江川路租房">江川路租房</a>
                			<a href="https://www.qk365.com/list/a11-k106" title="交大闵行校区租房">交大闵行校区租房</a>
                			<a href="https://www.qk365.com/list/a11-k107" title="金虹桥租房">金虹桥租房</a>
                			<a href="https://www.qk365.com/list/a11-k108" title="金平路步行街租房">金平路步行街租房</a>
                			<a href="https://www.qk365.com/list/a13-k144" title="嘉定城区租房">嘉定城区租房</a>
                			<a href="https://www.qk365.com/list/a13-k145" title="戬浜镇租房">戬浜镇租房</a>
                			<a href="https://www.qk365.com/list/a13-k146" title="江桥租房">江桥租房</a>
                			<a href="https://www.qk365.com/list/a13-k147" title="菊园新区租房">菊园新区租房</a>
                			<a href="https://www.qk365.com/list/a13-k312" title="嘉定镇租房">嘉定镇租房</a>
                			<a href="https://www.qk365.com/list/a14-k163" title="金杨地区租房">金杨地区租房</a>
                			<a href="https://www.qk365.com/list/a14-k5612" title="江镇租房">江镇租房</a>
                			<a href="https://www.qk365.com/list/a15-k190" title="金山卫租房">金山卫租房</a>
                			<a href="https://www.qk365.com/list/a15-k191" title="金山新城租房">金山新城租房</a>
                			<a href="https://www.qk365.com/list/a15-k192" title="金山中部租房">金山中部租房</a>
                			<a href="https://www.qk365.com/list/a15-k5624" title="金山工业区租房">金山工业区租房</a>
                			<a href="https://www.qk365.com/list/a16-k203" title="九亭租房">九亭租房</a>
                			<a href="https://www.qk365.com/list/a18-k234" title="金汇租房">金汇租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a14-k164" title="康桥/周浦租房">康桥/周浦租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a4-k28" title="龙华租房">龙华租房</a>
                			<a href="https://www.qk365.com/list/a9-k81" title="凉城/江湾镇租房">凉城/江湾镇租房</a>
                			<a href="https://www.qk365.com/list/a11-k110" title="老闵行租房">老闵行租房</a>
                			<a href="https://www.qk365.com/list/a11-k111" title="龙柏地区租房">龙柏地区租房</a>
                			<a href="https://www.qk365.com/list/a12-k128" title="罗店租房">罗店租房</a>
                			<a href="https://www.qk365.com/list/a13-k148" title="罗宾森广场租房">罗宾森广场租房</a>
                			<a href="https://www.qk365.com/list/a14-k168" title="陆家嘴租房">陆家嘴租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a11-k113" title="马桥租房">马桥租房</a>
                			<a href="https://www.qk365.com/list/a11-k114" title="梅陇租房">梅陇租房</a>
                			<a href="https://www.qk365.com/list/a13-k149" title="马陆租房">马陆租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a11-k115" title="南方商城租房">南方商城租房</a>
                			<a href="https://www.qk365.com/list/a13-k150" title="南翔租房">南翔租房</a>
                			<a href="https://www.qk365.com/list/a18-k235" title="南桥租房">南桥租房</a>
                			<a href="https://www.qk365.com/list/a18-k236" title="南桥新城区租房">南桥新城区租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a8-k72" title="彭浦镇租房">彭浦镇租房</a>
                			<a href="https://www.qk365.com/list/a11-k116" title="浦江镇租房">浦江镇租房</a>
                			<a href="https://www.qk365.com/list/a14-k5625" title="浦东周边租房">浦东周边租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a11-k117" title="七宝租房">七宝租房</a>
                			<a href="https://www.qk365.com/list/a17-k224" title="青浦城区租房">青浦城区租房</a>
                			<a href="https://www.qk365.com/list/a17-k225" title="青浦镇租房">青浦镇租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a11-k120" title="莘庄租房">莘庄租房</a>
                			<a href="https://www.qk365.com/list/a11-k121" title="莘庄龙之梦租房">莘庄龙之梦租房</a>
                			<a href="https://www.qk365.com/list/a12-k131" title="上海大学租房">上海大学租房</a>
                			<a href="https://www.qk365.com/list/a12-k2307" title="淞宝租房">淞宝租房</a>
                			<a href="https://www.qk365.com/list/a14-k173" title="三林地区租房">三林地区租房</a>
                			<a href="https://www.qk365.com/list/a16-k208" title="佘山租房">佘山租房</a>
                			<a href="https://www.qk365.com/list/a16-k209" title="泗泾租房">泗泾租房</a>
                			<a href="https://www.qk365.com/list/a16-k211" title="松江城区租房">松江城区租房</a>
                			<a href="https://www.qk365.com/list/a16-k212" title="松江大学城租房">松江大学城租房</a>
                			<a href="https://www.qk365.com/list/a16-k213" title="松江老城租房">松江老城租房</a>
                			<a href="https://www.qk365.com/list/a16-k214" title="松江新城租房">松江新城租房</a>
                			<a href="https://www.qk365.com/list/a16-k218" title="莘闵租房">莘闵租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a5-k42" title="天山租房">天山租房</a>
                			<a href="https://www.qk365.com/list/a7-k59" title="桃浦租房">桃浦租房</a>
                			<a href="https://www.qk365.com/list/a12-k135" title="通河/泗塘租房">通河/泗塘租房</a>
                			<a href="https://www.qk365.com/list/a14-k177" title="唐镇租房">唐镇租房</a>
                			<a href="https://www.qk365.com/list/a15-k196" title="亭林租房">亭林租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a4-k30" title="万体馆租房">万体馆租房</a>
                			<a href="https://www.qk365.com/list/a7-k61" title="武宁地区租房">武宁地区租房</a>
                			<a href="https://www.qk365.com/list/a10-k90" title="五角场/大学区租房">五角场/大学区租房</a>
                			<a href="https://www.qk365.com/list/a11-k119" title="吴泾镇租房">吴泾镇租房</a>
                			<a href="https://www.qk365.com/list/a12-k136" title="吴淞租房">吴淞租房</a>
                			<a href="https://www.qk365.com/list/a13-k370" title="外冈镇租房">外冈镇租房</a>
                			<a href="https://www.qk365.com/list/a14-k179" title="外高桥租房">外高桥租房</a>
                			<a href="https://www.qk365.com/list/a14-k367" title="王港租房">王港租房</a>
                			<a href="https://www.qk365.com/list/a17-k390" title="吾悦广场租房">吾悦广场租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a13-k584" title="徐行租房">徐行租房</a>
                			<a href="https://www.qk365.com/list/a14-k181" title="新场租房">新场租房</a>
                			<a href="https://www.qk365.com/list/a16-k217" title="小昆山租房">小昆山租房</a>
                			<a href="https://www.qk365.com/list/a16-k219" title="新桥租房">新桥租房</a>
                			<a href="https://www.qk365.com/list/a17-k2312" title="香花桥租房">香花桥租房</a>
                			<a href="https://www.qk365.com/list/a18-k237" title="西渡租房">西渡租房</a>
                			<a href="https://www.qk365.com/list/a18-k238" title="新都汇租房">新都汇租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a12-k137" title="杨行租房">杨行租房</a>
                			<a href="https://www.qk365.com/list/a12-k138" title="月浦租房">月浦租房</a>
                			<a href="https://www.qk365.com/list/a14-k184" title="源深体育中心租房">源深体育中心租房</a>
                			<a href="https://www.qk365.com/list/a14-k588" title="御桥租房">御桥租房</a>
                			</li>
                	<li >
                			<a href="https://www.qk365.com/list/a7-k63" title="真光租房">真光租房</a>
                			<a href="https://www.qk365.com/list/a10-k94" title="中原地区租房">中原地区租房</a>
                			<a href="https://www.qk365.com/list/a11-k123" title="颛桥租房">颛桥租房</a>
                			<a href="https://www.qk365.com/list/a13-k585" title="朱桥租房">朱桥租房</a>
                			<a href="https://www.qk365.com/list/a14-k185" title="张江租房">张江租房</a>
                			<a href="https://www.qk365.com/list/a14-k2314" title="周浦万达租房">周浦万达租房</a>
                			<a href="https://www.qk365.com/list/a14-k5609" title="周浦租房">周浦租房</a>
                			<a href="https://www.qk365.com/list/a15-k199" title="朱泾租房">朱泾租房</a>
                			<a href="https://www.qk365.com/list/a15-k200" title="朱行镇租房">朱行镇租房</a>
                			<a href="https://www.qk365.com/list/a16-k221" title="中山中路租房">中山中路租房</a>
                			<a href="https://www.qk365.com/list/a17-k226" title="赵巷镇租房">赵巷镇租房</a>
                			<a href="https://www.qk365.com/list/a17-k228" title="朱家角租房">朱家角租房</a>
                			<a href="https://www.qk365.com/list/a18-k240" title="柘林租房">柘林租房</a>
                			<a href="https://www.qk365.com/list/a18-k242" title="庄行租房">庄行租房</a>
                			</li>
                	</ul>
            </div>
        </div>
    </div>
    
    <p class="Copyright">Copyright (C) 沪ICP备14038413</p><br />
	<p class="Copyright">
		<script src="//kxlogo.knet.cn/seallogo.dll?sn=e15112731011461605igz0000000&size=0"></script> 
		<a target="cyxyv" href="https://v.yunaq.com/certificate?domain=www.qk365.com&from=label&code=90030"><img src="https://aqyzmedia.yunaq.com/labels/label_sm_90030.png"></a>
		<a id="_pingansec_bottomimagelarge_brand" target="_blank" target="_blank" target="_blank" target="_blank" href="//si.trustutn.org/info?sn=320200820040043160860&certType=1"><img src="//v.trustutn.org/images/cert/brand_bottom_large.jpg"/></a>
	</p>
	<div style="width:300px;margin:0 auto; padding:10px 0; text-align: center;">
		<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011402005354" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;" rel="nofollow">
		<img src="https://www.qk365.com/images/beian.png" style="float:left;"/><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">沪公网安备 31011402005354号</p>
		</a>
	</div>
</div>

<!-- cnzz Begin -->
<div style="display: none"><script type="text/javascript" src="https://s22.cnzz.com/z_stat.php?id=1000353613&web_id=1000353613"></script></div>
<!-- cnzz End -->
<input type="hidden" id="isValidate" value="0" />
<input type="hidden" id="uuid" />
<style>
	.slide-wrap {
		display: none;
		height: 46px;
    	margin-bottom: 20px;
	}
	
	.slide-active {
		display: block;
	}
	
	#getCoupon_message2 {
		text-align:  center;
	}
	
	#getCoupon_message3 {
		font-size: 16px;
	}
</style>
<div class="rob-box rob-box-tog" style="display: none">
	<div class="rob-cont rob-cont-tog">
		<div class="rob-close">
			<img alt="上海租房" src="https://www.qk365.com/img/close.jpg">
		</div>
		<div class="rob-tit">
			<h3 id="coupon_top"></h3>
			<p id="coupon_desc"></p>
		</div>
		<div class="importBox">
			<div class="import">
				<form class="phone" action="" method="">
					<input type="text" id="mobile" autocomplete="off" placeholder="请输入手机号"
						onfocus="if(placeholder=='请输入手机号')placeholder=''"
						onblur="if(!placeholder)placeholder='请输入手机号'" 
						onkeyup="value=value.replace(/\D/g,'')" maxlength="11">
					<div class="authCode" id="smsCodeBtn">发送验证码</div>
				</form>
				<form class="message" action="" method="">
					<input id="smsCode" type="text" autocomplete="off" placeholder="请输入手机验证码"
						onfocus="if(placeholder=='请输入手机验证码')placeholder=''"
						onblur="if(!placeholder)placeholder='请输入手机验证码'" 
						onkeyup="value=value.replace(/\D/g,'')" maxlength="10">
				</form>
			</div>
			<br />
			<div class="regSlider slide-wrap">
				<div id="regSlider" class="slider"></div>
			</div>
			<div class="chooseBox">
				<p id="coupon_message" style="display: none"></p>
				<form class="rob-key">
					<div class="choose" id="coupon_reg" >
						<input type="checkbox" style="-webkit-appearance: radio;"
							id="reg_protocol_chk"> <label>用户注册协议</label>
					</div>
					<input id="register" class="chooseGo" type="button" value="立即抢券">
				</form>
			</div>
		</div>
		<ul class="activity activity_type1" style="display: none">
			<li>活动规则：</li>
			<li>1、本活动仅限未注册用户参加；</li>
			<li>2、活动时间段内注册的新用户，即有机会获得500元租房券，用户可登录账号至“个人中心”-“我的优惠券”查看领取结果及优惠券使用规则；</li>
			<li>3、详情请电话联系：400-8198-365，青客保留法律允许范围内对本活动的最终解释权。</li>
		</ul>
		
		<ul class="activity activity_type2" style="display: none">
			<li>活动规则：</li>
			<li>1、本活动仅限未注册用户参加；</li>
			<li>2、活动时间段内注册的新用户，即有机会获得首月免30天租房券，用户可登录账号至“个人中心”-“我的优惠券”查看领取结果及优惠券使用规则；</li>
			<li>3、详情请电话联系：400-8198-365，青客保留法律允许范围内对本活动的最终解释权。</li>
		</ul>
		
		<ul class="activity activity_type3" style="display: none">
			<li>活动规则：</li>
			<li>1、本活动仅限未注册用户参加；</li>
			<li>2、每位新注册用户每人随机获得一张优惠券，用户可登录账号至“个人中心”-“我的优惠券”查看领取结果及优惠券使用规则；</li>
			<li>3、详情请电话联系：400-8198-365，青客保留法律允许范围内对本活动的最终解释权。</li>
		</ul>
	</div>
</div>
<!-- 抢300元租房券 end -->

<!-- 领取成功 start -->
<div class="rob-box rob-box-hide rob-box2" style="display: none">
	<div class="rob-cont rob-cont2">
		<div class="rob-close">
			<img alt="上海租房" src="https://www.qk365.com/img/close.jpg">
		</div>
		<div class="importBox">
			<div class="get-succeed">
				<h4 id="getCoupon_message1"></h4>
				<p id="getCoupon_message2"></p>
				<p id="getCoupon_message3"></p>
			</div>
		</div>
	</div>
</div>
<!-- 领取成功 end -->

<!-- 网站注册服务条款 -->
<div class="clause-wrap" style="display: none">
	<div class="clause-cont">
		<div class="clause">
			<h4>网站注册服务条款</h4>
			<p>尊敬的用户，欢迎您注册成为青客时尚租房网站的用户。此服务条款详细表述您在“青客时尚租房”网站享受我们的服务时所须遵守的条款，如您有任何疑问，请及时与我们联系。
				在您注册成为“青客时尚租房”电子商务用户（以下简称：本网站用户）前，请务必仔细阅读本用户协议、隐私保护、以及其他本网站公布之相关有效规则、文件，一旦您注册成为了本网站用户即表示您已经阅读、同意并接受本网站相关法律文件中所含的所有条款。如果我们对本声明进行了任何变更，我们会在“青客时尚租房”官方网站页面上发布相关变更事项的通知，所有协议内容在发布之日后自动生效。如您有任何疑问，请先致电我们的客服。</p>
			<dl>
				<dt>一、服务条款的确认和接纳 青客时尚租房网站各项服务的所有权和运作权归本网站拥有。 邮件/短信服务：
					青客时尚租房网站会通过邮件、短信的形式，对本网站注册、预约用户发送订单信息、促销活动等告知服务。如果你不想接受来自青客时尚租房网站的邮件、短信，您可以向青客时尚租房网站提出退阅申请，并注明您的E-mail地址、手机号或相关地址信息，青客时尚租房网站会在收到申请后为您办理退阅。</dt>
				<dt>二、用户注册</dt>
				<dd>1、在线用户注册成功后，您将拥有一个青客（商城、社区）专用免费帐号及相应的密码，该帐号和密码将成为用户登录“青客（商城、社区）”、享受“青客（商城、社区）”服务、发表评论、预约房源等服务的凭证。</dd>
				<dd>2、每位用户只允许在“青客（商城、社区）”拥有一个有效账户，如有证据证明用户存在恶意注册多个账户的情形，青客有权采取取消、冻结或关闭账号等措施。该账户被取消、冻结或关闭之前所作出的行为引起的所有法律后果均由该用户承担，如该行为造成青客官网损失的，用户需承担相应的损害赔偿责任。</dd>
				<dd>3、享受“青客（商城、社区）”服务过程中，用户有义务保管好其个人账号及密码，并对他人使用私人计算机作出限制。用户不得以任何形式擅自转让或授权他人使用自己的“青客（商城、社区）”帐号及密码。如果因为用户管理不善造成帐号、密码等被复制或被盗用，相应损失由用户自行承担。同时，通过该用户的个人账户在“青客（商城、社区）”上发生的所有活动以及产生的责任，亦应由该用户承担。</dd>
				<dd>4、注册用户不得采用测试、欺骗等任何非法手段，盗取其他用户的账户信息或对他人进行骚扰。</dd>
				<dd>5、青客承诺仅根据本网站服务目的使用用户个人信息。服务目的包括但不限于预约确认、时间安排、客户回访、政策更新、用户通知、发送促销信息、商业信息以及其他与预约和服务相关的辅助服务等。如用户认为“青客（商城、社区）”超范围使用了其个人信息，请立即与客服中心联系，上海青客设备租赁有限公司将核实处理。</dd>
				<dt>三、用户隐私保护</dt>
				<p>维护与尊重用户个人隐私是“青客时尚租房网站”的一项基本政策，因此，“青客时尚租房网站”非依法律规定或其他有效法律约定不会向任何第三方披露、转让、出租或者出售预约用户名单、预约记录等涉及消费者个人信息的数据以及用户保存在“青客时尚租房网站”各项服务中的非公开内容。
					对用户注册资料的保护用户可授权“青客时尚租房网站”向第三方透露其注册资料，否则“青客时尚租房网站”不会公开用户的姓名、住址、通信地址、电子邮箱、电话及帐号。以下情况除外：</p>
				<dd>1）事先获得用户明确授权后，用户许可或授权“青客时尚租房网站”通过电子邮件服务或其他方式透露这些信息；</dd>
				<dd>2）相应的法律、法规要求以及按照有关政府主管部门的要求，需要“青客时尚租房网站”提供用户的个人资料；</dd>
				<dd>3）为了维护交易双方、用户和（或）“青客时尚租房网站”、 上海青客设备租赁有限公司合法利益；</dd>
				<dd>4）“青客时尚租房网站”可能会与第三方合作向用户提供相关的网络服务，在此情况下，如该第三方同意承担与“青客时尚租房网站”同等的保护用户隐私的责任，则“青客时尚租房网站”有权将用户的注册资料等提供给该第三方；</dd>
				<dd>5）在不透露单个用户隐私资料的前提下，“青客时尚租房网站”有权对整个用户数据库进行分析并对用户数据库进行商业上的利用；</dd>
				<dd>6）根据本网站已经公布之有效法律文件，本网站有权许可第三方使用该用户个人信息的其他情形。</dd>
				<dt>四、预约及留言管理</dt>
				<p>注册用户在本网站进行商品预约和留言时必须遵守以下条款 ：</p>
				<dd>1.
					您在本网站的一切操作应遵守所有适用的中国法律法规、规章制度和地方性法规要求。同时您必须确保遵守本用户协议和隐私保护以及纳入上述文件的所有其它条款、规则等一切相关内容。</dd>
				<dd>2.
					如您在本网站预约商品，您有义务完成与本网站的预约流程（法律或本用户协议禁止的预约除外）。预约操作执行并下预约单后，即表示您同意该商品描述所含的一切出售条件，（商品出售条件不违反本协议并合法）。</dd>
				<dd>3.
					“青客时尚租房网站”保留对商品预约数量的限制权。在下预约单的同时，您也同时承认了您拥有购买这些产品的权利能力和行为能力，并且将您对您在订单中提供的所有信息的真实性负责。</dd>
				<dd>4.
					“青客时尚租房网站”网站上的广告，价目表和声明并不构成要约。在本网站对您的预约单进行确认之前，您和本网站之间不存在合同关系。本网站有权在发现显现的商品及订单的明显错误或缺货的情况下，单方面撤回该信息或终止交易。</dd>
				<dd>5.
					商品价格和可获性都在网站上指明。这类信息将随时更改且不另行通知。在确认了您的订单后发生的意外情况，比如由于商家提价、市场调节、税额变化引起的价格变化、或是由于网站的错误等造成价格变化，本网站会通过E-mail或电话形式通知您，让您决定是否取消订单。</dd>
				<dd>6. 拒绝提供担保:用户明确同意信息服务的使用由用户个人承担风险。
					“青客时尚租房网站”不担保服务不会受中断，对服务的及时性，安全性，出错发生都不作担保，但会在能力范围内，避免出错。</dd>
				<dd>7.
					用户不能在本网站上使用谩骂，侮辱，诽谤等不雅言语以及其它攻击其他用户和网站的言语。“青客时尚租房网站”有权自行决定删除此类言论及其它“青客时尚租房网站”认为不合适的言论，而不负有通知义务并承担责任。</dd>
				<dd>8. 您在本网站下订单并完成订单交易后，如出现任何问题需与客服人员取得联系，并按照本网站“消费保障”政策进行处理。</dd>
				<dt>五、网站安全</dt>
				<p>您同意，未经本网站明示书面准许，您不会为了任何目的使用任何机器人、蜘蛛软件、刷屏软件或其他自动方式进入网站。此外，您同意绝不进行以下操作：</p>
				<dd>1. 进行任何对本网站造成或可能造成（按本网站自行酌情确定）不合理或不合比例的重大负荷的行为；</dd>
				<dd>2.
					未经本网站事先明示书面准许，对本网站的任何内容（除您的个人信息以外）制作拷贝、进行复制、修改、制作衍生作品、分发或公开展示等的侵权行为；</dd>
				<dd>3. 干扰或试图干扰本网站的正常工作或活动；</dd>
				<dd>4. 在本网站中使用可能视为被禁止或可能被禁止的任何内容；</dd>
				<dd>5.
					对本网站使用不良数据。包含可能破坏、改变、删除、不利影响、秘密截取、未经授权而接触，或占用任何系统、数据、个人资料的病毒、间谍软件、其他电脑程序等；</dd>
				<dd>6、侵犯他人合法权益的行为；</dd>
				<dd>7、违反法律法规或本网站有效法律文件约定之行为。</dd>
				<dt>六、知识产权声明</dt>
				<p>本网站所提供的网络服务的相关著作权、专利权、商标、商业隐私及其它权利，均属“青客时尚租房网站”所有。非经本网站同意，任何个人或单位均不得擅自下载、复制、传输、修改、编辑制作等操作，否则将承担所有法律责任。“青客时尚租房网站”拥有本网站服务器中的任何数据信息的绝对所有权。</p>
				<dt>七、免责声明</dt>
				<p>本网站用户同意接收来自“青客时尚租房网站”或者“青客时尚租房网站”合作伙伴发出的信息，包括但不限于电子邮件，手机短消息。
					“青客时尚租房网站”有义务在技术上确保网站的正常运行，尽力避免服务中断或将中断时间限制在最短时间内，保证用户网上预约活动顺利进行。但如因不可抗力或其他本网站无法控制的因素使网站崩溃或无法正常使用导致网上预约无法完成或丢失有关的信息、记录等，本网站不承担责任；任何用户向本网站提供错误、不完整、不实信息等造成不能正常使用本网站服务或遭受任何其他损失，概与本网站无关。
					本网站《免责声明》中所列之其他情形。</p>
				<dt>八、服务终止</dt>
				<dd>1.
					注册会员或“青客时尚租房网站”可随时根据实际情况中断一项或多项服务。“青客时尚租房网站”不需对任何个人或第三方负责而随时中断服务。会员若反对任何服务条款的建议或对后来的条款修改有异议，或对“青客时尚租房网站”服务不满，会员可以行使如下权利：</dd>
				<dd>1)会员用户不再享受“青客时尚租房网站”相关信息服务 。</dd>
				<dd>2)通知“青客时尚租房网站”停止对该会员的服务。</dd>
				<dd>3)结束用户会员服务后，注册会员使用“青客时尚租房网站”服务的权利马上中止。会员服务终止后，会员没有权利，“青客时尚租房网站”也没有义务传送任何未处理的信息或未完成的服务给会员或第三方。</dd>
				<dd>2. 如有以下行为的注册会员将会被取消会员资格：</dd>
				<dd>1)违反“青客时尚租房网站”注册条款。</dd>
				<dd>2)提供虚假注册会员个人资料。</dd>
				<dd>3)注册会员有损公司利益的行为。</dd>
				<dd>4)有违反中国的法律、法规、违反互联网相关规定的行为。</dd>
				<dd>5)用户将会员帐号用于出售、拍卖等，利用会员帐号当作商品进行交易的行为。</dd>
				<dd>6)用户出借、转让会员帐号给其他会员等不恰当行使会员权利的行为。</dd>
				<dd>7)利用盗取密码、诈骗等不正当手段获得会员帐号的行为。</dd>
				<dd>8)恶意在商品留言，博客、微博等个人空间中多次或大量使用谩骂，侮辱，诽谤等不雅言语的行为。</dd>
				<dt>九、其它</dt>
				<dd>1、本服务条款以及与使用“青客时尚租房网站”服务相关的声明、说明、规则、政策、程序，构成“青客时尚租房网站”与用户之间有效的完整协议，将对用户持续有效，有效期至用户注销或者被取消账户、且停止一切使用“青客时尚租房网站”服务的行为后，但“青客时尚租房网站”与用户间已经产生的权利义务，仍对双方有约束力。</dd>
				<dd>2、上海青客设备租赁有限公司将视向用户所提供服务内容之特性，要求用户在注册青客时尚租房网站提供的有关服务时，遵守特定的条件和条款；如该特定条件和条款与以上服务条款有任何不一致之处，则以特定条件和条款为准。</dd>
				<dd>3、本服务条款中的任何条款无论因何种原因完全或部分无效或不具有执行力，其余条款仍应有效并且有约束力。</dd>
				<dd>4、本服务条款的标题、序号均为方便阅读而设定，不影响条款实际含义及其效力。</dd>
				<dd>5、本服务条款自公布及适用的当天生效，有效期持续至新版本发布之时。</dd>
				<dd>6、以上条款的解释权归上海青客设备租赁有限公司最终所有。</dd>

			</dl>
		</div>
		<div class="clause-close">
			<img alt="上海租房" src="https://www.qk365.com/img/close.jpg">
		</div>
	</div>
</div><link href="https://www.qk365.com/css/alert.css?v=20200824" rel="stylesheet" type="text/css" />
<ins id="newBridge">
    <ins class="nb-invite-wrap nb-invite-wrap-base nb-position-base nb-middle customer-invite-style ">
        <ins class="nb-invite-body nb-invite-skin-9">
            <ins class="nb-invite-tool nb-invite-tool-base" id="nb_invite_tool" style=""></ins>
            <ins class="nb-invite-text nb-invite-text-base">
                <ins class="nb-invite-welcome nb-invite-welcome-base nb-show" id="nb_invite_welcome"></ins>
            </ins>
            <ins class="nb-invite-btn-base nb-invte-btns-9">
                <ins class="nb-invite-cancel nb-invite-cancel-base" id="nb_invite_cancel">稍后再说</ins>
                <ins class="nb-invite-ok nb-invite-ok-base" id="nb_invite_ok" onclick="onKST();">现在咨询</ins>
            </ins>
        </ins>
    </ins>
</ins>
<script type="text/javascript" src="https://ryak66.kuaishang.cn/bs/ks.j?cI=929688&fI=69076" charset="utf-8"></script>
<script type="text/javascript" src="https://www.qk365.com/js/onKST.js"></script>

<script type="text/javascript" src="https://www.qk365.com/js/pageViewCount.js?version=20180820"></script>
<script type="text/javascript" src="https://www.qk365.com/js/alert.js?v=20191115"></script><script type="text/javascript">
	var fwtybh = '';
	var fyurl = '';
	if(fwtybh != null && fwtybh!= '' && fyurl != null && fyurl !=''){
        makeQrcode(fyurl);
	}
</script>
</body>
</html>


Process finished with exit code 0

'''
html_doc = etree.HTML(html)
left_node_list = html_doc.xpath("//div[@class='survey-left fL']/dd")
right_nod_list = html_doc.xpath("//div[@class='survey-right fR']/dd")
for left_node in left_node_list:
    # print(''.join(left_node.xpath("./span/text()|./text()|./em/text()|./a/text()")).strip())
    print(''.join(left_node.xpath("./text()|./em/text()|./a/text()")).strip())
for right_list in right_nod_list:
    print(''.join(right_list.xpath("./text()|./em/text()|./a/text()")).strip())
# re_pat = '<img src="(.*)">'
#
# print(re.findall(re_pat,html))
