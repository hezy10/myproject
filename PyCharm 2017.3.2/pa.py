import requests
from lxml import etree

str_1 = '''
D:\Anaconda\anaconda3\python.exe "D:/PyCharm 2017.3.2/venv/pa.py"
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
  <meta name="description" content="贝壳杭州租房网,提供真实的杭州≤1000元租房信息、出租房源信息、租房价格,包括杭州≤1000元整租、合租、公寓出租等信息,以及杭州≤1000元房屋出租个人信息、经纪人信息、品牌公寓信息等.找租房房源,就来杭州贝壳租房!">
  <meta name="keywords" content="杭州≤1000元租房信息,杭州≤1000元出租房网,杭州≤1000元房屋出租价格">
  <title>杭州≤1000元租房信息_杭州≤1000元出租房源|房屋出租价格【杭州贝壳租房】</title>

  

  <!--地址信息-->
  <meta name="location" content="province=浙江;city=杭州">

  <!-- 网站ico图标 -->
    <link href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/favicon.ico?_v=20200806113746ed7" type="image/x-icon" rel="icon">

    <meta name=""mobile-agent content="format=[wml|xhtml|html5];url=https://m.ke.com/chuzu/hz/zufang/rp1/" />
  <link rel="alternate" media="only screen and (max-width:640px)" href="https://m.ke.com/chuzu/hz/zufang/rp1/">
  
    <!-- 是否需要加载common.css -->
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/css/common.css?_v=20200806113746ed7">
  
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
            var filterStr = ['未登录', '/msg/sync ajax fail', '登录令牌缺失']

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
  <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_pc/dist/pc/src/page/list/index.css?_v=20200806113746ed7">
  
  
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
          <a href="//hz.ke.com" target="_blank">首页</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.ke.com/ershoufang/" target="_blank">二手房</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.fang.ke.com/loupan/" target="_blank">新房</a>
        </li>
                        <li class="header__item fl cur" >
          <a href="/zufang/" target="_blank">租房</a>
        </li>
                        <li class="header__item fl" >
          <a href="//i.ke.com" target="_blank">海外</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.ke.com/xiaoqu/" target="_blank">小区</a>
        </li>
                        <li class="header__item fl" >
          <a href="//news.ke.com/hz/baike/" target="_blank">百科</a>
        </li>
                        <li class="header__item fl" >
          <a href="//hz.ke.com/fangjia/" target="_blank">房价</a>
        </li>
                        <li class="header__item fl publish-house" data-event_id="20383">
          <a href="//hz.ke.com/yezhu/maifang/" target="_blank">发布房源</a>
        </li>
                        <li class="header__item fl download">
          <a href="javascript:;" target="_blank">下载APP</a>
          <div class="download__box">
            <img src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/getDownloadQr.png?_v=20200806113746ed7" alt="下载贝壳APP">
          </div>
        </li>
                                  <li class="header__item fl">
            <a href="https://open.ke.com/home?source=4" target="_blank">贝壳开放平台</a>
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
        <ul class="menu-list ">
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

                  <img width="94" height="94" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/getDownloadQr.png?_v=20200806113746ed7" alt="下载贝壳APP">
        
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
                  <a href="https://hz.zu.ke.com/">杭州贝壳网</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="https://hz.zu.ke.com/zufang/">杭州租房</a>
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
          <a href="/zufang/rp1/"  rel="nofollow">不限</a>
        </li>
              <li data-id="330106" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xihu/rp1/"  >西湖</a>
        </li>
              <li data-id="330103" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xiacheng/rp1/"  >下城</a>
        </li>
              <li data-id="330104" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/jianggan/rp1/"  >江干</a>
        </li>
              <li data-id="330105" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/gongshu/rp1/"  >拱墅</a>
        </li>
              <li data-id="330102" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/shangcheng/rp1/"  >上城</a>
        </li>
              <li data-id="330108" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/binjiang/rp1/"  >滨江</a>
        </li>
              <li data-id="330110" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/yuhang/rp1/"  >余杭</a>
        </li>
              <li data-id="330109" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/xiaoshan/rp1/"  >萧山</a>
        </li>
              <li data-id="330183" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/fuyang/rp1/"  >富阳</a>
        </li>
              <li data-id="330185" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/linan/rp1/"  >临安</a>
        </li>
              <li data-id="23011864" data-type="district" class="filter__item--level2  ">
          <a href="/zufang/qiantangxinqu/rp1/"  >钱塘新区</a>
        </li>
            </ul>
    
          <ul class="hide" data-target="station">
              <li data-id="0" data-type="line" class="filter__item--level2 filter__item--aside strong">
          <a href="/ditiezufang/rp1/" rel="nofollow">不限</a>
        </li>
              <li data-id="110460707" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li110460707/rp1/" >1号线(临平-湘湖)</a>
        </li>
              <li data-id="1820035120370916" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li1820035120370916/rp1/" >1号线(下沙江滨-湘湖)</a>
        </li>
              <li data-id="189500791680395" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li189500791680395/rp1/" >地铁2号线</a>
        </li>
              <li data-id="189503468170337" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li189503468170337/rp1/" >地铁4号线</a>
        </li>
              <li data-id="1820044952055481" data-type="line" class="filter__item--level2  ">
          <a href="/ditiezufang/li1820044952055481/rp1/" >地铁5号线</a>
        </li>
            </ul>
    
    
          <ul data-target="station">
              </ul>
    
          <ul class="filter__ul" data-el="rentType">
          <li class="filter__item--level4 filter__item--aside"><a href="javascript:;">方式</a></li>
                  <li data-id="0" class="filter__item--level4 strong">
            <a href="/zufang/rp1/" rel="nofollow" >不限</a>
          </li>
                  <li data-id="200600000001" class="filter__item--level4 ">
            <a href="/zufang/rt200600000001rp1/"  >整租</a>
          </li>
                  <li data-id="200600000002" class="filter__item--level4 ">
            <a href="/zufang/rt200600000002rp1/"  >合租</a>
          </li>
              </ul>
    
    
          <ul class="filter__ul" data-el="filterPrice">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">租金</a></li>
                  <li class="filter__item--level5 check checked">
            <a href="/zufang/">≤1000元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp1rp2/">1000-1500元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp1rp3/">1500-2000元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp1rp4/">2000-3000元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp1rp5/">3000-4500元</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/rp1rp6/">≥4500元</a>
          </li>
                  <li class="filter__item--input" data-url="/zufang/rp1brp{min}erp{max}/"><input type="text" data-el="input_start" value="">-<input data-el="input_end" type="text" value="">元<span class="filter__button" data-el="button"></span></li>
      </ul>
    
          <ul class="filter__ul">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">户型</a></li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l0rp1/">一居</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l1rp1/">两居</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l2rp1/">三居</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/l3rp1/">四居+</a>
          </li>
              </ul>
    
    
          <ul class="filter__ul ">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">朝向</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000001rp1/">东</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000005rp1/">西</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000003rp1/">南</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000007rp1/">北</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/f100500000009rp1/">南北</a>
          </li>
              </ul>
    
          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">品牌</a></li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200301001000rp1/">链家</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200302002000rp1/">自如</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200302003000rp1/">魔方公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200302144000rp1/">城家公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306001866rp1/">泊寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306006672rp1/">初九公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a href="/zufang/ab200306007028rp1/">奥通公寓</a>
          </li>
                    </ul>
    
          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">特色</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/su1rp1/">近地铁</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/bc1rp1/">拎包入住</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/de1rp1/">精装修</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/rpw1rp1/">押一付一</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/in1rp1/">新上</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/ht1rp1/">认证公寓</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/hk1rp1/">随时看房</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/vr1rp1/">VR房源</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/orec1rp1/">业主自荐</a>
          </li>
              </ul>
          <!--租期-->
            <ul class="filter__ul hide">
            <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">租期</a></li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp1rp1/">月租</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp2rp1/">年租</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp3rp1/">一个月起租</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp4rp1/">1-3个月</a>
                </li>
                            <li class="filter__item--level5 check ">
                    <a rel="nofollow" href="/zufang/rmp5rp1/">4-6个月</a>
                </li>
                    </ul>
    
          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">楼层</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/lc200500000003rp1/">低楼层</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/lc200500000002rp1/">中楼层</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/lc200500000001rp1/">高楼层</a>
          </li>
              </ul>
    
          <ul class="filter__ul hide">
          <li class="filter__item--level5 filter__item--aside"><a href="javascript:;">电梯</a></li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/ie0rp1/">无电梯</a>
          </li>
                  <li class="filter__item--level5 check ">
            <a rel="nofollow" href="/zufang/ie1rp1/">有电梯</a>
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
      已为您找到 <span class="content__title--hl">591</span> 套 <a href="https://hz.zu.ke.com/zufang/" target="_blank" style="text-decoration:none;color:black">杭州租房</a>
    <span class="content__title--aside"><a href="/zufang/" id="clearUrl">清空条件</a></span>
</p>

      <!-- 搜索结果排序模块 -->
      <ul class="content__filter" id="contentList">
            <li data-event_id="10800" data-event_action="search_condition=/zufang/rp1/" class='content__filter--selected'>
        <a href="/zufang/rp1/" 
           data-event_id="10797" 
           data-event_action="target=综合排序"
           data-event_position="target">综合排序</a>
      </li>
                <li data-event_id="10800" data-event_action="search_condition=/zufang/rco11rp1/" >
        <a href="/zufang/rco11rp1/" 
           data-event_id="10797" 
           data-event_action="target=最新上架"
           data-event_position="target">最新上架</a>
      </li>
                                                              <li data-event_id="10800" 
          data-event_action="search_condition=/zufang/rco21rp1/" 
          class=' '>

                  <a href="/zufang/rco21rp1/" 
             data-event_id="10797" 
             data-event_action="target=价格"
             data-event_position="target"
             >价格</a>
              </li>
                                                              <li data-event_id="10800" 
          data-event_action="search_condition=/zufang/rco31rp1/" 
          class=' '>

                  <a href="/zufang/rco31rp1/" 
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
  data-house_code="HZ2564284996370309120"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="0"
  data-total="591"
  data-fb_expo_id="345219254799417345"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2564284996370309120.html"
      title="整租·江南佳苑 2室1厅 南">
        <img
          alt="整租·江南佳苑 2室1厅 南_江南佳苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/330100-inspection/prod-0c12d1a9-f1da-406e-8f10-6f1da372a1c3.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2564284996370309120.html">
          整租·江南佳苑 2室1厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="江南佳苑" href="/zufang/c1820034035979534/" target="_blank">江南佳苑</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （18层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--rent_period_month">月租</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">8天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div class="content__list--item"
    data-el="listItem"
    data-house_code="231871"
    data-brand_code="200306001059"
    data-ad_code="37365965616726952"
    data-c_type="1"
    data-position="1"
    data-total="591"
    data-fb_expo_id="345219254937772033"
    data-t=""
    data-strategy_id=""
    data-click_position="1"
    data-ad_type="40"
    data-distribution_type="203500000002"
    >
  <a class="link" target="_blank" data-id="231871" href="/apartment/13355.html">
    <!-- 左边图片 -->
    <a
      class="content__list--item--aside" target="_blank"      href="/apartment/13355.html"
      title="独栋·随寓 乔司云村社区 单间独卫无中介费 开间">
        <img
        alt="独栋·随寓 乔司云村社区 单间独卫无中介费 开间_租房"
        src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
        data-src="https://ke-image.ljcdn.com/rent-user-avatar/a3a04e25-da84-4135-a02f-7a52df2156b2.250x182.jpg"
        class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
                  <p class="content__list--item--ad">
            精选          </p>
            </a>
    <!-- 右边内容 -->
    <div class="content__list--item--main">
      <!-- title -->
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/apartment/13355.html">
          独栋·随寓 乔司云村社区 单间独卫无中介费 开间        </a>
      </p>
      <!-- house info -->
      <p class="content__list--item--des">
                20-23㎡
        <i>/</i>20间在租        <i>/</i>
        1室0厅1卫      </p>
      <!-- tags -->
      <p class="content__list--item--bottom oneline">
                  <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                  <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
              </p>
      <!-- brand -->
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            随寓          </span>
                <span class="content__list--item--time">24天前维护</span>
      </p>
      
      <!-- price -->
      <span class="content__list--item-price"><em>906</em> 元/月</span>
    </div>
  </a>
</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2565854831110012928"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="2"
  data-total="591"
  data-fb_expo_id="345219254799417347"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2565854831110012928.html"
      title="整租·颐和山庄 3室2厅 南">
        <img
          alt="整租·颐和山庄 3室2厅 南_颐和山庄租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/330100-inspection/0fe82668-6791-43e6-8e26-eec579a03a03.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2565854831110012928.html">
          整租·颐和山庄 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="颐和山庄" href="/zufang/c1820021378572257/" target="_blank">颐和山庄</a>
        <i>/</i>
        93㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>900</em> 元/月</span>
    </div>

</div>
<div class="content__list--item"
    data-el="listItem"
    data-house_code="231914"
    data-brand_code="200306001059"
    data-ad_code="37365965616726952"
    data-c_type="1"
    data-position="3"
    data-total="591"
    data-fb_expo_id="345219254937772034"
    data-t=""
    data-strategy_id=""
    data-click_position="3"
    data-ad_type="40"
    data-distribution_type="203500000002"
    >
  <a class="link" target="_blank" data-id="231914" href="/apartment/13355.html">
    <!-- 左边图片 -->
    <a
      class="content__list--item--aside" target="_blank"      href="/apartment/13355.html"
      title="独栋·随寓 乔司云村社区 免中介直租 开间">
        <img
        alt="独栋·随寓 乔司云村社区 免中介直租 开间_租房"
        src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
        data-src="https://ke-image.ljcdn.com/rent-user-avatar/1d892ac3-28ac-4198-825f-e6ca1b2e02af.250x182.jpg"
        class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
                  <p class="content__list--item--ad">
            精选          </p>
            </a>
    <!-- 右边内容 -->
    <div class="content__list--item--main">
      <!-- title -->
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/apartment/13355.html">
          独栋·随寓 乔司云村社区 免中介直租 开间        </a>
      </p>
      <!-- house info -->
      <p class="content__list--item--des">
                20㎡
        <i>/</i>6间在租        <i>/</i>
        1室0厅1卫      </p>
      <!-- tags -->
      <p class="content__list--item--bottom oneline">
                  <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                  <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
              </p>
      <!-- brand -->
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            随寓          </span>
                <span class="content__list--item--time">6天前维护</span>
      </p>
      
      <!-- price -->
      <span class="content__list--item-price"><em>800</em> 元/月</span>
    </div>
  </a>
</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2565776734696259584"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="4"
  data-total="591"
  data-fb_expo_id="345219254799417349"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2565776734696259584.html"
      title="整租·金盾花园 1室0厅 北">
        <img
          alt="整租·金盾花园 1室0厅 北_金盾花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/520e494c-f36b-47e8-97e3-f6cde4f8129d.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2565776734696259584.html">
          整租·金盾花园 1室0厅 北        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="金盾花园" href="/zufang/c1820034628629104/" target="_blank">金盾花园</a>
        <i>/</i>
        30㎡
        <i>/</i>北        <i>/</i>
          1室0厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （1层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">2天前维护</span>
      </p>
      <span class="content__list--item-price"><em>800</em> 元/月</span>
    </div>

</div>
<div class="content__list--item"
    data-el="listItem"
    data-house_code="163968"
    data-brand_code="200306001059"
    data-ad_code="37365965616726952"
    data-c_type="1"
    data-position="5"
    data-total="591"
    data-fb_expo_id="345219254937772035"
    data-t=""
    data-strategy_id=""
    data-click_position="5"
    data-ad_type="40"
    data-distribution_type="203500000002"
    >
  <a class="link" target="_blank" data-id="163968" href="/apartment/13355.html">
    <!-- 左边图片 -->
    <a
      class="content__list--item--aside" target="_blank"      href="/apartment/13355.html"
      title="独栋·随寓 乔司云村社区 独卫斜坡可短租无中介 开间">
        <img
        alt="独栋·随寓 乔司云村社区 独卫斜坡可短租无中介 开间_租房"
        src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
        data-src="https://ke-image.ljcdn.com/rent-user-avatar/6672dfef-81cd-478b-88b7-9f4d4416128d.250x182.jpg"
        class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
                  <p class="content__list--item--ad">
            精选          </p>
            </a>
    <!-- 右边内容 -->
    <div class="content__list--item--main">
      <!-- title -->
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/apartment/13355.html">
          独栋·随寓 乔司云村社区 独卫斜坡可短租无中介 开间        </a>
      </p>
      <!-- house info -->
      <p class="content__list--item--des">
                25㎡
        <i>/</i>20间在租        <i>/</i>
        1室0厅1卫      </p>
      <!-- tags -->
      <p class="content__list--item--bottom oneline">
                  <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                  <i class="content__item__tag--rent_period_month">月租</i>
                  <i class="content__item__tag--open_kitchen">开放厨房</i>
                  <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
              </p>
      <!-- brand -->
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            随寓          </span>
                <span class="content__list--item--time">24天前维护</span>
      </p>
      
      <!-- price -->
      <span class="content__list--item-price"><em>900</em> 元/月</span>
    </div>
  </a>
</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2560624681334358016"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="6"
  data-total="591"
  data-fb_expo_id="345219254799417351"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2560624681334358016.html"
      title="整租·大园新城 2室1厅 南">
        <img
          alt="整租·大园新城 2室1厅 南_大园新城租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/330100-inspection/prod-e20077cc-1f26-44cb-8446-1ae91ef499a8.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2560624681334358016.html">
          整租·大园新城 2室1厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="大园新城" href="/zufang/c1820034666387304/" target="_blank">大园新城</a>
        <i>/</i>
        101㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （26层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2562916054263136256"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="7"
  data-total="591"
  data-fb_expo_id="345219254799417352"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2562916054263136256.html"
      title="整租·星汇花园 3室2厅 南">
        <img
          alt="整租·星汇花园 3室2厅 南_星汇花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_u2r3xpEYX.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2562916054263136256.html">
          整租·星汇花园 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="星汇花园" href="/zufang/c188123089433077/" target="_blank">星汇花园</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （34层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">4天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2562236842984882176"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="8"
  data-total="591"
  data-fb_expo_id="345219254799417353"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2562236842984882176.html"
      title="整租·颐和山庄 3室1厅 南">
        <img
          alt="整租·颐和山庄 3室1厅 南_颐和山庄租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_FbC7cc0eN_1.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2562236842984882176.html">
          整租·颐和山庄 3室1厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="颐和山庄" href="/zufang/c1820021378572257/" target="_blank">颐和山庄</a>
        <i>/</i>
        118㎡
        <i>/</i>南        <i>/</i>
          3室1厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2562915180313059328"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="9"
  data-total="591"
  data-fb_expo_id="345219254799417354"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2562915180313059328.html"
      title="整租·星汇花园 3室2厅 南">
        <img
          alt="整租·星汇花园 3室2厅 南_星汇花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_O77e7ehaK.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2562915180313059328.html">
          整租·星汇花园 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="星汇花园" href="/zufang/c188123089433077/" target="_blank">星汇花园</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （34层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">4天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2562922263183622144"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="10"
  data-total="591"
  data-fb_expo_id="345219254799417355"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2562922263183622144.html"
      title="整租·星汇花园 3室2厅 南">
        <img
          alt="整租·星汇花园 3室2厅 南_星汇花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_WhBLF4D3c.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2562922263183622144.html">
          整租·星汇花园 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="星汇花园" href="/zufang/c188123089433077/" target="_blank">星汇花园</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （34层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2316013670951559168"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="11"
  data-total="591"
  data-fb_expo_id="345219254799417346"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2316013670951559168.html"
      title="合租·新城红郡 4居室 南卧">
        <img
          alt="合租·新城红郡 4居室 南卧_新城红郡租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1595992330199/992ff873383152766bccb6b8458378c5.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2316013670951559168.html">
          合租·新城红郡 4居室 南卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="新城红郡" href="/zufang/c187624879255847/" target="_blank">新城红郡</a>
        <i>/</i>
        9㎡
        <i>/</i>南        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （24层）
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
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>960</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2562914961487560704"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="12"
  data-total="591"
  data-fb_expo_id="345219254799417357"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2562914961487560704.html"
      title="整租·星汇花园 3室2厅 南">
        <img
          alt="整租·星汇花园 3室2厅 南_星汇花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_lOaVAXGzn.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2562914961487560704.html">
          整租·星汇花园 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="星汇花园" href="/zufang/c188123089433077/" target="_blank">星汇花园</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （34层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">今天维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2350651562047062016"
  data-brand_code="200306007984"
  data-ad_code=""
  data-c_type="1"
  data-position="13"
  data-total="591"
  data-fb_expo_id="345219254799417348"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2350651562047062016.html"
      title="合租·教工里 4居室 南卧">
        <img
          alt="合租·教工里 4居室 南卧_教工里租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-user-avatar/11618a9d-b8f9-421e-8d05-d4dfede5a7b7.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2350651562047062016.html">
          合租·教工里 4居室 南卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/xinyifang/" target="_blank">信义坊</a>-<a title="教工里" href="/zufang/c1811043641830/" target="_blank">教工里</a>
        <i>/</i>
        12㎡
        <i>/</i>南        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （7层）
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
                <span class="content__list--item--time oneline">17天前维护</span>
      </p>
      <span class="content__list--item-price"><em>900</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2534017692810625024"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="14"
  data-total="591"
  data-fb_expo_id="345219254799417359"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2534017692810625024.html"
      title="整租·中天珺府 3室2厅 南">
        <img
          alt="整租·中天珺府 3室2厅 南_中天珺府租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182_1.png?_v=20200806113746ed7"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2534017692810625024.html">
          整租·中天珺府 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="中天珺府" href="/zufang/c188122743665334/" target="_blank">中天珺府</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>900</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2530444724003938304"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="15"
  data-total="591"
  data-fb_expo_id="345219254799417360"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2530444724003938304.html"
      title="整租·中天珺府 3室1厅 南">
        <img
          alt="整租·中天珺府 3室1厅 南_中天珺府租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_k1ESF9NGR.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2530444724003938304.html">
          整租·中天珺府 3室1厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="中天珺府" href="/zufang/c188122743665334/" target="_blank">中天珺府</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2513573316879450112"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="16"
  data-total="591"
  data-fb_expo_id="345219254799417361"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2513573316879450112.html"
      title="整租·绿城桃源小镇品霞苑 4室2厅 南">
        <img
          alt="整租·绿城桃源小镇品霞苑 4室2厅 南_绿城桃源小镇品霞苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_8fnkL6MV3_1.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2513573316879450112.html">
          整租·绿城桃源小镇品霞苑 4室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/xianlin1/" target="_blank">闲林</a>-<a title="绿城桃源小镇品霞苑" href="/zufang/c1820045793350441/" target="_blank">绿城桃源小镇品霞苑</a>
        <i>/</i>
        125㎡
        <i>/</i>南        <i>/</i>
          4室2厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （29层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">4天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2488484228962975744"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="17"
  data-total="591"
  data-fb_expo_id="345219254799417362"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2488484228962975744.html"
      title="整租·星汇花园 2室1厅 北">
        <img
          alt="整租·星汇花园 2室1厅 北_星汇花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_gDcGsLfyP_1.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2488484228962975744.html">
          整租·星汇花园 2室1厅 北        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="星汇花园" href="/zufang/c188123089433077/" target="_blank">星汇花园</a>
        <i>/</i>
        89㎡
        <i>/</i>北        <i>/</i>
          2室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （33层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2535418965359075328"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="18"
  data-total="591"
  data-fb_expo_id="345219254799417363"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2535418965359075328.html"
      title="整租·欣北钱江国际广场 1室1厅 南">
        <img
          alt="整租·欣北钱江国际广场 1室1厅 南_欣北钱江国际广场租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/48c4b6b2aa48bd062aff7b5274e29fd4-060.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2535418965359075328.html">
          整租·欣北钱江国际广场 1室1厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/tangqi1/" target="_blank">塘栖</a>-<a title="欣北钱江国际广场" href="/zufang/c187352713229253/" target="_blank">欣北钱江国际广场</a>
        <i>/</i>
        54㎡
        <i>/</i>南        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （28层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">4天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2561641949723361280"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="19"
  data-total="591"
  data-fb_expo_id="345219254799417364"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2561641949723361280.html"
      title="整租·星汇花园 3室2厅 南">
        <img
          alt="整租·星汇花园 3室2厅 南_星汇花园租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/330100-inspection/prod-e7336415-4c2b-4dd4-a995-66cafe2292d3.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2561641949723361280.html">
          整租·星汇花园 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="星汇花园" href="/zufang/c188123089433077/" target="_blank">星汇花园</a>
        <i>/</i>
        90㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （33层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">4天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2473806171015233536"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="20"
  data-total="591"
  data-fb_expo_id="345219254799417365"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2473806171015233536.html"
      title="整租·玖玖国际财富中心 1室1厅 北">
        <img
          alt="整租·玖玖国际财富中心 1室1厅 北_玖玖国际财富中心租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_4AqxzqFYI.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2473806171015233536.html">
          整租·玖玖国际财富中心 1室1厅 北        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/linping/" target="_blank">临平</a>-<a title="玖玖国际财富中心" href="/zufang/c187485132386311/" target="_blank">玖玖国际财富中心</a>
        <i>/</i>
        60㎡
        <i>/</i>北        <i>/</i>
          1室1厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （23层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">1天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2316475490791063552"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="21"
  data-total="591"
  data-fb_expo_id="345219254799417350"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2316475490791063552.html"
      title="合租·远洋香奈 4居室 北卧">
        <img
          alt="合租·远洋香奈 4居室 北卧_远洋香奈租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1594966238384/c44c0f63af41830e6672899b28dfae4f.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2316475490791063552.html">
          合租·远洋香奈 4居室 北卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="远洋香奈" href="/zufang/c1811099550720/" target="_blank">远洋香奈</a>
        <i>/</i>
        6㎡
        <i>/</i>北        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （16层）
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
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>930</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2347023684717518848"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="22"
  data-total="591"
  data-fb_expo_id="345219254799417367"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2347023684717518848.html"
      title="整租·相寓 2室1厅 南">
        <img
          alt="整租·相寓 2室1厅 南_相寓租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/330100-inspection/a05f51af-50c8-4e76-976a-14021b359064.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2347023684717518848.html">
          整租·相寓 2室1厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/linping/" target="_blank">临平</a>-<a title="相寓" href="/zufang/c187485132386882/" target="_blank">相寓</a>
        <i>/</i>
        63㎡
        <i>/</i>南        <i>/</i>
          2室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （5层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">3天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2306351581484302336"
  data-brand_code="200306002283"
  data-ad_code=""
  data-c_type="1"
  data-position="23"
  data-total="591"
  data-fb_expo_id="345219254799417356"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2306351581484302336.html"
      title="合租·岸上蓝山 4居室 东南卧">
        <img
          alt="合租·岸上蓝山 4居室 东南卧_岸上蓝山租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-user-avatar/7afdc76c-25cd-4f9f-b82d-0ac980963c51.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2306351581484302336.html">
          合租·岸上蓝山 4居室 东南卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/xianlin1/" target="_blank">闲林</a>-<a title="岸上蓝山" href="/zufang/c1811099689180/" target="_blank">岸上蓝山</a>
        <i>/</i>
        16㎡
        <i>/</i>东南        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--online_sign">租住保障</i>
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            房家加公寓          </span>
                <span class="content__list--item--time oneline">19天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2524695847665401856"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="24"
  data-total="591"
  data-fb_expo_id="345219254799417369"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2524695847665401856.html"
      title="整租·萧山区阳城路78号 1室0厅 南">
        <img
          alt="整租·萧山区阳城路78号 1室0厅 南_萧山区阳城路78号租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/69a67f26d3cc716a406ad354d14ccf2f-072.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2524695847665401856.html">
          整租·萧山区阳城路78号 1室0厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/qiantangxinqu/">钱塘新区</a>-<a href="/zufang/dajiangdong/" target="_blank">大江东</a>-<a title="萧山区阳城路78号" href="/zufang/c18000000003167/" target="_blank">萧山区阳城路78号</a>
        <i>/</i>
        35㎡
        <i>/</i>南        <i>/</i>
          1室0厅1卫        <span class="hide">
          <i>/</i>
          中楼层                        （6层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>900</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2316684429332332544"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="25"
  data-total="591"
  data-fb_expo_id="345219254799417358"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2316684429332332544.html"
      title="合租·金都梧桐苑 4居室 西卧">
        <img
          alt="合租·金都梧桐苑 4居室 西卧_金都梧桐苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1596529240789/06fe957ce60160e9efc53a89632a6b69.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2316684429332332544.html">
          合租·金都梧桐苑 4居室 西卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/feicuicheng1/" target="_blank">翡翠城</a>-<a title="金都梧桐苑" href="/zufang/c1811043636340/" target="_blank">金都梧桐苑</a>
        <i>/</i>
        9㎡
        <i>/</i>西        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （18层）
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
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>960</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2528863343796551680"
  data-brand_code="200306001852"
  data-ad_code=""
  data-c_type="1"
  data-position="26"
  data-total="591"
  data-fb_expo_id="345219254799417371"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2528863343796551680.html"
      title="整租·中天珺府 3室2厅 南">
        <img
          alt="整租·中天珺府 3室2厅 南_中天珺府租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/110000-inspection/pc1_b8dc5QerQ.jpg!m_fill,w_250,h_182,l_fbk,o_auto"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                    <i class="vr-logo"></i>
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2528863343796551680.html">
          整租·中天珺府 3室2厅 南        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/linan/">临安</a>-<a href="/zufang/linan1/" target="_blank">临安</a>-<a title="中天珺府" href="/zufang/c188122743665334/" target="_blank">中天珺府</a>
        <i>/</i>
        89㎡
        <i>/</i>南        <i>/</i>
          3室2厅2卫        <span class="hide">
          <i>/</i>
          低楼层                        （11层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--two_bathroom">双卫生间</i>
            </p>
      <p class="content__list--item--brand oneline">
                <span class="content__list--item--time oneline">2天前维护</span>
      </p>
      <span class="content__list--item-price"><em>1000</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2316013140573700096"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="27"
  data-total="591"
  data-fb_expo_id="345219254799417366"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2316013140573700096.html"
      title="合租·后珠家苑 5居室 东卧">
        <img
          alt="合租·后珠家苑 5居室 东卧_后珠家苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1596585549780/2f4ba6aca34478ee90ee120fe2f3411e.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2316013140573700096.html">
          合租·后珠家苑 5居室 东卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="后珠家苑" href="/zufang/c2711051178094/" target="_blank">后珠家苑</a>
        <i>/</i>
        9㎡
        <i>/</i>东        <i>/</i>
          5室1厅2卫        <span class="hide">
          <i>/</i>
          高楼层                        （6层）
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
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>960</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2263847278798176256"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="28"
  data-total="591"
  data-fb_expo_id="345219254799417368"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2263847278798176256.html"
      title="合租·上实海上海一期 4居室 北卧">
        <img
          alt="合租·上实海上海一期 4居室 北卧_上实海上海一期租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1594894141291/10986eaf6f9779cf602bfef460f70191.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2263847278798176256.html">
          合租·上实海上海一期 4居室 北卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/yuhang/">余杭</a>-<a href="/zufang/liangzhu/" target="_blank">良渚</a>-<a title="上实海上海一期" href="/zufang/c1811063918343000/" target="_blank">上实海上海一期</a>
        <i>/</i>
        5㎡
        <i>/</i>北        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （27层）
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
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>990</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2316133611453562880"
  data-brand_code="200302002000"
  data-ad_code=""
  data-c_type="1"
  data-position="29"
  data-total="591"
  data-fb_expo_id="345219254799417370"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2316133611453562880.html"
      title="合租·新城红郡 4居室 南卧">
        <img
          alt="合租·新城红郡 4居室 南卧_新城红郡租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-house-1/ad40efae68e06d5607579210fcfcecd2-1596157036158/a9db4fc5f0742fa0996b6b6c45ff80a0.jpg.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2316133611453562880.html">
          合租·新城红郡 4居室 南卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/jianggan/">江干</a>-<a href="/zufang/dingqiao/" target="_blank">丁桥</a>-<a title="新城红郡" href="/zufang/c187624879255847/" target="_blank">新城红郡</a>
        <i>/</i>
        10㎡
        <i>/</i>南        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （22层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--decoration">精装</i>
            <i class="content__item__tag--independent_balcony">独立阳台</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            自如          </span>
                <span class="content__list--item--time oneline">5天前维护</span>
      </p>
      <span class="content__list--item-price"><em>990</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2565931780070703104"
  data-brand_code="200306001395"
  data-ad_code=""
  data-c_type="1"
  data-position="30"
  data-total="591"
  data-fb_expo_id="345219254799417372"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2565931780070703104.html"
      title="合租·嘉绿文苑 4居室 北卧">
        <img
          alt="合租·嘉绿文苑 4居室 北卧_嘉绿文苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-user-avatar/a503e81a-efdc-4aaa-8a02-a06bdecdb68a.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2565931780070703104.html">
          合租·嘉绿文苑 4居室 北卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xihu/">西湖</a>-<a href="/zufang/jialv/" target="_blank">嘉绿</a>-<a title="嘉绿文苑" href="/zufang/c1811043641703/" target="_blank">嘉绿文苑</a>
        <i>/</i>
        8㎡
        <i>/</i>北        <i>/</i>
          4室1厅2卫        <span class="hide">
          <i>/</i>
          中楼层                        （16层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--online_sign">租住保障</i>
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--rent_period_month">月租</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            橘果公寓          </span>
                <span class="content__list--item--time oneline">2天前维护</span>
      </p>
      <span class="content__list--item-price"><em>910</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2536818412890898432"
  data-brand_code="200306007984"
  data-ad_code=""
  data-c_type="1"
  data-position="31"
  data-total="591"
  data-fb_expo_id="345219254799417373"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2536818412890898432.html"
      title="合租·吉庆院 3居室 南卧">
        <img
          alt="合租·吉庆院 3居室 南卧_吉庆院租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-user-avatar/9c509692-6d3a-485c-84f4-65833dab87e5.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2536818412890898432.html">
          合租·吉庆院 3居室 南卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/gongshu/">拱墅</a>-<a href="/zufang/gongchenqiao/" target="_blank">拱宸桥</a>-<a title="吉庆院" href="/zufang/c1811043636841/" target="_blank">吉庆院</a>
        <i>/</i>
        12㎡
        <i>/</i>南        <i>/</i>
          3室1厅1卫        <span class="hide">
          <i>/</i>
          高楼层                        （7层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            杭州-世纪鸿源          </span>
                <span class="content__list--item--time oneline">22天前维护</span>
      </p>
      <span class="content__list--item-price"><em>950</em> 元/月</span>
    </div>

</div>
<div
  class="content__list--item"
  data-el="listItem"
  data-house_code="HZ2566672562247434240"
  data-brand_code="200306001395"
  data-ad_code=""
  data-c_type="1"
  data-position="32"
  data-total="591"
  data-fb_expo_id="345219254799417374"
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
      class="content__list--item--aside" target="_blank"      href="/zufang/HZ2566672562247434240.html"
      title="合租·嘉绿文苑 4居室 西卧">
        <img
          alt="合租·嘉绿文苑 4居室 西卧_嘉绿文苑租房"
          src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/default/250-182.png?_v=20200806113746ed7"
          data-src="https://ke-image.ljcdn.com/rent-user-avatar/3ead1845-9e26-4f45-b92d-52abbfe5d473.250x182.jpg"
          class="lazyload">
        <!-- 是否展示vr图片 -->
                <!-- 广告标签 -->
            </a>
    <div class="content__list--item--main">
      <p class="content__list--item--title twoline">
        <a target="_blank" href="/zufang/HZ2566672562247434240.html">
          合租·嘉绿文苑 4居室 西卧        </a>
      </p>
      <p class="content__list--item--des">
        <a target="_blank" href="/zufang/xihu/">西湖</a>-<a href="/zufang/jialv/" target="_blank">嘉绿</a>-<a title="嘉绿文苑" href="/zufang/c1811043641703/" target="_blank">嘉绿文苑</a>
        <i>/</i>
        10㎡
        <i>/</i>西        <i>/</i>
          4室1厅1卫        <span class="hide">
          <i>/</i>
          低楼层                        （16层）
                  </span>
      </p>
      <p class="content__list--item--bottom oneline">
            <i class="content__item__tag--online_sign">租住保障</i>
            <i class="content__item__tag--authorization_apartment">公寓</i>
            <i class="content__item__tag--is_subway_house">近地铁</i>
            <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
            <i class="content__item__tag--is_key">随时看房</i>
            </p>
      <p class="content__list--item--brand oneline">
                  <span class="brand">
            橘果公寓          </span>
                <span class="content__list--item--time oneline">25天前维护</span>
      </p>
      <span class="content__list--item-price"><em>910</em> 元/月</span>
    </div>

</div>
        </div>

        <!-- 列表分页模块 -->
        <div class="content__pg" data-el="page_navigation" data-url="/zufang/pg{page}rp1/" data-totalPage=20 data-curPage=1>
        </div>

        <ul style="display:hidden">
                      <li><a href="/zufang/pg2rp1/"></a></li>
                      <li><a href="/zufang/pg3rp1/"></a></li>
                      <li><a href="/zufang/pg4rp1/"></a></li>
                      <li><a href="/zufang/pg5rp1/"></a></li>
                      <li><a href="/zufang/pg6rp1/"></a></li>
                      <li><a href="/zufang/pg7rp1/"></a></li>
                      <li><a href="/zufang/pg8rp1/"></a></li>
                      <li><a href="/zufang/pg9rp1/"></a></li>
                      <li><a href="/zufang/pg10rp1/"></a></li>
                      <li><a href="/zufang/pg11rp1/"></a></li>
                      <li><a href="/zufang/pg12rp1/"></a></li>
                      <li><a href="/zufang/pg13rp1/"></a></li>
                      <li><a href="/zufang/pg14rp1/"></a></li>
                      <li><a href="/zufang/pg15rp1/"></a></li>
                      <li><a href="/zufang/pg16rp1/"></a></li>
                      <li><a href="/zufang/pg17rp1/"></a></li>
                      <li><a href="/zufang/pg18rp1/"></a></li>
                      <li><a href="/zufang/pg19rp1/"></a></li>
                      <li><a href="/zufang/pg20rp1/"></a></li>
                  </ul>

      
          </div>

          <div class="content__aside">
        

<div class="download">
  
  <div class="qr-code">
          <img width="94" height="94" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/getDownloadQr.png?_v=20200806113746ed7" alt="下载贝壳APP">
        <div class="title">下载贝壳APP</div>
    <div class="text">
      <p>扫描上方二维码</p>
      <p>随时查看新房源</p>
      <p class="get-more">
        <a href="//www.ke.com/client/">了解更多
          <img width="9" height="9" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEUAAACcn6Gfn5+an5+bnqCbnqGfn5+cn6EV6DbuAAAAB3RSTlMA0BAw8LAgvf5k9AAAAEdJREFUKM9jIBOkBqMJhBcqoAmUC6EKmJSjKWEWR1eiiK6ECZsSA3QlzuhKSihRghDA0EJ/BWIoCgzh4YMIZALRYBrMQAkAAF5bGMBkrwzqAAAAAElFTkSuQmCC">
        </a>
      </p>
    </div>
  </div>
</div>
        <div class="download">
  <div class="qr-code">
    <img width="94" height="94" src="http://image1.ljcdn.com/params-compact/f871e2c517a63630ce5894caa5804464.jpeg" alt="贝壳小程序">
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
  <a href="/zufang/rp1/"></a>
  <a href="/zufang/pg2rp1/"></a>
  <a href="/zufang/pg3rp1/"></a>
  <a href="/zufang/pg4rp1/"></a>
  <a href="/zufang/pg5rp1/"></a>
  <a href="/zufang/pg6rp1/"></a>
  <a href="/zufang/pg7rp1/"></a>
  <a href="/zufang/pg8rp1/"></a>
  <a href="/zufang/pg9rp1/"></a>
  <a href="/zufang/pg10rp1/"></a>
</div>

<!-- 检索出房源结果时，添加检索id埋点 -->
<input type="hidden" id="queryId" value="345219254799417344">

<!-- 底部留资弹窗 -->
<div data-el="fix-bottom-pop" class="fix-bottom-wrap">
  <div class="bottom-content">
    <img class="left-img" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/resource/img/bg_agent@2x.png?_v=20200806113746ed7" alt="底部找房图片">
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
</div><script src="https://s1.ljcdn.com/agent-sj-sdk/1.2.0/agent-sj-sdk.js"></script>
<script>
    g_conf.pageId = 'rentalList';
  g_conf.requestId = '8101436856681';
  g_conf.resblockId ='';
  g_conf.total = '591';
  g_conf.cityId = '330100'
  var __requireList = ['https://s1.ljcdn.com/matrix_pc/dist/pc/src/page/list/index.js?_v=20200806113746ed7'];
  document.getElementById('clearUrl').href = '/zufang/rp1brp{min}erp{max}/'.split('zufang/')[0] + 'zufang/';

</script>
  </div>

  <!-- 登录弹窗 -->
  <!--登录-->
<div class="loninContaner">
     <!-- 扫码登录入口 -->
    <div class="qr_code_login" data-el="qr_code_login">
        <div class="left-text-info"></div> 
        <div class="right-img-info"></div> 
    </div>
    <!-- 密码登录入口 -->
    <div class="pass_word_login code_user_single" data-el="pass_word_login">
        <div class="left-text-info"></div> 
        <div class="right-img-info"></div> 
    </div>
    <!--mask-->
    <div class="overlay_bg" style="display: none;"></div>
    <!--账号密码登录-->
    <div id="dialog" class="panel_login animated">
        <div class="panel_info">
            <!-- 关闭按钮 -->
            <i class="close_login"></i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">账号密码登录</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"><em class="password-view"></em>
                            </li>
                            <li class="item checkVerimg" style="display:none;">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a>
                            </li>
                            <li class="li_btn"><a class="login-user-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机快捷登录-->
    <div id="dialog_tel" class="panel_login animated btn-login bounceIn actLoginBtn" style="display: none;">
        <div class="panel_info">
            <i class="close_login"></i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机快捷登录</div>
                    <div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> -->
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg" src="https://upassport.lianjia.com/freshCaptch?t=1517466208641">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label>
                            </li>
                            <li class="li_btn"><a class="login-user-tel-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机号码注册-->
    <div id="dialog_reg" class="panel_login animated">
        <div class="panel_info">
            <i class="close_login"></i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机号码注册</div>
                    <label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a>
                    </label>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_reg">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_reg" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-c Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked=""></span>我已阅读并同意</label>
                                                                  <a class="toprotocol" href="//www.ke.com/zhuanti/protocol" target="_blank">《贝壳用户使用协议》</a>
                                  及
                                  <a class="toprotocol" href="//www.ke.com/zhuanti/serviceProtocol" target="_blank">《贝壳用户服务协议》</a>
                                                            </li>
                            <li class="li_btn"><a class="register-user-btn">注册</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--找回密码-->
    <div id="dialog_forget" class="panel_login animated">
        <div class="panel_info">
            <i class="close_login"></i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">找回密码</div>
                </div>
                <div class="clear"></div>
                <div id="con_forget_user_tel" class="con_forget_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-t pwd" style="margin-top:-1px;">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="user-forget">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_forget_user_pw" class="con_forget_user_pw">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="modify-user-pswd">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!-- 微信小程序登录 -->
    <div id="dialog_qr_code" data-el="dialog_qr_code" class="panel_login panel_qr_login animated">
        <div class="panel_info panel_qr_info">
            <!-- 关闭按钮 -->
            <i class="close_login"></i>
            <!-- 弹窗内容 -->
            <div class="panel-content">
                <div class="beike_img_logo"></div>
                <img 
                    alt="贝壳小程序"
                    class="qr_code_img"
                    data-el="qr_code_img"
                    src="http://image1.ljcdn.com/params-compact/f871e2c517a63630ce5894caa5804464.jpeg">
                <a href="javascript:void(0)" class="user_info_entry">找房太难？试试帮我找房</a>
                <p>
                    扫码登录<span class="bottom_text">贝壳找房小程序，</span>了解更多房源详情
                </p>
            </div>

        </div>
    </div>
    <!-- 留资弹窗 -->
    <div id="dialog_user_info" data-el="dialog_user_info" class="panel_login panel_qr_login animated">
        <div class="panel_info panel_qr_info">
            <!-- 关闭按钮 -->
            <i class="close_login"></i>
            <!-- 弹窗内容 -->
            <div class="panel-content">
                <div class="img_logo"></div>
                <div class="user_info_text">找房太难？留下您的手机号为您推荐专业的找房顾问。</div>
                <div id="user_info_form" class="user_info_form panel_tab">
                    <form action="" method="post">
                        <ul>
                            <li>
                                <input type="text" name="user_phone" class="the_input form_item" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li>
                                <input type="text" name="user_remark" class="the_input form_item" placeholder="您的需求是？" maxlength="50">
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                        </ul>
                    </form>
                </div>
                <div class="user_info_bottom">
                    <button 
                        data-el="user_info_btn"
                        data-city_id="330100"
                        class="user_info_btn">提交</button>
                    <input class="user_info_radio" checked type="radio" name="agree"/>
                    <label class="user_info_label" htmlFor="agree"></label>
                    <span class="user_info_agree">提交即代表同意</span>
                    <a class="user_info_page" href="//www.ke.com/zhuanti/serviceProtocol">
                        《贝壳用户服务协议》                    </a>
                    <p class="user_info_desc">提交后租房顾问将与您电话联系并提供服务</p> 
                </div>
            </div>
        </div>
    </div>
    <!-- 留资成功弹窗 -->
    <div id="dialog_user_info_success" data-el="dialog_user_info_success" class="panel_login panel_qr_login animated">
        <div class="panel_info panel_qr_info">
            <!-- 关闭按钮 -->
            <i class="close_login"></i>
            <!-- 弹窗内容 -->
            <div class="panel-content">
                <div class="success_img_logo"></div>
                <div class="success_user_info_text">提交成功</div>
                <div class="success_agent_phone">
                经纪人将第一时间为您提供专属服务，请注意来电
                </div>
                <div class="user_info_success_bottom">
                    <button 
                        data-el="user_info_success_btn"
                        class="user_info_success_btn">确定</button>
                </div>
            </div>
        </div>
    </div>
</div>

    <div class="footer">
    <div class="footer__wrapper w1150">

      <div class="footer__top">
        <ul class="footer__light">
                    <li><a href="/wzdt/">网站地图</a></li>
                  </ul>
        <a class="footer__aside hide" href="tel:10109666">客服电话<span>10109666</span></a>
      </div>

      <div class="footer__middle">
        <ul data-el="parentList">
                      <li><a class="cur" data-index="0" target="_blank">热门商圈</a></li>
                      <li><a class="" data-index="1" target="_blank">推荐小区</a></li>
                      <li><a class="" data-index="2" target="_blank">租房城市</a></li>
                  </ul>
                  <ul data-el="childrenList"  style="display:block">
                          <li><a href="https://hz.zu.ke.com/zufang/changqing1112/" target="_blank">长庆租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/nanxing/" target="_blank">南星租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/fuxing/" target="_blank">复兴租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/renhe2/" target="_blank">仁和租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/wenyixilu/" target="_blank">文一西路租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/qingtai/" target="_blank">清泰租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/xixing/" target="_blank">西兴租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/yiqiao/" target="_blank">义桥租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jiande1/" target="_blank">建德租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jiubao/" target="_blank">九堡租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/wandaguangchang2/" target="_blank">万达广场租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/huanglong/" target="_blank">黄龙租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/gudang/" target="_blank">古荡租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/hemu/" target="_blank">和睦租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/xixi/" target="_blank">西溪租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/gongchenqiao/" target="_blank">拱宸桥租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/feicuicheng1/" target="_blank">翡翠城租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/wulin11/" target="_blank">武林租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/tianshui1/" target="_blank">天水租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/dajiangdong/" target="_blank">大江东租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/caihongcheng/" target="_blank">彩虹城租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/huajiachi/" target="_blank">华家池租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/shenhua/" target="_blank">申花租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/sichoucheng1/" target="_blank">丝绸城租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/hubin1/" target="_blank">湖滨租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jianqiao/" target="_blank">笕桥租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/banshan/" target="_blank">半山租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/puyan/" target="_blank">浦沿租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/santang/" target="_blank">三塘租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/changhe/" target="_blank">长河租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/sandun/" target="_blank">三墩租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/gouzhuang/" target="_blank">勾庄租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/yanjiangbei/" target="_blank">沿江北租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/gudang/" target="_blank">古荡租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/huochedongzhan/" target="_blank">火车东站租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/yiqiao/" target="_blank">义桥租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/xiongzhenlou/" target="_blank">雄镇楼租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/dingqiao/" target="_blank">丁桥租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jinjiang1/" target="_blank">近江租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/liangzhu/" target="_blank">良渚租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/deshengdong/" target="_blank">德胜东租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/changhe/" target="_blank">长河租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/fuyang1/" target="_blank">富阳租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/daguan/" target="_blank">大关租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/heping2/" target="_blank">和平租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/xuejun/" target="_blank">学军租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/linpu/" target="_blank">临浦租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/tonglushangquan/" target="_blank">桐庐租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/zhanongkou/" target="_blank">闸弄口租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jialv/" target="_blank">嘉绿租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/qingtai/" target="_blank">清泰租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jingfang1/" target="_blank">景芳租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/dajiangdong/" target="_blank">大江东租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/santang/" target="_blank">三塘租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/wenyixilu/" target="_blank">文一西路租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/xianlin1/" target="_blank">闲林租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/yanjiangnan/" target="_blank">沿江南租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/fuxing/" target="_blank">复兴租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/jinshahu/" target="_blank">金沙湖租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/liuxia1/" target="_blank">留下租房</a></li>
                      </ul>
                  <ul data-el="childrenList"  >
                          <li><a href="https://hz.zu.ke.com/zufang/c1820022260637977/" target="_blank">大通路98号租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043641307/" target="_blank">嘉绿福苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043636713/" target="_blank">和睦公寓租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1820022037245901/" target="_blank">解放路8号租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1820024445699943/" target="_blank">水岸鑫域租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043641703/" target="_blank">嘉绿文苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1815909850746844/" target="_blank">小河东河下66-11号租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1815440795176902/" target="_blank">永泰名苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043636393/" target="_blank">五洋东湖春天租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043641388/" target="_blank">武林门新村租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1815732752026627/" target="_blank">佑圣观路5号租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043638833/" target="_blank">云峰一区租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1820023393475872/" target="_blank">保利融信大国璟租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043639425/" target="_blank">广景苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043638496/" target="_blank">裕园公寓租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043636559/" target="_blank">湖墅北路101号租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043641404/" target="_blank">紫金公寓租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043641620/" target="_blank">金沙曲苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1820023902308543/" target="_blank">环城东路240号租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1820022536418987/" target="_blank">金隅空港公馆租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1815710271606474/" target="_blank">绿野清风租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043640426/" target="_blank">碧桂苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043641555/" target="_blank">筑品金座租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043637400/" target="_blank">大关东六苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043636769/" target="_blank">沈大北苑小区租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043642186/" target="_blank">天水巷租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043642200/" target="_blank">灯塔东苑租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043636635/" target="_blank">石油公寓租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043639517/" target="_blank">联合格里租房</a></li>
                          <li><a href="https://hz.zu.ke.com/zufang/c1811043635924/" target="_blank">知本大厦租房</a></li>
                      </ul>
                  <ul data-el="childrenList"  >
                          <li><a href="https://jn.zu.ke.com/zufang/" target="_blank">济南租房</a></li>
                          <li><a href="https://linyi.zu.ke.com/zufang/" target="_blank">临沂租房</a></li>
                          <li><a href="https://huzhou.zu.ke.com/zufang/" target="_blank">湖州租房</a></li>
                          <li><a href="https://wuhu.zu.ke.com/zufang/" target="_blank">芜湖租房</a></li>
                          <li><a href="https://nanchong.zu.ke.com/zufang/" target="_blank">南充租房</a></li>
                          <li><a href="https://xa.zu.ke.com/zufang/" target="_blank">西安租房</a></li>
                          <li><a href="https://gz.zu.ke.com/zufang/" target="_blank">广州租房</a></li>
                          <li><a href="https://zh.zu.ke.com/zufang/" target="_blank">珠海租房</a></li>
                          <li><a href="https://san.zu.ke.com/zufang/" target="_blank">三亚租房</a></li>
                          <li><a href="https://sjz.zu.ke.com/zufang/" target="_blank">石家庄租房</a></li>
                          <li><a href="https://xc.zu.ke.com/zufang/" target="_blank">许昌租房</a></li>
                          <li><a href="https://zj.zu.ke.com/zufang/" target="_blank">镇江租房</a></li>
                          <li><a href="https://baoji.zu.ke.com/zufang/" target="_blank">宝鸡租房</a></li>
                          <li><a href="https://yc.zu.ke.com/zufang/" target="_blank">盐城租房</a></li>
                          <li><a href="https://zz.zu.ke.com/zufang/" target="_blank">郑州租房</a></li>
                          <li><a href="https://dd.zu.ke.com/zufang/" target="_blank">丹东租房</a></li>
                          <li><a href="https://sh.zu.ke.com/zufang/" target="_blank">上海租房</a></li>
                          <li><a href="https://wf.zu.ke.com/zufang/" target="_blank">潍坊租房</a></li>
                          <li><a href="https://ts.zu.ke.com/zufang/" target="_blank">唐山租房</a></li>
                          <li><a href="https://bj.zu.ke.com/zufang/" target="_blank">北京租房</a></li>
                          <li><a href="https://liangshan.zu.ke.com/zufang/" target="_blank">凉山租房</a></li>
                          <li><a href="https://gy.zu.ke.com/zufang/" target="_blank">贵阳租房</a></li>
                          <li><a href="https://dazhou.zu.ke.com/zufang/" target="_blank">达州租房</a></li>
                          <li><a href="https://hanzhong.zu.ke.com/zufang/" target="_blank">汉中租房</a></li>
                          <li><a href="https://nb.zu.ke.com/zufang/" target="_blank">宁波租房</a></li>
                          <li><a href="https://cs.zu.ke.com/zufang/" target="_blank">长沙租房</a></li>
                          <li><a href="https://wh.zu.ke.com/zufang/" target="_blank">武汉租房</a></li>
                          <li><a href="https://xan.zu.ke.com/zufang/" target="_blank">雄安新区租房</a></li>
                          <li><a href="https://cq.zu.ke.com/zufang/" target="_blank">重庆租房</a></li>
                          <li><a href="https://tj.zu.ke.com/zufang/" target="_blank">天津租房</a></li>
                          <li><a href="https://ganzhou.zu.ke.com/zufang/" target="_blank">赣州租房</a></li>
                          <li><a href="https://yt.zu.ke.com/zufang/" target="_blank">烟台租房</a></li>
                          <li><a href="https://huzhou.zu.ke.com/zufang/" target="_blank">湖州租房</a></li>
                          <li><a href="https://hui.zu.ke.com/zufang/" target="_blank">惠州租房</a></li>
                          <li><a href="https://ms.zu.ke.com/zufang/" target="_blank">眉山租房</a></li>
                          <li><a href="https://nb.zu.ke.com/zufang/" target="_blank">宁波租房</a></li>
                          <li><a href="https://qd.zu.ke.com/zufang/" target="_blank">青岛租房</a></li>
                          <li><a href="https://zjk.zu.ke.com/zufang/" target="_blank">张家口租房</a></li>
                          <li><a href="https://jx.zu.ke.com/zufang/" target="_blank">嘉兴租房</a></li>
                          <li><a href="https://dd.zu.ke.com/zufang/" target="_blank">丹东租房</a></li>
                          <li><a href="https://yy.zu.ke.com/zufang/" target="_blank">岳阳租房</a></li>
                          <li><a href="https://xa.zu.ke.com/zufang/" target="_blank">西安租房</a></li>
                          <li><a href="https://nanchong.zu.ke.com/zufang/" target="_blank">南充租房</a></li>
                          <li><a href="https://zh.zu.ke.com/zufang/" target="_blank">珠海租房</a></li>
                          <li><a href="https://km.zu.ke.com/zufang/" target="_blank">昆明租房</a></li>
                          <li><a href="https://cq.zu.ke.com/zufang/" target="_blank">重庆租房</a></li>
                          <li><a href="https://changzhou.zu.ke.com/zufang/" target="_blank">常州租房</a></li>
                          <li><a href="https://san.zu.ke.com/zufang/" target="_blank">三亚租房</a></li>
                          <li><a href="https://linyi.zu.ke.com/zufang/" target="_blank">临沂租房</a></li>
                          <li><a href="https://cs.zu.ke.com/zufang/" target="_blank">长沙租房</a></li>
                          <li><a href="https://ez.zu.ke.com/zufang/" target="_blank">鄂州租房</a></li>
                          <li><a href="https://sx.zu.ke.com/zufang/" target="_blank">绍兴租房</a></li>
                          <li><a href="https://ks.zu.ke.com/zufang/" target="_blank">昆山租房</a></li>
                          <li><a href="https://tj.zu.ke.com/zufang/" target="_blank">天津租房</a></li>
                          <li><a href="https://jiujiang.zu.ke.com/zufang/" target="_blank">九江租房</a></li>
                          <li><a href="https://jn.zu.ke.com/zufang/" target="_blank">济南租房</a></li>
                          <li><a href="https://hk.zu.ke.com/zufang/" target="_blank">海口租房</a></li>
                          <li><a href="https://wuhu.zu.ke.com/zufang/" target="_blank">芜湖租房</a></li>
                          <li><a href="https://bj.zu.ke.com/zufang/" target="_blank">北京租房</a></li>
                          <li><a href="https://ty.zu.ke.com/zufang/" target="_blank">太原租房</a></li>
                      </ul>
              </div>

      <div class="footer__bottom">
        <p>天津小屋信息科技有限公司 | <a style="color: #B7BBC3" href="http://beian.miit.gov.cn">津ICP备18000836号</a> |  &copy; Copyright &copy; 2020 ke.com版权所有</p>
        <p class="hide">京公网安备 11010802024019号</p>
      </div>

    </div>
  </div>

<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"title":"\u70ed\u95e8\u5546\u5708","city_id":330100,"abbr":"rmsq","source":"m","children":[{"url":"https:\/\/hz.zu.ke.com\/zufang\/changqing1112\/","title":"\u957f\u5e86\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/nanxing\/","title":"\u5357\u661f\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/fuxing\/","title":"\u590d\u5174\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/renhe2\/","title":"\u4ec1\u548c\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/wenyixilu\/","title":"\u6587\u4e00\u897f\u8def\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/xixing\/","title":"\u897f\u5174\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/yiqiao\/","title":"\u4e49\u6865\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jiande1\/","title":"\u5efa\u5fb7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jiubao\/","title":"\u4e5d\u5821\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/wandaguangchang2\/","title":"\u4e07\u8fbe\u5e7f\u573a\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/huanglong\/","title":"\u9ec4\u9f99\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/gudang\/","title":"\u53e4\u8361\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/hemu\/","title":"\u548c\u7766\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/xixi\/","title":"\u897f\u6eaa\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/gongchenqiao\/","title":"\u62f1\u5bb8\u6865\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/feicuicheng1\/","title":"\u7fe1\u7fe0\u57ce\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/wulin11\/","title":"\u6b66\u6797\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/tianshui1\/","title":"\u5929\u6c34\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/dajiangdong\/","title":"\u5927\u6c5f\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/caihongcheng\/","title":"\u5f69\u8679\u57ce\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/huajiachi\/","title":"\u534e\u5bb6\u6c60\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/shenhua\/","title":"\u7533\u82b1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/sichoucheng1\/","title":"\u4e1d\u7ef8\u57ce\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/hubin1\/","title":"\u6e56\u6ee8\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jianqiao\/","title":"\u7b15\u6865\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/banshan\/","title":"\u534a\u5c71\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/puyan\/","title":"\u6d66\u6cbf\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/santang\/","title":"\u4e09\u5858\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/sandun\/","title":"\u4e09\u58a9\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/gouzhuang\/","title":"\u52fe\u5e84\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/yanjiangbei\/","title":"\u6cbf\u6c5f\u5317\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/gudang\/","title":"\u53e4\u8361\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/huochedongzhan\/","title":"\u706b\u8f66\u4e1c\u7ad9\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/yiqiao\/","title":"\u4e49\u6865\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/xiongzhenlou\/","title":"\u96c4\u9547\u697c\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/dingqiao\/","title":"\u4e01\u6865\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jinjiang1\/","title":"\u8fd1\u6c5f\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/liangzhu\/","title":"\u826f\u6e1a\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/deshengdong\/","title":"\u5fb7\u80dc\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/changhe\/","title":"\u957f\u6cb3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/fuyang1\/","title":"\u5bcc\u9633\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/daguan\/","title":"\u5927\u5173\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/heping2\/","title":"\u548c\u5e73\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/xuejun\/","title":"\u5b66\u519b\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/linpu\/","title":"\u4e34\u6d66\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/tonglushangquan\/","title":"\u6850\u5e90\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/zhanongkou\/","title":"\u95f8\u5f04\u53e3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jialv\/","title":"\u5609\u7eff\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/qingtai\/","title":"\u6e05\u6cf0\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jingfang1\/","title":"\u666f\u82b3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/dajiangdong\/","title":"\u5927\u6c5f\u4e1c\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/santang\/","title":"\u4e09\u5858\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/wenyixilu\/","title":"\u6587\u4e00\u897f\u8def\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/xianlin1\/","title":"\u95f2\u6797\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/yanjiangnan\/","title":"\u6cbf\u6c5f\u5357\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/fuxing\/","title":"\u590d\u5174\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/jinshahu\/","title":"\u91d1\u6c99\u6e56\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/liuxia1\/","title":"\u7559\u4e0b\u79df\u623f"}]},{"title":"\u63a8\u8350\u5c0f\u533a","city_id":330100,"abbr":"tjxq","source":"m","children":[{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1820022260637977\/","title":"\u5927\u901a\u8def98\u53f7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043641307\/","title":"\u5609\u7eff\u798f\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043636713\/","title":"\u548c\u7766\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1820022037245901\/","title":"\u89e3\u653e\u8def8\u53f7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1820024445699943\/","title":"\u6c34\u5cb8\u946b\u57df\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043641703\/","title":"\u5609\u7eff\u6587\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1815909850746844\/","title":"\u5c0f\u6cb3\u4e1c\u6cb3\u4e0b66-11\u53f7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1815440795176902\/","title":"\u6c38\u6cf0\u540d\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043636393\/","title":"\u4e94\u6d0b\u4e1c\u6e56\u6625\u5929\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043641388\/","title":"\u6b66\u6797\u95e8\u65b0\u6751\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1815732752026627\/","title":"\u4f51\u5723\u89c2\u8def5\u53f7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043638833\/","title":"\u4e91\u5cf0\u4e00\u533a\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1820023393475872\/","title":"\u4fdd\u5229\u878d\u4fe1\u5927\u56fd\u749f\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043639425\/","title":"\u5e7f\u666f\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043638496\/","title":"\u88d5\u56ed\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043636559\/","title":"\u6e56\u5885\u5317\u8def101\u53f7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043641404\/","title":"\u7d2b\u91d1\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043641620\/","title":"\u91d1\u6c99\u66f2\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1820023902308543\/","title":"\u73af\u57ce\u4e1c\u8def240\u53f7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1820022536418987\/","title":"\u91d1\u9685\u7a7a\u6e2f\u516c\u9986\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1815710271606474\/","title":"\u7eff\u91ce\u6e05\u98ce\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043640426\/","title":"\u78a7\u6842\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043641555\/","title":"\u7b51\u54c1\u91d1\u5ea7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043637400\/","title":"\u5927\u5173\u4e1c\u516d\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043636769\/","title":"\u6c88\u5927\u5317\u82d1\u5c0f\u533a\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043642186\/","title":"\u5929\u6c34\u5df7\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043642200\/","title":"\u706f\u5854\u4e1c\u82d1\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043636635\/","title":"\u77f3\u6cb9\u516c\u5bd3\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043639517\/","title":"\u8054\u5408\u683c\u91cc\u79df\u623f"},{"url":"https:\/\/hz.zu.ke.com\/zufang\/c1811043635924\/","title":"\u77e5\u672c\u5927\u53a6\u79df\u623f"}]},{"title":"\u79df\u623f\u57ce\u5e02","city_id":330100,"abbr":"zfcs","source":"m","children":[{"url":"https:\/\/jn.zu.ke.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/linyi.zu.ke.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/huzhou.zu.ke.com\/zufang\/","title":"\u6e56\u5dde\u79df\u623f"},{"url":"https:\/\/wuhu.zu.ke.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/nanchong.zu.ke.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/xa.zu.ke.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/gz.zu.ke.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/zh.zu.ke.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/san.zu.ke.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/sjz.zu.ke.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/xc.zu.ke.com\/zufang\/","title":"\u8bb8\u660c\u79df\u623f"},{"url":"https:\/\/zj.zu.ke.com\/zufang\/","title":"\u9547\u6c5f\u79df\u623f"},{"url":"https:\/\/baoji.zu.ke.com\/zufang\/","title":"\u5b9d\u9e21\u79df\u623f"},{"url":"https:\/\/yc.zu.ke.com\/zufang\/","title":"\u76d0\u57ce\u79df\u623f"},{"url":"https:\/\/zz.zu.ke.com\/zufang\/","title":"\u90d1\u5dde\u79df\u623f"},{"url":"https:\/\/dd.zu.ke.com\/zufang\/","title":"\u4e39\u4e1c\u79df\u623f"},{"url":"https:\/\/sh.zu.ke.com\/zufang\/","title":"\u4e0a\u6d77\u79df\u623f"},{"url":"https:\/\/wf.zu.ke.com\/zufang\/","title":"\u6f4d\u574a\u79df\u623f"},{"url":"https:\/\/ts.zu.ke.com\/zufang\/","title":"\u5510\u5c71\u79df\u623f"},{"url":"https:\/\/bj.zu.ke.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/liangshan.zu.ke.com\/zufang\/","title":"\u51c9\u5c71\u79df\u623f"},{"url":"https:\/\/gy.zu.ke.com\/zufang\/","title":"\u8d35\u9633\u79df\u623f"},{"url":"https:\/\/dazhou.zu.ke.com\/zufang\/","title":"\u8fbe\u5dde\u79df\u623f"},{"url":"https:\/\/hanzhong.zu.ke.com\/zufang\/","title":"\u6c49\u4e2d\u79df\u623f"},{"url":"https:\/\/nb.zu.ke.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/cs.zu.ke.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/wh.zu.ke.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/xan.zu.ke.com\/zufang\/","title":"\u96c4\u5b89\u65b0\u533a\u79df\u623f"},{"url":"https:\/\/cq.zu.ke.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/tj.zu.ke.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/ganzhou.zu.ke.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/yt.zu.ke.com\/zufang\/","title":"\u70df\u53f0\u79df\u623f"},{"url":"https:\/\/huzhou.zu.ke.com\/zufang\/","title":"\u6e56\u5dde\u79df\u623f"},{"url":"https:\/\/hui.zu.ke.com\/zufang\/","title":"\u60e0\u5dde\u79df\u623f"},{"url":"https:\/\/ms.zu.ke.com\/zufang\/","title":"\u7709\u5c71\u79df\u623f"},{"url":"https:\/\/nb.zu.ke.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/qd.zu.ke.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/zjk.zu.ke.com\/zufang\/","title":"\u5f20\u5bb6\u53e3\u79df\u623f"},{"url":"https:\/\/jx.zu.ke.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/dd.zu.ke.com\/zufang\/","title":"\u4e39\u4e1c\u79df\u623f"},{"url":"https:\/\/yy.zu.ke.com\/zufang\/","title":"\u5cb3\u9633\u79df\u623f"},{"url":"https:\/\/xa.zu.ke.com\/zufang\/","title":"\u897f\u5b89\u79df\u623f"},{"url":"https:\/\/nanchong.zu.ke.com\/zufang\/","title":"\u5357\u5145\u79df\u623f"},{"url":"https:\/\/zh.zu.ke.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/km.zu.ke.com\/zufang\/","title":"\u6606\u660e\u79df\u623f"},{"url":"https:\/\/cq.zu.ke.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/changzhou.zu.ke.com\/zufang\/","title":"\u5e38\u5dde\u79df\u623f"},{"url":"https:\/\/san.zu.ke.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/linyi.zu.ke.com\/zufang\/","title":"\u4e34\u6c82\u79df\u623f"},{"url":"https:\/\/cs.zu.ke.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/ez.zu.ke.com\/zufang\/","title":"\u9102\u5dde\u79df\u623f"},{"url":"https:\/\/sx.zu.ke.com\/zufang\/","title":"\u7ecd\u5174\u79df\u623f"},{"url":"https:\/\/ks.zu.ke.com\/zufang\/","title":"\u6606\u5c71\u79df\u623f"},{"url":"https:\/\/tj.zu.ke.com\/zufang\/","title":"\u5929\u6d25\u79df\u623f"},{"url":"https:\/\/jiujiang.zu.ke.com\/zufang\/","title":"\u4e5d\u6c5f\u79df\u623f"},{"url":"https:\/\/jn.zu.ke.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/hk.zu.ke.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/wuhu.zu.ke.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/bj.zu.ke.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/ty.zu.ke.com\/zufang\/","title":"\u592a\u539f\u79df\u623f"}]}]))

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
          "imAppid": "BEIKEZUFANG_WEB_20180809",
          "imAppkey": "f176ed588131309cb6fd3277bf5edf93"
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
    "@id": "https%3A%2F%2Fhz.zu.ke.com%2Fzufang%2Frp1%2F",
    "appid": "1597146525691227",
    "pubDate": "2020-08-10T14:58:04",
    "upDate": "2020-08-10T14:58:04"
  }
</script>


<!-- 页面依赖JS加载 -->

<!-- common.js线上引入灯塔 -->
  <script type="text/javascript" src="https://s1.ljcdn.com/matrix_pc/dist/pc/src/common/common.js?_v=20200806113746ed7" crossorigin="anonymous"></script>

<script>
  var __basePath = 'https://s1.ljcdn.com/matrix_pc/dist/pc/src?_v=20200806113746ed7'.split("?") || [];
  require.config({
    //baseUrl: __basePath[0],
    paths: {
    },
    urlArgs:  __basePath[1],
    crossorigin: Boolean('1') //线上环境加该属性,需要再amd.js中单独配置一下
  });
  var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_pc\/dist\/pc","version":"20200806113746ed7","js_ns":"m_pages_zufangSearch","cur_city_id":"330100","cur_city_name":"\u676d\u5dde","cur_city_short":"hz"}
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
window.__UDL_CONFIG.pid = window.__UDL_CONFIG.pid || "bigc_pc_rent"
window.__UDL_CONFIG.env = ('prod' === 'prod' ? "dac" : 'test')
window.__UDL_CONFIG["uicode"] = g_conf.pageId || ''

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
url = r'https://hz.qk365.com/list/r0-t500'

ret = requests.get(url)
print(ret)
# print(ret.text)

html = etree.HTML(str_1)
# 获取价格
data = html.xpath("//span[@class='content__list--item-price']/em")
print(data)
print(len(data))
# 获取位置
data_1 = html.xpath("//p[@class='content__list--item--des']/a")
print(data_1)
print(len(data_1))
