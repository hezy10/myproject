# coding=utf-8
import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '85.0.4183.83 Safari/537.36'
}
txt = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/链家.py"
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Content-language" content="zh-CN" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="applicable-device" content="pc">
  <meta http-equiv="Cache-Control" content="no-transform " />

  <!-- seo关键字相关信息 -->
  <meta name="description" content="贝壳杭州租房网,提供真实的杭州租房信息、出租房源信息、租房价格,包括杭州整租、合租、公寓出租等信息,以及杭州房屋出租个人信息、经纪人信息、品牌公寓信息等.找租房房源,就来杭州贝壳租房!">
  <meta name="keywords" content="杭州租房信息,杭州出租房网,杭州房屋出租价格">
  <title>杭州租房信息_杭州出租房源|房屋出租价格【杭州贝壳租房】</title>



  <!--地址信息-->
  <meta name="location" content="province=浙江;city=杭州">

  <!-- 网站ico图标 -->
    <link href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/lianjia/favicon.ico?_v=20200917160625398" type="image/x-icon" rel="icon">

    <meta name=""mobile-agent content="format=[wml|xhtml|html5];url=https://m.ke.com/chuzu/hz/zufang/" />
  <link rel="alternate" media="only screen and (max-width:640px)" href="https://m.ke.com/chuzu/hz/zufang/">

    <!-- 是否需要加载common.css -->
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/css/common.css?_v=20200917160625398">

  <!-- 载入灯塔 -->
  <!-- 接入灯塔 -->
<script src='//s1.ljcdn.com/link-static/resource/plat_framework/fee/js/1.4.0/index.js' crossorigin="anonymous"></script>
<script>
  // 获取cookie信息
  function getCookie(name){
    var cookies=document.cookie.split('; ');
    for(var i=0;i<cookies.length;i++){
      var crumb=cookies[i].split('=');
      if(name===crumb[0]){
        return crumb[1]
      }
    }
    return ''
  }
  // 灯塔加载完成后的回调函数
  ;;(function DT(){
    var uuid=getCookie('lianjia_uuid')
    window.dt && dt.set({
      pid: 'rent_fe_pc', // [必填]项目id, 由灯塔项目组统一分配
      uuid: uuid,
      ucid: uuid, // [可选]用户ucid, 用于发生异常时追踪用户信息, 一般在cookie中可以取到, 没有可传空字符串
      is_test: Boolean(''), // 是否为测试数据, 默认为false(测试模式下打点数据仅供浏览, 不会展示在系统中)
      record: {
        time_on_page: true, // 是否监控用户在线时长数据, 默认为true
        performance: true, // 是否监控页面载入性能, 默认为true
        js_error: true, //  是否监控页面报错信息, 默认为true
        // 配置需要监控的页面报错类别, 仅在js_error为true时生效, 默认均为true(可以将配置改为false, 以屏蔽不需要上报的错误类别)
        js_error_report_config: {
          ERROR_RUNTIME: true, // js运行时报错
          ERROR_SCRIPT: true, // js资源加载失败
          ERROR_STYLE: true, // css资源加载失败
          ERROR_IMAGE: false, // 图片资源加载失败
          ERROR_AUDIO: true, // 音频资源加载失败
          ERROR_VIDEO: true, // 视频资源加载失败
          ERROR_CONSOLE: false, // vue运行时报错
          ERROR_TRY_CATCH: true,
          checkErrorNeedReport: function(desc, stack){
            // 外网内容不上报
            if (!/\/\/(s1\.ljcdn\.com\/)/.test(desc) && !/\/\/(s1\.ljcdn\.com\/)/.test(stack)) {
              return false;
            }

            // 是否上报错误，默认为上报
            var needReport = true

            // 报错是否是从IMSDK中报出的
            var isThrowFromIM = (desc.indexOf('web-im-sdk') > -1)

            // desc 命中以下关键字的其中一个，即过滤掉，不上报错误，注： 从从IMSDK中报出的（第一类）
            var filterStr = ['未登录', '/msg/sync ajax fail', '登录令牌缺失', 'Session服务出错']

            // desc 命中以下关键字的其中一个，即可过滤掉，不上报信息，注： 并不是从从IMSDK中报出的（第二类）
            var filterStr2 = ['MyAppGetHTMLElementsAtPoint', 'vivoNewsDetailPage', 'Script error']

            //是否在desc中命中了关键字符串
            var hitKeyStr = false // 第一类
            var hitKeyStr2 = false // 第二类

            var i = 0, len = filterStr.length;
            for(; i < len; i++){
              if(desc.indexOf(filterStr[i]) > -1){
                hitKeyStr = true
                break
              }
            }

            var j = 0, len2 = filterStr2.length;
            for(; j < len2; j++){
              if(desc.indexOf(filterStr2[j]) > -1){
                hitKeyStr2 = true
                break
              }
            }

            // 错误是从IM中抛出，并且错误信息包含登录等内容时,或者命中第二类关键词，过滤掉，不上报
            if((isThrowFromIM && hitKeyStr) || hitKeyStr2){
              needReport = false
            }

            return needReport
          }
        }
      },
      version: '1.0.0',
      getPageType: function (location) {
        return location.host + location.pathname
      }
    })
  })()
</script>

    <!-- 载入后台返回的css文件 -->
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/page/list/index.css?_v=20200917160625398">

      <!-- 载入链家相关皮肤 -->
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/css/lianjia.css?_v=20200917160625398">

  <!-- 预置全局变量 -->
  <script>
    var g_conf = {}
  </script>
</head>

