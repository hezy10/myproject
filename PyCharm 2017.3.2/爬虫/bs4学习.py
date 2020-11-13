# coding=utf-8
from bs4 import BeautifulSoup
import re
from lxml import etree
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '85.0.4183.83 Safari/537.36'
}
url = 'https://www.qk365.com/list'

# response = requests.get(url=url,headers=headers)
# print(response.text)

html_str = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/bs4学习.py"
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>上海租房网_上海合租|房屋出租信息网_青客时尚租房网</title>
<meta http-equiv="Cache-Control" content="no-transform " />
<meta name="applicable-device" content="pc">
<meta name="keywords"
	 content="上海租房网、上海合租、上海房屋出租、上海租房信息网"   />
<meta name="description"
	 content="青客租房网提供上海同城全新全面的房屋出租信息，所有租房统一装修、设施齐全、租房临近地铁、无中介、定期保洁，是居家生活办公首选。上海租房、找合租、个人房屋出租，就上青客租房网。"   />
<link rel="alternate" media="only screen and (max-width: 640px)"
	
			href="https://i.qk365.com/sh/list/"
		
		/>
<link href="https://www.qk365.com/css/find.css?v=20191206" rel="stylesheet" type="text/css">
<script type="text/javascript" src="https://www.qk365.com/js/homepage/defaultPic.js"></script>
<style type="text/css">
	.jg_pic {
		width: 1170px;
		height: 160px;
		margin: 20px auto;
	}
	.jg_pic img {
		width: 1170px;
		height: 160px;
	}
</style>
</head>
<body onclick="reMoveLayerWait(this);">
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
<div class="easyTopSel">
		<div class="clearfix">
			<div class="easyCurve">
		<span>您当前的位置：</span>
		<div id="topnanv">
			<div id="anvlfteb">
				
				<div class="posbox">
						<a title="上海租房" href="https://www.qk365.com">上海租房</a> </div>
				<em>></em>
					<div class="posbox">
						<a title="轻松找房" href="https://www.qk365.com/list">轻松找房</a>
								</div>
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
				</div>
		</div>
		<div class="clear"></div>
	</div>
