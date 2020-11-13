import requests
import time
from lxml import etree

url = 'https://hz.qk365.com/list'
# //div[@class='clearfix']/div/span/i
# html = requests.get(url).text
html = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/xpath爬取青客.py"
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>杭州租房网_杭州合租|房屋出租信息网_青客时尚租房网</title>
<meta http-equiv="Cache-Control" content="no-transform " />
<meta name="applicable-device" content="pc">
<meta name="keywords"
	 content="杭州租房网、杭州合租、杭州房屋出租、杭州租房信息网"   />
<meta name="description"
	 content="青客租房网提供杭州同城全新全面的房屋出租信息，所有租房统一装修、设施齐全、租房临近地铁、无中介、定期保洁，是居家生活办公首选。杭州租房、找合租、个人房屋出租，就上青客租房网。"   />
<link rel="alternate" media="only screen and (max-width: 640px)"
	
			href="https://i.qk365.com/hz/list/"
		
		/>
<link href="https://hz.qk365.com/css/find.css?v=20191206" rel="stylesheet" type="text/css">
<script type="text/javascript" src="https://hz.qk365.com/js/homepage/defaultPic.js"></script>
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
<link href="https://hz.qk365.com/css/reset.css?v=20191205" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/style.css?v=20200901" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/head
.css?v=20191204" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/footer.css?v=20191204" rel="stylesheet" type="text/css">
<link href="https://hz.qk365.com/css/user.css?version=20191205" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="https://hz.qk365.com/css/packet.css?version=20180124" type="text/css">

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
        <a class="logo" title="杭州租房" href="https://hz.qk365.com/">
        	<img src="https://hz.qk365.com/images/2019-11-29-img/logo.png" alt="杭州租房" />
        </a>
        <div class="popup">杭州</div>
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
                    <a href="https://hz.qk365.com/list" title="杭州轻松找房">轻松找房</a>
                    <a href="https://hz.qk365.com/xiaoqu" title="杭州小区租房">小区租房</a>
                    <a href="https://hz.qk365.com/todaySpecial" title="杭州今日特惠">今日特惠</a>
                    <a href="https://hz.qk365.com/bus" title="杭州公交沿线租房">公交找房</a>
                </div>
            </li>
            <li>
                <a href="https://hz.qk365.com/map" target="_blank" class="subnav-top" title="杭州租房地图找房">地图找房</a>
            </li>
            <li>
                <a href="https://hz.qk365.com/fwtg" target="_blank" rel="nofollow" class="subnav-top" title="杭州租房房屋托管">房屋托管</a>
            </li>
            <li>
                <button class="subnav-top">商务合作</button>
                <div class="dropnav">
                    <a href="https://hz.qk365.com/supplier/index" rel="nofollow" title="杭州租房商务合作">商务合作</a>
                    <a href="https://hz.qk365.com/to/jsp_government" rel="nofollow" title="杭州政府视窗">政府视窗</a>
                </div>
            </li>
            <li>
                <button class="subnav-top">青客快讯</button>
                <div class="dropnav">
                    <a href="https://hz.qk365.com/qkkx/index.html" title="杭州租房">快讯首页</a>
                    <a href="https://hz.qk365.com/qkkx/zfgl/index.html" title="杭州租房找房攻略">找房攻略</a>
                    <a href="https://hz.qk365.com/qkkx/hydt/index.html" title="杭州租房行业动态">行业动态</a>
                    <a href="https://hz.qk365.com/qkkx/ssrd/index.html" title="杭州租房时事热点">时事热点</a>
                    <a href="https://hz.qk365.com/qkkx/sqgl/index.html" title="杭州租房省钱攻略">省钱攻略</a>
                    <a href="https://hz.qk365.com/qkkx/bmxx/index.html" title="杭州租房便民信息">便民信息</a>
                    <a href="https://hz.qk365.com/qkkx/zzhd/index.html" title="杭州租房组织活动">组织活动</a>
                    <a href="https://hz.qk365.com/mail.do" rel="nofollow" title="鸡毛信">鸡毛信</a>
                    </div>
            </li>
            <li>
                <button class="subnav-top">移动青客</button>
                <div class="dropnav">
                    <a href="https://www.qk365.com/qkkx/zthd/2019/7627932.html">下载APP</a>
                    <a href="https://i.qk365.com/hz">手机官网</a>
						</div>
            </li>
            
            <li class="" id="noLogin">
                <a href="https://hz.qk365.com/security/register" id="loginli" class="subnav-top" rel="nofollow">注册登录<em></em></a>
            </li>
            <li class="userico" id="loginIn" style="display: none">
                <a href="javascript:;" class="subnav-top pepSnapLogin"><i></i>注册登录</a>
                <div class="dropnav">
                    <a href="javascript:;" id="topMyData">我的资料</a>
					<a href="https://hz.qk365.com/security/reservation.do">我的预约</a>
					<a href="https://hz.qk365.com/security/subscribe.do">我的订阅</a>
					<a href="https://hz.qk365.com/security/userCouponsActivities.do">我的优惠券</a>
					<a href="https://hz.qk365.com/security/collection.do">我的收藏</a>
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
						<a title="杭州租房" href="https://hz.qk365.com">杭州租房</a> </div>
				<em>></em>
					<div class="posbox">
						<a title="轻松找房" href="https://hz.qk365.com/list">轻松找房</a>
								</div>
				</div>
			<div id="seledbox" class="posiabox">
			<div class="area areaCur">
						<a title="上海租房" href="https://www.qk365.com" target="_blank">上海租房</a>
						<a title="苏州租房" href="https://sz.qk365.com" target="_blank">苏州租房</a>
						<a title="北京租房" href="https://bj.qk365.com" target="_blank">北京租房</a>
						<a title="嘉兴租房" href="https://jx.qk365.com" target="_blank">嘉兴租房</a>
						<a title="南京租房" href="https://nj.qk365.com" target="_blank">南京租房</a>
						<a title="武汉租房" href="https://wh.qk365.com" target="_blank">武汉租房</a>
						<a title="天津租房" href="https://tj.qk365.com" target="_blank">天津租房</a>
						</div>
				<div class="area">
						<a title="小区找房" href="https://hz.qk365.com/xiaoqu" target="_blank">小区找房</a>
								<a title="地图找房" href="https://hz.qk365.com/map" target="_blank">地图找房</a>
								<a title="今日特惠" href="https://hz.qk365.com/todaySpecial" target="_blank">今日特惠</a>
								<a title="公交沿线租房" href="https://hz.qk365.com/bus/" target="_blank">公交沿线租房</a>
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
						<a title="500元以下租房" href="https://hz.qk365.com/list/r0-t500"
								style="color: #666;" onclick="price('500元以下','76');" rel="nofollow">
								<em	>500元以下</em>
							</a>
						<a title="500-700元租房" href="https://hz.qk365.com/list/r500-t700"
								style="color: #666;" onclick="price('500-700元','27');" rel="nofollow">
								<em	>500-700元</em>
							</a>
						<a title="700-1000元租房" href="https://hz.qk365.com/list/r700-t1000"
								style="color: #666;" onclick="price('700-1000元','28');" rel="nofollow">
								<em	>700-1000元</em>
							</a>
						<a title="1000-1500元租房" href="https://hz.qk365.com/list/r1000-t1500"
								style="color: #666;" onclick="price('1000-1500元','29');" rel="nofollow">
								<em	>1000-1500元</em>
							</a>
						<a title="1500-2000元租房" href="https://hz.qk365.com/list/r1500-t2000"
								style="color: #666;" onclick="price('1500-2000元','30');" rel="nofollow">
								<em	>1500-2000元</em>
							</a>
						<a title="2000-3000元租房" href="https://hz.qk365.com/list/r2000-t3000"
								style="color: #666;" onclick="price('2000-3000元','73');" rel="nofollow">
								<em	>2000-3000元</em>
							</a>
						<a title="3000元以上租房" href="https://hz.qk365.com/list/r3000"
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
						<a title="杭州租房" href="javascript:condition('prcId','');"> 
							<em 
								  class="cur" >不限</em>
						</a>
						<a title="上城区租房"
								href="https://hz.qk365.com/list/a47" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','47');"> 
								<em 
									>
									上城区</em>
							</a>
						<a title="下城区租房"
								href="https://hz.qk365.com/list/a48" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','48');"> 
								<em 
									>
									下城区</em>
							</a>
						<a title="江干区租房"
								href="https://hz.qk365.com/list/a49" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','49');"> 
								<em 
									>
									江干区</em>
							</a>
						<a title="拱墅区租房"
								href="https://hz.qk365.com/list/a50" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','50');"> 
								<em 
									>
									拱墅区</em>
							</a>
						<a title="西湖区租房"
								href="https://hz.qk365.com/list/a51" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','51');"> 
								<em 
									>
									西湖区</em>
							</a>
						<a title="滨江区租房"
								href="https://hz.qk365.com/list/a52" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','52');"> 
								<em 
									>
									滨江区</em>
							</a>
						<a title="萧山区租房"
								href="https://hz.qk365.com/list/a53" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','53');"> 
								<em 
									>
									萧山区</em>
							</a>
						<a title="余杭区租房"
								href="https://hz.qk365.com/list/a54" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','54');"> 
								<em 
									>
									余杭区</em>
							</a>
						<a title="桐庐县租房"
								href="https://hz.qk365.com/list/a55" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','55');"> 
								<em 
									>
									桐庐县</em>
							</a>
						<a title="淳安县租房"
								href="https://hz.qk365.com/list/a56" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','56');"> 
								<em 
									>
									淳安县</em>
							</a>
						<a title="建德市租房"
								href="https://hz.qk365.com/list/a57" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','57');"> 
								<em 
									>
									建德市</em>
							</a>
						<a title="富阳市租房"
								href="https://hz.qk365.com/list/a58" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','58');"> 
								<em 
									>
									富阳市</em>
							</a>
						<a title="临安市租房"
								href="https://hz.qk365.com/list/a59" 
								style="color: #666;" id="xzqy"
								
								onclick="condition('prcId','59');"> 
								<em 
									>
									临安市</em>
							</a>
						</a>
					</span>
				</div>
				<!-- 地铁沿线 -->
				<div class="easySo">
					<span class="easySoTit fL">地铁沿线：</span> 
					<span class="easySoCon metroSoList fL"> 
						<a title="杭州租房" href="javascript:condition('subway','');"> 
							<i 
								  class="cur"  >不限</i>
						</a> 
						<a title="1号线租房" href="https://hz.qk365.com/list/s19"
								style="color: #666;"
								onclick="condition('subway','19');"> 
								<em
									>
										1号线</em>
							</a>
						<a title="2号线租房" href="https://hz.qk365.com/list/s20"
								style="color: #666;"
								onclick="condition('subway','20');"> 
								<em
									>
										2号线</em>
							</a>
						<a title="4号线租房" href="https://hz.qk365.com/list/s21"
								style="color: #666;"
								onclick="condition('subway','21');"> 
								<em
									>
										4号线</em>
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
						<a title="杭州独卫租房" href="https://hz.qk365.com/list/f1"
								style="color: #666;"
								onclick="condition('romType','1');" rel="nofollow"> 
								<em 
									>
									独卫</em>
							</a>
						<a title="杭州单间租房" href="https://hz.qk365.com/list/f2"
								style="color: #666;"
								onclick="condition('romType','2');" rel="nofollow"> 
								<em 
									>
									单间</em>
							</a>
						<a title="杭州整租租房" href="https://hz.qk365.com/list/f3"
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
						<em>总共3392间房间</em> <span class="sortInpLay">
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
		<a title="杭州租房" href="https://hz.qk365.com/todaySpecial" target="_blank">
			<img src="https://hz.qk365.com/images/odds-more.png?v=20191225"
				 alt="杭州租房"></a>
	</div>
	<div class="imgBox">
		<div class="Imgscrollbox" id="box0">
			<ul class="boxList">
				<li>
						<a title="杭州绿都四季华庭租房" class="roomPic" href="https://hz.qk365.com/room/78081" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/BB/E1/CgoKaF1RMdiAP6lcAABuTVqMt1A376.jpg" title="城厢绿都四季华庭租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="萧山区租房" class="addArea" href="https://hz.qk365.com/list/a53" target="_blank">萧山区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v6025" target="_blank" title="绿都四季华庭租房">绿都四季华庭</a>
                                    </span>
							</div>
							<p>
									<i>
										1021</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州新城山语院租房" class="roomPic" href="https://hz.qk365.com/room/55125" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/CE/CgoKaFxGTyKAXuFnAACQ7z0yOOQ257.jpg" title="临平新城山语院租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="余杭区租房" class="addArea" href="https://hz.qk365.com/list/a54" target="_blank">余杭区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v23494" target="_blank" title="新城山语院租房">新城山语院</a>
                                    </span>
							</div>
							<p>
									<i>
										787</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州新城山语院租房" class="roomPic" href="https://hz.qk365.com/room/55124" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/A7/F3/CgoKaF1CqCiAXLWQAABu7dQckz8946.jpg" title="临平新城山语院租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="余杭区租房" class="addArea" href="https://hz.qk365.com/list/a54" target="_blank">余杭区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v23494" target="_blank" title="新城山语院租房">新城山语院</a>
                                    </span>
							</div>
							<p>
									<i>
										997</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州盛都苑租房" class="roomPic" href="https://hz.qk365.com/room/94877" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/D8/99/CgoKaFyHTYSAACARAABwS5ajmIQ182.jpg" title="义蓬盛都苑租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="萧山区租房" class="addArea" href="https://hz.qk365.com/list/a53" target="_blank">萧山区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v28113" target="_blank" title="盛都苑租房">盛都苑</a>
                                    </span>
							</div>
							<p>
									<i>
										662</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				<li>
						<a title="杭州红联九漾华庭东区租房" class="roomPic" href="https://hz.qk365.com/room/86181" target="_blank">
							<img width="218" height="144" src="https://oss-wuxi.qk365.com/qingkepic/M00/20/F1/CgoKZ12dmzOAYHa6AAB0QcWs9-0989.jpg" title="南苑红联九漾华庭东区租房"
										 alt="杭州租房"
										 onerror="defaultPic(this,'https://hz.qk365.com/','0')">
								<div class="playSmall"><img src="https://hz.qk365.com/images/play02.png"></div>   <!-- 新添播放按钮 -->
							<p>
									<span><img src="https://hz.qk365.com/images/special_price.png?v=20191209" ></span>
								</p>
							<!-- 立减 -->
							</a>
						<div class="roomAddress">
							<div class="address">
								<a title="余杭区租房" class="addArea" href="https://hz.qk365.com/list/a54" target="_blank">余杭区</a>
                                    <span>
                                        <i><img src="https://hz.qk365.com/images/icon_04.png" ></i>
                                        <a href="https://hz.qk365.com/xiaoqu/v26834" target="_blank" title="红联九漾华庭东区租房">红联九漾华庭东区</a>
                                    </span>
							</div>
							<p>
									<i>
										810</i>
									<em>元/月</em>
								</p>
							</div>
					</li>
				</ul>
		</div>
	</div>
	<a class="gor" id="gor0"><img src="https://hz.qk365.com/images/nextSnap.png" alt="杭州租房"></a>
