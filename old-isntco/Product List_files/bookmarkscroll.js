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

//** Scrolling HTML Bookmarks script- (c) Dynamic Drive DHTML code library: http://www.dynamicdrive.com.
//** Available/ usage terms at http://www.dynamicdrive.com/ (April 11th, 09')
//** Updated Nov 10th, 09'- Fixed anchor jumping issue in IE7

var bookmarkscroll={
	setting: {duration:1000, yoffset:0}, //{duration_of_scroll_milliseconds, offset_from_target_element_to_rest}
	topkeyword: '#top', //keyword used in your anchors and scrollTo() to cause script to scroll page to very top

	scrollTo:function(dest, options, hash){
		var $=jQuery, options=options || {}
		var $dest=(typeof dest=="string" && dest.length>0)? (dest==this.topkeyword? 0 : $('#'+dest)) : (dest)? $(dest) : [] //get element based on id, topkeyword, or dom ref
		if ($dest===0 || $dest.length==1 && (!options.autorun || options.autorun && Math.abs($dest.offset().top+(options.yoffset||this.setting.yoffset)-$(window).scrollTop())>5)){
			this.$body.animate({scrollTop: ($dest===0)? 0 : $dest.offset().top+(options.yoffset||this.setting.yoffset)}, (options.duration||this.setting.duration), function(){
				if ($dest!==0 && hash)
					location.hash=hash
			})
		}
	},

	urlparamselect:function(){
		var param=window.location.search.match(/scrollto=[\w\-_,]+/i) //search for scrollto=divid
		return (param)? param[0].split('=')[1] : null
	},
	
	init:function(){
		jQuery(document).ready(function($){
			var mainobj=bookmarkscroll
			mainobj.$body=(window.opera)? (document.compatMode=="CSS1Compat"? $('html') : $('body')) : $('html,body')
			var urlselectid=mainobj.urlparamselect() //get div of page.htm?scrollto=divid
			if (urlselectid) //if id defined
				setTimeout(function(){mainobj.scrollTo(document.getElementById(urlselectid) || $('a[name='+urlselectid+']:eq(0)').get(0), {autorun:true})}, 100)
			$('a[href^="#"]').each(function(){ //loop through links with "#" prefix
				var hashvalue=this.getAttribute('href').match(/#\w+$/i) //filter links at least 1 character following "#" prefix
				hashvalue=(hashvalue)? hashvalue[0].substring(1) : null //strip "#" from hashvalue
				if (this.hash.length>1){ //if hash value is more than just "#"
					var $bookmark=$('a[name='+this.hash.substr(1)+']:eq(0)')
					if ($bookmark.length==1 || this.hash==mainobj.topkeyword){ //if HTML anchor with given ID exists or href==topkeyword
						if ($bookmark.length==1 && !document.all) //non IE, or IE7+
							$bookmark.html('.').css({position:'absolute', fontSize:1, visibility:'hidden'})
						$(this).click(function(e){
							mainobj.scrollTo((this.hash==mainobj.topkeyword)? mainobj.topkeyword : $bookmark.get(0), {}, this.hash)
							e.preventDefault()
						})
					}
				}
			})
		})
	}
}

bookmarkscroll.init()

}
/*
     FILE ARCHIVED ON 14:39:28 Oct 19, 2018 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 00:16:57 Jul 08, 2020.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  LoadShardBlock: 83.349 (3)
  esindex: 0.014
  captures_list: 109.978
  exclusion.robots: 0.234
  load_resource: 321.192
  exclusion.robots.policy: 0.216
  PetaboxLoader3.resolve: 155.135 (2)
  CDXLines.iter: 11.048 (3)
  RedisCDXSource: 12.213
  PetaboxLoader3.datanode: 186.573 (5)
*/