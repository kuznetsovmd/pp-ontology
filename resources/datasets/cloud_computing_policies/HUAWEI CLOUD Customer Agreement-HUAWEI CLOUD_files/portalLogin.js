var portalDomain = "https://portal-intl.huaweicloud.com";
var ssoDomain = "https://auth-intl.huaweicloud.com";
var isVerified = false;//定义实名认证变量
var isLogin = false; //定义登录变量

function getUaCookie(c_name) {
  if (document.cookie.length > 0) {
    var c_start = document.cookie.indexOf(c_name + "=");
    if (c_start != -1) {
      c_start = c_start + c_name.length + 1;
      var c_end = document.cookie.indexOf(";", c_start);
      if (c_end == -1) c_end = document.cookie.length;
      return decodeURI(document.cookie.substring(c_start, c_end));
    }
  }
  return "";
}

var jsonParamInit = {};
var jsonParamView = {};
var jsonParamEvent = {};
jsonParamInit['UserAccount'] = 'host';
jsonParamEvent['rec_account'] = getUaCookie("ua");
jsonParamView['rec_account'] = getUaCookie("ua");

function showMenu(data) {
  data = data || [];
  var isVendor = data.isVendor || false;
  var isIsv = data.isIsv || false;
  var $_target = $(".user-info-layer ul.account-nav");
  if (isVendor) {
    $_target.find("li").hide();
    $_target.find(".isVendor,.logout").show();
  }
  else if (isIsv) {
    $_target.find(".isIsv").show();
    $_target.find(".isVendor").show();
  }
}
function removeTicket(query) {
  return query.replace(/ticket=[^&]*&?/, '');
}
function getScript(win, doc, tag, src, always) {
  var script = doc.createElement(tag),
    h = doc.getElementsByTagName(tag)[0];
  script.async = 1;
  script.src = src;

  if (script.addEventListener) {
    script.addEventListener("load", always, false);
  } else if (script.attachEvent) {
    script.attachEvent("onreadystatechange", function () {
      var target = window.event.srcElement;
      if (target.readyState == "loaded" || target.readyState == "complete") {
        always.call(target);
      }
    });
  }
  h.parentNode.insertBefore(script, h)
}
function loginCallback(data) {

  if (data.flag == 1) {
    var win_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    var isPc = win_width > 768 ? true : false;
    // 登录后显示的用户名
    var nameShow = '';

    var username = data.username;
    isLogin = true;
    jsonParamInit['UserAccount'] = data.userId;
    jsonParamEvent['rec_account'] = data.userId;
    jsonParamView['rec_account'] = data.userId;
    jsonParamInit['xdomain_type'] = data.xdomain_type;

    var image_url = data.image_url;
    if (image_url && image_url.small) {
      $(".account-pic").attr("src", image_url.small);
    }
    if (data.xdomain_type != "HWC_CN") {
      isGrayuser();
    }
    $("#header").addClass('logined');


    //  用户名展示
    // 1、未升级华为id的，只显示华为云账号名
    // 2、升级了华为id的，不管华为id和账号名是否一致，只展示 HWID
    // 3、iam子账号登录，只显示iam用户名

    var queryDomain =
      window.location.href.indexOf('huaweicloud.com') > -1
        ? 'https://portal-intl.huaweicloud.com'
        : 'https://portal-intl.ulanqab.huawei.com';
    var queryUrl = queryDomain + '/rest/cbc/cbccustomerregservice/v1/account/' + data.domainId;
    $.ajax({
      type: 'get',
      url: queryUrl,
      crossDomain: true,
      async: true,
      timeout: 10000,
      success: function (data) {
        // 用户升级了
        if (data.account) {
          if (data.account.domain_type === 'HWID') {
            nameShow = data.account.xdomain_name || '';
          } else {
            nameShow = data.account.domain_name || '';
          }
        } else {
          // 用户没升级 展示原来的华为云用户名
          nameShow = username;
        }

        $('.user-info').find('.my-acct').text(nameShow);
        $('.user-info').find('.my-acct').attr('title', nameShow);

        //  实名认证下展示用户名pc端
        if (isPc && $('.hwid').length === 0) {
          if ($('.account-nav .account-item').css("display") != 'none') {
            $('<li><a href="javascript:void(0);"style="color: #8A8E99; width: 100%; cursor:default;" class="hwid">' + nameShow + '</a><li class="header-user-info-split"></li>').insertAfter('.account-item');
          }
        }
      },
      error: function (data) { },
    });

    //导航用户菜单展示
    showMenu(data);

    // get user site info and show tips when user is HWC_CN
    if (data.xdomain_type == "HWC_CN") {
      window.prompts && window.prompts(true, window.reg, window.promptLan, window.refLan, window.promptTips, true);
      window.menuPrompts && window.menuPrompts(true, window.reg, window.promptLan, window.refLan, window.promptTips, true);
    }
  }

  if (window.observer) {
    observer("login").publish(null, data)
  }
}

function isGrayuser() {
  var is_gray_user = portalDomain + '/index/isgrayuser';
  getScript(window, document, "script", is_gray_user, function () { });
}

jQuery(function () {
  var href = encodeURIComponent(removeTicket(window.location.href));
  //登陆之后回到本页面
  $("[data-login-href]").each(function () {
    $(this).attr("href", $(this).data('login-href') + href);
  });

  function $parseQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) {
      return unescape(r[2]);
    }
    else {
      return null;
    }
  };
  if ($parseQueryString("fromacct") || $parseQueryString("fromuser")) {
    $(document).on("mouseenter", "a", function (e) {
      var fromacct = $parseQueryString("fromacct") || $parseQueryString("fromuser");
      var fromflag = $parseQueryString("fromacct") ? "fromacct" : "fromuser";
      var tmpEle = $("<div></div>");
      tmpEle.text(fromacct);
      fromacct = tmpEle.html();
      var $this = $(this);
      var href = $this.attr("href");
      if (href && (href.indexOf("//") == 0 || href.indexOf("http") == 0) && href.indexOf(fromflag) == -1) {
        var targetHref = (href.indexOf(".html?") != -1 || href.indexOf("/?") != -1) ? (href + "&" + fromflag + "=" + fromacct) : (href + "?" + fromflag + "=" + fromacct);
        $this.attr("href", targetHref);
      }
    })
  }

  var login_check_url = portalDomain + "/index/islogin?callback=?";
  window.raw_onerror = window.onerror;
  window.onerror = function (errorMsg, url, lineNumber) {
    return true;
  }
  var check_login_url = portalDomain + '/index/islogin?callback=loginCallback';
  getScript(window, document, "script", check_login_url, function () {
    try {
      if (typeof initBi === "function") {
        initBi(jsonParamInit, jsonParamView, jsonParamEvent);
      }
      if (!window.isLogin) {
        observer("login").publish(null, { flag: 0 })
      }
    } catch (e) { }
    window.onerror = window.raw_onerror;
  });
});