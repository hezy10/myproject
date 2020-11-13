# coding=utf-8
import requests
import re
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '85.0.4183.83 Safari/537.36'
}
kw = input('输入要抓取的贴吧名:')
pn = int(input('输入要爬取的页数:'))

url = 'https://tieba.baidu.com/f?'
for i in range(1,pn+1):
    response = requests.get(url,params={'kw':kw,'pn':(i-1)*50},headers=headers)
    print(response.url)
html_str = '''
D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/秦时明月.py"

<!DOCTYPE html>
<!--STATUS OK-->
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <link rel="search" type="application/opensearchdescription+xml" href="/tb/cms/content-search.xml" title="百度贴吧" />
    	<meta itemprop="dateUpdate" content="2020-09-21 18:20:51" />

        <meta name="keywords" content="海贼王,动漫·轻小说作品,动漫,风华,新世界杯">
    <meta name="description" content="本吧热帖: 1-外行员吃相真是越来越难看了 2-海贼王官方艾斯小说漫画第1话汉化：黑桃海贼团成立 3-这么多年了，武装色硬化都是男人在用，女的不能学吗？女生本来身 4-凯多三灾的情报这么差吗？人家索隆好歹也是罪恶一代的超新星，居 5-各位山黑，山治会武装色哦，武装色会变黑哦。 6-【Grand News】第四百一十九期《孤立无援》 7-海贼王990话《孤立无援》（讨论分析，感想预测楼）">
    <title>海贼王吧-百度贴吧--不管在贴吧的哪个角落，海吧是你坚强的后盾--这里有过电台，听海吧DJ在电台里说学逗唱；这里有过为了申请家族的斗争，众人的团结让海吧终于能进入了百度家族；这里有过辩论赛，看吧友怎样唇枪 </title>
    

    
<script>
    void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>    <link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/static-common/style/tb.js/dialog_bda1025.css,/tb/static-common/lib/tbui/style/all_f29e774.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/index_a147469.css,/tb/_/search_8bbfc49.css,/tb/_/http_transform_d41d8cd.css,/tb/_/frs-footer/content_footer_e1ac3c2.css,/tb/_/fixed_bar_af8c791.css,/tb/_/fixed_daoliu_ffac4fc.css,/tb/_/frs-footer/extension_d41d8cd.css,/tb/_/suggestion_c2d979b.css,/tb/_/page_router_6d81cff.css,/tb/_/login_dialog_4a340b6.css,/tb/_/icons_fba8214.css,/tb/_/base_user_data_f665ab7.css,/tb/_/base_dialog_user_bar_69fdf18.css,/tb/_/qianbao_cashier_dialog_179e56e.css,/tb/_/qianbao_purchase_member_f0586a7.css,/tb/_/cashier_dialog_0d74ed0.css,/tb/_/pay_member_d41d8cd.css,/tb/_/new_message_system_bea7f16.css,/tb/_/user_head_35f26e0.css,/tb/_/js_pager_5be1e39.css,/tb/_/wallet_dialog_fce7ffd.css,/tb/_/card_1f33a7b.css,/tb/_/userbar_b56525c.css,/tb/_/duoku_servers_dialog_f50364d.css,/tb/_/duoku_servers_list_42e14c2.css,/tb/_/poster/rich_poster_4d57f00.css,/tb/_/footer_fd940ae.css,/tb/_/head_main_6892579.css,/tb/_/full_width_head_ca1a4d5.css,/tb/_/forum_card_62fcc00.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/slide_show_aad29db.css,/tb/_/head_recom_ff98cef.css,/tb/_/conf_skin_e7f8d17.css,/tb/_/bubble_tip_17a9ec9.css,/tb/_/tbshare_share_4a2fcf9.css,/tb/_/tbshare_popup_d41d8cd.css,/tb/_/aside_float_bar_277a843.css,/tb/_/verify_manager_phone_7d1435e.css,/tb/_/bawu_add_section_cb95883.css,/tb/_/icon_tip_db299f2.css,/tb/_/umoney_query_d15a716.css,/tb/_/qianbao_purchase_tdou_4b31f54.css,/tb/_/tdou_template_3eae00b.css,/tb/_/paykey_safe_payment_8f2a8db.css,/tb/_/captcha_30e4d3c.css,/tb/_/captcha_safe_payment_d41d8cd.css,/tb/_/mobile_safe_payment_77949bb.css,/tb/_/tbean_safe_3c779a3.css,/tb/_/tbean_safe_ajax_d41d8cd.css,/tb/_/umoney_f12b09a.css,/tb/_/firework_v2_2e35f90.css,/tb/_/payment_dialog_title_5433211.css,/tb/_/tdou_get_1536ffc.css,/tb/_/tdou_d41d8cd.css,/tb/_/novel_icons_02ab048.css,/tb/_/global_notice_8c177cf.css,/tb/_/umoney_promotion_dialog_d0d023b.css,/tb/_/snowflow_45a89bb.css,/tb/_/dialog_6ed86bb.css,/tb/_/cont_sign_card_73a332e.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/buy_controller_a328148.css,/tb/_/tieba_sign_card_2928c29.css,/tb/_/placeholder_7eb7ce6.css,/tb/_/sms_verify_dialog_cd843b0.css,/tb/_/forbidden_752e552.css,/tb/_/poster/share_thread_cbacfa9.css,/tb/_/like_tip_65eb23b.css,/tb/_/poster/topic_suggestion_c9a8071.css,/tb/_/word_limit_3c5481d.css,/tb/_/complaint_bar_owner_3dd0d03.css,/tb/_/poster/rich_poster_e538a98.css,/tb/_/ueditor_base_60e7ce4.css,/tb/_/ueditor_extend_base_d41d8cd.css,/tb/_/background_c5ba91f.css,/tb/_/tb_gram_d41d8cd.css,/tb/_/slide_select_51d60fb.css,/tb/_/image_flash_editor_8f43e09.css,/tb/_/scroll_panel_eb74727.css,/tb/_/picture_uploader_7e6cefb.css,/tb/_/picture_web_selector_e53d66f.css,/tb/_/picture_59387e8.css,/tb/_/custom_emotion_2d0490a.css,/tb/_/ueditor_emotion_a5eeac8.css,/tb/_/ueditor_video_fbebf66.css,/tb/_/sketchpad_cf60180.css,/tb/_/scrawl_5840a35.css,/tb/_/ueditor_topic_bb19767.css,/tb/_/topic_suggestion_3234253.css,/tb/_/fullscreen_f64a424.css,/tb/_/at_d03b8c9.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/post_setting_46ea748.css,/tb/_/setting_ca19f87.css,/tb/_/medal_5022a4b.css,/tb/_/paypost_agree_dialog_fd57709.css,/tb/_/paypost_editor_6d704da.css,/tb/_/attention_category_game_d2d4220.css,/tb/_/focus_btn_21ad291.css,/tb/_/game_frs_in_head_8026069.css,/tb/_/game_rank_in_head_94ba4ce.css,/tb/_/game_frs_head_218209e.css,/tb/_/tbnav_bright_38bb9dc.css,/tb/_/conf_repost_2d678d2.css,/tb/_/iframe_head_b5db402.css,/tb/_/activity_btv_5b32c41.css,/tb/_/game_iframe_common_19e3259.css,/tb/_/game_banner_ff14_9ad227a.css,/tb/_/game_head_info_765f80b.css,/tb/_/duoku_xwj_vip_e9fab16.css,/tb/_/wca_head_49a2ff8.css,/tb/_/athletic_center_loader_d41d8cd.css,/tb/_/game_player_auth_dialog_2e5deb0.css,/tb/_/sign_mod_539e18c.css,/tb/_/sign_tip_98d0754.css,/tb/_/platform_spread_layer_b5ef871.css,/tb/_/platform_spread_video_070115e.css,/tb/_/top_activity_e12a4fe.css,/tb/_/popup_zhang_8b74e36.css,/tb/_/block_user_1e8ac98.css,/tb/_/music_player_0a327b2.css,/tb/_/game_code_thread_c9a2228.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/game_thread_d41d8cd.css,/tb/_/single_icons_3112de2.css,/tb/_/post_marry_1ed5b11.css,/tb/_/interaction_d4668aa.css,/tb/_/month_icon_240ecc1.css,/tb/_/user_visit_card_129ebe7.css,/tb/_/util_pop_video_5116377.css,/tb/_/voice_c5bf26e.css,/tb/_/thread_list_7faa4cd.css,/tb/_/aside_region_6df4cfc.css,/tb/_/frs-aside/app_download_29b7cd0.css,/tb/_/lecai_iframe_a48aee4.css,/tb/_/professional_manager_tips_af0267b.css,/tb/_/by_forum_db9c68b.css,/tb/_/celebrity_widget_974def6.css,/tb/_/celebrity_forum_dialog_b44a28b.css,/tb/_/forum_member_dialog_1d49009.css,/tb/_/exp_package_dialog_5cb5fdb.css,/tb/_/npc_vote_action_5b250b1.css,/tb/_/celebrity_81c8269.css,/tb/_/celebrity_expball_e0bb045.css,/tb/_/frs-aside/forum_info_6bd1ba5.css,/tb/_/mixin_bd9244b.css,/tb/_/bean_d41d8cd.css,/tb/_/guess_3c31a66.css,/tb/_/sidebar_2541a8b.css,/tb/_/thread_item_44be836.css,/tb/_/thread_item_title_88b0c21.css,/tb/_/frs_user_base_e6ee6b4.css,/tb/_/util_pager_fd327a7.css" />
<link rel="stylesheet" href="//tb1.bdstatic.com/??/tb/_/thread_list_footer_99af8d2.css" />
<link rel="shortcut icon" href="https://gsp0.baidu.com/5aAHeD3nKhI2p27j8IqW0jdnxx1xbK/tb/favicon.ico"/>

<script>
    // 页面的基本信息
    var PageData = {
        'tbs': "106aeb5c78fcc5621600683657"    };

    PageData.page = "frs";

    // 用户的基本信息
    PageData.user = {
        'id': 0,
        'name': "",
        'no_un': 0,
        'is_login': 0,
        'is_new_user': 1,
        'portrait': "00000000",
        'name_url': "&ie=utf-8"    };

    // 吧的基本信息
    PageData.forum = {
        'id': 11772,
        'name': "\u6d77\u8d3c\u738b",
        'first_class': "\u52a8\u6f2b",
        'second_class': "\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1"    };

    if (Object.freeze) {
        (function deepFreeze(o) {
            var prop, propKey;
            Object.freeze(o);
            for (propKey in o) {
                prop = o[propKey];
                if (!o.hasOwnProperty(propKey) ||
                    typeof prop !== 'object' ||
                    !prop ||
                    Object.isFrozen(prop)) {
                    continue;
                }
                deepFreeze(prop);
            }
        })(PageData);
    }
</script>

    <script> alog('speed.set', 'ht', +new Date); </script>

        <!-- 引入百度统计 -->
    <script>
        var _hmt = _hmt || [];
        (function() {
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?98b9d8c2fd6608d564bf2ac2ae642948";
          var s = document.getElementsByTagName("script")[0]; 
          s.parentNode.insertBefore(hm, s);
        })();
    </script>

</head>

<body>
<div class="wrap1">
    <div class="wrap2">
        
<div class="header">
    <div class="common-pagelet-userbar">
    
<div id="local_flash_cnt"></div>

</div>



<div id="head" class="search_bright clearfix">
<div class="head_inner">
    <div class="search_top clearfix">
        <div class="search_nav j_search_nav">
            <!-- 资讯、贴吧、知道、视频、音乐、图片、地图、文库 -->
            <a rel="noreferrer"  param="wd"
               href=http://www.baidu.com/s?cl=3&amp; >网页</a>
            <a rel="noreferrer"  param="word" href="http://www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;fr=tieba&amp;">资讯</a>
            <b>贴吧</b>
            <a rel="noreferrer"  param="word"
               href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;">知道</a>
            <!-- <a rel="noreferrer"  param="word" href="http://v.baidu.com/v?ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=21&amp;">视频</a> -->
            <a rel="noreferrer"  param="word" href="http://www.baidu.com/sf/vsearch?pd=video&amp;tn=vsearch&amp;ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=21&amp;rsv_spt=11&amp;">视频</a>
            <a rel="noreferrer"  param="key" href="http://music.baidu.com/search?fr=tieba&">音乐</a>
            <a rel="noreferrer"  param="word"
               href="http://image.baidu.com/i?tn=baiduimage&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;">图片</a>
            <a rel="noreferrer"  param="word" href="http://map.baidu.com/m?fr=map006&amp;">地图</a>
            <a rel="noreferrer"  href="http://wenku.baidu.com/search?fr=tieba&lm=0&od=0&" param="word" target="_blank">文库</a>
        </div>
    </div>
    <div class="search_main_wrap">
        <div class="search_main clearfix">
            <div class="search_form">
                <a rel="noreferrer"  title="到贴吧首页" href="/" class="search_logo" id="search_logo_large"></a>
                <a rel="noreferrer"  id="search_logo_small" class="" title="到贴吧首页" href="/"></a>
                <form name="f1" class="clearfix j_search_form" action="/f"
                      id="tb_header_search_form">
                                        <input class="search_ipt search_inp_border j_search_input tb_header_search_input"
                           name="kw1" value="海贼王" type="text" autocomplete="off" size="42"
                           tabindex="1" id="wd1" maxlength="100" x-webkit-grammar="builtin:search"
                           x-webkit-speech="true"/>
                    <input autocomplete="off" type="hidden" name="kw" value="海贼王" id="wd2"/>
                    <span class="search_btn_wrap search_btn_enter_ba_wrap">
                        <a rel="noreferrer"  class="search_btn search_btn_enter_ba j_enter_ba" href="#"
                           onclick="return false;"
                           onmousedown="this.className+=' search_btn_down'"
                           onmouseout="this.className=this.className.replace('search_btn_down','')">进入贴吧</a>
                    </span>
                    <span class="search_btn_wrap">
                        <a rel="noreferrer"  class="search_btn j_search_post" href="#" onclick="return false;"
                           onmousedown="this.className+=' search_btn_down'"
                           onmouseout="this.className=this.className.replace('search_btn_down','')">全吧搜索</a>
                    </span>
                    <a rel="noreferrer"  class="senior-search-link" href="//tieba.baidu.com/f/search/adv">高级搜索</a>
                                    </form>
                                <p style="display:none;" class="switch_radios">
                    <input type="radio" class="nowtb" name="tb" id="nowtb"><label
                        for="nowtb">吧内搜索</label>
                    <input type="radio" class="searchtb" name="tb" id="searchtb"><label for="searchtb">搜贴</label>
                    <input type="radio" class="authortb" name="tb" id="authortb"><label for="authortb">搜人</label>
                    <input type="radio" class="jointb" checked="checked" name="tb" id="jointb"><label
                        for="jointb">进吧</label>
                    <input type="radio" class="searchtag" name="tb" id="searchtag"
                           style="display:none;"><label for="searchtag"
                                                        style="display:none;">搜标签</label>
                </p>
            </div>
        </div>
    </div>
</div>
</div>
<script>
if (window.alog && window.alog.fire) {
    alog('speed.set', 'c_widget_search_show', +new Date);
    alog.fire("mark");
}
</script>



<div class="head_main">
        <div class="head_top">
        

<div class="top_iframe" style="position:relative;z-index:9999;">
    </div>


    </div>
    <div class="head_middle">
        



    </div>
    <div class="head_content">
        




        <div id="plat_recom_carousel" class="plat_recom_carousel tbui_slideshow_container">
                        <ul class="tbui_slideshow_list">
                                <li class="tbui_slideshow_slide tbui_slide_Inherit_width j_slide" data-title="19元200GB流量不限速+爱奇艺VIP会员" data-subtitle="橙包你的上网生活，流量玩尽兴，会员看过瘾，亲情号码免费打~" data-btn="立即查看" data-href="/official/click/redirect?client_type=pc_web&tbjump=https%3A%2F%2Fcard.10010.com%2Fqueen%2ForangeCard%2Fhqytb.html%3Fchannel%3D03-0765-a112-9999&ie=utf-8&task=%E5%90%A7%E5%A4%B4%E5%9B%BE%E6%8E%A8%E8%8D%90%E7%BB%9F%E8%AE%A1&ie=utf-8&locate=%E5%A4%B4%E9%83%A8%E8%BD%AE%E6%92%AD%E5%9B%BE&ie=utf-8&page=pfe&ie=utf-8&type=click&url=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36&ie=utf-8&refer=&ie=utf-8&fid=&fname=&uid=&uname=&is_new_user=&tid=&_t=1600683658&frame=1&evl_client_type=pc_web&evl_page=FRS&evl_locate=p0249&evl_task=ad_plat&evl_line=PT&evl_action_type=CLICK&evl_callfrom=effect_evl&evl_obj_id=258430013_13&evl_id=258430013&evl_res_id=13&evl_uid=&evl_uname=&evl_fid=&evl_fname=&evl_first_dir=&evl_second_dir=">
                    <a href="/official/click/redirect?client_type=pc_web&tbjump=https%3A%2F%2Fcard.10010.com%2Fqueen%2ForangeCard%2Fhqytb.html%3Fchannel%3D03-0765-a112-9999&ie=utf-8&task=%E5%90%A7%E5%A4%B4%E5%9B%BE%E6%8E%A8%E8%8D%90%E7%BB%9F%E8%AE%A1&ie=utf-8&locate=%E5%A4%B4%E9%83%A8%E8%BD%AE%E6%92%AD%E5%9B%BE&ie=utf-8&page=pfe&ie=utf-8&type=click&url=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36&ie=utf-8&refer=&ie=utf-8&fid=&fname=&uid=&uname=&is_new_user=&tid=&_t=1600683658&frame=1&evl_client_type=pc_web&evl_page=FRS&evl_locate=p0249&evl_task=ad_plat&evl_line=PT&evl_action_type=CLICK&evl_callfrom=effect_evl&evl_obj_id=258430013_13&evl_id=258430013&evl_res_id=13&evl_uid=&evl_uname=&evl_fid=&evl_fname=&evl_first_dir=&evl_second_dir=" target="_blank">
                        <img id="head_img" height="380" src="//tiebapic.baidu.com/forum/pic/item/c2fdfc039245d688870de3ffb3c27d1ed21b2459.jpg"/>
                    </a>
                </li>
                            </ul>
            <ul class="j_plat_recom_dots_nav plat_recom_dots_nav plat_recom_dots_nav_only">
                            <li class="plat_recom_dot plat_recom plat_recom_off plat_recom_on"></li>
                        </ul>
            <a id="plat_recom_carousel_prev" href="#" class="plat_recom_carousel_a plat_recom_carousel_prev plat_recom_carousel_a_only">
                <span class="plat_recom_carousel_a_bg"></span>
                <span class="plat_recom_arrow plat_recom plat_recom_arrowl"></span>
            </a>
            <a id="plat_recom_carousel_next" href="#" class="plat_recom_carousel_a plat_recom_carousel_next plat_recom_carousel_a_only">
                <span class="plat_recom_carousel_a_bg"></span>
                <span class="plat_recom_arrow plat_recom plat_recom_arrowr"></span>
            </a>

            <div class="activity_head ">
                <div class="activity_head_bg"></div>
            <a class="j_activity_title activity_title" title="19元200GB流量不限速+爱奇艺VIP会员" href="/official/click/redirect?client_type=pc_web&tbjump=https%3A%2F%2Fcard.10010.com%2Fqueen%2ForangeCard%2Fhqytb.html%3Fchannel%3D03-0765-a112-9999&ie=utf-8&task=%E5%90%A7%E5%A4%B4%E5%9B%BE%E6%8E%A8%E8%8D%90%E7%BB%9F%E8%AE%A1&ie=utf-8&locate=%E5%A4%B4%E9%83%A8%E8%BD%AE%E6%92%AD%E5%9B%BE&ie=utf-8&page=pfe&ie=utf-8&type=click&url=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36&ie=utf-8&refer=&ie=utf-8&fid=&fname=&uid=&uname=&is_new_user=&tid=&_t=1600683658&frame=1&evl_client_type=pc_web&evl_page=FRS&evl_locate=p0249&evl_task=ad_plat&evl_line=PT&evl_action_type=CLICK&evl_callfrom=effect_evl&evl_obj_id=258430013_13&evl_id=258430013&evl_res_id=13&evl_uid=&evl_uname=&evl_fid=&evl_fname=&evl_first_dir=&evl_second_dir=" target="_blank">19元200GB流量不限速+爱奇艺VIP会员</a>
            <a class="j_activity_subtitle activity_subtitle" href="/official/click/redirect?client_type=pc_web&tbjump=https%3A%2F%2Fcard.10010.com%2Fqueen%2ForangeCard%2Fhqytb.html%3Fchannel%3D03-0765-a112-9999&ie=utf-8&task=%E5%90%A7%E5%A4%B4%E5%9B%BE%E6%8E%A8%E8%8D%90%E7%BB%9F%E8%AE%A1&ie=utf-8&locate=%E5%A4%B4%E9%83%A8%E8%BD%AE%E6%92%AD%E5%9B%BE&ie=utf-8&page=pfe&ie=utf-8&type=click&url=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36&ie=utf-8&refer=&ie=utf-8&fid=&fname=&uid=&uname=&is_new_user=&tid=&_t=1600683658&frame=1&evl_client_type=pc_web&evl_page=FRS&evl_locate=p0249&evl_task=ad_plat&evl_line=PT&evl_action_type=CLICK&evl_callfrom=effect_evl&evl_obj_id=258430013_13&evl_id=258430013&evl_res_id=13&evl_uid=&evl_uname=&evl_fid=&evl_fname=&evl_first_dir=&evl_second_dir=" target="_blank">橙包你的上网生活，流量玩尽兴，会员看过瘾，亲情号码免费打~</a>
                            <a class="imme_see_btn j_imme_see_btn" href="/official/click/redirect?client_type=pc_web&tbjump=https%3A%2F%2Fcard.10010.com%2Fqueen%2ForangeCard%2Fhqytb.html%3Fchannel%3D03-0765-a112-9999&ie=utf-8&task=%E5%90%A7%E5%A4%B4%E5%9B%BE%E6%8E%A8%E8%8D%90%E7%BB%9F%E8%AE%A1&ie=utf-8&locate=%E5%A4%B4%E9%83%A8%E8%BD%AE%E6%92%AD%E5%9B%BE&ie=utf-8&page=pfe&ie=utf-8&type=click&url=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36&ie=utf-8&refer=&ie=utf-8&fid=&fname=&uid=&uname=&is_new_user=&tid=&_t=1600683658&frame=1&evl_client_type=pc_web&evl_page=FRS&evl_locate=p0249&evl_task=ad_plat&evl_line=PT&evl_action_type=CLICK&evl_callfrom=effect_evl&evl_obj_id=258430013_13&evl_id=258430013&evl_res_id=13&evl_uid=&evl_uname=&evl_fid=&evl_fname=&evl_first_dir=&evl_second_dir=" target="_blank">
                    立即查看                </a>
                        </div>
        </div>

        


<div class="card_top_wrap clearfix card_top_theme ">
   <div class="card_top_right">
       
    <div class="sign_mod_bright" id="sign_mod">
        
<div class="sign_tip_container">
    <div class="j_succ_info sign_succ1" style="display:none">
        <div class="sign_tip_bdwrap clearfix">
            <div class="sign_tip_bd_arr"></div>
            <div class="sign_tip_main">
                <div class="sign_succ_calendar">
                    <div class="sign_succ_calendar_title">
                        <div class="calendar_title_month clearfix">
                            <div class="calendar_month_next j_calendar_month_next">&nbsp;</div>
                            <div class="calendar_month_prev j_calendar_month_prev">&nbsp;</div>
                            <div class="calendar_month_span j_calendar_month">&nbsp;</div>
                        </div>
                    </div>
                    <table class="sign_succ_table "
                            >
                        <thead align="center">
                        <tr class="sign_succ_canlerdar_head">
                            <td>日</td>
                            <td>一</td>
                            <td>二</td>
                            <td>三</td>
                            <td>四</td>
                            <td>五</td>
                            <td>六</td>
                        </tr>
                        </thead>
                        <tbody align="center" class="sign_succ_canlerdar_days j_canlerdar_days">
                        <tr>
                            <td class="j_1_0">&nbsp;</td>
                            <td class="j_1_1">&nbsp;</td>
                            <td class="j_1_2">&nbsp;</td>
                            <td class="j_1_3">&nbsp;</td>
                            <td class="j_1_4">&nbsp;</td>
                            <td class="j_1_5">&nbsp;</td>
                            <td class="j_1_6">&nbsp;</td>
                        </tr>
                        <tr>
                            <td class="j_2_0">&nbsp;</td>
                            <td class="j_2_1">&nbsp;</td>
                            <td class="j_2_2">&nbsp;</td>
                            <td class="j_2_3">&nbsp;</td>
                            <td class="j_2_4">&nbsp;</td>
                            <td class="j_2_5">&nbsp;</td>
                            <td class="j_2_6">&nbsp;</td>
                        </tr>
                        <tr>
                            <td class="j_3_0">&nbsp;</td>
                            <td class="j_3_1">&nbsp;</td>
                            <td class="j_3_2">&nbsp;</td>
                            <td class="j_3_3">&nbsp;</td>
                            <td class="j_3_4">&nbsp;</td>
                            <td class="j_3_5">&nbsp;</td>
                            <td class="j_3_6">&nbsp;</td>
                        </tr>
                        <tr>
                            <td class="j_4_0">&nbsp;</td>
                            <td class="j_4_1">&nbsp;</td>
                            <td class="j_4_2">&nbsp;</td>
                            <td class="j_4_3">&nbsp;</td>
                            <td class="j_4_4">&nbsp;</td>
                            <td class="j_4_5">&nbsp;</td>
                            <td class="j_4_6">&nbsp;</td>
                        </tr>
                        <tr class="j_5" style="display:none">
                            <td class="j_5_0">&nbsp;</td>
                            <td class="j_5_1">&nbsp;</td>
                            <td class="j_5_2">&nbsp;</td>
                            <td class="j_5_3">&nbsp;</td>
                            <td class="j_5_4">&nbsp;</td>
                            <td class="j_5_5">&nbsp;</td>
                            <td class="j_5_6">&nbsp;</td>
                        </tr>
                        <tr class="j_6" style="display:none">
                            <td class="j_6_0">&nbsp;</td>
                            <td class="j_6_1">&nbsp;</td>
                            <td class="j_6_2">&nbsp;</td>
                            <td class="j_6_3">&nbsp;</td>
                            <td class="j_6_4">&nbsp;</td>
                            <td class="j_6_5">&nbsp;</td>
                            <td class="j_6_6">&nbsp;</td>
                        </tr>
                        </tbody>
                    </table>
                </div>

                <div class="sign_tip_boards">
                    <div class="sign_tip_board sign_tip_board_urank j_sign_ad_mobi">
                        <div class="sign_tip_board_ico"></div>
                        <p>签到排名：今日本吧第<span class="sign_index_num j_signin_index"></span>个签到，</p>

                        <p><span class="j_succ_text">本吧因你更精彩，明天继续来努力！</span></p>
                    </div>
                    <div class="sign_tip_board sign_tip_board_barrank">
                        <div class="sign_tip_board_ico"></div>
                                                    <p>本吧排名：<a rel="noreferrer" target="_blank"
                                       href="/sign/index?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8">1</a>
                            </p>
                                                <p>本吧签到人数：151920</p>
                    </div>
                </div>

            </div>

            <div class="sign_tip_aside">

                                                        <div class="sign_tip_sbox sign_tip_sbox_first sign_tip_sbox_1key">
                        <div class="sign_tip_sbox_hd">一键签到</div>
                        <div class="sign_tip_sbox_bd">
                            <div class="sign_tip_sbox_cnt">
                                <a rel="noreferrer" class="sign_tip_sbox_card j_sign_tip_1key_icon sign_tip_sbox_card_pencil"
                                   href="/tbmall/tshow?tab=detail" target="_blank"></a>

                                <div class="sign_tip_sbox_txt">可签<span class="orange_text">7</span>级以上的吧<span
                                        class="orange_text">50</span>个
                                </div>
                                <div class="sign_tip_sbox_btn">
                                    <a rel="noreferrer" href="/home/main?id=00000000#stipsign" target="_blank"
                                       class="btn-sub btn-small">
                                        <b class="sign_crown sign_crown_pencil" title="无瑕的T秀勋章"></b> 一键签到
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                
                <div class="sign_tip_sbox sign_tip_sbox_fixsign">
                    <div class="sign_tip_sbox_hd sign_tip_sbox_hd_inf j_need_rpln_wrap">本月漏签<span
                            class="j_lack_sign_monthly_count sign_num">0</span>次！
                    </div>
                    <div class="sign_tip_sbox_bd">
                        <div class="sign_tip_sbox_cnt">
                            <a rel="noreferrer" href="/tbmall/propslist?category=108" class="sign_tip_sbox_card" target="_blank"><span
                                    class="sign_num"><span class="j_rpln_card_count">0</span></span></a>

                            <div class="sign_tip_sbox_txt">成为超级会员，赠送8张补签卡</div>
                            <div class="sign_tip_sbox_btn">
                                <a rel="noreferrer" href="#" class="btn-sub btn-small j_lack_sign_monthly_help"
                                   target="_blank">如何使用？</a>

                                <div class="lack_sign_monthly_tip_wrap">
                                    <div class="ui_card_wrap lack_sign_monthly_tip_card j_lack_sign_monthly_tip_card"
                                         style="display:none;">
                                        <div class="ui_card_content ">
                                            <div class="time_gift_tip">点击日历上漏签日期，即可进行<span
                                                    class="strongerText">补签</span>。
                                            </div>
                                        </div>
                                        <span class="arrow ui_white_down" style="left:48%;"></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="sign_tip_sbox sign_tip_sbox_chainsign">
                    <div class="sign_tip_sbox_hd sign_tip_sbox_hd_inf">
                        连续签到：<span class="sign_num j_sign_succ_keep"></span>天&nbsp;&nbsp;累计签到：<span
                            class="sign_num j_sign_succ_count"></span>天
                    </div>
                    <div class="sign_tip_sbox_bd">
                        <div class="sign_tip_sbox_cnt">
                            <a rel="noreferrer" href="/tbmall/propslist?category=108" class="sign_tip_sbox_card" target="_blank"><span
                                    class="sign_num"><span
                                        class="j_sign_chainsign_num">0</span></span></a>

                            <div class="sign_tip_sbox_txt">超级会员单次开通12个月以上，赠送连续签到卡3张</div>
                            <div class="sign_tip_sbox_btn"><a rel="noreferrer" href="#" class="btn-sub btn-small j_cont_sign_card"
                                                              target="_blank">使用连续签到卡</a></div>
                        </div>
                    </div>
                </div>

                <div class="sign_tip_sbox sign_tip_sbox_last sign_tip_sbox_rights">
                    <div class="sign_tip_sbox_bd j_sign_rights">
                        <div class="sign_rights_display clearfix">
                            <div class="sign_rights_icon j_sign_rights_icon rights_1"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_2"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_3"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_4"></div>
                            <div class="sign_rights_icon j_sign_rights_icon rights_5"></div>
                            <span class="split_line"></span>
                            <a rel="noreferrer" href="/f/like/level?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&lv_t=lv_nav_who" class="balv_help"
                               title="签到规则" target="_blank"></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

        <div id="signstar_wrapper" class="j_sign_box sign_box_bright">
            <a rel="noreferrer" href="#" onclick="return false" data-dw="1" tabindex="3"
               title="签到"
               class="j_signbtn sign_btn_bright">
                                <span class="sign_today_date">09月21日</span>
                <span class="sign_month_lack_days">漏签<span class="j_sign_month_lack_days">0</span>天</span>
            </a>
        </div>

        
            </div>
   </div>
   <div class="card_top clearfix">
              <div class="card_head">
           <a rel="noreferrer" href="/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8">
               <img class="card_head_img" id="forum-card-head" src="https://gss3.bdstatic.com/84oSdTum2Q5BphGlnYG/timg?wapp&amp;quality=80&amp;size=b150_150&amp;subsize=20480&amp;cut_x=0&amp;cut_w=0&amp;cut_y=0&amp;cut_h=0&amp;sec=1369815402&amp;srctrace&amp;di=5a8b98e57241eb19ede752f3a648afeb&amp;wh_rate=null&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fpic%2Fitem%2F9d82d158ccbf6c81860b836bb63eb13533fa4070.jpg"/>
           </a>
       </div>

       <div class="card_title">
           <a rel="noreferrer" class=" card_title_fname" title=""
              href="/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8">
               海贼王吧
           </a>
                                 <div class="focus_btn_wrap">
               
<a rel="noreferrer" href="#" onclick="return false"
   class="focus_btn islike_focus" id="j_head_focus_btn"
   style="margin-top:2px;"></a>
           </div>
           <div class="card_num">
               <span class="">
  <span class="card_numLabel">关注：</span>
  <span class="card_menNum">10,124,066</span>
  <span class="card_numLabel">贴子：</span>
  <span class="card_infoNum">292,086,496</span>
</span>
           </div>
       </div>

       <p class="card_slogan">不管在贴吧的哪个角落，海吧是你坚强的后盾</p>

       <div class="card_info">
           <ul class="forum_dir_info bottom_list clearfix">
                                  <li>
                                          </li>
                   <li>
                       <span class="dir_text">目录：</span>
                   </li>
                   <li>
                                                  <a rel="noreferrer" target="_blank"
                              href="/f/fdir?fd=动漫&ie=utf-8&sd=动漫·轻小说作品">动漫·轻小说作品</a>
                                          </li>
                          </ul>
       </div>
   </div>
</div>



<div class="game_frs_in_head">
    </div>


<div class="nav_wrap " id="tb_nav">
        <ul class="nav_list j_nav_list">
                                <li class=" focus j_tbnav_tab " data-tab-main>
    <a href="/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&tab=main" class="j_nav_local_tab_link j_tbnav_tab_a" id="tab_forumname" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabmain">看贴</a>
</li>                                <li class=" j_tbnav_tab " data-tab-album>
    <a href="/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&tab=album" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabfrsphotogood" frs-page="main" id="tab_picture">图片</a>
</li>                                <li class=" j_tbnav_tab " data-tab-good>
    <a href="/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&tab=good" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabgood">精品</a>
</li>                                <li class=" j_tbnav_tab " data-tab-video>
    <a href="/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&tab=video" class="j_nav_local_tab_link j_tbnav_tab_a" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabvideo">视频</a>
</li>                                <li class=" j_tbnav_tab " data-tab->
    <a href="/f?ie=utf-8&kw=%E6%B8%B8%E6%88%8F%E4%B8%AD%E5%BF%83&ie=utf-8" class=" j_tbnav_tab_a" id="j_navtab_game" target="_blank" location="tabplay" stats-data="fr=tb0_forum&st_mod=frs&st_value=tabplay&fname=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8">游戏</a>
</li>            </ul>
                            <form class="search_internal_wrap pull_right j_search_internal_forum">
                <input class="search_internal_input j_search_internal_input" value="" placeholder="吧内搜索" type="text"/>
                <button class="search_internal_btn" type="submit"/>
                <i></i></button>
            </form>
            </div>
    </div>
</div>
</div>
<div class="content" id="content">
        <div class="forum_content clearfix">
        <div class="main" id="content_wrap">
            <div id="content_leftList" class="content_leftList j-content-leftList clearfix">
    






<ul id="thread_list" class="threadlist_bright j_threadlist_bright">
                <li class="thread_top_list_folder">
                <ul id="thread_top_list" class="thread_top_list">
                    <li class=" j_thread_list thread_top j_thread_list clearfix" data-field='{&quot;id&quot;:6955393107,&quot;author_name&quot;:&quot;GN\u5468\u520a&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.2c0e048.VFUJtjrbQl4EwWKNr0H0GA&quot;,&quot;first_post_id&quot;:134948274722,&quot;reply_num&quot;:53,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:true,&quot;is_top&quot;:true,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6955393107' data-thread-type="0" data-floor='0''>
            <div class="t_con cleafix">
                    <a rel="noreferrer"  href="javascript:;" title="点击隐藏本贴" data-field='{&quot;tid&quot;:6955393107}'               class="j_thread_hidden icon_thread_hidden"></a>
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">53</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit 
">
    <i class="icon-top" alt="置顶" title="置顶" ></i><i class="icon-good" alt="精品" title="精品" ></i>
    
    <a rel="noreferrer" href="/p/6955393107" title="【Grand News】第四百一十九期《孤立无援》" target="_blank" class="j_th_tit ">【Grand News】第四百一十九期《孤立无援》</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: GN周刊"
          data-field='{&quot;user_id&quot;:3141474943}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;GN\u5468\u520a&quot;,&quot;id&quot;:&quot;tb.1.2c0e048.VFUJtjrbQl4EwWKNr0H0GA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=GN%E5%91%A8%E5%88%8A&ie=utf-8&id=tb.1.2c0e048.VFUJtjrbQl4EwWKNr0H0GA&fr=frs" target="_blank">GN周刊</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-18</span>
</div>
            </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list thread_top j_thread_list clearfix" data-field='{&quot;id&quot;:6947522090,&quot;author_name&quot;:&quot;Smile\u4e1c\u5341\u533a&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.86f97cdb.HZWW566nk7tCtjVPCXhBgA&quot;,&quot;first_post_id&quot;:134863223097,&quot;reply_num&quot;:93,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:true,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6947522090' data-thread-type="0" data-floor='0''>
            <div class="t_con cleafix">
                    <a rel="noreferrer"  href="javascript:;" title="点击隐藏本贴" data-field='{&quot;tid&quot;:6947522090}'               class="j_thread_hidden icon_thread_hidden"></a>
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">93</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    <i class="icon-top" alt="置顶" title="置顶" ></i>
    
    <a rel="noreferrer" href="/p/6947522090" title="海贼王990话《孤立无援》（讨论分析，感想预测楼）" target="_blank" class="j_th_tit ">海贼王990话《孤立无援》（讨论分析，感想预测楼）</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: Smile东十区"
          data-field='{&quot;user_id&quot;:795502155}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Smile\u4e1c\u5341\u533a&quot;,&quot;id&quot;:&quot;tb.1.86f97cdb.HZWW566nk7tCtjVPCXhBgA&quot;}' title="该用户已经连续签到2822天了，连续30天一举“橙”名" class="frs-author-name sign_highlight j_user_card " href="/home/main/?un=Smile%E4%B8%9C%E5%8D%81%E5%8C%BA&ie=utf-8&id=tb.1.86f97cdb.HZWW566nk7tCtjVPCXhBgA&fr=frs" target="_blank">Smile东十区</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -750px  0;top:0px;left:0px" data-slot="1"  data-name="tiancheng" data-field='{&quot;name&quot;:&quot;tiancheng&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u5929\u79e4\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,15&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="天秤座印记"  locate="tiancheng_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -1300px  0;top:0px;left:28px" data-slot="2"  data-name="nativeuser" data-field='{&quot;name&quot;:&quot;nativeuser&quot;,&quot;end_time&quot;:&quot;1603450538&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;2&quot;,&quot;title&quot;:&quot;\u6838\u5fc3\u5427\u4e3b\u8ba4\u8bc1&quot;,&quot;intro&quot;:&quot;\u6838\u5fc3\u5427\u4e3b\u8ba4\u8bc1&quot;,&quot;intro_url&quot;:&quot;https:\/\/tieba.baidu.com\/p\/6587692442&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,26&quot;}}' target="_blank"   href="https://tieba.baidu.com/p/6587692442"  class="j_icon_slot"  title="核心吧主认证"  locate="nativeuser_1#icon"  style="top: 0px; left:28px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-14</span>
</div>
            </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list thread_top j_thread_list clearfix" data-field='{&quot;id&quot;:6942331791,&quot;author_name&quot;:&quot;GN\u5468\u520a&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.2c0e048.VFUJtjrbQl4EwWKNr0H0GA&quot;,&quot;first_post_id&quot;:134801592607,&quot;reply_num&quot;:57,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:true,&quot;is_top&quot;:true,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6942331791' data-thread-type="0" data-floor='0''>
            <div class="t_con cleafix">
                    <a rel="noreferrer"  href="javascript:;" title="点击隐藏本贴" data-field='{&quot;tid&quot;:6942331791}'               class="j_thread_hidden icon_thread_hidden"></a>
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">57</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    <i class="icon-top" alt="置顶" title="置顶" ></i><i class="icon-good" alt="精品" title="精品" ></i>
    
    <a rel="noreferrer" href="/p/6942331791" title="【Grand News】第四百一十八期《丝毫不觉得会输》" target="_blank" class="j_th_tit ">【Grand News】第四百一十八期《丝毫不觉得会输》</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: GN周刊"
          data-field='{&quot;user_id&quot;:3141474943}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;GN\u5468\u520a&quot;,&quot;id&quot;:&quot;tb.1.2c0e048.VFUJtjrbQl4EwWKNr0H0GA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=GN%E5%91%A8%E5%88%8A&ie=utf-8&id=tb.1.2c0e048.VFUJtjrbQl4EwWKNr0H0GA&fr=frs" target="_blank">GN周刊</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-12</span>
</div>
            </div>
                                </div>
    </div>
</li>
                </ul>
                                <a rel="noreferrer"  id="thread_top_folder" class="icon_top_folder" href="javascript:;"
                     ></a>
            </li>
        <li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6967867265,&quot;author_name&quot;:&quot;wuzhizhemu&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.17df3eb3.IRdY3i0d-f1MxG4SZThQtA&quot;,&quot;first_post_id&quot;:135072099701,&quot;reply_num&quot;:118,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6967867265' data-thread-type="0" data-floor='1''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">118</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6967867265" title="和之国目前没有一个塑造的很好的角色" target="_blank" class="j_th_tit ">和之国目前没有一个塑造的很好的角色</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: wuzhizhemu"
          data-field='{&quot;user_id&quot;:150855836}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;wuzhizhemu&quot;,&quot;id&quot;:&quot;tb.1.17df3eb3.IRdY3i0d-f1MxG4SZThQtA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=wuzhizhemu&ie=utf-8&id=tb.1.17df3eb3.IRdY3i0d-f1MxG4SZThQtA&fr=frs" target="_blank">wuzhizhemu</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-19</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            最失败的就是御田 简直就是垃圾 
        </div>


            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6967867265"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="45185" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=beb74b8461c6a7efb973a024cdca8368/f66bf21fbe096b63af82b00b1b338744eaf8ac84.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=53ddd9636cf40ad115e4c7eb671710df/6a600c338744ebf843ea8a64cef9d72a6159a7d6.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    

<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 💢超级赛亚人✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f38\u61f6\u8170\u7684\u8c6c&quot;,&quot;id&quot;:&quot;tb.1.372b2654.s4_XAYcl6RhrmoNDZz6rsw&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=%E4%BC%B8%E6%87%B6%E8%85%B0%E7%9A%84%E8%B1%AC&ie=utf-8&id=tb.1.372b2654.s4_XAYcl6RhrmoNDZz6rsw&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-31.png" class="nicknameEmoji" style="width:13px;height:13px"/>超级赛...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6967462381,&quot;author_name&quot;:&quot;\u6211\u5fd8\u4e86\u65b0\u751f&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.6977641d.Fhn6THyBtvf5T2SsQ-437g&quot;,&quot;first_post_id&quot;:135067417175,&quot;reply_num&quot;:248,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6967462381' data-thread-type="0" data-floor='2''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">248</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6967462381" title="理性判断下来战斗服山治应该有机会打赢卡二！山治高光时刻镇楼！" target="_blank" class="j_th_tit ">理性判断下来战斗服山治应该有机会打赢卡二！山治高光时刻镇楼！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 我忘了新生"
          data-field='{&quot;user_id&quot;:647976702}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6211\u5fd8\u4e86\u65b0\u751f&quot;,&quot;id&quot;:&quot;tb.1.6977641d.Fhn6THyBtvf5T2SsQ-437g&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%88%91%E5%BF%98%E4%BA%86%E6%96%B0%E7%94%9F&ie=utf-8&id=tb.1.6977641d.Fhn6THyBtvf5T2SsQ-437g&fr=frs" target="_blank">我忘了新生</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-19</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            理性判断下来战斗服山治应该有机会打赢卡二！山治高光时刻镇楼！
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6967462381"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="70202" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=01f4ccb3ab3eb1354492bfb9962e84ea/6f3eb07eca8065388d29444880dda144ac34825c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=8bb82774a9096b6381195e583c088544/902397dda144ad34d87c67dcc7a20cf430ad85ae.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 恶心丶易施😁">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6076\u884c\u4e36\u6613\u65bd&quot;,&quot;id&quot;:&quot;tb.1.1bc86c8d.o1oa6otb9CLI7ct6b_iGYw&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=%E6%81%B6%E8%A1%8C%E4%B8%B6%E6%98%93%E6%96%BD&ie=utf-8&id=tb.1.1bc86c8d.o1oa6otb9CLI7ct6b_iGYw&fr=frs" target="_blank">恶心丶易...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970516340,&quot;author_name&quot;:&quot;\u718a\u6218\u58eb\u7684\u96c4\u8d77&quot;,&quot;author_nickname&quot;:&quot;\u76db\u4e16-\u82b3\u534e&quot;,&quot;author_portrait&quot;:&quot;tb.1.bde99314.P8zPWUAluNTMl5Phg6JG4g&quot;,&quot;first_post_id&quot;:135107111413,&quot;reply_num&quot;:37,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970516340' data-thread-type="0" data-floor='3''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">37</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit  member_thread_title_frs ">
    
    
    <a rel="noreferrer" href="/p/6970516340" title="凯多明明还没杰克高，小玉为什么会产生凯多和大妈谁体积大的疑问" target="_blank" class="j_th_tit ">凯多明明还没杰克高，小玉为什么会产生凯多和大妈谁体积大的疑问</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author no_icon_author"
          title="主题作者: 盛世-芳华"
          data-field='{&quot;user_id&quot;:117859894}' ><i class="icon_author"></i><span class="pre_icon_wrap pre_icon_wrap_theme1 frs_bright_preicon"><a class="icon_tbworld icon-crown-year-v5" href="/tbmall/tshow" data-field='{&quot;user_id&quot;:117859894}' target="_blank" title="贴吧超级会员"></a></span><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u718a\u6218\u58eb\u7684\u96c4\u8d77&quot;,&quot;id&quot;:&quot;tb.1.bde99314.P8zPWUAluNTMl5Phg6JG4g&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=%E7%86%8A%E6%88%98%E5%A3%AB%E7%9A%84%E9%9B%84%E8%B5%B7&ie=utf-8&id=tb.1.bde99314.P8zPWUAluNTMl5Phg6JG4g&fr=frs" target="_blank">盛世<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>芳华</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -3850px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;2&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,76&quot;,&quot;2&quot;:&quot;1599647089,77&quot;,&quot;3&quot;:&quot;1599647089,78&quot;,&quot;4&quot;:&quot;1599647089,79&quot;,&quot;5&quot;:&quot;1599647089,80&quot;,&quot;6&quot;:&quot;1599647089,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_2#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">09:21</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            凯多明明还没杰克高，小玉为什么会产生凯多和大妈谁体积大的疑问 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6970516340"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="66683" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=dcdaab1b2e12b31bc739c52bb6281a43/c7ea9f3df8dcd10015f6cf7d658b4710b9122f35.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=22e6c97f5e540923aa696376a263d009/cc11728b4710b91267abc1a2d4fdfc0392452207.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="56537" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=3d84554006dfa9ecfd7b5e1552e0db3a/6b06d40735fae6cdb4de9c3d18b30f2442a70f35.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=066a72a32cc79f3d8fe1e4388a9acc11/9f510fb30f2442a71664caf9c643ad4bd1130207.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="36577" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=21e39f44c32a283443f33e096b85e5d3/4c7cf8198618367a9b0ef08439738bd4b21ce596.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=031d635adf95d143da76e42b43cb8302/4bed2e738bd4b31cc6bb1be290d6277f9f2ff8e0.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 我于万物之中◎">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5e1d\u56fd\u7edf\u5e052046&quot;,&quot;id&quot;:&quot;tb.1.15a4eaa9.7QfhDIrkthyQIYU9StGecA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%B8%9D%E5%9B%BD%E7%BB%9F%E5%B8%852046&ie=utf-8&id=tb.1.15a4eaa9.7QfhDIrkthyQIYU9StGecA&fr=frs" target="_blank">我于万物...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6847977501,&quot;author_name&quot;:&quot;\u7d2b\u8272\u706c\u65e0\u8da3&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.b76084b5.-5hMTjsEJgIcjkNWaN2Odg&quot;,&quot;first_post_id&quot;:133725309520,&quot;reply_num&quot;:193,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6847977501' data-thread-type="0" data-floor='4''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">193</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6847977501" title="尾田是真的不会画脸吗？" target="_blank" class="j_th_tit ">尾田是真的不会画脸吗？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 紫色灬无趣"
          data-field='{&quot;user_id&quot;:893567291}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7d2b\u8272\u706c\u65e0\u8da3&quot;,&quot;id&quot;:&quot;tb.1.b76084b5.-5hMTjsEJgIcjkNWaN2Odg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%B4%AB%E8%89%B2%E7%81%AC%E6%97%A0%E8%B6%A3&ie=utf-8&id=tb.1.b76084b5.-5hMTjsEJgIcjkNWaN2Odg&fr=frs" target="_blank">紫色灬无趣</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">7-29</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            娜美脸，罗宾脸，微微脸，好像就男性很少撞脸的。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6847977501"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="12469" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=3e97a25d0830e924cff194337c38423f/8133d21b0ef41bd594f157a146da81cb38db3df6.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=bb142c7bbfd3fd1f3609a2320075241f/dcc451da81cb39db8f62d803c7160924aa1830c0.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="33048" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=18548023e51fbe091c0bcb165b50200a/17e9b74543a98226ac6394729d82b9014b90ebf7.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=5a443c984566d0167e199e20a710d507/1f178a82b9014a90959cf9e8be773912b21beec1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="56224" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=476cb0e2fe50352ab1342d0a6373d7cb/db529e2f0708283862af6341af99a9014d08f1f7.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=d6fb892a6ff0f736d8fe4c093a6eb219/e824b899a9014c08139997f01d7b02087af4f4c1.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;4&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 尛尛尛尛丶尛陌">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5c1b\u5c1b\u5c1b\u5c1b\u4e36\u5c1b\u964c&quot;,&quot;id&quot;:&quot;tb.1.632d5b40.xZGMPlTh4Q6gHsciPSPQAQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%B0%9B%E5%B0%9B%E5%B0%9B%E5%B0%9B%E4%B8%B6%E5%B0%9B%E9%99%8C&ie=utf-8&id=tb.1.632d5b40.xZGMPlTh4Q6gHsciPSPQAQ&fr=frs" target="_blank">尛尛尛尛...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6966018457,&quot;author_name&quot;:&quot;dhurdjutgi8rf&quot;,&quot;author_nickname&quot;:&quot;\u7403\u68d2\u4eba\u266c&quot;,&quot;author_portrait&quot;:&quot;tb.1.9c466eb7.742BIeLW6-O3K5too1GPYQ&quot;,&quot;first_post_id&quot;:135051378623,&quot;reply_num&quot;:79,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6966018457' data-thread-type="0" data-floor='5''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">79</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6966018457" title="罗罗诺亚·索隆，未来的世界第一大剑豪，我觉得索隆才是草帽团二" target="_blank" class="j_th_tit ">罗罗诺亚·索隆，未来的世界第一大剑豪，我觉得索隆才是草帽团二</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 球棒人♬"
          data-field='{&quot;user_id&quot;:3405312259}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;dhurdjutgi8rf&quot;,&quot;id&quot;:&quot;tb.1.9c466eb7.742BIeLW6-O3K5too1GPYQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=dhurdjutgi8rf&ie=utf-8&id=tb.1.9c466eb7.742BIeLW6-O3K5too1GPYQ&fr=frs" target="_blank">球棒人<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-10.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            罗罗诺亚·索隆，未来的世界第一大剑豪，我觉得索隆才是草帽团二号人物，和之国之后草帽团悬赏肯定第二 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6966018457"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="86362" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=c91c7070a751f819f1700b48ea8466d4/04f1d100baa1cd118285847bae12c8fcc3ce2d6c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=b95aca48ca54564ee565e43183e59d82/4610b912c8fcc3ce33f33f688545d688d43f20be.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971677222,&quot;author_name&quot;:&quot;\u5c0f\u8c6aXASJj&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.1264aa32.MJK4pVUoE0FalidWJy6FvA&quot;,&quot;first_post_id&quot;:135118028788,&quot;reply_num&quot;:7,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971677222' data-thread-type="0" data-floor='6''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">7</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971677222" title="第一次发，不知道格式正不正确。其实很多红发巴基同框的画面，从" target="_blank" class="j_th_tit ">第一次发，不知道格式正不正确。其实很多红发巴基同框的画面，从</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 小豪XASJj"
          data-field='{&quot;user_id&quot;:516889544}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5c0f\u8c6aXASJj&quot;,&quot;id&quot;:&quot;tb.1.1264aa32.MJK4pVUoE0FalidWJy6FvA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%B0%8F%E8%B1%AAXASJj&ie=utf-8&id=tb.1.1264aa32.MJK4pVUoE0FalidWJy6FvA&fr=frs" target="_blank">小豪XASJj</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -1050px  0;top:0px;left:0px" data-slot="1"  data-name="jinniu" data-field='{&quot;name&quot;:&quot;jinniu&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u91d1\u725b\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,21&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="金牛座印记"  locate="jinniu_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -550px  0;top:0px;left:28px" data-slot="2"  data-name="gold_jinniu" data-field='{&quot;name&quot;:&quot;gold_jinniu&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;2&quot;,&quot;title&quot;:&quot;\u91d1\u725b\u5ea7\u9ec4\u91d1\u7248\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u96c6\u9f5012\u4e2a\u661f\u5ea7\u5370\u8bb0\u53ef\u4ee5\u83b7\u5f9712\u4e2a\u9ec4\u91d1\u7248\u661f\u5ea7\u5370\u8bb0\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,11&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="金牛座黄金版印记"  locate="gold_jinniu_1#icon"  style="top: 0px; left:28px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">18:00</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            第一次发，不知道格式正不正确。 其实很多红发巴基同框的画面，从尾田态度和同框的画面来看，我觉得他俩人就是“不相上下的死对头”。 红发很强，而且如果说比巴基强我也同意，但是仅仅是强一点，一点的意思大概就是“20道力”以内吧，就是形式上让红发当四皇，无论以后会不会是海贼王，都提前把坑填好。毕竟巴基也是七武海，七武海和四皇，海军又是三大势力，这都是尾田的暗示
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 在做渣渣">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5728\u505a\u6e23\u6e23&quot;,&quot;id&quot;:&quot;tb.1.4e305158.CC3PHGGSuc9WJUgllz0Nww&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%9C%A8%E5%81%9A%E6%B8%A3%E6%B8%A3&ie=utf-8&id=tb.1.4e305158.CC3PHGGSuc9WJUgllz0Nww&fr=frs" target="_blank">在做渣渣</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:5645058118,&quot;author_name&quot;:&quot;\u7fbd\u7eb1\u5feb\u4e50&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.8eaa9b1a.1KL_2jEnUQVMFMWAOed17Q&quot;,&quot;first_post_id&quot;:119133973957,&quot;reply_num&quot;:303533,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='5645058118' data-thread-type="0" data-floor='7''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">303533</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5645058118" title="海贼酒吧【文字扮演】" target="_blank" class="j_th_tit ">海贼酒吧【文字扮演】</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 羽纱快乐"
          data-field='{&quot;user_id&quot;:524276432}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7fbd\u7eb1\u5feb\u4e50&quot;,&quot;id&quot;:&quot;tb.1.8eaa9b1a.1KL_2jEnUQVMFMWAOed17Q&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%BE%BD%E7%BA%B1%E5%BF%AB%E4%B9%90&ie=utf-8&id=tb.1.8eaa9b1a.1KL_2jEnUQVMFMWAOed17Q&fr=frs" target="_blank">羽纱快乐</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><span class="j_icon_slot old_icon_size" style="filter: progid:DXImageTransform.Microsoft.AlphaImageLoader(src=https://imgsa.baidu.com/forum/pic/item/500fd9f9d72a60593de2e2952a34349b023bba4a.png, sizingMethod=scale); background: url(https://imgsa.baidu.com/forum/pic/item/500fd9f9d72a60593de2e2952a34349b023bba4a.png) no-repeat center  center;top:0px;left:0px; background-size: cover;"data-field='{&quot;name&quot;:null,&quot;end_time&quot;:null,&quot;category_id&quot;:null,&quot;slot_no&quot;:null,&quot;title&quot;:null,&quot;intro&quot;:null,&quot;intro_url&quot;:null,&quot;price&quot;:null,&quot;value&quot;:null,&quot;sprite&quot;:null}' data-slot="1" data-name="is_lottery"  class="j_icon_slot" title="银牌世界杯达人" locate="is_lottery_3#icon" style="top:0px;left:0px"><div class=" j_icon_slot_refresh"></div></span></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2018-04</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            这里是位于伟大航路上一个不起眼的小镇上的一个小酒馆。酒馆的主人是一位少女，或许有人认识他，几年前，她还活跃在这个大陆上，那时人们称她为洛娅，几年后，她在这个地方开了个酒馆，至于原因，无人而知。 这是一个文字扮演游戏，（所有的行动都以小说形式表达）， 　　规则如下： 　　创建一个角色，想好名字、外貌、身份。 　　这个角色可以是d之一族，镇子里的乡民等.伟大航路中各个势力的成员，或许是某个不起眼的学校的某个不
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 青红黑-白银灰">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8ff7\u7684\u6d77&quot;,&quot;id&quot;:&quot;tb.1.e98bc12.r0nVZRs6fiJd10frCAVqiQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%BF%B7%E7%9A%84%E6%B5%B7&ie=utf-8&id=tb.1.e98bc12.r0nVZRs6fiJd10frCAVqiQ&fr=frs" target="_blank">青红黑<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6956365150,&quot;author_name&quot;:&quot;\u6cb3\u9a6c\u9f99&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.eda71c42.Zr8fJHkSTJEDWO34YqDmow&quot;,&quot;first_post_id&quot;:134958817628,&quot;reply_num&quot;:795,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6956365150' data-thread-type="0" data-floor='8''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">795</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6956365150" title="真的是这么一回事吗？" target="_blank" class="j_th_tit ">真的是这么一回事吗？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 河马龙"
          data-field='{&quot;user_id&quot;:404339983}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6cb3\u9a6c\u9f99&quot;,&quot;id&quot;:&quot;tb.1.eda71c42.Zr8fJHkSTJEDWO34YqDmow&quot;}' title="该用户已经连续签到35天了，连续30天一举“橙”名" class="frs-author-name sign_highlight j_user_card " href="/home/main/?un=%E6%B2%B3%E9%A9%AC%E9%BE%99&ie=utf-8&id=tb.1.eda71c42.Zr8fJHkSTJEDWO34YqDmow&fr=frs" target="_blank">河马龙</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            真的是这么一回事吗？ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6956365150"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="81431" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=bad5f96379061d957d133f3a4bc426e8/21e951da81cb39dba529e70dc7160924aa1830a9.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=84de8525321f95caa6f592bef92c7e3e/5366d0160924ab1884ff616c22fae6cd7a890bfb.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: -听一半的曲">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;shuffle\u9896&quot;,&quot;id&quot;:&quot;tb.1.fa7b378e.w5-wsZcjDX77yr6w9fXaBw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=shuffle%E9%A2%96&ie=utf-8&id=tb.1.fa7b378e.w5-wsZcjDX77yr6w9fXaBw&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>听一半...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969780019,&quot;author_name&quot;:&quot;\u706b\u7bad\u6ce1\u6ce1\u7cd6&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.8dd54735.ygyxH-xZX91kvLWRR_hXiA&quot;,&quot;first_post_id&quot;:135096555713,&quot;reply_num&quot;:170,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969780019' data-thread-type="0" data-floor='9''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">170</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969780019" title="看完970话！感觉凯多好渣！" target="_blank" class="j_th_tit ">看完970话！感觉凯多好渣！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 火箭泡泡糖"
          data-field='{&quot;user_id&quot;:1818985625}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u706b\u7bad\u6ce1\u6ce1\u7cd6&quot;,&quot;id&quot;:&quot;tb.1.8dd54735.ygyxH-xZX91kvLWRR_hXiA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%81%AB%E7%AE%AD%E6%B3%A1%E6%B3%A1%E7%B3%96&ie=utf-8&id=tb.1.8dd54735.ygyxH-xZX91kvLWRR_hXiA&fr=frs" target="_blank">火箭泡泡糖</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -900px  0;top:0px;left:0px" data-slot="1"  data-name="shizi" data-field='{&quot;name&quot;:&quot;shizi&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u72ee\u5b50\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,18&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="狮子座印记"  locate="shizi_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            看完970话！感觉凯多好渣！ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969780019"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="19539" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=ff19c825321f95caa6a09ab4f9275307/4e9ad0a20cf431ada3fc8e625c36acaf2edd9869.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=391c2192c02a60595210e112180f359b/77094b36acaf2eddcbdf84b29a1001e9390193bb.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="50747" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=93c65505cac451daf6a304e986cd7e5f/01d7af51f3deb48f04476c85e71f3a292df57869.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=2527a1e9a5b7d0a27bc90495fbd47709/95eef01f3a292df568ed614eab315c6034a873bb.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 小公举啦🌞">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;heart\u6e9f\u7687&quot;,&quot;id&quot;:&quot;tb.1.e57ad6ad.u3vwbJKP7urss6_jAEHG0g&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=heart%E6%BA%9F%E7%9A%87&ie=utf-8&id=tb.1.e57ad6ad.u3vwbJKP7urss6_jAEHG0g&fr=frs" target="_blank">小公举啦<img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-28.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970611603,&quot;author_name&quot;:&quot;\u5341\u5206\u559c\u6b22_&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.6da69f8e.3xgiFo-ELj6tDuASsxUiQA&quot;,&quot;first_post_id&quot;:135107958109,&quot;reply_num&quot;:67,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970611603' data-thread-type="0" data-floor='10''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">67</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6970611603" title="理性讨论，多弗朗明哥真的如大家所说，连饼干都不如吗" target="_blank" class="j_th_tit ">理性讨论，多弗朗明哥真的如大家所说，连饼干都不如吗</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 十分喜欢_"
          data-field='{&quot;user_id&quot;:3582163455}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5341\u5206\u559c\u6b22_&quot;,&quot;id&quot;:&quot;tb.1.6da69f8e.3xgiFo-ELj6tDuASsxUiQA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%8D%81%E5%88%86%E5%96%9C%E6%AC%A2_&ie=utf-8&id=tb.1.6da69f8e.3xgiFo-ELj6tDuASsxUiQA&fr=frs" target="_blank">十分喜欢_</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10:04</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            确实在跟路飞的战斗中，完全跟不上四挡的速度，但是用与主角的战斗来做对比，真的公平吗？ 无挡打败沙鳄鱼，二挡打败路奇，不会霸气碾压自然系艾尼路，和卡二战斗犹如不倒翁，你能说这些人很弱吗？ 路飞的实力刻画一直很迷不是总所皆知吗？突然很强，突然被一棒子秒杀，突然打败卡二，又在阿普那吃瘪。 我只说明哥侧面的战斗，顶上战争定住乔兹、虽然大喘气但是和青雉短暂对决、追杀莫利亚、秒杀罗、吃罗装死大招伽玛刀依旧和路飞战
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6970611603"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="75178" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=2bd5c88361094b36dbc713ef93fc50e0/9efdf703918fa0ec12825251319759ee3c6ddbd6.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=aa29fb759118367aad897fd51e488ad4/503d269759ee3d6d4f83b19754166d224f4ade20.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="21082" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=5d3a754d06dfa9ecfd7b5e1552e0db3a/6b06d40735fae6cdd460bc3018b30f2443a70fbc.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=66d452ae2cc79f3d8fe1e4388a9acc11/9f510fb30f2442a776daeaf4c643ad4bd013028e.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="47036" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=8f5da874802bd4074292dbff4bb9b268/1cd39925bc315c60b2d15db39ab1cb13485477d7.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=2ad62db1b4cc7cd9fa2d34d1093a203f/5fdf8db1cb1349548f5ade38414e9258d1094a21.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: uruti😈">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;lvtianqi777&quot;,&quot;id&quot;:&quot;tb.1.8e560f92.3_57KDRtKxvdGMvJwhtL9w&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=lvtianqi777&ie=utf-8&id=tb.1.8e560f92.3_57KDRtKxvdGMvJwhtL9w&fr=frs" target="_blank">uruti<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-35.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971682945,&quot;author_name&quot;:&quot;\u5bfb\u627e\u8ff7\u832b\u7684\u75af\u5b50&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.f783b61f.UibucdNQ6ESJCyhPVFIeEQ&quot;,&quot;first_post_id&quot;:135118090663,&quot;reply_num&quot;:9,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971682945' data-thread-type="0" data-floor='11''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">9</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971682945" title="什么才叫最强的生物" target="_blank" class="j_th_tit ">什么才叫最强的生物</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 寻找迷茫的疯子"
          data-field='{&quot;user_id&quot;:2541250525}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5bfb\u627e\u8ff7\u832b\u7684\u75af\u5b50&quot;,&quot;id&quot;:&quot;tb.1.f783b61f.UibucdNQ6ESJCyhPVFIeEQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%AF%BB%E6%89%BE%E8%BF%B7%E8%8C%AB%E7%9A%84%E7%96%AF%E5%AD%90&ie=utf-8&id=tb.1.f783b61f.UibucdNQ6ESJCyhPVFIeEQ&fr=frs" target="_blank">寻找迷茫...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">18:03</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
             @千y丶千尋 读者：我的麻麻和爆了白胡子头 打败了大将青雉的赤犬 谁更厉害啊。 尾田：你是脑子出现了问题吗？ 这种废话也能说出来？赤犬的实力配跟你的麻麻相比？麻麻可是3次元第一战斗力 世界最强生物啊。怎么也得让海贼王史上最强凯多才有资格相比吧。现在你知道他们的差距有多大了吧，赤犬连相比的资格 都没有 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971682945"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="67648" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=39b60bffc7a20cf446c5f6dd4639670f/edf2a9ec8a13632702e44e4b868fa0ec08fac76f.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=13b9103f2e12b31bc76ccd21b623377a/f603918fa0ec08fa31099fdf4eee3d6d55fbdab9.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="39523" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=027e528a6a1ed21b799c26e79d5ef1fd/6cc276c6a7efce1b18fc0bb2b851f3deb58f65a5.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=e0d2fa9f862397ddd679980c69b9b3b7/fcfaaf51f3deb48f09be62a6e71f3a292cf578f7.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="70445" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=da99fe9695025aafd36776c9cbdd875d/60afd158ccbf6c818b8094beab3eb13532fa40da.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=444858049235e5dd902ca5d746fda6ef/18d8bc3eb13533fa89012b78bfd3fd1f41345b34.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 大将是天龙狗⛅">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;odf\u9b54\u672f\u80f8\u7f69&quot;,&quot;id&quot;:&quot;tb.1.73e758f4.0SD9UT6B8XGw-dq-U1saew&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=odf%E9%AD%94%E6%9C%AF%E8%83%B8%E7%BD%A9&ie=utf-8&id=tb.1.73e758f4.0SD9UT6B8XGw-dq-U1saew&fr=frs" target="_blank">大将是天...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:20        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6949846075,&quot;author_name&quot;:&quot;gzdmbzm&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.b90664de.Vd3c6ciYzbnQed1bLG965g&quot;,&quot;first_post_id&quot;:134887833809,&quot;reply_num&quot;:171,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6949846075' data-thread-type="0" data-floor='12''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">171</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6949846075" title="不懂就问，有恶魔果实真的重要嘛，为什么罗杰船上的人都不喜欢果" target="_blank" class="j_th_tit ">不懂就问，有恶魔果实真的重要嘛，为什么罗杰船上的人都不喜欢果</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: gzdmbzm"
          data-field='{&quot;user_id&quot;:2122256120}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;gzdmbzm&quot;,&quot;id&quot;:&quot;tb.1.b90664de.Vd3c6ciYzbnQed1bLG965g&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=gzdmbzm&ie=utf-8&id=tb.1.b90664de.Vd3c6ciYzbnQed1bLG965g&fr=frs" target="_blank">gzdmbzm</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-15</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            不懂就问，有恶魔果实真的重要嘛，为什么罗杰船上的人都不喜欢果实？红发害巴基吃了果实，巴基记了一辈子仇诶 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6949846075"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="80250" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=d07ad2779001a18bf0be1a4dae1f2b31/3fd0fc039245d6888f91e6ffb3c27d1ed31b2483.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=97110dea970a19d8cb03840d03c1838b/8694a4c27d1ed21b555a7abeba6eddc450da3fdd.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 💧水球碳酸拳🌐">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u94a2\u7259\u5927\u738b\u65e0\u654c&quot;,&quot;id&quot;:&quot;tb.1.ceda41d8.aBItCEQFv_rI2jpRbzJyBQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%92%A2%E7%89%99%E5%A4%A7%E7%8E%8B%E6%97%A0%E6%95%8C&ie=utf-8&id=tb.1.ceda41d8.aBItCEQFv_rI2jpRbzJyBQ&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-33.png" class="nicknameEmoji" style="width:13px;height:13px"/>水球碳...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:19        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969954092,&quot;author_name&quot;:&quot;q1306746007&quot;,&quot;author_nickname&quot;:&quot;\u6635\u79f0\u52a0\u8f7d\u4e2d\u00ba\u00ba&quot;,&quot;author_portrait&quot;:&quot;tb.1.25292d93.NBtCE-Tp85VLoG5Rkfxfnw&quot;,&quot;first_post_id&quot;:135098875906,&quot;reply_num&quot;:28,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969954092' data-thread-type="0" data-floor='13''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">28</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969954092" title="我记得布鲁克没有这么高的吧" target="_blank" class="j_th_tit ">我记得布鲁克没有这么高的吧</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 昵称加载中ºº"
          data-field='{&quot;user_id&quot;:3452772117}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;q1306746007&quot;,&quot;id&quot;:&quot;tb.1.25292d93.NBtCE-Tp85VLoG5Rkfxfnw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=q1306746007&ie=utf-8&id=tb.1.25292d93.NBtCE-Tp85VLoG5Rkfxfnw&fr=frs" target="_blank">昵称加载...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            我记得布鲁克没有这么高的吧
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969954092"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="12291" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=dc3b1d7a87ef76c6d087f329ad26d1c3/87e60a46f21fbe0952850c4f7c600c338644ad44.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=2473f01015087bf47dec57e1c2e8552c/f7246b600c338744d21ee027460fd9f9d62aa096.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 冷冷的塑料袋扣">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u51b7\u51b7\u7684\u5851\u6599\u888b\u6263&quot;,&quot;id&quot;:&quot;tb.1.879184fd.H4fdKUfM6jCPWu9oxoMTZA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%86%B7%E5%86%B7%E7%9A%84%E5%A1%91%E6%96%99%E8%A2%8B%E6%89%A3&ie=utf-8&id=tb.1.879184fd.H4fdKUfM6jCPWu9oxoMTZA&fr=frs" target="_blank">冷冷的塑...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            17:21        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970419081,&quot;author_name&quot;:&quot;starzhou\u4f1f&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.70db7501.TlawaJBRnvf40D-CQwpoDA&quot;,&quot;first_post_id&quot;:135106068353,&quot;reply_num&quot;:9,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970419081' data-thread-type="0" data-floor='14''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">9</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6970419081" title="看赤狗被暴揍 好爽。。" target="_blank" class="j_th_tit ">看赤狗被暴揍 好爽。。</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: starzhou伟"
          data-field='{&quot;user_id&quot;:378175059}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;starzhou\u4f1f&quot;,&quot;id&quot;:&quot;tb.1.70db7501.TlawaJBRnvf40D-CQwpoDA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=starzhou%E4%BC%9F&ie=utf-8&id=tb.1.70db7501.TlawaJBRnvf40D-CQwpoDA&fr=frs" target="_blank">starzhou伟</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">08:18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            看赤狗被暴揍 好爽。。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6970419081"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="48102" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=0305b8548c504fc2a20ab807d5edcb28/f5da90529822720e20d8d6a66ccb0a46f21fab01.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=331be848af99a9013b355b3e2dae0b7b/d6ca7bcb0a46f21f92226a0fe1246b600c33ae53.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="15702" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=c4d1ae3de4deb48ffb3ca9dcc02f1610/f01e8744ebf81a4c6824d895c02a6059252da601.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=6e0710b3beec8a13141a57e8c738908f/d8f9d72a6059252ded012958239b033b5bb5b953.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="26307" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=4208dc38414e9258a6618eecacb2fd61/4a2d3af33a87e9507e01c73007385343fbf2b401.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=046121c8512309f7e76fad1a42350df3/c75c10385343fbf2f93a927fa77eca8065388f53.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 鸡儿伽美什✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5b87\u667a\u6ce2\u58eb\u90ce_&quot;,&quot;id&quot;:&quot;tb.1.cd3f67ce.v9fNRtsTyZYHz5Wp7EuWeg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%AE%87%E6%99%BA%E6%B3%A2%E5%A3%AB%E9%83%8E_&ie=utf-8&id=tb.1.cd3f67ce.v9fNRtsTyZYHz5Wp7EuWeg&fr=frs" target="_blank">鸡儿伽美...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:19        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6967888010,&quot;author_name&quot;:&quot;\u6625\u8336\u5e7f\u9999&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.f1732b12.yUpUGo2FGizUgFTx2QlE1g&quot;,&quot;first_post_id&quot;:135072354520,&quot;reply_num&quot;:160,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6967888010' data-thread-type="0" data-floor='15''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">160</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6967888010" title="罗杰死后，如果白胡子想当海贼王，自己去找能找到吗？" target="_blank" class="j_th_tit ">罗杰死后，如果白胡子想当海贼王，自己去找能找到吗？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 春茶广香"
          data-field='{&quot;user_id&quot;:3007151661}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6625\u8336\u5e7f\u9999&quot;,&quot;id&quot;:&quot;tb.1.f1732b12.yUpUGo2FGizUgFTx2QlE1g&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%98%A5%E8%8C%B6%E5%B9%BF%E9%A6%99&ie=utf-8&id=tb.1.f1732b12.yUpUGo2FGizUgFTx2QlE1g&fr=frs" target="_blank">春茶广香</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,76&quot;,&quot;2&quot;:&quot;1599647089,77&quot;,&quot;3&quot;:&quot;1599647089,78&quot;,&quot;4&quot;:&quot;1599647089,79&quot;,&quot;5&quot;:&quot;1599647089,80&quot;,&quot;6&quot;:&quot;1599647089,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-19</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            罗杰死后，如果白胡子想当海贼王，自己去找能找到吗？ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6967888010"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="3503" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=46bffbcf512309f7e73aa510423e20ca/07c0ab64034f78f0fec374a86e310a55b2191c4a.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=ad37a675c51b0ef46ce89856edff53da/aec379310a55b319e2316c2e54a98226cefc17a4.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 贴吧用户_5btbMPP">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.2748a678.FLLaScYpSUwk4vg-CAWSbQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.2748a678.FLLaScYpSUwk4vg-CAWSbQ&fr=frs" target="_blank">贴吧用户_...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:19        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971695153,&quot;author_name&quot;:&quot;\u62db\u957f\u671f\u4e3b\u6301&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.8896c417.T6xcEsrYskMuZqH6Q5k12w&quot;,&quot;first_post_id&quot;:135118224763,&quot;reply_num&quot;:7,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971695153' data-thread-type="0" data-floor='16''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">7</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971695153" title="快，手。交友做主持有兴趣吗有兴趣的小姐姐小哥哥私聊" target="_blank" class="j_th_tit ">快，手。交友做主持有兴趣吗有兴趣的小姐姐小哥哥私聊</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 招长期主持"
          data-field='{&quot;user_id&quot;:4942564681}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u62db\u957f\u671f\u4e3b\u6301&quot;,&quot;id&quot;:&quot;tb.1.8896c417.T6xcEsrYskMuZqH6Q5k12w&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%8B%9B%E9%95%BF%E6%9C%9F%E4%B8%BB%E6%8C%81&ie=utf-8&id=tb.1.8896c417.T6xcEsrYskMuZqH6Q5k12w&fr=frs" target="_blank">招长期主持</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">18:10</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            快，手。交友做主持 有兴趣吗 有兴趣的小姐姐小哥哥私聊
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:19        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6945347379,&quot;author_name&quot;:&quot;\u5bd2\u51b0aHct&quot;,&quot;author_nickname&quot;:&quot;\u6211\u7231\u6d41\u5ddd\u67ab\ud83d\ude18&quot;,&quot;author_portrait&quot;:&quot;tb.1.2b0f4620.i8Os62mUFPoMKk9YgBub9w&quot;,&quot;first_post_id&quot;:134837932469,&quot;reply_num&quot;:417,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6945347379' data-thread-type="0" data-floor='17''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">417</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6945347379" title="尾田的格局真的不行了，才华更是江郎才尽作为一个资深海迷都有点" target="_blank" class="j_th_tit ">尾田的格局真的不行了，才华更是江郎才尽作为一个资深海迷都有点</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 我爱流川枫😘"
          data-field='{&quot;user_id&quot;:3448292349}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5bd2\u51b0aHct&quot;,&quot;id&quot;:&quot;tb.1.2b0f4620.i8Os62mUFPoMKk9YgBub9w&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%AF%92%E5%86%B0aHct&ie=utf-8&id=tb.1.2b0f4620.i8Os62mUFPoMKk9YgBub9w&fr=frs" target="_blank">我爱流川...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-13</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            尾田的格局真的不行了，才华更是江郎才尽作为一个资深海迷都有点反感海贼了 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6945347379"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="72907" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=f113f16c22fae6cd0ce1a3633f83231d/401c5c6034a85edfeb89ee785e540923dd547515.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=c5f459b29a1001e94e3c140788357aec/ca1349540923dd543076b733c609b3de9c824867.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 醉醉丶7">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9189\u9189\u4e367&quot;,&quot;id&quot;:&quot;tb.1.c89826b0.vIHI5WLIiSuHXPWw6UgO8A&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%86%89%E9%86%89%E4%B8%B67&ie=utf-8&id=tb.1.c89826b0.vIHI5WLIiSuHXPWw6UgO8A&fr=frs" target="_blank">醉醉丶7</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6074152544,&quot;author_name&quot;:&quot;\u77f3\u5934\u53f6\u5b50\u98ce&quot;,&quot;author_nickname&quot;:&quot;\u534a\u9053\u5f69\u8679\ud83c\udf08&quot;,&quot;author_portrait&quot;:&quot;tb.1.a3531d51.LEYP4gvF8yqW3Ul7d8ccBQ&quot;,&quot;first_post_id&quot;:124681917636,&quot;reply_num&quot;:21,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6074152544' data-thread-type="0" data-floor='18''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">21</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6074152544" title="为什么都认为打凯多是群殴呢，就不能是路飞单挑凯多吗？" target="_blank" class="j_th_tit ">为什么都认为打凯多是群殴呢，就不能是路飞单挑凯多吗？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 半道彩虹🌈"
          data-field='{&quot;user_id&quot;:1464647704}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u77f3\u5934\u53f6\u5b50\u98ce&quot;,&quot;id&quot;:&quot;tb.1.a3531d51.LEYP4gvF8yqW3Ul7d8ccBQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%9F%B3%E5%A4%B4%E5%8F%B6%E5%AD%90%E9%A3%8E&ie=utf-8&id=tb.1.a3531d51.LEYP4gvF8yqW3Ul7d8ccBQ&fr=frs" target="_blank">半道彩虹<img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-24.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -950px  0;top:0px;left:0px" data-slot="1"  data-name="sheshou" data-field='{&quot;name&quot;:&quot;sheshou&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u5c04\u624b\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,19&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="射手座印记"  locate="sheshou_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">2019-03</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            为什么都认为打凯多是群殴呢，就不能是路飞单挑凯多吗？
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 贴吧用户_7UR5QAA">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.825c9777.kK8Nl3W43KSyn_nmBR5JBg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.825c9777.kK8Nl3W43KSyn_nmBR5JBg&fr=frs" target="_blank">贴吧用户_...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:13        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969172361,&quot;author_name&quot;:&quot;zxzzxz010203&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.6eb3de25.AKb2amHYqlN-gX-TEvXw1Q&quot;,&quot;first_post_id&quot;:135089087380,&quot;reply_num&quot;:7,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969172361' data-thread-type="0" data-floor='19''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">7</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969172361" title="建议海贼王动画改名水贼王，漫画改名休刊王" target="_blank" class="j_th_tit ">建议海贼王动画改名水贼王，漫画改名休刊王</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: zxzzxz010203"
          data-field='{&quot;user_id&quot;:171355201}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;zxzzxz010203&quot;,&quot;id&quot;:&quot;tb.1.6eb3de25.AKb2amHYqlN-gX-TEvXw1Q&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=zxzzxz010203&ie=utf-8&id=tb.1.6eb3de25.AKb2amHYqlN-gX-TEvXw1Q&fr=frs" target="_blank">zxzzxz010203</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            建议海贼王动画改名水贼王，漫画改名休刊王
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: zxzzxz010203">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;zxzzxz010203&quot;,&quot;id&quot;:&quot;tb.1.6eb3de25.AKb2amHYqlN-gX-TEvXw1Q&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=zxzzxz010203&ie=utf-8&id=tb.1.6eb3de25.AKb2amHYqlN-gX-TEvXw1Q&fr=frs" target="_blank">zxzzxz010203</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971688763,&quot;author_name&quot;:&quot;year\u690d2\u8ff7&quot;,&quot;author_nickname&quot;:&quot;\u67d0\u79d1\u5b66\u7684\u675c\u82f1\u264b&quot;,&quot;author_portrait&quot;:&quot;tb.1.ec4853da.1TxmwXrhEagVktyWYvM6Aw&quot;,&quot;first_post_id&quot;:135118154896,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971688763' data-thread-type="0" data-floor='20''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">5</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971688763" title="重新修改了一下，画渣，勉强看看吧" target="_blank" class="j_th_tit ">重新修改了一下，画渣，勉强看看吧</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 某科学的杜英♋"
          data-field='{&quot;user_id&quot;:4357435405}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;year\u690d2\u8ff7&quot;,&quot;id&quot;:&quot;tb.1.ec4853da.1TxmwXrhEagVktyWYvM6Aw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=year%E6%A4%8D2%E8%BF%B7&ie=utf-8&id=tb.1.ec4853da.1TxmwXrhEagVktyWYvM6Aw&fr=frs" target="_blank">某科学的...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">18:07</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            重新修改了一下，画渣，勉强看看吧 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971688763"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="30819" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=a4d6c06cada1cd1105e37a228922e4c5/c52c213fb80e7bec08ed27bd382eb9389b506b60.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=8933a76c2df33a879e6d0012f6671138/37d12f2eb9389b5013c8c40e9235e5dde7116eb2.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6967966001,&quot;author_name&quot;:&quot;Andjbot\u9f99&quot;,&quot;author_nickname&quot;:&quot;\u4e16\u754c\u738b\u8005\u9882\u5df4\u00ba&quot;,&quot;author_portrait&quot;:&quot;tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&quot;,&quot;first_post_id&quot;:135073355489,&quot;reply_num&quot;:44,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6967966001' data-thread-type="0" data-floor='21''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">44</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6967966001" title="海贼王中被一笔带过的鱼人强者!" target="_blank" class="j_th_tit ">海贼王中被一笔带过的鱼人强者!</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 世界王者颂巴º"
          data-field='{&quot;user_id&quot;:1747699741}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Andjbot\u9f99&quot;,&quot;id&quot;:&quot;tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&quot;}' title="该用户已经连续签到36天了，连续30天一举“橙”名" class="frs-author-name sign_highlight j_user_card " href="/home/main/?un=Andjbot%E9%BE%99&ie=utf-8&id=tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&fr=frs" target="_blank">世界王者...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-19</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            不知道你们还记得没有，顶上战争的时候出现了一个鱼人高手那就是白团八队长那缪尔他的身上有8的符号，白团被称为世界最强海贼团，能成为白团队长的都是新世界的高手，这家伙的实力怎么也有佐佐木水平吧？参考第16队长以藏，白团队长都是高手这也是为什么白团能被称为最强的原因吧，这只是其中一个还有很多被一笔带过的白团强者或许都已经被我们遗忘了，希望以后尾田会揭露他们的实力。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6967966001"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="19360" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=4039a2557009c93d07a706f5af0dd4e5/b71bacaf2edda3ccf5f7507b16e93901213f920c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=a11ae9f0143b5bb5bed720f606e8d439/8c1001e93901213f3120a68743e736d12f2e955e.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="7182" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=acdac6beba6eddc426b2bcf909eb9ac4/613bfdfaaf51f3de16a1513f83eef01f3a29790c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=036a705f4e82b2b7a79f39cc0196caef/8d5494eef01f3a298fdb3d958e25bc315c607c5e.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="663" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=8bd52686bc64034f0f98ca049ff35508/e5f5bc3eb13533fa42a57b75bfd3fd1f41345b0c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=50c1abadb0efce1bea2bc8c29f6af2de/a71ea8d3fd1f41345724ed25321f95cad1c85e5e.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 世界王者颂巴º">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Andjbot\u9f99&quot;,&quot;id&quot;:&quot;tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Andjbot%E9%BE%99&ie=utf-8&id=tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&fr=frs" target="_blank">世界王者...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971680098,&quot;author_name&quot;:&quot;&quot;,&quot;author_nickname&quot;:&quot;\u5931\u7720\u7684\u61d2\u61d2\ud83d\ude08&quot;,&quot;author_portrait&quot;:&quot;tb.1.171647cd.CSCEI3OmMMp3JpXw9s1xCA&quot;,&quot;first_post_id&quot;:135118059148,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971680098' data-thread-type="0" data-floor='22''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">4</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971680098" title="锦卫门：我比小菊高" target="_blank" class="j_th_tit ">锦卫门：我比小菊高</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 失眠的懒懒😈"
          data-field='{&quot;user_id&quot;:2261104450}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.171647cd.CSCEI3OmMMp3JpXw9s1xCA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.171647cd.CSCEI3OmMMp3JpXw9s1xCA&fr=frs" target="_blank">失眠的懒...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">18:02</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            锦卫门：我比小菊高 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971680098"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="27095" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=77f285a6c6c8a786be7f420c5739e504/f0d931adcbef760919dbbcc339dda3cc7dd99e43.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=85c77035322dd42a5f0901a3330059b5/adaf2edda3cc7cd9dffd11852e01213fb90e919d.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="38978" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=258bc07a1e24ab18e043e93505cacaf4/c6042df5e0fe9925cbdc4c0c23a85edf8cb17143.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=01e45b5abbaf2eddd4f149e1bd2b03e9/5d6034a85edf8db1bcfe59381e23dd54574e749d.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:17        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969466179,&quot;author_name&quot;:&quot;\u6211\u662f\u4e00\u4ee3\u5e1d\u738b&quot;,&quot;author_nickname&quot;:&quot;\u5a1c\u83f2\u9c81\u5854\u5229\ud83c\udf3a&quot;,&quot;author_portrait&quot;:&quot;tb.1.d4398650.0zG96AwuPnDR3ayxRwhThw&quot;,&quot;first_post_id&quot;:135092486926,&quot;reply_num&quot;:77,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969466179' data-thread-type="0" data-floor='23''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">77</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit  member_thread_title_frs ">
    
    
    <a rel="noreferrer" href="/p/6969466179" title="有什么果实是比糯米更适合卡二用的？" target="_blank" class="j_th_tit ">有什么果实是比糯米更适合卡二用的？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author no_icon_author"
          title="主题作者: 娜菲鲁塔利🌺"
          data-field='{&quot;user_id&quot;:1867432841}' ><i class="icon_author"></i><span class="pre_icon_wrap pre_icon_wrap_theme1 frs_bright_preicon"><a class="icon-vip3-16" title="本吧会员" href="#" onclick="return false;" data-field='{&quot;user_id&quot;:1867432841}' target="_blank"></a></span><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6211\u662f\u4e00\u4ee3\u5e1d\u738b&quot;,&quot;id&quot;:&quot;tb.1.d4398650.0zG96AwuPnDR3ayxRwhThw&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=%E6%88%91%E6%98%AF%E4%B8%80%E4%BB%A3%E5%B8%9D%E7%8E%8B&ie=utf-8&id=tb.1.d4398650.0zG96AwuPnDR3ayxRwhThw&fr=frs" target="_blank">娜菲鲁塔...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/105_14.png?stamp=1599647089) no-repeat -0px  0;top:0px;left:0px" data-slot="1"  data-name="luffy" data-field='{&quot;name&quot;:&quot;luffy&quot;,&quot;end_time&quot;:&quot;1601830191&quot;,&quot;category_id&quot;:105,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u8def\u98de\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u5151\u6362\u6d77\u8d3c\u738b\u5427\u4f1a\u5458\u83b7\u5f97\u672c\u4e13\u5c5e\u5370\u8bb0&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=%BA%A3%D4%F4%CD%F5&amp;fr=index&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,0&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=%BA%A3%D4%F4%CD%F5&amp;fr=index"  class="j_icon_slot"  title="路飞印记"  locate="luffy_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -450px  0;top:0px;left:28px" data-slot="2"  data-name="meizituan1" data-field='{&quot;name&quot;:&quot;meizituan1&quot;,&quot;end_time&quot;:&quot;1600746510&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;2&quot;,&quot;title&quot;:&quot;\u59b9\u5b50\u56e2\u6210\u5458\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u5173\u6ce8\u82f1\u4e09\u5609\u54e5\u5427\uff0c\u7533\u8bf7\u52a0\u5165\u59b9\u5b50\u56e2\uff01\uff08\u6709\u6548\u671f30\u5929\uff09&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%8B%B1%E4%B8%89%E5%98%89%E5%93%A5&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,9&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%8B%B1%E4%B8%89%E5%98%89%E5%93%A5&amp;fr=search"  class="j_icon_slot"  title="妹子团成员印记"  locate="meizituan1_1#icon"  style="top: 0px; left:28px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            糯米果实本身并不棘手，真正强的是卡二的超强见闻色和武装色，什么果实是最适合卡二的？ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969466179"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="45847" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=2ea088a01d46f21fc9615651c6144759/4f34ebc4b74543a97b4c3c9709178a82b80114c0.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=78a1cab0a1fd5266a72b3c1c9b23962b/cefc1e178a82b901b3fa0568648da9773912ef13.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 云深不知处⛅º">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4f60\u5bb6\u5c11\u4e3b\u4ed6\u59d3\u5f20&quot;,&quot;id&quot;:&quot;tb.1.5f1c0e49.aPWZGS4PcGxvS3f5LrmSqQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%BD%A0%E5%AE%B6%E5%B0%91%E4%B8%BB%E4%BB%96%E5%A7%93%E5%BC%A0&ie=utf-8&id=tb.1.5f1c0e49.aPWZGS4PcGxvS3f5LrmSqQ&fr=frs" target="_blank">云深不知...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:17        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6868851398,&quot;author_name&quot;:&quot;\u6f02\u4eae\u9a6c\u98de\u98de&quot;,&quot;author_nickname&quot;:&quot;\u665a\u5b89\u5362\u672c\u4f1f\ud83d\ude01&quot;,&quot;author_portrait&quot;:&quot;tb.1.ae1fcb18.kIzzOyR0Rn41BCaji6aasQ&quot;,&quot;first_post_id&quot;:133948670373,&quot;reply_num&quot;:565,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6868851398' data-thread-type="0" data-floor='24''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">565</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6868851398" title="赤犬这体质是怪物吗？看过动漫都知道白胡子一拳头下去赤犬都给打" target="_blank" class="j_th_tit ">赤犬这体质是怪物吗？看过动漫都知道白胡子一拳头下去赤犬都给打</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 晚安卢本伟😁"
          data-field='{&quot;user_id&quot;:2418918068}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6f02\u4eae\u9a6c\u98de\u98de&quot;,&quot;id&quot;:&quot;tb.1.ae1fcb18.kIzzOyR0Rn41BCaji6aasQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%BC%82%E4%BA%AE%E9%A9%AC%E9%A3%9E%E9%A3%9E&ie=utf-8&id=tb.1.ae1fcb18.kIzzOyR0Rn41BCaji6aasQ&fr=frs" target="_blank">晚安卢本...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">8-8</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            赤犬这体质是怪物吗？看过动漫都知道白胡子一拳头下去赤犬都给打扭曲了，愤怒的一击直接把岛都打沉了一半了，打到赤犬身上的冲击力都可以把海军总部给冲烂了，赤犬没死就算了，既然还能站起来接着战斗，事后不但没有治疗还敢去追黑胡子团，赤犬还是人类的体质？还是说他的果实有治疗效果的？ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6868851398"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="97296" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=d2467e7ffcc4b74534c1bf14ffcc322e/bd19970a304e251f4dd91caeb086c9177f3e536c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=6c9c413283eef01f4d1418cdd0c59825/d0c8a786c9177f3ebf1a045b67cf3bc79f3d56be.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="5660" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=430f4a67b68b87d65017a31d37380401/002e9245d688d43f778769a46a1ed21b0ef43b6c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=9c924d6c0ed8bc3ec60806c2b2b0a71e/a5c27d1ed21b0ef4ebc66008cac451da81cb3ebe.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 水墨_芳华">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6c34\u58a8_\u82b3\u534e&quot;,&quot;id&quot;:&quot;tb.1.8e88a43f.4gx34lkIbN__RiRBOJ6c4w&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%B0%B4%E5%A2%A8_%E8%8A%B3%E5%8D%8E&ie=utf-8&id=tb.1.8e88a43f.4gx34lkIbN__RiRBOJ6c4w&fr=frs" target="_blank">水墨_芳华</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:17        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6968905973,&quot;author_name&quot;:&quot;\u73a9\u6e38\u620f\u53ea\u56fe\u4e2a\u723d&quot;,&quot;author_nickname&quot;:&quot;\u9f99\u6f6d\u65b9\u65b9\u9762\ud83c\udf7a&quot;,&quot;author_portrait&quot;:&quot;tb.1.1295d9a4.cx2S08gJDBfY3d8Xk34xqg&quot;,&quot;first_post_id&quot;:135085975568,&quot;reply_num&quot;:44,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6968905973' data-thread-type="0" data-floor='25''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">44</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6968905973" title="怎么总感觉海贼王里的男角色都隐隐约约有一种大男子主义，打架不" target="_blank" class="j_th_tit ">怎么总感觉海贼王里的男角色都隐隐约约有一种大男子主义，打架不</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 龙潭方方面🍺"
          data-field='{&quot;user_id&quot;:1094752423}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u73a9\u6e38\u620f\u53ea\u56fe\u4e2a\u723d&quot;,&quot;id&quot;:&quot;tb.1.1295d9a4.cx2S08gJDBfY3d8Xk34xqg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%8E%A9%E6%B8%B8%E6%88%8F%E5%8F%AA%E5%9B%BE%E4%B8%AA%E7%88%BD&ie=utf-8&id=tb.1.1295d9a4.cx2S08gJDBfY3d8Xk34xqg&fr=frs" target="_blank">龙潭方方...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,76&quot;,&quot;2&quot;:&quot;1599647089,77&quot;,&quot;3&quot;:&quot;1599647089,78&quot;,&quot;4&quot;:&quot;1599647089,79&quot;,&quot;5&quot;:&quot;1599647089,80&quot;,&quot;6&quot;:&quot;1599647089,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            怎么总感觉海贼王里的男角色都隐隐约约有一种大男子主义，打架不舍得砍女人，女人不应该受伤。即使受伤也比男角色轻多了，根本就是皮外伤，看男角色受伤，基本都是重伤快死。尾田似乎也不舍得让女人受伤。
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 嗜杀肥猪💥">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6700\u7231sh5&quot;,&quot;id&quot;:&quot;tb.1.437ae77c.Fvi1Nyn_OmPu11s5KlSY5g&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=%E6%9C%80%E7%88%B1sh5&ie=utf-8&id=tb.1.437ae77c.Fvi1Nyn_OmPu11s5KlSY5g&fr=frs" target="_blank">嗜杀肥猪<img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-29.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:13        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969518501,&quot;author_name&quot;:&quot;wz88365&quot;,&quot;author_nickname&quot;:&quot;\ud83d\ude3ePony\ud83d\ude3e&quot;,&quot;author_portrait&quot;:&quot;tb.1.49e75e9.z54c4WPwc3oeCtrrbDs4UA&quot;,&quot;first_post_id&quot;:135093139715,&quot;reply_num&quot;:12,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969518501' data-thread-type="0" data-floor='26''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">12</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969518501" title="李嘉诚这么多钱在中国不是首富？" target="_blank" class="j_th_tit ">李嘉诚这么多钱在中国不是首富？</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 😾Pony😾"
          data-field='{&quot;user_id&quot;:979981081}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;wz88365&quot;,&quot;id&quot;:&quot;tb.1.49e75e9.z54c4WPwc3oeCtrrbDs4UA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=wz88365&ie=utf-8&id=tb.1.49e75e9.z54c4WPwc3oeCtrrbDs4UA&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-25.png" class="nicknameEmoji" style="width:13px;height:13px"/>Pony<img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-25.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            李嘉诚这么多钱在中国不是首富？
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969518501"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="2384" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=86384770a751f819f1700b48ea8466d4/04f1d100baa1cd11cda1b37bae12c8fcc3ce2d00.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=f67efd48ca54564ee565e43183e59d82/4610b912c8fcc3ce7cd708688545d688d43f2052.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 老司机💯℃">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5f26\u821e\u6b8b\u9633&quot;,&quot;id&quot;:&quot;tb.1.c38730b5.ihukrjH0TJDi1yj1EikxNQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%BC%A6%E8%88%9E%E6%AE%8B%E9%98%B3&ie=utf-8&id=tb.1.c38730b5.ihukrjH0TJDi1yj1EikxNQ&fr=frs" target="_blank">老司机<img src="//tb1.bdstatic.com/tb/cms/nickemoji/4-21.png" class="nicknameEmoji" style="width:13px;height:13px"/><img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-17.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6952166052,&quot;author_name&quot;:&quot;\u8d64\u773c\u5c0f\u5b50&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.f3533520.0kC7aGIqEx4sGQowRJSuzg&quot;,&quot;first_post_id&quot;:134913143885,&quot;reply_num&quot;:176,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6952166052' data-thread-type="0" data-floor='27''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">176</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6952166052" title="如果大和不上船，那她出现的意义是什么，冷不丁的出来个四皇之子" target="_blank" class="j_th_tit ">如果大和不上船，那她出现的意义是什么，冷不丁的出来个四皇之子</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 赤眼小子"
          data-field='{&quot;user_id&quot;:2169980311}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8d64\u773c\u5c0f\u5b50&quot;,&quot;id&quot;:&quot;tb.1.f3533520.0kC7aGIqEx4sGQowRJSuzg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%B5%A4%E7%9C%BC%E5%B0%8F%E5%AD%90&ie=utf-8&id=tb.1.f3533520.0kC7aGIqEx4sGQowRJSuzg&fr=frs" target="_blank">赤眼小子</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-16</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            如果大和不上船，那她出现的意义是什么，冷不丁的出来个四皇之子 冷不丁的断绝关系，最后再不上船冷不丁的又没她戏份了，大和出现不就奔着第十人的位子嘛，，，这需要争辩吗 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6952166052"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="33873" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=7a058968648da9774e7a8e298061d420/351070cf3bc79f3dc849ae6bada1cd11738b29ea.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=043d21b49ab1cb133e693c1bed6f574e/d000baa1cd11728b7785c679dffcc3cec2fd2cc4.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 东軒森">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4e1c\u8ed2\u68ee&quot;,&quot;id&quot;:&quot;tb.1.6ebf89a7.9y6adTDIDCGyGIGXhMJgpg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%B8%9C%E8%BB%92%E6%A3%AE&ie=utf-8&id=tb.1.6ebf89a7.9y6adTDIDCGyGIGXhMJgpg&fr=frs" target="_blank">东軒森</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:16        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969120556,&quot;author_name&quot;:&quot;\u9ed1\u5d0e\u4e0d\u5403\u7cd6&quot;,&quot;author_nickname&quot;:&quot;\u8d85\u5f71\u5929\u624d\u73a9\u5bb6\u00ba&quot;,&quot;author_portrait&quot;:&quot;tb.1.7b489de3.5hvIxJpMr0lQz-gJFVB6lQ&quot;,&quot;first_post_id&quot;:135088532044,&quot;reply_num&quot;:126,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969120556' data-thread-type="0" data-floor='28''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">126</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969120556" title="这么多年了，武装色硬化都是男人在用，女的不能学吗？女生本来身" target="_blank" class="j_th_tit ">这么多年了，武装色硬化都是男人在用，女的不能学吗？女生本来身</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 超影天才玩家º"
          data-field='{&quot;user_id&quot;:2748139035}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9ed1\u5d0e\u4e0d\u5403\u7cd6&quot;,&quot;id&quot;:&quot;tb.1.7b489de3.5hvIxJpMr0lQz-gJFVB6lQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%BB%91%E5%B4%8E%E4%B8%8D%E5%90%83%E7%B3%96&ie=utf-8&id=tb.1.7b489de3.5hvIxJpMr0lQz-gJFVB6lQ&fr=frs" target="_blank">超影天才...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            这么多年了，武装色硬化都是男人在用，女的不能学吗？女生本来身板就脆，学硬化难道不更好吗？还是女生认为黑色太丑不想学 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969120556"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="18129" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=10bf57538c504fc2a20ab807d5edcb28/f5da90529822720e336239a16ccb0a46f31fabef.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=20a1074faf99a9013b355b3e2dae0b7b/d6ca7bcb0a46f21f81988508e1246b600c33ae39.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="35431" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=9782a73f1e23dd542126af6ae1399fe7/cafed539b6003af36616073b222ac65c1138b6ef.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=1f878349584a20a4311e3ccfa0699922/e850352ac65c10380fd21599a5119313b07e8939.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="90096" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=9f65f5beba6eddc426b2bcf909eb9ac4/613bfdfaaf51f3de251e623f83eef01f3b2979ef.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=30d5435f4e82b2b7a79f39cc0196caef/8d5494eef01f3a29bc640e958e25bc315c607c39.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;6&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 醉卧赏明月">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9189\u5367\u8d4f\u660e\u6708&quot;,&quot;id&quot;:&quot;tb.1.86158283.mpa8wwQbdFBw8OHX22L0Cg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%86%89%E5%8D%A7%E8%B5%8F%E6%98%8E%E6%9C%88&ie=utf-8&id=tb.1.86158283.mpa8wwQbdFBw8OHX22L0Cg&fr=frs" target="_blank">醉卧赏明月</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:16        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970658629,&quot;author_name&quot;:&quot;&quot;,&quot;author_nickname&quot;:&quot;\u8d34\u5427\u7528\u6237_5CbbMWA&quot;,&quot;author_portrait&quot;:&quot;tb.1.48103ca7.qQg4TPmeB1tTOaLwUACy4g&quot;,&quot;first_post_id&quot;:135108362104,&quot;reply_num&quot;:3,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970658629' data-thread-type="0" data-floor='29''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">3</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6970658629" title="论恶魔果实为什么那么难吃 ？一个个吃水果不削皮好吃才怪！" target="_blank" class="j_th_tit ">论恶魔果实为什么那么难吃 ？一个个吃水果不削皮好吃才怪！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 贴吧用户_5CbbMWA"
          data-field='{&quot;user_id&quot;:4281981512}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.48103ca7.qQg4TPmeB1tTOaLwUACy4g&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.48103ca7.qQg4TPmeB1tTOaLwUACy4g&fr=frs" target="_blank">贴吧用户_...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10:24</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            论恶魔果实为什么那么难吃 ？一个个吃水果不削皮好吃才怪！
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 哇路飞zwj">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u54c7\u8def\u98dezwj&quot;,&quot;id&quot;:&quot;tb.1.69246af8.T1q_7va1y4v72hzkU6ojfA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%93%87%E8%B7%AF%E9%A3%9Ezwj&ie=utf-8&id=tb.1.69246af8.T1q_7va1y4v72hzkU6ojfA&fr=frs" target="_blank">哇路飞zwj</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:16        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971150592,&quot;author_name&quot;:&quot;gongxiaoping04&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.a0d3445f.H0EMljOjB2CqN1-3euwzlg&quot;,&quot;first_post_id&quot;:135113121308,&quot;reply_num&quot;:29,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971150592' data-thread-type="0" data-floor='30''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">29</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971150592" title="动画组让索隆说了砍大蛇，山治杀凯多，这意味着什么？算是立誓吗" target="_blank" class="j_th_tit ">动画组让索隆说了砍大蛇，山治杀凯多，这意味着什么？算是立誓吗</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: gongxiaoping04"
          data-field='{&quot;user_id&quot;:1478313872}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;gongxiaoping04&quot;,&quot;id&quot;:&quot;tb.1.a0d3445f.H0EMljOjB2CqN1-3euwzlg&quot;}' title="该用户已经连续签到106天了，连续30天一举“橙”名" class="frs-author-name sign_highlight j_user_card " href="/home/main/?un=gongxiaoping04&ie=utf-8&id=tb.1.a0d3445f.H0EMljOjB2CqN1-3euwzlg&fr=frs" target="_blank">gongxiaoping04</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">14:12</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            动画组让索隆说了砍大蛇，山治杀凯多，这意味着什么？算是立誓吗？我还一直以为是路飞和索隆砍凯多，看来动画组比我们要看得明白…… 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971150592"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="4490" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=36ee735d1d55b3199cac8a777399ae1f/54fefd1f4134970aa9632f7382cad1c8a7865d03.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=367cf9b2a38f8c54e3d3c5270a122cf5/241f95cad1c8a786503a75527009c93d70cf505d.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="16861" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=413e694b75d0f703e6e79dde38ca7d04/87a49e510fb30f24898ad35fdf95d143ad4b0303.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=33f1db6cada1cd1105b672288929c9fc/d833c895d143ad4b1a3e799c95025aafa40f065d.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="9635" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=27072258239b033b2cddf4d825fe1aea/7a35367adab44aeddd5e81b8a41c8701a18bfb0c.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=3bb8db2fba4bd11304cdb73a6a94a50f/8ad4b31c8701a18b74fb2d13892f07082838fe5e.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;6&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 韩烨王者😳😳">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5929\u7167\u6657\u6930&quot;,&quot;id&quot;:&quot;tb.1.e068f8a2.aMpO2GI9_-R9m4NBTNx6UQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%A4%A9%E7%85%A7%E6%99%97%E6%A4%B0&ie=utf-8&id=tb.1.e068f8a2.aMpO2GI9_-R9m4NBTNx6UQ&fr=frs" target="_blank">韩烨王者...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:12        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6923896258,&quot;author_name&quot;:&quot;Andjbot\u9f99&quot;,&quot;author_nickname&quot;:&quot;\u4e16\u754c\u738b\u8005\u9882\u5df4\u00ba&quot;,&quot;author_portrait&quot;:&quot;tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&quot;,&quot;first_post_id&quot;:134590019419,&quot;reply_num&quot;:45,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6923896258' data-thread-type="0" data-floor='31''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">45</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6923896258" title="海贼王彩漫深海大监狱篇之毒王麦哲伦出场合集!" target="_blank" class="j_th_tit ">海贼王彩漫深海大监狱篇之毒王麦哲伦出场合集!</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 世界王者颂巴º"
          data-field='{&quot;user_id&quot;:1747699741}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Andjbot\u9f99&quot;,&quot;id&quot;:&quot;tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&quot;}' title="该用户已经连续签到36天了，连续30天一举“橙”名" class="frs-author-name sign_highlight j_user_card " href="/home/main/?un=Andjbot%E9%BE%99&ie=utf-8&id=tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&fr=frs" target="_blank">世界王者...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-3</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            这里面还加了老沙女帝希留黑胡子汉尼拔等人，话说老沙自从大监狱篇开始就越来越强了，不管是智商还是战斗力都是一流的，还有希留据说他有着和麦哲伦平分秋色的实力，真要是这样那他真的太危险了再加上现在还吃了透明果实真不知道会强到什么地步! ! ! 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6923896258"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="55237" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=0216467aae12c8fcb4a6fecfcc33be7c/a8ca36d12f2eb938ebcd4ea8c2628535e4dd6ff1.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=99cd3440d15c1038247ececa822a9213/4ec2d5628535e5dd978c918561c6a7efcf1b62c3.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 世界王者颂巴º">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Andjbot\u9f99&quot;,&quot;id&quot;:&quot;tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Andjbot%E9%BE%99&ie=utf-8&id=tb.1.dbf43de1.4-3dMMtXHMUkGN0PmJGh9Q&fr=frs" target="_blank">世界王者...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:15        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6965969039,&quot;author_name&quot;:&quot;\u6731\u745e\u5b8f\u7684\u6625\u5929&quot;,&quot;author_nickname&quot;:&quot;RK\u5927\u9b54\u738b\ud83d\ude33&quot;,&quot;author_portrait&quot;:&quot;tb.1.d34fdcc4.g5JKbh7Q8Se8hcdlB4-wUw&quot;,&quot;first_post_id&quot;:135050778458,&quot;reply_num&quot;:40,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6965969039' data-thread-type="0" data-floor='32''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">40</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6965969039" title="奥哈拉：35岁赤犬+30岁青雉司法岛：大将青雉第一次逮捕巴雷" target="_blank" class="j_th_tit ">奥哈拉：35岁赤犬+30岁青雉司法岛：大将青雉第一次逮捕巴雷</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: RK大魔王😳"
          data-field='{&quot;user_id&quot;:3905341380}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6731\u745e\u5b8f\u7684\u6625\u5929&quot;,&quot;id&quot;:&quot;tb.1.d34fdcc4.g5JKbh7Q8Se8hcdlB4-wUw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%9C%B1%E7%91%9E%E5%AE%8F%E7%9A%84%E6%98%A5%E5%A4%A9&ie=utf-8&id=tb.1.d34fdcc4.g5JKbh7Q8Se8hcdlB4-wUw&fr=frs" target="_blank">RK大魔王<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-24.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            奥哈拉：35岁赤犬+30岁青雉 司法岛：大将青雉 第一次逮捕巴雷特：卡普+战国 第二次揍巴雷特：黄猿+藤虎 揍世界破坏王：元帅赤犬 辅助战力：五中将+十少将+50准将+200本部上校（大左）。感觉一个屠魔令战力为1，则四皇团也就1.5左右。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6965969039"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="92038" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=1f0a1362a4de9c82a630f18d5cb1ac33/157d352ac65c1038de113999a5119313b07e8928.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=84a552398f22720e7bcee2f24bf00b46/faf2b2119313b07e47d2a7531bd7912397dd8c7a.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 番茄零式">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u756a\u8304\u96f6\u5f0f&quot;,&quot;id&quot;:&quot;tb.1.cce3f30c.8yFEL280WVhymtH4saVs4w&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%95%AA%E8%8C%84%E9%9B%B6%E5%BC%8F&ie=utf-8&id=tb.1.cce3f30c.8yFEL280WVhymtH4saVs4w&fr=frs" target="_blank">番茄零式</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:15        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6927340765,&quot;author_name&quot;:&quot;Red__\u82cd\u7a79&quot;,&quot;author_nickname&quot;:&quot;\u96f6\u96f6lyc\ud83d\udc3c&quot;,&quot;author_portrait&quot;:&quot;tb.1.4e25aabe.UW5huakFBXxCmcPRkCcosQ&quot;,&quot;first_post_id&quot;:134631223451,&quot;reply_num&quot;:81,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6927340765' data-thread-type="0" data-floor='33''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">81</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6927340765" title="提问:索隆会不会再次用九刀流" target="_blank" class="j_th_tit ">提问:索隆会不会再次用九刀流</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 零零lyc🐼"
          data-field='{&quot;user_id&quot;:2565065350}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Red__\u82cd\u7a79&quot;,&quot;id&quot;:&quot;tb.1.4e25aabe.UW5huakFBXxCmcPRkCcosQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Red__%E8%8B%8D%E7%A9%B9&ie=utf-8&id=tb.1.4e25aabe.UW5huakFBXxCmcPRkCcosQ&fr=frs" target="_blank">零零lyc<img src="//tb1.bdstatic.com/tb/cms/nickemoji/2-7.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -4800px  0;top:0px;left:0px" data-slot="1"  data-name="signprize" data-field='{&quot;name&quot;:&quot;signprize&quot;,&quot;end_time&quot;:&quot;1600790400&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u521d\u7ea7\u6838\u5fc3\u7528\u6237&quot;,&quot;intro&quot;:&quot;\u624b\u673a\u7aef\u8fde\u7eed\u7b7e\u52307\u5929\u53ef\u83b7\u5f97\u672c\u5370\u8bb0&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/mo\/q\/medal&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;3&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,94&quot;,&quot;2&quot;:&quot;1599647089,95&quot;,&quot;3&quot;:&quot;1599647089,96&quot;}}' target="_blank"   href="http://tieba.baidu.com/mo/q/medal"  class="j_icon_slot"  title="初级核心用户"  locate="signprize_3#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-5</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            和之国一战，草帽一伙每个人肯定会使出自己的全部实力，那么索隆会不会再次使出很久没有用过的九刀流呢 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6927340765"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="30717" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=6e93a760274e251fe2a2ecfa97b6e52e/a5afb2b7d0a20cf41e0afb8561094b36adaf99fb.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=35eb6165cef9d72a17641015e4112934/caef76094b36acaf017a93a66bd98d1000e99cd5.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            17:50        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6966342487,&quot;author_name&quot;:&quot;\u6c11\u9662\u5fc3\u91cc\u8bdd&quot;,&quot;author_nickname&quot;:&quot;\u677f\u84dd\u6839\ud83c\udf34\u677f\u62e6\u6839&quot;,&quot;author_portrait&quot;:&quot;tb.1.99f9a5bc.tSy4Qa72y3ypi9iHrxI6Nw&quot;,&quot;first_post_id&quot;:135055709502,&quot;reply_num&quot;:21,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6966342487' data-thread-type="0" data-floor='34''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">21</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6966342487" title="暗示罗自小父母双亡" target="_blank" class="j_th_tit ">暗示罗自小父母双亡</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 板蓝根🌴板拦根"
          data-field='{&quot;user_id&quot;:1604400638}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6c11\u9662\u5fc3\u91cc\u8bdd&quot;,&quot;id&quot;:&quot;tb.1.99f9a5bc.tSy4Qa72y3ypi9iHrxI6Nw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%B0%91%E9%99%A2%E5%BF%83%E9%87%8C%E8%AF%9D&ie=utf-8&id=tb.1.99f9a5bc.tSy4Qa72y3ypi9iHrxI6Nw&fr=frs" target="_blank">板蓝根<img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-10.png" class="nicknameEmoji" style="width:13px;height:13px"/>...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-19</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            暗示罗自小父母双亡
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6966342487"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="2272" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=559a9428ecf2b211e47b8d4cfab04901/1509b899a9014c082ba4dafe1d7b02087af4f4f8.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=3c93cd3ea419ebc4c0787691b21dcefc/1c950a7b02087bf44f73a5b2e5d3572c10dfcfca.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 不可食用♬">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;kattoKID1412&quot;,&quot;id&quot;:&quot;tb.1.aeb35b2a.DxLhC_h2bMYZ_bEK52-FfA&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=kattoKID1412&ie=utf-8&id=tb.1.aeb35b2a.DxLhC_h2bMYZ_bEK52-FfA&fr=frs" target="_blank">不可食用<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-10.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:15        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971371403,&quot;author_name&quot;:&quot;Miss\u9f99\u7fbd\u51e1&quot;,&quot;author_nickname&quot;:&quot;\u72d0\u4e0d\u5f52\ud83d\udca4&quot;,&quot;author_portrait&quot;:&quot;tb.1.36aa6681.IukIix0-o1qWhnvDvfecgQ&quot;,&quot;first_post_id&quot;:135115080467,&quot;reply_num&quot;:11,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971371403' data-thread-type="0" data-floor='35''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">11</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971371403" title="为什么我看除了海吧外的很多地方都是对红狗咬牙切齿啊 就我一个" target="_blank" class="j_th_tit ">为什么我看除了海吧外的很多地方都是对红狗咬牙切齿啊 就我一个</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 狐不归💤"
          data-field='{&quot;user_id&quot;:1262786158}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;Miss\u9f99\u7fbd\u51e1&quot;,&quot;id&quot;:&quot;tb.1.36aa6681.IukIix0-o1qWhnvDvfecgQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=Miss%E9%BE%99%E7%BE%BD%E5%87%A1&ie=utf-8&id=tb.1.36aa6681.IukIix0-o1qWhnvDvfecgQ&fr=frs" target="_blank">狐不归<img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-34.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -1100px  0;top:0px;left:0px" data-slot="1"  data-name="chunv" data-field='{&quot;name&quot;:&quot;chunv&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u5904\u5973\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,22&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="处女座印记"  locate="chunv_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">15:42</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            为什么我看除了海吧外的很多地方都是对红狗咬牙切齿啊 就我一个人感觉红狗其实还不错吗？
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 混吃等死咸鱼👻">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u96f7\u4fca\u6770smile&quot;,&quot;id&quot;:&quot;tb.1.8d60e3b0.BLubz_siQf88Zlpy9TNVnw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%9B%B7%E4%BF%8A%E6%9D%B0smile&ie=utf-8&id=tb.1.8d60e3b0.BLubz_siQf88Zlpy9TNVnw&fr=frs" target="_blank">混吃等死...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:15        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971485262,&quot;author_name&quot;:&quot;\u6211\u5c31\u662f\u5c06\u5439&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.52175e6a._aMJNG_B_YnQ63JHZ7hLXA&quot;,&quot;first_post_id&quot;:135116153724,&quot;reply_num&quot;:24,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971485262' data-thread-type="0" data-floor='36''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">24</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971485262" title="理性分析：大和如果上船了，三大主力会变成四大主力吗？大和的实" target="_blank" class="j_th_tit ">理性分析：大和如果上船了，三大主力会变成四大主力吗？大和的实</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 我就是将吹"
          data-field='{&quot;user_id&quot;:3398597277}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6211\u5c31\u662f\u5c06\u5439&quot;,&quot;id&quot;:&quot;tb.1.52175e6a._aMJNG_B_YnQ63JHZ7hLXA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%88%91%E5%B0%B1%E6%98%AF%E5%B0%86%E5%90%B9&ie=utf-8&id=tb.1.52175e6a._aMJNG_B_YnQ63JHZ7hLXA&fr=frs" target="_blank">我就是将吹</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">16:31</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            理性分析：大和如果上船了，三大主力会变成四大主力吗？大和的实力可以跟得上索隆、山治、甚平吗？
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971485262"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="59685" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=c0bce97d87ef76c6d087f329ad26d1c3/87e60a46f21fbe094e02f8487c600c338744ad3f.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=38f4041715087bf47dec57e1c2e8562c/f7246b600c338744ce991420460fd9f9d72aa009.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 贴吧用户_5CP3SSe">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.a31894a0.OcNpGMc4xKsVHua6cwbQwA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.a31894a0.OcNpGMc4xKsVHua6cwbQwA&fr=frs" target="_blank">贴吧用户_...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:09        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971632577,&quot;author_name&quot;:&quot;\u9999\u514b\u65af\u8def\u98de\u9f99&quot;,&quot;author_nickname&quot;:&quot;\u7b14\u8005\u5854\u7384-&quot;,&quot;author_portrait&quot;:&quot;tb.1.8ff8ce2c.EM0ly88wYevbgLKQwS1fQw&quot;,&quot;first_post_id&quot;:135117584164,&quot;reply_num&quot;:2,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971632577' data-thread-type="0" data-floor='37''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">2</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971632577" title="我不小心把自己破防了。" target="_blank" class="j_th_tit ">我不小心把自己破防了。</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 笔者塔玄-"
          data-field='{&quot;user_id&quot;:713483748}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9999\u514b\u65af\u8def\u98de\u9f99&quot;,&quot;id&quot;:&quot;tb.1.8ff8ce2c.EM0ly88wYevbgLKQwS1fQw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%A6%99%E5%85%8B%E6%96%AF%E8%B7%AF%E9%A3%9E%E9%BE%99&ie=utf-8&id=tb.1.8ff8ce2c.EM0ly88wYevbgLKQwS1fQw&fr=frs" target="_blank">笔者塔玄<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/></a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">17:38</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            我不小心把自己破防了。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971632577"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="70239" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=8f56aacdda11728b30788420f8cceff7/dd12b80e7bec54e768873f42ae389b504fc26a34.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=e8562a9f2d87e9504217f36420035243/2e2eb9389b504fc28b349559f2dde71190ef6d06.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 笔者塔玄-">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9999\u514b\u65af\u8def\u98de\u9f99&quot;,&quot;id&quot;:&quot;tb.1.8ff8ce2c.EM0ly88wYevbgLKQwS1fQw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%A6%99%E5%85%8B%E6%96%AF%E8%B7%AF%E9%A3%9E%E9%BE%99&ie=utf-8&id=tb.1.8ff8ce2c.EM0ly88wYevbgLKQwS1fQw&fr=frs" target="_blank">笔者塔玄<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:14        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970319204,&quot;author_name&quot;:&quot;&quot;,&quot;author_nickname&quot;:&quot;\u8d34\u5427\u7528\u6237_7UR5QAA&quot;,&quot;author_portrait&quot;:&quot;tb.1.825c9777.kK8Nl3W43KSyn_nmBR5JBg&quot;,&quot;first_post_id&quot;:135104636486,&quot;reply_num&quot;:10,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970319204' data-thread-type="0" data-floor='38''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">10</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6970319204" title="路飞的血液、骨头、肌肉是不同的概念，2档血液加速、3档骨气球" target="_blank" class="j_th_tit ">路飞的血液、骨头、肌肉是不同的概念，2档血液加速、3档骨气球</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 贴吧用户_7UR5QAA"
          data-field='{&quot;user_id&quot;:2557576456}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.825c9777.kK8Nl3W43KSyn_nmBR5JBg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.825c9777.kK8Nl3W43KSyn_nmBR5JBg&fr=frs" target="_blank">贴吧用户_...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">06:13</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            路飞的血液、骨头、肌肉是不同的概念，2档血液加速、3档骨气球、4档肌肉气球也是不同的原理。蛇人其实是4档+2档的半成品，是为了击败卡二临时开发的，减少了肌肉气球份量并引入2档原理。同样是大蛇炮，弹力人以橡胶为前缀，蛇人则是JET。 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6970319204"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="72717" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=53f7437a7a224f4a57cc7b1139c7bc6b/a682a40f4bfbfbed4a6803236ff0f736afc31f62.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=3784d4539094a4c20a23e7233ecf1ad5/024f78f0f736afc3983d0a39a419ebc4b74512bc.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="39935" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=ed405163cef9d72a1731181fe41a040d/8fa0a9773912b31b475df8759118367adab4e163.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=8c859e3d18b30f24359aec0bf8aed043/f9198618367adab4bde12e1f9cd4b31c8701e4bd.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            17:49        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6955711687,&quot;author_name&quot;:&quot;\u9633\u5149\u7684yangok&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.f2d09e9f.3M4rUICtnP-VyFa8zXZgYw&quot;,&quot;first_post_id&quot;:134952738408,&quot;reply_num&quot;:5,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6955711687' data-thread-type="0" data-floor='39''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">5</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6955711687" title="有没有可能山治小时候基因改造当时是失败的，后来觉醒了，虽然没" target="_blank" class="j_th_tit ">有没有可能山治小时候基因改造当时是失败的，后来觉醒了，虽然没</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 阳光的yangok"
          data-field='{&quot;user_id&quot;:1198765412}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u9633\u5149\u7684yangok&quot;,&quot;id&quot;:&quot;tb.1.f2d09e9f.3M4rUICtnP-VyFa8zXZgYw&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E9%98%B3%E5%85%89%E7%9A%84yangok&ie=utf-8&id=tb.1.f2d09e9f.3M4rUICtnP-VyFa8zXZgYw&fr=frs" target="_blank">阳光的yangok</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-18</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            有没有可能山治小时候基因改造当时是失败的，后来觉醒了，虽然没有钢铁的皮肤，但似乎和他的兄弟们一样有一些特殊能力，恶魔果实遗传因子获得的力量，火焰。两年前恶魔风脚是看出来高速旋转出来的，两年后要说火焰的话，参考路飞的火拳统，是武装色硬化的状态下高速摩擦空气产生的火焰攻击对手，而山治并没有在硬化的状态下可以提出火焰，所以我认为可能当时改造并没有失败，只是觉醒的比较慢而已。不喜勿喷，谢谢！
        </div>

                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 可爱娇声">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u53ef\u7231\u5a07\u58f0&quot;,&quot;id&quot;:&quot;tb.1.6bbddf88.qvjxuB-qc59Qjsu4vaivCQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%8F%AF%E7%88%B1%E5%A8%87%E5%A3%B0&ie=utf-8&id=tb.1.6bbddf88.qvjxuB-qc59Qjsu4vaivCQ&fr=frs" target="_blank">可爱娇声</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            17:49        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6950261780,&quot;author_name&quot;:&quot;\u6c38\u8fdc\u7684\u4e54\u4e3923&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.6635e8be.ZxFqfQUGwkIkXMUVHOSbGg&quot;,&quot;first_post_id&quot;:134892030483,&quot;reply_num&quot;:213,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6950261780' data-thread-type="0" data-floor='40''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">213</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6950261780" title="海贼王完结时赏金预测！" target="_blank" class="j_th_tit ">海贼王完结时赏金预测！</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 永远的乔丹23"
          data-field='{&quot;user_id&quot;:40594832}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6c38\u8fdc\u7684\u4e54\u4e3923&quot;,&quot;id&quot;:&quot;tb.1.6635e8be.ZxFqfQUGwkIkXMUVHOSbGg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%B0%B8%E8%BF%9C%E7%9A%84%E4%B9%94%E4%B8%B923&ie=utf-8&id=tb.1.6635e8be.ZxFqfQUGwkIkXMUVHOSbGg&fr=frs" target="_blank">永远的乔...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-15</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
             1.路飞：56亿贝里 2.索隆：35亿贝里 3.山治：30亿贝里 4.甚平：28亿3千9百万贝里 5.大和：25亿贝里 6.乌索普：12亿 7.罗宾：9亿3千万 8.弗兰奇：8亿9千4百万 9.布鲁克：8亿8千3百万 10.娜美：7亿6千6百万 11.乔巴：3亿
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6950261780"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="82530" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=7edf0162de3d70cf4cafa20fc8ecfd39/50822edda3cc7cd98cf167822e01213fb90e91be.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=357a65504cb5c9ea62f303ebe502b700/00e93901213fb80e7a0d328c21d12f2eb8389488.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="20818" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=e26ac6871ffa513d51ff64dc0d5d79c2/be8ad933c895d143deaeb77864f082025baf07ba.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=016e217bae12c8fcb4f3f6c5cc389045/d01373f082025aafd7ea2d90ecedab64024f1a94.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="55637" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=787d6c1015087bf47db95febc2e37b15/c5f6b6fd5266d0166ccccd73802bd40734fa3545.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=f022b7a3b086c91708035231f90672cf/aa18972bd40735fa83251de289510fb30e240897.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;11&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 幻影绝瑟">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u5e7b\u5f71\u7edd\u745f&quot;,&quot;id&quot;:&quot;tb.1.a0dd2454.oSguV7hIuXolA7QVBMgpWg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E5%B9%BB%E5%BD%B1%E7%BB%9D%E7%91%9F&ie=utf-8&id=tb.1.a0dd2454.oSguV7hIuXolA7QVBMgpWg&fr=frs" target="_blank">幻影绝瑟</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:09        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971107858,&quot;author_name&quot;:&quot;chongzi517&quot;,&quot;author_nickname&quot;:&quot;\ud83c\udf39\u963f\u5f25\u9640\u4f5b&quot;,&quot;author_portrait&quot;:&quot;tb.1.f7aa10be.WXnsrXoD10KR2yrTNjmMCA&quot;,&quot;first_post_id&quot;:135112729522,&quot;reply_num&quot;:4,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971107858' data-thread-type="0" data-floor='41''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">4</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971107858" title="卡普联手罗杰对抗洛克斯海贼团，德雷克联手未来海贼王路飞对抗复" target="_blank" class="j_th_tit ">卡普联手罗杰对抗洛克斯海贼团，德雷克联手未来海贼王路飞对抗复</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 🌹阿弥陀佛"
          data-field='{&quot;user_id&quot;:459134648}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;chongzi517&quot;,&quot;id&quot;:&quot;tb.1.f7aa10be.WXnsrXoD10KR2yrTNjmMCA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=chongzi517&ie=utf-8&id=tb.1.f7aa10be.WXnsrXoD10KR2yrTNjmMCA&fr=frs" target="_blank"><img src="//tb1.bdstatic.com/tb/cms/nickemoji/3-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>阿弥陀佛</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">13:54</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            卡普联手罗杰对抗洛克斯海贼团，德雷克联手未来海贼王路飞对抗复活的洛克斯联盟，德雷克回到海军就算得到海军英雄称号也没啥大惊小怪的 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971107858"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="8836" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=68e42c7382cad1c8d0eef4254f0e4b30/2c8f0cf431adcbef2ea3425abbaf2edda2cc9f80.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=8153de467759252da3171d0c04a0023b/4a36acaf2edda3cc2473847c16e93901203f92d2.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 仙一样的男人💤">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;QQ1025986867&quot;,&quot;id&quot;:&quot;tb.1.325f697f.2BSffTACEGIwSYYP6YjYSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=QQ1025986867&ie=utf-8&id=tb.1.325f697f.2BSffTACEGIwSYYP6YjYSA&fr=frs" target="_blank">仙一样的...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            17:18        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969514023,&quot;author_name&quot;:&quot;\u8349\u5e3dboy\u8def\u98deop&quot;,&quot;author_nickname&quot;:&quot;\u88ab\u9009\u53ec\u7684\u5b69\u5b50\ud83d\udc96&quot;,&quot;author_portrait&quot;:&quot;tb.1.f65c27ab.LsinrJvyfbmOhejWl8bHpQ&quot;,&quot;first_post_id&quot;:135093082260,&quot;reply_num&quot;:59,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969514023' data-thread-type="0" data-floor='42''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">59</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969514023" title="震震果实：伤害：对建筑ex 对人b-岩浆果实：伤害：对建筑a" target="_blank" class="j_th_tit ">震震果实：伤害：对建筑ex 对人b-岩浆果实：伤害：对建筑a</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 被选召的孩子💖"
          data-field='{&quot;user_id&quot;:2081040316}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8349\u5e3dboy\u8def\u98deop&quot;,&quot;id&quot;:&quot;tb.1.f65c27ab.LsinrJvyfbmOhejWl8bHpQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%8D%89%E5%B8%BDboy%E8%B7%AF%E9%A3%9Eop&ie=utf-8&id=tb.1.f65c27ab.LsinrJvyfbmOhejWl8bHpQ&fr=frs" target="_blank">被选召的...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,76&quot;,&quot;2&quot;:&quot;1599647089,77&quot;,&quot;3&quot;:&quot;1599647089,78&quot;,&quot;4&quot;:&quot;1599647089,79&quot;,&quot;5&quot;:&quot;1599647089,80&quot;,&quot;6&quot;:&quot;1599647089,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            震震果实：伤害：对建筑ex 对人b- 岩浆果实：伤害：对建筑a 对人ex 不吹不黑，是不是这个道理，吧友们 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969514023"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="24320" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=01001fafa04543a9f54ef2ce2e27a6bb/6b27304e251f95ca63d153edde177f3e67095277.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=3e4d6085e71f3a295ac8d5c6a91ebd31/a686c9177f3e67097b2484a42cc79f3df8dc5541.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="28543" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=b43afd9c87529822056631c1e7fa57f2/ff6278f0f736afc38b28fe3ea419ebc4b7451277.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=2002fa9f0cd5ad6eaaf964e2b1f038db/0b55b319ebc4b745b1b0764dd8fc1e178a821541.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 木基哇啦😁">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;24K\u7eaf\u5e05\u7684\u5e86\u54e5&quot;,&quot;id&quot;:&quot;tb.1.26dd6096.4vQo7cQf5tVFev6qU6ps4w&quot;}' class="frs-author-name j_user_card  vip_red " href="/home/main/?un=24K%E7%BA%AF%E5%B8%85%E7%9A%84%E5%BA%86%E5%93%A5&ie=utf-8&id=tb.1.26dd6096.4vQo7cQf5tVFev6qU6ps4w&fr=frs" target="_blank">木基哇啦<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-25.png" class="nicknameEmoji" style="width:13px;height:13px"/></a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:13        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6949219378,&quot;author_name&quot;:&quot;\u706d\u840c\u9b54\u5bfc\u58eb&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.78fb11c6.g65oqPcvyeKNPlSO1Ti6GQ&quot;,&quot;first_post_id&quot;:134882141010,&quot;reply_num&quot;:1284,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6949219378' data-thread-type="0" data-floor='43''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">1284</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6949219378" title="不懂就问，把男朋友的论文资料全删了，" target="_blank" class="j_th_tit ">不懂就问，把男朋友的论文资料全删了，</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 灭萌魔导士"
          data-field='{&quot;user_id&quot;:300352354}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u706d\u840c\u9b54\u5bfc\u58eb&quot;,&quot;id&quot;:&quot;tb.1.78fb11c6.g65oqPcvyeKNPlSO1Ti6GQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%81%AD%E8%90%8C%E9%AD%94%E5%AF%BC%E5%A3%AB&ie=utf-8&id=tb.1.78fb11c6.g65oqPcvyeKNPlSO1Ti6GQ&fr=frs" target="_blank">灭萌魔导士</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-15</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            这事儿跟删游戏存档一样严重吗？ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6949219378"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="39655" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=3cc5376d0a950a7b756046c63ae14ee0/adf781cb39dbb6fd22ab897d1e24ab18962b37a2.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=40837c7482cad1c8d0bbfc2f4f056609/d1160924ab18972ba4ca6c91f1cd7b899f510afc.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="43680" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=64d1e7627c63f6241c083101b774c7c1/bf848226cffc1e171c4ce06a5d90f603728de9ac.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=c4a8897d1e24ab18e016e13f05c1e7cd/b8014a90f603738d3fb96079a41bb051f919ecfe.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="35725" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=fcc1d07f7a224f4a57cc7b1139c7bc6b/a682a40f4bfbfbede55e90266ff0f736afc31f15.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=98b247569094a4c20a23e7233ecf1ad5/024f78f0f736afc3370b993ca419ebc4b7451267.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 子真子平丶♬">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6234\u963f\u946b\u4e36&quot;,&quot;id&quot;:&quot;tb.1.acb62484.AlLJPzLUzzvZBIYzi9-uQA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%88%B4%E9%98%BF%E9%91%AB%E4%B8%B6&ie=utf-8&id=tb.1.acb62484.AlLJPzLUzzvZBIYzi9-uQA&fr=frs" target="_blank">子真子平...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:13        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970731921,&quot;author_name&quot;:&quot;\u4e5d\u54c8\u56e2\u56e2&quot;,&quot;author_nickname&quot;:&quot;\u756a\u8304\u8638\u756a\u8304\u9171\ud83d\ude31&quot;,&quot;author_portrait&quot;:&quot;tb.1.3e0a4372.aE_CNBS9poIPBww-k-H8AA&quot;,&quot;first_post_id&quot;:135108960973,&quot;reply_num&quot;:6,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970731921' data-thread-type="0" data-floor='44''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">6</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6970731921" title="今天思考诺亚和冥王是不是有关系的时候，突然反应过来，预言“路" target="_blank" class="j_th_tit ">今天思考诺亚和冥王是不是有关系的时候，突然反应过来，预言“路</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 番茄蘸番茄酱😱"
          data-field='{&quot;user_id&quot;:3183424038}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u4e5d\u54c8\u56e2\u56e2&quot;,&quot;id&quot;:&quot;tb.1.3e0a4372.aE_CNBS9poIPBww-k-H8AA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E4%B9%9D%E5%93%88%E5%9B%A2%E5%9B%A2&ie=utf-8&id=tb.1.3e0a4372.aE_CNBS9poIPBww-k-H8AA&fr=frs" target="_blank">番茄蘸番...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">10:51</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            今天思考诺亚和冥王是不是有关系的时候，突然反应过来，预言“路飞毁灭鱼人岛”是已定事实的话，方舟诺亚作为曾经为了把鱼人们转移到陆地上去的工具，是不是就是为此而继续存在的？ 路飞在最终之战中毁灭了鱼人岛，然后鱼人们搭乘有半个鱼人岛大小的诺亚来到陆上，实现乙姬王妃的梦想，大概是这个走向？ 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6970731921"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="40318" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=dc1f7972c51b0ef46cbd905cedf47de3/8aeba7efce1b9d168527ab3de4deb48f8d5464b3.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=740a954f80dda144da096cba828cd1a2/ae51f3deb48f8c54ec33f4732d292df5e1fe7f8d.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 真波鲁萨利诺✨">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.abcbae59._pY8thfdr_G8wXqvUHimSA&fr=frs" target="_blank">真波鲁萨...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            17:37        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6970067504,&quot;author_name&quot;:&quot;\u7d22\u9686\u7684\u960e\u9b54&quot;,&quot;author_nickname&quot;:&quot;\u5b87\u667a\u6ce2\u7f8e\u7434\ud83d\udd2f&quot;,&quot;author_portrait&quot;:&quot;tb.1.3c14cb7.mTqFJ0eH0PT7Gr9Mr8a9EA&quot;,&quot;first_post_id&quot;:135100587538,&quot;reply_num&quot;:51,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6970067504' data-thread-type="0" data-floor='45''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">51</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6970067504" title="不懂就问，海贼王哪句台词可以追女孩子" target="_blank" class="j_th_tit ">不懂就问，海贼王哪句台词可以追女孩子</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 宇智波美琴🔯"
          data-field='{&quot;user_id&quot;:4190467370}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u7d22\u9686\u7684\u960e\u9b54&quot;,&quot;id&quot;:&quot;tb.1.3c14cb7.mTqFJ0eH0PT7Gr9Mr8a9EA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%B4%A2%E9%9A%86%E7%9A%84%E9%98%8E%E9%AD%94&ie=utf-8&id=tb.1.3c14cb7.mTqFJ0eH0PT7Gr9Mr8a9EA&fr=frs" target="_blank">宇智波美...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/102_14.png?stamp=1599647089) no-repeat -1000px  0;top:0px;left:0px" data-slot="1"  data-name="juxie" data-field='{&quot;name&quot;:&quot;juxie&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:102,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u5de8\u87f9\u5ea7\u5370\u8bb0&quot;,&quot;intro&quot;:&quot;\u83b7\u53d6\u89c4\u5219\uff1a\u5728\u661f\u5ea7\u52cb\u7ae0\u9986\u4e2d\u83b7\u5f97\u3002&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,20&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?ie=utf-8&amp;kw=%E8%9B%87%E5%A4%AB%E5%BA%A7&amp;fr=search"  class="j_icon_slot"  title="巨蟹座印记"  locate="juxie_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">00:04</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            不懂就问，海贼王哪句台词可以追女孩子 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6970067504"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="70774" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=1120e627460fd9f9a0425d6b151df813/0a2e738da977391249c34c3aef198618377ae2b7.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=1c1587e289510fb37819779fe908c995/b151f8198618367a206cb68639738bd4b21ce581.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 贴吧用户_5CP3SSe">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;&quot;,&quot;id&quot;:&quot;tb.1.a31894a0.OcNpGMc4xKsVHua6cwbQwA&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=&ie=utf-8&id=tb.1.a31894a0.OcNpGMc4xKsVHua6cwbQwA&fr=frs" target="_blank">贴吧用户_...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:13        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6969657938,&quot;author_name&quot;:&quot;\u6b66\u5eb7\u4e0d\u55ef&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.d6c85c98.Y-E5j4_tzp_ShG7H07HTyg&quot;,&quot;first_post_id&quot;:135094983878,&quot;reply_num&quot;:31,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6969657938' data-thread-type="0" data-floor='46''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">31</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6969657938" title="虽然说是剧场版，山治可以挡下路奇确实强了很多" target="_blank" class="j_th_tit ">虽然说是剧场版，山治可以挡下路奇确实强了很多</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 武康不嗯"
          data-field='{&quot;user_id&quot;:965074797}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u6b66\u5eb7\u4e0d\u55ef&quot;,&quot;id&quot;:&quot;tb.1.d6c85c98.Y-E5j4_tzp_ShG7H07HTyg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E6%AD%A6%E5%BA%B7%E4%B8%8D%E5%97%AF&ie=utf-8&id=tb.1.d6c85c98.Y-E5j4_tzp_ShG7H07HTyg&fr=frs" target="_blank">武康不嗯</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -3800px  0;top:0px;left:0px" data-slot="1"  data-name="starmaster" data-field='{&quot;name&quot;:&quot;starmaster&quot;,&quot;end_time&quot;:&quot;1735660800&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u624b\u6e380\u661f\u8fbe\u4eba&quot;,&quot;intro&quot;:&quot;\u5728\u624b\u6e38\u73a9\u5bb6\u5427\u6210\u4e3a\u624b\u6e380\u661f\u8fbe\u4eba\u8ba4\u8bc1\u7528\u6237\uff0c\u5373\u53ef\u83b7\u53d6\u54e6~&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/f?kw=\u73a9\u5bb6\u8ba4\u8bc1&amp;ie=utf-8&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,76&quot;,&quot;2&quot;:&quot;1599647089,77&quot;,&quot;3&quot;:&quot;1599647089,78&quot;,&quot;4&quot;:&quot;1599647089,79&quot;,&quot;5&quot;:&quot;1599647089,80&quot;,&quot;6&quot;:&quot;1599647089,81&quot;}}' target="_blank"   href="http://tieba.baidu.com/f?kw=玩家认证&amp;ie=utf-8"  class="j_icon_slot"  title="手游0星达人"  locate="starmaster_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">9-20</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            虽然说是剧场版，山治可以挡下路奇确实强了很多 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6969657938"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="74702" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=65eba8b49ab1cb133e3c3411ed647a77/a798c9ea15ce36d3847a406b2df33a87e950b119.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=6c2ea390a5fb43161a1f7a72109f4723/b7003af33a87e9506469303707385343fbf2b46b.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: zz不可不见">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;zz\u4e0d\u53ef\u4e0d\u89c1&quot;,&quot;id&quot;:&quot;tb.1.4fba27ce.JtHuEePx-WNyNBz9YhcEhg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=zz%E4%B8%8D%E5%8F%AF%E4%B8%8D%E8%A7%81&ie=utf-8&id=tb.1.4fba27ce.JtHuEePx-WNyNBz9YhcEhg&fr=frs" target="_blank">zz不可不见</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:12        </span>
</div>
                </div>
                                </div>
    </div>
</li>
<li class=" j_thread_list clearfix" data-field='{&quot;id&quot;:6971422634,&quot;author_name&quot;:&quot;\u767d\u730e\u4eba\u65af\u6469\u683c&quot;,&quot;author_nickname&quot;:null,&quot;author_portrait&quot;:&quot;tb.1.23d6b345.GFVz_K_f4jDepRR6j0LeZg&quot;,&quot;first_post_id&quot;:135115569452,&quot;reply_num&quot;:18,&quot;is_bakan&quot;:null,&quot;vid&quot;:&quot;&quot;,&quot;is_good&quot;:null,&quot;is_top&quot;:null,&quot;is_protal&quot;:null,&quot;is_membertop&quot;:null,&quot;is_multi_forum&quot;:null,&quot;frs_tpoint&quot;:null}'  data-tid='6971422634' data-thread-type="0" data-floor='47''>
            <div class="t_con cleafix">
                            <div class="col2_left j_threadlist_li_left">
                                     
                            <span class="threadlist_rep_num center_text"
                                title="回复">18</span>
                                                </div>
                <div class="col2_right j_threadlist_li_right ">
            <div class="threadlist_lz clearfix">
                <div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/6971422634" title="总有人黑偷袭，但是没实力凭什么偷袭?" target="_blank" class="j_th_tit ">总有人黑偷袭，但是没实力凭什么偷袭?</a>
</div><div class="threadlist_author pull_right">
    <span class="tb_icon_author "
          title="主题作者: 白猎人斯摩格"
          data-field='{&quot;user_id&quot;:25189038}' ><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u767d\u730e\u4eba\u65af\u6469\u683c&quot;,&quot;id&quot;:&quot;tb.1.23d6b345.GFVz_K_f4jDepRR6j0LeZg&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E7%99%BD%E7%8C%8E%E4%BA%BA%E6%96%AF%E6%91%A9%E6%A0%BC&ie=utf-8&id=tb.1.23d6b345.GFVz_K_f4jDepRR6j0LeZg&fr=frs" target="_blank">白猎人斯...</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "><a style="background: url(//tb1.bdstatic.com/tb/cms/com/icon/104_14.png?stamp=1599647089) no-repeat -4700px  0;top:0px;left:0px" data-slot="1"  data-name="signprize" data-field='{&quot;name&quot;:&quot;signprize&quot;,&quot;end_time&quot;:&quot;1600790400&quot;,&quot;category_id&quot;:104,&quot;slot_no&quot;:&quot;1&quot;,&quot;title&quot;:&quot;\u521d\u7ea7\u6838\u5fc3\u7528\u6237&quot;,&quot;intro&quot;:&quot;\u624b\u673a\u7aef\u8fde\u7eed\u7b7e\u52307\u5929\u53ef\u83b7\u5f97\u672c\u5370\u8bb0&quot;,&quot;intro_url&quot;:&quot;http:\/\/tieba.baidu.com\/mo\/q\/medal&quot;,&quot;price&quot;:0,&quot;value&quot;:&quot;1&quot;,&quot;sprite&quot;:{&quot;1&quot;:&quot;1599647089,94&quot;,&quot;2&quot;:&quot;1599647089,95&quot;,&quot;3&quot;:&quot;1599647089,96&quot;}}' target="_blank"   href="http://tieba.baidu.com/mo/q/medal"  class="j_icon_slot"  title="初级核心用户"  locate="signprize_1#icon"  style="top: 0px; left:0px">  <div class=" j_icon_slot_refresh"></div></a></span>    </span>
    <span class="pull-right is_show_create_time" title="创建时间">16:04</span>
</div>
            </div>
                            <div class="threadlist_detail clearfix">
                    <div class="threadlist_text pull_left">
                                <div class="threadlist_abs threadlist_abs_onlyline ">
            这里面偷袭的，哪个不是鼎鼎大名的大人物? 
        </div>

            <div class="small_wrap j_small_wrap">
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_pre j_small_pic_pre" style="display:none"></a>
                <a rel="noreferrer"  href="#" onclick="return false;" class="small_btn_next j_small_pic_next" style="display:none"></a>
                <div class="small_list j_small_list cleafix">
                    <div class="small_list_gallery">
                        <ul class="threadlist_media j_threadlist_media clearfix" id="fm6971422634"><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="86165" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=2ae4b46d5d90f60304e5944509229f22/83136709c93d70cf9ba19251efdcd100bba12bc4.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=1c57510c23a85edffa8cfe2b796f0823/9e3df8dcd100baa16d777fe75010b912c8fc2e16.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="68070" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=97c9c1d37b81800a6eb0810c81051fc3/af6efbf2b2119313f6efc7ec72380cd790238def.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=4a62daa66ccb0a4685228b315b58f724/cb8065380cd79123d14cac28ba345982b2b78039.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li><li><a rel="noreferrer"  class="thumbnail vpic_wrap"><img src="" attr="80362" data-original="http://tiebapic.baidu.com/forum/wh%3D200%2C90%3B/sign=7e9d8fe7b11ea8d38a777c06a73a1c77/f0fa912397dda144e05354eea5b7d0a20df486c5.jpg"  bpic="http://tiebapic.baidu.com/forum/w%3D580%3B/sign=bb43660c1b3387449cc52f746134d8f9/5882b2b7d0a20cf47ccac68361094b36acaf9917.jpg" class="threadlist_pic j_m_pic "  /></a><div class="threadlist_pic_highlight j_m_pic_light"></div></li></ul>
                        <div class="small_pic_num center_text">共&nbsp;4&nbsp;张</div>
                    </div>
                </div>
            </div>                    </div>

                    
<div class="threadlist_author pull_right">
        <span class="tb_icon_author_rely j_replyer" title="最后回复人: 青红黑-白银灰">
            <i class="icon_replyer"></i>
            <a rel="noreferrer"  data-field='{&quot;un&quot;:&quot;\u8ff7\u7684\u6d77&quot;,&quot;id&quot;:&quot;tb.1.e98bc12.r0nVZRs6fiJd10frCAVqiQ&quot;}' class="frs-author-name j_user_card " href="/home/main/?un=%E8%BF%B7%E7%9A%84%E6%B5%B7&ie=utf-8&id=tb.1.e98bc12.r0nVZRs6fiJd10frCAVqiQ&fr=frs" target="_blank">青红黑<img src="//tb1.bdstatic.com/tb/cms/nickemoji/1-3.png" class="nicknameEmoji" style="width:13px;height:13px"/>...</a>        </span>
        <span class="threadlist_reply_date pull_right j_reply_data" title="最后回复时间">
            18:12        </span>
</div>
                </div>
                                </div>
    </div>
</li>










</ul>

<div class="thread_list_bottom clearfix">
        
<div id="frs_list_pager" class="pagination-default clearfix"><span class="pagination-current pagination-item ">1</span>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=50" class=" pagination-item " >2</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=100" class=" pagination-item " >3</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=150" class=" pagination-item " >4</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=200" class=" pagination-item " >5</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=250" class=" pagination-item " >6</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=300" class=" pagination-item " >7</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=350" class=" pagination-item " >8</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=400" class=" pagination-item " >9</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=450" class=" pagination-item " >10</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=50" class="next pagination-item " >下一页&gt;</a>
<a href="//tieba.baidu.com/f?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8&pn=5953550" class="last pagination-item " >尾页</a>
</div>    <div class="th_footer_bright">
        <div class="th_footer_l">
                            共有主题数<span class="red_text">5953588</span>个，贴子数
                <span class="red_text">292086496</span>篇
                <a rel="noreferrer"  class="fans_name" href="/bawu2/platform/listMemberInfo?word=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8"
                   target="_blank">海贼</a>数<span
                    class="red_text">10124066</span>
                    </div>
    </div>
</div>

</div>
        </div>
        <div class="aside" id="aside">
            <div class="aside_region celebrity" id="">
    <h4 class="region_header clearfix">
                <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
        <div class="intro">
    <div class="col2-left">
        <a class="gift-wrapper j-gift-buy" href="javascript:;">
            <span class="gift">
                <img src="//tb2.bdstatic.com/tb/img/single_member_100_0b51e9e.png">
            </span>
            皇冠身份
        </a>
    </div>
    <div class="col2-right">
        <ul class="privilege-list">
            <li>
                <i class="icon icon-red-thread-title"></i>
                发贴红色标题
            </li>
            <li>
                <i class="icon icon-red-name"></i>
                显示红名
            </li>
            <li>
                <i class="icon icon-sign-exp"></i>
                签到六倍经验
            </li>
        </ul>
    </div>
</div>
    <div class="more-privilege-container">
        <div class="first-show-container">
            <div class="open-btn gray-text-btn">更多定制特权<i class="down-icon"></i></div>
            <button class="purchase-member-btn j-gift-buy">兑换本吧会员</button>
        </div>
        <div class="second-show-container">
                        <ul class="privilege-unactivated-list">
                <li>
                    <i class="privilege-mark privilege-unactivated-icon"></i>
                    本吧专属印记
                </li>
                <li>
                    <i class="privilege-card-bg privilege-unactivated-icon"></i>
                    定制名片背景
                </li>
                <li>
                    <i class="privilege-top-thread privilege-unactivated-icon"></i>
                    名人自动顶贴
                </li>
                <li>
                    <i class="privilege-head-border privilege-unactivated-icon"></i>
                    定制头像边框
                </li>
            </ul>
            <div class="close-btn gray-text-btn">收起特权<i class="up-icon"></i></div>
            <button class="purchase-member-btn j-gift-buy">兑换本吧会员</button>
        </div>
    </div>
    <p class="gray-text">赠送补签卡1张，获得<a href="#" class="celebrity-purchase-exp" onclick="return false" target="_blank">[经验书购买权]</a>
    </p>

    </div>
    <div class="region_footer">        <div class="celebrity-cut-off"></div>
        <h4 class="celebrity-title">本吧名人
            <a href="#" target="_blank" style="display:none;">[本吧全部名人]</a>
        </h4>
        <div class="celebrity-content">
            <div class="col2-left">
                <a href="/celebrity/rankHome" target="_blank">
                    <img src="https://gss0.baidu.com/7Ls0a8Sm2Q5IlBGlnYG/sys/portrait/item/tb.1.8b5a06b8.gp5LUNHVfIez8ISnTlbkUQ" width="80"
                         height="80"/>
                </a>
            </div>
            <div class="col2-right">
                <p class="name">路飞<i class="icon-red"></i></p>

                <div class="user_level clearfix">
                    <a href="/celebrity/rankHome" target="_blank" class="celebrity-level">
    <span class="label">等级: </span>
    <span class="level">
        <span class="level-text">75</span>
    </span>
</a>                </div>
                <p>
                    <a href="/celebrity/rankHome" target="_blank">贴吧名人榜：</a>
                    <b class="red-text">1</b>
                </p>
            </div>
        </div>
        <a href="javascript:" class="btn btn-celebrity j-btn-celebrity">助攻名人，领特权</a>
                    <p class="tip">
                <i class="icon-horn"></i>海贼团专属路飞发贴气泡            </p>
            </div>
</div>
<div class="aside_region app_download_box" id="">
    <h4 class="region_header clearfix">
        扫二维码下载贴吧客户端        <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
        
<div class="clearfix app_download_wrap">
	<div class="app_download_icon">
		
	</div>
	<div class="app_download_info">
		下载贴吧APP<br />看高清直播、视频！
	</div>
</div>
    </div>
    <div class="region_footer"></div>
</div>
<div class="aside_region forum_info j_forum_info" id="">
    <h4 class="region_header clearfix">
        本吧信息        <span class="pull_right j_op"><a rel="noreferrer"  target="_blank" href="/bawu2/platform/detailsInfo?word=%E6%B5%B7%E8%B4%BC%E7%8E%8B&amp;ie=utf-8">查看详情&gt;&gt;</a>
 </span>
    </h4>
    <div class="region_cnt clearfix">
        


    <div class="author-manager media_horizontal clearfix">
      <a rel="noreferrer"  href="//tieba.baidu.com/tbvip/literary/index" target="_blank"
         class="interface2">百度贴吧作者认证</a>
    </div>

      <ul class="manager_groups aside_media_horizontal clearfix">
                                <li class="media_vertical ">
                                <a rel="noreferrer"  class="media_top manager_media" href="/home/main/?un=Smile%E4%B8%9C%E5%8D%81%E5%8C%BA&ie=utf-8&amp;id=tb.1.86f97cdb.HZWW566nk7tCtjVPCXhBgA&amp;fr=frs"
                   target="_blank" title="Smile东十区">
                    <img src="https://gss0.bdstatic.com/6LZ1dD3d1sgCo2Kml5_Y_D3/sys/portrait/item/tb.1.86f97cdb.HZWW566nk7tCtjVPCXhBgA" alt="">
                                            <span class="media_caption">吧主</span>
                                    </a>

                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/home/main/?un=Smile%E4%B8%9C%E5%8D%81%E5%8C%BA&ie=utf-8&amp;id=tb.1.86f97cdb.HZWW566nk7tCtjVPCXhBgA&amp;fr=frs" target="_blank"
                       title="Smile东十区">Smile东十区</a>
                                    </div>
            </li>
            </ul>
<div id="tbManagerCandidatesNum" style="display:none">
    </div>


    <p class="forum_info_desc">
        <span>小吧：</span>小吧主共<em>29</em>人
    </p>
<p class="forum_info_desc">
    <span>会员：</span>
    <a rel="noreferrer"  id="member_name_link" href="/bawu2/platform/listMemberInfo?word=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8"
       target="_blank">海贼</a>
        </p>
<p class="forum_info_desc">
    <span>目录：</span>
            <a rel="noreferrer"  href="/f/fdir?fd=%E5%8A%A8%E6%BC%AB&ie=utf-8&amp;sd=%E5%8A%A8%E6%BC%AB%C2%B7%E8%BD%BB%E5%B0%8F%E8%AF%B4%E4%BD%9C%E5%93%81&ie=utf-8"
           target="_blank">动漫·轻小说作品</a>
    </p>

<div class="apply_groups">
            <span id="tbManagerApply"></span>
                <ins>|</ins>
        <span id="tbManagerAssistApply"><a rel="noreferrer"  class="frs_apply_assist j_btn_apply_assist"
                                           href="/bawu2/platform/listCandidateInfo?word=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8">申请小吧主</a></span>
    </div>


    </div>
    <div class="region_footer"></div>
</div>
<div class="aside_region zyq_mod_link j_zyq_mod_link" id="">
    <h4 class="region_header clearfix">
        海内存知己        <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
            <ul class="unordered_list_dot">
                    <li><a rel="noreferrer"  href="http://bbs.talkop.com/?fromuid=23023" target="_blank" class="j_mod_item">TalkOP海贼王论坛</a></li>
                    <li><a rel="noreferrer"  href="http://tieba.baidu.com/f?kw=DNF&amp;fr=wwwt" target="_blank" class="j_mod_item">地下城与勇士</a></li>
                    <li><a rel="noreferrer"  href="http://tieba.baidu.com/f?kw=灌篮高手&amp;frs=yqtb" target="_blank" class="j_mod_item">灌篮高手</a></li>
                    <li><a rel="noreferrer"  href="http://www.ishuhui.com" target="_blank" class="j_mod_item">鼠绘汉化论坛</a></li>
            </ul>
    </div>
    <div class="region_footer"></div>
</div>
<div class="aside_region zyq_mod_friend j_zyq_mod_friend" id="">
    <h4 class="region_header clearfix">
        友情贴吧        <span class="pull_right j_op"> </span>
    </h4>
    <div class="region_cnt clearfix">
            <ul class="aside_media_horizontal clearfix">
                    <li class="media_vetical ">
                <a rel="noreferrer"  class="media_top" href="/f?kw=lol&frs=yqtb" target="_blank" title="lol">
                <img src="https://imgsa.baidu.com/forum/wh%3D60%2C60%3B/sign=35d8da1b5682b2b7a7ca31c20181fddf/9f2f070828381f307db8cfb6a6014c086e06f008.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=lol&frs=yqtb" target="_blank" class="j_mod_item" title="lol">lol</a>
                </div>
            </li>
                    <li class="media_vetical ">
                <a rel="noreferrer"  class="media_top" href="/f?kw=魔兽世界&frs=yqtb" target="_blank" title="魔兽世界">
                <img src="https://imgsa.baidu.com/forum/wh%3D60%2C60%3B/sign=280b9399222eb938ec3872f4e54eb305/622762d0f703918fdc00adb25c3d269758eec4f1.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=魔兽世界&frs=yqtb" target="_blank" class="j_mod_item" title="魔兽世界">魔兽世界</a>
                </div>
            </li>
                    <li class="media_vetical media_last">
                <a rel="noreferrer"  class="media_top" href="/f?kw=火影忍者&frs=yqtb" target="_blank" title="火影忍者">
                <img src="https://imgsa.baidu.com/forum/wh%3D60%2C60%3B/sign=899b9bf1da1373f0f56a679994237dcb/3b292df5e0fe9925e4e96ada3fa85edf8cb17156.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=火影忍者&frs=yqtb" target="_blank" class="j_mod_item" title="火影忍者">火影忍者</a>
                </div>
            </li>
                    <li class="media_vetical ">
                <a rel="noreferrer"  class="media_top" href="/f?kw=七龙珠&frs=yqtb" target="_blank" title="七龙珠">
                <img src="https://imgsa.baidu.com/forum/wh%3D60%2C60%3B/sign=82d097528f13632715b8ca35a1a396dc/a911349b033b5bb55ae52b7033d3d539b600bc37.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=七龙珠&frs=yqtb" target="_blank" class="j_mod_item" title="七龙珠">七龙珠</a>
                </div>
            </li>
                    <li class="media_vetical ">
                <a rel="noreferrer"  class="media_top" href="/f?kw=死神&frs=yqtb" target="_blank" title="死神">
                <img src="https://imgsa.baidu.com/forum/wh%3D60%2C60%3B/sign=75e697b5fe03738dde1f042483378661/b03533fa828ba61e6434203a4934970a314e59c9.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=死神&frs=yqtb" target="_blank" class="j_mod_item" title="死神">死神</a>
                </div>
            </li>
                    <li class="media_vetical media_last">
                <a rel="noreferrer"  class="media_top" href="/f?kw=银魂&frs=yqtb" target="_blank" title="银魂">
                <img src="https://imgsa.baidu.com/forum/wh%3D60%2C60%3B/sign=85da3ca151fbb2fb347e50147f661694/0824ab18972bd407e9cee7017f899e510eb309c4.jpg" alt=""></a>
                <div class="text_overflow media_bottom">
                    <a rel="noreferrer"  href="/f?kw=银魂&frs=yqtb" target="_blank" class="j_mod_item" title="银魂">银魂</a>
                </div>
            </li>
            </ul>
    </div>
    <div class="region_footer"></div>
</div>



        <div id="branding_ads">
        </div>
        </div>
    </div>
</div>
<div class="foot">
    
<div class="frs_content_footer_pagelet">
	
	
		
		<div class="editor_wrap_bright ">
	




<a name="sub"></a>
<div id="tb_rich_poster_container" class="tb_rich_poster_container">
    <div id="rich_ueditor_tpl">
        <div id="tb_rich_poster" class="tb_rich_poster">
            <div class="j_bubble_container"></div>

            
                        <div class="poster_head clearfix">
                <div class="poster_head_text">
                                            <a class="add_thread_btn post_head_btn cur" title="发表新贴" href="javascript:;"><span  class="post_head_btn_icon post_head_btn_icon_post"></span>发表新贴</a>

                        

                        
                                                <a class="add_vote_btn post_head_btn" title="发起投票" target="_blank" href="/newvote/createvote?kw=%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8"><span  class="post_head_btn_icon post_head_btn_icon_vote"></span>发起投票</a>

                        
                    
                </div>

                                <div class="poster_head_surveillance j_surveillance">
                    发贴请遵守 <a href="/tb/eula.html" target="_blank" onclick="$.stats.track('post_agreement', 'poster')">贴吧协议及“七条底线”</a>
					<a href="javascript:;" id="frs_footer_tieba_report" class="btn_tousu fr post_head_tousu" data-checkun="un">贴吧投诉</a>                    <button type="button" class="poster_disable_float j_disable_float" title="停止浮动">停止浮动</button>
                </div>
            </div>
            
                        







			<div class="poster_body editor_wrapper">
                                <div class="poster_component title_container">
                    <div class="poster_title">标&nbsp;&nbsp;题:</div>
                    <div class="j_title_wrap">
                        <input type="text" class="editor_textfield editor_title ui_textfield j_title j_topic_sug_input" name="title" autocomplete="off" />
                        <span class="topic_add_btn j_topic_add_btn"></span>
                        <p class="fullscreen-word-limit"><span class="fullscreen-limit j-fullscreen-wl">0</span>/30</p>
                    </div>
                    <div class="poster_error j_error"></div>
                </div>
                
                
                                <div class="poster_component editor_content_wrapper ueditor_container">
                    <div class="poster_reply">内&nbsp;&nbsp;容:</div>
                    <div class="old_style_wrapper">
                        <div id="ueditor_replace" style="width: 700px; height: 220px;"></div>
                    </div>
                    <div class="poster_error j_error"></div>
                </div>

                                <div class="j_poster_share poster_share">
                                <label><input type="checkbox" class="j_use_share"/> 发表后自动分享本贴</label>
                
                </div>

                                <div class="j_poster_signature poster_signature">
                    <label><input type="checkbox" class="j_use_signature"/> 使用签名档</label>&nbsp;
                    <span class="j_signature_wrapper signature_wrapper">
                        <select name="sign_id" class='j_sign_id'>

                        </select>
                        &nbsp;<a style="color:#0449BE" target="_blank" href="/i/sys/jump?type=signsetting">查看全部</a>
                    </span>
                </div>

                
                
                                <div class="poster_component editor_bottom_panel clearfix">
                    <div class="j_floating">
                        <button class="btn_default btn_middle j_submit poster_submit" title="Ctrl+Enter快捷发表">
                            发 表
                        </button>
                        <span class="poster_posting_status j_posting_status"></span>

                        <div class="poster_draft_status j_draft" style="display: none;">
                            <span class="j_content"></span>
                            <span title="清空草稿" class="poster_draft_delete j_clear"></span>
                        </div>
                        <button class="btn_sub btn_middle j_clear_fullscreen poster_clear_fullscreen" title="">
                            退 出
                        </button>
                    </div>
                </div>

            </div>


            
                                </div>
    </div>
</div>
	</div>

	
	
<div id="footer" class="footer">   
                                                                                                      
	<span>&copy;2020 Baidu</span>
	<a pv_code="0" href="/tb/eula.html" target="_blank">贴吧协议</a>	<span>|</span>
	<a pv_code="0" href="https://tieba.baidu.com/tb/cms/tieba-fe/tieba_promise.html" target="_blank">隐私政策</a>	<span>|</span>
	<a pv_code="0" href="http://tieba.baidu.com/tb/system.html" target="_blank">吧主制度</a>	<span>|</span>
	<a class="ueg_feedback-link" data-site="feedbackLink"  pv_code="0" href="http://tieba.baidu.com/hermes/feedback" target="_blank">意见反馈</a>	<span>|</span>
	<a pv_code="0" href="/tb/zt/declare/" target="_blank">网络谣言警示</a>	</div>

</div>

</div>
<div id="fixed_bar" class="">
    <img src="//tb1.bdstatic.com/tb/cms/PC%E7%AB%AF%E5%BA%95%E9%83%A8%E9%80%9A%E6%A0%8F%E5%BC%B9%E5%B1%821000x120.png" alt="">
    <img src="//tb2.bdstatic.com/tb/img/icon_close_1683259.png" alt="" class="close">
</div>

<a id="fixed_daoliu" href="" target="_blank" data-switch="">
    <img src="">
    <span class="close"></span>
</a>
    </div>
</div>

<script src="//tb1.bdstatic.com/??/tb/static-common/js/promise_3464b70.js,/tb/static-common/js/promise_config_91c2822.js,/tb/static-common/lib/uri.js/src/URI.min_e84a17a.js,/tb/static-common/js/jquery/jquery_ba2d628.js,/tb/static-common/js/jquery/jquery-ui-1.10.3.custom_65f256d.js,/tb/static-common/js/jquery/jquery.ui.droppable_3b547e9.js,/tb/static-common/js/jquery/jquery.lazyload_49a7282.js,/tb/static-common/lib/fis-module/fis_c1e11e0.js,/tb/static-common/js/__aop_af3a579.js,/tb/static-common/js/baiduTemplate_841433b.js,/tb/static-common/js/jcarousellite_1.0.1_a033082.js,/tb/static-common/js/page_link_2ec40cf.js,/tb/static-common/js/pageconf_8abbe38.js,/tb/static-common/js/tb_0329f65.js,/tb/static-common/js/tb_extend_000de9f.js,/tb/static-common/js/tb_fis_config_6ca7118.js,/tb/static-common/js/tb_stats_ba8deb9.js,/tb/static-common/js/underscore_b23cfa6.js,/tb/static-common/js/qrcode_f84ab06.js,/tb/static-common/lib/fis-module/module_5ae89d6.js,/tb/static-common/lib/bigpipe.js/lib/bigpipe_eabdb6b.js,/tb/static-common/js/bigpipe_config_9c152a9.js,/tb/static-common/js/lcs/lib/Long_8276e76.js,/tb/static-common/js/lcs/lcsas_4e45cc0.js,/tb/static-common/js/bsk/dknsaZmLdyKfEeIVbKxn_7b5edbc.js,/tb/static-common/js/bsk/omzVouOACqkNljzDbdOB_4efff96.js,/tb/static-common/js/bsk/jkaEbldlZmvawIuwAdqo_670b771.js"></script>
<script src="//tb1.bdstatic.com/??/tb/static-common/lib/smallpipe.js/lib/smallpipe_d0797f3.js"></script>
<script src="//tb1.bdstatic.com/??/tb/static-common/js/common/MessageSystem_2f3859e.js,/tb/static-common/js/common/CommonManager_main_d3b4283.js,/tb/static-common/js/common/passport/pass_shell_7351279.js,/tb/static-common/js/common/passport/passport_reset_ec12f65.js,/tb/static-common/js/common/passport/PassportFillName_925655f.js,/tb/static-common/js/common/uiDecorator_125371a.js,/tb/static-common/js/common/passport/PassportLogin_fe8162a.js,/tb/static-common/js/common/user/User_11fe4ca.js,/tb/static-common/js/common/crosspage_msg_system/utils/LCFManager_f2555be.js,/tb/static-common/js/common/crosspage_msg_system/utils/MessageProxy_25dc8d9.js,/tb/static-common/js/common/crosspage_msg_system/utils/SWFListen_87d118b.js,/tb/static-common/js/common/crosspage_msg_system/utils/SWFRequest_f586836.js,/tb/static-common/js/common/crosspage_msg_system/MsgSystem_9ef7035.js,/tb/static-common/js/common/user_message/UserMessage_e770e9e.js,/tb/static-common/js/tb_https_2f6042d.js"></script>





<style style="text/css">
.special_conf_skin{background:;}</style>
















<div id="global_notice_wrap" class="global_notice_wrap"></div>












<script type="text/javascript">window.alogObjectConfig={product:"14",page:"14_21",monkey_page:"",speed_page:"",speed:{sample:"0.001"},monkey:{sample:"0.001"},exception:{sample:"0.001"},feature:{sample:"0.001"},cus:{sample:"0.001"},csp:{sample:"0.001","default-src":[{match:"*bae.baidu.com",target:"Accept,Warn"},{match:"*.baidu.com,*.bdstatic.com,*.bdimg.com,localhost,*.hao123.com,*.hao123img.com",target:"Accept"},{match:/^(127|172|192|10)(\.\d+){3}$/,target:"Accept"},{match:"*",target:"Accept,Warn"}]}},void function(e,t,a,c,n,o){function r(t){e.attachEvent?e.attachEvent("onload",t,!1):e.addEventListener&&e.addEventListener("load",t)}function s(e,a,c){c=c||15;var n=new Date;n.setTime((new Date).getTime()+1e3*c),t.cookie=e+"="+escape(a)+";path=/;expires="+n.toGMTString()}function i(e){var a=t.cookie.match(new RegExp("(^| )"+e+"=([^;]*)(;|$)"));return null!=a?unescape(a[2]):null}function p(){var e=i("PMS_JT");if(e){s("PMS_JT","",-1);try{e=e.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),e=e&&e[1]&&e[2]?{s:parseInt(e[1]),r:e[2]}:{}}catch(a){e={}}e.r&&t.referrer.replace(/#.*/,"")!=e.r||alog("speed.set","wt",e.s)}}if(e.alogObjectConfig){var m=e.alogObjectConfig.sample,l=e.alogObjectConfig.rand;c="https:"===e.location.protocol?"https://fex.bdstatic.com"+c:"http://fex.bdstatic.com"+c,m&&l&&l>m||(r(function(){alog("speed.set","lt",+new Date),n=t.createElement(a),n.async=!0,n.src=c+"?v="+~(new Date/864e5)+~(new Date/864e5),o=t.getElementsByTagName(a)[0],o.parentNode.insertBefore(n,o)}),p())}}(window,document,"script","/hunter/alog/dp.min.js");</script>
<script type="text/javascript">!function(){"use strict";Bigpipe.addEventListener("beforepageletload",function(e){e.on("styleloaded",function(){this.dpStyleLoadedTime=+new Date}),e.on("scriptloaded",function(){this.dpScriptLoadedTime=+new Date})}),Bigpipe.addEventListener("pageletstyleloaded",function(e){e.emit("styleloaded"),this.dpSelfStyleLoadedTime=+new Date}),Bigpipe.addEventListener("pageletscriptloaded",function(e){e.emit("scriptloaded"),this.dpSelfScriptLoadedTime=+new Date}),Bigpipe.addEventListener("pageloaded",function(e){var d,a,t,o=[{name:"frs-header/pagelet/head",showKey:"c_head_pagelet_show",loadedKey:"c_head_pagelet_loaded"},{name:"search/pagelet/search_logic",showKey:"c_search_pagelet_show",loadedKey:"c_search_pagelet_loaded"},{name:"frs-list/pagelet/content",showKey:"c_list_pagelet_show",loadedKey:"c_list_pagelet_loaded"},{name:"frs-aside/pagelet/aside",showKey:"c_aside_pagelet_show",loadedKey:"c_aside_pagelet_loaded"},{name:"frs-footer/pagelet/content_footer",showKey:"c_foot_pagelet_show",loadedKey:"c_foot_pagelet_loaded"}];$.each(o,function(){var o=e[this.name];o&&alog&&alog.fire&&(alog("speed.set",this.showKey,this.isSelf?o.dpSelfStyleLoadedTime:o.dpStyleLoadedTime),alog.fire("mark"),alog("speed.set",this.loadedKey,this.isSelf?o.dpSelfScriptLoadedTime:o.dpScriptLoadedTime),alog.fire("mark"),d=!d||d>o.dpStyleLoadedTime?o.dpStyleLoadedTime:d,a=!a||a>o.dpScriptLoadedTime?o.dpScriptLoadedTime:a,t=!t||t<o.dpStyleLoadedTime?o.dpStyleLoadedTime:t)}),d&&a&&(alog("speed.set","c_first_pagelet_show",d),alog.fire("mark"),alog("speed.set","c_first_pagelet_loaded",a),alog.fire("mark")),alog("speed.set","drt",t)})}();</script><script src="//tb1.bdstatic.com/??/tb/_/title_1a42886.js,/tb/_/http_transform_d9b1cbd.js,/tb/_/content_1216e5e.js,/tb/_/frs-footer/content_footer_bc94b74.js,/tb/_/fixed_bar_e002a0a.js,/tb/_/fixed_daoliu_422cc1d.js,/tb/_/suggestion_d2ee788.js,/tb/_/search_handler_7e7697d.js,/tb/_/search_dialog_b4dc63b.js,/tb/_/search_logic_13e7c51.js,/tb/_/page_router_9f0f230.js,/tb/_/login_dialog_21db6a0.js,/tb/_/tdou_open_type_a72e1ed.js,/tb/_/user_api_10e048c.js,/tb/_/icons_a4b7c8c.js,/tb/_/base_user_data_ff57bd7.js,/tb/_/base_dialog_user_bar_bf63bc8.js,/tb/_/qianbao_cashier_dialog_bb2a1a5.js,/tb/_/qianbao_purchase_member_533123a.js,/tb/_/messenger_e5c0696.js,/tb/_/cashier_dialog_d52cf7c.js,/tb/_/pay_member_c57f92d.js,/tb/_/event_center_ca531c9.js,/tb/_/new_message_system_eb357ea.js,/tb/_/join_vip_dialog_9242ef7.js,/tb/_/user_head_00b2e11.js,/tb/_/js_pager_753507e.js,/tb/_/wallet_dialog_193e3f1.js,/tb/_/card_d6007e6.js,/tb/_/userbar_32c5b26.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/tbcopy_f4f2e14.js,/tb/_/duoku_servers_dialog_0291705.js,/tb/_/duoku_servers_list_046cdf2.js,/tb/_/poster/rich_poster_af27300.js,/tb/_/footer_8d5b425.js,/tb/_/head_main_c294af5.js,/tb/_/full_width_head_6874452.js,/tb/_/loader_12d7714.js,/tb/_/preview_e43ce97.js,/tb/_/slide_show_d52e648.js,/tb/_/js_redirect_ed0cfa9.js,/tb/_/head_recom_a01b7b3.js,/tb/_/focus_btn_9db672d.js,/tb/_/conf_skin_3b60c27.js,/tb/_/frs-footer/frs_from_guide_55b4caa.js,/tb/_/bubble_tip_d34e792.js,/tb/_/tbshare_share_61f1525.js,/tb/_/tbshare_popup_1c599af.js,/tb/_/aside_float_bar_a3ab60b.js,/tb/_/frs-footer/aside_float_btns_4709252.js,/tb/_/verify_manager_phone_cba5a4d.js,/tb/_/inform_manager_verify_phone_f5289a5.js,/tb/_/detect_manager_block_3e52a76.js,/tb/_/bawu_add_section_e27c6f2.js,/tb/_/icon_tip_f5bc853.js,/tb/_/umoney_query_e6ef23a.js,/tb/_/qianbao_purchase_tdou_f4c69c0.js,/tb/_/tdou_template_8d6b3f6.js,/tb/_/tdou_builder_05101dd.js,/tb/_/tdou_view_util_d282db0.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/rsa_safe_ffe2fa7.js,/tb/_/paykey_safe_payment_f7a973d.js,/tb/_/captcha_d99d16f.js,/tb/_/captcha_dialog_ceaacd2.js,/tb/_/captcha_safe_payment_7f700b4.js,/tb/_/mobile_safe_payment_b2a273c.js,/tb/_/tbean_safe_3668241.js,/tb/_/tbean_safe_ajax_5dbae2e.js,/tb/_/tdou_data_747c462.js,/tb/_/tdou_view_check_f11908d.js,/tb/_/tdou_counter_cbe5c8a.js,/tb/_/tdou_view_fec0b7b.js,/tb/_/umoney_1379f71.js,/tb/_/tdou_view_operation_bootstrap_4a983b5.js,/tb/_/tdou_view_cashier_6afe462.js,/tb/_/tdou_view_auto_redirect_653558b.js,/tb/_/tdou_view_pay_1461feb.js,/tb/_/firework_v2_43f8946.js,/tb/_/show_dialog_d46d0a5.js,/tb/_/payment_dialog_title_3e773b9.js,/tb/_/tdou_get_6d6607b.js,/tb/_/tdou_3289666.js,/tb/_/tcharge_dialog_29efc3e.js,/tb/_/novel_icons_5f06004.js,/tb/_/global_notice_8f03246.js,/tb/_/pay_util_e0a3684.js,/tb/_/umoney_promotion_dialog_0174dae.js,/tb/_/snowflow_6f0903a.js,/tb/_/dialog_d31c70c.js,/tb/_/util_fdb7481.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/cont_sign_card_641fc4e.js,/tb/_/net_proxy_f5ecab7.js,/tb/_/use_controller_e92bca8.js,/tb/_/buy_controller_516c900.js,/tb/_/tieba_sign_card_f938fb7.js,/tb/_/thread_631d0b6.js,/tb/_/frs-aside/base_aside_43591cb.js,/tb/_/placeholder_fd56d8e.js,/tb/_/sms_verify_dialog_cb7b503.js,/tb/_/forbidden_ea6d3fd.js,/tb/_/poster/poster_context_72abca5.js,/tb/_/poster/post_signature_e83b73e.js,/tb/_/poster/mouse_pwd_355b0e7.js,/tb/_/poster/share_thread_c8aa28c.js,/tb/_/poster/jiyan_service_e407177.js,/tb/_/poster/bsk_service_c6680a4.js,/tb/_/poster/params_xss_handler_2083372.js,/tb/_/tool_696c6e8.js,/tb/_/tpl_async_15_395293f.js,/tb/_/loader_630632a.js,/tb/_/like_tip_4f71dda.js,/tb/_/poster/post_service_e3f5dd3.js,/tb/_/poster/topic_suggestion_4827396.js,/tb/_/poster/post_prefix_3837331.js,/tb/_/word_limit_c30df3b.js,/tb/_/poster/post_manager_968b3bd.js,/tb/_/complaint_bar_owner_4d7fe74.js,/tb/_/poster/rich_poster_5476127.js,/tb/_/ueditor_base_66b0746.js,/tb/_/ueditor_extend_base_29960fa.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/background_3047546.js,/tb/_/auto_link_e48bd2b.js,/tb/_/tb_gram_a17c017.js,/tb/_/slide_select_d3198f9.js,/tb/_/image_flash_editor_96f9f79.js,/tb/_/scroll_panel_0150f9a.js,/tb/_/image_exif_285bafe.js,/tb/_/image_uploader_3de9609.js,/tb/_/image_uploader_manager_7dfd79e.js,/tb/_/picture_uploader_1cc7938.js,/tb/_/picture_selector_7697bc3.js,/tb/_/picture_web_selector_0bc6de4.js,/tb/_/picture_76ba58a.js,/tb/_/custom_emotion_24326d5.js,/tb/_/ueditor_emotion_f766931.js,/tb/_/emotion_4add196.js,/tb/_/ueditor_video_12099f9.js,/tb/_/video_ae09aec.js,/tb/_/sketchpad_2ef5fac.js,/tb/_/scrawl_0005979.js,/tb/_/jquery_caret_2d51110.js,/tb/_/ueditor_topic_e81e6a5.js,/tb/_/topic_09c6508.js,/tb/_/topic_suggestion_9bb3805.js,/tb/_/fullscreen_9b3dd34.js,/tb/_/height_limit_e4b1ffa.js,/tb/_/draft_91a3223.js,/tb/_/at_68fdde7.js,/tb/_/counter_d482e1c.js,/tb/_/word_limit_0f6ca1b.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/props_data_2514f70.js,/tb/_/bubble_factory_279ffe5.js,/tb/_/post_setting_0ce6f36.js,/tb/_/setting_f184c24.js,/tb/_/medal_549f6f1.js,/tb/_/paypost_data_70c1ba1.js,/tb/_/paypost_agree_dialog_a4c48b3.js,/tb/_/paypost_editor_7d000d4.js,/tb/_/paypost_867d76a.js,/tb/_/attention_category_game_5978a17.js,/tb/_/focus_btn_bb15d87.js,/tb/_/game_rank_in_head_a46e35a.js,/tb/_/game_frs_head_b792766.js,/tb/_/navigator_b701689.js,/tb/_/search_handler_2ff14b8.js,/tb/_/tbnav_bright_f51371d.js,/tb/_/conf_repost_b8046ac.js,/tb/_/iframe_head_f52cc7a.js,/tb/_/activity_btv_3cd04b8.js,/tb/_/game_iframe_common_7e353a3.js,/tb/_/game_banner_ff14_621e357.js,/tb/_/game_head_info_2bba44c.js,/tb/_/duoku_xwj_vip_8dbb9c2.js,/tb/_/wca_head_559d315.js,/tb/_/game_player_auth_dialog_e694748.js,/tb/_/sign100_c123624.js,/tb/_/sign_shai_0d657eb.js,/tb/_/sign_mod_8e3931c.js,/tb/_/platform_spread_layer_6e2b6ed.js,/tb/_/platform_spread_video_c26eda2.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/popup_zhang_8e0fca3.js,/tb/_/block_user_7c0f0ff.js,/tb/_/util_top_cookie_b437d61.js,/tb/_/music_player_5f6a3b2.js,/tb/_/util_picture_slide_9a62a0d.js,/tb/_/util_media_init_de70972.js,/tb/_/util_favorite_3dd4905.js,/tb/_/util_picture_rotation_2d0e178.js,/tb/_/util_image_process_cc67662.js,/tb/_/util_media_controller_f6aeb20.js,/tb/_/util_https_stat_a01778b.js,/tb/_/scroll_event_a9a7916.js,/tb/_/game_code_thread_7141b4c.js,/tb/_/game_thread_90bad35.js,/tb/_/single_icons_9d843f9.js,/tb/_/post_marry_d80a1ea.js,/tb/_/interaction_bdbd175.js,/tb/_/member_api_c29c369.js,/tb/_/month_icon_63870d4.js,/tb/_/user_visit_card_02c510d.js,/tb/_/util_pop_video_0bb4bc1.js,/tb/_/audio_player_0e5ab66.js,/tb/_/voice_9f54341.js,/tb/_/thread_list_1e49711.js,/tb/_/professional_manager_tips_41b690e.js,/tb/_/celebrity_widget_a676416.js,/tb/_/celebrity_forum_dialog_dc04b7c.js,/tb/_/forum_member_dialog_1139bd7.js,/tb/_/exp_package_dialog_67a3307.js,/tb/_/npc_vote_action_0c26f5f.js"></script>
<script src="//tb1.bdstatic.com/??/tb/_/celebrity_b5cf0a5.js,/tb/_/celebrity_expball_13260da.js,/tb/_/frs-aside/forum_info_fec7f4c.js,/tb/_/frs-aside/zyq_3a18750.js,/tb/_/frs-aside/define_link_20c468f.js,/tb/_/frs-aside/friend_b2f77b0.js,/tb/_/mixin_b5f95cd.js,/tb/_/bean_a6c16b5.js,/tb/_/guess_f82c751.js,/tb/_/sidebar_8446bb9.js,/tb/_/tpl_ext_c01a6ba.js,/tb/_/util_pager_9cf1330.js"></script>
<script>    _.Module.use('tbui/widget/httpTransform', [], function () {
    });
    _.Module.use('search/widget/suggestion', [], function () {
    });
    _.Module.use('search/widget/search_logic', [
        $('#head'),
        {
            product: 'frs',
            forumName: '海贼王',
            searchFixed: '1',
            sugOn: '1'
        }
    ]);
    _.Module.use('tbui/widget/page_router', [pagelet]);
    _.Module.use('frs-base/pagelet/content', [pagelet], function (instance) {

    });
    // PageData.product = frs TODO
    _.Module.use("common/widget/Userbar", {
        page: 'frs',
        userLevel:null,
        userScore:null,
        vipInfo:null,
        isVideoPGCUser: 0,
        lcsKey: '', // flash_lcs.js 中使用
        bluePush: {
            unit: {"url":["http:\/\/push.dui1dui.com\/tieba\/awaken"],"button":["\u9a6c\u4e0a\u62a2"],"text":["\u4eb2\u7231\u7684\uff0c\u4f60\u4e0d\u77e5\u9053\u5417\uff1f\u4f60\u8d26\u6237\u4e2d\u7684\u84dd\u94bb\u53ef\u4ee5\u7528\u6765\u5151\u6362\u8d34\u5427\u4f1a\u5458\uff01\u540d\u989d\u6709\u9650\uff0c\u901f\u6765\u62a2\uff01"]},
            handle: null,
            diamond: null        },
        userBarConfigData: {"switch":"0","word":"hao123","url":"https:\/\/www.hao123.com\/?tn=50000076_hao_pg"}    });
_.Module.use('common/widget/footer', [], function(){});
_.Module.use('frs-footer/pagelet/content_footer', [pagelet]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('tbui/widget/httpTransform', [], function () {
    });
_.Module.use('tbui/widget/preview', [], function(){});
_.Module.use('tbui/widget/preview', [], function(){});
    _.Module.use('platform-activity/widget/headRecom', [true, {"line":"PT","action_type":"VIEW_TRUE","obj_id":"258430013_13","uid":null,"uname":null,"fid":null,"fname":null,"first_dir":null,"second_dir":null}, {"line":"PT","callfrom":"effect_evl","action_type":"VIEW_TRUE","id":258430013,"res_id":13,"uid":null,"uname":null,"fid":null,"fname":null,"first_dir":null,"second_dir":null}, {"activity_type":0,"head_imgs":[{"img_url":"\/\/tiebapic.baidu.com\/forum\/pic\/item\/c2fdfc039245d688870de3ffb3c27d1ed21b2459.jpg","override":false,"btn_text":"\u7acb\u5373\u67e5\u770b","title":"19\u5143200GB\u6d41\u91cf\u4e0d\u9650\u901f+\u7231\u5947\u827aVIP\u4f1a\u5458","subtitle":"\u6a59\u5305\u4f60\u7684\u4e0a\u7f51\u751f\u6d3b\uff0c\u6d41\u91cf\u73a9\u5c3d\u5174\uff0c\u4f1a\u5458\u770b\u8fc7\u763e\uff0c\u4eb2\u60c5\u53f7\u7801\u514d\u8d39\u6253~","pc_url":"\/official\/click\/redirect?client_type=pc_web&tbjump=https%3A%2F%2Fcard.10010.com%2Fqueen%2ForangeCard%2Fhqytb.html%3Fchannel%3D03-0765-a112-9999&ie=utf-8&task=%E5%90%A7%E5%A4%B4%E5%9B%BE%E6%8E%A8%E8%8D%90%E7%BB%9F%E8%AE%A1&ie=utf-8&locate=%E5%A4%B4%E9%83%A8%E8%BD%AE%E6%92%AD%E5%9B%BE&ie=utf-8&page=pfe&ie=utf-8&type=click&url=http%3A%2F%2Ftieba.baidu.com%2Ff%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36%3Fkw%3D%25E6%25B5%25B7%25E8%25B4%25BC%25E7%258E%258B%26User-Agent%3DMozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWOW64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F85.0.4183.83%2BSafari%252F537.36&ie=utf-8&refer=&ie=utf-8&fid=&fname=&uid=&uname=&is_new_user=&tid=&_t=1600683658&frame=1&evl_client_type=pc_web&evl_page=FRS&evl_locate=p0249&evl_task=ad_plat&evl_line=PT&evl_action_type=CLICK&evl_callfrom=effect_evl&evl_obj_id=258430013_13&evl_id=258430013&evl_res_id=13&evl_uid=&evl_uname=&evl_fid=&evl_fname=&evl_first_dir=&evl_second_dir="}],"activity_title":null,"res_id":13,"id":258430013,"adtype":"mis"}],  function(instance) {});
    _.Module.use('frs-header/widget/head_main', [{
        kw: "海贼王",
        source: ""
    }], function () {
    });
_.Module.use('tbui/widget/preview', [], function(){});
_.Module.use('tbui/widget/preview', [], function(){});
_.Module.use('tbui/widget/conf_skin', [{
	bodyClass: "special_conf_skin",
	couplet: {"start_time":1575889436,"end_time":4100497464,"background_info":{"adtype":null,"showurl":null},"task_id":null},
	isStar: 0,
    isOnStatus: true,
	evlParam: {"line":"PT","action_type":"VIEW_TRUE","obj_id":"_","uid":0,"uname":"","fid":11772,"fname":"\u6d77\u8d3c\u738b","first_dir":"\u52a8\u6f2b","second_dir":"\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1"},
	evlParamPb: {"line":"PT","callfrom":"effect_evl","action_type":"VIEW_TRUE","id":null,"res_id":null,"uid":0,"uname":"","fid":11772,"fname":"\u6d77\u8d3c\u738b","first_dir":"\u52a8\u6f2b","second_dir":"\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1"},
	bg_top_pic: "",
	asp_showurl: "",
	task_id: "",
	adtype: ""
}]);
	_.Module.use("frs-footer/widget/frs_from_guide");
	_.Module.use('frs-footer/widget/aside_float_btns', [{
        isBottle: 0,
        isNewBottle: 0,
        bottleTid: ""    }]);
    _.Module.use('ueglib/widget/inform_manager_verifyPhone', [
        false,
        false,
        false    ]);
    _.Module.use('ueglib/widget/detect_manager_block', [], function (moduleInstance) {
        moduleInstance.setBlockState(false);
    });
	_.Module.use('bawu/widget/bawuAddSection',{
		"fname_u": "%E6%B5%B7%E8%B4%BC%E7%8E%8B&ie=utf-8" ,
		"fname": "\u6d77\u8d3c\u738b" ,
		"tbs": "106aeb5c78fcc5621600683657"	});
    _.Module.use('user/widget/icon_tip',{
        myIcons:[] ,
        pagelet: pagelet
        });
_.Module.use('encourage-base/widget/global_notice', [{
    scores: [],
    level : [],
    fireworkOptionsConf: "",
    isFireworkV2: "1"
}], function(){});
    _.Module.use('yunying/widget/snowflow', [{
            content: '海贼王',
            page: 'frs',
            snowflowImg: '',
            snowflowUrl: ''
        }]
    );
    _.Module.use('encourage-props/widget/tieba_sign_card',[{
        superboy: []    }]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
if (!window.PosterContext) {
_.Module.use('poster/widget/poster_context', [{
    blockInfo: {
        is_block : 0,
        block_reason:'',
        opgroup : '',
        days_tofree:0,
        block_errno: '0'
    }
}], function() {
    PosterContext.loadContextFromPageData($.extend({},PageData,{
        user:{
                        id: PageData.user.id,
            name: PageData.user.name,
            level: 1,
            isFavorForum: 0,
            isLogin: !!PageData.user.is_login,
            isBlocked: 0,
            isBlack: 0,
            noUsername: !!PageData.user.no_un,
            canPost: 0,
            canVote: 0,
            forbidFlag: 0,
            signNumber: 0,
            superboy: "",
            memberLevel: 0        },
        is_zone_forum: "0",
        is_user_has_zone_right: "0",
    }));
    PosterContext.loadAuthorities({"img_num":50,"video_num":1,"smiley_num":50,"white_list":["http:\/\/www.tudou.com\/","http:\/\/v.blog.sohu.com\/","http:\/\/tv.sohu.com\/","http:\/\/share.vrs.sohu.com\/","http:\/\/my.tv.sohu.com\/","http:\/\/player.56.com\/","http:\/\/www.56.com\/","http:\/\/kankanews.com\/","http:\/\/video6.smgbb.cn\/","http:\/\/www.youku.com\/","http:\/\/player.youku.com\/","http:\/\/static.youku.com\/","http:\/\/www.ku6.com\/","http:\/\/player.ku6.com\/","http:\/\/video.sina.com.cn\/","http:\/\/vhead.blog.sina.com.cn\/","http:\/\/you.video.sina.com.cn\/","http:\/\/video.qq.com\/","http:\/\/www.baidu.com\/","http:\/\/box.baidu.com\/","http:\/\/hi.baidu.com\/","http:\/\/mv.baidu.com\/","http:\/\/mvimg.baidu.com\/","http:\/\/mvideo.baidu.com\/","http:\/\/player.cntv.cn\/","http:\/\/player.xiyou.cntv.cn\/","http:\/\/www.yinyuetai.com\/","http:\/\/player.yinyuetai.com\/","http:\/\/www.aipai.com\/","http:\/\/www.cutv.com\/","http:\/\/player.cutv.com\/","http:\/\/www.pptv.com\/","http:\/\/v.pptv.com\/","http:\/\/www.letv.com\/","http:\/\/www.iqiyi.com\/","http:\/\/yule.iqiyi.com\/","http:\/\/player.video.qiyi.com\/","http:\/\/www.ifeng.com\/","http:\/\/s.v.ifeng.com\/","http:\/\/v.ifeng.com\/","http:\/\/www.m1905.com\/","http:\/\/www.joy.cn\/","http:\/\/client.joy.cn\/","http:\/\/www.molihe.com\/","http:\/\/mv.molihe.com\/","http:\/\/swf.molihe.com\/","http:\/\/www.baomihua.com\/","http:\/\/video.baomihua.com\/","http:\/\/www.ouou.com\/","http:\/\/flash.ouou.com\/","http:\/\/dv.ouou.com\/","http:\/\/misc.home.news.cn\/","http:\/\/www.news.cn\/","http:\/\/www.wasu.cn\/","http:\/\/play1.wasu.cn\/","http:\/\/play.wasu.cn\/","http:\/\/v.iask.com\/","http:\/\/i7.imgs.letv.com\/","http:\/\/static.video.qq.com\/","http:\/\/player.pptv.com\/","http:\/\/v.pps.tv\/","http:\/\/ipd.pps.tv\/","http:\/\/www.funshion.com\/","http:\/\/player.pps.tv\/","http:\/\/api.funshion.com\/","http:\/\/www.hunantv.com\/","http:\/\/video.brtn.cn","http:\/\/news.brtn.cn\/","http:\/\/life.brtn.cn\/","http:\/\/mil.brtn.cn\/","http:\/\/finance.brtn.cn\/","http:\/\/btv.brtn.cn\/","http:\/\/host.brtn.cn\/","http:\/\/zmbj.brtn.cn\/","http:\/\/www.brtn.cn\/","http:\/\/ent.brtn.cn\/","http:\/\/sports.brtn.cn\/","http:\/\/legal.brtn.cn\/","http:\/\/tv.brtn.cn\/","http:\/\/iptv.brtn.cn\/","http:\/\/yst.brtn.cn\/","http:\/\/pxgw.brtn.cn\/","http:\/\/zcmx.brtn.cn\/","http:\/\/zhanbo.brtn.cn\/","http:\/\/app.brtn.cn\/","http:\/\/search.brtn.cn\/","http:\/\/itv.brtn.cn\/","http:\/\/www.meipai.com\/","http:\/\/www.acfun.tv\/","https:\/\/ssl.acfun.tv\/","http:\/\/m.acfun.tv\/","http:\/\/www.bilibili.com\/","http:\/\/share.acg.tv\/","http:\/\/static.hdslb.com\/","http:\/\/bangumi.bilibili.com"],"is_readonly":0,"can_local_upload":null,"paypost":"1","music_num":10,"attachment_num":5,"attachment_size":209715200,"long_editor":false,"float_editor":"","custom_emotion":false,"emotion_transform":false,"tb_gram":false,"formula_editor":""});
});
}
	_.Module.use('ueditor/widget/ueditor_base');
_.Module.use('ueditor/widget/ueditor_extend_base');
_.Module.use('ueditor/widget/background', [UE, EditorUI]);
_.Module.use('ueditor/widget/auto_link', [UE, EditorUI]);
_.Module.use('ueditor/widget/picture', [UE, EditorUI, {
	props: {
		'103':[]	}
}]);
_.Module.use('ueditor/widget/emotion', [UE, EditorUI]);
_.Module.use('ueditor/widget/video', [UE, EditorUI, {
	is_video_pgc_user: 0}]);
_.Module.use('ueditor/widget/scrawl', [UE, EditorUI]);
        _.Module.use('ueditor/widget/jquery_caret');
    _.Module.use('ueditor/widget/topic', [UE, EditorUI]);
_.Module.use('ueditor/widget/topic_suggestion', [UE, EditorUI]);
    _.Module.use('ueditor/widget/fullscreen', [UE, EditorUI]);
_.Module.use('ueditor/widget/height_limit', [UE, EditorUI]);
_.Module.use('ueditor/widget/draft', [UE, EditorUI]);
_.Module.use('ueditor/widget/at', [UE, EditorUI]);
_.Module.use('ueditor/widget/counter', [UE, EditorUI]);
_.Module.use('ueditor/widget/word_limit', [UE, EditorUI]);
_.Module.use('encourage-thread/widget/setting', [UE, EditorUI, {
	scores: [],
	level : []}]);
_.Module.use('encourage-thread/widget/medal', [UE, EditorUI, {
	defaultBubble: [],
	level: 0}]);
_.Module.use('encourage-thread/widget/paypost', [UE, EditorUI, {
    isPaypost		: 0, 
    needPaypostAgree: !0}]);
_.Module.use("poster/widget/rich_poster", {
    prefix: undefined,
    hotTopic: '',//传递后台抓取话题
    // placeholder: '',
    feedback:'<p>温馨提示：反馈bug、帐号异常或删贴问题时，请提供文字形式的问题帐号（非截图）、问题发生的时间，并尽可能上传截图，以上信息有助于贴吧更好的解决您的问题。<\/p>',
    QinglangData: {"qingLangExtType":"","title":"","content":""},
    ImgNum: 50,
    user: {
        memberLevel : 0,
        user_nickname: ''
    },
    blockInfo: {
        is_block : 0,
        block_reason:'',
        opgroup : '',
        days_tofree:0,
    },
    snowflow: {
        img : '',
        url : ''
    },
    pagelet: pagelet,
    initPage: 'frs'
});
    _.Module.use('forum/widget/focus_btn', [{
        'islike': '0',
        'levelId': '1',
        'levelName': '',
        'userLevel': null,
        'isCategoryOfGame': true,
        'firstClass': '动漫',
        'forumVdir': null,
        'isBawu': null    }]);
    _.Module.use('forum/pagelet/focus_btn', [pagelet], function () {});
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('navigation/widget/tbnav_bright', [
        $('#tb_nav'),
        {
            jq_search: $('#tb_nav').find('.j_search_internal_forum'),
            forumName: '海贼王'
        },
        {
            promotion_setting: [[]]        }
    ]);
    var closeTip = document.getElementById('corezoneX');
    if(closeTip) {
		closeTip.onclick = function (){
           document.getElementById('corezone').style.display='none';
		}
	}
    _.Module.use('navigation/widget/navigator', [pagelet, true], function (instance) {

    });
_.Module.use('tbui/widget/preview', [], function(){});
    _.Module.use('platform-activity/widget/fullWidthHead', [], function(){});
    _.Module.use('forum/widget/sign_mod', [$('#sign_mod'), {
        'hasClass': 1,
        'page': '',
        'isLike':0, // 是否已like本吧
        'isBlock':0, // 是否已封禁
        'isSignIn':0, // 今日是否已经签到
        'signForumInfo':{"is_on":true,"is_filter":false,"forum_info":{"forum_id":11772,"level_1_dir_name":"\u52a8\u6f2b"},"current_rank_info":{"sign_count":151920,"member_count":10121118,"sign_rank":1,"dir_rate":"0.1"},"yesterday_rank_info":{"sign_count":171883,"member_count":10120653,"sign_rank":1,"dir_rate":"0.1"},"weekly_rank_info":{"sign_count":173407,"member_count":10113101,"sign_rank":1},"monthly_rank_info":{"sign_count":0,"member_count":0,"sign_rank":0},"level_1_dir_name":"\u52a8\u6f2b","level_2_dir_name":"\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1"},
        'memberTitle': '',
        'memberNumber': '10124066',
        'isActivitySign': '',
        'userProp': null    },
    {
        'sign_mod_tiptitle1': '签到经验奖励',
        'sign_mod_tiptitle2': '连续签到双倍经验',
        'sign_mod_tiptitle3': '加粗字体使用特权',
        'sign_mod_tiptitle4': '红色字体使用特权',
        'sign_mod_tiptitle5': '一举橙名',
        'sign_mod_tiptext1': '签到即奖励2个经验值。<br \/>手机签到额外奖励2个经验值。',
        'sign_mod_tiptext2': '连续签到奖励经验值双倍。',
        'sign_mod_tiptext3': '在本吧发贴时可以使用加粗字体。',
        'sign_mod_tiptext4': '在本吧发贴时可以使用红色字体。',
        'sign_mod_tiptext5': '在本吧用户ID橙名高亮显示。',
        'sign_mod_tipcondition1': '条件：每天点击签到后即可获得。',
        'sign_mod_tipcondition2': '条件：保持连续签到2天及以上。',
        'sign_mod_tipcondition3': '条件：连续签到10天及以上，不能中断哦',
        'sign_mod_tipcondition4': '条件：连续签到20天及以上，不能中断哦',
        'sign_mod_tipcondition5': '条件：连续签到30天及以上，不能中断哦',
        'sign_mod_card_title': '一键签到，最高<span>6倍经验！<\/span>',
        'sign_mod_card_detail': '',
        'sign_mod_card_positive_btn': '<i class=\"icon\"><\/i>客户端免费体验',
        'sign_mod_card_no_txt': '<i class=\"icon\"><\/i>会员一键签到',
    }]);
    _.Module.use('frs-list/widget/popup_zhang', [], function () {
    });
    _.Module.use('frs-list/pagelet/thread', [pagelet], function (instance) {

    });
window['__abbaidu_2027_subidgetf'] = function () {
    var subid = 'tb_pc_frs';
    return subid;
};
window['__abbaidu_2027_cb'] = function (responseData) {
    Object.keys(JSON.parse(responseData)).forEach(function (key) {
        document.cookie = 'st_' + key + '=' + JSON.parse(responseData)[key];
    });
};
;(function() {
  var hm = document.createElement("script");
  hm.src = "https://dlswbr.baidu.com/heicha/mw/abclite-2027-s.js";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})()
    _.Module.use('frs-aside/pagelet/base_aside', {
        forumName: "\u6d77\u8d3c\u738b",
        forumSecLvName: "\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1",
        brandAdsenseSwitch: 1    });
_.Module.use('tbui/widget/preview', [], function(){});
    _.Module.use('encourage-celebrity/widget/celebrity', {
        celebrity: {"celebrity_status":"2","fans_head_pic":"1430794372110.png","fans_name":"\u6d77\u8d3c\u56e2","fans_tail_pic":"1429754794434.png","npc_info":[{"cur_level":75,"level_id":16,"level_name":"\u718a\u732b\u4eba","npc_avatar":"tb.1.8b5a06b8.gp5LUNHVfIez8ISnTlbkUQ","npc_fans_name":"\u6d77\u8d3c\u56e2","npc_id":1337628265,"npc_name":"\u8def\u98de","npc_rank":1,"npc_vip_level":0,"props_id":"1010101","props_title":"\u8def\u98de\u53d1\u8d34\u6c14\u6ce1"}]},
        isCelebrityForum: true,
        user: {"is_login":false,"Parr_scores":null,"mParr_props":null},
        forum: {"forum_id":11772,"forum_name":null},
        isCurForumMember: false,
        memberLastDays: 0    });
    _.Module.use('encourage-celebrity/widget/celebrity_expball', {"pageData":{"Parr_scores":null,"Parr_props":null,"forum":{"forum_id":11772,"forum_name":"\u6d77\u8d3c\u738b","dir_info":{"level_1_name":"\u52a8\u6f2b","level_2_name":"\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1"},"kw":"\u6d77\u8d3c\u738b","title":"\u6d77\u8d3c\u738b\u5427-\u767e\u5ea6\u8d34\u5427--\u4e0d\u7ba1\u5728\u8d34\u5427\u7684\u54ea\u4e2a\u89d2\u843d\uff0c\u6d77\u5427\u662f\u4f60\u575a\u5f3a\u7684\u540e\u76fe--\u8fd9\u91cc\u6709\u8fc7\u7535\u53f0\uff0c\u542c\u6d77\u5427DJ\u5728\u7535\u53f0\u91cc\u8bf4\u5b66\u9017\u5531\uff1b\u8fd9\u91cc\u6709\u8fc7\u4e3a\u4e86\u7533\u8bf7\u5bb6\u65cf\u7684\u6597\u4e89\uff0c\u4f17\u4eba\u7684\u56e2\u7ed3\u8ba9\u6d77\u5427\u7ec8\u4e8e\u80fd\u8fdb\u5165\u4e86\u767e\u5ea6\u5bb6\u65cf\uff1b\u8fd9\u91cc\u6709\u8fc7\u8fa9\u8bba\u8d5b\uff0c\u770b\u5427\u53cb\u600e\u6837\u5507\u67aa","description":"\u672c\u5427\u70ed\u5e16: 1-\u5916\u884c\u5458\u5403\u76f8\u771f\u662f\u8d8a\u6765\u8d8a\u96be\u770b\u4e86 2-\u6d77\u8d3c\u738b\u5b98\u65b9\u827e\u65af\u5c0f\u8bf4\u6f2b\u753b\u7b2c1\u8bdd\u6c49\u5316\uff1a\u9ed1\u6843\u6d77\u8d3c\u56e2\u6210\u7acb 3-\u8fd9\u4e48\u591a\u5e74\u4e86\uff0c\u6b66\u88c5\u8272\u786c\u5316\u90fd\u662f\u7537\u4eba\u5728\u7528\uff0c\u5973\u7684\u4e0d\u80fd\u5b66\u5417\uff1f\u5973\u751f\u672c\u6765\u8eab 4-\u51ef\u591a\u4e09\u707e\u7684\u60c5\u62a5\u8fd9\u4e48\u5dee\u5417\uff1f\u4eba\u5bb6\u7d22\u9686\u597d\u6b79\u4e5f\u662f\u7f6a\u6076\u4e00\u4ee3\u7684\u8d85\u65b0\u661f\uff0c\u5c45 5-\u5404\u4f4d\u5c71\u9ed1\uff0c\u5c71\u6cbb\u4f1a\u6b66\u88c5\u8272\u54e6\uff0c\u6b66\u88c5\u8272\u4f1a\u53d8\u9ed1\u54e6\u3002 6-\u3010Grand News\u3011\u7b2c\u56db\u767e\u4e00\u5341\u4e5d\u671f\u300a\u5b64\u7acb\u65e0\u63f4\u300b 7-\u6d77\u8d3c\u738b990\u8bdd\u300a\u5b64\u7acb\u65e0\u63f4\u300b\uff08\u8ba8\u8bba\u5206\u6790\uff0c\u611f\u60f3\u9884\u6d4b\u697c\uff09","keywords":"\u6d77\u8d3c\u738b,\u52a8\u6f2b\u00b7\u8f7b\u5c0f\u8bf4\u4f5c\u54c1,\u52a8\u6f2b,\u98ce\u534e,\u65b0\u4e16\u754c\u676f","is_private_forum":0},"user":{"is_login":false,"user_id":0,"user_name":"","no_un":false,"mobile":"","email":"","is_new_user":1,"portrait":"00000000","start_time":1600683657}}}, function (expball) {
        var $voteNum = $('.j_vote_num');
        expball.setCallback(function (data) {
            $voteNum.html(+$voteNum.html() + (data['add_vote_num'] || 0));
        });
    });
    _.Module.use('frs-aside/widget/forum_info', [
        1,
        0,
        PageData.forum,
        {
            is_block: 0,
            block_reason: '',
            opgroup: '',
            days_tofree:0,
        },
        false    ]);
    _.Module.use('frs-aside/widget/zyq');
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.getInstance('encourage-tbguess/widget/mixin', function (mixin) {
        mixin.bindData({"mineGuessInfo":{"count":0,"bean":0,"scores":{"total":0,"money":0,"other":0}},"homeForum":"\u7ade\u6280\u4f53\u80b2","mineAwardMap":[]});
    });
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('adsense-base/widget/tpl_ext', [{
        'type': 'POST',
    }]);
    // TODO 多次加载白名单，需要优化
    _.Module.use('adsense-base/widget/loader', [{
        'whiteList':[["http:\/\/fedev.baidu.com"],["http:\/\/jiaoyu.baidu.com"],["http:\/\/caifu.baidu.com"],["http:\/\/jiankang.baidu.com"],["http:\/\/tieba.dre8.com"],["http:\/\/tdsp.nuomi.com"],["http:\/\/baiju.baidu.com"],["http:\/\/temai.baidu.com"],["http:\/\/tieba.baidu.com"],["http:\/\/zt.chuanke.com"],["http:\/\/window.sturgeon.mopaas.com"],["http:\/\/api.union.vip.com"],["http:\/\/api.dongqiudi.com"],["http:\/\/www.chuanke.com"],["http:\/\/dcp.kuaizitech.com\/"]],
        'adValue':""    }]);
    _.Module.use('frs-list/widget/util_pager', [pagelet, true]);
    _.Module.use('frs-list/pagelet/thread_list', [], function (instance) {
        instance.init({
            pagelet: pagelet,
            ifCheck: null,
            videoAutoPlay: true,
            is_zone_forum:  0,
        })
    });
</script>
</body>
</html>


Process finished with exit code 0

'''

# rpat = '<a rel="noreferrer" href="(.*)" title=".*" target="_blank" class="j_th_tit ">.*</a>'
# list_pat = re.findall(rpat,html_str)
# print(list_pat)
# list_url = []
# for i in list_pat:
#     new_url = 'https://tieba.baidu.com' + i
#     list_url.append(new_url)
# print(list_url)

# rpat = '<img src="" attr="\d+?" data-original=".*"  bpic="(.*)" class="threadlist_pic j_m_pic "  />'
# list_pat1 = re.findall(rpat,html_str)
# for i in new_url:
#     bimg = requests.get(i,headers).content
#     with open(i[-8:]+'.jpg','wb+') as f:
#         f.write(bimg)