</div>
<form id="roomForm" name="roomForm" method="post"
				action="https://hz.qk365.com/list/">
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
					<a target="_blank" title="杭州绿都四季华庭图"
						href="https://hz.qk365.com/room/78080">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/BB/E2/CgoKZ11RMdGAFbn8AACceiEmSVE682.jpg" 
							alt="杭州绿都四季华庭图" title="杭州绿都四季华庭图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】2号线 曹家桥站 绿都四季华庭 精装白领公寓朝南阳台房出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1999</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="城厢租房" href="https://hz.qk365.com/list/a53-k418">城厢</a>-<a title="绿都四季华庭租房" href="https://hz.qk365.com/xiaoqu/v6025">绿都四季华庭</a>租房 27/33层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>优选</i>
		<i>阳台</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyMember fr">
									<em>VIP价：</em> <span><i>1608</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e2002" title="曹家桥租房">曹家桥</a>
		                   	<span>约1442米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10499922" title="吕才庄租房">吕才…</a>
						 		<span>&nbsp;公交站约319米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州绿都四季华庭图"
						href="https://hz.qk365.com/room/78081">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/BB/E1/CgoKaF1RMdiAP6lcAABuTVqMt1A376.jpg" 
							alt="杭州绿都四季华庭图" title="杭州绿都四季华庭图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】2号线 曹家桥站 绿都四季华庭 精装白领公寓 朝南次卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1792</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="城厢租房" href="https://hz.qk365.com/list/a53-k418">城厢</a>-<a title="绿都四季华庭租房" href="https://hz.qk365.com/xiaoqu/v6025">绿都四季华庭</a>租房 27/33层
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
									<em>特价：</em> <span><i>1021</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e2002" title="曹家桥租房">曹家桥</a>
		                   	<span>约1442米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10499922" title="吕才庄租房">吕才…</a>
						 		<span>&nbsp;公交站约319米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州新城山语院图"
						href="https://hz.qk365.com/room/55124">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A7/F3/CgoKaF1CqCiAXLWQAABu7dQckz8946.jpg" 
							alt="杭州新城山语院图" title="杭州新城山语院图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线  临平站  新城山语院 精装白领公寓朝南主卧带独卫带阳台出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2179</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="临平租房" href="https://hz.qk365.com/list/a54-k407">临平</a>-<a title="新城山语院租房" href="https://hz.qk365.com/xiaoqu/v23494">新城山语院</a>租房 5/6层
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
									<em>特价：</em> <span><i>997</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19027" title="临平租房">临平；</a>
						</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州新城山语院图"
						href="https://hz.qk365.com/room/55125">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/CE/CgoKaFxGTyKAXuFnAACQ7z0yOOQ257.jpg" 
							alt="杭州新城山语院图" title="杭州新城山语院图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】临平 新城山语院 精装白领公寓 朝南卧室带阳台出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1813</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="临平租房" href="https://hz.qk365.com/list/a54-k407">临平</a>-<a title="新城山语院租房" href="https://hz.qk365.com/xiaoqu/v23494">新城山语院</a>租房 5/6层
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
									<em>特价：</em> <span><i>787</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19027" title="临平租房">临平；</a>
						</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州盛都苑图"
						href="https://hz.qk365.com/room/94877">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/D8/99/CgoKaFyHTYSAACARAABwS5ajmIQ182.jpg" 
							alt="杭州盛都苑图" title="杭州盛都苑图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】 义前街129号 盛都苑 精装白领公寓朝南阳台房出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1647</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="盛都苑租房" href="https://hz.qk365.com/xiaoqu/v28113">盛都苑</a>租房 3/6层
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
									<em>特价：</em> <span><i>662</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10181924" title="义蓬路口租房">义蓬路口</a>
						 		<span>&nbsp;公交站约240米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州红联九漾华庭东区图"
						href="https://hz.qk365.com/room/86181">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/20/F1/CgoKZ12dmzOAYHa6AAB0QcWs9-0989.jpg" 
							alt="杭州红联九漾华庭东区图" title="杭州红联九漾华庭东区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】地铁1号线 南苑站 红莲九漾华庭东区 精装白领公寓 朝南主卧出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1830</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="南苑租房" href="https://hz.qk365.com/list/a54-k404">南苑</a>-<a title="红联九漾华庭东区租房" href="https://hz.qk365.com/xiaoqu/v26834">红联九漾华庭东区</a>租房 3/26层
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
									<em>特价：</em> <span><i>810</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19026" title="南苑租房">南苑</a>
		                   	<span>约862米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10437783" title="高铁立交北租房">高铁…</a>
						 		<span>&nbsp;公交站约738米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州三卫家园南苑图"
						href="https://hz.qk365.com/room/103950">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/AA/56/CgoKaFxIhZ2AQHaAAAA4vSZ2z4Q974.jpg" 
							alt="杭州三卫家园南苑图" title="杭州三卫家园南苑图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【江干区】1号线 乔司南站 三卫家园 精装白领公寓 单间出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2060</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="江干区租房" href="https://hz.qk365.com/list/a49">江干区</a>-<a title="九堡租房" href="https://hz.qk365.com/list/a49-k437">九堡</a>-<a title="三卫家园南苑租房" href="https://hz.qk365.com/xiaoqu/v27924">三卫家园南苑</a>租房 10/16层
                                        </span>
							</p>
							<p class="p2">
								<i>优选</i>
		<i>飘窗</i>
		<i>0中介费</i>