<div class="easySoBox clearfix">
				<!-- 房间价格 -->
				<div class="easySo">
					<span class="easySoTit fL">房间价格：</span> 
					<span class="easySoCon priceCon fL"> 
						<a href="javascript:price('');" rel="nofollow">
							<em	
								  class="cur" >不限</em>
						</a>
						<a title="500元以下租房" href="https://www.qk365.com/list/r0-t500"
								style="color: #666;" onclick="price('500元以下','76');" rel="nofollow">
								<em	>500元以下</em>
							</a>
						<a title="500-700元租房" href="https://www.qk365.com/list/r500-t700"
								style="color: #666;" onclick="price('500-700元','27');" rel="nofollow">
								<em	>500-700元</em>
							</a>
						<a title="700-1000元租房" href="https://www.qk365.com/list/r700-t1000"
								style="color: #666;" onclick="price('700-1000元','28');" rel="nofollow">
								<em	>700-1000元</em>
							</a>
						<a title="1000-1500元租房" href="https://www.qk365.com/list/r1000-t1500"
								style="color: #666;" onclick="price('1000-1500元','29');" rel="nofollow">
								<em	>1000-1500元</em>
							</a>
						<a title="1500-2000元租房" href="https://www.qk365.com/list/r1500-t2000"
								style="color: #666;" onclick="price('1500-2000元','30');" rel="nofollow">
								<em	>1500-2000元</em>
							</a>
						<a title="2000-3000元租房" href="https://www.qk365.com/list/r2000-t3000"
								style="color: #666;" onclick="price('2000-3000元','73');" rel="nofollow">
								<em	>2000-3000元</em>
							</a>
						<a title="3000元以上租房" href="https://www.qk365.com/list/r3000"
								style="color: #666;" onclick="price('3000元以上','31');" rel="nofollow">
								<em	>3000元以上</em>
							</a>
						</span> 
					<span class="priceAuto fR">
						<em>自定义：</em> 
						<input name="priceL" maxlength="6" class="priceInput" type="text" id="priceL"
							value="" />
						<em>到</em>
						<input name="priceH" maxlength="6" class="priceInput" type="text" class="dd_input" id="priceH"
							value="" />
						<input type="button" value="确  定" id="bt_sub" class="priceSub"/>
					</span>
				</div>
				
				<!-- 行政区域 -->
				<div class="easySo" id="easySo">
					<span class="easySoTit fL">行政区域：</span> 
					<span class="easySoCon areaCon fL"> 
						<a title="上海租房" href="javascript:condition('prcId','');"> 
							<em 
								  class="cur" >不限</em>
						</a>
						<a title="黄浦区租房"
								href="https://www.qk365.com/list/a3" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','3');"> 
								<em 
									>
									黄浦区</em>
							</a>
						<a title="徐汇区租房"
								href="https://www.qk365.com/list/a4" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','4');"> 
								<em 
									>
									徐汇区</em>
							</a>
						<a title="长宁区租房"
								href="https://www.qk365.com/list/a5" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','5');"> 
								<em 
									>
									长宁区</em>
							</a>
						<a title="静安区租房"
								href="https://www.qk365.com/list/a6" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','6');"> 
								<em 
									>
									静安区</em>
							</a>
						<a title="普陀区租房"
								href="https://www.qk365.com/list/a7" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','7');"> 
								<em 
									>
									普陀区</em>
							</a>
						<a title="闸北区租房"
								href="https://www.qk365.com/list/a8" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','8');"> 
								<em 
									>
									闸北区</em>
							</a>
						<a title="虹口区租房"
								href="https://www.qk365.com/list/a9" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','9');"> 
								<em 
									>
									虹口区</em>
							</a>
						<a title="杨浦区租房"
								href="https://www.qk365.com/list/a10" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','10');"> 
								<em 
									>
									杨浦区</em>
							</a>
						<a title="闵行区租房"
								href="https://www.qk365.com/list/a11" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','11');"> 
								<em 
									>
									闵行区</em>
							</a>
						<a title="宝山区租房"
								href="https://www.qk365.com/list/a12" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','12');"> 
								<em 
									>
									宝山区</em>
							</a>
						<a title="嘉定区租房"
								href="https://www.qk365.com/list/a13" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','13');"> 
								<em 
									>
									嘉定区</em>
							</a>
						<a title="浦东新区租房"
								href="https://www.qk365.com/list/a14" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','14');"> 
								<em 
									>
									浦东新区</em>
							</a>
						<a title="金山区租房"
								href="https://www.qk365.com/list/a15" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','15');"> 
								<em 
									>
									金山区</em>
							</a>
						<a title="松江区租房"
								href="https://www.qk365.com/list/a16" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','16');"> 
								<em 
									>
									松江区</em>
							</a>
						<a title="青浦区租房"
								href="https://www.qk365.com/list/a17" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','17');"> 
								<em 
									>
									青浦区</em>
							</a>
						<a title="奉贤区租房"
								href="https://www.qk365.com/list/a18" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','18');"> 
								<em 
									>
									奉贤区</em>
							</a>
						<a title="崇明区租房"
								href="https://www.qk365.com/list/a19" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','19');"> 
								<em 
									>
									崇明区</em>
							</a>
						<a title="卢湾区租房"
								href="https://www.qk365.com/list/a26" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','26');"> 
								<em 
									>
									卢湾区</em>
							</a>
						<a title="上海花桥租房"
								href="https://sz.qk365.com/list/a37-k353" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','41');"> 
								<em 
									>
									上海花桥</em>
							</a>
						</a>
					</span>
				</div>
				<!-- 地铁沿线 -->
				<div class="easySo">
					<span class="easySoTit fL">地铁沿线：</span> 
					<span class="easySoCon metroSoList fL"> 
						<a title="上海租房" href="javascript:condition('subway','');"> 
							<i 
								  class="cur"  >不限</i>
						</a> 
						<a title="1号线租房" href="https://www.qk365.com/list/s1"
								style="color: #666;"
								onclick="condition('subway','1');"> 
								<em
									>
										1号线</em>
							</a>
						<a title="2号线租房" href="https://www.qk365.com/list/s2"
								style="color: #666;"
								onclick="condition('subway','2');"> 
								<em
									>
										2号线</em>
							</a>
						<a title="3号线租房" href="https://www.qk365.com/list/s3"
								style="color: #666;"
								onclick="condition('subway','3');"> 
								<em
									>
										3号线</em>
							</a>
						<a title="4号线租房" href="https://www.qk365.com/list/s4"
								style="color: #666;"
								onclick="condition('subway','4');"> 
								<em
									>
										4号线</em>
							</a>
						<a title="5号线租房" href="https://www.qk365.com/list/s5"
								style="color: #666;"
								onclick="condition('subway','5');"> 
								<em
									>
										5号线</em>
							</a>
						<a title="6号线租房" href="https://www.qk365.com/list/s6"
								style="color: #666;"
								onclick="condition('subway','6');"> 
								<em
									>
										6号线</em>
							</a>
						<a title="7号线租房" href="https://www.qk365.com/list/s7"
								style="color: #666;"
								onclick="condition('subway','7');"> 
								<em
									>
										7号线</em>
							</a>
						<a title="8号线租房" href="https://www.qk365.com/list/s8"
								style="color: #666;"
								onclick="condition('subway','8');"> 
								<em
									>
										8号线</em>
							</a>
						<a title="9号线租房" href="https://www.qk365.com/list/s9"
								style="color: #666;"
								onclick="condition('subway','9');"> 
								<em
									>
										9号线</em>
							</a>
						<a title="10号线租房" href="https://www.qk365.com/list/s10"
								style="color: #666;"
								onclick="condition('subway','10');"> 
								<em
									>
										10号线</em>
							</a>
						<a title="11号线租房" href="https://www.qk365.com/list/s11"
								style="color: #666;"
								onclick="condition('subway','11');"> 
								<em
									>
										11号线</em>
							</a>
						<a title="12号线租房" href="https://www.qk365.com/list/s12"
								style="color: #666;"
								onclick="condition('subway','12');"> 
								<em
									>
										12号线</em>
							</a>
						<a title="13号线租房" href="https://www.qk365.com/list/s13"
								style="color: #666;"
								onclick="condition('subway','13');"> 
								<em
									>
										13号线</em>
							</a>
						<a title="16号线租房" href="https://www.qk365.com/list/s16"
								style="color: #666;"
								onclick="condition('subway','16');"> 
								<em
									>
										16号线</em>
							</a>
						<a title="17号线租房" href="https://www.qk365.com/list/s54"
								style="color: #666;"
								onclick="condition('subway','54');"> 
								<em
									>
										17号线</em>
							</a>
						<a title="浦江线租房" href="https://www.qk365.com/list/s61"
								style="color: #666;"
								onclick="condition('subway','61');"> 
								<em
									>
										浦江线</em>
							</a>
						</span>
				</div>
				<!-- 房间户型 -->
				<div class="easySo">
					<span class="easySoTit fL">房间户型：</span> 
					<span class="easySoCon roomDoor fL"> 
						<a href="javascript:condition('romType','');" rel="nofollow"> 
							<em 
								 class="cur"  >不限</em>
						</a> 
						<a title="上海独卫租房" href="https://www.qk365.com/list/f1"
								style="color: #666;"
								onclick="condition('romType','1');" rel="nofollow"> 
								<em 
									>
									独卫</em>
							</a>
						<a title="上海单间租房" href="https://www.qk365.com/list/f2"
								style="color: #666;"
								onclick="condition('romType','2');" rel="nofollow"> 
								<em 
									>
									单间</em>
							</a>
						<a title="上海整租租房" href="https://www.qk365.com/list/f3"
								style="color: #666;"
								onclick="condition('romType','3');" rel="nofollow"> 
								<em 
									>
									整租</em>
							</a>
						</span>
				</div>
				<!-- 可租日期 -->
				<div class="easySo easySoNo">
					<span class="easySoTit fL">可租日期：</span> 
					<span class="easySoCon roomDoor fL"> 
						<a href="javascript:queryRent('');"> 
							<em 
								 class="cur" >不限</em>
						</a> 
						<a style="color: #666;" href="javascript:queryRent('anyTimeRent');"> 
							<em 
								>立即可租</em>
						</a> 
						<a style="color: #666;" href="javascript:queryRent('oneWeekRent');"> 
							<em
								>一周内可租</em>
						</a> 
						<a style="color: #666;" href="javascript:queryRent('twoWeekRent');"> 
							<em
								>两周内可租</em>
						</a> 
						<a style="color: #666;" href="javascript:queryRent('oneMonthRent');"> 
							<em
								>一月内可租</em>
						</a>
						<a style="color: #666;" href="javascript:queryRent('sixtyDayRent');"> 
							<em
								>两月内可租</em>
						</a>
					</span>
				</div>
				
				<!-- 特色标签 -->
				<div class="easySo">
					<span class="easySoTit fL" style="text-align:right;width:60px;">特色：</span> 
					<span class="easySoCon fL"> 
						<a href="javascript:queryFeature('');" rel="nofollow">
							<em	
								  class="cur" 
								>不限</em>
						</a>
						<a title="近地铁租房" 
								style="color: #666;" onclick="queryFeature('1');" rel="nofollow">
								<em
									
								>近地铁</em>
							</a>
						<a title="视频看房租房" 
								style="color: #666;" onclick="queryFeature('2');" rel="nofollow">
								<em
									
								>视频看房</em>
							</a>
						<a title="房东原装租房" 
								style="color: #666;" onclick="queryFeature('3');" rel="nofollow">
								<em
									
								>房东原装</em>
							</a>
						</span> 
				</div>
			</div>
			<div class="easySo easySocurrent">
				</div>
			
			<div class="easySort clearfix">
				<div class="easySo">
					<a onclick="javascript:sort('romVacantDays');"> <span
						class="easySoTit fL"> 默认排序： </span>
					</a> <span class="easySoCon roomDoor fL"> <a style="color: #666;" href="javascript:sort('showPrice');">
							<em
							>价格</em>
					</a> <a style="color: #666;" href="javascript:sort('romArea');"> <em
							>面积</em>
					</a> <a style="color: #666;" href="javascript:sort('cucSubwayDistance');"> <em
							>距地铁</em>
					</a> <a style="color: #666;" href="javascript:sort('romView');"> <em
							>浏览次数</em>
					</a>
							<a style="color: #666;" href="javascript:sort('cucVideoUrl');">
								<em id="new"
								>视频看房
									</em>
							</a>
					</span>
					<div class="SortSel fR">
						<em>总共6200间房间</em> <span class="sortInpLay">
							<input type="text" class="sortinText" id="houseRoad" onkeydown="keyUpSearch('qszf')"
								   onfocus="addLayer(this);"
							
							 value="输入区域、地铁、小区名" onfocus="if (this.value =='输入区域、地铁、小区名'){this.value =''}" onblur="if (this.value ==''){this.value='输入区域、地铁、小区名';$('.delete').hide();}"
						 
						 maxlength="50" />
						<input type="hidden" id="houseRoad_b" value="">
						<input type="hidden" id="stamp" value="spread">
						<em class="delete"></em>
						<input type="button" onclick="keySearch('qszf');" value="" class="sortSub">
						<ul class="jeasySearch blsearch hide" id="resultList">
						</ul>
						<ul class="easySearch blsearch hide" id="hotSearchList">
						</ul>
						</span>
					</div>
				</div>
			</div>
			<div class="preference">
	<div class="limit">
		<h4>限时特惠</h4>
		<a title="上海租房" href="https://www.qk365.com/todaySpecial" target="_blank">
			<img src="https://www.qk365.com/images/odds-more.png?v=20191225"
				 alt="上海租房"></a>
	</div>
	<div class="imgBox">
		<div class="Imgscrollbox" id="box0">
			<ul class="boxList">
				<li>
						<a title="上海知雅汇志成花苑租房" class="roomPic" href="https://www.qk365.com/room/91295" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/AF/FE/CgoKaF1H6G-ADfUVAABvFSHGggg415.jpg" title="九亭知雅汇志成花苑租房"
										 alt="上海租房"
										 onerror="defaultPic(this,'https://www.qk365.com/','0')">
								<p>
									<span><img src="https://www.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="松江区租房" class="addArea" href="https://www.qk365.com/list/a16" target="_blank">松江区</a>
                                    <span>
                                        <i><img src="https://www.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://www.qk365.com/xiaoqu/v6762" target="_blank" title="知雅汇志成花苑租房">知雅汇志成花苑</a>
                                    </span>
							</div>
							<p>
									<i>
										1280</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="上海如意家园租房" class="roomPic" href="https://www.qk365.com/room/106397" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/8D/DF/CgoKZ10v1sWAViKSAAB9ZSiFAFM543.jpg" title="柘林如意家园租房"
										 alt="上海租房"
										 onerror="defaultPic(this,'https://www.qk365.com/','0')">
								<div class="playSmall"><img src="https://www.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://www.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="奉贤区租房" class="addArea" href="https://www.qk365.com/list/a18" target="_blank">奉贤区</a>
                                    <span>
                                        <i><img src="https://www.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://www.qk365.com/xiaoqu/v24116" target="_blank" title="如意家园租房">如意家园</a>
                                    </span>
							</div>
							<p>
									<i>
										900</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="上海河东小区租房" class="roomPic" href="https://www.qk365.com/room/61178" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/9A/7E/CgoKZ1xFqmOADY4AAACMsNRMafM061.jpg" title="江桥河东小区租房"
										 alt="上海租房"
										 onerror="defaultPic(this,'https://www.qk365.com/','0')">
								<div class="playSmall"><img src="https://www.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://www.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="嘉定区租房" class="addArea" href="https://www.qk365.com/list/a13" target="_blank">嘉定区</a>
                                    <span>
                                        <i><img src="https://www.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://www.qk365.com/xiaoqu/v6490" target="_blank" title="河东小区租房">河东小区</a>
                                    </span>
							</div>
							<p>
									<i>
										1278</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="上海育秀东区租房" class="roomPic" href="https://www.qk365.com/room/106922" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/26/15/CgoKaFzSSwuAfuRIAACPGZufrT4272.jpg" title="南桥育秀东区租房"
										 alt="上海租房"
										 onerror="defaultPic(this,'https://www.qk365.com/','0')">
								<div class="playSmall"><img src="https://www.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://www.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="奉贤区租房" class="addArea" href="https://www.qk365.com/list/a18" target="_blank">奉贤区</a>
                                    <span>
                                        <i><img src="https://www.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://www.qk365.com/xiaoqu/v3620" target="_blank" title="育秀东区租房">育秀东区</a>
                                    </span>
							</div>
							<p>
									<i>
										647</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="上海美罗家园罗翔苑租房" class="roomPic" href="https://www.qk365.com/room/54137" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/97/DC/CgoKaFxFWK6ADdvtAABc2XqMym8106.jpg" title="罗店美罗家园罗翔苑租房"
										 alt="上海租房"
										 onerror="defaultPic(this,'https://www.qk365.com/','0')">
								<div class="playSmall"><img src="https://www.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://www.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="宝山区租房" class="addArea" href="https://www.qk365.com/list/a12" target="_blank">宝山区</a>
                                    <span>
                                        <i><img src="https://www.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://www.qk365.com/xiaoqu/v6813" target="_blank" title="美罗家园罗翔苑租房">美罗家园罗翔苑</a>
                                    </span>
							</div>
							<p>
									<i>
										1020</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				</ul>
		</div>
	</div>
	<a class="gor" id="gor0"><img src="https://www.qk365.com/images/nextSnap.png" alt="上海租房"></a>
