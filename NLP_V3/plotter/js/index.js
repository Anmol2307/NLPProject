$(function() {
    var nav = $('.my-container');
    nav.css({backgroundColor: "rgba(44,62,80,0.5)"});
    $(window).on('scroll',function(){
        var nav = $('.my-container');
        var max_shift = 200;
        stop = Math.round($(window).scrollTop());
        if(stop > max_shift){
            nav.css({backgroundColor: "rgb(44,62,80)", paddingTop: "5px",paddingBottom: "5px"});
        }else{
            value = (1.0*(stop+max_shift))/(2.0*max_shift);
            nav.css({backgroundColor: "rgba(44,62,80," + value +")", padding: "13px"});
        }
    });
    
});