<i>立即可租</i>
	</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>907</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19022" title="乔司南租房">乔司南</a>
		                   	<span>约1775米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184113" title="九福路公交站租房">九福…</a>
						 		<span>&nbsp;公交站约655米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州宋都丽郡国际图"
						href="https://hz.qk365.com/room/110370">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/22/80/CgoKZ12e786APYNhAABRu4D2iy0699.jpg" 
							alt="杭州宋都丽郡国际图" title="杭州宋都丽郡国际图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】义蓬中路   宋都丽郡国际    精装白领公寓朝南主卧带独卫阳台出租  配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1788</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="宋都丽郡国际租房" href="https://hz.qk365.com/xiaoqu/v29477">宋都丽郡国际</a>租房 8/33层
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
									<em>特价：</em> <span><i>945</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184489" title="青六村租房">青六村</a>
						 		<span>&nbsp;公交站约581米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州宋都丽郡园图"
						href="https://hz.qk365.com/room/110958">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/22/A0/CgoKZ12e97qAefnIAABdxY75_aQ379.jpg" 
							alt="杭州宋都丽郡园图" title="杭州宋都丽郡园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】萧山开发区 宋都丽郡园 精装白领公寓 朝南主卧阳台房带独卫出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1851</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="宋都丽郡园租房" href="https://hz.qk365.com/xiaoqu/v29921">宋都丽郡园</a>租房 11/18层
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
									<em>特价：</em> <span><i>945</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184489" title="青六村租房">青六村</a>
						 		<span>&nbsp;公交站约581米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州顺丰家园图"
						href="https://hz.qk365.com/room/79707">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/6F/0C/CgoKZ13k3EaAFQPdAAA4vc_O0kY971.jpg" 
							alt="杭州顺丰家园图" title="杭州顺丰家园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】2号线 振宁路站 顺丰家园 精装白领公寓朝南单间出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2157</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="钱江世纪城租房" href="https://hz.qk365.com/list/a53-k416">钱江世纪城</a>-<a title="顺丰家园租房" href="https://hz.qk365.com/xiaoqu/v6059">顺丰家园</a>租房 1/6层
                                        </span>
							</p>
							<p class="p2">
								<i>近地铁</i>
	<i>房东原装</i>
		<i>朝南</i>
		<i>0中介费</i>