</div>
<form id="roomForm" name="roomForm" method="post"
				action="https://www.qk365.com/list/">
				<input name="queryDto.priceFrom" id="priceFrom" type="hidden"
		value="" />
	<input name="queryDto.priceTo" id="priceTo" type="hidden"
		value="" />
	<input name="queryDto.priceId" id="priceId" type="hidden"
		value="" />
	<input name="queryDto.prcId" id="prcId" type="hidden"
		value="" />
	<input name="queryDto.cellArea" id="cellArea" type="hidden"
		value="" />
	<input name="queryDto.romType" id="romType" type="hidden"
		value="" />
	<input name="queryDto.romAds" id="romAds" type="hidden"
		value="" />
	<input name="queryDto.subway" id="subway" type="hidden"
		value="" />
		<input name="queryDto.station" id="station" type="hidden"
		value="" />
	<input name="queryDto.stationCode" id="stationCode" type="hidden"
		value="" />
	<input name="queryDto.currentPage" id="currentPage" type="hidden"
		value="1" />
	<input name="queryDto.pageSize" id="pageSize" type="hidden"
		value="21" />
	
	<input name="queryDto.orderByField" id="orderByField" type="hidden"
		value="" />
		<input name="queryDto.orderShort" id="orderShort" type="hidden"
		value="" />
	
	<input name="queryDto.sortDirection" id="sortDirection" type="hidden"
		value="" />
	
	<input name="queryDto.pinyin" id="pinyin" type="hidden"
		value="" />
	<input name="queryDto.village" id="village" type="hidden"
		value="" />
	
	<input name="queryDto.villageId" id="villageId" type="hidden"
		value="" />
	
	<input name="queryDto.order" id="order" type="hidden"
		value="" />
	<input name="queryDto.roomCode" id="roomCode" type="hidden"
		value="" />

	<input name="expectedCheckinTime" id="expectedCheckinTime"
		type="hidden" value="" />
	<input name="romAddress" id="romAddress" type="hidden" value="" />
    <input name="queryDto.rentDateName" id="rentDateName" type="hidden"
	   value="" />
    <input name="queryDto.activityId" id="activityId" type="hidden"
	   value="" />
    <input name="queryDto.activityLabelName" id="activityLabelName" type="hidden"
	   value="" />
	<input name="queryDto.feature" id="feature" type="hidden" value="" />