<body>

  <!-- 载入低版本浏览器样式 -->
  <style>
  .browser__low{height:100%;overflow:hidden}.browser__low--wrapper,.browser__low--inner{display:none}.browser__low .browser__low--wrapper{position:absolute;left:0;right:0;top:0;bottom:0;z-index:199999;background:#000;opacity:.5;filter:alpha(opacity=50);display:block}.browser__low .browser__low--inner{background:#fff;position:absolute;left:50%;top:50%;z-index:19999999;width:360px;height:100px;margin-top:-90px;margin-left:-200px;padding:40px 20px;display:block}.browser__low .browser__low--inner p{font-size:20px;padding-bottom:40px}.browser__low .browser__low--inner a{display:inline-block;color:#fff;background:#2ab78e;padding:10px 6px}

</style>
<div class="browser__low--wrapper"></div>
<div class="browser__low--inner">
  <p>您的浏览器版本过低，请升级：</p>
  <a href="https://www.baidu.com/s?wd=chrome" target="_blank">谷歌 Chrome浏览器</a>
</div>
<script>
;;(function() {
  if(!([].forEach)) {
    document.body.className += ' browser__low'
  }
})()
</script>


  <div class="wrapper">
     <link href='//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' property='stylesheet' rel="stylesheet">

<div>
  <!-- 顶部总站导航 -->
  <div class="header ">
  <ul class="header__wrapper w1150 clear typeUserInfo" id="top">
                      <li class="header__item fl" >
          <a href="//hz.lianjia.com" target="_blank">首页</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/ershoufang/" target="_blank">二手房</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.fang.lianjia.com/loupan/" target="_blank">新房</a>
        </li>
                        <li class="header__item fl cur" >
          <a href="/zufang/" target="_blank">租房</a>
        </li>
                        <li class="header__item fl" >
          <a href="//us.lianjia.com" target="_blank">海外</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/xiaoqu/" target="_blank">小区</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/jingjiren/" target="_blank">经纪人</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/wenda/" target="_blank">指南</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/fangjia/" target="_blank">房价</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/tool.html" target="_blank">工具</a>
        </li>
                        <li class="header__item fl publish-house" data-event_id="20383">
          <a href="//hz.lianjia.com/yezhu/" target="_blank">发布房源</a>
        </li>
                  <li class="header__aside fr pointer typeShowUser" data-el="login" data-event_id="10794" data-event_action="target=login">
      <span data-el="login_box">
        <span data-el="btn_login" data-id="dialog_tel" class="btn-login">登录</span>/<span class="btn-resgiter" data-el="register" data-id="dialog_reg">注册</span>
      </span>
    </li>
    <li class="top__aside fr hide" data-el="user_box">
      <a href="" data-el="userName">18****87</a>
      <a data-el="logout_btn">退出</a>
      <div class="menu-pop">
        <i class="allow"></i>
        <ul class="menu-list lj">
          <li class="menu-item"><a href="/zufang/users/index?cur_type=attention" target="_blank">我的关注</a></li>
          <li class="menu-item"><a href="/zufang/users/index?cur_type=contact" target="_blank">最近联系</a></li>
          <li class="menu-item"><a href="/zufang/users/index?cur_type=scan" target="_blank">浏览记录</a></li>
        </ul>
      </div>
    </li>

  </ul>

</div>

  <div class="search__area">
    <!-- 租房导航 -->
  <div class="beike__nav">
  <a class="beike__nav--logo" href="/zufang/"></a>


  <ul class="beike__nav--tab">
    <li>
      <a 
        class="cur" 
        href="/zufang/" 
        data-event_id="25754" 
        exposure-event_id="25753" 
        exposure-event_action="click_name=首页" 
        data-event_action="click_name=首页" 
        data-event_position="click_name"
        exposure-event_position="click_name">首页</a>
    </li>

    <li>
      <a 
      class="" 
      href="/zufang/rt200600000001/" 
      data-event_id="25754" 
      exposure-event_id="25753" 
      exposure-event_action="click_name=整租" 
      data-event_action="click_name=整租" 
      data-event_position="click_name"
      exposure-event_position="click_name">整租</a>
    </li>

    <li>
      <a 
      class="" 
      href="/zufang/rt200600000002/" 
      data-event_id="25754" 
      exposure-event_id="25753" 
      exposure-event_action="click_name=合租" 
      data-event_action="click_name=合租" 
      data-event_position="click_name"
      exposure-event_position="click_name">合租</a></li>

    <li>
      <a 
      href="/zufang/proprietor/offer?city_id=330100&city_name=杭州&position=rent_pc_toptbar_rent" 
      data-event_id="25754" 
      exposure-event_id="25753" 
      exposure-event_action="click_name=发布房源" 
      data-event_action="click_name=发布房源" 
      data-event_position="click_name"
      exposure-event_position="click_name">发布房源</a></li>

    <!-- <li><a href="" data-event_id="25754" data-event_action="click_name=入驻公寓">公寓入驻</a></li> -->

            <li class="beike__nav--code">
      下载APP
      <div class="nav-list beike__nav--qrcode">

                  <img width="94" height="94" src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=right&amp;ljweb_channel_key=zufang_search" alt="下载链家APP">

      </div>
    </li>

  </ul>
</div>
  <!-- 搜索房源sug -->
  <div class="search w1150" id="search">
  <!-- <a class="search__logo" href="/"></a> -->
  <div class="search__wrap">
    <input class="search__input fl" type="text" data-el="input" placeholder="请输入区域、商圈或小区名开始找房" autocomplete="off" value="" data-value="">
    <span class="search__button fl" data-el="button" data-event_id="10800" data-event_send="no"></span>
  </div>

</div>  </div>

  <!-- 列表页面包屑 -->
  <div class="bread__nav w1150 ">
  <p class="bread__nav__wrapper oneline">
                  <a href="https://hz.lianjia.com/">杭州链家网</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="https://hz.lianjia.com/zufang/">杭州租房</a>
      </h1>
            </p>
</div>

  <!-- 筛选项 -->
  <div class="filter">
  <div class="filter__wrapper w1150" id="filter">
    <ul class="filter__item--noaside">
      <li class="filter__item--level1 down strong" data-tab="1" data-el="area" data-antitarget="station"><a href="/zufang/" onclick="return false;">按区域</a></li>
          <li class="filter__item--level1 " data-tab="1" data-el="station" data-antitarget="area"><a href="/zufang/" onclick="return false;">按地铁线</a></li>
        </ul>

          <ul data-target="area" class="">
              <li data-id="0" data-type="district" class="filter__item--level2 filter__item--aside strong">
          <a href="/zufang/"  rel="nofollow">不限</a>
        </li>
              <li data-id="330106" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xihu/"  >西湖</a>
        </li>
              <li data-id="330103" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xiacheng/"  >下城</a>
        </li>
              <li data-id="330104" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/jianggan/"  >江干</a>
        </li>
              <li data-id="330105" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/gongshu/"  >拱墅</a>
        </li>
              <li data-id="330102" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/shangcheng/"  >上城</a>
        </li>
              <li data-id="330108" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/binjiang/"  >滨江</a>
        </li>
              <li data-id="330110" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/yuhang/"  >余杭</a>
        </li>
              <li data-id="330109" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xiaoshan/"  >萧山</a>
        </li>
              <li data-id="330183" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/fuyang/"  >富阳</a>
        </li>
              <li data-id="330185" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/linan/"  >临安</a>
        </li>
              <li data-id="23011864" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/qiantangxinqu/"  >钱塘新区</a>
        </li>
            </ul>

          <ul class="hide" data-target="station">
              <li data-id="0" data-type="line" class="filter__item--level2 filter__item--aside strong">
          <a href="/ditiezufang/" rel="nofollow">不限</a>
        </li>
              <li data-id="110460707" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li110460707/" >1号线(临平-湘湖)</a>
        </li>
              <li data-id="1820035120370916" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li1820035120370916/" >1号线(下沙江滨-湘湖)</a>
        </li>
              <li data-id="189500791680395" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li189500791680395/" >地铁2号线</a>
        </li>
              <li data-id="189503468170337" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li189503468170337/" >地铁4号线</a>
        </li>
              <li data-id="1820044952055481" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li1820044952055481/" >地铁5号线</a>
        </li>
            </ul>


          <ul data-target="station">
              </ul>

          <ul class="filter__ul" data-el="rentType">
          <li class="filter__item--level4 filter__item--aside"><a href="javascript:;">方式</a></li>
                  <li data-id="0" class="filter__item--level4 strong">
            <a href="/zufang/" rel="nofollow" >不限</a>
          </li>
                  <li data-id="200600000001" class="filter__item--level4 ">
            <a href="/zufang/rt200600000001/"  >整租</a>
          </li>
                  <li data-id="200600000002" class="filter__item--level4 ">
            <a href="/zufang/rt200600000002/"  >合租</a>
          </li>
              </ul>


          <ul class="filter__ul" data-el="filterPrice">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">租金</a></li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp1/">≤1000元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp2/">1000-1500元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp3/">1500-2000元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp4/">2000-3000元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp5/">3000-4500元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp6/">≥4500元</a>
          </li>
                  <li class="filter__item--input" data-url="/zufang/brp{min}erp{max}/"><input type="text" data-el="input_start" value="">-<input data-el="input_end" type="text" value="">元<span class="filter__button" data-el="button"></span></li>
      </ul>

          <ul class="filter__ul">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">户型</a></li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l0/">一居</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l1/">两居</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l2/">三居</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l3/">四居+</a>
          </li>
              </ul>


          <ul class="filter__ul ">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">朝向</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000001/">东</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000005/">西</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000003/">南</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000007/">北</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000009/">南北</a>
          </li>
              </ul>

          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">品牌</a></li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200301001000/">链家</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200302002000/">自如</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200302003000/">魔方公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200302144000/">城家公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306001917/">宅一起新青年社区</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306006672/">初九公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306007028/">奥通公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306001866/">泊寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306001062/">江南寓</a>
          </li>
                    </ul>

          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">特色</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/su1/">近地铁</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/bc1/">拎包入住</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/de1/">精装修</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/rpw1/">押一付一</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/in1/">新上</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/ht1/">认证公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/hk1/">随时看房</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/vr1/">VR房源</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/orec1/">业主自荐</a>
          </li>
              </ul>
          <!--租期-->
            <ul class="filter__ul hide">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">租期</a></li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp1/">月租</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp2/">年租</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp3/">一个月起租</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp4/">1-3个月</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp5/">4-6个月</a>
                </li>
                    </ul>

          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">楼层</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/lc200500000003/">低楼层</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/lc200500000002/">中楼层</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/lc200500000001/">高楼层</a>
          </li>
              </ul>

          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">电梯</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/ie0/">无电梯</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/ie1/">有电梯</a>
          </li>
              </ul>

      </div>
  <div class="filter__item--more" data-el="filterMore">收起<i class="more-icon"></i></div>
</div>

  <!-- 房源列表相关信息 -->
  <div class="content w1150" id="content">
    <div class="content__article">

      <!-- 搜索结果信息 -->
      <p class="content__title">
      已为您找到 <span class="content__title--hl">50105</span> 套 <a href="https://hz.lianjia.com/zufang/" target="_blank" style="text-decoration:none;color:black">杭州租房</a>
    <span class="content__title--aside"><a href="/zufang/" id="clearUrl">清空条件</a></span>
</p>

      <!-- 搜索结果排序模块 -->
      <ul class="content__filter" id="contentList">
            <li data-event_id="10800" data-event_action="search_condition=/zufang/" class='content__filter--selected'>
        <a href="/zufang/" 
           data-event_id="10797" 
           data-event_action="target=综合排序"
           data-event_position="target">综合排序</a>
      </li>
                <li data-event_id="10800" data-event_action="search_condition=/zufang/rco11/" >
        <a href="/zufang/rco11/" 
           data-event_id="10797" 
           data-event_action="target=最新上架"
           data-event_position="target">最新上架</a>
      </li>
                                                              <li data-event_id="10800" 
          data-event_action="search_condition=/zufang/rco21/" 
          class=' '>

                  <a href="/zufang/rco21/" 
             data-event_id="10797" 
             data-event_action="target=价格"
             data-event_position="target"
             >价格</a>
              </li>
                                                              <li data-event_id="10800" 
          data-event_action="search_condition=/zufang/rco31/" 
          class=' '>

                  <a href="/zufang/rco31/" 
             data-event_id="10797" 
             data-event_action="target=面积"
             data-event_position="target"
             >面积</a>
              </li>
        </ul>

      <!-- 小区吊顶模块 -->


        <!-- 有结果时，房源列表 -->
        <div class="content__list">

          <!--直通车 品牌或门店-->
                    <!-- 直升机 广告房源与list去重 && 广告房源插入list第1、3、4位(房源数不足3个时广告可按顺序排列) -->

          <!-- 房源列表模块 -->
          <div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2298569620442841088"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="0"
  data-total="50105"
  data-fb_expo_id="360867990149844993"
  data-t="default"
  data-strategy_id=""
  data-click_position="0"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=0"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2298569620442841088.html"
      title="整租·柏悦公馆 1室1厅 南">
        <img
          alt="整租·柏悦公馆 1室1厅 南_柏悦公馆租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/17481878-0a80-477b-82c1-f5b7544dec73.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2298569620442841088.html">
          整租·柏悦公馆 1室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="柏悦公馆" href="/zufang/c1820027199512739/" target="_blank">柏悦公馆</a>
        <i>/</i>
        38㎡
        <i>/</i>南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （16层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">8天前维护</span>
      </p>
      <span class="content__list--item-price"><em>2250</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2341047302694633472"
  data-brand_code="200306007897"
  data-ad_code="39304822697903016"
  data-c_type="1"
  data-position="1"
  data-total="50105"
  data-fb_expo_id="360867990300844033"
  data-t=""
  data-strategy_id=""
  data-click_position="1"
  data-ad_type="40"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=1"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2341047302694633472.html"
      title="合租·万科杭宸 4居室 南卧">
        <img
          alt="合租·万科杭宸 4居室 南卧_万科杭宸租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/20c696cb-df2a-4c9b-8300-af5e5d05ebe5.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
                  <p class="content__list--item--ad">
            精选          </p>
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2341047302694633472.html">
          合租·万科杭宸 4居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/gouzhuang/" target="_blank">勾庄</a>-<a title="万科杭宸" href="/zufang/c1810451854045197/" target="_blank">万科杭宸</a>
        <i>/</i>
        13㎡
        <i>/</i>南        <i>/</i>
          4室2厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            途牛居          </span>
                <span class="content__list--item--time oneline">14天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1560</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2546240842856153088"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="2"
  data-total="50105"
  data-fb_expo_id="360867990149844995"
  data-t="default"
  data-strategy_id=""
  data-click_position="2"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=2"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2546240842856153088.html"
      title="整租·丁桥大唐苑 2室1厅 南">
        <img
          alt="整租·丁桥大唐苑 2室1厅 南_丁桥大唐苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/7cd3a374-5b26-4387-98b1-5fad99daa3d8.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2546240842856153088.html">
          整租·丁桥大唐苑 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="丁桥大唐苑" href="/zufang/c188325621625485/" target="_blank">丁桥大唐苑</a>
        <i>/</i>
        66㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">12天前维护</span>
      </p>
      <span class="content__list--item-price"><em>4500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2549927416776622080"
  data-brand_code="200306001499"
  data-ad_code="39319884577260640"
  data-c_type="1"
  data-position="3"
  data-total="50105"
  data-fb_expo_id="360867990300844034"
  data-t=""
  data-strategy_id=""
  data-click_position="3"
  data-ad_type="40"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=3"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2549927416776622080.html"
      title="合租·仓乐雅苑 3居室 南卧">
        <img
          alt="合租·仓乐雅苑 3居室 南卧_仓乐雅苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/4e58cf0b-5141-487c-8c84-6a8c265cbfb4.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
                  <p class="content__list--item--ad">
            精选          </p>
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2549927416776622080.html">
          合租·仓乐雅苑 3居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/weilaikejicheng/" target="_blank">未来科技城</a>-<a title="仓乐雅苑" href="/zufang/c1820031760637478/" target="_blank">仓乐雅苑</a>
        <i>/</i>
        18㎡
        <i>/</i>南        <i>/</i>
          3室2厅3卫        <span class="hide">
          <i>/</i>
          高楼层                        （19层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--independent_bathroom">独立卫生间</i>
            <i class="content__item__tag--rent_period_month">月租</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            鹿汀公寓          </span>
                <span class="content__list--item--time oneline">2天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1480</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2346427074744418304"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="4"
  data-total="50105"
  data-fb_expo_id="360867990149844997"
  data-t="default"
  data-strategy_id=""
  data-click_position="4"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=4"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2346427074744418304.html"
      title="整租·东方时代中心 1室1厅 东南/南">
        <img
          alt="整租·东方时代中心 1室1厅 东南/南_东方时代中心租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/e4d7690a-6256-4230-864a-9f104c25266b.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2346427074744418304.html">
          整租·东方时代中心 1室1厅 东南/南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/sanliting/" target="_blank">三里亭</a>-<a title="东方时代中心" href="/zufang/c1811100597136/" target="_blank">东方时代中心</a>
        <i>/</i>
        38㎡
        <i>/</i>东南 南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （18层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--is_new">新上</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>3300</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2549930602258505728"
  data-brand_code="200306001499"
  data-ad_code="39319884577260640"
  data-c_type="1"
  data-position="5"
  data-total="50105"
  data-fb_expo_id="360867990300844035"
  data-t=""
  data-strategy_id=""
  data-click_position="5"
  data-ad_type="40"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=5"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2549930602258505728.html"
      title="合租·仓乐雅苑 3居室 南卧">
        <img
          alt="合租·仓乐雅苑 3居室 南卧_仓乐雅苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/f99c9a1c-20be-40e8-81b6-7375def869cd.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
                  <p class="content__list--item--ad">
            精选          </p>
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2549930602258505728.html">
          合租·仓乐雅苑 3居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/weilaikejicheng/" target="_blank">未来科技城</a>-<a title="仓乐雅苑" href="/zufang/c1820031760637478/" target="_blank">仓乐雅苑</a>
        <i>/</i>
        21㎡
        <i>/</i>南        <i>/</i>
          3室2厅3卫        <span class="hide">
          <i>/</i>
          高楼层                        （19层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--independent_bathroom">独立卫生间</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--independent_balcony">独立阳台</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            鹿汀公寓          </span>
                <span class="content__list--item--time oneline">2天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1580</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2298572371604275200"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="6"
  data-total="50105"
  data-fb_expo_id="360867990149844999"
  data-t="default"
  data-strategy_id=""
  data-click_position="6"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=6"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2298572371604275200.html"
      title="整租·贝利云栖中心 2室1厅 南">
        <img
          alt="整租·贝利云栖中心 2室1厅 南_贝利云栖中心租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/6f7136f9-e304-413d-b724-2040ea004465.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2298572371604275200.html">
          整租·贝利云栖中心 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xihu/">西湖</a>-<a href="/zufang/zhuantang/" target="_blank">转塘</a>-<a title="贝利云栖中心" href="/zufang/c187330714366333/" target="_blank">贝利云栖中心</a>
        <i>/</i>
        47㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （10层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">10个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>2950</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2352015362263875584"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="7"
  data-total="50105"
  data-fb_expo_id="360867990149845000"
  data-t="default"
  data-strategy_id=""
  data-click_position="7"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=7"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2352015362263875584.html"
      title="整租·三里亭苑四区 2室1厅 南">
        <img
          alt="整租·三里亭苑四区 2室1厅 南_三里亭苑四区租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/931dc96c-9d95-426c-bdea-5516689adfcd.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2352015362263875584.html">
          整租·三里亭苑四区 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/sanliting/" target="_blank">三里亭</a>-<a title="三里亭苑四区" href="/zufang/c1811043638687/" target="_blank">三里亭苑四区</a>
        <i>/</i>
        48㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （7层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">7天前维护</span>
      </p>
      <span class="content__list--item-price"><em>3000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2322270625831862272"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="8"
  data-total="50105"
  data-fb_expo_id="360867990149845001"
  data-t="default"
  data-strategy_id=""
  data-click_position="8"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=8"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2322270625831862272.html"
      title="整租·之江富城 2室1厅 南">
        <img
          alt="整租·之江富城 2室1厅 南_之江富城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/9ad97967-ddef-471f-8e67-2737dcf988cc.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2322270625831862272.html">
          整租·之江富城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xihu/">西湖</a>-<a href="/zufang/zhuantang/" target="_blank">转塘</a>-<a title="之江富城" href="/zufang/c1820022264839218/" target="_blank">之江富城</a>
        <i>/</i>
        44㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">6个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>2600</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2322287039779192832"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="9"
  data-total="50105"
  data-fb_expo_id="360867990149845002"
  data-t="default"
  data-strategy_id=""
  data-click_position="9"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=9"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2322287039779192832.html"
      title="整租·之江富城 1室1厅 南">
        <img
          alt="整租·之江富城 1室1厅 南_之江富城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/a3664ada-4dcd-420c-b096-b95e8b78bc7d.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2322287039779192832.html">
          整租·之江富城 1室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xihu/">西湖</a>-<a href="/zufang/zhuantang/" target="_blank">转塘</a>-<a title="之江富城" href="/zufang/c1820022264839218/" target="_blank">之江富城</a>
        <i>/</i>
        44㎡
        <i>/</i>南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">6个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>2300</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2298573207588323328"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="10"
  data-total="50105"
  data-fb_expo_id="360867990149845003"
  data-t="default"
  data-strategy_id=""
  data-click_position="10"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=10"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2298573207588323328.html"
      title="整租·克拉公馆 1室1厅 南">
        <img
          alt="整租·克拉公馆 1室1厅 南_克拉公馆租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/9bc2f1fc-ba3b-470a-8fe7-59372a8cc7f7.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2298573207588323328.html">
          整租·克拉公馆 1室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/sanliting/" target="_blank">三里亭</a>-<a title="克拉公馆" href="/zufang/c1811100058498/" target="_blank">克拉公馆</a>
        <i>/</i>
        42㎡
        <i>/</i>南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （15层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">2个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>2660</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2353350935486939136"
  data-brand_code="200306001247"
  data-ad_code=""
  data-c_type="1"
  data-position="11"
  data-total="50105"
  data-fb_expo_id="360867990149844994"
  data-t="default"
  data-strategy_id=""
  data-click_position="11"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=11"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2353350935486939136.html"
      title="整租·福鼎家园 1室0厅 北">
        <img
          alt="整租·福鼎家园 1室0厅 北_福鼎家园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/ea30d5f8-d006-4009-affb-c10fe5ae30f1.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2353350935486939136.html">
          整租·福鼎家园 1室0厅 北        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/weilaikejicheng/" target="_blank">未来科技城</a>-<a title="福鼎家园" href="/zufang/c1810726255636885/" target="_blank">福鼎家园</a>
        <i>/</i>
        28㎡
        <i>/</i>北        <i>/</i>
          1室0厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （15层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            航湾悦居          </span>
                <span class="content__list--item--time oneline">3天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1800</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2298568908871319552"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="12"
  data-total="50105"
  data-fb_expo_id="360867990149845005"
  data-t="default"
  data-strategy_id=""
  data-click_position="12"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=12"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2298568908871319552.html"
      title="整租·美好桂花星城 2室1厅 南">
        <img
          alt="整租·美好桂花星城 2室1厅 南_美好桂花星城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/a5a92b80-5ee9-4302-b21c-e7a2e01fd8a0.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2298568908871319552.html">
          整租·美好桂花星城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/linping/" target="_blank">临平</a>-<a title="美好桂花星城" href="/zufang/c2711057887713/" target="_blank">美好桂花星城</a>
        <i>/</i>
        85㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （27层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">6个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>2900</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2341673058265473024"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="13"
  data-total="50105"
  data-fb_expo_id="360867990149844996"
  data-t="default"
  data-strategy_id=""
  data-click_position="13"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=13"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2341673058265473024.html"
      title="合租·龙湖旭辉春江悦茗 4居室 北卧">
        <img
          alt="合租·龙湖旭辉春江悦茗 4居室 北卧_龙湖旭辉春江悦茗租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-house-1/img/ad40efae68e06d5607579210fcfcecd2-1600338622337/7a1a88dab97bd4ff542a3cc4763cd670.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2341673058265473024.html">
          合租·龙湖旭辉春江悦茗 4居室 北卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xiaoshan/">萧山</a>-<a href="/zufang/xiaoshanxinchengqu/" target="_blank">萧山新城区</a>-<a title="龙湖旭辉春江悦茗" href="/zufang/c188390937162697/" target="_blank">龙湖旭辉春江悦茗</a>
        <i>/</i>
        6㎡
        <i>/</i>北        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （30层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>1290</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2298569342998290432"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="14"
  data-total="50105"
  data-fb_expo_id="360867990149845007"
  data-t="default"
  data-strategy_id=""
  data-click_position="14"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=14"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2298569342998290432.html"
      title="整租·复地壹中心 1室1厅 南">
        <img
          alt="整租·复地壹中心 1室1厅 南_复地壹中心租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/31ce9cca-2c09-4db7-b4fa-c2dd999ffbca.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2298569342998290432.html">
          整租·复地壹中心 1室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/shenhua/" target="_blank">申花</a>-<a title="复地壹中心" href="/zufang/c188397849899270/" target="_blank">复地壹中心</a>
        <i>/</i>
        53㎡
        <i>/</i>南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （23层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">10个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3200</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2368847896033361920"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="15"
  data-total="50105"
  data-fb_expo_id="360867990149845008"
  data-t="default"
  data-strategy_id=""
  data-click_position="15"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=15"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2368847896033361920.html"
      title="整租·西溪乐天城 2室1厅 南">
        <img
          alt="整租·西溪乐天城 2室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/95642df3-58bc-49c8-9096-9d90d8fa0ebd.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2368847896033361920.html">
          整租·西溪乐天城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        49㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （7层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">1个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2373797058998960128"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="16"
  data-total="50105"
  data-fb_expo_id="360867990149845009"
  data-t="default"
  data-strategy_id=""
  data-click_position="16"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=16"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2373797058998960128.html"
      title="整租·西溪乐天城 1室1厅 南">
        <img
          alt="整租·西溪乐天城 1室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/4479e0c9-c197-4d2d-a5ac-6ed889aa863f.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2373797058998960128.html">
          整租·西溪乐天城 1室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        48㎡
        <i>/</i>南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （8层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">5个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2330281705073811456"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="17"
  data-total="50105"
  data-fb_expo_id="360867990149845010"
  data-t="default"
  data-strategy_id=""
  data-click_position="17"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=17"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2330281705073811456.html"
      title="整租·西溪乐天城 2室1厅 南">
        <img
          alt="整租·西溪乐天城 2室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/fcc38635-7519-4a5c-86f2-d692967c6501.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2330281705073811456.html">
          整租·西溪乐天城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        50㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （8层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">1个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2373800904378810368"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="18"
  data-total="50105"
  data-fb_expo_id="360867990149845011"
  data-t="default"
  data-strategy_id=""
  data-click_position="18"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=18"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2373800904378810368.html"
      title="整租·西溪乐天城 2室1厅 南">
        <img
          alt="整租·西溪乐天城 2室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/941eb638-bd86-434c-abb0-350f7e421d77.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2373800904378810368.html">
          整租·西溪乐天城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        49㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （8层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">1个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2373792394824130560"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="19"
  data-total="50105"
  data-fb_expo_id="360867990149845012"
  data-t="default"
  data-strategy_id=""
  data-click_position="19"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=19"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2373792394824130560.html"
      title="整租·西溪乐天城 2室2厅 南">
        <img
          alt="整租·西溪乐天城 2室2厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/0e172928-9455-4073-8d60-b39e916d6bc2.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2373792394824130560.html">
          整租·西溪乐天城 2室2厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        48㎡
        <i>/</i>南        <i>/</i>
          2室2厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （8层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">6个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2384034105412026368"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="20"
  data-total="50105"
  data-fb_expo_id="360867990149845013"
  data-t="default"
  data-strategy_id=""
  data-click_position="20"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=20"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2384034105412026368.html"
      title="整租·西溪乐天城 2室1厅 南">
        <img
          alt="整租·西溪乐天城 2室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/f8bf9f30-de38-4ce4-af96-98e8ce213afb.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2384034105412026368.html">
          整租·西溪乐天城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        48㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （7层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">1个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2414267898764722176"
  data-brand_code="200306002808"
  data-ad_code=""
  data-c_type="1"
  data-position="21"
  data-total="50105"
  data-fb_expo_id="360867990149844998"
  data-t="default"
  data-strategy_id=""
  data-click_position="21"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=21"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2414267898764722176.html"
      title="合租·文晖铭园 4居室 东南卧">
        <img
          alt="合租·文晖铭园 4居室 东南卧_文晖铭园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/3d2dfaa2-0963-429c-8b05-6d00b7ed689a.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2414267898764722176.html">
          合租·文晖铭园 4居室 东南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/zhanongkou/" target="_blank">闸弄口</a>-<a title="文晖铭园" href="/zufang/c2711052041651/" target="_blank">文晖铭园</a>
        <i>/</i>
        18㎡
        <i>/</i>东南        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--independent_balcony">独立阳台</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            i+公寓（杭州）          </span>
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1700</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2385281251188670464"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="22"
  data-total="50105"
  data-fb_expo_id="360867990149845015"
  data-t="default"
  data-strategy_id=""
  data-click_position="22"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=22"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2385281251188670464.html"
      title="整租·西溪乐天城 2室1厅 南">
        <img
          alt="整租·西溪乐天城 2室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/917a268e-8a6d-41ad-a342-6802834c4605.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2385281251188670464.html">
          整租·西溪乐天城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        48㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （8层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">1个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2337168819409395712"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="23"
  data-total="50105"
  data-fb_expo_id="360867990149845004"
  data-t="default"
  data-strategy_id=""
  data-click_position="23"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=23"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2337168819409395712.html"
      title="合租·月雅苑 4居室 南卧">
        <img
          alt="合租·月雅苑 4居室 南卧_月雅苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-house-1/img/ad40efae68e06d5607579210fcfcecd2-1599623016488/e8c18ff7480e5d669023afab64c1e0c5.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2337168819409395712.html">
          合租·月雅苑 4居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/qiantangxinqu/">钱塘新区</a>-<a href="/zufang/gaojiaoyuanquxi/" target="_blank">高教园区西</a>-<a title="月雅苑" href="/zufang/c1811043638514/" target="_blank">月雅苑</a>
        <i>/</i>
        14㎡
        <i>/</i>南        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>1590</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2298569525819613184"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="24"
  data-total="50105"
  data-fb_expo_id="360867990149845017"
  data-t="default"
  data-strategy_id=""
  data-click_position="24"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=24"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2298569525819613184.html"
      title="整租·复地壹中心 1室1厅 东">
        <img
          alt="整租·复地壹中心 1室1厅 东_复地壹中心租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/0939cff7-c4d6-40c4-b4d1-5f4c11b9329b.jpeg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2298569525819613184.html">
          整租·复地壹中心 1室1厅 东        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/shenhua/" target="_blank">申花</a>-<a title="复地壹中心" href="/zufang/c188397849899270/" target="_blank">复地壹中心</a>
        <i>/</i>
        50㎡
        <i>/</i>东        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （23层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">9个月前维护</span>
      </p>
      <span class="content__list--item-price"><em>3200</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2323480615326064640"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="25"
  data-total="50105"
  data-fb_expo_id="360867990149845006"
  data-t="default"
  data-strategy_id=""
  data-click_position="25"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=25"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2323480615326064640.html"
      title="合租·铭雅苑东区 5居室 东卧">
        <img
          alt="合租·铭雅苑东区 5居室 东卧_铭雅苑东区租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1597965361142/f84236e5bf5876192d7e84dff1d9d618.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2323480615326064640.html">
          合租·铭雅苑东区 5居室 东卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/sandun/" target="_blank">三墩</a>-<a title="铭雅苑东区" href="/zufang/c1811044536765/" target="_blank">铭雅苑东区</a>
        <i>/</i>
        8㎡
        <i>/</i>东        <i>/</i>
          5室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>1260</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2373799781261910016"
  data-brand_code="200306004772"
  data-ad_code=""
  data-c_type="1"
  data-position="26"
  data-total="50105"
  data-fb_expo_id="360867990149845019"
  data-t="default"
  data-strategy_id=""
  data-click_position="26"
  data-ad_type="0"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=26"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2373799781261910016.html"
      title="整租·西溪乐天城 2室1厅 南">
        <img
          alt="整租·西溪乐天城 2室1厅 南_西溪乐天城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/lease-image/house/dca1209a-8c30-475c-a231-3f58bb67d38e.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2373799781261910016.html">
          整租·西溪乐天城 2室1厅 南        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="西溪乐天城" href="/zufang/c1820025360457947/" target="_blank">西溪乐天城</a>
        <i>/</i>
        50㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （8层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            贝壳优选          </span>
                <span class="content__list--item--time oneline">13天前维护</span>
      </p>
      <span class="content__list--item-price"><em>3500</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2352079673367724032"
  data-brand_code="200306002283"
  data-ad_code=""
  data-c_type="1"
  data-position="27"
  data-total="50105"
  data-fb_expo_id="360867990149845014"
  data-t="default"
  data-strategy_id=""
  data-click_position="27"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=27"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2352079673367724032.html"
      title="合租·岸上蓝山 4居室 西北卧">
        <img
          alt="合租·岸上蓝山 4居室 西北卧_岸上蓝山租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/67e95c74-1336-48ff-8104-3be71ecba839.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2352079673367724032.html">
          合租·岸上蓝山 4居室 西北卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/xianlin1/" target="_blank">闲林</a>-<a title="岸上蓝山" href="/zufang/c1811099689180/" target="_blank">岸上蓝山</a>
        <i>/</i>
        10㎡
        <i>/</i>西北        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            房家加公寓          </span>
                <span class="content__list--item--time oneline">8天前维护</span>
      </p>
      <span class="content__list--item-price"><em>950</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2316602621219315712"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="28"
  data-total="50105"
  data-fb_expo_id="360867990149845016"
  data-t="default"
  data-strategy_id=""
  data-click_position="28"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=28"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2316602621219315712.html"
      title="合租·阳光郡 4居室 东卧">
        <img
          alt="合租·阳光郡 4居室 东卧_阳光郡租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1597242045533/626a0a26d190c8963a2157ab7f42423f.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2316602621219315712.html">
          合租·阳光郡 4居室 东卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/sandun/" target="_blank">三墩</a>-<a title="阳光郡" href="/zufang/c1811100817588/" target="_blank">阳光郡</a>
        <i>/</i>
        6㎡
        <i>/</i>东        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （23层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>1190</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2323711811536289792"
  data-brand_code="200306001062"
  data-ad_code=""
  data-c_type="1"
  data-position="29"
  data-total="50105"
  data-fb_expo_id="360867990149845018"
  data-t="default"
  data-strategy_id=""
  data-click_position="29"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=29"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2323711811536289792.html"
      title="合租·雍荣华庭 4居室 南卧">
        <img
          alt="合租·雍荣华庭 4居室 南卧_雍荣华庭租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/108e8e91-f0fb-4208-a896-98199abdcaf1.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2323711811536289792.html">
          合租·雍荣华庭 4居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/shenhua/" target="_blank">申花</a>-<a title="雍荣华庭" href="/zufang/c1811067839491313/" target="_blank">雍荣华庭</a>
        <i>/</i>
        14㎡
        <i>/</i>南        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （30层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--rent_period_month">月租</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            江南寓          </span>
                <span class="content__list--item--time oneline">22天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1450</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2327486257283997696"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="30"
  data-total="50105"
  data-fb_expo_id="360867990149845020"
  data-t="default"
  data-strategy_id=""
  data-click_position="30"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=30"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2327486257283997696.html"
      title="合租·顺发江南丽锦 5居室 南卧">
        <img
          alt="合租·顺发江南丽锦 5居室 南卧_顺发江南丽锦租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1598343491312/bf4af73fe1a2c5e64a67bf82964c4ca5.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2327486257283997696.html">
          合租·顺发江南丽锦 5居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xiaoshan/">萧山</a>-<a href="/zufang/qianjiangshijicheng/" target="_blank">钱江世纪城</a>-<a title="顺发江南丽锦" href="/zufang/c187261814534484/" target="_blank">顺发江南丽锦</a>
        <i>/</i>
        14㎡
        <i>/</i>南        <i>/</i>
          5室1厅2卫        <span class="hide">
          <i>/</i>
          低楼层                        （33层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--independent_balcony">独立阳台</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>2160</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2350664107336155136"
  data-brand_code="200306007984"
  data-ad_code=""
  data-c_type="1"
  data-position="31"
  data-total="50105"
  data-fb_expo_id="360867990149845021"
  data-t="default"
  data-strategy_id=""
  data-click_position="31"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=31"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2350664107336155136.html"
      title="合租·香兰名院 4居室 南卧">
        <img
          alt="合租·香兰名院 4居室 南卧_香兰名院租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-user-avatar/754cb3b8-5318-4fa6-9010-0d670a9f228b.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2350664107336155136.html">
          合租·香兰名院 4居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/daguan/" target="_blank">大关</a>-<a title="香兰名院" href="/zufang/c1820031044052712/" target="_blank">香兰名院</a>
        <i>/</i>
        15㎡
        <i>/</i>南        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （20层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            杭州-世纪鸿源          </span>
                <span class="content__list--item--time oneline">14天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1150</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2339011079428120576"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="32"
  data-total="50105"
  data-fb_expo_id="360867990149845022"
  data-t="default"
  data-strategy_id=""
  data-click_position="32"
  data-ad_type="50"
  data-distribution_type="203500000001"
  data-event_id="21333"
  data-event_action="click_position=32"
  data-event_position="click_position"
  data-event_send="no"
  >
    <a
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2339011079428120576.html"
      title="合租·阳光城翡丽湾 4居室 南卧">
        <img
          alt="合租·阳光城翡丽湾 4居室 南卧_阳光城翡丽湾租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200917160625398"
          data-src="https://image1.ljcdn.com/rent-house-1/img/ad40efae68e06d5607579210fcfcecd2-1600051531458/db33d541e6a42b8fcffe166447fdd37f.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title">
        <a class="twoline" target="_blank" href="/zufang/HZ2339011079428120576.html">
          合租·阳光城翡丽湾 4居室 南卧        </a>
              </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="阳光城翡丽湾" href="/zufang/c1811100819179/" target="_blank">阳光城翡丽湾</a>
        <i>/</i>
        12㎡
        <i>/</i>南        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （17层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>1430</em> 元/月</span>
    </div>

</div>
        </div>

        <!-- 列表分页模块 -->
        <div class="content__pg" data-el="page_navigation" data-url="/zufang/pg{page}/" data-totalPage=100 data-curPage=1>
        </div>

        <ul style="display:hidden">
                      <li><a href="/zufang/pg2/"></a></li>
                      <li><a href="/zufang/pg3/"></a></li>
                      <li><a href="/zufang/pg4/"></a></li>
                      <li><a href="/zufang/pg5/"></a></li>
                      <li><a href="/zufang/pg6/"></a></li>
                      <li><a href="/zufang/pg7/"></a></li>
                      <li><a href="/zufang/pg8/"></a></li>
                      <li><a href="/zufang/pg9/"></a></li>
                      <li><a href="/zufang/pg10/"></a></li>
                      <li><a href="/zufang/pg11/"></a></li>
                      <li><a href="/zufang/pg12/"></a></li>
                      <li><a href="/zufang/pg13/"></a></li>
                      <li><a href="/zufang/pg14/"></a></li>
                      <li><a href="/zufang/pg15/"></a></li>
                      <li><a href="/zufang/pg16/"></a></li>
                      <li><a href="/zufang/pg17/"></a></li>
                      <li><a href="/zufang/pg18/"></a></li>
                      <li><a href="/zufang/pg19/"></a></li>
                      <li><a href="/zufang/pg20/"></a></li>
                      <li><a href="/zufang/pg21/"></a></li>
                      <li><a href="/zufang/pg22/"></a></li>
                      <li><a href="/zufang/pg23/"></a></li>
                      <li><a href="/zufang/pg24/"></a></li>
                      <li><a href="/zufang/pg25/"></a></li>
                      <li><a href="/zufang/pg26/"></a></li>
                      <li><a href="/zufang/pg27/"></a></li>
                      <li><a href="/zufang/pg28/"></a></li>
                      <li><a href="/zufang/pg29/"></a></li>
                      <li><a href="/zufang/pg30/"></a></li>
                      <li><a href="/zufang/pg31/"></a></li>
                      <li><a href="/zufang/pg32/"></a></li>
                      <li><a href="/zufang/pg33/"></a></li>
                      <li><a href="/zufang/pg34/"></a></li>
                      <li><a href="/zufang/pg35/"></a></li>
                      <li><a href="/zufang/pg36/"></a></li>
                      <li><a href="/zufang/pg37/"></a></li>
                      <li><a href="/zufang/pg38/"></a></li>
                      <li><a href="/zufang/pg39/"></a></li>
                      <li><a href="/zufang/pg40/"></a></li>
                      <li><a href="/zufang/pg41/"></a></li>
                      <li><a href="/zufang/pg42/"></a></li>
                      <li><a href="/zufang/pg43/"></a></li>
                      <li><a href="/zufang/pg44/"></a></li>
                      <li><a href="/zufang/pg45/"></a></li>
                      <li><a href="/zufang/pg46/"></a></li>
                      <li><a href="/zufang/pg47/"></a></li>
                      <li><a href="/zufang/pg48/"></a></li>
                      <li><a href="/zufang/pg49/"></a></li>
                      <li><a href="/zufang/pg50/"></a></li>
                      <li><a href="/zufang/pg51/"></a></li>
                      <li><a href="/zufang/pg52/"></a></li>
                      <li><a href="/zufang/pg53/"></a></li>
                      <li><a href="/zufang/pg54/"></a></li>
                      <li><a href="/zufang/pg55/"></a></li>
                      <li><a href="/zufang/pg56/"></a></li>
                      <li><a href="/zufang/pg57/"></a></li>
                      <li><a href="/zufang/pg58/"></a></li>
                      <li><a href="/zufang/pg59/"></a></li>
                      <li><a href="/zufang/pg60/"></a></li>
                      <li><a href="/zufang/pg61/"></a></li>
                      <li><a href="/zufang/pg62/"></a></li>
                      <li><a href="/zufang/pg63/"></a></li>
                      <li><a href="/zufang/pg64/"></a></li>
                      <li><a href="/zufang/pg65/"></a></li>
                      <li><a href="/zufang/pg66/"></a></li>
                      <li><a href="/zufang/pg67/"></a></li>
                      <li><a href="/zufang/pg68/"></a></li>
                      <li><a href="/zufang/pg69/"></a></li>
                      <li><a href="/zufang/pg70/"></a></li>
                      <li><a href="/zufang/pg71/"></a></li>
                      <li><a href="/zufang/pg72/"></a></li>
                      <li><a href="/zufang/pg73/"></a></li>
                      <li><a href="/zufang/pg74/"></a></li>
                      <li><a href="/zufang/pg75/"></a></li>
                      <li><a href="/zufang/pg76/"></a></li>
                      <li><a href="/zufang/pg77/"></a></li>
                      <li><a href="/zufang/pg78/"></a></li>
                      <li><a href="/zufang/pg79/"></a></li>
                      <li><a href="/zufang/pg80/"></a></li>
                      <li><a href="/zufang/pg81/"></a></li>
                      <li><a href="/zufang/pg82/"></a></li>
                      <li><a href="/zufang/pg83/"></a></li>
                      <li><a href="/zufang/pg84/"></a></li>
                      <li><a href="/zufang/pg85/"></a></li>
                      <li><a href="/zufang/pg86/"></a></li>
                      <li><a href="/zufang/pg87/"></a></li>
                      <li><a href="/zufang/pg88/"></a></li>
                      <li><a href="/zufang/pg89/"></a></li>
                      <li><a href="/zufang/pg90/"></a></li>
                      <li><a href="/zufang/pg91/"></a></li>
                      <li><a href="/zufang/pg92/"></a></li>
                      <li><a href="/zufang/pg93/"></a></li>
                      <li><a href="/zufang/pg94/"></a></li>
                      <li><a href="/zufang/pg95/"></a></li>
                      <li><a href="/zufang/pg96/"></a></li>
                      <li><a href="/zufang/pg97/"></a></li>
                      <li><a href="/zufang/pg98/"></a></li>
                      <li><a href="/zufang/pg99/"></a></li>
                      <li><a href="/zufang/pg100/"></a></li>
                  </ul>


          </div>

          <div class="content__aside">


<div class="download">

  <div class="qr-code">
          <img width="94" height="94" src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=right&amp;ljweb_channel_key=zufang_search" alt="下载贝壳APP">
        <div class="title">下载链家APP</div>
    <div class="text">
      <p>扫描上方二维码</p>
      <p>随时查看新房源</p>
      <p class="get-more">
        <a href="//www.lianjia.com/client/">了解更多
          <img width="9" height="9" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEUAAACcn6Gfn5+an5+bnqCbnqGfn5+cn6EV6DbuAAAAB3RSTlMA0BAw8LAgvf5k9AAAAEdJREFUKM9jIBOkBqMJhBcqoAmUC6EKmJSjKWEWR1eiiK6ECZsSA3QlzuhKSihRghDA0EJ/BWIoCgzh4YMIZALRYBrMQAkAAF5bGMBkrwzqAAAAAElFTkSuQmCC">
        </a>
      </p>
    </div>
  </div>
</div>
        <div class="download">
  <div class="qr-code">
    <img width="94" height="94" src="https://image1.ljcdn.com/params-compact/f871e2c517a63630ce5894caa5804464.jpeg" alt="贝壳小程序">
    <div class="title">扫描微信咨询</div>
  </div>
</div>
        <div class="list-recommend" id="listRecommend">
        </div>
      </div>

  </div>




</div>

<!-- seo相关路径信息 -->
<div class="hide">
  <a href="/zufang/"></a>
  <a href="/zufang/pg2/"></a>
  <a href="/zufang/pg3/"></a>
  <a href="/zufang/pg4/"></a>
  <a href="/zufang/pg5/"></a>
  <a href="/zufang/pg6/"></a>
  <a href="/zufang/pg7/"></a>
  <a href="/zufang/pg8/"></a>
  <a href="/zufang/pg9/"></a>
  <a href="/zufang/pg10/"></a>
</div>

<!-- 检索出房源结果时，添加检索id埋点 -->
<input type="hidden" id="queryId" value="360867990149844992">

<!-- 底部留资弹窗 -->
<div data-el="fix-bottom-pop" class="fix-bottom-wrap">
  <div class="bottom-content">
    <img class="left-img" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/bg_agent@2x.png?_v=20200917160625398" alt="底部找房图片">
    <div class="middle-text">专业经纪人找房更高效</div>
    <div class="right-percent">
      <p class="top-text">想租到独家优惠的心仪房源？<span data-el="red-text" class="red-text">请不要频繁操作</span></p>
      <div class="form-user-info">
        <div class="login" style="display: none">
          <input 
            class="bottom-form-item" 
            data-el="phone-user"
            type="text" 
            value="" 
            name="phone"
            maxlength="11" 
            placeholder="请输入您的手机号">
          <button 
            class="submit-btn" 
            data-city_id="330100"
            data-el="submit-btn">预约咨询</button>
        </div>
        <div class="not-login" style="display: none">
          <div class="not-login-phone">
            <input 
              class="bottom-form-item bottom-form-phone" 
              data-el="phone-input"
              type="text" 
              value="" 
              name="phone"
              maxlength="11" 
              placeholder="请输入您的手机号">
            <span class="send-msg-code" data-el="msgCode">发送验证码</span>
          </div>
          <div>
            <input 
              class="bottom-form-item" 
              type="text" 
              value="" 
              data-el="inputMsgCode"
              maxlength="6" 
              placeholder="请输入验证码">
            <button 
              class="submit-btn" 
              data-city_id="330100"
              data-el="submit-btn">预约咨询</button>
          </div>
        </div>
      </div>
      <i data-el="fix-bottom-close" data-event_id="25435" class="close"></i>
    </div>
  </div>
</div>  <script src="https://s1.ljcdn.com/agent-sj-sdk/1.2.0/agent-sj-sdk.js"></script>

<script>
    g_conf.pageId = 'rentalList';
  g_conf.requestId = '9221617676935';
  g_conf.resblockId ='';
  g_conf.total = '50105';
  g_conf.cityId = '330100'
  var __requireList = ['https://s1.ljcdn.com/matrix_pc/dist/pc/src/page/list/index.js?_v=20200917160625398'];
  document.getElementById('clearUrl').href = '/zufang/brp{min}erp{max}/'.split('zufang/')[0] + 'zufang/';

</script>
  </div>

  <div class="fix-right-v3" id="back-top" log-mod="sidebar" data-el="right_bar">
  <table>
    <tbody>
      <tr>
        <td>
          <ul>
            <li class="myfav sidebar-item">
              <a title="我关注的房源" data-url="//user.lianjia.com/site/favorHouse/" data-bl="myfav" exposure-event_id="25755" data-event_id="25756" exposure-event_action="click_name=心愿单" data-event_action="click_name=心愿单">我关注的房源</a>
              <span class="popup"><i></i>我关注的房源</span>
            </li>
            <li class="sell sidebar-item" data-el="rightbar_entry">
              <a title="在线租房" href="/zufang/proprietor/offer?city_id=330100&city_name=杭州&position=rent_pc_rightbar_rent" target="_blank" data-bl="sell" exposure-event_id="25755" exposure-event_action="click_name=出租"  data-event_id="25756" data-event_action="click_name=出租">我要出租</a>
              <span class="popup"><i></i>我要出租</span>
            </li>
                          <li class="baodan sidebar-item">
                <a href="//hz.lianjia.com/anxinchengnuo" title="安心服务承诺" target="_blank" data-bl="baodan" data-event_id="25756" exposure-event_id="25755" exposure-event_action="click_name=安心保单" data-event_action="click_name=安心保单">安心服务承诺</a>
                <span class="popup">
                  <i></i>安心服务承诺
                </span>
              </li>

            <li class="download sidebar-item">
              <a href="//www.lianjia.com/client/" title="" target="_blank" data-bl="client" data-event_id="25756" exposure-event_id="25755" exposure-event_action="click_name=微信小程序" data-event_action="click_name=微信小程序">下载掌上链家</a>
              <span class="popup popup-qr">
                <i></i><img src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/lianjia/wxapp.jpg?_v=20200917160625398" alt="下载掌上链家" width="94">
                <em class="qr-title">链家微信小程序</em>
              </span>
            </li>
            <li class="phone sidebar-item">
              <a title="官方客服"  data-event_id="25756" exposure-event_id="25755" exposure-event_action="click_name=官方客服" data-event_action="click_name=官方客服">官方客服</a>
              <span class="popup"><i></i>官方客服</span>
            </li>

                        <li class="feedback sidebar-item">
              <a href="https://helper.lianjia.com/it/index2#/feedbackForC?channel=lj-pc&city=330100" title="反馈/投诉" data-bl="feedback" exposure-event_id="25755" data-event_id="25756" exposure-event_action="click_name=反馈" data-event_action="click_name=反馈"></a>
              <span class="popup"><i></i>反馈/投诉</span>
            </li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <ul>
    <li class="gotop sidebar-item" id="gotop" style="display: none;"><a title="返回顶部">返回顶部</a><span class="popup"><i></i>返回顶部</span></li>
  </ul>
</div>
  <div class="footer" style="margin-top:20px">
    <div class="footer__wrapper w1150">

      <div class="footer__top">
        <ul class="footer__light">
                    <li><a href="/zufang/wzdt/">网站地图</a></li>
                  </ul>
        <a class="footer__aside" href="tel:10109666">客服电话<span>10109666</span></a>
      </div>

      <div class="footer__middle">
        <ul data-el="parentList">
                      <li><a class="cur" data-index="0">热门商圈</a></li>
                      <li><a class="" data-index="1">推荐小区</a></li>
                      <li><a class="" data-index="2">租房城市</a></li>
                  </ul>
                  <ul data-el="childrenList"  style="display:block">
                          <li><a href="https://hz.lianjia.com/zufang/changqing1112/">长庆租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/nanxing/">南星租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/fuxing/">复兴租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/renhe2/">仁和租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wenyixilu/">文一西路租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/qingtai/">清泰租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xixing/">西兴租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yiqiao/">义桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jiande1/">建德租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jiubao/">九堡租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wandaguangchang2/">万达广场租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/huanglong/">黄龙租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gudang/">古荡租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/hemu/">和睦租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xixi/">西溪租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gongchenqiao/">拱宸桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/feicuicheng1/">翡翠城租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wulin11/">武林租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/tianshui1/">天水租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/dajiangdong/">大江东租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/caihongcheng/">彩虹城租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/huajiachi/">华家池租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/shenhua/">申花租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/sichoucheng1/">丝绸城租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/hubin1/">湖滨租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jianqiao/">笕桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/banshan/">半山租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/puyan/">浦沿租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/santang/">三塘租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/changhe/">长河租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/sandun/">三墩租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gouzhuang/">勾庄租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yanjiangbei/">沿江北租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gudang/">古荡租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/huochedongzhan/">火车东站租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yiqiao/">义桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xiongzhenlou/">雄镇楼租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/dingqiao/">丁桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jinjiang1/">近江租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/liangzhu/">良渚租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/deshengdong/">德胜东租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/changhe/">长河租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/fuyang1/">富阳租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/daguan/">大关租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/heping2/">和平租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xuejun/">学军租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/linpu/">临浦租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/tonglushangquan/">桐庐租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/zhanongkou/">闸弄口租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jialv/">嘉绿租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/qingtai/">清泰租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jingfang1/">景芳租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/dajiangdong/">大江东租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/santang/">三塘租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wenyixilu/">文一西路租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xianlin1/">闲林租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yanjiangnan/">沿江南租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/fuxing/">复兴租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jinshahu/">金沙湖租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/liuxia1/">留下租房</a></li>
                      </ul>
                  <ul data-el="childrenList"  >
                          <li><a href="https://hz.lianjia.com/zufang/c1820022260637977/">大通路98号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641307/">嘉绿福苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636713/">和睦公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820022037245901/">解放路8号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820024445699943/">水岸鑫域租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641703/">嘉绿文苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815909850746844/">小河东河下66-11号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815440795176902/">永泰名苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636393/">五洋东湖春天租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641388/">武林门新村租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815732752026627/">佑圣观路5号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043638833/">云峰一区租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820023393475872/">保利融信大国璟租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043639425/">广景苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043638496/">裕园公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636559/">湖墅北路101号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641404/">紫金公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641620/">金沙曲苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820023902308543/">环城东路240号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820022536418987/">金隅空港公馆租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815710271606474/">绿野清风租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043640426/">碧桂苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641555/">筑品金座租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043637400/">大关东六苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636769/">沈大北苑小区租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043642186/">天水巷租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043642200/">灯塔东苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636635/">石油公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043639517/">联合格里租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043635924/">知本大厦租房</a></li>
                      </ul>
                  <ul data-el="childrenList"  >
                          <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                          <li><a href="https://linyi.lianjia.com/zufang/">临沂租房</a></li>
                          <li><a href="https://huzhou.lianjia.com/zufang/">湖州租房</a></li>
                          <li><a href="https://wuhu.lianjia.com/zufang/">芜湖租房</a></li>
                          <li><a href="https://nanchong.lianjia.com/zufang/">南充租房</a></li>
                          <li><a href="https://xa.lianjia.com/zufang/">西安租房</a></li>
                          <li><a href="https://gz.lianjia.com/zufang/">广州租房</a></li>
                          <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                          <li><a href="https://san.lianjia.com/zufang/">三亚租房</a></li>
                          <li><a href="https://sjz.lianjia.com/zufang/">石家庄租房</a></li>
                          <li><a href="https://xc.lianjia.com/zufang/">许昌租房</a></li>
                          <li><a href="https://zj.lianjia.com/zufang/">镇江租房</a></li>
                          <li><a href="https://baoji.lianjia.com/zufang/">宝鸡租房</a></li>
                          <li><a href="https://yc.lianjia.com/zufang/">盐城租房</a></li>
                          <li><a href="https://zz.lianjia.com/zufang/">郑州租房</a></li>
                          <li><a href="https://dd.lianjia.com/zufang/">丹东租房</a></li>
                          <li><a href="https://sh.lianjia.com/zufang/">上海租房</a></li>
                          <li><a href="https://wf.lianjia.com/zufang/">潍坊租房</a></li>
                          <li><a href="https://ts.lianjia.com/zufang/">唐山租房</a></li>
                          <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                          <li><a href="https://liangshan.lianjia.com/zufang/">凉山租房</a></li>
                          <li><a href="https://gy.lianjia.com/zufang/">贵阳租房</a></li>
                          <li><a href="https://dazhou.lianjia.com/zufang/">达州租房</a></li>
                          <li><a href="https://hanzhong.lianjia.com/zufang/">汉中租房</a></li>
                          <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                          <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                          <li><a href="https://wh.lianjia.com/zufang/">武汉租房</a></li>
                          <li><a href="https://xan.lianjia.com/zufang/">雄安新区租房</a></li>
                          <li><a href="https://cq.lianjia.com/zufang/">重庆租房</a></li>
                          <li><a href="https://tj.lianjia.com/zufang/">天津租房</a></li>
                          <li><a href="https://ganzhou.lianjia.com/zufang/">赣州租房</a></li>
                          <li><a href="https://yt.lianjia.com/zufang/">烟台租房</a></li>
                          <li><a href="https://huzhou.lianjia.com/zufang/">湖州租房</a></li>
                          <li><a href="https://hui.lianjia.com/zufang/">惠州租房</a></li>
                          <li><a href="https://ms.lianjia.com/zufang/">眉山租房</a></li>
                          <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                          <li><a href="https://qd.lianjia.com/zufang/">青岛租房</a></li>
                          <li><a href="https://zjk.lianjia.com/zufang/">张家口租房</a></li>
                          <li><a href="https://jx.lianjia.com/zufang/">嘉兴租房</a></li>
                          <li><a href="https://dd.lianjia.com/zufang/">丹东租房</a></li>
                          <li><a href="https://yy.lianjia.com/zufang/">岳阳租房</a></li>
                          <li><a href="https://xa.lianjia.com/zufang/">西安租房</a></li>
                          <li><a href="https://nanchong.lianjia.com/zufang/">南充租房</a></li>
                          <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                          <li><a href="https://km.lianjia.com/zufang/">昆明租房</a></li>
                          <li><a href="https://cq.lianjia.com/zufang/">重庆租房</a></li>
                          <li><a href="https://changzhou.lianjia.com/zufang/">常州租房</a></li>
                          <li><a href="https://san.lianjia.com/zufang/">三亚租房</a></li>
                          <li><a href="https://linyi.lianjia.com/zufang/">临沂租房</a></li>
                          <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                          <li><a href="https://ez.lianjia.com/zufang/">鄂州租房</a></li>
                          <li><a href="https://sx.lianjia.com/zufang/">绍兴租房</a></li>
                          <li><a href="https://ks.lianjia.com/zufang/">昆山租房</a></li>
                          <li><a href="https://tj.lianjia.com/zufang/">天津租房</a></li>
                          <li><a href="https://jiujiang.lianjia.com/zufang/">九江租房</a></li>
                          <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                          <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                          <li><a href="https://wuhu.lianjia.com/zufang/">芜湖租房</a></li>
                          <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                          <li><a href="https://ty.lianjia.com/zufang/">太原租房</a></li>
                      </ul>
              </div>

      <div class="footer__bottom">
        <p>链家网（北京）科技有限公司 | 网络经营许可证 <a href="http://beian.miit.gov.cn">京ICP备16057509号</a> | &copy; Copyright &copy;2010-2020 链家网Lianjia.com版权所有</p>
        <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/lianjia/beian.png?_v=20200917160625398">京公网安备 11010802024019号</a>
      </div>

    </div>
  </div>
<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"title":"\u70ed\u95e8\u5546\u5708","city_id":330100,"abbr":"rmsq","source":"m","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/changqing1112\/","title":"\u957f\u5e86\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/nanxing\/","title":"\u5357\u661f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuxing\/","title":"\u590d\u5174\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/renhe2\/","title":"\u4ec1\u548c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wenyixilu\/","title":"\u6587\u4e00\u897f\u8def\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xixing\/","title":"\u897f\u5174\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yiqiao\/","title":"\u4e49\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jiande1\/","title":"\u5efa\u5fb7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jiubao\/","title":"\u4e5d\u5821\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wandaguangchang2\/","title":"\u4e07\u8fbe\u5e7f\u573a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/huanglong\/","title":"\u9ec4\u9f99\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gudang\/","title":"\u53e4\u8361\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/hemu\/","title":"\u548c\u7766\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xixi\/","title":"\u897f\u6eaa\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gongchenqiao\/","title":"\u62f1\u5bb8\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/feicuicheng1\/","title":"\u7fe1\u7fe0\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wulin11\/","title":"\u6b66\u6797\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/tianshui1\/","title":"\u5929\u6c34\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dajiangdong\/","title":"\u5927\u6c5f\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/caihongcheng\/","title":"\u5f69\u8679\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/huajiachi\/","title":"\u534e\u5bb6\u6c60\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/shenhua\/","title":"\u7533\u82b1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/sichoucheng1\/","title":"\u4e1d\u7ef8\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/hubin1\/","title":"\u6e56\u6ee8\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jianqiao\/","title":"\u7b15\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/banshan\/","title":"\u534a\u5c71\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/puyan\/","title":"\u6d66\u6cbf\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/santang\/","title":"\u4e09\u5858\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/sandun\/","title":"\u4e09\u58a9\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gouzhuang\/","title":"\u52fe\u5e84\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yanjiangbei\/","title":"\u6cbf\u6c5f\u5317\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gudang\/","title":"\u53e4\u8361\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/huochedongzhan\/","title":"\u706b\u8f66\u4e1c\u7ad9\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yiqiao\/","title":"\u4e49\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xiongzhenlou\/","title":"\u96c4\u9547\u697c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dingqiao\/","title":"\u4e01\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jinjiang1\/","title":"\u8fd1\u6c5f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/liangzhu\/","title":"\u826f\u6e1a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/deshengdong\/","title":"\u5fb7\u80dc\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuyang1\/","title":"\u5bcc\u9633\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/daguan\/","title":"\u5927\u5173\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/heping2\/","title":"\u548c\u5e73\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xuejun\/","title":"\u5b66\u519b\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/linpu\/","title":"\u4e34\u6d66\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/tonglushangquan\/","title":"\u6850\u5e90\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/zhanongkou\/","title":"\u95f8\u5f04\u53e3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jialv\/","title":"\u5609\u7eff\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jingfang1\/","title":"\u666f\u82b3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dajiangdong\/","title":"\u5927\u6c5f\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/santang\/","title":"\u4e09\u5858\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wenyixilu\/","title":"\u6587\u4e00\u897f\u8def\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xianlin1\/","title":"\u95f2\u6797\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yanjiangnan\/","title":"\u6cbf\u6c5f\u5357\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuxing\/","title":"\u590d\u5174\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jinshahu\/","title":"\u91d1\u6c99\u6e56\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/liuxia1\/","title":"\u7559\u4e0b\u79df\u623f"}]},{"title":"\u63a8\u8350\u5c0f\u533a","city_id":330100,"abbr":"tjxq","source":"m","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820022260637977\/","title":"\u5927\u901a\u8def98\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641307\/","title":"\u5609\u7eff\u798f\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636713\/","title":"\u548c\u7766\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820022037245901\/","title":"\u89e3\u653e\u8def8\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820024445699943\/","title":"\u6c34\u5cb8\u946b\u57df\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641703\/","title":"\u5609\u7eff\u6587\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815909850746844\/","title":"\u5c0f\u6cb3\u4e1c\u6cb3\u4e0b66-11\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815440795176902\/","title":"\u6c38\u6cf0\u540d\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636393\/","title":"\u4e94\u6d0b\u4e1c\u6e56\u6625\u5929\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641388\/","title":"\u6b66\u6797\u95e8\u65b0\u6751\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815732752026627\/","title":"\u4f51\u5723\u89c2\u8def5\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043638833\/","title":"\u4e91\u5cf0\u4e00\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820023393475872\/","title":"\u4fdd\u5229\u878d\u4fe1\u5927\u56fd\u749f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639425\/","title":"\u5e7f\u666f\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043638496\/","title":"\u88d5\u56ed\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636559\/","title":"\u6e56\u5885\u5317\u8def101\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641404\/","title":"\u7d2b\u91d1\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641620\/","title":"\u91d1\u6c99\u66f2\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820023902308543\/","title":"\u73af\u57ce\u4e1c\u8def240\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820022536418987\/","title":"\u91d1\u9685\u7a7a\u6e2f\u516c\u9986\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815710271606474\/","title":"\u7eff\u91ce\u6e05\u98ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640426\/","title":"\u78a7\u6842\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641555\/","title":"\u7b51\u54c1\u91d1\u5ea7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043637400\/","title":"\u5927\u5173\u4e1c\u516d\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636769\/","title":"\u6c88\u5927\u5317\u82d1\u5c0f\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043642186\/","title":"\u5929\u6c34\u5df7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043642200\/","title":"\u706f\u5854\u4e1c\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636635\/","title":"\u77f3\u6cb9\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639517\/","title":"\u8054\u5408\u683c\u91cc\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043635924\/","title":"\u77e5\u672c\u5927\u53a6\u79df\u623f"}]},{"title":"\u79df\u623f\u57ce\u5e02","city_id":330100,"abbr":"zfcs","source":"m","children":[{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/linyi.lianjia.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/huzhou.lianjia.com\/zufang\/","title":"\u6e56\u5dde\u79df\u623f"},{"url":"https:\/\/wuhu.lianjia.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/nanchong.lianjia.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/xa.lianjia.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/gz.lianjia.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/san.lianjia.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/sjz.lianjia.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/xc.lianjia.com\/zufang\/","title":"\u8bb8\u660c\u79df\u623f"},{"url":"https:\/\/zj.lianjia.com\/zufang\/","title":"\u9547\u6c5f\u79df\u623f"},{"url":"https:\/\/baoji.lianjia.com\/zufang\/","title":"\u5b9d\u9e21\u79df\u623f"},{"url":"https:\/\/yc.lianjia.com\/zufang\/","title":"\u76d0\u57ce\u79df\u623f"},{"url":"https:\/\/zz.lianjia.com\/zufang\/","title":"\u90d1\u5dde\u79df\u623f"},{"url":"https:\/\/dd.lianjia.com\/zufang\/","title":"\u4e39\u4e1c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/","title":"\u4e0a\u6d77\u79df\u623f"},{"url":"https:\/\/wf.lianjia.com\/zufang\/","title":"\u6f4d\u574a\u79df\u623f"},{"url":"https:\/\/ts.lianjia.com\/zufang\/","title":"\u5510\u5c71\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/liangshan.lianjia.com\/zufang\/","title":"\u51c9\u5c71\u79df\u623f"},{"url":"https:\/\/gy.lianjia.com\/zufang\/","title":"\u8d35\u9633\u79df\u623f"},{"url":"https:\/\/dazhou.lianjia.com\/zufang\/","title":"\u8fbe\u5dde\u79df\u623f"},{"url":"https:\/\/hanzhong.lianjia.com\/zufang\/","title":"\u6c49\u4e2d\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/wh.lianjia.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/xan.lianjia.com\/zufang\/","title":"\u96c4\u5b89\u65b0\u533a\u79df\u623f"},{"url":"https:\/\/cq.lianjia.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/tj.lianjia.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/ganzhou.lianjia.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/yt.lianjia.com\/zufang\/","title":"\u70df\u53f0\u79df\u623f"},{"url":"https:\/\/huzhou.lianjia.com\/zufang\/","title":"\u6e56\u5dde\u79df\u623f"},{"url":"https:\/\/hui.lianjia.com\/zufang\/","title":"\u60e0\u5dde\u79df\u623f"},{"url":"https:\/\/ms.lianjia.com\/zufang\/","title":"\u7709\u5c71\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/qd.lianjia.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/zjk.lianjia.com\/zufang\/","title":"\u5f20\u5bb6\u53e3\u79df\u623f"},{"url":"https:\/\/jx.lianjia.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/dd.lianjia.com\/zufang\/","title":"\u4e39\u4e1c\u79df\u623f"},{"url":"https:\/\/yy.lianjia.com\/zufang\/","title":"\u5cb3\u9633\u79df\u623f"},{"url":"https:\/\/xa.lianjia.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/nanchong.lianjia.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/km.lianjia.com\/zufang\/","title":"\u6606\u660e\u79df\u623f"},{"url":"https:\/\/cq.lianjia.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/changzhou.lianjia.com\/zufang\/","title":"\u5e38\u5dde\u79df\u623f"},{"url":"https:\/\/san.lianjia.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/linyi.lianjia.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/ez.lianjia.com\/zufang\/","title":"\u9102\u5dde\u79df\u623f"},{"url":"https:\/\/sx.lianjia.com\/zufang\/","title":"\u7ecd\u5174\u79df\u623f"},{"url":"https:\/\/ks.lianjia.com\/zufang\/","title":"\u6606\u5c71\u79df\u623f"},{"url":"https:\/\/tj.lianjia.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/jiujiang.lianjia.com\/zufang\/","title":"\u4e5d\u6c5f\u79df\u623f"},{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/wuhu.lianjia.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/ty.lianjia.com\/zufang\/","title":"\u592a\u539f\u79df\u623f"}]}]))
</script>