</p>
							</div>
						<div class="easyPrivilege" title="首签指定房源，享受特价优惠">
									<em>特价：</em> <span><i>1313</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e2009" title="振宁路租房">振宁路</a>
		                   	<span>约181米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10389522" title="恒泰·御庭园租房">恒泰…</a>
						 		<span>&nbsp;公交站约172米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州宋都丽郡园图"
						href="https://hz.qk365.com/room/110691">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/2E/2A/CgoKZ12pe4CAZbRkAABY07mawAg459.jpg" 
							alt="杭州宋都丽郡园图" title="杭州宋都丽郡园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】萧山开发区 宋都丽郡园 精装白领公寓 朝南主卧阳台房带独卫出租 配备齐全 拎包即住</p>
					</div>
					<em class="fr0923">
						<b>原价:1615</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="宋都丽郡园租房" href="https://hz.qk365.com/xiaoqu/v29921">宋都丽郡园</a>租房 3/30层
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
									<em>特价：</em> <span><i>945</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184489" title="青六村租房">青六村</a>
						 		<span>&nbsp;公交站约581米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州定北家园二区图"
						href="https://hz.qk365.com/room/76390">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9C/79/CgoKZ1xF7uKAY320AAB08GNuf_Q118.jpg" 
							alt="杭州定北家园二区图" title="杭州定北家园二区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【西湖区】转塘 定北家园 精装白领公寓 朝南主卧带阳台出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2189</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="西湖区租房" href="https://hz.qk365.com/list/a51">西湖区</a>-<a title="转塘租房" href="https://hz.qk365.com/list/a51-k505">转塘</a>-<a title="定北家园二区租房" href="https://hz.qk365.com/xiaoqu/v26156">定北家园二区</a>租房 4/11层
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
									<em>特价：</em> <span><i>975</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10721038" title="横桥沈合苑西租房">横桥沈合苑西</a>
						 		<span>&nbsp;公交站约227米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州红联九漾华庭东区图"
						href="https://hz.qk365.com/room/89179">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9E/D0/CgoKaFxGT2iAZhutAAB7D6jw83k946.jpg" 
							alt="杭州红联九漾华庭东区图" title="杭州红联九漾华庭东区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线 南苑站 红联九漾华庭 精装白领公寓 朝南次卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1853</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="南苑租房" href="https://hz.qk365.com/list/a54-k404">南苑</a>-<a title="红联九漾华庭东区租房" href="https://hz.qk365.com/xiaoqu/v26834">红联九漾华庭东区</a>租房 12/17层
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
									<em>特价：</em> <span><i>831</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19026" title="南苑租房">南苑</a>
		                   	<span>约862米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10437783" title="高铁立交北租房">高铁…</a>
						 		<span>&nbsp;公交站约738米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州宋都丽郡国际图"
						href="https://hz.qk365.com/room/108123">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/35/42/CgoKZ12wFo-AebsnAACKRpHGum0091.jpg" 
							alt="杭州宋都丽郡国际图" title="杭州宋都丽郡国际图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】义蓬街道   宋都丽郡园 精装白领公寓朝南阳台房出租   配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1578</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="宋都丽郡国际租房" href="https://hz.qk365.com/xiaoqu/v29477">宋都丽郡国际</a>租房 10/23层
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
									<em>特价：</em> <span><i>752</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184489" title="青六村租房">青六村</a>
						 		<span>&nbsp;公交站约581米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州宋都丽郡国际图"
						href="https://hz.qk365.com/room/108124">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/35/41/CgoKaF2wFomAQzzWAAB2UGf6k7Q627.jpg" 
							alt="杭州宋都丽郡国际图" title="杭州宋都丽郡国际图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】义蓬街道   宋都丽郡园 精装白领公寓朝南主卧带独卫出租   配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1792</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="宋都丽郡国际租房" href="https://hz.qk365.com/xiaoqu/v29477">宋都丽郡国际</a>租房 10/23层
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
									<em>特价：</em> <span><i>919</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184489" title="青六村租房">青六村</a>
						 		<span>&nbsp;公交站约581米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州义蓬名苑图"
						href="https://hz.qk365.com/room/102493">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/85/0C/CgoKaF35vJaAbEsRAABswT0Rzzs372.jpg" 
							alt="杭州义蓬名苑图" title="杭州义蓬名苑图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】 义蓬名苑 精装白领公寓 朝南次卧出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1522</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="义蓬名苑租房" href="https://hz.qk365.com/xiaoqu/v28934">义蓬名苑</a>租房 3/20层
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
									<em>特价：</em> <span><i>770</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10182251" title="益民租房">益民</a>
						 		<span>&nbsp;公交站约572米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州定北家园二区图"
						href="https://hz.qk365.com/room/76387">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9C/79/CgoKaFxF7uaAAzQeAAB0U2BDRnA325.jpg" 
							alt="杭州定北家园二区图" title="杭州定北家园二区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【西湖区】转塘 定北家园 精装白领公寓 朝南次卧带飘窗出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2108</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="西湖区租房" href="https://hz.qk365.com/list/a51">西湖区</a>-<a title="转塘租房" href="https://hz.qk365.com/list/a51-k505">转塘</a>-<a title="定北家园二区租房" href="https://hz.qk365.com/xiaoqu/v26156">定北家园二区</a>租房 4/11层
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
									<em>特价：</em> <span><i>1004</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10721038" title="横桥沈合苑西租房">横桥沈合苑西</a>
						 		<span>&nbsp;公交站约227米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州宋都丽郡园图"
						href="https://hz.qk365.com/room/108152">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/56/2F/CgoKaF0B52CATVytAABcaRralBw361.jpg" 
							alt="杭州宋都丽郡园图" title="杭州宋都丽郡园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】萧山开发区 宋都丽郡园 精装白领公寓 朝南主卧阳台房带独卫出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:1815</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="义蓬租房" href="https://hz.qk365.com/list/a53-k5649">义蓬</a>-<a title="宋都丽郡园租房" href="https://hz.qk365.com/xiaoqu/v29921">宋都丽郡园</a>租房 2/18层
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
									<em>特价：</em> <span><i>945</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10184489" title="青六村租房">青六村</a>
						 		<span>&nbsp;公交站约581米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州迎春南苑图"
						href="https://hz.qk365.com/room/56192">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/3B/1C/CgoKaFzo3KaAG344AABz6YEyHaE261.jpg" 
							alt="杭州迎春南苑图" title="杭州迎春南苑图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【滨江区】地铁1号线 江陵路站 迎春南苑 精装白领公寓 朝南主卧带飘窗出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:3193</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="滨江区租房" href="https://hz.qk365.com/list/a52">滨江区</a>-<a title="西兴租房" href="https://hz.qk365.com/list/a52-k551">西兴</a>-<a title="迎春南苑租房" href="https://hz.qk365.com/xiaoqu/v6051">迎春南苑</a>租房 11/11层
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
									<em>VIP价：</em> <span><i>2325</i>元/月起</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e1904" title="滨和路租房">滨和路</a>
		                   	<span>约663米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180469" title="迎春小区租房">迎春…</a>
						 		<span>&nbsp;公交站约329米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州丰润家园图"
						href="https://hz.qk365.com/room/91851">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/A0/3A/CgoKZ1xGlTSAH_KfAABs9B5IJw8332.jpg" 
							alt="杭州丰润家园图" title="杭州丰润家园图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【萧山区】2号线 人民广场站 丰润家园 精装白领公寓朝南单间出租 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2567</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="萧山区租房" href="https://hz.qk365.com/list/a53">萧山区</a>-<a title="北干租房" href="https://hz.qk365.com/list/a53-k419">北干</a>-<a title="丰润家园租房" href="https://hz.qk365.com/xiaoqu/v24756">丰润家园</a>租房 2/20层
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
									<em>特价：</em> <span><i>1397</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s20" title="2号线租房">2号线</a>
		                   	<a href="https://hz.qk365.com/list/s20-e2007" title="建设一路租房">建设一路</a>
		                   	<span>约1258米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10635085" title="博学路金鸡路口租房">博学…</a>
						 		<span>&nbsp;公交站约95米</span>
					 		</a>
					</div>
					</div>
				</li>
				<li>
					<a target="_blank" title="杭州胜稼红星嘉园一区图"
						href="https://hz.qk365.com/room/77542">
							<img src="https://oss-wuxi.qk365.com/qingkepic/M00/9C/B1/CgoKaFxF9s6AZUvpAABpkTHGQBQ850.jpg" 
							alt="杭州胜稼红星嘉园一区图" title="杭州胜稼红星嘉园一区图"
							onerror="this.src='https://hz.qk365.com/images/noPic_Big0.jpg'"/>
						<div class="play"><img src="https://hz.qk365.com/images/play01.png" ></div>   <!-- 新添播放按钮 -->
						</a>
					
					<div class="coverBox">
					<p class="easySub  clearfix">【余杭区】1号线 乔司南站 胜稼红星嘉园一区 精装白领公寓朝南主卧带阳台 配备齐全</p>
					</div>
					<em class="fr0923">
						<b>原价:2269</b> 元/月
					</em>
					<div class="easyCon ">
						<div class="clearfix">
							<div class="easyEq fl">
							<p>
								<span class="placeText fl" style="font-size: 12px;">
                                    <a title="余杭区租房" href="https://hz.qk365.com/list/a54">余杭区</a>-<a title="乔司租房" href="https://hz.qk365.com/list/a54-k402">乔司</a>-<a title="胜稼红星嘉园一区租房" href="https://hz.qk365.com/xiaoqu/v24595">胜稼红星嘉园一区</a>租房 4/15层
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
									<em>特价：</em> <span><i>1166</i>元/月</span>
								</div>
							</div>
					<div class="easyBottomInfo">
						<!-- 地铁 -->
						<a class="metroText fl">
						<span>距&nbsp;</span><a href="https://hz.qk365.com/list/s19" title="1号线租房">1号线</a>
		                   	<a href="https://hz.qk365.com/list/s19-e19022" title="乔司南租房">乔司南</a>
		                   	<span>约933米；</span>
						<span>距&nbsp;</span><a href="https://hz.qk365.com/bus/10180839" title="三卫村租房">三卫…</a>
						 		<span>&nbsp;公交站约174米</span>
					 		</a>
					</div>
					</div>
				</li>
				</ul>
		</div>
		<p class="easyPage">
  <a href="https://hz.qk365.com/list/" onclick="javascript:void(0);return false;" class="prePage">&nbsp;</a>
    <a href="https://hz.qk365.com/list/" onclick="javascript:void(0);return false;" class="active">1</a>
        <a href="https://hz.qk365.com/list/p2" onclick="javascript:simpleTable.togglePage(2);return false;">2</a>
          <a href="https://hz.qk365.com/list/p3" onclick="javascript:simpleTable.togglePage(3);return false;">3</a>
          <a href="https://hz.qk365.com/list/p4" onclick="javascript:simpleTable.togglePage(4);return false;">4</a>
          <a href="https://hz.qk365.com/list/p5" onclick="javascript:simpleTable.togglePage(5);return false;">5</a>
          <a href="https://hz.qk365.com/list/p6" onclick="javascript:simpleTable.togglePage(6);return false;">6</a>
          <a href="https://hz.qk365.com/list/p7" onclick="javascript:simpleTable.togglePage(7);return false;">7</a>
          <a class="nextPage" href="https://hz.qk365.com/list/p2" onclick="javascript:simpleTable.togglePage(2);return false;">&nbsp;</a>
      </p>
