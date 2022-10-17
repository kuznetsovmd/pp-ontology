$(function () {
    var win_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
        win_height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    //tab
    $(".announ_tab ul li").click(function () {
        $(this).addClass("active").siblings("").removeClass("active");
    })
     

    if ($('.announ_tab li').length > 0) {
        $('.announ_tab li').click(function () {
            var $con = $(this).closest(".announ_tab").siblings(".announ_center");
            $(this).addClass('active').siblings().removeClass('active');
            $con.removeClass('show').filter("." + $(this).data('target')).addClass('show');
        });
    };
    if (win_width < 1280) {
        $(".law_right>h1").click(function () {
            $(this).toggleClass("unfold");
            $(".law_left").toggleClass("show");
        })

    }






})
