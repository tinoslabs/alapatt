/*!
 * fastshell
 * Fiercely quick and opinionated front-ends
 * https://HosseinKarami.github.io/fastshell
 * @author Hossein Karami
 * @version 1.0.5
 * Copyright 2016. MIT licensed.
 */
/*!
 * fastshell
 * Fiercely quick and opinionated front-ends
 * https://HosseinKarami.github.io/fastshell
 * @author Hossein Karami
 * @version 1.0.5
 * Copyright 2016. MIT licensed.
 */
/*!
* NetbaseTeam Jewelry HTML Javascript file
*/
(function ($, window, document, undefined) {
	'use strict';
	$(function () {
		jQuery(document).ready(function() {

			// Initialize Revolution Slider
			var revapi;
			revapi = jQuery('.vt-slideshow').revolution({
				delay:5000,
				startwidth:1920,
				startheight:920,
				fullWidth:'on',
				forceFullWidth:'on',
				navigationType:'none'
			});

			// Add Grayscale hover effect
			jQuery('.grayscale').on({
				mouseenter: function() {
					jQuery(this).addClass('disabled');
				},
				mouseleave: function() {
					jQuery( this ).removeClass( 'disabled' );
				}
			});

			//Add slide-in effect for choosen components
			function trustView(elem){
				if( jQuery(elem).length ) {
					var bottomOfObject = jQuery(elem).offset().top;
					var bottomOfWindow = jQuery(window).scrollTop() + jQuery(window).height();
					if(bottomOfWindow > bottomOfObject){
						return true;
					}
				}
			}
			function addClassView(addClass, elem){
				if (trustView(elem) === true) {
					jQuery(addClass).addClass('inview');
				}
			}
			jQuery(window).on('scroll', function() {
				addClassView('.new-products .products','.new-products .products');
				addClassView('.blog-posts','.blog-posts');
				addClassView('.team-members','.team-members');
				addClassView('.collection','.collection');
			});

			//Drop down megamenu
			jQuery('.has-sub').on({
				mouseenter: function() {
					jQuery(this).children('.sub-menu').stop().slideDown('slow');
				},
				mouseleave: function() {
					jQuery(this).children('.sub-menu').stop().slideUp('medium');
				}
			});

			//Mobile megamenu
			var screenHeight = jQuery(window).height();
			jQuery('#mb-main-menu').css('height', screenHeight);
			jQuery('#mb-main-menu li.parent a').on('click', function(){
				jQuery('#mb-main-menu li.parent a').removeClass('active');
				//slide up all the link lists
				jQuery('#mb-main-menu li.parent ul').slideUp();
				if(!jQuery(this).next('ul').is(':visible'))
				{
					jQuery(this).next().slideDown();
					jQuery(this).addClass('active');
				}
			});
			var isMenuShowing = false;
			function menuShow(){
				jQuery('#mb-main-menu').animate({ 'left': '0' }, 250);
				jQuery('#mb-main-menu').css('display','block');
				jQuery('#sitebodyoverlay').show();
				jQuery(window).scrollTop(0);
				isMenuShowing = true;
			}
			function menuHide(){
				jQuery('#mb-main-menu').animate({ 'left': '-100%' }, 250);
				jQuery('#sitebodyoverlay').hide();
				isMenuShowing = false;
			}
			jQuery('.mbmenu-icon').on('click', function(){
				if(isMenuShowing){
					menuHide();
				}else{
					menuShow();
				}
			});
			jQuery('#close-mb-menu').on('click', function(){
				menuHide();
			});

			// Back to top button
			jQuery('#back-to-top').on('click', function(){
				jQuery('html, body').animate({ scrollTop: 0 }, 600);
				return false;
			});

			// Tooltip effect
			jQuery(document).ready(function(){
				jQuery('[data-toggle="tooltip"]').tooltip();
			});

			// Initialize StackTable components
			jQuery('#cart-stack-table').stacktable();
			jQuery('#wishlist-stack-table').stacktable({myClass:'your-class-name'});

			// Simple accordion effect for shop page
			jQuery('.cate_list li.parent a').on('click', function(){
				jQuery('.cate_list li.parent a').removeClass('active');
				//slide up all the link lists
				jQuery('.cate_list li.parent ul').slideUp();
				//slide down the link list below the h3 clicked - only if its closed
				if(!jQuery(this).next('ul').is(':visible'))
				{
					jQuery(this).next().slideDown();
					jQuery(this).addClass('active');
				}
			});

			// Checkout page create account	button
			jQuery('input:checkbox[name="create-acc"]').on('click', function(){
				jQuery(this).parent().siblings('.acc-hidden').slideToggle();
			});

			// OwlCarousel init
			jQuery('.gallery-images').owlCarousel({
				margin:8,
				nav : true,
				navText: ['<i class="icon-left-open-1"></i>', '<i class="icon-right-open-1"></i>'],
				autoplay:true,
				autoplayTimeout:3000,
				autoplayHoverPause:true,
				loop: true,
				responsive: {
					0: {
						items: 3
					},
					992: {
						items: 4
					}
				}
			});
			jQuery('.cross-sell-products .products').owlCarousel({
				items: 4,
				margin:30,
				nav : true,
				navText: ['<i class="icon-left-open"></i>', '<i class="icon-right-open"></i>'],
				autoplay:true,
				autoplayTimeout:3000,
				autoplayHoverPause:true,
				loop: true,
				responsive: {
					0: {
						items: 1,
					},
					400: {
						items: 2,
					},
					600: {
						items: 3,
					},
					992: {
						items: 4,
					}
				},
			});
			jQuery('.related-products').owlCarousel({
				items: 1,
				nav : true,
				loop: true,
				navText: ['<i class="icon-left-open"></i>', '<i class="icon-right-open"></i>'],
			});

			// Initialize select2 components
			jQuery('#country-select').select2();
			jQuery('#country-select').select2();

			// Checkout page login and coupon field effect
			jQuery('.page-info > a').on('click', function(e){
				e.preventDefault();
				jQuery(this).parent().siblings('.hidden-form').slideToggle();
			});

			// Submit mail form
			jQuery('form').submit(function (e) {
				e.preventDefault();
				var validate = true;
				var p = [];
				var array = ['msg_name', 'msg_email', 'msg_message'];
				jQuery.each(array, function(index, value){
					p[value] = jQuery('#' + value).val();
					if(p[value] === ''){
						jQuery('.form-group.' + value).addClass('has-error');
						validate = false;

					}else {
						jQuery('.form-group.' + value).removeClass('has-error');
					}
				});
				//return validate;
				if(!validate) {alert('Please fill all required field!'); return validate;} else {
					jQuery.post('newsletter.send.php',
					{ msg_email:p['msg_email'], msg_name: p['msg_name'], msg_message: p['msg_message']},
					function( result ){

						console.log( result );

						if ( result==='SUCCESS' ){
							alert('Thank you. Your email is added to our database.');
						}

						else if ( result==='EXIST' ){
							alert('Error. Your email address is already exist our database.');
						}

						else {
							alert('Error. Your email isn\'t added to our database.');
						}
					});
				}
			});

			// Fancybox components init
			jQuery(".fancybox").fancybox();

			// jQuery UI Accordion
			jQuery( '#CMStab' ).accordion({
				event: 'mouseup',
			});
			jQuery( '.payment-methods' ).accordion({
				event: 'mouseup',
			});			

			// Add accordion to footer on small screen
			var windowWidth = jQuery(window).width();
			if(windowWidth < 992) {
				jQuery('.footer-columns').accordion({
					header: '.footer-column > h4',
					heightStyle: 'content'
				});
			}			
			jQuery(window).on('resize', function() {	
				var windowWidth = jQuery(window).width();			
				if(windowWidth < 992) {					
					jQuery('.footer-columns').accordion({
						header: '.footer-column > h4',
						heightStyle: 'content'
					});
					jQuery('.footer-acordion-wrap').hide();	
					jQuery('.footer-acordion-wrap').first().show();						
				}  else {
					jQuery('.footer-columns').accordion('destroy');
				}
			});			
		});
	});

})(jQuery, window, document);