</div>
<div id="sidebarRig">
	<ul>
		<li>
			<span class="sidebarBox">
                <div class="sideFadeIn">
                    <div id="SideBox01">
                        <div class="tit">
                            <img src="https://hz.qk365.com/images/index/sidebar1.png" />
                            <h3>关注青客</h3>
                        </div>
                        <div class="scan scan0">
                            <p><img src="https://hz.qk365.com/images/Side/wxImg02.png" /></p>
                            <p>扫描二维码</p>
                            <p>下载APP</p>
                        </div>
                    </div>
                </div>
                <img src="https://hz.qk365.com/images/index/sidebar1.png" width="53" height="45" class="sideFadeOut" />
            </span>
        </li>
        <li>
            <span class="sidebarBox">
                <div class="sideFadeIn">
                    <div id="SideBox02">
                        <a class="tit" href="https://hz.qk365.com/fwtg" target="_blank">
                            <img src="https://hz.qk365.com/images/index/sidebar2.png" />
                            <h3>房屋托管</h3>
                        </a>
                    </div>
                </div>
                <img src="https://hz.qk365.com/images/index/sidebar2.png" width="53" height="45" class="sideFadeOut" />
            </span>
        </li>
        <li>
            <span class="sidebarBox">
                <div>
                    <div id="SideBox03">
                        <a class="tit" target="_blank" href="javascript:;" onclick="onKST();">
                            <img src="https://hz.qk365.com/images/index/sidebar3.png" />
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
                            <span><img src="https://hz.qk365.com/images/index/sidebar4.png" /></span>
                            <h3>租客需求</h3>
                        </div>
                        <div class="text">
                            <textarea name="mydiyue" id="mydiyue" onclick="changeShowList(this)">求租火车站附近房源</textarea>
                        </div>
                        <div class="submit">
                            <form id="mail">
                                <input type="submit" onclick="diyue_center('https://hz.qk365.com/security/subscribe.do');" value="确认" />
                            </form>
                        </div>
                    </div>
                </div>
                <img src="https://hz.qk365.com/images/index/sidebar4.png"  class="sideFadeOut" />
            </span>
        </li>
        <li id="sidebarTop">
            <span class="sidebarBox" id="top_btn">
                <div class="sideFadeIn" >
                    <img src="https://hz.qk365.com/images/index/top-arrow2.png"/>
                    <h3>TOP</h3>
                </div>
                <img src="https://hz.qk365.com/images/index/top-arrow2.png"  class="sideFadeOut" />
            </span>
        </li>
    </ul>
