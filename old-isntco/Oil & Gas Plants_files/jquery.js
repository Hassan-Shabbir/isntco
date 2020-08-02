var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

;(function($){ // secure $ jQuery alias
/*******************************************************************************************/	
// jquery.event.hover.js - rev 5 
// Copyright (c) 2008, Three Dub Media (http://threedubmedia.com)
// Liscensed under the MIT License (MIT-LICENSE.txt)
// http://www.opensource.org/licenses/mit-license.php
// Created: 2008-06-02 | Updated: 2008-07-30
/*******************************************************************************************/

//	USE THESE PROPERTIES TO CUSTOMIZE SETTINGS...

//	jQuery.event.special.hover.delay = 100; 
//	Defines the delay (msec) while mouse is inside the element before checking the speed

//	jQuery.event.special.hover.speed = 100; 
//	Defines the maximum speed (px/sec) the mouse may be moving to trigger the hover event

// save the old jquery "hover" method
$.fn._hover = $.fn.hover;

// jquery method 
$.fn.hover = function( fn1, fn2, fn3 ) {
	if ( fn3 ) this.bind('hoverstart', fn1 ); // 3 args
	if ( fn2 ) this.bind('hoverend', fn3 ? fn3 : fn2 ); // 2+ args
	return !fn1 ? this.trigger('hover') // 0 args 
		: this.bind('hover', fn3 ? fn2 : fn1 ); // 1+ args
	};	

// special event configuration
var hover = $.event.special.hover = {
	delay: 100, // milliseconds
	speed: 100, // pixels per second
	setup: function( data ){
		data = $.extend({ speed: hover.speed, delay: hover.delay, hovered:0 }, data||{} );
		$.event.add( this, "mouseenter mouseleave", hoverHandler, data );
		},
	teardown: function(){
		$.event.remove( this, "mouseenter mouseleave", hoverHandler );
		}
	};

// shared event handler
function hoverHandler( event ){
	var data = event.data || event;
	switch ( event.type ){
		case 'mouseenter': // mouseover
			data.dist2 = 0; // init mouse distance²
			data.event = event; // store the event
			event.type = "hoverstart"; // hijack event
			if ( $.event.handle.call( this, event )!==false ){ // handle "hoverstart"
				data.elem = this; // ref to the current element
				$.event.add( this, "mousemove", hoverHandler, data ); // track the mouse
				data.timer = setTimeout( compare, data.delay ); // start async compare
				}
			break;
		case 'mousemove': // track the event, mouse distance² = x² + y²
			data.dist2 += Math.pow( event.pageX-data.event.pageX, 2 ) 
				+ Math.pow( event.pageY-data.event.pageY, 2 ); 
			data.event = event; // store current event
			break;
		case 'mouseleave': // mouseout
			clearTimeout( data.timer ); // uncompare
			if ( data.hovered ){ 
				event.type = "hoverend"; // hijack event
				$.event.handle.call( this, event ); // handle "hoverend"
				data.hovered--; // reset flag
				}
			else $.event.remove( data.elem, "mousemove", hoverHandler ); // untrack
			break;
		default: // timeout compare // distance² = x² + y²  = ( speed * time )²
			if ( data.dist2  <= Math.pow( data.speed*( data.delay/1e3 ), 2 ) ){ // speed acceptable
				$.event.remove( data.elem, "mousemove", hoverHandler ); // untrack
				data.hovered++; // flag for "hoverend"
				data.event.type = "hover"; // hijack event
				if ( $.event.handle.call( data.elem, data.event ) === false ) // handle "hover"
					data.hovered--; // flag for "hoverend"
				}
			else data.timer = setTimeout( compare, data.delay ); // async recurse
			data.dist2 = 0; // reset distance² for next compare
			break;
		}
	function compare(){ hoverHandler( data ); }; // timeout/recursive function
	};
	
/*******************************************************************************************/
})(jQuery); // confine scope

}
/*
     FILE ARCHIVED ON 10:34:43 Aug 21, 2018 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 00:13:59 Jul 08, 2020.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  exclusion.robots: 0.253
  RedisCDXSource: 2.803
  PetaboxLoader3.resolve: 156.421 (2)
  exclusion.robots.policy: 0.238
  load_resource: 244.814
  PetaboxLoader3.datanode: 358.586 (5)
  esindex: 0.009
  CDXLines.iter: 13.328 (3)
  captures_list: 318.818
  LoadShardBlock: 299.189 (3)
*/