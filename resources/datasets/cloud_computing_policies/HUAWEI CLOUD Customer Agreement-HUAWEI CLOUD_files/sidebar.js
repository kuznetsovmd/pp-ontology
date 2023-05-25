$(function () {
    $('.left_sidebar .nav-item p.sidebar_active')
        .parent()
        .addClass('active');
    $('.left_sidebar .nav-item p.sidebar_active')
        .siblings('.the_sidebar')
        .slideDown();

    // 左侧栏点击效果
    $('.left_sidebar').on('click', 'p, .foldIcon', function(){
        var target = $(this);
        var con = $(target).closest('li');
        $('.the_sidebar').hide();
        if (!con.hasClass('active')) {
            con.addClass('active')
                .siblings('li')
                .removeClass('active');
            con.find('.the_sidebar').slideDown();
        } else {
            con.removeClass('active');
            con.find('.the_sidebar').slideUp();
        }
    });
    var win_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    var win_height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    var $frame = $('body');
    // 移动端交互
    if (win_width < 1024) {
        $('.law_left h2').click(function(){
            var target = $(this);
            var con = $('.law_left .left_sidebar');
            var sideHei = win_height - $(target).outerHeight() - 56;
            if (!$(target).hasClass('active')) {
                $(target).addClass('active');
                con.height(sideHei).slideDown();
                $frame.height(win_height).addClass('overflow-hide');
                $('.indicator-triangle').addClass('show');
            } else {
                $(target).removeClass('active');
                $frame.height('auto').removeClass('overflow-hide');
                con.height('0').slideUp();
                $('.indicator-triangle').removeClass('show');
            }
        });
    }

    $('.the_sidebar .third-txt-ellipsis .nav-void').click(function(){
        var target = $(this);

        var con = $(target).closest('dd.third-txt-ellipsis');
        $('.third-level').hide();
        if (!con.hasClass('active')) {
            con.addClass('active')
                .siblings('dd')
                .removeClass('active');
            con.find('.third-level').slideDown();
        } else {
            con.removeClass('active');
            con.find('.third-level').slideUp();
        }
    });
});