</div><script type="text/javascript"
		src="https://hz.qk365.com/js/jquery-1.11.0.min.js"></script>
	<script type="text/javascript"
		src="https://hz.qk365.com/js/homepage/autoFill.js"></script>
	<script type="text/javascript"
		src="https://hz.qk365.com/js/homepage/homepage.js?version=20171102"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/public/public.js?v=20181025"></script>
	<script src="https://hz.qk365.com/js/require.js"
		data-main="https://hz.qk365.com/js/main.js?version=20171024"></script>
	<script src="https://hz.qk365.com/js/public/sc.js?v=20170808"></script>
	<script type="text/javascript">
	var titleindex = '1';
	if(titleindex==''){
		titleindex = 0;
	}
	$(document).ready(function(){
		$("#titleindex"+titleindex).addClass("active");
	});
		var basePathUrl = 'https://hz.qk365.com/';
	</script>
	<script type="text/javascript" src="https://hz.qk365.com/widgets/simpletable/simpletable.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/roomdetail/findrooms.js?v=20190524"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/common/urlMatch.js?v=20190524"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/js/recomBox.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/common/topanv.js?version=20170808"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/hide-box.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/activityViewCount.js"></script>
	<script type="text/javascript" src="https://hz.qk365.com/js/houseView360.js?v=20171225"></script>
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
	<script type="text/javascript" src="https://hz.qk365.com/js/activityLabel.js"></script>
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
                    <li>杭州热门区县租房<i></i></li>
						<li>杭州热门小区租房<i></i></li>
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
                    	<a title="市辖租房" href="https://hz.qk365.com/list/a45" target="_blank"> 市辖租房</a>
								
									|
								<a title="建德租房" href="https://hz.qk365.com/list/a57" target="_blank"> 建德租房</a>
								
									|
								<a title="滨江租房" href="https://hz.qk365.com/list/a52" target="_blank"> 滨江租房</a>
								
									|
								<a title="上城租房" href="https://hz.qk365.com/list/a47" target="_blank"> 上城租房</a>
								
									|
								<a title="富阳租房" href="https://hz.qk365.com/list/a58" target="_blank"> 富阳租房</a>
								
									|
								<a title="萧山租房" href="https://hz.qk365.com/list/a53" target="_blank"> 萧山租房</a>
								
									|
								<a title="下城租房" href="https://hz.qk365.com/list/a48" target="_blank"> 下城租房</a>
								
									|
								<a title="临安租房" href="https://hz.qk365.com/list/a59" target="_blank"> 临安租房</a>
								
									|
								<a title="余杭租房" href="https://hz.qk365.com/list/a54" target="_blank"> 余杭租房</a>
								
									|
								<a title="江干租房" href="https://hz.qk365.com/list/a49" target="_blank"> 江干租房</a>
								
									|
								<a title="桐庐租房" href="https://hz.qk365.com/list/a55" target="_blank"> 桐庐租房</a>
								
									|
								<a title="拱墅租房" href="https://hz.qk365.com/list/a50" target="_blank"> 拱墅租房</a>
								
									|
								<a title="淳安租房" href="https://hz.qk365.com/list/a56" target="_blank"> 淳安租房</a>
								
									|
								<a title="西湖租房" href="https://hz.qk365.com/list/a51" target="_blank"> 西湖租房</a>
								</div>
                </div>
                <div class="tabBox2">
                    <div class="fotLink">
                    	<a title="融创东南海" href="https://hz.qk365.com/xiaoqu/v27581" target="_blank">融创东南海</a>
								
								 |
								<a title="红联九漾华庭西区" href="https://hz.qk365.com/xiaoqu/v26833" target="_blank">红联九漾华庭西区</a>
								
								 |
								<a title="红联九漾华庭东区" href="https://hz.qk365.com/xiaoqu/v26834" target="_blank">红联九漾华庭东区</a>
								
								 |
								<a title="三卫家园北苑" href="https://hz.qk365.com/xiaoqu/v27123" target="_blank">三卫家园北苑</a>
								
								 |
								<a title="城发云锦城" href="https://hz.qk365.com/xiaoqu/v27471" target="_blank">城发云锦城</a>
								
								 |
								<a title="得力名望府" href="https://hz.qk365.com/xiaoqu/v23993" target="_blank">得力名望府</a>
								
								 |
								<a title="绿都御景蓝湾" href="https://hz.qk365.com/xiaoqu/v6345" target="_blank">绿都御景蓝湾</a>
								
								 |
								<a title="朝阳逸景苑" href="https://hz.qk365.com/xiaoqu/v6683" target="_blank">朝阳逸景苑</a>
								
								 |
								<a title="新城红郡" href="https://hz.qk365.com/xiaoqu/v24140" target="_blank">新城红郡</a>
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
							<a href="https://hz.qk365.com/list" target="_blank">房屋出租</a>
								
									|
								<a href="https://hz.qk365.com/list" target="_blank">出租信息</a>
								
									|
								<a href="https://hz.qk365.com/qkkx/index.html" target="_blank">青客快讯</a>
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
								<a title="青客公司简介" href="https://hz.qk365.com/qkkx/about/2018/1.html?gsjj" rel="nofollow">公司简介</a>
								<a title="青客杭州网站地图" href="https://hz.qk365.com/qkkx/about/2018/5.html?wzdh">网站地图</a>
				                <a title="联系青客杭州租房" href="https://hz.qk365.com/qkkx/about/2018/3.html?lxwm" rel="nofollow">联系我们</a>
								<a title="加入青客" href="https://hz.qk365.com/qkkx/about/2018/2.html?qkzp" rel="nofollow">加入我们</a>
								<a title="杭州租房小区专题" href="https://hz.qk365.com/xiaoqu/xqjh">小区专题</a>
								<a title="隐私政策" href="https://hz.qk365.com/qkkx/about/2019/7628049.html?yszc">隐私政策</a>
								</li>
                            <li>
                                <p>新手指南</p>
                                <a title="青客杭州租房注册方式" href="https://hz.qk365.com/qkkx/service/2018/8.html?zcfs" target="_blank" rel="nofollow">注册方式</a>
								<a title="青客杭州租房租房流程" href="https://hz.qk365.com/qkkx/service/2018/10.html?zflc" target="_blank" rel="nofollow">租房流程</a>
