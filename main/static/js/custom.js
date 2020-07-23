$(function() {
    "use strict";

    var o = function() {
        var o = 390,
            n = (window.innerHeight > 0 ? window.innerHeight : this.screen.height) - 1;
        n -= o, 1 > n && (n = 1), n > o && $(".page-wrapper").css("min-height", n + "px")
    };
	
    $(window).ready(o), $(window).on("resize", o), $(function() {
        $('[data-toggle="tooltip"]').tooltip()
    }), $(function() {
        $('[data-toggle="popover"]').popover()
    }), jQuery(document).on("click", ".nav-dropdown", function(o) {
        o.stopPropagation()
    }), jQuery(document).on("click", ".navbar-nav > .dropdown", function(o) {
        o.stopPropagation()
    }), $(".dropdown-submenu").on("click", function() {
        $(".dropdown-submenu > .dropdown-menu").toggleClass("show")
    }), $("body").trigger("resize");
    var n = $(window);
    n.on("load", function() {
        var o = n.scrollTop(),
            e = $(".topbar");
        o > 100 ? e.addClass("fixed-header animated slideInDown") : e.removeClass("fixed-header animated slideInDown")
    }), $(window).scroll(function() {
        $(window).scrollTop() >= 200 ? ($(".topbar").addClass("fixed-header animated slideInDown"), $(".bt-top").addClass("visible")) : ($(".topbar").removeClass("fixed-header animated slideInDown"), $(".bt-top").removeClass("visible"))
    }), AOS.init(), $(".bt-top").on("click", function(o) {
        o.preventDefault(), $("html,body").animate({
            scrollTop: 0
        }, 700)
    })
	
	// Add Pricing
	function newMenuItem() {
		var newElem = $('tr.pricing-list-item.pattern').first().clone();
		newElem.find('input').val('');
		newElem.appendTo('table#price-list-wrap');
	}
	if ($("table#price-list-wrap").is('*')) {
		$('.add-pr-item-btn').on('click', function(e) {
			e.preventDefault();
			newMenuItem();
		});
		$(document).on("click", "#price-list-wrap .delete", function(e) {
			e.preventDefault();
			$(this).parent().parent().remove();
		});
		$('.add-cat-btn').on('click', function(e) {
			e.preventDefault();
			var newElem = $('' +
				'<tr class="pricing-list-item pricing-submenu">' +
				'<td>' +
				'<div class="box-move"><i class="ti-move"></i></div>' +
				'<div class="box-input"><input type="text" class="frm-control" placeholder="Category Title" /></div>' +
				'<div class="box-close"><a class="delete" href="#"><i class="ti-close"></i></a></div>' +
				'</td>' +
				'</tr>');
			newElem.appendTo('table#price-list-wrap');
		});
		$('table#price-list-wrap tbody').sortable({
			forcePlaceholderSize: true,
			forceHelperSize: false,
			placeholder: 'sortableHelper',
			zIndex: 999990,
			opacity: 0.6,
			tolerance: "pointer",
			start: function(e, ui) {
				ui.placeholder.height(ui.helper.outerHeight());
			}
		});
	}
	var fieldUnit = $('.pr-price').children('input').attr('data-unit');
	$('.pr-price').children('input').before('<i class="data-unit">' + fieldUnit + '</i>');
	$("a.close").removeAttr("href").on('click', function() {
		function slideFade(elem) {
			var fadeOut = {
				opacity: 0,
				transition: 'opacity 0.5s'
			};
			elem.css(fadeOut).slideUp();
		}
		slideFade($(this).parent());
	});
	$(".price-add-wrapper").each(function() {
		var switcherSection = $(this);
		var switcherInput = $(this).find('.switch input');
		if (switcherInput.is(':checked')) {
			$(switcherSection).addClass('switch-on');
		}
		switcherInput.change(function() {
			if (this.checked === true) {
				$(switcherSection).addClass('switch-on');
			} else {
				$(switcherSection).removeClass('switch-on');
			}
		});
	});
	
	// All Select Category
	$('#category').select2({
		placeholder: "Choose Category...",
		allowClear: true
	});
	
	$('#area').select2({
		placeholder: "Choose Area",
		allowClear: true
	});
	
	$('#minbed').select2({
		placeholder: "Min Bed",
		allowClear: true
	});
	
	$('#minbath').select2({
		placeholder: "Min Bath",
		allowClear: true
	});

	$('#author').select2({
		placeholder: "Choose Author...",
		allowClear: true
	});
	
	
	// Testimonials
	$("#testimonials").owlCarousel({
		nav: !0,
		dots: !0,
		items: 1,
		center: !0,
		loop: !0,
		navText: ['<i class="fa fa-arrow-left"></i>', '<i class="fa fa-arrow-right"></i>'],
		responsive: {
			1700: {
				stagePadding: 620,
				margin:120
			},
			1430: {
				stagePadding: 320,
				margin:100
			},
			1025: {
				stagePadding: 300,
				margin:80
			},
			768: {
				stagePadding: 150,
				margin:50
			},
			0: {
				stagePadding: 0,
				margin: 0
			}
		}
	})
	
	// Testimonials 2
	$("#testimonials-2").owlCarousel({
		nav: !0,
		dots: !0,
		items: 1,
		center: !0,
		loop: !0,
		navText: ['<i class="fa fa-arrow-left"></i>', '<i class="fa fa-arrow-right"></i>'],
		responsive: {
			1700: {
				stagePadding: 620,
				margin:120
			},
			1430: {
				stagePadding: 320,
				margin:100
			},
			1025: {
				stagePadding:280,
				margin:10
			},
			768: {
				stagePadding: 150,
				margin:50
			},
			0: {
				stagePadding: 0,
				margin: 0
			}
		}
	})
	
	// Company Brand
	$("#company-brand").owlCarousel({
		loop:true,
		autoplay:true,
		nav:false,
		dots:false,
		margin:60,
		responsiveClass:true,
		responsive:{
			0:{
				items:1,
				nav:false
			},
			600:{
				items:3,
				nav:false
			},
			1000:{
				items:6,
				nav:false,
				loop:false
			}
		}
	})

	
	// List Slide
	$('#list-slide').owlCarousel({
		loop:true,
		margin:15,
		responsiveClass:true,
		responsive:{
			0:{
				items:1,
				autoplay:true,
				nav:true
			},
			600:{
				items:2,
				autoplay:true,
				nav:false
			},
			1000:{
				items:3,
				nav:false,
				autoplay:true,
				loop:false
			},
			1280:{
				items:3,
				nav:false,
				autoplay:true,
				loop:false
			}
		}
	})
	
	/*------ Testimonial 3 Script ----*/
	$('.slick-carousel-3').slick({
	  slidesToShow:1,
	  responsive: [
		{
		  breakpoint: 768,
		  settings: {
			arrows: false,
			centerPadding: '40px',
			slidesToShow: 1
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			arrows: false,
			centerPadding: '40px',
			slidesToShow: 1
		  }
		}
	  ]
	});
	
	// Destination Slide
	$('#destination-slide').owlCarousel({
		loop:true,
		margin:15,
		responsiveClass:true,
		responsive:{
			0:{
				items:1,
				autoplay:true,
				nav:true
			},
			600:{
				items:2,
				autoplay:true,
				nav:false
			},
			1000:{
				items:3,
				nav:false,
				autoplay:true,
				loop:false
			},
			1280:{
				items:3,
				nav:false,
				autoplay:true,
				loop:false
			}
		}
	})
	
	// Category Slide
	$('#category-slide').owlCarousel({
		loop:true,
		margin:15,
		responsiveClass:true,
		responsive:{
			0:{
				items:1,
				autoplay:true,
				nav:true
			},
			600:{
				items:2,
				autoplay:true,
				nav:false
			},
			1000:{
				items:3,
				nav:false,
				autoplay:true,
				loop:false
			},
			1280:{
				items:3,
				nav:false,
				autoplay:true,
				loop:false
			}
		}
	})
	
	// Range Slider Script
	$("#qua").slider({});
	$("#ser").slider({});
	$("#pri").slider({});
	$("#spa").slider({});
	$("#loc").slider({});
	$("#ex6").slider({});

});