<input name="ajax" id="priceFrom" type="hidden" value="ajax" />
			</form>
			</div>
	</div>
	<div class="easyWarp">
		<div class="w1170 clearfix">
			<ul class="easyList">
				<li>
					<a target="_blank" title="上海美罗家园美文苑图"
						href="https://www.qk365.com/room/49077">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/96/F2/CgoKZ1xFQLuAQg0hAABf23kHEGk495.jpg" 
							alt="上海美罗家园美文苑图" title="上海美罗家园美文苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【宝山区】地铁七号线 罗南新村 美罗家园美文苑 精装白领公寓朝北单间 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1722</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="宝山区租房" href="https://www.qk365.com/list/a12">宝山区</a>-<a title="罗店租房" href="https://www.qk365.com/list/a12-k128">罗店</a>-<a title="美罗家园美文苑租房" href="https://www.qk365.com/xiaoqu/v6815">美罗家园美文苑</a>租房 4/18层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1208</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s7" title="7号线租房">7号线</a>
		                   	<a href="https://www.qk365.com/list/s7-e702" title="罗南新村租房">罗南新村</a>
		                   	<span>约1201米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10555728" title="美安路罗智路租房">美安…</a>
						 		<span>&nbsp;公交站约101米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海松南城华乐苑图"
						href="https://www.qk365.com/room/59214">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/96/B0/CgoKZ14LHXqALr-JAACa557EFP8823.jpg" 
							alt="上海松南城华乐苑图" title="上海松南城华乐苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【松江区】香亭路1200弄 松南城华乐苑 精装白领公寓 朝南带阳台出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1777</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="松江区租房" href="https://www.qk365.com/list/a16">松江区</a>-<a title="车墩镇租房" href="https://www.qk365.com/list/a16-k388">车墩镇</a>-<a title="松南城华乐苑租房" href="https://www.qk365.com/xiaoqu/v24219">松南城华乐苑</a>租房 7/17层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1365</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>&nbsp;</span><a href="https://www.qk365.com/list/s9" title="9号线租房">9号线</a>
		                   	<a href="https://www.qk365.com/list/s9-e9025" title="醉白池租房">醉白池；</a>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10036839" title="美德隆租房">美德…</a>
						 		<span>&nbsp;公交站约372米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海知雅汇志成花苑图"
						href="https://www.qk365.com/room/91295">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/AF/FE/CgoKaF1H6G-ADfUVAABvFSHGggg415.jpg" 
							alt="上海知雅汇志成花苑图" title="上海知雅汇志成花苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【松江区】涞坊路333弄 知雅汇志成花苑 精装白领公寓 单间次卧出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2570</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="松江区租房" href="https://www.qk365.com/list/a16">松江区</a>-<a title="九亭租房" href="https://www.qk365.com/list/a16-k203">九亭</a>-<a title="知雅汇志成花苑租房" href="https://www.qk365.com/xiaoqu/v6762">知雅汇志成花苑</a>租房 4/4层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1280</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s9" title="9号线租房">9号线</a>
		                   	<a href="https://www.qk365.com/list/s9-e9018" title="九亭租房">九亭</a>
		                   	<span>约1728米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10507228" title="涞坊路(知雅汇)租房">涞坊…</a>
						 		<span>&nbsp;公交站约39米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海中山茸惠苑图"
						href="https://www.qk365.com/room/103397">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A9/46/CgoKaFxIS0-AYujqAABuKmogSHA125.jpg" 
							alt="上海中山茸惠苑图" title="上海中山茸惠苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【松江区】9号线 松江大学城 近万达广场 中山茸惠苑 精装单间出租</p>
					</div>
					<em class="fr0923">
						<b>原价:2101</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="松江区租房" href="https://www.qk365.com/list/a16">松江区</a>-<a title="洞泾租房" href="https://www.qk365.com/list/a16-k368">洞泾</a>-<a title="中山茸惠苑租房" href="https://www.qk365.com/xiaoqu/v27337">中山茸惠苑</a>租房 10/17层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1665</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>&nbsp;</span><a href="https://www.qk365.com/list/s9" title="9号线租房">9号线</a>
		                   	<a href="https://www.qk365.com/list/s9-e9022" title="松江大学城租房">松江大学…；</a>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10035009" title="沪松公路辰花公路租房">沪松…</a>
						 		<span>&nbsp;公交站约297米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海如意家园图"
						href="https://www.qk365.com/room/106397">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/8D/DF/CgoKZ10v1sWAViKSAAB9ZSiFAFM543.jpg" 
							alt="上海如意家园图" title="上海如意家园图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【奉贤区】拓林  新塘路198弄   如意家园   精装白领公寓朝南主卧带独卫出租   配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1515</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="奉贤区租房" href="https://www.qk365.com/list/a18">奉贤区</a>-<a title="柘林租房" href="https://www.qk365.com/list/a18-k240">柘林</a>-<a title="如意家园租房" href="https://www.qk365.com/xiaoqu/v24116">如意家园</a>租房 3/18层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>主卧</i>
		<i>独卫</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>900</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10385567" title="骑塘村租房">骑塘村</a>
						 		<span>&nbsp;公交站约687米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海河东小区图"
						href="https://www.qk365.com/room/61178">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9A/7E/CgoKZ1xFqmOADY4AAACMsNRMafM061.jpg" 
							alt="上海河东小区图" title="上海河东小区图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【嘉定区】吴杨路100弄 封浜小学旁  河东小区  精装白领公寓朝南单间出租  配备齐全  拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:2371</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="嘉定区租房" href="https://www.qk365.com/list/a13">嘉定区</a>-<a title="江桥租房" href="https://www.qk365.com/list/a13-k146">江桥</a>-<a title="河东小区租房" href="https://www.qk365.com/xiaoqu/v6490">河东小区</a>租房 6/6层
                                        </span>
							</p>
							<p class="p2">
								<i>房东原装</i>
		<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1278</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10420844" title="星华公路乡思路租房">星华公路乡思路</a>
						 		<span>&nbsp;公交站约95米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海育秀东区图"
						href="https://www.qk365.com/room/106922">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/26/15/CgoKaFzSSwuAfuRIAACPGZufrT4272.jpg" 
							alt="上海育秀东区图" title="上海育秀东区图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【奉贤区】南桥镇   育秀东区    精装白领公寓    精装卧室出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1340</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="奉贤区租房" href="https://www.qk365.com/list/a18">奉贤区</a>-<a title="南桥租房" href="https://www.qk365.com/list/a18-k235">南桥</a>-<a title="育秀东区租房" href="https://www.qk365.com/xiaoqu/v3620">育秀东区</a>租房 5/6层
                                        </span>
							</p>
							<p class="p2">
								<i>房东原装</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>647</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10568758" title="育秀路租房">育秀路</a>
						 		<span>&nbsp;公交站约25米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海金地都会艺境图"
						href="https://www.qk365.com/room/92510">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/99/07/CgoKaF039euAVM2qAABmkU1NDbQ691.jpg" 
							alt="上海金地都会艺境图" title="上海金地都会艺境图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【松江区】 陈春公路677弄 金地都会艺境 精装白领公寓朝南单间出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2451</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="松江区租房" href="https://www.qk365.com/list/a16">松江区</a>-<a title="莘闵租房" href="https://www.qk365.com/list/a16-k218">莘闵</a>-<a title="金地都会艺境租房" href="https://www.qk365.com/xiaoqu/v9252">金地都会艺境</a>租房 2/3层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1212</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10038221" title="陈春路明兴路租房">陈春路明兴路</a>
						 		<span>&nbsp;公交站约241米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海美罗家园罗翔苑图"
						href="https://www.qk365.com/room/54137">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/97/DC/CgoKaFxFWK6ADdvtAABc2XqMym8106.jpg" 
							alt="上海美罗家园罗翔苑图" title="上海美罗家园罗翔苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【宝山区】地铁七号线 罗南新村 美罗家园罗翔苑 精装白领公寓 朝南卧室 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1965</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="宝山区租房" href="https://www.qk365.com/list/a12">宝山区</a>-<a title="罗店租房" href="https://www.qk365.com/list/a12-k128">罗店</a>-<a title="美罗家园罗翔苑租房" href="https://www.qk365.com/xiaoqu/v6813">美罗家园罗翔苑</a>租房 7/18层
                                        </span>
							</p>
							<p class="p2">
								<i>朝南</i>
		<i>飘窗</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1020</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s7" title="7号线租房">7号线</a>
		                   	<a href="https://www.qk365.com/list/s7-e702" title="罗南新村租房">罗南新村</a>
		                   	<span>约1716米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10515195" title="罗和路天家路租房">罗和…</a>
						 		<span>&nbsp;公交站约145米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海聚航苑一期图"
						href="https://www.qk365.com/room/106900">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/5B/7F/CgoKZ10GEVKAefUhAACe2xJBzRo792.jpg" 
							alt="上海聚航苑一期图" title="上海聚航苑一期图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【浦东新区】航梅路526弄 聚航苑一期 精装白领公寓 朝南带阳台出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2035</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="浦东新区租房" href="https://www.qk365.com/list/a14">浦东新区</a>-<a title="航头租房" href="https://www.qk365.com/list/a14-k159">航头</a>-<a title="聚航苑一期租房" href="https://www.qk365.com/xiaoqu/v11197">聚航苑一期</a>租房 6/6层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1187</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10505474" title="航梅路航定路租房">航梅路航定路</a>
						 		<span>&nbsp;公交站约219米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海育苑小区南区图"
						href="https://www.qk365.com/room/6152">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/5F/8A/CgoKaF0JzViAdzzTAABm0ta_3_0227.jpg" 
							alt="上海育苑小区南区图" title="上海育苑小区南区图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【嘉定区】11号线 马陆 马陆育苑小区 精装全配 家电齐全 拎包入住</p>
					</div>
					<em class="fr0923">
						<b>原价:1816</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="嘉定区租房" href="https://www.qk365.com/list/a13">嘉定区</a>-<a title="马陆租房" href="https://www.qk365.com/list/a13-k149">马陆</a>-<a title="育苑小区南区租房" href="https://www.qk365.com/xiaoqu/v2215">育苑小区南区</a>租房 3/4层
                                        </span>
							</p>
							<p class="p2">
								<i>主卧</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1086</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s11" title="11号线租房">11号线</a>
		                   	<a href="https://www.qk365.com/list/s11-e11020" title="马陆租房">马陆</a>
		                   	<span>约1523米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10031078" title="沪宜公路亚钢路租房">沪宜…</a>
						 		<span>&nbsp;公交站约350米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海盛蔷坊图"
						href="https://www.qk365.com/room/82039">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A3/35/CgoKZ1xHIcCAV1iTAAB10wUYTCE739.jpg" 
							alt="上海盛蔷坊图" title="上海盛蔷坊图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【嘉定区】地铁11号线 嘉定西站 盛蔷坊 精装白领公寓朝南单间出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1568</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="嘉定区租房" href="https://www.qk365.com/list/a13">嘉定区</a>-<a title="菊园新区租房" href="https://www.qk365.com/list/a13-k147">菊园新区</a>-<a title="盛蔷坊租房" href="https://www.qk365.com/xiaoqu/v3908">盛蔷坊</a>租房 3/18层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1368</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s11" title="11号线租房">11号线</a>
		                   	<a href="https://www.qk365.com/list/s11-e11030" title="嘉定西租房">嘉定西</a>
		                   	<span>约1396米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10410444" title="嘉朱公路四号桥租房">嘉朱…</a>
						 		<span>&nbsp;公交站约305米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海英雄新村小区图"
						href="https://www.qk365.com/room/101821">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A9/F0/CgoKaFxIcWKAPz-qAABWEjXN8PE713.jpg" 
							alt="上海英雄新村小区图" title="上海英雄新村小区图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【浦东新区】16号线   惠南站  英雄新村小区 精装白领公寓单间出租  配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1524</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="浦东新区租房" href="https://www.qk365.com/list/a14">浦东新区</a>-<a title="惠南镇租房" href="https://www.qk365.com/list/a14-k161">惠南镇</a>-<a title="英雄新村小区租房" href="https://www.qk365.com/xiaoqu/v28755">英雄新村小区</a>租房 5/5层
                                        </span>
							</p>
							<p class="p2">
								<i>房东原装</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>741</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s16" title="16号线租房">16号线</a>
		                   	<a href="https://www.qk365.com/list/s16-e1609" title="惠南租房">惠南</a>
		                   	<span>约1832米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10524720" title="英雄路福缘路租房">英雄…</a>
						 		<span>&nbsp;公交站约12米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海人民南路图"
						href="https://www.qk365.com/room/57892">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9C/7B/CgoKaFxF7y2Ad6tGAABhVAdgH2E642.jpg" 
							alt="上海人民南路图" title="上海人民南路图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【松江区】地铁9号线 醉白池站 人民南路 精装白领公寓 朝南次卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2225</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="松江区租房" href="https://www.qk365.com/list/a16">松江区</a>-<a title="中山中路租房" href="https://www.qk365.com/list/a16-k221">中山中路</a>-<a title="人民南路租房" href="https://www.qk365.com/xiaoqu/v24297">人民南路</a>租房 5/5层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1205</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s9" title="9号线租房">9号线</a>
		                   	<a href="https://www.qk365.com/list/s9-e9025" title="醉白池租房">醉白池</a>
		                   	<span>约486米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10027911" title="人民南路松汇路租房">人民…</a>
						 		<span>&nbsp;公交站约15米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海世贸爱马尚郡图"
						href="https://www.qk365.com/room/84076">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/D8/CgoKZ1xGsMeACQ2mAACkQpELiLA513.jpg" 
							alt="上海世贸爱马尚郡图" title="上海世贸爱马尚郡图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【奉贤区】 地铁5号线 奉贤新城 世贸爱马尚郡 精装白领公寓朝南主卧带阳台 单间出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1553</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="奉贤区租房" href="https://www.qk365.com/list/a18">奉贤区</a>-<a title="海湾旅游区租房" href="https://www.qk365.com/list/a18-k231">海湾旅游区</a>-<a title="世贸爱马尚郡租房" href="https://www.qk365.com/xiaoqu/v24649">世贸爱马尚郡</a>租房 3/4层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>主卧</i>
		<i>阳台</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>798</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10486737" title="星火农工商租房">星火农工商</a>
						 		<span>&nbsp;公交站约219米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海世贸爱马尚郡图"
						href="https://www.qk365.com/room/84077">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/D8/CgoKZ1xGsNeAfLmjAACQllSxNHM205.jpg" 
							alt="上海世贸爱马尚郡图" title="上海世贸爱马尚郡图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【奉贤区】 地铁5号线 奉贤新城 世贸爱马尚郡 精装白领公寓 主卧带阳台出租 安全卫生 性价比高 可月付</p>
					</div>
					<em class="fr0923">
						<b>原价:1233</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="奉贤区租房" href="https://www.qk365.com/list/a18">奉贤区</a>-<a title="海湾旅游区租房" href="https://www.qk365.com/list/a18-k231">海湾旅游区</a>-<a title="世贸爱马尚郡租房" href="https://www.qk365.com/xiaoqu/v24649">世贸爱马尚郡</a>租房 4/4层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>主卧</i>
		<i>阳台</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>625</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10486737" title="星火农工商租房">星火农工商</a>
						 		<span>&nbsp;公交站约219米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海世贸爱马尚郡图"
						href="https://www.qk365.com/room/84079">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/D8/CgoKaFxGsNOAK4baAACNcj6eiTA864.jpg" 
							alt="上海世贸爱马尚郡图" title="上海世贸爱马尚郡图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【奉贤区】 地铁5号线 奉贤新城 世贸爱马尚郡 精装白领公寓 朝南次卧带阳台出租 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1410</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="奉贤区租房" href="https://www.qk365.com/list/a18">奉贤区</a>-<a title="海湾旅游区租房" href="https://www.qk365.com/list/a18-k231">海湾旅游区</a>-<a title="世贸爱马尚郡租房" href="https://www.qk365.com/xiaoqu/v24649">世贸爱马尚郡</a>租房 4/4层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>729</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10486737" title="星火农工商租房">星火农工商</a>
						 		<span>&nbsp;公交站约219米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海瑞和雅苑·壹街区图"
						href="https://www.qk365.com/room/100622">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A3/D9/CgoKaFxHP7WABBvjAABA3GjQbnk884.jpg" 
							alt="上海瑞和雅苑·壹街区图" title="上海瑞和雅苑·壹街区图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【闵行区】地铁98号线 沈杜公路站 瑞和雅苑·壹街区 精装白领公寓 朝南卧室带阳台出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2205</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="闵行区租房" href="https://www.qk365.com/list/a11">闵行区</a>-<a title="浦江镇租房" href="https://www.qk365.com/list/a11-k116">浦江镇</a>-<a title="瑞和雅苑·壹街区租房" href="https://www.qk365.com/xiaoqu/v25728">瑞和雅苑·壹街区</a>租房 14/18层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>阳台</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1558</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s61" title="浦江线租房">浦江线</a>
		                   	<a href="https://www.qk365.com/list/s61-e20711" title="三鲁公路租房">三鲁公路</a>
		                   	<span>约1745米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10037204" title="浦江宝邸租房">浦江…</a>
						 		<span>&nbsp;公交站约463米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海培元新苑图"
						href="https://www.qk365.com/room/81686">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/B1/CgoKZ1xGSc6AUgzyAABlJ9GDHQw336.jpg" 
							alt="上海培元新苑图" title="上海培元新苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【浦东新区】地铁2号线 创新中路站 培元新苑 精装白领公寓 朝南主卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:3230</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="浦东新区租房" href="https://www.qk365.com/list/a14">浦东新区</a>-<a title="唐镇租房" href="https://www.qk365.com/list/a14-k177">唐镇</a>-<a title="培元新苑租房" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>租房 7/17层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>主卧</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>2415</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s2" title="2号线租房">2号线</a>
		                   	<a href="https://www.qk365.com/list/s2-e2025" title="创新中路租房">创新中路</a>
		                   	<span>约585米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10382262" title="机口村租房">机口…</a>
						 		<span>&nbsp;公交站约96米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海松南城谷水佳苑图"
						href="https://www.qk365.com/room/81446">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/40/CgoKZ1xGljGANQuWAABTWW9-6fA582.jpg" 
							alt="上海松南城谷水佳苑图" title="上海松南城谷水佳苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【松江区】9号线 醉白池站 松南城谷水佳苑 精装白领公寓朝南单间出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1918</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="松江区租房" href="https://www.qk365.com/list/a16">松江区</a>-<a title="松江老城租房" href="https://www.qk365.com/list/a16-k213">松江老城</a>-<a title="松南城谷水佳苑租房" href="https://www.qk365.com/xiaoqu/v25852">松南城谷水佳苑</a>租房 10/17层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>904</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s9" title="9号线租房">9号线</a>
		                   	<a href="https://www.qk365.com/list/s9-e9026" title="松江南站租房">松江南站</a>
		                   	<span>约910米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10038103" title="富强路金玉路租房">富强…</a>
						 		<span>&nbsp;公交站约109米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="上海培元新苑图"
						href="https://www.qk365.com/room/82223">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A1/97/CgoKZ1xG0nCATYRPAABrxbWA12k081.jpg" 
							alt="上海培元新苑图" title="上海培元新苑图"
							onerror="this.src='https://www.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://www.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【浦东新区】2号线 创新中路站 培元新苑 精装白领公寓 朝南主卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:3313</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="浦东新区租房" href="https://www.qk365.com/list/a14">浦东新区</a>-<a title="唐镇租房" href="https://www.qk365.com/list/a14-k177">唐镇</a>-<a title="培元新苑租房" href="https://www.qk365.com/xiaoqu/v27081">培元新苑</a>租房 10/17层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>主卧</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1840</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://www.qk365.com/list/s2" title="2号线租房">2号线</a>
		                   	<a href="https://www.qk365.com/list/s2-e2025" title="创新中路租房">创新中路</a>
		                   	<span>约585米；</span>
						<span>距&nbsp;</span><a href="https://www.qk365.com/bus/10382262" title="机口村租房">机口…</a>
						 		<span>&nbsp;公交站约96米</span>
					 		</a>
					</div>
					</div>
				</li>
				</ul>
		</div>
		<p class="easyPage">
  <a href="https://www.qk365.com/list/" onclick="javascript:void(0);return false;" class="prePage">&nbsp;</a>
    <a href="https://www.qk365.com/list/" onclick="javascript:void(0);return false;" class="active">1</a>
        <a href="https://www.qk365.com/list/p2" onclick="javascript:simpleTable.togglePage(2);return false;">2</a>
          <a href="https://www.qk365.com/list/p3" onclick="javascript:simpleTable.togglePage(3);return false;">3</a>
          <a href="https://www.qk365.com/list/p4" onclick="javascript:simpleTable.togglePage(4);return false;">4</a>
          <a href="https://www.qk365.com/list/p5" onclick="javascript:simpleTable.togglePage(5);return false;">5</a>
          <a href="https://www.qk365.com/list/p6" onclick="javascript:simpleTable.togglePage(6);return false;">6</a>
          <a href="https://www.qk365.com/list/p7" onclick="javascript:simpleTable.togglePage(7);return false;">7</a>
          <a class="nextPage" href="https://www.qk365.com/list/p2" onclick="javascript:simpleTable.togglePage(2);return false;">&nbsp;</a>
      </p>
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
</div><script type="text/javascript"
		src="https://www.qk365.com/js/jquery-1.11.0.min.js"></script>
	<script type="text/javascript"
		src="https://www.qk365.com/js/homepage/autoFill.js"></script>
	<script type="text/javascript"
		src="https://www.qk365.com/js/homepage/homepage.js?version=20171102"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/public/public.js?v=20181025"></script>
	<script src="https://www.qk365.com/js/require.js"
		data-main="https://www.qk365.com/js/main.js?version=20171024"></script>
	<script src="https://www.qk365.com/js/public/sc.js?v=20170808"></script>
	<script type="text/javascript">
	var titleindex = '1';
	if(titleindex==''){
		titleindex = 0;
	}
	$(document).ready(function(){
		$("#titleindex"+titleindex).addClass("active");
	});
		var basePathUrl = 'https://www.qk365.com/';
	</script>
	<script type="text/javascript" src="https://www.qk365.com/widgets/simpletable/simpletable.js"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/roomdetail/findrooms.js?v=20190524"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/common/urlMatch.js?v=20190524"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/js/recomBox.js"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/common/topanv.js?version=20170808"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/hide-box.js"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/activityViewCount.js"></script>
	<script type="text/javascript" src="https://www.qk365.com/js/houseView360.js?v=20171225"></script>
	<script type="text/javascript">
	function initSimpleTable(){
		if(typeof(SimpleTable)!= 'function'){
			setTimeout("initSimpleTable()",100);
		}else{
			window.simpleTable = new SimpleTable('roomForm',1,21,'','currentPage','pageSize','sortColumns');
		}
	 }
		// 分页需要依赖的初始化动作
		initSimpleTable();
	    $(function(){
	        $('#keywords').bind('keypress',function(event){
	            if(event.keyCode == "13")    
	            {
	            	romAds();
	            }
	        });
	    });
		</script>
	<script type="text/javascript" src="https://www.qk365.com/js/activityLabel.js"></script>
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
					<li>友情链接<i></i></li>
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
                <div class="tabBox4">
			                     <div class="fotLink">
							<a href="https://www.qk365.com/list" target="_blank">房屋出租</a>
								
									|
								<a href="https://www.qk365.com/list" target="_blank">出租信息</a>
								
									|
								<a href="https://www.qk365.com/qkkx/index.html" target="_blank">青客快讯</a>
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
<link href="https://www.qk365.com/css/alert.css?v=20200824" rel="stylesheet" type="text/css" />
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
<script type="text/javascript" src="https://www.qk365.com/js/alert.js?v=20191115"></script></body>
</html>