<a title="青客杭州租房在线报修" href="https://hz.qk365.com/qkkx/service/2018/13.html?zxbx" target="_blank" rel="nofollow">在线报修</a>
                            </li>
                            <li>
                                <p>租期服务</p>
                                <a title="青客杭州租房400服务" href="https://hz.qk365.com/qkkx/service/2018/21.html?400fw" target="_blank" rel="nofollow">400服务</a>
								<a title="青客杭州租房保洁服务" href="https://hz.qk365.com/qkkx/service/2018/22.html?bjfw" target="_blank" rel="nofollow">保洁服务</a>
								<a title="青客杭州租房维修服务" href="https://hz.qk365.com/qkkx/service/2018/23.html?wxfw" target="_blank" rel="nofollow">维修服务</a>
								<a title="青客杭州租房宽带服务" href="https://hz.qk365.com/qkkx/service/2018/24.html?kdfw" target="_blank" rel="nofollow">宽带服务</a>
                            </li>
                            <li>
                                <p>会员专区</p>
                                <a title="青客杭州租房会员介绍" href="https://hz.qk365.com/qkkx/service/2018/34.html?hyjs" target="_blank" rel="nofollow">会员介绍</a>
								<a title="青客杭州租房会员积分" href="https://hz.qk365.com/qkkx/service/2018/40.html?hyjf" target="_blank" rel="nofollow">会员积分</a>
								<a title="青客杭州租房门店支付" href="https://hz.qk365.com/qkkx/service/2018/33.html?mdzf" target="_blank" rel="nofollow">门店支付</a>
								<a title="青客杭州租房ATM支付" href="https://hz.qk365.com/qkkx/service/2018/36.html?atmzf" target="_blank" rel="nofollow">ATM支付</a>
								<a title="青客杭州租房APP支付" href="https://hz.qk365.com/qkkx/service/2018/37.html?appzf" target="_blank" rel="nofollow">APP支付</a>
                            </li>
                        </ul>
                    </div>
                    <div class="QcoL5 fL">
                        <ul class="serviceR clearfix">
                           <li>
                               <img class="sicon" src="https://hz.qk365.com/images/2019-11-29-img/applet-qkgy.png"></img>
                               <img class="sicon1" src="https://hz.qk365.com/images/2019-11-29-img/applet-qkgyClick.png"></img>
                               <div class="scode"><img src="https://hz.qk365.com/images/index/code-qkgy.jpg" alt="青客公寓APP"></div>
                               <p>青客公寓APP</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://hz.qk365.com/images/2019-11-29-img/applet-qkfw.png"></img>
                               <img class="sicon1" src="https://hz.qk365.com/images/2019-11-29-img/applet-qkfwClick.png"></img>
                               <div class="scode"><img src="https://hz.qk365.com/images/index/code-qkfw.jpg?v=20191225" alt="青客服务号"></div>
                               <p>青客服务号</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://hz.qk365.com/images/2019-11-29-img/applet-qkzf.png"></img>
                               <img class="sicon1" src="https://hz.qk365.com/images/2019-11-29-img/applet-qkzfClick.png"></img>
                               <div class="scode"><img src="https://hz.qk365.com/images/index/code-qkzf.jpg?v=20191225" alt="青客找房小程序"></div>
                               <p>青客找房小程序</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://hz.qk365.com/images/2019-11-29-img/applet-zfb.png"></img>
                               <img class="sicon1" src="https://hz.qk365.com/images/2019-11-29-img/applet-zfbClick.png"></img>
                               <div class="scode"><img src="https://hz.qk365.com/images/index/code-zfb.jpg?v=20191225" alt="支付宝小程序"></div>
                               <p>支付宝小程序</p>
                           </li> 
                           <li>
                               <img class="sicon" src="https://hz.qk365.com/images/2019-11-29-img/applet-bd.png"></img>
                               <img class="sicon1" src="https://hz.qk365.com/images/2019-11-29-img/applet-bdClick.png"></img>
                               <div class="scode"><img src="https://hz.qk365.com/images/index/code-bd.jpg" alt="百度小程序"></div>
                               <p>百度小程序</p>
                           </li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <p class="description">青客<a href="https://hz.qk365.com/" title="杭州租房网">杭州租房网</a>提供优质<a href="https://hz.qk365.com/list" title="房屋出租">房屋出租</a>信息，海量直租房、经纪人租房信息，帮您轻松在杭州<a href="https://hz.qk365.com/" title="租房">租房</a>。包括<a href="https://hz.qk365.com/" title="白领公寓">白领公寓</a>、<a href="https://hz.qk365.com/" title="合租公寓">合租公寓</a>、<a href="https://hz.qk365.com/" title="单身公寓">单身公寓</a>、
						<a href="https://hz.qk365.com/" title="时尚租房">时尚租房</a>、<a href="https://hz.qk365.com/" title="杭州合租">杭州合租</a>等信息，您还可以选择青客
						<a href="https://i.qk365.com/hz" title="杭州租房移动端">杭州租房移动端</a>，更方便、更快捷。</p>
            	<div class="alphabet">
            	<div>
					<p class="alphabet-tit">商圈索引：</p>
                    <ul class="alphabet-tabs">
                    	<li class="selected">B</li>
                    	<li >C</li>
                    	<li >D</li>
                    	<li >G</li>
                    	<li >H</li>
                    	<li >J</li>
                    	<li >L</li>
                    	<li >M</li>
                    	<li >N</li>
                    	<li >P</li>
                    	<li >Q</li>
                    	<li >R</li>
                    	<li >S</li>
                    	<li >W</li>
                    	<li >X</li>
                    	<li >Y</li>
                    	<li >Z</li>
                    	</ul>
				</div>
                <ul class="alphabet-item">
                	<li style="display: list-item;">
                			<a href="https://hz.qk365.com/list/a49-k445" title="白杨租房">白杨租房</a>
                			<a href="https://hz.qk365.com/list/a50-k546" title="半山租房">半山租房</a>
                			<a href="https://hz.qk365.com/list/a53-k419" title="北干租房">北干租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a49-k443" title="城东新城租房">城东新城租房</a>
                			<a href="https://hz.qk365.com/list/a52-k547" title="长河租房">长河租房</a>
                			<a href="https://hz.qk365.com/list/a53-k418" title="城厢租房">城厢租房</a>
                			<a href="https://hz.qk365.com/list/a54-k397" title="仓前租房">仓前租房</a>
                			<a href="https://hz.qk365.com/list/a54-k410" title="崇贤租房">崇贤租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a49-k442" title="丁桥租房">丁桥租房</a>
                			<a href="https://hz.qk365.com/list/a50-k544" title="大关租房">大关租房</a>
                			<a href="https://hz.qk365.com/list/a53-k5650" title="大江东租房">大江东租房</a>
                			<a href="https://hz.qk365.com/list/a54-k409" title="东湖租房">东湖租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a50-k528" title="拱墅周边租房">拱墅周边租房</a>
                			<a href="https://hz.qk365.com/list/a51-k522" title="古墩路租房">古墩路租房</a>
                			<a href="https://hz.qk365.com/list/a54-k408" title="勾庄租房">勾庄租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a49-k424" title="火车东站租房">火车东站租房</a>
                			<a href="https://hz.qk365.com/list/a49-k440" title="海天城租房">海天城租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a49-k436" title="金沙湖租房">金沙湖租房</a>
                			<a href="https://hz.qk365.com/list/a49-k437" title="九堡租房">九堡租房</a>
                			<a href="https://hz.qk365.com/list/a49-k438" title="景芳租房">景芳租房</a>
                			<a href="https://hz.qk365.com/list/a51-k520" title="蒋村租房">蒋村租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a54-k405" title="良渚租房">良渚租房</a>
                			<a href="https://hz.qk365.com/list/a54-k406" title="老余杭租房">老余杭租房</a>
                			<a href="https://hz.qk365.com/list/a54-k407" title="临平租房">临平租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a50-k536" title="莫干山路租房">莫干山路租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a53-k417" title="宁围街道租房">宁围街道租房</a>
                			<a href="https://hz.qk365.com/list/a54-k404" title="南苑租房">南苑租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a49-k434" title="彭埠租房">彭埠租房</a>
                			<a href="https://hz.qk365.com/list/a52-k550" title="浦沿租房">浦沿租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a52-k554" title="区政府租房">区政府租房</a>
                			<a href="https://hz.qk365.com/list/a53-k416" title="钱江世纪城租房">钱江世纪城租房</a>
                			<a href="https://hz.qk365.com/list/a54-k402" title="乔司租房">乔司租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a54-k401" title="仁和租房">仁和租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a48-k461" title="石桥租房">石桥租房</a>
                			<a href="https://hz.qk365.com/list/a50-k534" title="石祥路租房">石祥路租房</a>
                			<a href="https://hz.qk365.com/list/a51-k515" title="三墩租房">三墩租房</a>
                			<a href="https://hz.qk365.com/list/a51-k516" title="申花租房">申花租房</a>
                			<a href="https://hz.qk365.com/list/a53-k415" title="蜀山租房">蜀山租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a53-k414" title="闻堰租房">闻堰租房</a>
                			<a href="https://hz.qk365.com/list/a54-k395" title="未来科技城租房">未来科技城租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a49-k426" title="下沙沿江租房">下沙沿江租房</a>
                			<a href="https://hz.qk365.com/list/a49-k427" title="下沙租房">下沙租房</a>
                			<a href="https://hz.qk365.com/list/a50-k531" title="祥符租房">祥符租房</a>
                			<a href="https://hz.qk365.com/list/a50-k533" title="小河租房">小河租房</a>
                			<a href="https://hz.qk365.com/list/a52-k551" title="西兴租房">西兴租房</a>
                			<a href="https://hz.qk365.com/list/a53-k392" title="萧山开发区租房">萧山开发区租房</a>
                			<a href="https://hz.qk365.com/list/a53-k411" title="萧山周边租房">萧山周边租房</a>
                			<a href="https://hz.qk365.com/list/a53-k412" title="湘湖租房">湘湖租房</a>
                			<a href="https://hz.qk365.com/list/a53-k413" title="新塘租房">新塘租房</a>
                			<a href="https://hz.qk365.com/list/a53-k5713" title="新街租房">新街租房</a>
                			<a href="https://hz.qk365.com/list/a54-k398" title="闲林租房">闲林租房</a>
                			<a href="https://hz.qk365.com/list/a54-k399" title="星桥租房">星桥租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a53-k5649" title="义蓬租房">义蓬租房</a>
                			<a href="https://hz.qk365.com/list/a54-k394" title="余杭周边租房">余杭周边租房</a>
                			<a href="https://hz.qk365.com/list/a58-k5648" title="银湖租房">银湖租房</a>
                			</li>
                	<li >
                			<a href="https://hz.qk365.com/list/a51-k505" title="转塘租房">转塘租房</a>
                			<a href="https://hz.qk365.com/list/a52-k552" title="中兴租房">中兴租房</a>
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
		<img src="https://hz.qk365.com/images/beian.png" style="float:left;"/><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">沪公网安备 31011402005354号</p>
		</a>
	</div>
