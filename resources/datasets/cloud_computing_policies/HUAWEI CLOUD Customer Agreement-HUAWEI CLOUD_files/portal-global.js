var BO = { wekit: true, Chrome: false, Safari: false, Firefox: false, Opera: false, IE: false, oldIE: false, newIE: false, iDevice: false, iPhone: false, iPad: false, android: false, name: "unkonwn", version: "" }; (function () { "use strict"; var uaInfo = navigator.userAgent; BO.getUAInfo = function () { return uaInfo }; BO.init = function () { BO.detectBrowser(); BO.detectDevice() }; BO.detectBrowser = function () { var regF = /Firefox[\/\s](\d+\.\d+)/, regO = /Opera|OPR[\/\s](\d+\.\d+)/, regI = /MSIE[\/\s](\d+\.\d+)/, regC = /Chrome[\/\s](\d+\.\d+)/, regS = /Safari[\/\s](\d+\.\d+)/, regIn = /rv[\:\s](\d+\.\d+).*like Gecko/; BO.Firefox = regF.test(uaInfo); BO.Opera = regO.test(uaInfo); BO.Chrome = regC.test(uaInfo); BO.Safari = !BO.Chrome && regS.test(uaInfo); BO.newIE = regIn.test(uaInfo); BO.IE = BO.newIE || regI.test(uaInfo); BO.oldIE = BO.IE && !BO.newIE && Number(uaInfo.match(regI)[1]) < 9; var regSV = /Version\/(\d+.\d+.\d+)/; BO.Chrome && (BO.name = "Chrome") && (BO.version = uaInfo.match(regC) && uaInfo.match(regC)[1]); BO.Firefox && (BO.name = "Firefox") && (BO.version = uaInfo.match(regF) && uaInfo.match(regF)[1]); BO.Safari && (BO.name = "Safari") && (BO.version = uaInfo.match(regSV) && uaInfo.match(regSV)[1]); BO.Opera && (BO.name = "Opera") && (BO.version = uaInfo.match(regO) && uaInfo.match(regO)[1]); BO.IE && (BO.name = "IE") && (BO.version = BO.newIE ? uaInfo.match(regIn) && uaInfo.match(regIn)[1] : (uaInfo.match(regI) && uaInfo.match(regI))[1]); BO.webkit = !(BO.Firefox || BO.Opera || BO.IE) }; BO.detectDevice = function () { var ua = uaInfo.toLowerCase(); BO.android = ua.indexOf("android") > -1; /iPad/i.test(uaInfo) && (BO.iPad = true) && (BO.iDevice = true); /iPhone|iPod/i.test(uaInfo) && (BO.iPhone = true) && (BO.iDevice = true) } })(); !function (global, factory) { if (typeof exports === "object" && typeof module !== "undefined") { module.exports = factory() } else if (typeof define === "function" && define.amd) { define([], factory) } else { global.observer = factory() } }(typeof window !== "undefined" ? window : this, function () { function Observer(initData) { this.data = null; this.oldData = null; this.subscribers = {}; this.anonymous = []; if (typeof initData !== "undefined") { this.publish(null, initData) } } Observer.prototype.subscribe = function (name, callback) { if (name === null) { this.anonymous.push(callback) } else { this.subscribers[name] = callback } if (this.data !== null) { callback.call(this, this.data) } return this }; Observer.prototype.unsubscribe = function (name) { if (this.subscribers[name] !== undefined) { delete this.subscribers[name] } return this }; Observer.prototype.publish = function (name, data) { this.oldData = this.data; this.data = data; for (var key in this.subscribers) { if (name === null || name !== key) { this.subscribers[key].call(this, data) } } for (var i = 0; i < this.anonymous.length; i++) { this.anonymous[i].call(this, data) } return this }; Observer.prototype.getData = function () { return this.data }; Observer.prototype.getOldData = function () { return this.oldData }; var observers = {}; var observer = function (observerName, init, initData) { var instance = observer.get(observerName); if (instance) { return instance } else if (init) { return observer.init(observerName, initData) } }; observer.get = function (observerName) { return observers[observerName] }; observer.init = function (observerName, initData) { return observers[observerName] = new Observer(initData) }; observer.constructor = Observer; return observer }); $.fn.scrollUnique = function () { return $(this).each(function () { var eventType = "mousewheel"; if (document.mozHidden !== undefined) { eventType = "DOMMouseScroll" } $(this).on(eventType, function (event) { var scrollTop = this.scrollTop, scrollHeight = this.scrollHeight, height = this.clientHeight; if ("wheelDeltaX" in event.originalEvent && event.originalEvent.wheelDeltaX !== 0) return; if ("deltaX" in event.originalEvent && event.originalEvent.deltaX !== 0) return; if ("axis" in event.originalEvent && event.originalEvent.axis === event.originalEvent.HORIZONTAL_AXIS) return; var delta = event.originalEvent.wheelDelta ? event.originalEvent.wheelDelta : -(event.originalEvent.detail || 0); delta = delta / 5; if (delta > 0 && scrollTop <= delta || delta < 0 && scrollHeight - height - scrollTop <= -1 * delta) { this.scrollTop = delta > 0 ? 0 : scrollHeight; event.preventDefault() } }) }) }; (function () { var lastTime = 0; var vendors = ["webkit", "moz"]; for (var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) { window.requestAnimationFrame = window[vendors[x] + "RequestAnimationFrame"]; window.cancelAnimationFrame = window[vendors[x] + "CancelAnimationFrame"] || window[vendors[x] + "CancelRequestAnimationFrame"] } if (!window.requestAnimationFrame) { window.requestAnimationFrame = function (callback, element) { var currTime = (new Date).getTime(); var timeToCall = Math.max(0, 16.7 - (currTime - lastTime)); var id = window.setTimeout(function () { callback(currTime + timeToCall) }, timeToCall); lastTime = currTime + timeToCall; return id } } if (!window.cancelAnimationFrame) { window.cancelAnimationFrame = function (id) { clearTimeout(id) } } })(); jQuery.extend(jQuery.easing, { easeOutSine: function (x, t, b, c, d) { return c * Math.sin(t / d * (Math.PI / 2)) + b } }); $(function () { BO.init(); BO.oldIE && $("body").addClass("oldIE"); BO.iDevice && $("body").addClass("Mobile"); if (BO.oldIE && !localStorage.getItem("hideCompatible")) { $("body").addClass("Compatible") } var win_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth, win_height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight; var $frame = $("body"); $(window).scroll(function (event) { if (!$("#header").hasClass("loaded")) { return } var currTop = $(window).scrollTop(); if (currTop <= 30) { $frame.removeClass("scrolled") } else { $frame.addClass("scrolled") } if (currTop > win_height) { $(".float-sidebar").addClass("show-totop") } else { $(".float-sidebar").removeClass("show-totop") } $(".float-sidebar").removeClass("show") }); if (win_width < 1024) { $(".float-sidebar").on("click", ".shown-btn", function (event) { $(this).closest(".float-sidebar").addClass("show") }); $(".icons-float-bar").click(function (e) { window.open("https://www.huaweicloud.com/intl/en-us/contact-sales.html") }); $(document).bind("click", function (e) { if ($(e.target).closest(".float-bar-nav").length == 0 && $(e.target).closest(".sub-nav-layer").length == 0 && $(e.target).closest("#open").length == 0) { $(".sub-nav-layer").removeClass("float-expand") } }); $(".help-header").addClass("hide") } var $header = $("#header"); function setSubNav() { $(".subnav-layer").each(function (index, el) { $(this).css("top", $(this).height() * -1) }) } headerFun(); function headerFun() { $header.addClass("loaded"); $(".compatibility .close-large").on("click", function (event) { $("body").removeClass("Compatible"); localStorage.setItem("hideCompatible", true) }); $(".my-account").on("click", ".my-acct", function (event) { $(this).closest("#header").toggleClass("logined") }); $(window).scroll() } $(".code-2-box").hover(function () { $(this).addClass("show").siblings(".code-2-box").removeClass("show") }, function () { }); $frame.on("click", 'a[href="#toTop"]', function (event) { event.stopPropagation(); $("body,html").stop().animate({ scrollTop: 0 }, 500, "easeOutSine", function () { href_click = false }) }); $frame.on("click", 'a[href^="#"]', function (event) { event.preventDefault(); var headerHeight = $("#header").height(); var target = $(this).attr("href").substr(1); var top = 0; if ($("#" + target).length > 0) { top = $("#" + target).offset().top - headerHeight } else if ($("[name='" + target + "']").length > 0) { top = $("[name='" + target + "']").offset().top - headerHeight } $("body,html").stop().animate({ scrollTop: top }, 500, "easeOutSine", function () { href_click = false }) }); $(".js-title").each(function (index, el) { if (el.offsetWidth < el.scrollWidth) { $(el).attr("title", $.trim($(el).text())) } }); var lang = $("html").attr("lang") ? $("html").attr("lang").toLowerCase() : null; var service = encodeURIComponent(window.location.href); var registerUrl = "https://reg.huaweicloud.com/registerui/intl/register.html?" + (lang ? "locale=" + lang : "") + "&service=" + service + "&hwid=portal"; $("#header .header-register>a").attr("href", registerUrl); !function () { var $register = $(".register-area"); if ($register.length === 0) return; var $registerBg = $(".register-area-bg"); var registerHeight = $register.outerHeight(); var maxBgMoveLength = $registerBg.outerHeight() - registerHeight; var maxDiff = $("body").height() - $register.offset().top; var moveRatio = maxBgMoveLength / maxDiff; var setBgPosition = function () { var offset = $register.offset(); var topToWindow = offset.top - $(window).scrollTop(); var windowHeight = $(window).height(); var diff = windowHeight - topToWindow; var bgMoveLength = moveRatio * diff; bgMoveLength = bgMoveLength < 0 ? 0 : bgMoveLength; bgMoveLength = bgMoveLength > maxBgMoveLength ? maxBgMoveLength : bgMoveLength; $registerBg.css("margin-bottom", -bgMoveLength + "px") }; setBgPosition(); $(window).scroll(function () { setBgPosition() }) }(); function setParms(args) { var parms = {}, newParms = "?"; var query = location.search.substring(1).split("&"); for (var i = 0; i < query.length; i++) { var pos = query[i].split("="); if (pos[0]) { parms[pos[0]] = pos[1] ? pos[1] : "" } } if (!args) { return parms } for (var argKey in args) { for (var parmskey in parms) { if (argKey === parmskey) { parms[parmskey] = args[parmskey]; break } } parms[argKey] = args[argKey] } for (var key in parms) { if (key == "locale") { continue } newParms += key + "=" + parms[key] + "&" } return newParms.substring(0, newParms.length - 1) } window.changeLang = window.changeLang || function (lang) { function setCookie(name, value, expiredays) { var exdate, cookieString; exdate = new Date; exdate.setDate(exdate.getDate() + expiredays); cookieString = name + "=" + escape(value) + (expiredays === null ? "" : ";expires=" + exdate.toGMTString()) + ";path=/;" + "domain=.huaweicloud.com;"; document.cookie = cookieString } var href = window.location.href; var origin = window.location.origin; var pathname = window.location.pathname; var hash = window.location.hash; var current_lang = $("html").attr("lang").toLowerCase(); var start_lang = current_lang; var end_lang = lang; var index = origin.replace("activity-intl", "intl") + "/" + end_lang + "/"; var url = ""; if (index) { $.ajax({ url: index, type: "get", success: function () { index = index }, error: function () { index = "https://intl.huaweicloud.com/" } }) } else { index = "https://intl.huaweicloud.com/" } if (pathname.indexOf(start_lang) === 1) { url = href.replace(start_lang, end_lang).replace(/locale=[A-Za-z0-9_-]{5}/gi, "locale=" + end_lang) } else { var pathnameLang = pathname.split("/")[1]; if (pathnameLang == "zh-cn" || pathnameLang == "en-us" || pathnameLang == "es-us" || pathnameLang == "pt-br") { url = origin + "/" + end_lang + pathname.replace("/" + pathnameLang, "") + hash } else { url = origin + "/" + end_lang + pathname + hash } } setCookie("locale", lang, 30); if (url) { $.ajax({ url: url, type: "get", success: function () { window.location.href = url }, error: function () { window.location.href = index } }) } else { window.location.href = index } }; function initFloatDialog() { try { function getCookie(name) { var arr = document.cookie.replace(/\s/g, "").split(";"); for (var i = 0; i < arr.length; i++) { var tempArr = arr[i].split("="); if (tempArr[0] === name) { return decodeURIComponent(tempArr[1]) } } return undefined } function setCookie(name, value, expiredays) { var exdate, cookieString; exdate = new Date; exdate.setDate(exdate.getDate() + expiredays); cookieString = name + "=" + escape(value) + (expiredays === null ? "" : ";expires=" + exdate.toGMTString()) + ";path=/;" + "domain=.huaweicloud.com;"; document.cookie = cookieString } var currentData = (new Date).getMonth() + "0" + (new Date).getDay(); var dialogUrl = "https://www.huaweicloud.com/intl/en-us/common/float-dialog-page-hk.html?" + currentData; var currentUrl = location.href; if (currentUrl.indexOf("/intl/pt-br") > -1 || currentUrl.indexOf("/intl/es-us") > -1) { return } if (location.href.indexOf("/content/") > -1) { dialogUrl = location.origin + "/content/cloudbu-site/hk/en-us/common/float-dialog-page-hk.html?" + currentData } var tocList1 = { "/content/cloudbu-site/hk/en-us/activity/": "activity.huaweicloud.com/intl/en-us/", "/content/cloudbu-site/hk/en-us/support/": "support.huaweicloud.com/intl/en-us/", "/content/cloudbu-site/hk/en-us/": "www.huaweicloud.com/intl/en-us/", "/content/cloudbu-site/hk/zh-cn/activity/": "activity.huaweicloud.com/intl/zh-cn/", "/content/cloudbu-site/hk/zh-cn/support/": "support.huaweicloud.com/intl/zh-cn/", "/content/cloudbu-site/hk/zh-cn/": "www.huaweicloud.com/intl/zh-cn/" }; if (currentUrl.indexOf("/content") > -1) { for (var key in tocList1) { currentUrl = currentUrl.replace(window.location.hostname + (window.location.port ? ":" + window.location.port : ""), "").replace(key, tocList1[key]) } } var container = document.createElement("div"); var showBottomAd = true; $.ajax({ url: dialogUrl, async: false, timeout: 1e4, success: function (data) { container.innerHTML = data; var insertItem = ""; var insertBottomAD = ""; var insertTopAD = ""; var urlLength = 0; $(container).find(".float-sidebar").each(function (index, item) { var $this = $(item); var rangUrls = $this.attr("range") ? $this.attr("range").split(";") : []; var unRangeUrls = $this.attr("unrange") ? $this.attr("unrange").split(";") : []; var isShow = true; unRangeUrls.forEach(function (item2) { if (currentUrl.indexOf(item2) > -1) { isShow = false } }); if (isShow) { rangUrls.forEach(function (item1) { if (currentUrl.indexOf(item1) > -1 || $this.attr("range") == "default") { insertItem = item1.length > urlLength ? item : insertItem; urlLength = item1.length > urlLength ? item1.length : urlLength } try { if ($this.attr("range") == "homeindex" && window.location.host == "www.huaweicloud.com" && (window.location.pathname == "/" || window.location.pathname == "/index.html")) { insertItem = item; return } } catch (error) { } }) } }); urlLength = 0; $(container).find(".tm-adv-space").each(function (index, item) { var $this = $(item); if (getCookie($this.attr("ahref")) && getCookie($this.attr("ahref")) >= ($this.attr("times") || 3)) { showBottomAd = false; return false } }); if (showBottomAd) { $(container).find(".tm-adv-space").each(function (index, item) { var $this = $(item); if (getCookie($this.attr("ahref")) < $this.attr("times") || 3) { var rangUrls = $this.attr("range") ? $this.attr("range").split(";") : []; var unRangeUrls = $this.attr("unrange") ? $this.attr("unrange").split(";") : []; var isShow = true; unRangeUrls.forEach(function (item2) { if (currentUrl.indexOf(item2) > -1) { isShow = false } }); if (isShow) { rangUrls.forEach(function (item1) { if (currentUrl.indexOf(item1) > -1) { var adContent = '<div class="tm-adv-space-content" bi_name="bottom-ad-mb" style="background:url(' + $this.attr("abg") + ');background-size:100% 100%;"><div class="tm-adv-space-content-close"><i class="tm-adv-space-content-close__icon"></i></div><a target="_blank" href="' + $this.attr("ahref") + '" class="tm-adv-space-content__main"><div class="tm-adv-space-content__title">' + ($this.attr("atitle") || "") + '</div><div class="tm-adv-space-content__desc">' + ($this.attr("adesc") || "") + "</div></a>" + ($this.attr("abtn") ? '<div class="tm-adv-space-btn"><a target="_blank" href="' + $this.attr("ahref") + '" class="tm-adv-space-btn__inner">' + $this.attr("abtn") + "</a></div>" : "") + "</div>"; $this.append(adContent); insertBottomAD = item1.length > urlLength ? $this : insertBottomAD; urlLength = item1.length > urlLength ? item1.length : urlLength } try { if ($this.attr("range") == "homeindex" && window.location.host == "www.huaweicloud.com" && (window.location.pathname == "/" || window.location.pathname == "/index.html")) { insertBottomAD = $this; return } } catch (error) { } }) } } }) } if (!$("body").hasClass("showPrompt") && !getCookie("header-top-ad-hk")) { urlLength = 0; $(container).find(".prompt-content.header-top-ad").each(function (index, item) { var $this = $(item); var rangUrls = $this.attr("range") ? $this.attr("range").split(";") : []; var unRangeUrls = $this.attr("unrange") ? $this.attr("unrange").split(";") : []; var isShow = true; unRangeUrls.forEach(function (item2) { if (currentUrl.indexOf(item2) > -1) { isShow = false } }); if (isShow) { rangUrls.forEach(function (item1) { if (currentUrl.indexOf(item1) > -1) { var adContent = '<a href="' + $this.attr("adurl") + '" target="blank" bi_name="top-ad" class="top-ad"><img class="img1" src="' + $this.attr("adbg") + '"><img class="img2" src="' + $this.attr("adbg2") + '"><img class="img3" src="' + $this.attr("adbg3") + '"><i bi_name="top-ad-close"></i><style>.header-top-ad img {width: auto;height: 100%;margin: 0 auto;position: absolute;left: 50%;transform: translate(-50%,0);max-width: inherit;}</style></a>'; $this.html(adContent); insertTopAD = item1.length > urlLength ? $this : insertTopAD; urlLength = item1.length > urlLength ? item1.length : urlLength } try { if ($this.attr("range") == "homeindex" && window.location.host == "www.huaweicloud.com" && (window.location.pathname == "/" || window.location.pathname == "/index.html")) { insertTopAD = $this; return } } catch (error) { } }) } }); $(".header-topnav").after(insertTopAD); if (insertTopAD.length > 0) { if ($("html").attr("lang") !== "en-US") { $("body").addClass("showPrompt"); $("#header").addClass("showPrompt") } $("#header").addClass("top-ad-height") } } $("#footer").append(insertBottomAD); $("#footer").append(insertItem); if (typeof afterFooterSidebar === "function") { afterFooterSidebar() } }, error: function (XMLHttpRequest, textStatus, errorThrown) { console.log(XMLHttpRequest.status, XMLHttpRequest.readyState, textStatus) } }); $(".prompt-content .top-ad i").on("click", function (e) { $(".header-top-ad").remove(); $("body").removeClass("showPrompt"); $("#header").removeClass("showPrompt"); $("#header").removeClass("top-ad-height"); if (!getCookie("header-top-ad-hk")) { setCookie("header-top-ad-hk", "hide", 1) } e.preventDefault(); e.stopPropagation(); return }); $(".icons-float-bar").click(function (e) { $(".sub-nav-layer").toggleClass("float-expand"); if (window.screen.width < 1024) { e.preventDefault() } }); $(".nps-score-btns p").on("click", function () { var $this = $(this); $this.siblings().removeClass("active"); $this.addClass("active") }); $(".float-config-nps .por-textarea").blur(function () { $(".float-config-nps").removeClass("active") }); $(".float-config-nps .por-textarea").focus(function () { $(".float-config-nps").addClass("active") }); $(".float-config-nps .por-textarea").on("input", function () { $(".float-config-nps .por-textarea-word").text($(this).val().length) }); $(".tm-adv-space-content-close").on("click", function () { var $this = $(this); var adKey = $this.parents(".tm-adv-space").attr("ahref"); $(this).parents(".tm-adv-space").remove(); var times = getCookie(adKey) ? getCookie(adKey) : 0; setCookie(adKey, ++times, 1) }); $(".tm-adv-space-content a").on("click", function (e) { var $this = $(this); if ($this.attr("href").indexOf("/login") > -1 && window.portalLogin) { portalLogin(encodeURIComponent(window.location.href), "zh-cn"); e.preventDefault() } else if ($this.attr("href").indexOf("/register") > -1 && window.portalRegister) { portalRegister(encodeURIComponent(window.location.href), "zh-cn"); e.preventDefault() } else if ($this.attr("href").indexOf("/realNameAuth") > -1 && window.portalrealNameAuthing) { portalrealNameAuthing(encodeURIComponent(window.location.href), "zh-cn"); e.preventDefault() } }) } catch (error) { } } $(window).load(function () { initFloatDialog() }) });
// Cookie Settings
$(function () {
	var lang = $("html").attr("lang") || 'en-us';
	var site = $("html").attr("site") || 'hk';
	var currLang = lang.toLowerCase();
    site = site.toLowerCase();
	var floatTextObj = {
		'en-us': {
			'information': 'We use cookies on the site, including third party cookies, in order for the site to work properly and to analyse traffic,offer enhanced functionality, social media features,and personalies content and ads.<a href="https://www.huaweicloud.com/intl/en-us/declaration/sa_cookies.html" target="_blank" class="por-link">Learn more</a>',
			'accept': 'ACCEPT COOKIES',
			'settings': 'COOKIES SETTINGS'
		},
		'th-th':{
			'information': 'เว็บไซต์นี้ใช้คุกกี้<br/>เราใช้คุกกี้บนเว็บไซต์นี้ รวมถึงคุกกี้ของบุคคลที่สาม เพื่อให้เว็บไซต์ทำงานได้อย่างถูกต้องและเพื่อวิเคราะห์การเข้าชมเว็บไซต์ เพิ่มประสิทธิภาพการทำงาน ฟีเจอร์อื่น ๆ บนโซเชียลมีเดีย รวมถึงข้อมูลส่วนบุคคลและโฆษณาต่าง ๆ <a href="https://www.huaweicloud.com/intl/en-us/declaration/sa_cookies.html" target="_blank" class="por-link">เรียนรู้เพิ่มเติม</a>',
			'accept': 'ยอมรับคุกกี้',
			'settings': 'การตั้งค่าคุกกี้'
		}
	}
	if(!floatTextObj[currLang]){
		currLang = 'en-us';
	}
    var floatDialog = '<div class="float-cookie-dialog">';
    floatDialog += '<div class="cookie-information">';
    floatDialog += '    <div>';
    floatDialog += 		floatTextObj[currLang].information
    floatDialog += '    </div>';
    floatDialog += '</div>';
    floatDialog += '<div class="cookie-btn-group">';
    floatDialog += '    <a class="por-btn por-btn-primary-light">'+ floatTextObj[currLang].accept +'</a>';
    floatDialog += '    <a class="por-btn por-btn-light">'+ floatTextObj[currLang].settings +'</a>';
    floatDialog += '</div>';
    floatDialog += '    </div>';

    var cookieModal = '<div class="por-modal" data-hide="modal" id="cookie-setting-modal">';
    cookieModal += '    <div class="por-modal-dialog">';
    cookieModal += '        <div class="por-modal-inner">';
    cookieModal += '            <div class="por-modal-head">';
    cookieModal += '                <div class="por-modal-title">Cookies Preference Center</div>';
    cookieModal += '            </div>';
    cookieModal += '            <div class="por-modal-body">';
    cookieModal += '                <div class="por-modal-text">';
    cookieModal += '                    <div class="por-tab-container combination cf">';
    cookieModal += '                        <div class="por-tab por-scrollbar-s">';
    cookieModal += '                            <ul>';
    cookieModal += '                                <li class="active">';
    cookieModal += '                                    <a>';
    cookieModal += '                                        <div class="por-tab-text">Your Privacy</div>';
    cookieModal += '                                    </a>';
    cookieModal += '                                </li>                                    ';
    cookieModal += '                                <li>';
    cookieModal += '                                    <a>';
    cookieModal += '                                        <div class="por-tab-text">Essential Cookies</div>';
    cookieModal += '                                    </a>';
    cookieModal += '                                </li>';
    cookieModal += '                                <li>';
    cookieModal += '                                    <a>';
    cookieModal += '                                        <div class="por-tab-text">Analytics Cookies</div>';
    cookieModal += '                                    </a>';
    cookieModal += '                                </li>';
    cookieModal += '                                <li>';
    cookieModal += '                                    <a>';
    cookieModal += '                                        <div class="por-tab-text">Advertising Cookies</div>';
    cookieModal += '                                    </a>';
    cookieModal += '                                </li>';
    cookieModal += '                                <li>';
    cookieModal += '                                    <a>';
    cookieModal += '                                        <div class="por-tab-text">More Information</div>';
    cookieModal += '                                    </a>';
    cookieModal += '                                </li>';
    cookieModal += '                            </ul>';
    cookieModal += '                        </div>';
    cookieModal += '                        <div class="por-tab-wrapper">';
    cookieModal += '                            <div class="por-tab-content active">';
    cookieModal += '                                <div class="por-collapse-container">';
    cookieModal += '                                    <a class="por-collapse-trigger expended" data-toggle="por-collapse">';
    cookieModal += '                                        <div class="por-collapse-head-text">Your Privacy</div>';
    cookieModal += '                                        <i class="por-icon por-icon-down"></i>';
    cookieModal += '                                    </a>';
    cookieModal += '                                    <div class="por-collapse show">';
    cookieModal += '                                        <div class="collapse-inner por-scrollbar-s">';
    cookieModal += '                                            <dl>';
    cookieModal += '                                                <dt class="por-text-title-t7">Your Privacy</dt>';
    cookieModal += '                                                <dd>';
    cookieModal += '                                                We use cookies on this website. To learn in detail about how we use cookies, please read our full Cookie Policy.<br/>';
    cookieModal += '                                                Our cookies setting is by default "inactive" apart from the essential cookies. To keep the current setting, simply click "Save and Close" below. You can also click “Accept Cookies” to activate all non-essential cookie groups.<br/>';
    cookieModal += '                                                To accept or deactivate cookies by category, simply click on the tabs to the left, then set your preference in the upper right corner and finally click "Save and Close" below.<br/>';
    cookieModal += '                                                You can revisit and change your settings at any time. Such change will not affect the lawfulness of the processing activities based on the consent and prior to such change.';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                        </div>                                            ';
    cookieModal += '                                    </div>';
    cookieModal += '                                </div>';
    cookieModal += '                                ';
    cookieModal += '                            </div>';
    cookieModal += '                            <div class="por-tab-content">';
    cookieModal += '                                <div class="por-collapse-container">';
    cookieModal += '                                    <a class="por-collapse-trigger" data-toggle="por-collapse">';
    cookieModal += '                                        <div class="por-collapse-head-text">Essential Cookies</div>';
    cookieModal += '                                        <i class="por-icon por-icon-down"></i>';
    cookieModal += '                                    </a>';
    cookieModal += '                                    <div class="por-collapse">';
    cookieModal += '                                        <div class="collapse-inner por-scrollbar-s">';
    cookieModal += '                                            <dl>';
    cookieModal += '                                                <dt class="por-text-title-t7"><span class="plain-text">Always Active</span>Essential Cookies</dt>';
    cookieModal += '                                                <dd>These cookies are necessary for the website to function and cannot be switched off in our systems.';
    cookieModal += '                                                    They are usually only set in response to actions made by you which amount to a request for services,';
    cookieModal += '                                                    such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies,';
    cookieModal += '                                                    but some parts of the site will not then work. These cookies do not store any personally identifiable information.       ';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                            <dl classs="cookie-used">';
    cookieModal += '                                                <dt class="por-text-title-t7">Cookies Used</dt>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">OneTrust Cookie Management Platform: </div> ';
    cookieModal += '                                                    cookies.js, OptanonConsent, OptanonAlertBoxClosed';
    cookieModal += '                                                </dd>                                                   ';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">Huawei:</div>';
    cookieModal += '                                                    JSESSIONID, CAS_THEME_NAME, VERSION_NO, ajaxUrl, scrollPercentage, HWSTORE-SESSION, ';
    cookieModal += '                                                    hwsso_uniportal, galleryConfigs, ';
    cookieModal += '                                                    20001_currentLanguage, 20017_currentLanguage,';
    cookieModal += '                                                    ae47714b02ca4de4bb1b101f320d3c89,';
    cookieModal += '                                                    RT, HWWAFSESID, awxxxx, qRCode, expiredTime, qrCodeCreateTime, cookieBannerOnOff, ';
    cookieModal += '                                                    cversion, HWWAFSESTIME, currentUrl, r-beta__sticky     ';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">Huawei Self-Service Platform Cookies:</div>';
    cookieModal += '                                                    JSESSIONID';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">Huawei Knowlege Base:</div>';
    cookieModal += '                                                    consumer-tkbdownload-dg_ctkbfm_sticky, JSESSIONID';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">Huawei NPS:</div>';
    cookieModal += '                                                    currentUrl, awxxxx<br/>';
    cookieModal += '                                                    Google Tag Manager:<br/>';
    cookieModal += '                                                    _dlt';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                        </div>                                            ';
    cookieModal += '                                    </div>';
    cookieModal += '                                </div>                                    ';
    cookieModal += '                            </div>';
    cookieModal += '                            <div class="por-tab-content">';
    cookieModal += '                                <div class="por-collapse-container">';
    cookieModal += '                                    <a class="por-collapse-trigger" data-toggle="por-collapse">';
    cookieModal += '                                        <div class="por-collapse-head-text">Analytics Cookies</div>';
    cookieModal += '                                        <i class="por-icon por-icon-down"></i>';
    cookieModal += '                                    </a>';
    cookieModal += '                                    <div class="por-collapse">';
    cookieModal += '                                        <div class="collapse-inner por-scrollbar-s">';
    cookieModal += '                                            <dl>';
    cookieModal += '                                                <dt class="por-text-title-t7">';
    cookieModal += '                                                    <div class="status inactive">';
    cookieModal += '                                                        <div class="choose-zone">';
    cookieModal += '                                                            <div class="switch"></div>';
    cookieModal += '                                                            Inactive';
    cookieModal += '                                                        </div>';
    cookieModal += '                                                        <div class="choose-zone">';
    cookieModal += '                                                            <div class="switch"></div>';
    cookieModal += '                                                            Active';
    cookieModal += '                                                        </div>';
    cookieModal += '                                                    </div>';
    cookieModal += '                                                    Analytics Cookies';
    cookieModal += '                                                </dt>';
    cookieModal += '                                                <dd>These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site.';
    cookieModal += '                                                    They help us to know which pages are the most and least popular and see how visitors move around the site.';
    cookieModal += '                                                    All information these cookies collect is aggregated and therefore anonymous. However, the third parties providing these services, Google Analytics, ';
    cookieModal += '                                                    will process your personal data in order to provide the aggregated data.    ';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                            <dl classs="cookie-used">';
    cookieModal += '                                                <dt class="por-text-title-t7">Cookies Used</dt>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">Google Analytics: </div> ';
    cookieModal += '                                                    _gid, _gat_xxxxxxxxxxxxxxxxxxxxxxxxxx, _dc_gtm_UA-xxxxxxxx, _gat, _ga, ';
    cookieModal += '                                                    _gclxxxx, _gat_UA-nnnnnnn-nn, _gat_UA-, galleryConfigs, _gac_UA-7728030-19, ';
    cookieModal += '                                                    first_utm, last_utm, ';
    cookieModal += '                                                    _gac_UA-7728030-4 Analytics Data Element Cookies:<br/>';
    cookieModal += '                                                    starttime, scrollPercentage, prevScrollPercentage, ';
    cookieModal += '                                                    prevpagetime';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">Huawei DMP Analytics:</div> ';
    cookieModal += '                                                    _dmpa_ses_time, _dmpa_id, _dmpa_ses, eu-1nebula-collector_dmpa_open_sticky, ';
    cookieModal += '                                                    eu-1nebula-collector_api_sticky, _dmpa_ref, eu-1nebula-collector_dmpa_sticky';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl> ';
    cookieModal += '                                        </div>                                            ';
    cookieModal += '                                    </div>';
    cookieModal += '                                </div>                                 ';
    cookieModal += '                            </div>';
    cookieModal += '                            <div class="por-tab-content">';
    cookieModal += '                                <div class="por-collapse-container">';
    cookieModal += '                                    <a class="por-collapse-trigger" data-toggle="por-collapse">';
    cookieModal += '                                        <div class="por-collapse-head-text">Advertising Cookies</div>';
    cookieModal += '                                        <i class="por-icon por-icon-down"></i>';
    cookieModal += '                                    </a>';
    cookieModal += '                                    <div class="por-collapse">';
    cookieModal += '                                        <div class="collapse-inner por-scrollbar-s">';
    cookieModal += '                                            <dl>';
    cookieModal += '                                                <dt class="por-text-title-t7">';
    cookieModal += '                                                    <div class="status inactive">';
    cookieModal += '                                                        <div class="choose-zone">';
    cookieModal += '                                                            <div class="switch"></div>';
    cookieModal += '                                                            Inactive';
    cookieModal += '                                                        </div>';
    cookieModal += '                                                        <div class="choose-zone">';
    cookieModal += '                                                            <div class="switch"></div>';
    cookieModal += '                                                            Active';
    cookieModal += '                                                        </div>';
    cookieModal += '                                                    </div>';
    cookieModal += '                                                    Advertising Cookies';
    cookieModal += '                                                </dt>';
    cookieModal += '                                                <dd>These cookies are set by our advertising partners. ';
    cookieModal += '                                                    They are used to build a profile of your interests and show relevant ads on other websites, and to also allow you to ‘Like’ and ‘Share’ our content on social media. ';
    cookieModal += '                                                    They do not store directly personal information, but are based on uniquely identifying your browser and internet device. ';
    cookieModal += '                                                    Additionally, the third parties setting these cookies may link your personal data with your browsing behaviour if you are logged into their services at the time.   ';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                            <dl classs="cookie-used">';
    cookieModal += '                                                <dt class="por-text-title-t7">Cookies Used</dt>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">bs.serving-sys.com:</div> ';
    cookieModal += '                                                    OT_6075';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">doubleclick.net:</div> ';
    cookieModal += '                                                    test_cookie, IDE';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">twitter.com:</div> ';
    cookieModal += '                                                    personalization_id';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">serving-sys.com:</div> ';
    cookieModal += '                                                    eyeblaster, OT2, ActivityInfo2, u2, t1';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">ads.linkedin.com:</div> ';
    cookieModal += '                                                    lang';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">bing.com</div> ';
    cookieModal += '                                                    MUID, _uetsid, _uetvid';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">linkedin.com:</div> ';
    cookieModal += '                                                    lidc, bcookie, lissc, bscookie, UserMatchHistory, lang';
    cookieModal += '                                                </dd>';
    cookieModal += '                                                <dd class="por-text-caption-t1">';
    cookieModal += '                                                    <div class="color_text_primary_dark">youtube.com:</div> ';
    cookieModal += '                                                    YSC, VISITOR_INFO1_LIVE, GPS';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                        </div>                                        ';
    cookieModal += '                                    </div>';
    cookieModal += '                                </div>';
    cookieModal += '                                ';
    cookieModal += '                            </div>';
    cookieModal += '                            <div class="por-tab-content">';
    cookieModal += '                                <div class="por-collapse-container">';
    cookieModal += '                                    <a class="por-collapse-trigger" data-toggle="por-collapse">';
    cookieModal += '                                        <div class="por-collapse-head-text">More Information</div>';
    cookieModal += '                                        <i class="por-icon por-icon-down"></i>';
    cookieModal += '                                    </a>';
    cookieModal += '                                    <div class="por-collapse">';
    cookieModal += '                                        <div class="collapse-inner por-scrollbar-s">';
    cookieModal += '                                            <dl>';
    cookieModal += '                                                <dt class="por-text-title-t7">More Information</dt>';
    cookieModal += '                                                <dd style="font-size: 14px;">';
    cookieModal += '                                                    <a class="por-link" href="https://www.huaweicloud.com/intl/en-us/declaration/sa_cookies.html" target="_blank">https://www.huaweicloud.com/intl/en-us/declaration/sa_cookies.html</a>       ';
    cookieModal += '                                                </dd>';
    cookieModal += '                                            </dl>';
    cookieModal += '                                        </div>                                           ';
    cookieModal += '                                    </div>';
    cookieModal += '                                </div>';
    cookieModal += '                                ';
    cookieModal += '                            </div>';
    cookieModal += '                        </div>';
    cookieModal += '                    </div>';
    cookieModal += '                </div>';
    cookieModal += '            </div>';
    cookieModal += '            <div class="por-modal-footer">';
    cookieModal += '                <a class="por-btn por-btn-small por-btn-primary" data-hide="modal">Accept Cookies</a>';
    cookieModal += '                <a class="por-btn por-btn-small por-btn-dark" data-hide="modal">Save and close</a>';
    cookieModal += '            </div>';
    cookieModal += '        </div>';
    cookieModal += '        <div class="por-modal-close" data-hide="modal">';
    cookieModal += '            <i class="u-icon u-icon-cancel"></i>';
    cookieModal += '        </div>';
    cookieModal += '    </div>';
    cookieModal += '</div>';

    
    if (location.href.indexOf('developer') != -1 || location.href.indexOf('edu') != -1 || location.href.indexOf('marketplace') != -1) {
        $('.privacy-popup').css('display', 'block');
    } else {
        $.ajax({
            url: 'https://portal-intl.huaweicloud.com/portaluserqueryservice/ipsearch',
            method: 'GET',
            datatype: 'json',
            success: function success(rep) {
                if (rep.data) {
                    localStorage.setItem('countrycode', rep.data[0].location.countrycode);
                    if (rep.data[0].location.countrycode === 'TH' && (location.href.indexOf('intl/en-us') != -1 || location.href.indexOf('intl/th-th') != -1 || (site == 'hk' && (currLang == 'en-us' || currLang == 'th-th')))) {
                        $('<dd><a class="footer-link reset-cookies">Cookie Settings</a></dd>').insertAfter($('.footer-nav-menus dl:nth-child(3) dd:last-child'));
                        window.$PrivacyUtil.setCookie("essential", "active", 20000);
                        var $settingCookieModule = $('<div class="pep-settingcookie-module"></div>');
                        var modalContainer = $('#content').length ? $('#content') : $('#__nuxt');
                        $settingCookieModule.insertAfter(modalContainer);
                        $settingCookieModule.append(cookieModal);

                        var currentCookieSetting = {
                            Analytics: window.$PrivacyUtil.getCookie("Analytics"),
                            Advertising: window.$PrivacyUtil.getCookie("Advertising")
                        };

                        function saveAll() {
                            window.$PrivacyUtil.setCookie("Analytics", "active", 20000);
                            window.$PrivacyUtil.setCookie("Advertising", "active", 20000);

                            if ($('.float-cookie-dialog').length) {
                                $('.float-cookie-dialog').remove();
                            }
                        };

                        function saveSelected() {
                            $('#cookie-setting-modal').porModal('show');
                            window.$PrivacyUtil.getCookie("Analytics") === 'active' ? $('#cookie-setting-modal .status').eq(0).removeClass('inactive').addClass('active') : $('#cookie-setting-modal .status').eq(0).removeClass('active').addClass('inactive');
                            window.$PrivacyUtil.getCookie("Advertising") === 'active' ? $('#cookie-setting-modal .status').eq(1).removeClass('inactive').addClass('active') : $('#cookie-setting-modal .status').eq(1).removeClass('active').addClass('inactive');

                            $('.por-modal-footer').on('click', '.por-btn', function (e) {
                                var $target = $(e.target);

                                switch ($target.index()) {
                                    case 0:
                                        saveAll();
                                        break;

                                    case 1:
                                        $('#cookie-setting-modal .status').eq(0).is('.active') ? window.$PrivacyUtil.setCookie("Analytics", "active", 20000) : window.$PrivacyUtil.setCookie("Analytics", "inactive", 20000);
                                        $('#cookie-setting-modal .status').eq(1).is('.active') ? window.$PrivacyUtil.setCookie("Advertising", "active", 20000) : window.$PrivacyUtil.setCookie("Advertising", "inactive", 20000);
                                        break;
                                }

                                $('.float-cookie-dialog').remove();
                            });
                        };

                        // 首次打开页面
                        if (currentCookieSetting.Analytics == null && currentCookieSetting.Advertising == null) {
                            $settingCookieModule.append(floatDialog);

                            $('.cookie-btn-group').on('click', '.por-btn', function (e) {
                                var $target = $(e.target);

                                switch ($target.index()) {
                                    case 0:
                                        saveAll();
                                        break;

                                    case 1:
                                        saveSelected();
                                        break;
                                }
                            });
                        }

                        $('.reset-cookies').click(function () {
                            saveSelected();
                        });

                        $('#cookie-setting-modal .por-collapse-trigger').on('click', function (e) {
                            $(e.target).closest('.por-tab-content').siblings().find('.por-collapse-trigger').removeClass('expended').end().find('.por-collapse').removeClass('show');
                        });

                        $('#cookie-setting-modal .status').click(function (e) {
                            $(e.currentTarget).is('.inactive') ? $(e.currentTarget).removeClass('inactive').addClass('active') : $(e.currentTarget).removeClass('active').addClass('inactive');
                        });
                    } else {
                        $('.privacy-popup').css('display', 'block');
                    }
                }
            }
        });
    }
})