Process finished with exit code 0

'''
# html_doc = etree.HTML(html_str)
# print(''.join(html_doc.xpath("//ins[@id='nb_invite_cancel']/text()")))
# print(''.join(html_doc.xpath("//ins[@id='nb_invite_ok']/text()")))
soup = BeautifulSoup(html_str,'lxml')
# # 获取标签
# print(soup.title)
# # 获取内容title
# print(soup.title.text)
# print(soup.title.string)
# print(soup.title.get_text())
#
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a['href'])
# print(soup.a.get('href'))

# soup.find()
# tag_list = soup.find_all('a')
# tag_list = soup.find_all('i')

# tag_list = soup.find_all(re.compile('^d'))
# tag_list = soup.find_all(re.compile('^i$'))
# tag_list = soup.find_all(re.compile('^a'))
# 搜索文档中的字符串
# tag_list = soup.find_all(text=904)
# tag_list = soup.find_all(class_='easyList')
# tag_list = soup.find_all(id='roomForm')
# tag_list = soup.find_all(name='roomForm')
# print(tag_list)
# print(len(tag_list))

# css
# print(soup.select('title'))

# id选择器
# print(soup.select('#roomForm'))

# class选择器
# print(soup.select('.easyList'))

# 组合查找
print(soup.select('li > img'))

#
print(soup.select('ul[class="easyList"]'))

# print(soup.select_one('title'))


