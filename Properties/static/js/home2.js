!function(o){"use strict";o(window).on("load",function(){o("#preloader").length&&o("#preloader").delay(100).fadeOut("slow",function(){o(this).remove()})}),o(window).scroll(function(){100<o(this).scrollTop()?o(".back-to-top").fadeIn("slow"):o(".back-to-top").fadeOut("slow")}),o(".back-to-top").click(function(){return o("html, body").animate({scrollTop:0},1500,"easeInOutExpo"),!1});o("nav").outerHeight();window.sr=ScrollReveal(),sr.reveal(".foo",{duration:1e3,delay:15}),o("#carousel").owlCarousel({loop:!0,margin:-1,items:1,nav:!0,navText:['<i class="fa fa-arrow-left" aria-hidden="true"></i>','<i class="ion-ios-arrow-right" aria-hidden="true"></i>'],autoplay:!0,autoplayTimeout:3e3,autoplayHoverPause:!0}),o(".intro-carousel").on("translate.owl.carousel",function(){o(".intro-content .intro-title").removeClass("zoomIn animated").hide(),o(".intro-content .intro-price").removeClass("fadeInUp animated").hide(),o(".intro-content .intro-title-top, .intro-content .spacial").removeClass("fadeIn animated").hide()}),o(".intro-carousel").on("translated.owl.carousel",function(){o(".intro-content .intro-title").addClass("zoomIn animated").show(),o(".intro-content .intro-price").addClass("fadeInUp animated").show(),o(".intro-content .intro-title-top, .intro-content .spacial").addClass("fadeIn animated").show()}),o(".navbar-toggle-box-collapse").on("click",function(){o("body").removeClass("box-collapse-closed").addClass("box-collapse-open")}),o(".close-box-collapse, .click-closed").on("click",function(){o("body").removeClass("box-collapse-open").addClass("box-collapse-closed"),o(".menu-list ul").slideUp(700)}),o(window).trigger("scroll"),o(window).bind("scroll",function(){50<o(window).scrollTop()?(o(".navbar-default").addClass("navbar-reduce"),o(".navbar-default").removeClass("navbar-trans")):(o(".navbar-default").addClass("navbar-trans"),o(".navbar-default").removeClass("navbar-reduce")),1200<o(window).scrollTop()?o(".scrolltop-mf").fadeIn(1e3,"easeInOutExpo"):o(".scrolltop-mf").fadeOut(1e3,"easeInOutExpo")}),o("#property-carousel").owlCarousel({loop:!0,margin:30,responsive:{0:{items:1},769:{items:2},992:{items:3}}}),o("#property-single-carousel").owlCarousel({loop:!0,margin:0,nav:!0,navText:['<i class="fa fa-arrow-left" aria-hidden="true"></i>','<i class="fa fa-arrow-right" aria-hidden="true"></i>'],responsive:{0:{items:1}}}),o("#new-carousel").owlCarousel({loop:!0,margin:30,responsive:{0:{items:1},769:{items:2},992:{items:3}}}),o("#testimonial-carousel").owlCarousel({margin:0,autoplay:!0,nav:!0,animateOut:"fadeOut",animateIn:"fadeInUp",navText:['<i class="fa fa-arrow-left" aria-hidden="true"></i>','<i class="fa fa-arrow-right" aria-hidden="true"></i>'],autoplayTimeout:4e3,autoplayHoverPause:!0,responsive:{0:{items:1}}})}(jQuery);


(function(){
    var bsa = document.createElement('script');
    bsa.type = 'text/javascript';
    bsa.async = true;
    bsa.src = '//s3.buysellads.com/ac/bsa.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(bsa);
})();


var gaProperty = 'UA-120201777-1';
var disableStr = 'ga-disable-' + gaProperty;

if (document.cookie.indexOf(disableStr + '=true') > -1) {
    window[disableStr] = true;
}

function gaOptout() {
    document.cookie = disableStr + '=true; expires=Thu, 31 Dec 2045 23:59:59 UTC; path=/';
    window[disableStr] = true;
    alert('Google Tracking has been deactivated');
}

(function(i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function() {
        (i[r].q = i[r].q || []).push(arguments);
    }, i[r].l = 1 * new Date();
    a = s.createElement(o),
    m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m);
})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

ga('create', 'UA-120201777-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');


$(document).ready(function(){
    $("#agents-carousel-slider").owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        responsive:{
            0:{ items: 1 },
            600:{ items: 2 },
            1000:{ items: 3 }
        }
    });
});