</div>

<!-- cnzz Begin -->
<div style="display: none"><script type="text/javascript" src="https://s22.cnzz.com/z_stat.php?id=1000353613&web_id=1000353613"></script></div>
<!-- cnzz End -->
<link href="https://hz.qk365.com/css/alert.css?v=20200824" rel="stylesheet" type="text/css" />
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
<script type="text/javascript" src="https://hz.qk365.com/js/onKST.js"></script>

<script type="text/javascript" src="https://hz.qk365.com/js/pageViewCount.js?version=20180820"></script>
<script type="text/javascript" src="https://hz.qk365.com/js/alert.js?v=20191115"></script></body>
</html>


Process finished with exit code 0

'''
# print(html)
html_doc = etree.HTML(html)
# price_list = html_doc.xpath("//div[@class='clearfix']/div/span/i/text()")
# print(price_list)
#
# pos_list = html_doc.xpath("//div[@class='clearfix']/div/p/span/a/text()")
lable = html_doc.xpath("//ul[@class='easyList']/li")

for i in lable:
    # todo 提取原价
    print(''.join(i.xpath(".//b/text()")))
    # todo 提取价格
    print(''.join(i.xpath(".//span/i/text()")))
    # todo 提取位置
    print(''.join(i.xpath(".//span/a/text()")))
    # todo 提取标签
    print('-'.join(i.xpath(".//p/i/text()")))
    # todo 提取链接
    print(''.join(i.xpath("./a/@href")))