</body>
<!-- 登录弹窗sdk -->
<script src="https://s1.ljcdn.com/clogin/js/pcLogin.js"></script>
<script src="https://s1.ljcdn.com/captcha-js-sdk-v2/captcha.js"></script>

<script>
  BeikeLoginSDK.config({
    env: 'prod', 
    loginCallback: function(){
      location.reload()
    },
    registerCallback: function(){
      location.reload()
    }
  })
</script>

<!--动态脚本内容-->

<!-- 页面IM相关配置内容 -->


<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      }
</script>

<!-- 设备指纹接入 -->
<script>
  window['__abbaidu_2011_subidgetf'] = function () {
    var subid = 110200;
    return subid;
  }
</script>
<script>
  window['__abbaidu_2011_cb'] = function (responseData) {
    var fpStr = JSON.stringify({
      t: responseData,
      r: location.href,
      os: 'web',
      v: '0.1'
    })
    var fpBase = window.btoa(fpStr)
    document.cookie = "srcid=" + fpBase +';path=/';
  };
</script>
<script async="" src="https://dlswbr.baidu.com/heicha/mw/abclite-2011-s2.js"></script><!-- 百度seo自动推送代码 -->
<script>
  (function(){var canonicalURL,curProtocol;var x=document.getElementsByTagName("link");if(x.length>0){for(i=0;i<x.length;i++){if(x[i].rel.toLowerCase()=="canonical"&&x[i].href){canonicalURL=x[i].href}}}if(!canonicalURL){curProtocol=window.location.protocol.split(":")[0]}else{curProtocol=canonicalURL.split(":")[0]}if(!canonicalURL){canonicalURL=window.location.href}!function(){var e=/([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r=canonicalURL,t=document.referrer;if(!e.test(r)){var n=(String(curProtocol).toLowerCase()==="https")?"https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif":"//api.share.baidu.com/s.gif";t?(n+="?r="+encodeURIComponent(document.referrer),r&&(n+="&l="+r)):r&&(n+="?l="+r);var i=new Image;i.src=n}}(window)})();
</script>

<!-- 落地时间因子 -->
<script type="application/ld+json">
  {
    "@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
    "@id": "https%3A%2F%2Fhz.zu.lianjia.com%2Fzufang",
    "appid": "1597146525691227",
    "pubDate": "2020-09-22T19:20:33",
    "upDate": "2020-09-22T19:20:33"
  }
</script>


<!-- 页面依赖JS加载 -->

<!-- common.js线上引入灯塔 -->
  <script type="text/javascript" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/common.js?_v=20200917160625398" crossorigin="anonymous"></script>

<script>
  var __basePath = 'https://s1.ljcdn.com/matrix_pc/dist/pc/src?_v=20200917160625398'.split("?") || [];
  require.config({
    //baseUrl: __basePath[0],
    paths: {
    },
    urlArgs:  __basePath[1],
    crossorigin: Boolean('1') //线上环境加该属性,需要再amd.js中单独配置一下
  });
  var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_pc\/dist\/pc","version":"20200917160625398","js_ns":"m_pages_zufangSearch","cur_city_id":"330100","cur_city_name":"\u676d\u5dde","cur_city_short":"hz"}
  ;;(function() {
    for(var i = 0, len = __requireList.length; i < len; i++) {
      var item = __requireList[i]
      item = item.split("?")[0]
      require([item], function(engine) {
        engine.init()
      })
    }
  })()
</script>

<!-- 埋点配置文件 -->

<script>
window.__UDL_CONFIG = window.__UDL_CONFIG || {}
window.__UDL_CONFIG.pid = window.__UDL_CONFIG.pid || "matrixpc"
window.__UDL_CONFIG.env = ('prod' === 'prod' ? "lianjia" : 'test')
window.__UDL_CONFIG["ljweb_channel_key"] = g_conf.pageId || ''

var _script = document.createElement('script')
_script.type = 'text/javascript'
// 该属性是为了配合接入灯塔，所有script标签都需加的属性
_script.setAttribute('crossorigin', 'anonymous')
document.getElementsByTagName('head')[0].appendChild(_script)
if(window.__UDL_CONFIG.env === 'test'){
  _script.src='//s1.rent39.internal.lianjia.com/matrix_pc/dist/pc/third/dig.js?' + __basePath[1]
}else{
  _script.src='//s1.ljcdn.com/matrix_pc/dist/pc/third/dig.js?' + __basePath[1]
}
</script>

</html>


Process finished with exit code 0

'''
doc = etree.HTML(txt)

pat = '<a class="twoline" target="_blank" href="(.*)">'
'.*</a>'
# a = re.findall(pat,txt)
# print(a)


txt1 = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/链家.py"
<Response [200]>
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Content-language" content="zh-CN" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="applicable-device" content="pc">
  <meta http-equiv="Cache-Control" content="no-transform " />

  <!-- seo关键字相关信息 -->
  <meta name="description" content="贝壳杭州租房网,提供整租·柏悦公馆 1室1厅 南出租房源信息,此房源位于杭州江干丁桥的柏悦公馆,1室38㎡2250元.找租房房源,就来杭州贝壳租房!">
  <meta name="keywords" content="整租·柏悦公馆 1室1厅 南,柏悦公馆租房信息,杭州江干丁桥房屋出租">
  <title>整租·柏悦公馆 1室1厅 南-柏悦公馆租房信息-杭州柏悦公馆丁桥房屋出租【杭州贝壳租房】</title>

  

  <!--地址信息-->
  <meta name="location" content="province=浙江;city=杭州">

  <!-- 网站ico图标 -->
    <link href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/lianjia/favicon.ico?_v=20200917160625398" type="image/x-icon" rel="icon">

    <meta name=""mobile-agent content="format=[wml|xhtml|html5];url=https://m.ke.com/chuzu/hz/zufang/zufang/HZ2298569620442841088.html" />
  <link rel="alternate" media="only screen and (max-width:640px)" href="https://m.ke.com/chuzu/hz/zufang/zufang/HZ2298569620442841088.html">
  
    <!-- 是否需要加载common.css -->
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/css/common.css?_v=20200917160625398">
  
  <!-- 载入灯塔 -->
  <!-- 接入灯塔 -->
<script src='//s1.ljcdn.com/link-static/resource/plat_framework/fee/js/1.4.0/index.js' crossorigin="anonymous"></script>
<script>
  // 获取cookie信息
  function getCookie(name){
    var cookies=document.cookie.split('; ');
    for(var i=0;i<cookies.length;i++){
      var crumb=cookies[i].split('=');
      if(name===crumb[0]){
        return crumb[1]
      }
    }
    return ''
  }
  // 灯塔加载完成后的回调函数
  ;;(function DT(){
    var uuid=getCookie('lianjia_uuid')
    window.dt && dt.set({
      pid: 'rent_fe_pc', // [必填]项目id, 由灯塔项目组统一分配
      uuid: uuid,
      ucid: uuid, // [可选]用户ucid, 用于发生异常时追踪用户信息, 一般在cookie中可以取到, 没有可传空字符串
      is_test: Boolean(''), // 是否为测试数据, 默认为false(测试模式下打点数据仅供浏览, 不会展示在系统中)
      record: {
        time_on_page: true, // 是否监控用户在线时长数据, 默认为true
        performance: true, // 是否监控页面载入性能, 默认为true
        js_error: true, //  是否监控页面报错信息, 默认为true
        // 配置需要监控的页面报错类别, 仅在js_error为true时生效, 默认均为true(可以将配置改为false, 以屏蔽不需要上报的错误类别)
        js_error_report_config: {
          ERROR_RUNTIME: true, // js运行时报错
          ERROR_SCRIPT: true, // js资源加载失败
          ERROR_STYLE: true, // css资源加载失败
          ERROR_IMAGE: false, // 图片资源加载失败
          ERROR_AUDIO: true, // 音频资源加载失败
          ERROR_VIDEO: true, // 视频资源加载失败
          ERROR_CONSOLE: false, // vue运行时报错
          ERROR_TRY_CATCH: true,
          checkErrorNeedReport: function(desc, stack){
            // 外网内容不上报
            if (!/\/\/(s1\.ljcdn\.com\/)/.test(desc) && !/\/\/(s1\.ljcdn\.com\/)/.test(stack)) {
              return false;
            }

            // 是否上报错误，默认为上报
            var needReport = true

            // 报错是否是从IMSDK中报出的
            var isThrowFromIM = (desc.indexOf('web-im-sdk') > -1)

            // desc 命中以下关键字的其中一个，即过滤掉，不上报错误，注： 从从IMSDK中报出的（第一类）
            var filterStr = ['未登录', '/msg/sync ajax fail', '登录令牌缺失', 'Session服务出错']

            // desc 命中以下关键字的其中一个，即可过滤掉，不上报信息，注： 并不是从从IMSDK中报出的（第二类）
            var filterStr2 = ['MyAppGetHTMLElementsAtPoint', 'vivoNewsDetailPage', 'Script error']

            //是否在desc中命中了关键字符串
            var hitKeyStr = false // 第一类
            var hitKeyStr2 = false // 第二类

            var i = 0, len = filterStr.length;
            for(; i < len; i++){
              if(desc.indexOf(filterStr[i]) > -1){
                hitKeyStr = true
                break
              }
            }

            var j = 0, len2 = filterStr2.length;
            for(; j < len2; j++){
              if(desc.indexOf(filterStr2[j]) > -1){
                hitKeyStr2 = true
                break
              }
            }

            // 错误是从IM中抛出，并且错误信息包含登录等内容时,或者命中第二类关键词，过滤掉，不上报
            if((isThrowFromIM && hitKeyStr) || hitKeyStr2){
              needReport = false
            }

            return needReport
          }
        }
      },
      version: '1.0.0',
      getPageType: function (location) {
        return location.host + location.pathname
      }
    })
  })()
</script>

    <!-- 载入后台返回的css文件 -->
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/page/detail/index.css?_v=20200917160625398">
    <!-- 载入后台返回的css文件 -->
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/module/send_message/index.css?_v=20200917160625398">
  
      <!-- 载入链家相关皮肤 -->
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/css/lianjia.css?_v=20200917160625398">
  
  <!-- 预置全局变量 -->
  <script>
    var g_conf = {}
  </script>
</head>

<body>

  <!-- 载入低版本浏览器样式 -->
  <style>
  .browser__low{height:100%;overflow:hidden}.browser__low--wrapper,.browser__low--inner{display:none}.browser__low .browser__low--wrapper{position:absolute;left:0;right:0;top:0;bottom:0;z-index:199999;background:#000;opacity:.5;filter:alpha(opacity=50);display:block}.browser__low .browser__low--inner{background:#fff;position:absolute;left:50%;top:50%;z-index:19999999;width:360px;height:100px;margin-top:-90px;margin-left:-200px;padding:40px 20px;display:block}.browser__low .browser__low--inner p{font-size:20px;padding-bottom:40px}.browser__low .browser__low--inner a{display:inline-block;color:#fff;background:#2ab78e;padding:10px 6px}

</style>
<div class="browser__low--wrapper"></div>
<div class="browser__low--inner">
  <p>您的浏览器版本过低，请升级：</p>
  <a href="https://www.baidu.com/s?wd=chrome" target="_blank">谷歌 Chrome浏览器</a>
</div>
<script>
;;(function() {
  if(!([].forEach)) {
    document.body.className += ' browser__low'
  }
})()
</script>


  <div class="wrapper">
     <link href='//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' property='stylesheet' rel="stylesheet">

<!-- 转换contact格式，从数组转成对象,用于统一存放页面[不同位置]的商机信息，如 dig_v, ucid, id 等  -->

<div>
  <!-- 引入公用的头、导航、搜索栏 -->
  <div class="header ">
  <ul class="header__wrapper w1150 clear typeUserInfo" id="top">
                      <li class="header__item fl" >
          <a href="//hz.lianjia.com" target="_blank">首页</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/ershoufang/" target="_blank">二手房</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.fang.lianjia.com/loupan/" target="_blank">新房</a>
        </li>
                        <li class="header__item fl cur" >
          <a href="/zufang/" target="_blank">租房</a>
        </li>
                        <li class="header__item fl" >
          <a href="//us.lianjia.com" target="_blank">海外</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/xiaoqu/" target="_blank">小区</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/jingjiren/" target="_blank">经纪人</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/wenda/" target="_blank">指南</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/fangjia/" target="_blank">房价</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.lianjia.com/tool.html" target="_blank">工具</a>
        </li>
                        <li class="header__item fl publish-house" data-event_id="20383">
          <a href="//hz.lianjia.com/yezhu/" target="_blank">发布房源</a>
        </li>
                  <li class="header__aside fr pointer typeShowUser" data-el="login" data-event_id="10794" data-event_action="target=login">
      <span data-el="login_box">
        <span data-el="btn_login" data-id="dialog_tel" class="btn-login">登录</span>/<span class="btn-resgiter" data-el="register" data-id="dialog_reg">注册</span>
      </span>
    </li>
    <li class="top__aside fr hide" data-el="user_box">
      <a href="" data-el="userName">18****87</a>
      <a data-el="logout_btn">退出</a>
      <div class="menu-pop">
        <i class="allow"></i>
        <ul class="menu-list lj">
          <li class="menu-item"><a href="/zufang/users/index?cur_type=attention" target="_blank">我的关注</a></li>
          <li class="menu-item"><a href="/zufang/users/index?cur_type=contact" target="_blank">最近联系</a></li>
          <li class="menu-item"><a href="/zufang/users/index?cur_type=scan" target="_blank">浏览记录</a></li>
        </ul>
      </div>
    </li>

  </ul>

</div>
  <div class="search__area">
  <div class="beike__nav">
  <a class="beike__nav--logo" href="/zufang/"></a>

  
  <ul class="beike__nav--tab">
    <li>
      <a 
        class="cur" 
        href="/zufang/" 
        data-event_id="25754" 
        exposure-event_id="25753" 
        exposure-event_action="click_name=首页" 
        data-event_action="click_name=首页" 
        data-event_position="click_name"
        exposure-event_position="click_name">首页</a>
    </li>

    <li>
      <a 
      class="" 
      href="/zufang/rt200600000001/" 
      data-event_id="25754" 
      exposure-event_id="25753" 
      exposure-event_action="click_name=整租" 
      data-event_action="click_name=整租" 
      data-event_position="click_name"
      exposure-event_position="click_name">整租</a>
    </li>

    <li>
      <a 
      class="" 
      href="/zufang/rt200600000002/" 
      data-event_id="25754" 
      exposure-event_id="25753" 
      exposure-event_action="click_name=合租" 
      data-event_action="click_name=合租" 
      data-event_position="click_name"
      exposure-event_position="click_name">合租</a></li>

    <li>
      <a 
      href="/zufang/proprietor/offer?city_id=330100&city_name=杭州&position=rent_pc_toptbar_rent" 
      data-event_id="25754" 
      exposure-event_id="25753" 
      exposure-event_action="click_name=发布房源" 
      data-event_action="click_name=发布房源" 
      data-event_position="click_name"
      exposure-event_position="click_name">发布房源</a></li>

    <!-- <li><a href="" data-event_id="25754" data-event_action="click_name=入驻公寓">公寓入驻</a></li> -->

            <li class="beike__nav--code">
      下载APP
      <div class="nav-list beike__nav--qrcode">

                  <img width="94" height="94" src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=right&amp;ljweb_channel_key=zufang_search" alt="下载链家APP">
        
      </div>
    </li>
        
  </ul>
</div>
  <div class="search w1150" id="search">
  <!-- <a class="search__logo" href="/"></a> -->
  <div class="search__wrap">
    <input class="search__input fl" type="text" data-el="input" placeholder="请输入区域、商圈或小区名开始找房" autocomplete="off" value="" data-value="">
    <span class="search__button fl" data-el="button" data-event_id="10800" data-event_send="no"></span>
  </div>

</div>  </div>
  <!-- 房源有效时 -->
      <div class="content clear w1150">

      <!-- 房源标题 -->
      <p class="content__title">整租·柏悦公馆 1室1厅 南</p>

      <!-- 房源副标题 -->
      <div class="content__subtitle">
        房源维护时间：2020-09-14        <!-- 发布人、发布机构入口 -->
        
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100001610 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title=""
  data-type="house"
  data-appoint-uc-id="1000000026652402"
></div>
          
                 
         
         
        <span class="tel_complaint" style="margin-right: 6px;">链家官方投诉电话：10109666</span>
        <br/>
                  <i class="house_code">房源编号：HZ2298569620442841088</i>
        
      </div>

      <div class="content__core">

        <!-- 房源图片轮播图 -->
        <div class="content__article__slide" id="mySwipe">

          <!-- 房源大图 -->
          <ul class="content__article__slide__wrapper">
          <!-- 如果有vr图片 -->
                                            <div class="content__article__slide__item" data-el="slideItem">
                                <img alt="整租·柏悦公馆 1室1厅 南" src="https://image1.ljcdn.com/lease-image/house/17481878-0a80-477b-82c1-f5b7544dec73.jpg.780x439.jpg" data-el="lazy-img" data-src="https://image1.ljcdn.com/lease-image/house/17481878-0a80-477b-82c1-f5b7544dec73.jpg.780x439.jpg" data-type="202000000101" data-name="卧室"/>
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租·柏悦公馆 1室1厅 南" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/565-319.png?_v=20200917160625398" data-el="lazy-img" data-src="https://image1.ljcdn.com/lease-image/house/77cb396b-904e-4a0a-b68d-9694bf1c5ce3.jpg.780x439.jpg" data-type="202000000201" data-name="客厅" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租·柏悦公馆 1室1厅 南" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/565-319.png?_v=20200917160625398" data-el="lazy-img" data-src="https://image1.ljcdn.com/lease-image/house/120ef5d6-a78f-4e84-af80-15eefbc47c34.jpg.780x439.jpg" data-type="202000000300" data-name="厨房" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租·柏悦公馆 1室1厅 南" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/565-319.png?_v=20200917160625398" data-el="lazy-img" data-src="https://image1.ljcdn.com/lease-image/house/11e24eb5-b540-463b-b8e2-05862a57104c.jpg.780x439.jpg" data-type="202000000400" data-name="卫生间" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租·柏悦公馆 1室1厅 南" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/565-319.png?_v=20200917160625398" data-el="lazy-img" data-src="https://image1.ljcdn.com/lease-image/house/482e54ea-5844-4d5b-91b1-c480fb77390a.jpg.780x439.jpg" data-type="202000000500" data-name="户型图" />
                          </div>
                                          </ul>

          <!-- 房源缩略图 -->
          <div class="content__thumb--box">

            <ul class="content__article__slide--small content__article__slide_dot" data-el="prefix" id="prefix">
                                                              <li class="active" data-index="0">
                    <img src="https://image1.ljcdn.com/lease-image/house/17481878-0a80-477b-82c1-f5b7544dec73.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="1">
                    <img src="https://image1.ljcdn.com/lease-image/house/77cb396b-904e-4a0a-b68d-9694bf1c5ce3.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="2">
                    <img src="https://image1.ljcdn.com/lease-image/house/120ef5d6-a78f-4e84-af80-15eefbc47c34.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="3">
                    <img src="https://image1.ljcdn.com/lease-image/house/11e24eb5-b540-463b-b8e2-05862a57104c.jpg.126x86.jpg">
                  </li>
                                  <li class="" data-index="4">
                    <img src="https://image1.ljcdn.com/lease-image/house/482e54ea-5844-4d5b-91b1-c480fb77390a.jpg.126x86.jpg">
                  </li>
                                                        </ul>
          </div>

          <!-- 图片切换按钮 -->
          <span class="content__article__slide--prev" data-el="prev"></span>
          <span class="content__article__slide--next" data-el="next"></span>
          <span class="content__article__slide__item__num"><i>1</i>/5</span>
        </div>

        <!-- 右侧黄金展位 -->
        <div class="content__aside fr" id="aside">

          <!-- 租金及支付方式 -->
          <div class="content__aside--title">
            <span>2250</span>元/月
            (季付价)            <div class="operate-box">
              <div class="operate-item share">
                <span class="qrcode-h5" id="share"><!-- <img src="https://image1.ljcdn.com/params-compact/5c0134394b38a079574d308314343f1d.jpeg"> --></span>
                <span class="icon wechat"></span> 分享
              </div>

              <!-- 房源关注入口及hover浮层 -->
              <div class="operate-item">
                <span class="watch-tips hide detail" data-el="getApp">关注的房源请在链家APP中查看</span>
                <!-- <div class="attention-pop" data-el="getApp">
                  <div class="inner">

                  </div>
                </div> -->
                <span 
                  class="watch-btn" 
                  data-type="house" 
                  data-id="HZ2298569620442841088" 
                  data-el="checkWatch"
                  data-event_id="10801"
                  data-event_action="house_code=HZ2298569620442841088&status=1">
                  <i class="heart"></i>
                  <span>关注</span>
                </span>

              </div>
            </div>
          </div>

          <!-- 房源标签列表 -->
          <p class="content__aside--tags">
                                      <i class="content__item__tag--is_key" data-class="is_key">随时看房</i>
                      </p>

          <!-- 房源户型、朝向、面积、租赁方式 -->
          <ul class="content__aside__list">
            <li><span class="label">租赁方式：</span>整租</li>
            <li><span class="label">房屋类型：</span>1室1厅1卫 38㎡</li>
            <li class="floor"><span class="label">朝向楼层：</span><span class="">南 低楼层/16层</span>
                          </li>
            <li><span class="label">风险提示：</span><a href="https://m.lianjia.com/text/disclaimer">用户风险提示</a></li>
          </ul>

          <!-- 经纪人信息 -->
          
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100000192 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title=""
  data-type="house"
  data-appoint-uc-id=""
><style></style>	<div style="width: 0;height: 0;" class="ke-agent-data" data-agent='{"agentDomain":"OTHER","agentProofList":[],"agentToken":"1308371986696638473","allCustomerCount":5,"allDealCount":0,"allVisitCount":0,"answerCount":0,"avatar":"https://img.ljcdn.com/usercenter/images/uc_ehr_avatar/55497045-1654-41ed-9d30-4e0fc9d2a8ee.jpg.480x640.jpg","brand":"链家","brandCode":"2","commentCount":0,"compFullName":"杭州链家事业部","compName":"杭州链家事业部","dianpuUrl":"https://dianpu.lianjia.com/1000000026652402","digV":"{\"u\":1000000026652402,\"v\":\"V3\",\"s\":\"NATURAL\",\"adId\":100000192,\"flow\":\"natural\",\"b\":\"HouseHostingBuilder\",\"p\":\"\",\"g\":\"\",\"rid\":\"5233487946585710944\",\"sid\":\"103103783178_1000000026652402\"}","feedbackScore":5.0,"flowType":"natural","imQualified":0,"imRate":0.273,"jobTitle":"助理经纪人","keQuality":213,"levelLabel":"","levelLabelUrl":"","majorBizcircle":"","majorDistrict":"","mobile":"","mobileType":"AGENT","name":"江尚霖","nhProperty":{"lastThirtyCust":0,"lastThirtyVisit":0,"allDealCount":0},"officeAddress":"330100","officeAddressName":"杭州","orgProofList":[],"phoneQualified":1,"phoneRate":0.0,"politicalCode":"","politicalName":"","port":"shangyehua_rent_house_info","positionCode":"785","positionName":"综合经纪人","primaryProof":{},"proofComplete":false,"reason":"我是房源托管人，对房源最了解","rentProperty":{"allDealCount":0},"responseRate":0.273,"school":"浙江师范大学","sellProperty":{"allDealCount":0},"seniority":"1年以内","shopCode":"H13589","shopName":"服务支持部","showingCount":0,"source":"NATURAL","specialtyList":["贝壳分一般"],"ucId":"1000000026652402","usefulAnswerCount":0,"usefulCount":0,"userCode":"26652402","vipLevel":0}'></div>
    <div class="content__aside__list house-detail">
    	<span class="content__aside__list--icon" style="background-image: url(https://img.ljcdn.com/usercenter/images/uc_ehr_avatar/55497045-1654-41ed-9d30-4e0fc9d2a8ee.jpg.480x640.jpg);"></span>
        <div class="content__aside__list--title oneline">
        	<span class="contact_name" title="江尚霖">江尚霖</span> 
                    </div>
        <p class="content__aside__list--subtitle oneline">
         	                                        链家 经纪人
                    </p>
     	<div class="phone__hover--wrapper">
        	<div class="content__aside__list--bottom oneline phone num ke-agent-sj-phone ke-agent-sj-phone-100000192 ke-agent-sj-phone-1000000026652402" id="phone1">
            	                	电话咨询
                            </div>
            <span class="contact__im im__online ke-agent-sj-im ke-agent-sj-im-100000192 ke-agent-sj-im-1000000026652402" data-port="pc_lianjia_zufangplat_detail_house" data-digv='{"u":1000000026652402,"v":"V3","s":"NATURAL","adId":100000192,"flow":"natural","b":"HouseHostingBuilder","p":"","g":"","rid":"5233487946585710944","sid":"103103783178_1000000026652402"}'> 在线咨询 </span>
        </div>
    </div>
</div>
            
            <div class="xcx-phone">
              <img src="https://image1.ljcdn.com/params-compact/fa4347308247fb70e61901206f222b62.jpeg">
              <p>免费拨打无骚扰</p>
            </div>
                  </div>
      </div>

      <div class="content__detail">
        <div id="baseInfo" style="height: 1px;margin: 0; padding:0; background: transparent"></div>
        <ul class="w1150 nav__tab fixednav" id="fixed">
          <li class="cur" data-el="fixedNavItem" data-event_id="26125" data-event_action="pcdetailtoptab=0" data-event_position="pcdetailtoptab" data-href="info">房屋信息</li>
                    <li data-el="fixedNavItem" data-event_id="26125" data-event_action="pcdetailtoptab=1" data-event_position="pcdetailtoptab" data-href="desc">房源描述</li>
                              <li data-el="fixedNavItem" data-event_id="26125" data-event_action="pcdetailtoptab=2" data-event_position="pcdetailtoptab" data-href="cost">费用详情</li>
                              <li data-el="fixedNavItem" data-event_id="26125" data-event_action="pcdetailtoptab=4" data-event_position="pcdetailtoptab" data-href="around">位置周边</li>
          <li data-el="fixedNavItem" data-event_id="26125" data-event_action="pcdetailtoptab=5" data-event_position="pcdetailtoptab" data-href="nearbyList">附近房源</li>
          <li data-el="fixedNavItem" data-event_id="26125" data-event_action="pcdetailtoptab=6" data-event_position="pcdetailtoptab" data-href="recom">推荐房源</li>
                    <li class="fixed-contact">
            
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100010585 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title=""
  data-type="house"
  data-appoint-uc-id="1000000026652402"
></div>
            <!-- <span class="phone">电话咨询</span> -->
            <span class="appoint" data-el="appointHouse" exposure-event_id="34988" exposure-event_action="event=Web元素曝光" data-event_id="34991" data-event_action="Web元素点击">预约看房</span>
          </li>
                  </ul>
        <!-- 房源左侧内容 -->
        <div class="content__article fl">
          <div class="report__house">
            <img src="https://image1.ljcdn.com/rent-front-image/ea4f955b555dc13dd6364436691d1f77.1522402869543_d5ac046b-21a1-465a-9a26-628065c9ae84">
            <a href="/zufang/truehouse/content" target="_blank">真实存在，真实在租，真实价格，假一赔百<i class="icon"></i></a>
            <span class="content-right" data-el="showReportBox" data-event_id="10804" data-event_action="house_code=HZ2298569620442841088">我要举报</span>
          </div>

          <!-- 房源基本信息 -->
          <div class="content__article__info" id="info">
            <h3 id="info">房屋信息</h3>
            <ul>
              <li class="fl oneline">基本信息</li>
                              <li class="fl oneline">面积：38㎡</li>
                                              <li class="fl oneline">朝向：南</li>
                                  <li class="fl oneline">&nbsp;</li>
                                              <li class="fl oneline">维护：8天前</li>
                                              <li class="fl oneline">入住：随时入住</li>
                                  <li class="fl oneline">&nbsp;</li>
                                              <li class="fl oneline">楼层：低楼层/16层</li>
                                              <li class="fl oneline">电梯：有</li>
                                  <li class="fl oneline">&nbsp;</li>
                                              <li class="fl oneline">车位：暂无数据</li>
                                              <li class="fl oneline">用水：商水</li>
                                  <li class="fl oneline">&nbsp;</li>
                                              <li class="fl oneline">用电：商电</li>
                                              <li class="fl oneline">燃气：有</li>
                                  <li class="fl oneline">&nbsp;</li>
                                              <li class="fl oneline">采暖：自采暖</li>
                                          </ul>
            <ul>
              <li class="fl oneline"></li>
              <li class="fl oneline">租期：暂无数据</li>
              <li class="fl oneline">
                
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100001513 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title="请问最短可以租多久？"
  data-type="house"
  data-appoint-uc-id=""
></div>
                &nbsp;
              </li>
              <li class="fl oneline"></li>
              <li class="fl oneline">看房：随时可看</li>
              <li class="fl oneline">
                
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100001517 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title="请问什么时间可以看房？"
  data-type="house"
  data-appoint-uc-id=""
></div>
              &nbsp;</li>
            </ul>
          </div>

          <!-- 房源分割标识线，js里用到，勿删 -->
          <div class="info__line line"></div>

          <!-- 配套设施列表 -->
          <ul class="content__article__info2">
            <li class="fl oneline">配套设施</li>
                          <li class="fl oneline facility_no ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ff28f17d82337aaa2cbdcd44ad1bda4c.1524906571057_0c1a2541-7e92-4557-92d0-7588846918d1);"></i>
                洗衣机              </li>
                          <li class="fl oneline  ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/2c5080db6cb434413d39fe816faddafe.1524906138308_77f21b82-5983-4448-8348-ef9346263338);"></i>
                空调              </li>
                          <li class="fl oneline  ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/b024f9fdd5797563ead74f237105fd5a.1524906626107_4b1c45fe-0266-40af-b39c-6311887b0aaa);"></i>
                衣柜              </li>
                          <li class="fl oneline facility_no ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/8705ff7fb13cf9fabdc2aed4ca0052c0.1524906061250_49197f72-e296-4eb7-b9c0-78e443675cfa);"></i>
                电视              </li>
                          <li class="fl oneline  ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/f01e63a2d0b36d2b6b92269dac7210a8.1524905973505_6a9e4bde-4acb-4699-ba93-32f4dc13304a);"></i>
                冰箱              </li>
                          <li class="fl oneline  ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/82e5b44b21844b608071ac426a5eb7e6.1524906411157_ae925a22-d95e-48bf-975c-447a27dd4ce9);"></i>
                热水器              </li>
                          <li class="fl oneline  ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/c40aee40a80ebcaa8d716a2c9ae14391.1524906024762_ac4fb64e-8467-46de-b6f5-7f9ba1ce2622);"></i>
                床              </li>
                          <li class="fl oneline facility_no ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ce93a6cec4a601367fbd8f5d8760ecc8.1525926673137_fa39878e-9033-4494-9912-13c176c060ca);"></i>
                暖气              </li>
                          <li class="fl oneline facility_no ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/c2e2d43d75f2158cf08fae1c4d2f433f.1524906202377_004ba35e-ce03-480f-bb0c-0acd46ebb1ce);"></i>
                宽带              </li>
                          <li class="fl oneline facility_no ">
                <i style="background-image: url(https://image1.ljcdn.com/rent-front-image/f0e67d57b15b3c47c4ee77847eef5b97.1524906489358_60a401ee-ee85-42eb-aaf3-5caaa5efc0a6);"></i>
                天然气              </li>
                      </ul>

          <div class="content__article__info3" id="desc">
            <h3>房源描述</h3>
            <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
            
            <!-- 房源经纪人 -->
            
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100001525 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title=""
  data-type="house"
  data-appoint-uc-id=""
></div>

            <!-- 房源描述 -->
                          <p data-el="houseComment" data-desc="【房源亮点】<br />
全新装修，可办公自住，地理位置优越，近大唐城、丁兰广场、物美，配套完善。<br />
<br />
【户型介绍】<br />
一房一厅一厨一卫，产证面积38方，朝北，平层，两梯八户，大开间。<br />
<br />
【装修描述】<br />
业主自住中装，家具家电齐全，房屋已经保洁干净，可办公、自住。<br />
<br />
【交通出行】<br />
留石高架及石大高架，B3到城战火车站，85到大关，81 99到景芳，218到武林广场，95到运河广场，B支2到政府大楼，272到文一路，386到临平。<br />
<br />
【周边配套】<br />
小区配套完善，出门即是大唐城、丁桥物美、丁兰广场，吃喝玩乐一应俱全。<br />
<br />
【小区介绍】<br />
该小区属于次新房公寓，40年产权，建于2012年，房龄新，地处丁桥。<br />
<br />
" class="threeline">【房源亮点】<br />
全新装修，可办公自住，地理位置优越，近大唐城、丁兰广场、物美，配套完善。<br />
<br />
【户型介绍】<br />
一房一厅一厨一卫，产证面积38方，朝北，平层，两梯八户，大开间。<br />
<br />
【装修描述】<br />
业主自住中装，家具家电齐全，房屋已经保洁干净，可办公、自住。<br />
<br />
【交通出行】<br />
留石高架及石大高架，B3到城战火车站，85到大关，81 99到景芳，218到武林广场，95到运河广场，B支2到政府大楼，272到文一路，386到临平。<br />
<br />
【周边配套】<br />
小区配套完善，出门即是大唐城、丁桥物美、丁兰广场，吃喝玩乐一应俱全。<br />
<br />
【小区介绍】<br />
该小区属于次新房公寓，40年产权，建于2012年，房龄新，地处丁桥。<br />
<br />
</p>
              <p class="detail__info--more" data-el="commentShowMore">查看更多<i class="more__icon up"></i></p>
            
            <!-- 房源图片 -->
                          <ul class="piclist" data-el="detail-pic">
                                  <li data-index="0">
                    <img src="https://image1.ljcdn.com/lease-image/house/17481878-0a80-477b-82c1-f5b7544dec73.jpg.780x439.jpg" alt="" data-type="202000000101" data-name="卧室"/>
                  </li>
                                  <li data-index="1">
                    <img src="https://image1.ljcdn.com/lease-image/house/77cb396b-904e-4a0a-b68d-9694bf1c5ce3.jpg.780x439.jpg" alt="" data-type="202000000201" data-name="客厅"/>
                  </li>
                                  <li data-index="2">
                    <img src="https://image1.ljcdn.com/lease-image/house/120ef5d6-a78f-4e84-af80-15eefbc47c34.jpg.780x439.jpg" alt="" data-type="202000000300" data-name="厨房"/>
                  </li>
                                  <li data-index="3">
                    <img src="https://image1.ljcdn.com/lease-image/house/11e24eb5-b540-463b-b8e2-05862a57104c.jpg.780x439.jpg" alt="" data-type="202000000400" data-name="卫生间"/>
                  </li>
                                  <li data-index="4">
                    <img src="https://image1.ljcdn.com/lease-image/house/482e54ea-5844-4d5b-91b1-c480fb77390a.jpg.780x439.jpg" alt="" data-type="202000000500" data-name="户型图"/>
                  </li>
                              </ul>
            
            <!-- 合租信息 -->
                      </div>

          <!-- 费用详情 -->
                      <div class="content__article__info3 cost_box" id="cost">
    <h3>费用详情
      
<div
  id=""
  class="ke-agent-sj-sdk component-agent-id-100001521 " 
  data-medium-id="100000032"
  data-house-code="103103783178"
  data-id="103103783178"
  data-resblock-id="1820027199512739"
  data-bizcircle-id=""
  data-station-id=""
  data-hdic-city-id="330100"
  data-title="请问可以优惠一些吗？"
  data-type="house"
  data-appoint-uc-id=""
></div>
    </h3>
            <div class="cost_content" data-el="costEl">
            <div class="price_title">
                <p class="title_info">年租价 当租期不足1年时租金可能会上浮，详询管家</p>
                            </div>
            <div class="table_wrapper " data-el="foldEl">
                <ul class="table_title">
                                        <li class="table_col">付款方式 <span class="sub_title"></span></li>
                                        <li class="table_col">租金 <span class="sub_title">(元/月)</span></li>
                                        <li class="table_col">押金 <span class="sub_title">(元)</span><img class="question_icon" data-desc="该房源押金包含：房屋押金" data-el="desc" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/detail/question@3x.png?_v=20200917160625398" alt=""></li>
                                        <li class="table_col">服务费 <span class="sub_title">( 元(一次收取))</span></li>
                                        <li class="table_col">中介费 <span class="sub_title">(元)</span></li>
                                   
                </ul>
                <div class="table_content">
                                            <ul class="table_row">
                            <li class="table_col font_gray">季付</li>
                            <li class="table_col font_orange">2250</li>
                            <li class="table_col">2250</li>
                            <li class="table_col">0</li>
                            <li class="table_col">1125</li>
                        </ul>
                                    </div>
            </div>
        </div>
        
    </div>
          
        </div>

        <div class="content__extend fr">
          <!-- 右侧fixed卡片 -->
          <div class="content__aside content__aside--fixed" id="asideFixed">

            <!-- 小程序二维码 -->
            <div class="flat-fix-qrCode">
              <div class="download">
  <div class="qr-code">
    <img width="94" height="94" src="https://image1.ljcdn.com/params-compact/5c0134394b38a079574d308314343f1d.jpeg" alt="贝壳小程序">
    <div class="title">扫描微信咨询</div>
  </div>
</div>
            </div>
          </div>
          
          <!-- 必看好房 -->
                    <div class="list-recommend" exposure-event_id="26151">
            <p>必看好房</p>
                          <div class="recommend-item">
                <a href="/zufang/HZ2377433314358468608.html" data-event_id="26152" data-event_action="rank_id=0">
                <img src="https://image1.ljcdn.com/110000-inspection/pc1_Dk7TiFLr9.jpg!m_fill,w_250,h_182,l_flianjia_black,o_auto" alt="">
                <p class="title">整租·丁桥景园南苑 2室2厅</p>
                                <p class="desc">丁桥 / 南 / 90㎡</p>
                                                <p class="price">2200元/月</p>
                                  <p class="tips">该小区低价抢手房</p>
                                </a>
              </div>
                          <div class="recommend-item">
                <a href="/zufang/HZ2541074949280366592.html" data-event_id="26152" data-event_action="rank_id=1">
                <img src="https://image1.ljcdn.com/110000-inspection/de0034dd-3d36-43e3-8999-6644fd5de9f9.jpg!m_fill,w_250,h_182,l_flianjia_black,o_auto" alt="">
                <p class="title">整租·城发云锦城 3室1厅</p>
                                <p class="desc">丁桥 / 南 / 89㎡</p>
                                                <p class="price">1800元/月</p>
                                  <p class="tips">该小区低价抢手房</p>
                                </a>
              </div>
                          <div class="recommend-item">
                <a href="/zufang/HZ2533427161986244608.html" data-event_id="26152" data-event_action="rank_id=2">
                <img src="https://image1.ljcdn.com/110000-inspection/1f3f3bec59b56622ef48fc4f1e221395-033.jpg!m_fill,w_250,h_182,l_flianjia_black,o_auto" alt="">
                <p class="title">整租·天阳明朗 3室2厅</p>
                                <p class="desc">丁桥 / 东南 / 90㎡</p>
                                                <p class="price">2600元/月</p>
                                  <p class="tips">该小区低价抢手房</p>
                                </a>
              </div>
                          <div class="recommend-item">
                <a href="/zufang/HZ2400455612346671104.html" data-event_id="26152" data-event_action="rank_id=3">
                <img src="https://image1.ljcdn.com/110000-inspection/pc1_Bk3CGopEe.jpg!m_fill,w_250,h_182,l_flianjia_black,o_auto" alt="">
                <p class="title">整租·丁桥颐景园 2室1厅</p>
                                <p class="desc">丁桥 / 南 / 74㎡</p>
                                                <p class="price">2800元/月</p>
                                </a>
              </div>
                          <div class="recommend-item">
                <a href="/zufang/HZ2553598897746345984.html" data-event_id="26152" data-event_action="rank_id=4">
                <img src="https://image1.ljcdn.com/110000-inspection/pc1_rvrE39J4b.jpg!m_fill,w_250,h_182,l_flianjia_black,o_auto" alt="">
                <p class="title">整租·城发云锦城 2室2厅</p>
                                <p class="desc">丁桥 / 南 / 87㎡</p>
                                                <p class="price">2400元/月</p>
                                  <p class="tips">该小区低价抢手房</p>
                                </a>
              </div>
                      </div>
                  </div>
       
      </div>
    </div>

    <!-- 房源地址与交通 -->
    <!-- 地址信息 -->
<div class="content__article__info4 w1150" id="around">
  <h3>地址和交通</h3>
  <ul class="nav_list" data-el="nav_list">
  </ul>
  <!-- 地图插件显示 -->
  <div class="content__map">
    <div id="map" class="content__map--container">
    </div>
  </div>
  <ul>
    </ul>
</div>
    
    <!-- 附近房源 -->
    <div class="content--recommend w1150">
        <div class="bottom w1150" id="nearbyList" data-el="recommend-module" exposure-event_id="26163"></div>
    </div>
    
    <!-- 推荐房源 -->
    <div class="content--recommend w1150">

      <!-- 推荐房源分割线 -->
      <p style="height: 1px;" id="recom"></p>
            <!-- 推荐房源 -->
      <div class="bottom w1150" id="recommendList" data-el="recommend-module" data-source="">
      </div>
    </div>

    <!-- 业主端-房源发布入口、下载二维码 -->
     
      <div class="bottom_entry w1150"  data-el="landlord_bottom" exposure-event_id="25418">
            <div class="title">我有房子要租</div>
            <div class="inner">
                              <a href="/zufang/proprietor/offer?city_id=330100&amp;city_name=杭州&amp;position=rent_pc_detail_rent"" 
                    class="landlord_entry" 
                                        data-event_id="25149">
                  <img src="http://image1.ljcdn.com/rent-front-image/5a13f1be8489fd02414fa6ce8f34dd4c.png" alt="" class="bg">
                  <p class="subtitle">把房源委托给链家</p>
                  <p class="desc">一键出租 快速匹配优质经纪人 收益稳定更省心</p>
                  <p class="btn">发布房源                                    </p>
                </a>
                              <a " 
                    class="landlord_entry" 
                                        data-event_id="25149">
                  <img src="http://image1.ljcdn.com/rent-front-image/2a155c77e723c1d5c7fbfb37a5b5db17.png" alt="" class="bg">
                  <p class="subtitle">已有房源在链家出租</p>
                  <p class="desc">去APP业主中心管理委托</p>
                  <p class="btn">去app管理委托房源                                    </p>
                </a>
                          </div>
      </div>
    
    <!-- 房源失效时兜底处理 -->
    <div class="appointment" data-el="appointPop">
    <div class="appointment-bg" data-el="appointClose"></div>
    <div class="appointment-content">
      <div class="appoint-close" data-el="appointClose"></div>
      <div class="title">我要预约</div>
      <div class="appoint-date">
        <p>看房日期</p>
        <ul data-el="appointDate">
          <li data-type="0">今天</li>
          <li data-type="1">明天</li>
          <li data-type="2">周末</li>
        </ul>
      </div>
      <div class="appoint-time">
        <p>看房时间</p>
        <ul data-el="appointTime">
          <li data-type="1" class="cur">全天</li>
          <li data-type="2">上午</li>
          <li data-type="3">下午</li>
          <li data-type="4">晚上</li>
        </ul>
      </div>
      <div class="appoint-btn" data-el="appointConfirm" data-event_id="34989" data-event_action="Web元素点击">立即预约</div>
    </div>
  </div>
  <div class="appoint-success" data-el="appointSuccess">
    <div class="success-bg" data-el="successClose"></div>
    <div class="success-content">
      <p class="title">预约成功</p>
      <p class="tips">经纪人确认后将与您联系，请保持电话通畅。<br/>您可以在贝壳APP/小程序「租房-心愿单」中查看预约信息</p>
      <div class="code">
        <div>
          <img src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/getDownloadQr.png" alt="下载app">
          <p>下载贝壳APP</p>
        </div>
        <div>
          <img src="https://image1.ljcdn.com/params-compact/9ec80e3ee4d8ddf0f1397f718553efce.jpeg" alt="小程序">
          <p>扫码识别小程序</p>
        </div>
      </div>
      <div class="success-close" data-el="successClose"></div>
      <div class="confirm-btn" data-el="successClose">我知道了</div>
    </div>
  </div>
  <!-- 底部面包屑链接 -->
  <div class="bread__nav w1150 bread__nav--bottom">
  <p class="bread__nav__wrapper oneline">
                  <a href="/zufang/">杭州链家网</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/jianggan/">江干租房</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/dingqiao/">丁桥租房</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="/zufang/c1820027199512739/">柏悦公馆租房</a>
      </h1>
            </p>
</div>

</div>
<!-- 验证码容器 -->
<div id="captcha"></div>

<input type="hidden" data-el="showBooth" value="1">


<div class="send_message_wrapper" data-el="popup-wrapper">
  <div class="send_message_popup">
    <i class="send_message_popup-close" data-el="close-popup"></i>
    <h2 class="send_message_popup-title">我们将把经纪人/管家的联系电话以短信方式发送至您的手机，请注意查收</h2>
    <label class="send_message_popup-body">
      <p>
        <span class="send_message_popup-label">您的手机号</span>
        <input class="send_message_popup-input" data-el="message-tel" type="tel" maxlength="11" placeholder="请填写您的手机号">
      </p>
      <p class="send_message_popup-imgcode"></p>
    </label>
    <div class="send_message_popup-error"></div>
    <div class="send_message_popup-btn" data-el="message-submit">
      <div class="loading load-container"><div class="load"></div></div>
      <span class="submit-text">发送号码</span>
    </div>
    
  </div>
</div>

<!-- 400 商业化SDK -->
  <script src="https://s1.ljcdn.com/agent-sj-sdk/1.2.0/agent-sj-sdk.js"></script>
<script>
  var contact = {};
  contact = JSON.parse(JSON.stringify([]));
  
  // 留资需要传参
  g_conf.hdic_bizcircle_id = '611100152';
  g_conf.contact_ucid = '';
  g_conf.hdic_resblock_id = '1820027199512739';
  // 小程序二维码
  g_conf.qr_code_url = 'https://image1.ljcdn.com/params-compact/5c0134394b38a079574d308314343f1d.jpeg';

  g_conf.coord = {
    longitude: '120.234006',
    latitude: '30.367603'
  };
  g_conf.subway = [];
  g_conf.name = '柏悦公馆';
  g_conf.houseCode = 'HZ2298569620442841088';
  g_conf.offline = '';
  g_conf.city_id = 330100;
  g_conf.houseCondition = 'dingqiao';
  g_conf.houseConditionName = '丁桥'
  g_conf.frame_hall_num = '1';
  g_conf.bedroom_num = '1';
  g_conf.rent_price = '2250';
  g_conf.rent_type = '1';
  g_conf.use_pc_duty_info = '';
  g_conf.app_source = '200100000004';
  g_conf.app_source_brand = '200306004772';
  g_conf.bargainTitle = ''
  g_conf.bargainDesc = ''
  g_conf.appointUcId = '1000000026652402'
  g_conf.pageId = 'rentalDetail';
  var __requireList = ['https://s1.ljcdn.com/matrix_pc/dist/pc/src/page/detail/index.js?_v=20200917160625398'];
</script>
  </div>

  <div class="fix-right-v3" id="back-top" log-mod="sidebar" data-el="right_bar">
  <table>
    <tbody>
      <tr>
        <td>
          <ul>
            <li class="myfav sidebar-item">
              <a title="我关注的房源" data-url="//user.lianjia.com/site/favorHouse/" data-bl="myfav" exposure-event_id="25755" data-event_id="25756" exposure-event_action="click_name=心愿单" data-event_action="click_name=心愿单">我关注的房源</a>
              <span class="popup"><i></i>我关注的房源</span>
            </li>
            <li class="sell sidebar-item" data-el="rightbar_entry">
              <a title="在线租房" href="/zufang/proprietor/offer?city_id=330100&city_name=杭州&position=rent_pc_rightbar_rent" target="_blank" data-bl="sell" exposure-event_id="25755" exposure-event_action="click_name=出租"  data-event_id="25756" data-event_action="click_name=出租">我要出租</a>
              <span class="popup"><i></i>我要出租</span>
            </li>
                          <li class="baodan sidebar-item">
                <a href="//hz.lianjia.com/anxinchengnuo" title="安心服务承诺" target="_blank" data-bl="baodan" data-event_id="25756" exposure-event_id="25755" exposure-event_action="click_name=安心保单" data-event_action="click_name=安心保单">安心服务承诺</a>
                <span class="popup">
                  <i></i>安心服务承诺
                </span>
              </li>
                        
            <li class="download sidebar-item">
              <a href="//www.lianjia.com/client/" title="" target="_blank" data-bl="client" data-event_id="25756" exposure-event_id="25755" exposure-event_action="click_name=微信小程序" data-event_action="click_name=微信小程序">下载掌上链家</a>
              <span class="popup popup-qr">
                <i></i><img src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/lianjia/wxapp.jpg?_v=20200917160625398" alt="下载掌上链家" width="94">
                <em class="qr-title">链家微信小程序</em>
              </span>
            </li>
            <li class="phone sidebar-item">
              <a title="官方客服"  data-event_id="25756" exposure-event_id="25755" exposure-event_action="click_name=官方客服" data-event_action="click_name=官方客服">官方客服</a>
              <span class="popup"><i></i>官方客服</span>
            </li>

                        <li class="feedback sidebar-item">
              <a href="https://helper.lianjia.com/it/index2#/feedbackForC?channel=lj-pc&city=330100" title="反馈/投诉" data-bl="feedback" exposure-event_id="25755" data-event_id="25756" exposure-event_action="click_name=反馈" data-event_action="click_name=反馈"></a>
              <span class="popup"><i></i>反馈/投诉</span>
            </li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <ul>
    <li class="gotop sidebar-item" id="gotop" style="display: none;"><a title="返回顶部">返回顶部</a><span class="popup"><i></i>返回顶部</span></li>
  </ul>
</div>
  <div class="footer" style="margin-top:20px">
    <div class="footer__wrapper w1150">

      <div class="footer__top">
        <ul class="footer__light">
                    <li><a href="/zufang/wzdt/">网站地图</a></li>
                  </ul>
        <a class="footer__aside" href="tel:10109666">客服电话<span>10109666</span></a>
      </div>

      <div class="footer__middle">
        <ul data-el="parentList">
                      <li><a class="cur" data-index="0">热门商圈</a></li>
                      <li><a class="" data-index="1">推荐小区</a></li>
                      <li><a class="" data-index="2">租房城市</a></li>
                  </ul>
                  <ul data-el="childrenList"  style="display:block">
                          <li><a href="https://hz.lianjia.com/zufang/changqing1112/">长庆租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/nanxing/">南星租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/fuxing/">复兴租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/renhe2/">仁和租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wenyixilu/">文一西路租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/qingtai/">清泰租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xixing/">西兴租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yiqiao/">义桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jiande1/">建德租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jiubao/">九堡租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wandaguangchang2/">万达广场租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/huanglong/">黄龙租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gudang/">古荡租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/hemu/">和睦租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xixi/">西溪租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gongchenqiao/">拱宸桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/feicuicheng1/">翡翠城租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wulin11/">武林租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/tianshui1/">天水租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/dajiangdong/">大江东租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/caihongcheng/">彩虹城租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/huajiachi/">华家池租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/shenhua/">申花租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/sichoucheng1/">丝绸城租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/hubin1/">湖滨租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jianqiao/">笕桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/banshan/">半山租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/puyan/">浦沿租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/santang/">三塘租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/changhe/">长河租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/sandun/">三墩租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gouzhuang/">勾庄租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yanjiangbei/">沿江北租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/gudang/">古荡租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/huochedongzhan/">火车东站租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yiqiao/">义桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xiongzhenlou/">雄镇楼租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/dingqiao/">丁桥租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jinjiang1/">近江租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/liangzhu/">良渚租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/deshengdong/">德胜东租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/changhe/">长河租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/fuyang1/">富阳租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/daguan/">大关租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/heping2/">和平租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xuejun/">学军租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/linpu/">临浦租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/tonglushangquan/">桐庐租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/zhanongkou/">闸弄口租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jialv/">嘉绿租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/qingtai/">清泰租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jingfang1/">景芳租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/dajiangdong/">大江东租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/santang/">三塘租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/wenyixilu/">文一西路租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/xianlin1/">闲林租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/yanjiangnan/">沿江南租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/fuxing/">复兴租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/jinshahu/">金沙湖租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/liuxia1/">留下租房</a></li>
                      </ul>
                  <ul data-el="childrenList"  >
                          <li><a href="https://hz.lianjia.com/zufang/c1820022260637977/">大通路98号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641307/">嘉绿福苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636713/">和睦公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820022037245901/">解放路8号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820024445699943/">水岸鑫域租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641703/">嘉绿文苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815909850746844/">小河东河下66-11号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815440795176902/">永泰名苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636393/">五洋东湖春天租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641388/">武林门新村租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815732752026627/">佑圣观路5号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043638833/">云峰一区租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820023393475872/">保利融信大国璟租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043639425/">广景苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043638496/">裕园公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636559/">湖墅北路101号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641404/">紫金公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641620/">金沙曲苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820023902308543/">环城东路240号租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1820022536418987/">金隅空港公馆租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1815710271606474/">绿野清风租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043640426/">碧桂苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043641555/">筑品金座租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043637400/">大关东六苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636769/">沈大北苑小区租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043642186/">天水巷租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043642200/">灯塔东苑租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043636635/">石油公寓租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043639517/">联合格里租房</a></li>
                          <li><a href="https://hz.lianjia.com/zufang/c1811043635924/">知本大厦租房</a></li>
                      </ul>
                  <ul data-el="childrenList"  >
                          <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                          <li><a href="https://linyi.lianjia.com/zufang/">临沂租房</a></li>
                          <li><a href="https://huzhou.lianjia.com/zufang/">湖州租房</a></li>
                          <li><a href="https://wuhu.lianjia.com/zufang/">芜湖租房</a></li>
                          <li><a href="https://nanchong.lianjia.com/zufang/">南充租房</a></li>
                          <li><a href="https://xa.lianjia.com/zufang/">西安租房</a></li>
                          <li><a href="https://gz.lianjia.com/zufang/">广州租房</a></li>
                          <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                          <li><a href="https://san.lianjia.com/zufang/">三亚租房</a></li>
                          <li><a href="https://sjz.lianjia.com/zufang/">石家庄租房</a></li>
                          <li><a href="https://xc.lianjia.com/zufang/">许昌租房</a></li>
                          <li><a href="https://zj.lianjia.com/zufang/">镇江租房</a></li>
                          <li><a href="https://baoji.lianjia.com/zufang/">宝鸡租房</a></li>
                          <li><a href="https://yc.lianjia.com/zufang/">盐城租房</a></li>
                          <li><a href="https://zz.lianjia.com/zufang/">郑州租房</a></li>
                          <li><a href="https://dd.lianjia.com/zufang/">丹东租房</a></li>
                          <li><a href="https://sh.lianjia.com/zufang/">上海租房</a></li>
                          <li><a href="https://wf.lianjia.com/zufang/">潍坊租房</a></li>
                          <li><a href="https://ts.lianjia.com/zufang/">唐山租房</a></li>
                          <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                          <li><a href="https://liangshan.lianjia.com/zufang/">凉山租房</a></li>
                          <li><a href="https://gy.lianjia.com/zufang/">贵阳租房</a></li>
                          <li><a href="https://dazhou.lianjia.com/zufang/">达州租房</a></li>
                          <li><a href="https://hanzhong.lianjia.com/zufang/">汉中租房</a></li>
                          <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                          <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                          <li><a href="https://wh.lianjia.com/zufang/">武汉租房</a></li>
                          <li><a href="https://xan.lianjia.com/zufang/">雄安新区租房</a></li>
                          <li><a href="https://cq.lianjia.com/zufang/">重庆租房</a></li>
                          <li><a href="https://tj.lianjia.com/zufang/">天津租房</a></li>
                          <li><a href="https://ganzhou.lianjia.com/zufang/">赣州租房</a></li>
                          <li><a href="https://yt.lianjia.com/zufang/">烟台租房</a></li>
                          <li><a href="https://huzhou.lianjia.com/zufang/">湖州租房</a></li>
                          <li><a href="https://hui.lianjia.com/zufang/">惠州租房</a></li>
                          <li><a href="https://ms.lianjia.com/zufang/">眉山租房</a></li>
                          <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                          <li><a href="https://qd.lianjia.com/zufang/">青岛租房</a></li>
                          <li><a href="https://zjk.lianjia.com/zufang/">张家口租房</a></li>
                          <li><a href="https://jx.lianjia.com/zufang/">嘉兴租房</a></li>
                          <li><a href="https://dd.lianjia.com/zufang/">丹东租房</a></li>
                          <li><a href="https://yy.lianjia.com/zufang/">岳阳租房</a></li>
                          <li><a href="https://xa.lianjia.com/zufang/">西安租房</a></li>
                          <li><a href="https://nanchong.lianjia.com/zufang/">南充租房</a></li>
                          <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                          <li><a href="https://km.lianjia.com/zufang/">昆明租房</a></li>
                          <li><a href="https://cq.lianjia.com/zufang/">重庆租房</a></li>
                          <li><a href="https://changzhou.lianjia.com/zufang/">常州租房</a></li>
                          <li><a href="https://san.lianjia.com/zufang/">三亚租房</a></li>
                          <li><a href="https://linyi.lianjia.com/zufang/">临沂租房</a></li>
                          <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                          <li><a href="https://ez.lianjia.com/zufang/">鄂州租房</a></li>
                          <li><a href="https://sx.lianjia.com/zufang/">绍兴租房</a></li>
                          <li><a href="https://ks.lianjia.com/zufang/">昆山租房</a></li>
                          <li><a href="https://tj.lianjia.com/zufang/">天津租房</a></li>
                          <li><a href="https://jiujiang.lianjia.com/zufang/">九江租房</a></li>
                          <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                          <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                          <li><a href="https://wuhu.lianjia.com/zufang/">芜湖租房</a></li>
                          <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                          <li><a href="https://ty.lianjia.com/zufang/">太原租房</a></li>
                      </ul>
              </div>

      <div class="footer__bottom">
        <p>链家网（北京）科技有限公司 | 网络经营许可证 <a href="http://beian.miit.gov.cn">京ICP备16057509号</a> | &copy; Copyright &copy;2010-2020 链家网Lianjia.com版权所有</p>
        <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/lianjia/beian.png?_v=20200917160625398">京公网安备 11010802024019号</a>
      </div>

    </div>
  </div>
<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"title":"\u70ed\u95e8\u5546\u5708","city_id":330100,"abbr":"rmsq","source":"m","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/changqing1112\/","title":"\u957f\u5e86\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/nanxing\/","title":"\u5357\u661f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuxing\/","title":"\u590d\u5174\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/renhe2\/","title":"\u4ec1\u548c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wenyixilu\/","title":"\u6587\u4e00\u897f\u8def\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xixing\/","title":"\u897f\u5174\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yiqiao\/","title":"\u4e49\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jiande1\/","title":"\u5efa\u5fb7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jiubao\/","title":"\u4e5d\u5821\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wandaguangchang2\/","title":"\u4e07\u8fbe\u5e7f\u573a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/huanglong\/","title":"\u9ec4\u9f99\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gudang\/","title":"\u53e4\u8361\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/hemu\/","title":"\u548c\u7766\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xixi\/","title":"\u897f\u6eaa\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gongchenqiao\/","title":"\u62f1\u5bb8\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/feicuicheng1\/","title":"\u7fe1\u7fe0\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wulin11\/","title":"\u6b66\u6797\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/tianshui1\/","title":"\u5929\u6c34\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dajiangdong\/","title":"\u5927\u6c5f\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/caihongcheng\/","title":"\u5f69\u8679\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/huajiachi\/","title":"\u534e\u5bb6\u6c60\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/shenhua\/","title":"\u7533\u82b1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/sichoucheng1\/","title":"\u4e1d\u7ef8\u57ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/hubin1\/","title":"\u6e56\u6ee8\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jianqiao\/","title":"\u7b15\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/banshan\/","title":"\u534a\u5c71\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/puyan\/","title":"\u6d66\u6cbf\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/santang\/","title":"\u4e09\u5858\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/sandun\/","title":"\u4e09\u58a9\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gouzhuang\/","title":"\u52fe\u5e84\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yanjiangbei\/","title":"\u6cbf\u6c5f\u5317\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/gudang\/","title":"\u53e4\u8361\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/huochedongzhan\/","title":"\u706b\u8f66\u4e1c\u7ad9\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yiqiao\/","title":"\u4e49\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xiongzhenlou\/","title":"\u96c4\u9547\u697c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dingqiao\/","title":"\u4e01\u6865\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jinjiang1\/","title":"\u8fd1\u6c5f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/liangzhu\/","title":"\u826f\u6e1a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/deshengdong\/","title":"\u5fb7\u80dc\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuyang1\/","title":"\u5bcc\u9633\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/daguan\/","title":"\u5927\u5173\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/heping2\/","title":"\u548c\u5e73\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xuejun\/","title":"\u5b66\u519b\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/linpu\/","title":"\u4e34\u6d66\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/tonglushangquan\/","title":"\u6850\u5e90\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/zhanongkou\/","title":"\u95f8\u5f04\u53e3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jialv\/","title":"\u5609\u7eff\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jingfang1\/","title":"\u666f\u82b3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/dajiangdong\/","title":"\u5927\u6c5f\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/santang\/","title":"\u4e09\u5858\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/wenyixilu\/","title":"\u6587\u4e00\u897f\u8def\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/xianlin1\/","title":"\u95f2\u6797\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/yanjiangnan\/","title":"\u6cbf\u6c5f\u5357\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/fuxing\/","title":"\u590d\u5174\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/jinshahu\/","title":"\u91d1\u6c99\u6e56\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/liuxia1\/","title":"\u7559\u4e0b\u79df\u623f"}]},{"title":"\u63a8\u8350\u5c0f\u533a","city_id":330100,"abbr":"tjxq","source":"m","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820022260637977\/","title":"\u5927\u901a\u8def98\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641307\/","title":"\u5609\u7eff\u798f\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636713\/","title":"\u548c\u7766\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820022037245901\/","title":"\u89e3\u653e\u8def8\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820024445699943\/","title":"\u6c34\u5cb8\u946b\u57df\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641703\/","title":"\u5609\u7eff\u6587\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815909850746844\/","title":"\u5c0f\u6cb3\u4e1c\u6cb3\u4e0b66-11\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815440795176902\/","title":"\u6c38\u6cf0\u540d\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636393\/","title":"\u4e94\u6d0b\u4e1c\u6e56\u6625\u5929\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641388\/","title":"\u6b66\u6797\u95e8\u65b0\u6751\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815732752026627\/","title":"\u4f51\u5723\u89c2\u8def5\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043638833\/","title":"\u4e91\u5cf0\u4e00\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820023393475872\/","title":"\u4fdd\u5229\u878d\u4fe1\u5927\u56fd\u749f\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639425\/","title":"\u5e7f\u666f\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043638496\/","title":"\u88d5\u56ed\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636559\/","title":"\u6e56\u5885\u5317\u8def101\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641404\/","title":"\u7d2b\u91d1\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641620\/","title":"\u91d1\u6c99\u66f2\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820023902308543\/","title":"\u73af\u57ce\u4e1c\u8def240\u53f7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1820022536418987\/","title":"\u91d1\u9685\u7a7a\u6e2f\u516c\u9986\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1815710271606474\/","title":"\u7eff\u91ce\u6e05\u98ce\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043640426\/","title":"\u78a7\u6842\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043641555\/","title":"\u7b51\u54c1\u91d1\u5ea7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043637400\/","title":"\u5927\u5173\u4e1c\u516d\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636769\/","title":"\u6c88\u5927\u5317\u82d1\u5c0f\u533a\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043642186\/","title":"\u5929\u6c34\u5df7\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043642200\/","title":"\u706f\u5854\u4e1c\u82d1\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043636635\/","title":"\u77f3\u6cb9\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043639517\/","title":"\u8054\u5408\u683c\u91cc\u79df\u623f"},{"url":"https:\/\/hz.lianjia.com\/zufang\/c1811043635924\/","title":"\u77e5\u672c\u5927\u53a6\u79df\u623f"}]},{"title":"\u79df\u623f\u57ce\u5e02","city_id":330100,"abbr":"zfcs","source":"m","children":[{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/linyi.lianjia.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/huzhou.lianjia.com\/zufang\/","title":"\u6e56\u5dde\u79df\u623f"},{"url":"https:\/\/wuhu.lianjia.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/nanchong.lianjia.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/xa.lianjia.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/gz.lianjia.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/san.lianjia.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/sjz.lianjia.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/xc.lianjia.com\/zufang\/","title":"\u8bb8\u660c\u79df\u623f"},{"url":"https:\/\/zj.lianjia.com\/zufang\/","title":"\u9547\u6c5f\u79df\u623f"},{"url":"https:\/\/baoji.lianjia.com\/zufang\/","title":"\u5b9d\u9e21\u79df\u623f"},{"url":"https:\/\/yc.lianjia.com\/zufang\/","title":"\u76d0\u57ce\u79df\u623f"},{"url":"https:\/\/zz.lianjia.com\/zufang\/","title":"\u90d1\u5dde\u79df\u623f"},{"url":"https:\/\/dd.lianjia.com\/zufang\/","title":"\u4e39\u4e1c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/","title":"\u4e0a\u6d77\u79df\u623f"},{"url":"https:\/\/wf.lianjia.com\/zufang\/","title":"\u6f4d\u574a\u79df\u623f"},{"url":"https:\/\/ts.lianjia.com\/zufang\/","title":"\u5510\u5c71\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/liangshan.lianjia.com\/zufang\/","title":"\u51c9\u5c71\u79df\u623f"},{"url":"https:\/\/gy.lianjia.com\/zufang\/","title":"\u8d35\u9633\u79df\u623f"},{"url":"https:\/\/dazhou.lianjia.com\/zufang\/","title":"\u8fbe\u5dde\u79df\u623f"},{"url":"https:\/\/hanzhong.lianjia.com\/zufang\/","title":"\u6c49\u4e2d\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/wh.lianjia.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/xan.lianjia.com\/zufang\/","title":"\u96c4\u5b89\u65b0\u533a\u79df\u623f"},{"url":"https:\/\/cq.lianjia.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/tj.lianjia.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/ganzhou.lianjia.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/yt.lianjia.com\/zufang\/","title":"\u70df\u53f0\u79df\u623f"},{"url":"https:\/\/huzhou.lianjia.com\/zufang\/","title":"\u6e56\u5dde\u79df\u623f"},{"url":"https:\/\/hui.lianjia.com\/zufang\/","title":"\u60e0\u5dde\u79df\u623f"},{"url":"https:\/\/ms.lianjia.com\/zufang\/","title":"\u7709\u5c71\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/qd.lianjia.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/zjk.lianjia.com\/zufang\/","title":"\u5f20\u5bb6\u53e3\u79df\u623f"},{"url":"https:\/\/jx.lianjia.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/dd.lianjia.com\/zufang\/","title":"\u4e39\u4e1c\u79df\u623f"},{"url":"https:\/\/yy.lianjia.com\/zufang\/","title":"\u5cb3\u9633\u79df\u623f"},{"url":"https:\/\/xa.lianjia.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/nanchong.lianjia.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/km.lianjia.com\/zufang\/","title":"\u6606\u660e\u79df\u623f"},{"url":"https:\/\/cq.lianjia.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/changzhou.lianjia.com\/zufang\/","title":"\u5e38\u5dde\u79df\u623f"},{"url":"https:\/\/san.lianjia.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/linyi.lianjia.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/ez.lianjia.com\/zufang\/","title":"\u9102\u5dde\u79df\u623f"},{"url":"https:\/\/sx.lianjia.com\/zufang\/","title":"\u7ecd\u5174\u79df\u623f"},{"url":"https:\/\/ks.lianjia.com\/zufang\/","title":"\u6606\u5c71\u79df\u623f"},{"url":"https:\/\/tj.lianjia.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/jiujiang.lianjia.com\/zufang\/","title":"\u4e5d\u6c5f\u79df\u623f"},{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/wuhu.lianjia.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/ty.lianjia.com\/zufang\/","title":"\u592a\u539f\u79df\u623f"}]}]))
</script>

</body>
<!-- 登录弹窗sdk -->
<script src="https://s1.ljcdn.com/clogin/js/pcLogin.js"></script>
<script src="https://s1.ljcdn.com/captcha-js-sdk-v2/captcha.js"></script>

<script>
  BeikeLoginSDK.config({
    env: 'prod', 
    loginCallback: function(){
      location.reload()
    },
    registerCallback: function(){
      location.reload()
    }
  })
</script>

<!--动态脚本内容-->

<!-- 页面IM相关配置内容 -->


<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      }
</script>

<!-- 设备指纹接入 -->
<script>
  window['__abbaidu_2011_subidgetf'] = function () {
    var subid = 110200;
    return subid;
  }
</script>
<script>
  window['__abbaidu_2011_cb'] = function (responseData) {
    var fpStr = JSON.stringify({
      t: responseData,
      r: location.href,
      os: 'web',
      v: '0.1'
    })
    var fpBase = window.btoa(fpStr)
    document.cookie = "srcid=" + fpBase +';path=/';
  };
</script>
<script async="" src="https://dlswbr.baidu.com/heicha/mw/abclite-2011-s2.js"></script><!-- 百度seo自动推送代码 -->
<script>
  (function(){var canonicalURL,curProtocol;var x=document.getElementsByTagName("link");if(x.length>0){for(i=0;i<x.length;i++){if(x[i].rel.toLowerCase()=="canonical"&&x[i].href){canonicalURL=x[i].href}}}if(!canonicalURL){curProtocol=window.location.protocol.split(":")[0]}else{curProtocol=canonicalURL.split(":")[0]}if(!canonicalURL){canonicalURL=window.location.href}!function(){var e=/([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r=canonicalURL,t=document.referrer;if(!e.test(r)){var n=(String(curProtocol).toLowerCase()==="https")?"https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif":"//api.share.baidu.com/s.gif";t?(n+="?r="+encodeURIComponent(document.referrer),r&&(n+="&l="+r)):r&&(n+="?l="+r);var i=new Image;i.src=n}}(window)})();
</script>

<!-- 落地时间因子 -->
<script type="application/ld+json">
  {
    "@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
    "@id": "https%3A%2F%2Fhz.zu.lianjia.com%2Fzufang%2Fzufang%2FHZ2298569620442841088.html",
    "appid": "1597146525691227",
    "pubDate": "2020-09-22T19:46:04",
    "upDate": "2020-09-22T19:46:04"
  }
</script>


<!-- 页面依赖JS加载 -->

<!-- common.js线上引入灯塔 -->
  <script type="text/javascript" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/common.js?_v=20200917160625398" crossorigin="anonymous"></script>

<script>
  var __basePath = 'https://s1.ljcdn.com/matrix_pc/dist/pc/src?_v=20200917160625398'.split("?") || [];
  require.config({
    //baseUrl: __basePath[0],
    paths: {
    },
    urlArgs:  __basePath[1],
    crossorigin: Boolean('1') //线上环境加该属性,需要再amd.js中单独配置一下
  });
  var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_pc\/dist\/pc","version":"20200917160625398","js_ns":"m_pages_zufangDetail","cur_city_id":"330100","cur_city_name":"\u676d\u5dde","cur_city_short":"hz"}
  ;;(function() {
    for(var i = 0, len = __requireList.length; i < len; i++) {
      var item = __requireList[i]
      item = item.split("?")[0]
      require([item], function(engine) {
        engine.init()
      })
    }
  })()
</script>

<!-- 埋点配置文件 -->

<script>
window.__UDL_CONFIG = window.__UDL_CONFIG || {}
window.__UDL_CONFIG.pid = window.__UDL_CONFIG.pid || "matrixpc"
window.__UDL_CONFIG.env = ('prod' === 'prod' ? "lianjia" : 'test')
window.__UDL_CONFIG["ljweb_channel_key"] = g_conf.pageId || ''

var _script = document.createElement('script')
_script.type = 'text/javascript'
// 该属性是为了配合接入灯塔，所有script标签都需加的属性
_script.setAttribute('crossorigin', 'anonymous')
document.getElementsByTagName('head')[0].appendChild(_script)
if(window.__UDL_CONFIG.env === 'test'){
  _script.src='//s1.rent39.internal.lianjia.com/matrix_pc/dist/pc/third/dig.js?' + __basePath[1]
}else{
  _script.src='//s1.ljcdn.com/matrix_pc/dist/pc/third/dig.js?' + __basePath[1]
}
</script>

</html>


Process finished with exit code 0

'''
txt_doc = etree.HTML(txt1)
# todo 爬取租房方式
temp = txt_doc.xpath("//ul[@class='content__aside__list']/li")
for i in temp:
    a = ''.join(i.xpath("./text()|./span/text()|./a/text()")).strip()
    print(a)
# todo 爬取房屋基本信息
temp1 = txt_doc.xpath("//div[@id='info']/ul/li")
for i in temp1:
    b = ''.join(i.xpath("./text()")).strip()
    print(b)

# todo 爬取配套设施
temp2 = txt_doc.xpath("//ul[@class='content__article__info2']/li")
for i in temp2:
    c = ''.join(i.xpath("./text()")).strip()
    print(c)

# todo 爬取房源描述
d = ''.join(txt_doc.xpath("//p[@data-el='houseComment']/text()")).strip()
print(d)

# todo 爬取费用详情
# 爬取的是付款方式
temp3 = txt_doc.xpath("//ul[@class='table_title']/li")
for i in temp3:
    e = ''.join(i.xpath("./text()")).strip()
    print(e)
# 爬取的是季付
temp4 = txt_doc.xpath("//ul[@class='table_row']/li")
for i in temp4:
    e = ''.join(i.xpath("./text()")).strip()
    print(e)

pat_1 = ' <img src="(.*)">'
f1 = re.findall(pat_1,txt1)
for i in f1:
    g = requests.get(i,headers).content
    with open(i[-32:-16]+'.png','wb+') as f:
        f.write(g)