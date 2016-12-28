#!/usr/bin/python
# -*- coding: utf-8 -*-
import re, os, urllib, sys, socket, string, time

reload(sys)
sys.setdefaultencoding('utf-8')  # Set utf-8 encoding, ignore IDE error promote


def getHtml(url):  # 获取网页源代码
    '''
    Ger website source context
    :param url: website url
    :return: the source content (String)
    '''
    page = urllib.urlopen(url)
    htmlSource = page.read()
    return htmlSource


def getVocabularyList(htmlSource):  # 获取列表中的单词
    '''
    Get word list from website source file
    :param htmlSource: the source content
    :return: list of word (list)
    '''
    reg = r'lang="en" word="([^\s]*?)"'
    mre = re.compile(reg)
    wordList = re.findall(mre, htmlSource)
    return wordList


def getVocabularyChineseDefineList(wordList):  # 获取单词列表的词典翻译
    '''
    Get whole word translation
    :param wordList: the English word list
    :return: Native translation list
    '''
    nativeWordList = []
    print "Total " + str(len(wordList)) + " Words"
    i = 1
    for word in wordList:
        if (i < 2000):
            nativeWordList.append(getVocabularyChineseDefine(word))
        else:
            nativeWordList.append("!!!!!")
        print str(i) + " word translated...  "
        print wordList[i - 1] + "  " + nativeWordList[i - 1]
        i = i + 1
    return nativeWordList


def getVocabularyChineseDefine(word):  # 获取单个单词的词典翻译,尽量少重复调用，防止封IP，
    # 如果网络不好请分段下载,可能有道翻译做了根据IP跳转，所以国外服务器不能跑啊
    '''
    Get single word translation from youdao
    :param word: English word
    :return:  native translation (String)
    '''
    bingBase = 'http://cn.bing.com/dict/search?q='
    reg = r'网络释义：(.*?)" \/>'
    mre = re.compile(reg)
    nativeWord = re.findall(mre, getHtml(bingBase + word))
    if (len(nativeWord) > 0):
        nativeWord = nativeWord[0]
    else:
        nativeWord = " "
    return nativeWord


def getVocabularyDefine(htmlSource):  # 获取列表中单词的定义
    '''
    Get english define from list
    :param htmlSource: the source content
    :return: word define list (list)
    '''
    reg = r'<div class="definition">(.*?)<\/div>'
    mre = re.compile(reg)
    wordDefineList = re.findall(mre, htmlSource)
    return wordDefineList


def getVocabularyExample(htmlSource):  # 获取单词的例句
    '''
    Get english sentences from list
    :param htmlSource: the source content
    :return: word sentence list (list)
    '''
    reg = r'<div class="example">([\s\S]*?)<\/div>'
    mre = re.compile(reg)
    picUrl = re.findall(mre, htmlSource)
    sentenceList = []
    for str in picUrl:
        str = str.replace("<strong>", "").replace("</strong>", "") \
            .replace("<br>", "").replace("\n", " ") \
            .replace("&nbsp;", " ") \
            .replace("\xe2\x80\x94", "") \
            # .replace("\x9c", "").replace("\x9d", "");
        str = re.sub('<a href.*?<\/a>', '', str)
        sentenceList.append(str)
    return sentenceList


def printToFile():
    for i in range(20):
        f = open("WordList " + str(i * 50 + 1) + "~" + str((i + 1) * 50), "w+")
        for j in range(50):
            f.write(vocabularyList[i * 50 + j] + "&&"
                    + nativeList[i * 50 + j] + " " + vocabularyDefine[i * 50 + j]
                    + " --- " + vocabularyExample[i * 50 + j] + "\n")


vocabularyURL = "https://www.vocabulary.com/lists/52473"

# textInfo = getHtml(vocabularyURL);   # 网络太慢，直接拷贝网站源代码吧
textInfo = '''



<!DOCTYPE html>
<html xmlns:vcom xmlns:fb>
<head>
	<title>The Vocabulary.com Top 1000 - Vocabulary List : Vocabulary.com</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
    <link rel="canonical" href="https://www.vocabulary.com/lists/52473" />

	<link rel="search" type="application/opensearchdescription+xml" href="https://www.vocabulary.com/search.xml" title="Vocabulary.com" />
	<link href="//cdn.vocab.com/images/ios-icons/114x114-off5pn.png" rel="apple-touch-icon" >
	<link href="//cdn.vocab.com/images/favicons/favicon-32x32-2frmtt.png" sizes="32x32" rel="icon" type="image/png" >
	<link href="//cdn.vocab.com/images/favicons/favicon-16x16-uf6i7e.png" sizes="16x16" rel="icon" type="image/png" >


	<link href="//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css">
	<link href="//cdn.vocab.com/css/3/header-s3n52z.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/3/main-s7x38o.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/3/grids-1440hlx.css" rel="stylesheet" type="text/css" >

	<link href="//cdn.vocab.com/css/progress-zjqx3f.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/dictionary-rlnzej.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/achievements-goaje8.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/leaderboards-1jskpje.css" rel="stylesheet" type="text/css" >

	<link href="//cdn.vocab.com/css/fonts/ss-social-circle-1708mdo.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/fonts/ss-symbolicons-block-1u3l0c5.css" rel="stylesheet" type="text/css" >
	<link href="//cdn.vocab.com/css/fonts/ss-standard-1nx9nw2.css" rel="stylesheet" type="text/css" >

	<link href="//cdn.vocab.com/css/wordlist2-1vgjs50.css" rel="stylesheet" type="text/css" >
<style>
	.filterMessage {
		font-size: 12px;
		background-color: #F9FDBA;
		color: #707070;
		padding: 8px;
		border-radius: 10px;
		margin-top: 1em;
		float: left;
	}
</style>


	<script>var loginData = {"validUser":false,"auth":{"loggedin":false},"perms":{},"points":0,"level":{"id":"L01","name":"Novice"}};</script>


<script src="//cdn.vocab.com/js/module-i5xbgv.js" type="text/javascript" ></script>

	<script>
	(function(){
		var deps=['vcom/usermenu', 'vcom/maintabs',  ]
		try { window.localStorage.setItem('x','1'); window.localStorage.removeItem('x'); } catch (e) {
			deps.unshift('localstorage');
		}
		Module.use(deps,{});
	})();
	</script>

	<script>
window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
ga('create', 'UA-154986-6', 'auto');
ga('set','dimension1','anon');
ga('send', 'pageview');
</script>

<script async src='https://www.google-analytics.com/analytics.js'></script>




	<script type='text/javascript' >
	var googletag = googletag || {};
	googletag.cmd = googletag.cmd || [];
	(function() {
	var gads = document.createElement('script');
	gads.async = true;
	gads.type = 'text/javascript';
	var useSSL = 'https:' == document.location.protocol;
	gads.src = (useSSL ? 'https:' : 'http:') +
	'//www.googletagservices.com/tag/js/gpt.js';
	var node = document.getElementsByTagName('script')[0];
	node.parentNode.insertBefore(gads, node);
	})();
	</script>
	<script>Module.use('vcom/adslots',{});</script>

	<script type="text/javascript">
Module.after(['params','jquery'],function() {

	jQuery(function($) {

		$('#wlOrder').on('change',function() {
			if (order[this.value]) {
				orderBy(order[this.value]);
			}
		});

		$('.page_wordlist .viewSelector a').on('click',function(){
			changeView($(this).data('view'));
		});

		function updateProgress() {
			$('.page_wordlist ol.wordlist i.progress').remove()
		$('.page_wordlist.learning li.learnable').each(function(){
				$('<i class="progress"/>').attr({
					'data-prg':this.getAttribute('prog'),
					'title':this.getAttribute('prog')+'% Mastered'
				}).appendTo(this);
		});
			}
		$('.page_wordlist').on('updateProgress',updateProgress);


		window.changeView = changeView;
		function changeView(view) {
			var lastHash = ''+hashParams;
			if (view=='notes') {
				delete hashParams.view;
			} else {
				hashParams.view = view;
			}
			$('#view_'+view).addClass('selected').siblings('a').removeClass('selected');
			if (view=='notes') {
				$('#wordlist').addClass('notesView').removeClass('listView').trigger('resize');
				} else {
				$('#wordlist').addClass('listView').removeClass('notesView').trigger('resize');
			}
			if (''+hashParams != lastHash)	setHash();
		}

		function orderBy(compare) {
			$('#wordlist li.entry').sort(compare).appendTo($('#wordlist').scrollTop(0));
			order.current=compare;
		}



		var order = {}
		order.alpha=function(a,b){
			a=a.getAttribute('word');
			b=b.getAttribute('word');
			var al = normalize(a);
			var bl = normalize(b);
			if (al==bl) {
				return a==b ? 0 : a<b ? -1 : 1;
			} else {
				return al<bl ? -1 : 1;
			}
		};

		function normalize(word) {
			return word.toLowerCase().replace(/[-\/\'\s]+/,'');
		}

		order.ralpha=reverse(order.alpha);
		order.freq=function(a,b){
			a=parseFloat(a.getAttribute('freq'));
			b=parseFloat(b.getAttribute('freq'));
			if (isNaN(a)) {
				return (isNaN(b)) ? 0 : 1;
			} else if (isNaN(b)) {
				return -1;
			}
			return (a==b) ? 0 : (a<b) ? -1 : 1;
		};
		order.rfreq=reverse(order.freq);
		order.natural=function(a,b) {
			a=parseInt(a.id.substring(5));
			b=parseInt(b.id.substring(5));
			return (a==b) ? 0 : (a<b) ? -1 : 1;
		}
		order.progress=function(a,b) {
			a=parseFloat(a.getAttribute('prog'));
			b=parseFloat(b.getAttribute('prog'));
			if (isNaN(a)) return isNaN(b) ? 0 : 1;
			if (isNaN(b)) return -1;
			return (a==b) ? 0 : (a<b) ? 1 : -1;
		}

		order.current = order.natural;

		function reverse(fn) {
			return function(a,b) { return -fn(a,b); }
		}

		var hashParams = null;
		function updateHash() {
			hashParams = new modules.params.Params((document.location.hash) ? document.location.hash.substring(0):'');
			changeView((hashParams.view=='list')?'list':'notes');
		}

		function setHash() {
			var hash = hashParams.toString();
			console.log('hash',hash+'');
			if (hash.length || !window.history) {
				document.location.hash= '#'+hashParams;
			} else {
				var loc = document.location.toString(), hm = loc.indexOf('#');
				window.history.replaceState({},document.title,loc.substring(0,hm));
			}
		}

		$(window).on('hashchange',updateHash);
		updateHash();
		updateProgress();
	});
});

</script>
	<script type="text/javascript">
	Module.after(['cookie','timezone'],function() {
		modules.cookie.Cookie.set('tz', modules.timezone.determine().name(), 3650, '/');
	});
	</script>

</head>
<body class="with-top-tab with-tab-lists top-section-lists  loggedout">
<div class="body-wrapper">
<header class="page-header noselect" role="banner"><div class="limited-width"><nav class="main">
		<a href="/" title="Vocabulary.com" class="logo" ><img src="//cdn.vocab.com/images/header/logo-1wobq9i.png" alt="Vocabulary.com" class="screen-only" ><img src="//cdn.vocab.com/images/logo-sar2cf.svg" class="print-only" ></a>
		<div class="logininfo"><a role="button" class="signin" href="/login">Sign In</a><a role="button" class="signup" href="/signup">Sign Up</a></div><button role="button" aria-pressed="false" aria-label="navigation menu" class="hamburger menu"><span class="rows"></span></button></nav><nav class="tabs"><ul  ><li title="Play Vocabulary.com" class="playTab"><a  href="/play/"><span>PLAY</span></a></li><li title="Look up a word" class="dictTab empty"><a href="/dictionary/"><span>LOOK UP</span></a><div class="wrapper"><input id="search" type="text" autofocus spellcheck="false" autocapitalize="off" autocomplete="off" autocorrect="off" ><i role="button" class="ss-delete" ></i></div></li><li title="Find a Vocabulary List" class="listsTab selected"><a href="/lists/"><span>LISTS</span></a></li></ul></nav></div></header>
<div class="fixed-tray"></div>


<div id="page" class="page">
<div id="pageContent" class="pageContent clearfloat">
<div class="page_wordlist view-words ">
	<div class="header with-header-margin">

		<div class="limited-width">
		<div class="grid grid-3 responsive">

		<div class="col span-2 leftpane">
		<div class="breadcrumb">
			<a class="level0" href="/lists">VOCABULARY LISTS</a>
			: <a class="level1" href="/lists/test-prep">TEST PREP</a>
		</div>
		<div class="titleblock">
			<h1 class="dynamictext">The Vocabulary.com Top 1000</h1>
			<div class="byline">
			<span class="date">May 19, 2011

			</span>

			<span class="author"><span class="profileLink">By <a href="/profiles/B0O97M2G11KL4B" target="_top">Vocabulary.com</a><span class="location"> (NY)</span><span class="badges"> <a href="#" target="_top" title="Vocabulary.com Moderator" class="badge moderator" ><img src="//cdn.vocab.com/images/profiles/mod-badge-sm-yugkxz.gif" alt="Vocabulary.com Moderator" class="badge" ></a></span></span></span>

			</div>


			<div class="description">The top 1,000 vocabulary words have been carefully chosen to represent difficult but common words that appear in everyday academic and business writing. These words are also the most likely to appear on the SAT, ACT, GRE, and ToEFL.
<br> To create this list, we started with the words that give our users the most trouble and then ranked them by how frequently they appear in our corpus of billions of words from edited sources. If you only have time to study one list of words, this is the list.<div role="button" class="readmore">Read more...</div></div>



		</div>
		<script>
		Module.after(['jquery'],function() {
			jQuery(function($){
				var $desc = $('.titleblock .description').addClass('v-overflow');
				$desc.find('.readmore').one('click',function(){
					$desc.toggleClass('open');
					$(window).off('resize orientationchange',reclamp);
				});
				function reclamp() {
					$desc.toggleClass('v-overflowed',$desc.length && $desc[0].scrollHeight > $desc.height());
				}
				$(window).on('resize orientationchange',reclamp);
				reclamp();
			});
		});
		</script>


			<div class="rating">
				<label>Rate this list:</label>
				<vcom:votes objid="52473" objtype="wl" cansave="true" objtypename="Vocabulary List" ></vcom:votes>
			</div>


		<section class="activities screen-only">
	<div class="clearfloat limited-width">
	<h3>Activities for this list:</h3>
	<ul >

		<li class="practice">
			<a href="/lists/52473/practice" class="card clearfloat">

			<h4><i></i>Practice</h4>
			<blockquote>
			Answer a few questions on each word on this list. <span class="hide-mobile">Get one wrong? We'll ask some follow-up questions.</span>
			Use it to prep for your next quiz!

			</blockquote>
			<div class="actions">



					<button>Start Practice Session</button>


			</div>
			</a>
		</li>

		<li class="spellingbee">
			<a href="/lists/52473/bee" class="card clearfloat">

			<h4><i></i>Spelling Bee</h4>
			<blockquote>
			Test your spelling acumen.  See the definition, listen to the word, then try to spell it correctly.
			<span class="hide-mobile">Beat your last streak, or best your overall time.  Spellers of the world, untie!</span>
			</blockquote>
			<div class="actions">
				<button>Start Spelling Bee</button>
			</div>
			</a>
		</li>
	</ul>

	<script>
	Module.after(['jquery'],function() {
		jQuery(function($){
			$('.page_wordlist').on('click','*[data-action="restart-practice"]',function(e){
				if (confirm('Are you sure you would like to restart your practice session?')) {
					document.location.href='/lists/52473/reset';
				}
				e.preventDefault();
				e.stopPropagation();
				return false;
			});
		});
	});
</script>
</div>
</section>


		</div>

		<div class="col rightpane" >

			<div class="item listprogress"></div>
			<div class="item tools" data-wordlist-id="52473"
			                        data-learning="false"
			                        data-learnable="1000"
			                        data-unlearnable="0"
			                        data-progress="0"
			                        data-bookmarked="false">

				<a class="button" href="/lists/52473/assign" ><i class="ss-attach icon"></i> Assign this list</a>
				<vcom:share itemtype="list" label="Share this list..." ></vcom:share>
				<a class="button print" href="javascript:void(0);" data-action="print"><i class="ss-fax icon"></i> Print this list</a>


				<a class="button" href="javascript:void(0);" data-action="copy"><i class="ss-fill icon"></i> Copy this list to...</a>
				<a class="button" href="/lists/new" ><i class="ss-compose icon"></i> Start a new list</a>
			</div>

			<script>Module.after('vcom/listtools');</script>
		</div>
		</div>
	</div>

</div>
	<div class="tabbar clearfloat">
	<div class="tabcontainer limited-width">


	<a class="selected" href="/lists/52473">1000&nbsp;Words</a>




	<a class="ss-attach assign"  href="/lists/52473/assign">Assignments</a>





	</div>
</div>


	<div class="content-wrapper"><div class="centeredContent">

	<div class="viewSelector">
		<label>show:</label>
		<a data-view="notes" href="#view=notes" id="view_notes">definitions &amp; notes</a>
		<a data-view="list" href="#view=list" id="view_list">only words</a>

		<select id="wlOrder">
		<option value="natural">in list order</option>
		<option value="alpha">from A to Z</option>
		<option value="ralpha">from Z to A</option>
		<option value="freq">from easy to hard</option>
		<option value="rfreq">from hard to easy</option>

	</select>

	</div>


	<ol class="wordlist notesView" id="wordlist">





<li class="entry learnable" id="entry0"
 lang="en" word="consider" freq="16.38" prog="0">

<a class="word dynamictext" href="/dictionary/consider">consider</a>
<div class="definition">deem to be</div>
<div class="example">At the moment, artemisinin-based therapies are
<strong>considered</strong> the best treatment, but cost about $10 per dose - far too much for impoverished communities.
<br> —
<a href="http://seattletimes.nwsource.com/html/health/2017518627_apeugermanymalariadrug.html?syndication=rss" rel="nofollow">Seattle Times (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry1"
 lang="en" word="minute" freq="24.91" prog="0">

<a class="word dynamictext" href="/dictionary/minute">minute</a>
<div class="definition">infinitely or immeasurably small</div>
<div class="example">The
<strong>minute</strong> stain on the document was not visible to the naked eye.</div>


</li>






<li class="entry learnable" id="entry2"
 lang="en" word="accord" freq="24.93" prog="0">

<a class="word dynamictext" href="/dictionary/accord">accord</a>
<div class="definition">concurrence of opinion</div>
<div class="example">The committee worked in
<strong>accord</strong> on the bill, and it eventually passed.</div>


</li>






<li class="entry learnable" id="entry3"
 lang="en" word="evident" freq="29.89" prog="0">

<a class="word dynamictext" href="/dictionary/evident">evident</a>
<div class="definition">clearly revealed to the mind or the senses or judgment</div>
<div class="example">That confidence was certainly
<strong>evident</strong> in the way Smith handled the winning play with 14 seconds left on the clock.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/sportsNews/~3/MO4-5RDu8TE/us-nfl-49ers-smith-idUSTRE80E0I420120115" rel="nofollow">Reuters (Jan 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry4"
 lang="en" word="practice" freq="32.07" prog="0">

<a class="word dynamictext" href="/dictionary/practice">practice</a>
<div class="definition">a customary way of operation or behavior</div>
<div class="example">He directed and acted in plays every season and became known for exploring Elizabethan theatre
<strong>practices</strong>.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/entertainment-arts-17055214" rel="nofollow">BBC (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry5"
 lang="en" word="intend" freq="35.65" prog="0">

<a class="word dynamictext" href="/dictionary/intend">intend</a>
<div class="definition">have in mind as a purpose</div>
<div class="example">“Lipstick, as a product
<strong>intended</strong> for topical use with limited absorption, is ingested only in very small quantities,” the agency said on its website.
<br> —
<a href="http://www.businessweek.com/news/2012-02-15/l-oreal-pink-petal-tops-list-of-400-lipsticks-containing-lead.html" rel="nofollow">BusinessWeek (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry6"
 lang="en" word="concern" freq="36.16" prog="0">

<a class="word dynamictext" href="/dictionary/concern">concern</a>
<div class="definition">something that interests you because it is important</div>
<div class="example">The scandal broke out in October after former chief executive Michael Woodford claimed he was fired for raising
<strong>concerns</strong> about the company's accounting practices.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/business-17054089" rel="nofollow">BBC (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry7"
 lang="en" word="commit" freq="36.58" prog="0">

<a class="word dynamictext" href="/dictionary/commit">commit</a>
<div class="definition">perform an act, usually with a negative connotation</div>
<div class="example">In an unprecedented front page article in 2003 The Times reported that Mr.&nbsp;Blair, a young reporter on its staff, had
<strong>committed</strong> journalistic fraud.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=741ae96c213e0c6e529698fbf0824b3b" rel="nofollow">New York Times (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry8"
 lang="en" word="issue" freq="41.47" prog="0">

<a class="word dynamictext" href="/dictionary/issue">issue</a>
<div class="definition">some situation or event that is thought about</div>
<div class="example">As a result, the privacy
<strong>issues</strong> surrounding mobile computing are becoming ever-more complex.
<br> —
<a href="http://feedproxy.google.com/~r/time/business/~3/f9bugNxUEus/" rel="nofollow">Time (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry9"
 lang="en" word="approach" freq="42.27" prog="0">

<a class="word dynamictext" href="/dictionary/approach">approach</a>
<div class="definition">move towards</div>
<div class="example">Spain’s jobless rate for people ages 16 to 24 is
<strong>approaching</strong> 50 percent.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=f8dfc38b7b9c38e37ad63e6b13dbd643" rel="nofollow">New York Times (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry10"
 lang="en" word="establish" freq="44.37" prog="0">

<a class="word dynamictext" href="/dictionary/establish">establish</a>
<div class="definition">set up or found</div>
<div class="example">A small French colony, Port Louis, was
<strong>established</strong> on East Falkland in 1764 and handed to the Spanish three years later.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/magazine-17045169" rel="nofollow">BBC (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry11"
 lang="en" word="utter" freq="45.01" prog="0">

<a class="word dynamictext" href="/dictionary/utter">utter</a>
<div class="definition">without qualification</div>
<div class="example">No one can blame an honest mechanic for holding a wealthy snob in
<strong>utter</strong> contempt.
<br> —
<a href="http://www.gutenberg.org/ebooks/38807" rel="nofollow">Ingersoll, Robert Green</a></div>


</li>






<li class="entry learnable" id="entry12"
 lang="en" word="conduct" freq="46.46" prog="0">

<a class="word dynamictext" href="/dictionary/conduct">conduct</a>
<div class="definition">direct the course of; manage or control</div>
<div class="example">Scientists have been
<strong>conducting</strong> studies of individual genes for years.
<br> —
<a href="http://www.businessweek.com/news/2012-02-15/harvard-mapping-my-dna-turns-scary-as-threatening-gene-emerges.html" rel="nofollow">BusinessWeek (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry13"
 lang="en" word="engage" freq="47.05" prog="0">

<a class="word dynamictext" href="/dictionary/engage">engage</a>
<div class="definition">consume all of one's attention or time</div>
<div class="example">We had nearly two hundred passengers, who were seated about on the sofas, reading, or playing games, or
<strong>engaged</strong> in conversation.
<br> —
<a href="http://www.gutenberg.org/ebooks/38869" rel="nofollow">Field, Henry M. (Henry Martyn)</a></div>


</li>






<li class="entry learnable" id="entry14"
 lang="en" word="obtain" freq="48.23" prog="0">

<a class="word dynamictext" href="/dictionary/obtain">obtain</a>
<div class="definition">come into possession of</div>
<div class="example">He delayed making the unclassified report public while awaiting an Army review, but Rolling Stone magazine
<strong>obtained</strong> the report and posted it Friday night.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=a094ecab5d5a801a22d5e9784c35df14" rel="nofollow">New York Times (Feb 11, 2012)</a></div>


</li>






<li class="entry learnable" id="entry15"
 lang="en" word="scarce" freq="49.44" prog="0">

<a class="word dynamictext" href="/dictionary/scarce">scarce</a>
<div class="definition">deficient in quantity or number compared with the demand</div>
<div class="example">Meanwhile, heating oil could grow more
<strong>scarce</strong> in the Northeast this winter, the Energy Department warned last month.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=bc4ae8a7dca11c165565ad93bf095bdc" rel="nofollow">New York Times (Jan 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry16"
 lang="en" word="policy" freq="54.33" prog="0">

<a class="word dynamictext" href="/dictionary/policy">policy</a>
<div class="definition">a plan of action adopted by an individual or social group</div>
<div class="example">Inflation has lagged behind the central bank’s 2 percent target, giving
<strong>policy</strong> makers extra scope to cut rates.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/Ga1Rl4qZzG8/sweden-s-riksbank-set-to-cut-rates-as-export-pain-deepens.html" rel="nofollow">BusinessWeek (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry17"
 lang="en" word="straight" freq="55.08" prog="0">

<a class="word dynamictext" href="/dictionary/straight">straight</a>
<div class="definition">successive, without a break</div>
<div class="example">After three
<strong>straight</strong> losing seasons, Hoosiers fans were just hoping for a winning record.
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2017518092_apbkct25northwestern.html?syndication=rss" rel="nofollow">Seattle Times (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry18"
 lang="en" word="stock" freq="55.5" prog="0">

<a class="word dynamictext" href="/dictionary/stock">stock</a>
<div class="definition">capital raised by a corporation through the issue of shares</div>
<div class="example">In other words, Apple’s
<strong>stock</strong> is cheap, and you should buy it.
<br> —
<a href="http://www.forbes.com/sites/davidthier/2012/02/16/apples-future-isnt-in-magic-its-in-math/" rel="nofollow">Forbes (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry19"
 lang="en" word="apparent" freq="56.65" prog="0">

<a class="word dynamictext" href="/dictionary/apparent">apparent</a>
<div class="definition">clearly revealed to the mind or the senses or judgment</div>
<div class="example">But the elderly creak is beginning to become
<strong>apparent</strong> in McCartney’s voice.
<br> —
<a href="http://feedproxy.google.com/~r/time/entertainment/~3/qLif_KgIm4I/" rel="nofollow">Time (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry20"
 lang="en" word="property" freq="57.16" prog="0">

<a class="word dynamictext" href="/dictionary/property">property</a>
<div class="definition">a basic or essential attribute shared by members of a class</div>
<div class="example">Owing to these magic
<strong>properties</strong>, it was often planted near dwellings to keep away evil spirits.
<br> —
<a href="http://www.gutenberg.org/ebooks/38886" rel="nofollow">Parsons, Mary Elizabeth</a></div>


</li>






<li class="entry learnable" id="entry21"
 lang="en" word="fancy" freq="58.41" prog="0">

<a class="word dynamictext" href="/dictionary/fancy">fancy</a>
<div class="definition">imagine; conceive of; see in one's mind</div>
<div class="example">For a time, indeed, he had
<strong>fancied</strong> that things were changed.
<br> —
<a href="http://www.gutenberg.org/ebooks/38871" rel="nofollow">Weyman, Stanley J.</a></div>


</li>






<li class="entry learnable" id="entry22"
 lang="en" word="concept" freq="58.97" prog="0">

<a class="word dynamictext" href="/dictionary/concept">concept</a>
<div class="definition">an abstract or general idea inferred from specific instances</div>
<div class="example">As a psychologist, I have always found the
<strong>concept</strong> of speed dating fascinating.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=4da5bb3ec873a4c841a9c2d7dd8a2c14" rel="nofollow">Scientific American (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry23"
 lang="en" word="court" freq="59.1" prog="0">

<a class="word dynamictext" href="/dictionary/court">court</a>
<div class="definition">an assembly to conduct judicial business</div>
<div class="example">When Brown pleaded not guilty to assaulting Rihanna, their violent past came out in
<strong>court</strong>.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/j8X-7WO04lY/click.phdo" rel="nofollow">Slate (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry24"
 lang="en" word="appoint" freq="59.5" prog="0">

<a class="word dynamictext" href="/dictionary/appoint">appoint</a>
<div class="definition">assign a duty, responsibility or obligation to</div>
<div class="example">In 1863 he was
<strong>appointed</strong> by the general assembly professor of oriental languages at New College.
<br> —
<a href="http://www.gutenberg.org/ebooks/38892" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry25"
 lang="en" word="passage" freq="60.1" prog="0">

<a class="word dynamictext" href="/dictionary/passage">passage</a>
<div class="definition">a section of text, particularly a section of medium length</div>
<div class="example">His interpretation of many obscure scriptural
<strong>passages</strong> by means of native manners and customs and traditions is particularly helpful and informing.
<br> —
<a href="http://www.gutenberg.org/ebooks/38881" rel="nofollow">Sheets, Emily Churchill Thompson</a></div>


</li>






<li class="entry learnable" id="entry26"
 lang="en" word="vain" freq="60.34" prog="0">

<a class="word dynamictext" href="/dictionary/vain">vain</a>
<div class="definition">unproductive of success</div>
<div class="example">An attempt was made to ignore this brilliant and irregular book, but in
<strong>vain</strong>; it was read all over Europe.
<br> —
<a href="http://www.gutenberg.org/ebooks/38892" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry27"
 lang="en" word="instance" freq="61.11" prog="0">

<a class="word dynamictext" href="/dictionary/instance">instance</a>
<div class="definition">an occurrence of something</div>
<div class="example">In many
<strong>instances</strong> large districts or towns would have fewer representatives than smaller ones, or perhaps none at all.
<br> —
<a href="http://www.gutenberg.org/ebooks/38874" rel="nofollow">Clarke, Helen Archibald</a></div>


</li>






<li class="entry learnable" id="entry28"
 lang="en" word="coast" freq="62.11" prog="0">

<a class="word dynamictext" href="/dictionary/coast">coast</a>
<div class="definition">the shore of a sea or ocean</div>
<div class="example">Martello towers must be built within short distances all round the
<strong>coast</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38862" rel="nofollow">Wingfield, Lewis</a></div>


</li>






<li class="entry learnable" id="entry29"
 lang="en" word="project" freq="63.04" prog="0">

<a class="word dynamictext" href="/dictionary/project">project</a>
<div class="definition">a planned undertaking</div>
<div class="example">The funds are aimed at helping build public
<strong>projects</strong> including mass transit, electricity networks, water utility and ports, it said.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/asiaindex/~3/h_wPfeXaye0/thai-mutual-fund-assets-to-accelerate-in-2012-on-infrastructure.html" rel="nofollow">BusinessWeek (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry30"
 lang="en" word="commission" freq="63.58" prog="0">

<a class="word dynamictext" href="/dictionary/commission">commission</a>
<div class="definition">a special group delegated to consider some matter</div>
<div class="example">The developers are now seeking approval from the landmarks
<strong>commission</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=63253539702f2ff206a1d24280e6d24f" rel="nofollow">New York Times (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry31"
 lang="en" word="constant" freq="63.6" prog="0">

<a class="word dynamictext" href="/dictionary/constant">constant</a>
<div class="definition">a quantity that does not vary</div>
<div class="example">In 1929, Hubble independently put forward and confirmed the same idea, and the parameter later became known as the Hubble
<strong>constant</strong>.
<br> —
<a href="http://feeds.nature.com/~r/nature/rss/current/~3/j3C22l1igXc/479150a" rel="nofollow">Nature (Nov 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry32"
 lang="en" word="circumstances" freq="64.7" prog="0">

<a class="word dynamictext" href="/dictionary/circumstances">circumstances</a>
<div class="definition">one's overall condition in life </div>
<div class="example">The
<strong>circumstances</strong> leading up to the shootings was not immediately available.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/arts/~3/X9VmHlQTwgE/chi-2-dead-5-others-wounded-at-shooting-at-south-side-liquor-store-20120219,0,4139587.story" rel="nofollow">Chicago Tribune (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry33"
 lang="en" word="constitute" freq="64.39" prog="0">

<a class="word dynamictext" href="/dictionary/constitute">constitute</a>
<div class="definition">to compose or represent</div>
<div class="example">Oil and natural gas
<strong>constituted</strong> almost 50 percent of Russian government revenue last year.
<br> —
<a href="http://www.businessweek.com/news/2012-02-19/oil-jump-buoys-fund-flows-as-n-y-stocks-climb-russia-overnight.html" rel="nofollow">BusinessWeek (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry34"
 lang="en" word="level" freq="65.59" prog="0">

<a class="word dynamictext" href="/dictionary/level">level</a>
<div class="definition">a relative position or degree of value in a graded group</div>
<div class="example">Only last month did the men’s and women’s unemployment rates reach the same
<strong>level</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1bd6b0bd3c217538e5e3cce776819bd5" rel="nofollow">New York Times (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry35"
 lang="en" word="affect" freq="67.76" prog="0">

<a class="word dynamictext" href="/dictionary/affect">affect</a>
<div class="definition">have an influence upon</div>
<div class="example">The central bank will start distributing low-interest loans in early March to individuals and small- and medium-sized companies
<strong>affected</strong> by the flooding.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/asiaindex/~3/HvpeoUGX8_0/thai-economy-shrinks-first-time-in-two-years-after-floods.html" rel="nofollow">BusinessWeek (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry36"
 lang="en" word="institute" freq="68.34" prog="0">

<a class="word dynamictext" href="/dictionary/institute">institute</a>
<div class="definition">set up or lay the groundwork for</div>
<div class="example">Corporations have to be more and more focused on
<strong>instituting</strong> higher labor standards.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=e4d2a0eeb0f2bcd2d9a683fcf443ef17" rel="nofollow">Washington Post (Feb 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry37"
 lang="en" word="render" freq="69.29" prog="0">

<a class="word dynamictext" href="/dictionary/render">render</a>
<div class="definition">give an interpretation of</div>
<div class="example">But authorities had
<strong>rendered</strong> the weapon and the explosive device inoperable, officials said.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/arts/~3/8eessV_m1ls/la-na-suicide-bomber-20120218,0,4225230.story" rel="nofollow">Chicago Tribune (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry38"
 lang="en" word="appeal" freq="72.01" prog="0">

<a class="word dynamictext" href="/dictionary/appeal">appeal</a>
<div class="definition">be attractive to</div>
<div class="example">To get traditional women’s accessories to
<strong>appeal</strong> to men, some designers are giving them manly names and styles.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1bd6b0bd3c217538e5e3cce776819bd5" rel="nofollow">New York Times (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry39"
 lang="en" word="generate" freq="72.5" prog="0">

<a class="word dynamictext" href="/dictionary/generate">generate</a>
<div class="definition">bring into existence</div>
<div class="example">Qualities such as these are not
<strong>generated</strong> under bad working practices of any sort.
<br> —
<a href="http://www.gutenberg.org/ebooks/38921" rel="nofollow">Hungerford, Edward</a></div>


</li>






<li class="entry learnable" id="entry40"
 lang="en" word="theory" freq="75.57" prog="0">

<a class="word dynamictext" href="/dictionary/theory">theory</a>
<div class="definition">a well-substantiated explanation of some aspect of the world</div>
<div class="example">Testing that
<strong>theory</strong> begins Saturday night, as the Capitals take on Tampa Bay in another important contest.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=36783693353333810cd28ce8022f5e4d" rel="nofollow">Washington Post (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry41"
 lang="en" word="range" freq="75.97" prog="0">

<a class="word dynamictext" href="/dictionary/range">range</a>
<div class="definition">a variety of different things or activities</div>
<div class="example">Like American community colleges, admission at an open university is not competitive, but the schools offer a
<strong>range</strong> of programs, including doctoral degrees.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/upoLO5iYoGs/0,8599,2107146,00.html" rel="nofollow">Time (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry42"
 lang="en" word="campaign" freq="76.75" prog="0">

<a class="word dynamictext" href="/dictionary/campaign">campaign</a>
<div class="definition">a race between candidates for elective office</div>
<div class="example">At the same point in 2004 — as an incumbent facing re-election — Mr. Bush had taken in about $145.6 million for his
<strong>campaign</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=edf352fe43ea8f78af9fda5597c4a83b" rel="nofollow">New York Times (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry43"
 lang="en" word="league" freq="77.72" prog="0">

<a class="word dynamictext" href="/dictionary/league">league</a>
<div class="definition">an association of sports teams that organizes matches</div>
<div class="example">"When I broke into the big
<strong>leagues</strong> until a month ago, Gary kept in touch," Mets third baseman David Wright said.
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2017536678_apbbocarterremembered.html?syndication=rss" rel="nofollow">Seattle Times (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry44"
 lang="en" word="labor" freq="78.33" prog="0">

<a class="word dynamictext" href="/dictionary/labor">labor</a>
<div class="definition">any piece of work that is undertaken or attempted</div>
<div class="example">More
<strong>labor</strong> is entailed, more time is required, greater delay is occasioned in cleaning up, and the amount of water used is much greater.
<br> —
<a href="http://www.gutenberg.org/ebooks/38903" rel="nofollow">Hoskin, Arthur J.</a></div>


</li>






<li class="entry learnable" id="entry45"
 lang="en" word="confer" freq="79.5" prog="0">

<a class="word dynamictext" href="/dictionary/confer">confer</a>
<div class="definition">have a meeting in order to talk something over</div>
<div class="example">Ms. Stewart said Mrs. Bachmann
<strong>conferred</strong> with her family and a few aides after her disappointing showing on Tuesday evening.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b74a1a450c267af675d609850b22d65d" rel="nofollow">New York Times (Jan 4, 2012)</a></div>


</li>






<li class="entry learnable" id="entry46"
 lang="en" word="grant" freq="80.51" prog="0">

<a class="word dynamictext" href="/dictionary/grant">grant</a>
<div class="definition">allow to have</div>
<div class="example">He had been
<strong>granted</strong> entry into the White House only for the daily briefing, later that afternoon.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c3f6b95af86b7f6ad608ad28a129456d" rel="nofollow">New York Times (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry47"
 lang="en" word="dwell" freq="80.52" prog="0">

<a class="word dynamictext" href="/dictionary/dwell">dwell</a>
<div class="definition">think moodily or anxiously about something</div>
<div class="example">But it is hardly necessary to
<strong>dwell</strong> on so normal an event.
<br> —
<a href="http://www.gutenberg.org/ebooks/38876" rel="nofollow">Vinogradoff, Paul</a></div>


</li>






<li class="entry learnable" id="entry48"
 lang="en" word="entertain" freq="81.81" prog="0">

<a class="word dynamictext" href="/dictionary/entertain">entertain</a>
<div class="definition">provide amusement for</div>
<div class="example">The first Super Bowl in 1967 featured college marching bands
<strong>entertaining</strong> the crowds at halftime.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/entertainment/~3/Xcd8xuq4uXY/us-superbowl-tv-idUSTRE8151Q020120207" rel="nofollow">Reuters (Feb 6, 2012)</a></div>


</li>






<li class="entry learnable" id="entry49"
 lang="en" word="contract" freq="83.11" prog="0">

<a class="word dynamictext" href="/dictionary/contract">contract</a>
<div class="definition">a binding agreement that is enforceable by law</div>
<div class="example"><strong>Contracts</strong> with utilities will be signed starting next month, he said.
<br> —
<a href="http://www.businessweek.com/news/2012-02-16/coal-india-may-revive-imports-to-comply-with-singh-s-order.html" rel="nofollow">BusinessWeek (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry50"
 lang="en" word="earnest" freq="83.77" prog="0">

<a class="word dynamictext" href="/dictionary/earnest">earnest</a>
<div class="definition">characterized by a firm, humorless belief in one's opinions</div>
<div class="example">Too much praise cannot be given to the
<strong>earnest</strong> and efficient missionaries who founded and have maintained this mission.
<br> —
<a href="http://www.gutenberg.org/ebooks/38815" rel="nofollow">Miller, George A.</a></div>


</li>






<li class="entry learnable" id="entry51"
 lang="en" word="yield" freq="85.89" prog="0">

<a class="word dynamictext" href="/dictionary/yield">yield</a>
<div class="definition">give or supply</div>
<div class="example">It is a very important honey plant, as it
<strong>yields</strong> an exceptionally pure nectar and remains in bloom a long time.
<br> —
<a href="http://www.gutenberg.org/ebooks/38886" rel="nofollow">Parsons, Mary Elizabeth</a></div>


</li>






<li class="entry learnable" id="entry52"
 lang="en" word="wander" freq="88.34" prog="0">

<a class="word dynamictext" href="/dictionary/wander">wander</a>
<div class="definition">move or cause to move in a sinuous or circular course</div>
<div class="example">While each animal
<strong>wandered</strong> through the maze, its brain was working furiously.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6a32131552aa8ac692f9b2f4f77a8f16" rel="nofollow">New York Times (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry53"
 lang="en" word="insist" freq="78.94" prog="0">

<a class="word dynamictext" href="/dictionary/insist">insist</a>
<div class="definition">be emphatic or resolute and refuse to budge</div>
<div class="example">Interior Department officials
<strong>insisted</strong> that they had conducted an extensive scientific inquiry before moving ahead with the spill response plan.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=829a9eb37e8afddffe7168d14b83d0a3" rel="nofollow">New York Times (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry54"
 lang="en" word="knight" freq="88.69" prog="0">

<a class="word dynamictext" href="/dictionary/knight">knight</a>
<div class="definition">a person of noble birth trained to arms and chivalry</div>
<div class="example">The
<strong>knight</strong> was gallant not only in war, but in love also.
<br> —
<a href="http://www.gutenberg.org/ebooks/38873" rel="nofollow">Crothers, Samuel McChord</a></div>


</li>






<li class="entry learnable" id="entry55"
 lang="en" word="convince" freq="89.31" prog="0">

<a class="word dynamictext" href="/dictionary/convince">convince</a>
<div class="definition">make realize the truth or validity of something</div>
<div class="example">But though he listened he was not
<strong>convinced</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38895" rel="nofollow">Reade, Charles</a></div>


</li>






<li class="entry learnable" id="entry56"
 lang="en" word="inspire" freq="89.32" prog="0">

<a class="word dynamictext" href="/dictionary/inspire">inspire</a>
<div class="definition">serve as the inciting cause of</div>
<div class="example">His surprising performance
<strong>inspired</strong> an outpouring of fan adoration that has been dubbed "Linsanity."
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/arts/~3/C6btCNuYrgo/sns-rt-us-nba-lin-espntre81h0gh-20120218,0,4997931.story" rel="nofollow">Chicago Tribune (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry57"
 lang="en" word="convention" freq="91.48" prog="0">

<a class="word dynamictext" href="/dictionary/convention">convention</a>
<div class="definition">a large formal assembly</div>
<div class="example">Last year, the industry’s main trade
<strong>convention</strong>, the Inside Self-Storage World Expo, organized workshops in Las Vegas focusing on lien laws and auction sales.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=5bd290fe41b753a36fcca8551bb1de53" rel="nofollow">New York Times (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry58"
 lang="en" word="skill" freq="92.7" prog="0">

<a class="word dynamictext" href="/dictionary/skill">skill</a>
<div class="definition">an ability that has been acquired by training</div>
<div class="example">He says many new drivers are terrified of motorway driving because they do not have the
<strong>skills</strong> or confidence needed.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/newsbeat/17093564" rel="nofollow">BBC (Feb 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry59"
 lang="en" word="harry" freq="94.64" prog="0">

<a class="word dynamictext" href="/dictionary/harry">harry</a>
<div class="definition">annoy continually or chronically</div>
<div class="example">There’s something uplifting about hearing a string instrument when I’m feeling ragged or
<strong>harried</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1769ad94d73121b3a4f80c0e234643ba" rel="nofollow">New York Times (Feb 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry60"
 lang="en" word="financial" freq="95.49" prog="0">

<a class="word dynamictext" href="/dictionary/financial">financial</a>
<div class="definition">involving fiscal matters</div>
<div class="example">Meanwhile, universities have raised tuition every year, putting many students in a
<strong>financial</strong> bind.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=dc0c440021cb8b0511d38c40302a9cc9" rel="nofollow">New York Times (Feb 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry61"
 lang="en" word="reflect" freq="61.02" prog="0">

<a class="word dynamictext" href="/dictionary/reflect">reflect</a>
<div class="definition">show an image of</div>
<div class="example">Teens ranting over chores and whatnot can often
<strong>reflect</strong> deeper feelings of alienation or perceived uncaring on the part of parents.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/imfaMIMxR0U/" rel="nofollow">Time (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry62"
 lang="en" word="novel" freq="96.86" prog="0">

<a class="word dynamictext" href="/dictionary/novel">novel</a>
<div class="definition">an extended fictional work in prose</div>
<div class="example">Before Robert Barr publishes a
<strong>novel</strong> he spends years in thinking the thing out.
<br> —
<a href="http://www.gutenberg.org/ebooks/38887" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry63"
 lang="en" word="furnish" freq="97.01" prog="0">

<a class="word dynamictext" href="/dictionary/furnish">furnish</a>
<div class="definition">provide or equip with furniture</div>
<div class="example">Instead, according to court documents, the money went toward
<strong>furnishing</strong> mansions, flying in private jets, and retaining a $120,000-a-year personal hairstylist.
<br> —
<a href="http://www.businessweek.com/magazine/the-dodgers-allstar-lineup-of-suitors-02012012.html" rel="nofollow">BusinessWeek (Feb 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry64"
 lang="en" word="compel" freq="97.22" prog="0">

<a class="word dynamictext" href="/dictionary/compel">compel</a>
<div class="definition">force somebody to do something</div>
<div class="example">But the flames grew too large,
<strong>compelling</strong> firefighters to call off the rescue.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b71ddd1a90e3280a29fa5e6c17de0fdb" rel="nofollow">New York Times (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry65"
 lang="en" word="venture" freq="98.96" prog="0">

<a class="word dynamictext" href="/dictionary/venture">venture</a>
<div class="definition">proceed somewhere despite the risk of possible dangers</div>
<div class="example">Clearly he would not
<strong>venture</strong> to descend while his enemy moved.
<br> —
<a href="http://www.gutenberg.org/ebooks/38795" rel="nofollow">Strang, Herbert</a></div>


</li>






<li class="entry learnable" id="entry66"
 lang="en" word="territory" freq="99.54" prog="0">

<a class="word dynamictext" href="/dictionary/territory">territory</a>
<div class="definition">the geographical area under the jurisdiction of a state</div>
<div class="example">On Friday, West Africa regional group Ecowas condemned the rebels, urging them to end hostilities and surrender all occupied
<strong>territory</strong>.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-africa-17082365" rel="nofollow">BBC (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry67"
 lang="en" word="temper" freq="103.42" prog="0">

<a class="word dynamictext" href="/dictionary/temper">temper</a>
<div class="definition">a characteristic state of feeling</div>
<div class="example">Oscar Wilde, to do him justice, bore this sort of rebuff with astonishing good
<strong>temper</strong> and sweetness.
<br> —
<a href="http://www.gutenberg.org/ebooks/38916" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry68"
 lang="en" word="bent" freq="106.48" prog="0">

<a class="word dynamictext" href="/dictionary/bent">bent</a>
<div class="definition">fixed in your purpose</div>
<div class="example">The business-oriented constituency of the Republican Party, Jacobs said, has been weakened by a faction
<strong>bent</strong> on lowering taxes and cutting spending.
<br> —
<a href="http://www.businessweek.com/news/2012-02-17/minneapolis-football-stadium-subsidy-blocked-by-taxpayer-anger.html" rel="nofollow">BusinessWeek (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry69"
 lang="en" word="intimate" freq="107.62" prog="0">

<a class="word dynamictext" href="/dictionary/intimate">intimate</a>
<div class="definition">marked by close acquaintance, association, or familiarity</div>
<div class="example">The female spider can choose when to cut off
<strong>intimate</strong> relations by eating her partner, or kicking him out.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=cd186c93f4cdebe99863ede310750b8d" rel="nofollow">Scientific American (Jan 31, 2012)</a></div>


</li>






<li class="entry learnable" id="entry70"
 lang="en" word="undertake" freq="108" prog="0">

<a class="word dynamictext" href="/dictionary/undertake">undertake</a>
<div class="definition">enter upon an activity or enterprise</div>
<div class="example">An autopsy has reportedly been
<strong>undertaken</strong> but the results are not expected for several weeks.
<br> —
<a href="http://www.guardian.co.uk/film/2012/feb/13/whitney-houston-film-sparkle-release" rel="nofollow">The Guardian (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry71"
 lang="en" word="majority" freq="108.69" prog="0">

<a class="word dynamictext" href="/dictionary/majority">majority</a>
<div class="definition"> more than half of the votes in an election</div>
<div class="example">Republicans need just four seats in the Senate to take control as the
<strong>majority</strong> party.
<br> —
<a href="http://feeds.reuters.com/~r/Reuters/PoliticsNews/~3/JBTjg4qYODY/us-usa-campaign-spending-shepac-idUSTRE81623H20120207" rel="nofollow">Reuters (Feb 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry72"
 lang="en" word="assert" freq="109.2" prog="0">

<a class="word dynamictext" href="/dictionary/assert">assert</a>
<div class="definition">declare or affirm solemnly and formally as true</div>
<div class="example">In your talk you
<strong>asserted</strong> the pill's risks of blood clotting, lung artery blockage, heart attack and stroke are minimal.
<br> —
<a href="http://news.sciencemag.org/sciencenow/2012/02/q-and-a-the-50th-anniversary-of-.html?rss=1" rel="nofollow">Science Magazine (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry73"
 lang="en" word="crew" freq="111.51" prog="0">

<a class="word dynamictext" href="/dictionary/crew">crew</a>
<div class="definition">the men and women who man a vehicle</div>
<div class="example">Several pilots and
<strong>crew</strong> members would have to escape at once, while safety divers watched, ready to rescue anyone who became stuck.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=8310d7da01bc1793245c2e8f18272ee9" rel="nofollow">New York Times (Feb 6, 2012)</a></div>


</li>






<li class="entry learnable" id="entry74"
 lang="en" word="chamber" freq="112.98" prog="0">

<a class="word dynamictext" href="/dictionary/chamber">chamber</a>
<div class="definition">a natural or artificial enclosed space</div>
<div class="example">"Today," said the old man, "you must push through with me into my most solitary
<strong>chamber</strong>, that we may not be disturbed."
<br> —
<a href="http://www.gutenberg.org/ebooks/38779" rel="nofollow">Carlyle, Thomas</a></div>


</li>






<li class="entry learnable" id="entry75"
 lang="en" word="humble" freq="113.28" prog="0">

<a class="word dynamictext" href="/dictionary/humble">humble</a>
<div class="definition">marked by meekness or modesty; not arrogant or prideful</div>
<div class="example">“Challenging yourself, playing up against stronger, tougher, and overall better competition will keep you
<strong>humble</strong>.”
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=61a30ce69f6b466d21029e123c4deafe" rel="nofollow">Washington Post (Jan 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry76"
 lang="en" word="scheme" freq="113.77" prog="0">

<a class="word dynamictext" href="/dictionary/scheme">scheme</a>
<div class="definition">an elaborate and systematic plan of action</div>
<div class="example">Some companies in the Globe District of Arizona have started extensive underground
<strong>schemes</strong> for mining large tonnages very cheaply by "caving" methods.
<br> —
<a href="http://www.gutenberg.org/ebooks/38903" rel="nofollow">Hoskin, Arthur J.</a></div>


</li>






<li class="entry learnable" id="entry77"
 lang="en" word="keen" freq="114.85" prog="0">

<a class="word dynamictext" href="/dictionary/keen">keen</a>
<div class="definition">demonstrating ability to recognize or draw fine distinctions</div>
<div class="example">Not one of his movements escaped her
<strong>keen</strong> observation; she drank in every shiver.
<br> —
<a href="http://www.gutenberg.org/ebooks/38863" rel="nofollow">Wingfield, Lewis</a></div>


</li>






<li class="entry learnable" id="entry78"
 lang="en" word="liberal" freq="111.23" prog="0">

<a class="word dynamictext" href="/dictionary/liberal">liberal</a>
<div class="definition">having political views favoring reform and progress</div>
<div class="example">Romney’s actually done well in open primaries where fiscally conservative yet socially
<strong>liberal</strong> independents have backed him over his opponents.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/EyYlnYF0xYY/" rel="nofollow">Time (Feb 14, 2012)</a></div>


</li>






<li class="entry learnable" id="entry79"
 lang="en" word="despair" freq="117.43" prog="0">

<a class="word dynamictext" href="/dictionary/despair">despair</a>
<div class="definition">a state in which all hope is lost or absent</div>
<div class="example">There were wounded love, and wounded pride, and
<strong>despair</strong>, and coming madness, all in that piteous cry.
<br> —
<a href="http://www.gutenberg.org/ebooks/38895" rel="nofollow">Reade, Charles</a></div>


</li>






<li class="entry learnable" id="entry80"
 lang="en" word="tide" freq="117.68" prog="0">

<a class="word dynamictext" href="/dictionary/tide">tide</a>
<div class="definition">the periodic rise and fall of the sea level</div>
<div class="example">In the case of mobile connectivity, a rising
<strong>tide</strong> does not lift all boats.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/xT7NFSEcKNo/click.phdo" rel="nofollow">Slate (Feb 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry81"
 lang="en" word="attitude" freq="118.37" prog="0">

<a class="word dynamictext" href="/dictionary/attitude">attitude</a>
<div class="definition">a complex mental state involving beliefs and feelings</div>
<div class="example">"Behaviours have changed and
<strong>attitudes</strong> have changed," Mr Taylor said.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-us-canada-17070731" rel="nofollow">BBC (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry82"
 lang="en" word="justify" freq="118.43" prog="0">

<a class="word dynamictext" href="/dictionary/justify">justify</a>
<div class="definition">show to be reasonable or provide adequate ground for</div>
<div class="example">He felt sure that if the circumstances
<strong>justified</strong> it, the necessary proceedings could be taken.”
<br> —
<a href="http://www.gutenberg.org/ebooks/38916" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry83"
 lang="en" word="flag" freq="120.36" prog="0">

<a class="word dynamictext" href="/dictionary/flag">flag</a>
<div class="definition">a rectangular piece of cloth of distinctive design</div>
<div class="example">Palestinian President Mahmoud Abbas declared three days of mourning and ordered
<strong>flags</strong> flown at half staff.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=472f9efb4b905e80a7b221460b065703" rel="nofollow">New York Times (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry84"
 lang="en" word="merit" freq="123.51" prog="0">

<a class="word dynamictext" href="/dictionary/merit">merit</a>
<div class="definition">any admirable or beneficial attribute</div>
<div class="example">Thus far in our inquiry extraordinary
<strong>merits</strong> have been offset by extraordinary defects.
<br> —
<a href="http://www.gutenberg.org/ebooks/38280" rel="nofollow">Ayres, Harry Morgan</a></div>


</li>






<li class="entry learnable" id="entry85"
 lang="en" word="manifest" freq="126.01" prog="0">

<a class="word dynamictext" href="/dictionary/manifest">manifest</a>
<div class="definition">reveal its presence or make an appearance</div>
<div class="example">A too rapid transformation of existing conditions might very easily lead to an economic crisis, symptoms of which are already beginning to
<strong>manifest</strong> themselves.
<br> —
<a href="http://www.gutenberg.org/ebooks/38508" rel="nofollow">Vay, P?ter</a></div>


</li>






<li class="entry learnable" id="entry86"
 lang="en" word="notion" freq="132.58" prog="0">

<a class="word dynamictext" href="/dictionary/notion">notion</a>
<div class="definition">a general inclusive concept</div>
<div class="example">Does that old
<strong>notion</strong> that defense wins championships still hold up these days?
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2017229696_apfbnsaints49ers.html?syndication=rss" rel="nofollow">Seattle Times (Jan 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry87"
 lang="en" word="scale" freq="134.12" prog="0">

<a class="word dynamictext" href="/dictionary/scale">scale</a>
<div class="definition">relative magnitude</div>
<div class="example">And there might not be much money, so fashion shows are done on a much smaller
<strong>scale</strong>.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2017532833_apusfeanyfashionweekupandcomers.html?syndication=rss" rel="nofollow">Seattle Times (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry88"
 lang="en" word="formal" freq="134.41" prog="0">

<a class="word dynamictext" href="/dictionary/formal">formal</a>
<div class="definition">characteristic of or befitting a person in authority</div>
<div class="example">A
<strong>formal</strong> decision to call off the search is likely on Wednesday, rescue officials said.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=19dfbe68db37bd53bcbde670f99e7791" rel="nofollow">New York Times (Jan 31, 2012)</a></div>


</li>






<li class="entry learnable" id="entry89"
 lang="en" word="resource" freq="139.37" prog="0">

<a class="word dynamictext" href="/dictionary/resource">resource</a>
<div class="definition">a new or reserve supply that can be drawn upon when needed</div>
<div class="example">“Economists assume that, under normal conditions, markets will allocate
<strong>resources</strong> efficiently,” he added.
<br> —
<a href="http://www.businessweek.com/news/2012-02-17/santorum-picks-own-winners-and-losers-even-as-he-chides-obama.html" rel="nofollow">BusinessWeek (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry90"
 lang="en" word="persist" freq="154.09" prog="0">

<a class="word dynamictext" href="/dictionary/persist">persist</a>
<div class="definition">continue to exist</div>
<div class="example">Old ideas, long after the conditions under which they were produced have passed away, often
<strong>persist</strong> in surviving.
<br> —
<a href="http://www.gutenberg.org/ebooks/38806" rel="nofollow">Ingersoll, Robert Green</a></div>


</li>






<li class="entry learnable" id="entry91"
 lang="en" word="contempt" freq="155.44" prog="0">

<a class="word dynamictext" href="/dictionary/contempt">contempt</a>
<div class="definition">lack of respect accompanied by a feeling of intense dislike</div>
<div class="example">And with his backhanded
<strong>contempt</strong> for all things ordinary, Blake is making some of the catchiest, most difficult music in recent memory.
<br> —
<a href="http://feedproxy.google.com/~r/time/entertainment/~3/QJc7kyec9yc/" rel="nofollow">Time (Dec 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry92"
 lang="en" word="tour" freq="107.52" prog="0">

<a class="word dynamictext" href="/dictionary/tour">tour</a>
<div class="definition">a route all the way around a particular place or area</div>
<div class="example">He typed in “South Park” and took senior executives on a
<strong>tour</strong> of Web sites offering pirated episodes.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b7e742cb8bb1022fd370336ff400b169" rel="nofollow">New York Times (Feb 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry93"
 lang="en" word="plead" freq="160.48" prog="0">

<a class="word dynamictext" href="/dictionary/plead">plead</a>
<div class="definition">enter a defendant's answer</div>
<div class="example">Aria
<strong>pleaded</strong> not guilty, but he acknowledged that he had violated some laws.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=761b724e0eaf676e5c33f916ae14d26f" rel="nofollow">New York Times (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry94"
 lang="en" word="weigh" freq="161.51" prog="0">

<a class="word dynamictext" href="/dictionary/weigh">weigh</a>
<div class="definition">be oppressive or burdensome</div>
<div class="example">So far, the political turmoil has not appeared to have discouraged visitors, but prolonged strife could
<strong>weigh</strong> on tourism.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6ad91531375ac703ed7de184f0b73c07" rel="nofollow">New York Times (Feb 11, 2012)</a></div>


</li>






<li class="entry learnable" id="entry95"
 lang="en" word="mode" freq="161.79" prog="0">

<a class="word dynamictext" href="/dictionary/mode">mode</a>
<div class="definition">how something is done or how it happens</div>
<div class="example">Speaking of science, he says, in language far in advance of his times: ‘There are two
<strong>modes</strong> of knowing—by argument and by experiment.
<br> —
<a href="http://www.gutenberg.org/ebooks/38763" rel="nofollow">Adams, W. H. Davenport (William Henry Davenport)</a></div>


</li>






<li class="entry learnable" id="entry96"
 lang="en" word="distinction" freq="164.02" prog="0">

<a class="word dynamictext" href="/dictionary/distinction">distinction</a>
<div class="definition">a discrimination between things as different</div>
<div class="example">But such a
<strong>distinction</strong> is quite external; at heart the men may be very much alike.
<br> —
<a href="http://www.gutenberg.org/ebooks/38887" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry97"
 lang="en" word="inclined" freq="166.33" prog="0">

<a class="word dynamictext" href="/dictionary/inclined">inclined</a>
<div class="definition">at an angle to the horizontal or vertical position</div>
<div class="example">Such an
<strong>inclined</strong> passage following a seam of coal is known as a slope.
<br> —
<a href="http://www.gutenberg.org/ebooks/38903" rel="nofollow">Hoskin, Arthur J.</a></div>


</li>






<li class="entry learnable" id="entry98"
 lang="en" word="attribute" freq="167.16" prog="0">

<a class="word dynamictext" href="/dictionary/attribute">attribute</a>
<div class="definition">a quality belonging to or characteristic of an entity</div>
<div class="example">The authors found that when the available prospects varied more in
<strong>attributes</strong> such as age, height, occupation and educational background, people made fewer dating proposals.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=4da5bb3ec873a4c841a9c2d7dd8a2c14" rel="nofollow">Scientific American (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry99"
 lang="en" word="exert" freq="168.36" prog="0">

<a class="word dynamictext" href="/dictionary/exert">exert</a>
<div class="definition">make a great effort at a mental or physical task</div>
<div class="example">School boards may come to
<strong>exert</strong> even greater influence over what students read.
<br> —
<a href="http://www.forbes.com/sites/erikkain/2012/01/23/our-digital-book-future-turning-a-new-virtual-page-in-human-evolution/" rel="nofollow">Forbes (Jan 23, 2012)</a></div>


</li>






<li class="entry learnable" id="entry100"
 lang="en" word="oppress" freq="170.91" prog="0">

<a class="word dynamictext" href="/dictionary/oppress">oppress</a>
<div class="definition">come down on or keep down by unjust use of one's authority</div>
<div class="example">Those who managed to survive were later
<strong>oppressed</strong> by Poland's post-war communist authorities.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/entertainment/~3/0nFQX1cPhug/us-poland-holocaust-film-idUSTRE80H0Y320120118" rel="nofollow">Reuters (Jan 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry101"
 lang="en" word="contend" freq="175.36" prog="0">

<a class="word dynamictext" href="/dictionary/contend">contend</a>
<div class="definition">compete for something</div>
<div class="example">But eight men, however bold and stout-hearted, could not long
<strong>contend</strong> with an enemy at least four times their number.
<br> —
<a href="http://www.gutenberg.org/ebooks/38795" rel="nofollow">Strang, Herbert</a></div>


</li>






<li class="entry learnable" id="entry102"
 lang="en" word="stake" freq="177.94" prog="0">

<a class="word dynamictext" href="/dictionary/stake">stake</a>
<div class="definition">a strong wooden or metal post driven into the ground</div>
<div class="example">His remains were buried in Cannon Street, and a
<strong>stake</strong> was driven through the body.
<br> —
<a href="http://www.gutenberg.org/ebooks/38905" rel="nofollow">Andrews, William</a></div>


</li>






<li class="entry learnable" id="entry103"
 lang="en" word="toil" freq="179.49" prog="0">

<a class="word dynamictext" href="/dictionary/toil">toil</a>
<div class="definition">work hard</div>
<div class="example">He
<strong>toiled</strong> in the sweat of his brow, tilling the stubborn ground, taking out stones, building fences.
<br> —
<a href="http://www.gutenberg.org/ebooks/38730" rel="nofollow">Adler, Felix</a></div>


</li>






<li class="entry learnable" id="entry104"
 lang="en" word="perish" freq="180.44" prog="0">

<a class="word dynamictext" href="/dictionary/perish">perish</a>
<div class="definition">pass from physical life</div>
<div class="example">Simon Wiesenthal's parents are long since deceased, with his father dying in World War I and his mother
<strong>perishing</strong> in the Holocaust.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-us-canada-17036046" rel="nofollow">BBC (Feb 14, 2012)</a></div>


</li>






<li class="entry learnable" id="entry105"
 lang="en" word="disposition" freq="181.69" prog="0">

<a class="word dynamictext" href="/dictionary/disposition">disposition</a>
<div class="definition">your usual mood</div>
<div class="example">Melancholia — the state of mind — can hide behind seemingly sunny
<strong>dispositions</strong>.
<br> —
<a href="http://seattletimes.nwsource.com/html/thearts/2017112801_weekahead01.html?syndication=rss" rel="nofollow">Seattle Times (Dec 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry106"
 lang="en" word="rail" freq="187" prog="0">

<a class="word dynamictext" href="/dictionary/rail">rail</a>
<div class="definition">complain bitterly</div>
<div class="example">Mr. Gray
<strong>railed</strong> against lengthy stage directions, saying he crossed them out in scripts before he would begin rehearsals with his actors.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=f09b7a796696eed59765b98c7585ed48" rel="nofollow">New York Times (Feb 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry107"
 lang="en" word="cardinal" freq="188.31" prog="0">

<a class="word dynamictext" href="/dictionary/cardinal">cardinal</a>
<div class="definition">one of a group of prominent bishops in the Sacred College</div>
<div class="example">Each time he names
<strong>cardinals</strong> he puts his stamp on Roman Catholicism's future by choosing men who share his views.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/arts/~3/goivEXoY7VA/sns-rt-us-pope-consistorytre81h09x-20120218,0,3414816.story" rel="nofollow">Chicago Tribune (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry108"
 lang="en" word="boast" freq="191.56" prog="0">

<a class="word dynamictext" href="/dictionary/boast">boast</a>
<div class="definition">show off</div>
<div class="example">Mr. Estes was also well connected politically,
<strong>boasting</strong> that the president of the United States took his calls.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=677c11dc275e27aaf052db065765f575" rel="nofollow">New York Times (Dec 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry109"
 lang="en" word="advocate" freq="191.83" prog="0">

<a class="word dynamictext" href="/dictionary/advocate">advocate</a>
<div class="definition">a person who pleads for a person, cause, or idea</div>
<div class="example">Well, safety
<strong>advocates</strong>, consumers and the government dragged the automobile industry toward including seat belts, air bags, more visible taillights and other safety features.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2d3fbbb5dda4e6dfce2fa8920b8eabba" rel="nofollow">New York Times (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry110"
 lang="en" word="bestow" freq="193.13" prog="0">

<a class="word dynamictext" href="/dictionary/bestow">bestow</a>
<div class="definition">present</div>
<div class="example">He
<strong>bestowed</strong> public buildings and river improvements in return for votes.
<br> —
<a href="http://www.gutenberg.org/ebooks/38819" rel="nofollow">Gilbert, Clinton W. (Clinton Wallace)</a></div>


</li>






<li class="entry learnable" id="entry111"
 lang="en" word="allege" freq="193.55" prog="0">

<a class="word dynamictext" href="/dictionary/allege">allege</a>
<div class="definition">report or maintain</div>
<div class="example">It is being fired into enclosed areas and homes, the human rights group
<strong>alleges</strong>.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-middle-east-16931206" rel="nofollow">BBC (Feb 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry112"
 lang="en" word="notwithstanding" freq="193.95" prog="0">

<a class="word dynamictext" href="/dictionary/notwithstanding">notwithstanding</a>
<div class="definition">despite anything to the contrary</div>
<div class="example">He seems to have taken things easily enough,
<strong>notwithstanding</strong> the sorrow and suffering that surrounded him on every side.
<br> —
<a href="http://www.gutenberg.org/ebooks/38763" rel="nofollow">Adams, W. H. Davenport (William Henry Davenport)</a></div>


</li>






<li class="entry learnable" id="entry113"
 lang="en" word="lofty" freq="194.91" prog="0">

<a class="word dynamictext" href="/dictionary/lofty">lofty</a>
<div class="definition">of imposing height; especially standing out above others</div>
<div class="example">He found himself in an enormous hall with a
<strong>lofty</strong> ceiling.
<br> —
<a href="http://www.gutenberg.org/ebooks/38458" rel="nofollow">Blasco Ib??ez, Vicente</a></div>


</li>






<li class="entry learnable" id="entry114"
 lang="en" word="multitude" freq="196.75" prog="0">

<a class="word dynamictext" href="/dictionary/multitude">multitude</a>
<div class="definition">a large indefinite number</div>
<div class="example">Department store chains in general have been strained in recent years as a "
<strong>multitude</strong>" of alternatives has emerged, all competing for customers.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/business/~3/p3Ix5xpYhAI/chi-listing-of-sears-kmart-closures-not-certain-yet-20111228,0,3259304.story" rel="nofollow">Chicago Tribune (Dec 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry115"
 lang="en" word="steep" freq="197.17" prog="0">

<a class="word dynamictext" href="/dictionary/steep">steep</a>
<div class="definition">having a sharp inclination</div>
<div class="example">It was narrow and very
<strong>steep</strong>, and had precipices in all parts, so that they could not mount upward except one at a time.
<br> —
<a href="http://www.gutenberg.org/ebooks/38748" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry116"
 lang="en" word="heed" freq="202.8" prog="0">

<a class="word dynamictext" href="/dictionary/heed">heed</a>
<div class="definition">pay close attention to</div>
<div class="example">But Cain was already too far gone to
<strong>heed</strong> the warning voice.
<br> —
<a href="http://www.gutenberg.org/ebooks/38730" rel="nofollow">Adler, Felix</a></div>


</li>






<li class="entry learnable" id="entry117"
 lang="en" word="modest" freq="208.4" prog="0">

<a class="word dynamictext" href="/dictionary/modest">modest</a>
<div class="definition">not large but sufficient in size or amount</div>
<div class="example">A healthy person living in an unfashionable city with no student loans to pay off can get by on a fairly
<strong>modest</strong> income.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/1FfoOGlJkI8/click.phdo" rel="nofollow">Slate (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry118"
 lang="en" word="partial" freq="213.59" prog="0">

<a class="word dynamictext" href="/dictionary/partial">partial</a>
<div class="definition">being or affecting only a segment</div>
<div class="example">Generalizations of this sweeping order are apt to contain only
<strong>partial</strong> truth.
<br> —
<a href="http://www.gutenberg.org/ebooks/38874" rel="nofollow">Clarke, Helen Archibald</a></div>


</li>






<li class="entry learnable" id="entry119"
 lang="en" word="apt" freq="215.48" prog="0">

<a class="word dynamictext" href="/dictionary/apt">apt</a>
<div class="definition">naturally disposed toward</div>
<div class="example">Another reason to display beds at an electronics show: consumers are
<strong>apt</strong> to use high-tech devices while tucked in.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=38f50c4041e47326d3b46accf96ecb2e" rel="nofollow">New York Times (Jan 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry120"
 lang="en" word="esteem" freq="215.88" prog="0">

<a class="word dynamictext" href="/dictionary/esteem">esteem</a>
<div class="definition">the condition of being honored</div>
<div class="example">Despite being held in the highest
<strong>esteem</strong> by his fellow poets, Redgrove never quite achieved the critical reception or readership he deserved.
<br> —
<a href="http://www.guardian.co.uk/books/2012/feb/10/collected-poems-peter-redgrove-review" rel="nofollow">The Guardian (Feb 10, 2012)</a></div>


</li>






<li class="entry learnable" id="entry121"
 lang="en" word="credible" freq="220.33" prog="0">

<a class="word dynamictext" href="/dictionary/credible">credible</a>
<div class="definition">appearing to merit belief or acceptance</div>
<div class="example">Mike Mullen, then chairman of the Joint Chiefs of Staff, has acknowledged receiving the memo but said he ignored it as not
<strong>credible</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=add6f84287cc3fc52b0bdc5be4a19280" rel="nofollow">New York Times (Dec 19, 2011)</a></div>


</li>






<li class="entry learnable" id="entry122"
 lang="en" word="provoke" freq="220.83" prog="0">

<a class="word dynamictext" href="/dictionary/provoke">provoke</a>
<div class="definition">provide the needed stimulus for</div>
<div class="example">It
<strong>provoked</strong> a bigger reaction than we could ever have anticipated.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2012/feb/10/the-conversation-big-fat-gypsy-weddings" rel="nofollow">The Guardian (Feb 10, 2012)</a></div>


</li>






<li class="entry learnable" id="entry123"
 lang="en" word="tread" freq="220.92" prog="0">

<a class="word dynamictext" href="/dictionary/tread">tread</a>
<div class="definition">a step in walking or running</div>
<div class="example">The farmer went down, his clumsy boots making no sound on the uncarpeted stairway, so careful was his
<strong>tread</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38792" rel="nofollow">Woolson, Constance Fenimore</a></div>


</li>






<li class="entry learnable" id="entry124"
 lang="en" word="ascertain" freq="228.25" prog="0">

<a class="word dynamictext" href="/dictionary/ascertain">ascertain</a>
<div class="definition">learn or discover with confidence</div>
<div class="example">Health care providers and manufacturers can
<strong>ascertain</strong> alternative treatment more effectively by tackling predicted drug shortage incidences early in the process.
<br> —
<a href="http://www.forbes.com/sites/dougschoen/2012/02/13/the-drug-shortage-crisis-in-america/" rel="nofollow">Forbes (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry125"
 lang="en" word="fare" freq="235.7" prog="0">

<a class="word dynamictext" href="/dictionary/fare">fare</a>
<div class="definition">proceed, get along, or succeed</div>
<div class="example">A recent study breaks down how graduates with various college degrees are
<strong>faring</strong> in today’s difficult job market.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=2dd2cdc73d5e3676e96f08d34215d3be" rel="nofollow">Washington Post (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry126"
 lang="en" word="cede" freq="235.76" prog="0">

<a class="word dynamictext" href="/dictionary/cede">cede</a>
<div class="definition">relinquish possession or control over</div>
<div class="example">Some militia chiefs say they will only
<strong>cede</strong> command of their fighters once an organized military and security apparatus is in place.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/topNews/~3/6gMGDlx9wbY/us-libya-idUSTRE80301120120104" rel="nofollow">Reuters (Jan 3, 2012)</a></div>


</li>






<li class="entry learnable" id="entry127"
 lang="en" word="perpetual" freq="236.04" prog="0">

<a class="word dynamictext" href="/dictionary/perpetual">perpetual</a>
<div class="definition">continuing forever or indefinitely</div>
<div class="example">The river is a
<strong>perpetual</strong> enjoyment, always something going on.
<br> —
<a href="http://www.gutenberg.org/ebooks/38825" rel="nofollow">Waddington, Mary King</a></div>


</li>






<li class="entry learnable" id="entry128"
 lang="en" word="decree" freq="237.13" prog="0">

<a class="word dynamictext" href="/dictionary/decree">decree</a>
<div class="definition">a legally binding command or decision</div>
<div class="example">While the
<strong>decree</strong> takes effect immediately, it requires Parliament’s approval within 60 days to remain in force.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/diMmVgs5oI0/monti-s-cabinet-approved-measures-to-cut-italian-red-tape.html" rel="nofollow">BusinessWeek (Jan 28, 2012)</a></div>


</li>






<li class="entry learnable" id="entry129"
 lang="en" word="contrive" freq="241.01" prog="0">

<a class="word dynamictext" href="/dictionary/contrive">contrive</a>
<div class="definition">make or work out a plan for; devise</div>
<div class="example">The wily Roc, never taken much by surprise,
<strong>contrived</strong> to escape, but old Tributor and his men were all captured.
<br> —
<a href="http://www.gutenberg.org/ebooks/38631" rel="nofollow">Thornbury, Walter</a></div>


</li>






<li class="entry learnable" id="entry130"
 lang="en" word="derived" freq="242.31" prog="0">

<a class="word dynamictext" href="/dictionary/derived">derived</a>
<div class="definition">formed or developed from something else; not original</div>
<div class="example">Modern kale, cabbage, broccoli, cauliflower, Brussels sprouts, and kohlrabi are all members of the same species,
<strong>derived</strong> from a single prehistoric plant variety.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/sOZ_Gg_uDGA/click.phdo" rel="nofollow">Slate (Feb 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry131"
 lang="en" word="elaborate" freq="246.11" prog="0">

<a class="word dynamictext" href="/dictionary/elaborate">elaborate</a>
<div class="definition">marked by complexity and richness of detail</div>
<div class="example">But the tobacco industry and owners of other convenience stores say tribal cigarette manufacturing is just an
<strong>elaborate</strong> form of tax evasion.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c11106d37f7c5554fc1314f3dbd42f40" rel="nofollow">New York Times (Feb 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry132"
 lang="en" word="substantial" freq="248.39" prog="0">

<a class="word dynamictext" href="/dictionary/substantial">substantial</a>
<div class="definition">real; having a material or factual existence</div>
<div class="example">Defence lawyers said the large number of forensic tests which had been carried out had failed to find any
<strong>substantial</strong> evidence linked to the accused.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/uk-scotland-edinburgh-east-fife-17142957" rel="nofollow">BBC (Feb 23, 2012)</a></div>


</li>






<li class="entry learnable" id="entry133"
 lang="en" word="frontier" freq="248.41" prog="0">

<a class="word dynamictext" href="/dictionary/frontier">frontier</a>
<div class="definition">a wilderness at the edge of a settled area of a country</div>
<div class="example">Adding to the precarious security situation, tribesmen kidnapped 18 Egyptian border guards along the
<strong>frontier</strong> with Israel in Sinai Peninsula.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=034ba29adc96f18bd803fc9287a13517" rel="nofollow">New York Times (Feb 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry134"
 lang="en" word="facile" freq="249.65" prog="0">

<a class="word dynamictext" href="/dictionary/facile">facile</a>
<div class="definition">arrived at without due care or effort; lacking depth</div>
<div class="example">As one teacher remarks about a troubled student, “There is no
<strong>facile</strong> solution.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=ddfc5af109cd2f71f8e19b3c2d8abcb7" rel="nofollow">New York Times (Oct 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry135"
 lang="en" word="cite" freq="253.25" prog="0">

<a class="word dynamictext" href="/dictionary/cite">cite</a>
<div class="definition">make reference to</div>
<div class="example">The Federal Reserve has pledged low interest rates until late 2014,
<strong>citing</strong> in part the weakness of the job market.
<br> —
<a href="http://www.businessweek.com/news/2012-02-21/margins-improve-at-u-s-companies-as-wages-lag-behind-economy.html" rel="nofollow">BusinessWeek (Feb 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry136"
 lang="en" word="warrant" freq="254.73" prog="0">

<a class="word dynamictext" href="/dictionary/warrant">warrant</a>
<div class="definition">show to be reasonable or provide adequate ground for</div>
<div class="example">In the United Kingdom and Europe the devices are not used unless the need is
<strong>warranted</strong> by the patient's medical condition.
<br> —
<a href="http://www.usnews.com/science/articles/2012/1/17/phsycists-fear-of-diagnostic-radiation-is-overblown?s_cid=rss:phsycists-fear-of-diagnostic-radiation-is-overblown" rel="nofollow">US News (Jan 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry137"
 lang="en" word="sob" freq="254.93" prog="0">

<a class="word dynamictext" href="/dictionary/sob">sob</a>
<div class="definition">weep convulsively</div>
<div class="example">He cried and trembled,
<strong>sobbing</strong>, while they spoke, like the child he was.
<br> —
<a href="http://www.gutenberg.org/ebooks/38872" rel="nofollow">Weyman, Stanley J.</a></div>


</li>






<li class="entry learnable" id="entry138"
 lang="en" word="rider" freq="255.96" prog="0">

<a class="word dynamictext" href="/dictionary/rider">rider</a>
<div class="definition">a traveler who actively sits and travels on an animal</div>
<div class="example">In horseback riding, a
<strong>rider</strong> will give commands by squeezing or lengthening the reins and altering the position of his legs.
<br> —
<a href="http://feedproxy.google.com/~r/time/entertainment/~3/4qK_9cF_9rI/" rel="nofollow">Time (Jan 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry139"
 lang="en" word="dense" freq="256" prog="0">

<a class="word dynamictext" href="/dictionary/dense">dense</a>
<div class="definition">permitting little if any light to pass through</div>
<div class="example"><strong>Dense</strong> black smoke rose in the distance as demonstrators burned tires in Shiite villages.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/dD8atjz3OS0/bahrain-police-arrest-demonstrators-on-protest-anniversary.html" rel="nofollow">BusinessWeek (Feb 14, 2012)</a></div>


</li>






<li class="entry learnable" id="entry140"
 lang="en" word="afflict" freq="258.03" prog="0">

<a class="word dynamictext" href="/dictionary/afflict">afflict</a>
<div class="definition">cause physical pain or suffering in</div>
<div class="example">Melanoma globally
<strong>afflicts</strong> nearly 160,000 new people each year.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/healthNews/~3/e4dPbF6mKpk/us-europe-medicines-idUSTRE7BF0VT20111216" rel="nofollow">Reuters (Dec 16, 2011)</a></div>


</li>






<li class="entry learnable" id="entry141"
 lang="en" word="flourish" freq="262.3" prog="0">

<a class="word dynamictext" href="/dictionary/flourish">flourish</a>
<div class="definition">grow vigorously</div>
<div class="example">His business had been all along steadily
<strong>flourishing</strong>, his patrons had been of high social position, some most illustrious, others actually royal.
<br> —
<a href="http://www.gutenberg.org/ebooks/36535" rel="nofollow">Petherick, Horace William</a></div>


</li>






<li class="entry learnable" id="entry142"
 lang="en" word="ordain" freq="274.11" prog="0">

<a class="word dynamictext" href="/dictionary/ordain">ordain</a>
<div class="definition">invest with ministerial or priestly authority</div>
<div class="example">One of the present bishops was consecrated when quite a young boy, and deacons are often
<strong>ordained</strong> at sixteen, and even much earlier.
<br> —
<a href="http://www.gutenberg.org/ebooks/38828" rel="nofollow">Bird, Isabella L. (Isabella Lucy)</a></div>


</li>






<li class="entry learnable" id="entry143"
 lang="en" word="pious" freq="274.72" prog="0">

<a class="word dynamictext" href="/dictionary/pious">pious</a>
<div class="definition">having or showing or expressing reverence for a deity</div>
<div class="example">Mother, you see, is a very
<strong>pious</strong> woman, and she attributes it all to Providence, saying that it was the Divine interference in her behalf.
<br> —
<a href="http://www.gutenberg.org/ebooks/34150" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry144"
 lang="en" word="vex" freq="282.28" prog="0">

<a class="word dynamictext" href="/dictionary/vex">vex</a>
<div class="definition">disturb, especially by minor irritations</div>
<div class="example">There are
<strong>vexing</strong> problems slowing the growth and the practical implementation of big data technologies.
<br> —
<a href="http://www.forbes.com/sites/danwoods/2011/10/21/big-data-technology-evaluation-checklist/" rel="nofollow">Forbes (Oct 21, 2011)</a></div>


</li>






<li class="entry learnable" id="entry145"
 lang="en" word="gravity" freq="287.13" prog="0">

<a class="word dynamictext" href="/dictionary/gravity">gravity</a>
<div class="definition">the force of attraction between all masses in the universe</div>
<div class="example">Once captured, the combined object will have a new center of
<strong>gravity</strong> and may be spinning in an uncontrolled way.
<br> —
<a href="http://news.sciencemag.org/scienceinsider/2012/02/swiss-want-to-build-a-satellite.html?rss=1" rel="nofollow">Science Magazine (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry146"
 lang="en" word="suspended" freq="287.98" prog="0">

<a class="word dynamictext" href="/dictionary/suspended">suspended</a>
<div class="definition"> supported or kept from sinking or falling by buoyancy</div>
<div class="example">Frustrating enough at ground level, but can you imagine the agony about a stranded, ever-soggier Oreo being
<strong>suspended</strong> 11 feet above the ground?
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=d67d35dfad53d9434a26967746ad241f" rel="nofollow">Washington Post (Feb 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry147"
 lang="en" word="conspicuous" freq="288.02" prog="0">

<a class="word dynamictext" href="/dictionary/conspicuous">conspicuous</a>
<div class="definition">obvious to the eye or mind</div>
<div class="example">Its bright scarlet fruits are
<strong>conspicuous</strong> in late autumn.
<br> —
<a href="http://www.gutenberg.org/ebooks/38904" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry148"
 lang="en" word="retort" freq="292.37" prog="0">

<a class="word dynamictext" href="/dictionary/retort">retort</a>
<div class="definition">a quick reply to a question or remark</div>
<div class="example">Having put him in ill humour with this
<strong>retort</strong>, she fled away rejoicing.
<br> —
<a href="http://www.gutenberg.org/ebooks/38247" rel="nofollow">Coster, Charles Th?odore Henri de</a></div>


</li>






<li class="entry learnable" id="entry149"
 lang="en" word="jet" freq="294.03" prog="0">

<a class="word dynamictext" href="/dictionary/jet">jet</a>
<div class="definition">an airplane powered by gas turbines</div>
<div class="example">Typhoon fighter
<strong>jets</strong>, helicopters, two warships and bomb disposal experts will also be on duty to guard against security threats.
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2017552274_apolylondon2012security.html?syndication=rss" rel="nofollow">Seattle Times (Feb 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry150"
 lang="en" word="bolt" freq="294.79" prog="0">

<a class="word dynamictext" href="/dictionary/bolt">bolt</a>
<div class="definition">run away</div>
<div class="example">The blare of bugles was heard, and a few seconds afterwards Jackson, still facing the enemy, shouted: "By Jupiter, they're
<strong>bolting</strong>, sir."
<br> —
<a href="http://www.gutenberg.org/ebooks/38714" rel="nofollow">Strang, Herbert</a></div>


</li>






<li class="entry learnable" id="entry151"
 lang="en" word="assent" freq="296.46" prog="0">

<a class="word dynamictext" href="/dictionary/assent">assent</a>
<div class="definition">to agree or express agreement</div>
<div class="example">His two companions readily
<strong>assented</strong>, and the promise was mutually given and received.
<br> —
<a href="http://www.gutenberg.org/ebooks/38785" rel="nofollow">Keightley, Thomas</a></div>


</li>






<li class="entry learnable" id="entry152"
 lang="en" word="purse" freq="298.18" prog="0">

<a class="word dynamictext" href="/dictionary/purse">purse</a>
<div class="definition">a sum spoken of as the contents of a money container</div>
<div class="example">She watched over her husband, kept his accounts, held the family
<strong>purse</strong>, managed all his affairs.&nbsp;
<br> —
<a href="http://www.gutenberg.org/ebooks/38662" rel="nofollow">Shorter, Clement K.</a></div>


</li>






<li class="entry learnable" id="entry153"
 lang="en" word="plus" freq="299.53" prog="0">

<a class="word dynamictext" href="/dictionary/plus">plus</a>
<div class="definition">the arithmetic operation of summing</div>
<div class="example">The survey’s margin of error was
<strong>plus</strong> or minus four percentage points.
<br> —
<a href="http://www.businessweek.com/news/2011-12-29/romney-sets-sights-on-iowa-win-after-stealth-campaign-there.html" rel="nofollow">BusinessWeek (Dec 29, 2011)</a></div>


</li>






<li class="entry learnable" id="entry154"
 lang="en" word="sanction" freq="301.53" prog="0">

<a class="word dynamictext" href="/dictionary/sanction">sanction</a>
<div class="definition">give authority or permission to</div>
<div class="example">The Securities and Exchange Commission said last year it had
<strong>sanctioned</strong> 39 senior officers for conduct related to the housing market meltdown.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/Ya198CePVFc/icelandic-anger-brings-debt-forgiveness-in-best-recovery-story.html" rel="nofollow">BusinessWeek (Feb 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry155"
 lang="en" word="proceeding" freq="303.45" prog="0">

<a class="word dynamictext" href="/dictionary/proceeding">proceeding</a>
<div class="definition">a sequence of steps by which legal judgments are invoked</div>
<div class="example">Chu attended the special court-martial
<strong>proceeding</strong> on Monday in Hawaii, Hill said.
<br> —
<a href="http://feeds.reuters.com/~r/Reuters/domesticNews/~3/VZIvBtBHhUM/us-marine-assault-idUSTRE80U07W20120131" rel="nofollow">Reuters (Jan 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry156"
 lang="en" word="exalt" freq="305.43" prog="0">

<a class="word dynamictext" href="/dictionary/exalt">exalt</a>
<div class="definition">praise, glorify, or honor</div>
<div class="example">Some
<strong>exalt</strong> themselves by anonymously posting their own laudatory reviews.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=3d3aab69f3732ea3072b650ed5458c22" rel="nofollow">New York Times (Jan 26, 2012)</a></div>


</li>






<li class="entry learnable" id="entry157"
 lang="en" word="siege" freq="305.54" prog="0">

<a class="word dynamictext" href="/dictionary/siege">siege</a>
<div class="definition">an action of an armed force that surrounds a fortified place</div>
<div class="example">Rebellion broke out, and finally the aged Caliph, after enduring a
<strong>siege</strong> of several weeks, was murdered in his own house.
<br> —
<a href="http://www.gutenberg.org/ebooks/37985" rel="nofollow">Nicholson, Reynold</a></div>


</li>






<li class="entry learnable" id="entry158"
 lang="en" word="malice" freq="307.19" prog="0">

<a class="word dynamictext" href="/dictionary/malice">malice</a>
<div class="definition">feeling a need to see others suffer</div>
<div class="example">He viewed the moths with
<strong>malice</strong>, their fluttering wings fanning his resentment.
<br> —
<a href="http://www.gutenberg.org/ebooks/38341" rel="nofollow">Lyman, Olin L.</a></div>


</li>






<li class="entry learnable" id="entry159"
 lang="en" word="extravagant" freq="307.84" prog="0">

<a class="word dynamictext" href="/dictionary/extravagant">extravagant</a>
<div class="definition">recklessly wasteful</div>
<div class="example">Advisers say new millionaires are prone to mistakes, like making
<strong>extravagant</strong> purchases or risky deals with friends.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/technologyNews/~3/IfMJfD4TOpQ/us-facebook-wealth-managers-idUSTRE8112BR20120202" rel="nofollow">Reuters (Feb 2, 2012)</a></div>


</li>






<li class="entry learnable" id="entry160"
 lang="en" word="wax" freq="312.61" prog="0">

<a class="word dynamictext" href="/dictionary/wax">wax</a>
<div class="definition">increase in phase</div>
<div class="example">Carols had existed for centuries, though their popularity
<strong>waxed</strong> and waned as different governments and religious movements periodically declared them sinful.
<br> —
<a href="http://feedproxy.google.com/~r/time/entertainment/~3/WZog4Nhcpl4/" rel="nofollow">Time (Dec 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry161"
 lang="en" word="throng" freq="312.73" prog="0">

<a class="word dynamictext" href="/dictionary/throng">throng</a>
<div class="definition">press tightly together or cram</div>
<div class="example">Deafening cheers rent the air as he landed; hundreds
<strong>thronged</strong> around him to clasp his hand.
<br> —
<a href="http://www.gutenberg.org/ebooks/38795" rel="nofollow">Strang, Herbert</a></div>


</li>






<li class="entry learnable" id="entry162"
 lang="en" word="venerate" freq="313.53" prog="0">

<a class="word dynamictext" href="/dictionary/venerate">venerate</a>
<div class="definition">regard with feelings of respect and reverence</div>
<div class="example">He
<strong>venerated</strong> me like a being descended from an upper world.
<br> —
<a href="http://www.gutenberg.org/ebooks/38458" rel="nofollow">Blasco Ib??ez, Vicente</a></div>


</li>






<li class="entry learnable" id="entry163"
 lang="en" word="assail" freq="317.8" prog="0">

<a class="word dynamictext" href="/dictionary/assail">assail</a>
<div class="definition">attack someone physically or emotionally</div>
<div class="example">His campaign even issued a press release
<strong>assailing</strong> other rivals for, in Mr. Paul’s view, taking Mr. Romney’s quote about firing people out of context.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=0df55f2d4f2677749ae97faf20bf413e" rel="nofollow">New York Times (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry164"
 lang="en" word="sublime" freq="320.67" prog="0">

<a class="word dynamictext" href="/dictionary/sublime">sublime</a>
<div class="definition">of high moral or intellectual value</div>
<div class="example">He was uneven, disproportioned, saying ordinary things on great occasions, and now and then, without the slightest provocation, uttering the
<strong>sublimest</strong> and most beautiful thoughts.
<br> —
<a href="http://www.gutenberg.org/ebooks/38808" rel="nofollow">Ingersoll, Robert Green</a></div>


</li>






<li class="entry learnable" id="entry165"
 lang="en" word="exploit" freq="324" prog="0">

<a class="word dynamictext" href="/dictionary/exploit">exploit</a>
<div class="definition">draw from; make good use of</div>
<div class="example">As humans increasingly
<strong>exploit</strong> the deep seas for fish, oil and mining, understanding how species are dispersed is crucial, Copley said.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=0524d0e933bf913a2d54694ef06a8abe" rel="nofollow">Scientific American (Jan 3, 2012)</a></div>


</li>






<li class="entry learnable" id="entry166"
 lang="en" word="exertion" freq="326.34" prog="0">

<a class="word dynamictext" href="/dictionary/exertion">exertion</a>
<div class="definition">use of physical or mental energy; hard work</div>
<div class="example">One day overcome by
<strong>exertion</strong>, she fainted in the street.
<br> —
<a href="http://www.gutenberg.org/ebooks/38806" rel="nofollow">Ingersoll, Robert Green</a></div>


</li>






<li class="entry learnable" id="entry167"
 lang="en" word="kindle" freq="327.69" prog="0">

<a class="word dynamictext" href="/dictionary/kindle">kindle</a>
<div class="definition">catch fire</div>
<div class="example">Then a match was
<strong>kindled</strong> and fire applied.
<br> —
<a href="http://www.gutenberg.org/ebooks/38922" rel="nofollow">Warner, Susan</a></div>


</li>






<li class="entry learnable" id="entry168"
 lang="en" word="endow" freq="328.41" prog="0">

<a class="word dynamictext" href="/dictionary/endow">endow</a>
<div class="definition">furnish with a capital fund</div>
<div class="example">The grammar school here, founded in 1533, is liberally
<strong>endowed</strong>, with scholarships and exhibitions.
<br> —
<a href="http://www.gutenberg.org/ebooks/38709" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry169"
 lang="en" word="imposed" freq="331.57" prog="0">

<a class="word dynamictext" href="/dictionary/imposed">imposed</a>
<div class="definition">set forth authoritatively as obligatory</div>
<div class="example">The Arab League has already suspended Syria and
<strong>imposed</strong> economic sanctions.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/tJbW_8lpHBE/u-s-french-journalists-killed-in-besieged-syrian-city.html" rel="nofollow">BusinessWeek (Feb 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry170"
 lang="en" word="humiliate" freq="332.2" prog="0">

<a class="word dynamictext" href="/dictionary/humiliate">humiliate</a>
<div class="definition">cause to feel shame</div>
<div class="example">The letter claims pensioners are too often patronised,
<strong>humiliated</strong>, denied privacy or even medical treatment.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/uk-17124054" rel="nofollow">BBC (Feb 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry171"
 lang="en" word="suffrage" freq="333.42" prog="0">

<a class="word dynamictext" href="/dictionary/suffrage">suffrage</a>
<div class="definition">a legal right to vote</div>
<div class="example">There has been a great deal said in this country of late in regard to giving the right of
<strong>suffrage</strong> to women.
<br> —
<a href="http://www.gutenberg.org/ebooks/38809" rel="nofollow">Ingersoll, Robert Green</a></div>


</li>






<li class="entry learnable" id="entry172"
 lang="en" word="ensue" freq="334.6" prog="0">

<a class="word dynamictext" href="/dictionary/ensue">ensue</a>
<div class="definition">issue or terminate in a specified way</div>
<div class="example">An uproar
<strong>ensued</strong> months after the approval, when opponents realized the online gambling measure had been slipped in.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=240f8d32e2d5c0a8c96fa0d44811028b" rel="nofollow">New York Times (Feb 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry173"
 lang="en" word="brook" freq="336.09" prog="0">

<a class="word dynamictext" href="/dictionary/brook">brook</a>
<div class="definition">a natural stream of water smaller than a river</div>
<div class="example">He walked across the little bridge over the
<strong>brook</strong> and at once his mood changed.
<br> —
<a href="http://www.gutenberg.org/ebooks/38664" rel="nofollow">Mason, A. E. W. (Alfred Edward Woodley)</a></div>


</li>






<li class="entry learnable" id="entry174"
 lang="en" word="gale" freq="336.54" prog="0">

<a class="word dynamictext" href="/dictionary/gale">gale</a>
<div class="definition">a strong wind moving 45-90 knots</div>
<div class="example">The
<strong>gale</strong> was accompanied, as usual, by incessant rain and thick weather, and a heavy confused sea kept our decks always flooded.
<br> —
<a href="http://www.gutenberg.org/ebooks/38961" rel="nofollow">Fitzroy, Robert</a></div>


</li>






<li class="entry learnable" id="entry175"
 lang="en" word="muse" freq="347.29" prog="0">

<a class="word dynamictext" href="/dictionary/muse">muse</a>
<div class="definition">reflect deeply on a subject</div>
<div class="example"><strong>Musing</strong> about the Big Picture may be a lot more gratifying than focusing on the details of the specific policies that aren’t working.
<br> —
<a href="http://feedproxy.google.com/~r/time/business/~3/u9u_M8Lomi0/" rel="nofollow">Time (Jan 24, 2012)</a></div>


</li>






<li class="entry learnable" id="entry176"
 lang="en" word="satire" freq="349.69" prog="0">

<a class="word dynamictext" href="/dictionary/satire">satire</a>
<div class="definition">witty language used to convey insults or scorn</div>
<div class="example">There’s plenty of humor on Russian television, though not much political
<strong>satire</strong>; Mr. Putin put a stop to that long ago.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=8d20540f766ca9a57ab3e6ea86f87b31" rel="nofollow">New York Times (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry177"
 lang="en" word="intrigue" freq="353.08" prog="0">

<a class="word dynamictext" href="/dictionary/intrigue">intrigue</a>
<div class="definition">cause to be interested or curious</div>
<div class="example">Designing and building models that
<strong>intrigue</strong> and educate without overwhelming has been challenging.
<br> —
<a href="http://www.sciencemag.org/content/334/6059/1077.full?rss=1" rel="nofollow">Science Magazine (Nov 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry178"
 lang="en" word="indication" freq="354.99" prog="0">

<a class="word dynamictext" href="/dictionary/indication">indication</a>
<div class="definition">something that serves to suggest</div>
<div class="example">Authorities said an autopsy found no
<strong>indications</strong> of foul play or obvious signs of trauma on Houston.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2017512583_apuswhitneyhoustoninvestigation.html?syndication=rss" rel="nofollow">Seattle Times (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry179"
 lang="en" word="dispatch" freq="365.61" prog="0">

<a class="word dynamictext" href="/dictionary/dispatch">dispatch</a>
<div class="definition">send away towards a designated goal</div>
<div class="example">More than one assassin was
<strong>dispatched</strong> by the Turkish authorities to murder Napoleon.
<br> —
<a href="http://www.gutenberg.org/ebooks/38952" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry180"
 lang="en" word="cower" freq="367.76" prog="0">

<a class="word dynamictext" href="/dictionary/cower">cower</a>
<div class="definition">crouch or curl up</div>
<div class="example">The knaves lowered their weapons and shrank back
<strong>cowering</strong> before him.
<br> —
<a href="http://www.gutenberg.org/ebooks/38985" rel="nofollow">Weyman, Stanley J.</a></div>


</li>






<li class="entry learnable" id="entry181"
 lang="en" word="wont" freq="370.15" prog="0">

<a class="word dynamictext" href="/dictionary/wont">wont</a>
<div class="definition">an established custom</div>
<div class="example">He made his customary slick feeds to open teammates, but as is their
<strong>wont</strong>, the Nets struggled at times to convert points on his passes.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/0vePbjqtF7o/deron-williams-of-nets-turns-tables-on-jeremy-lin-and-the-knicks.html" rel="nofollow">New York Times (Feb 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry182"
 lang="en" word="tract" freq="374.88" prog="0">

<a class="word dynamictext" href="/dictionary/tract">tract</a>
<div class="definition">a system of body parts that serve some particular purpose</div>
<div class="example">When probiotics flourish in the digestive
<strong>tract</strong>, nutrients are better absorbed and bad bugs are held at bay, research suggests.
<br> —
<a href="http://seattletimes.nwsource.com/html/health/2017202291_nutrition13.html?syndication=rss" rel="nofollow">Seattle Times (Jan 10, 2012)</a></div>


</li>






<li class="entry learnable" id="entry183"
 lang="en" word="canon" freq="377.86" prog="0">

<a class="word dynamictext" href="/dictionary/canon">canon</a>
<div class="definition">a collection of books accepted as holy scripture</div>
<div class="example">For me, all novels of any consequence are literary, and they take their place, high and low, in the
<strong>canon</strong> of English literature.
<br> —
<a href="http://www.guardian.co.uk/books/booksblog/2011/jan/10/creative-writing-courses-too-literary" rel="nofollow">The Guardian (Jan 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry184"
 lang="en" word="impel" freq="378.99" prog="0">

<a class="word dynamictext" href="/dictionary/impel">impel</a>
<div class="definition">cause to move forward with force</div>
<div class="example">Some power beyond his comprehension was
<strong>impelling</strong> him toward the neighboring city.
<br> —
<a href="http://www.gutenberg.org/ebooks/38458" rel="nofollow">Blasco Ib??ez, Vicente</a></div>


</li>






<li class="entry learnable" id="entry185"
 lang="en" word="latitude" freq="382.4" prog="0">

<a class="word dynamictext" href="/dictionary/latitude">latitude</a>
<div class="definition">freedom from normal restraints in conduct</div>
<div class="example">Great employees often get more
<strong>latitude</strong> to bring up controversial subjects in a group setting because their performance allows greater freedom.
<br> —
<a href="http://feedproxy.google.com/~r/inc/headlines/~3/1kgE3QFFJkA/the-8-qualities-of-remarkable-employees.html" rel="nofollow">Inc (Feb 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry186"
 lang="en" word="vacate" freq="393.56" prog="0">

<a class="word dynamictext" href="/dictionary/vacate">vacate</a>
<div class="definition">leave behind empty; move out of</div>
<div class="example">Their number diminished sharply after Villaraigosa announced last week that he wanted protesters to
<strong>vacate</strong> the grounds by Monday or be forcibly removed.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/arts/~3/7VGCbCfVSn4/sns-rt-us-usa-proteststre7at0fo-20111129,0,1775292.story" rel="nofollow">Chicago Tribune (Nov 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry187"
 lang="en" word="undertaking" freq="397.24" prog="0">

<a class="word dynamictext" href="/dictionary/undertaking">undertaking</a>
<div class="definition">any piece of work that is attempted</div>
<div class="example">"Let my epitaph be, Here lies Joseph, who was unsuccessful in all his
<strong>undertakings</strong>."
<br> —
<a href="http://www.gutenberg.org/ebooks/38940" rel="nofollow">Marvin, Frederic Rowland</a></div>


</li>






<li class="entry learnable" id="entry188"
 lang="en" word="slay" freq="399.25" prog="0">

<a class="word dynamictext" href="/dictionary/slay">slay</a>
<div class="definition">kill intentionally and with premeditation</div>
<div class="example">"It were shame," said Lancelot, "for an armed to
<strong>slay</strong> an unarmed man."
<br> —
<a href="http://www.gutenberg.org/ebooks/36462" rel="nofollow">Unknown</a></div>


</li>






<li class="entry learnable" id="entry189"
 lang="en" word="predecessor" freq="401.89" prog="0">

<a class="word dynamictext" href="/dictionary/predecessor">predecessor</a>
<div class="definition">one who precedes you in time</div>
<div class="example">Heller fills in the blanks about Taft, overshadowed by colorful
<strong>predecessor</strong> Teddy Roosevelt.
<br> —
<a href="http://seattletimes.nwsource.com/html/books/2017571934_br26taft.html?syndication=rss" rel="nofollow">Seattle Times (Feb 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry190"
 lang="en" word="delicacy" freq="406.92" prog="0">

<a class="word dynamictext" href="/dictionary/delicacy">delicacy</a>
<div class="definition">the quality of being exquisitely fine in appearance</div>
<div class="example">This refinement appears in his works, which are full of artistic grace and dainty
<strong>delicacy</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38941" rel="nofollow">Drake, Samuel Adams</a></div>


</li>






<li class="entry learnable" id="entry191"
 lang="en" word="forsake" freq="407.05" prog="0">

<a class="word dynamictext" href="/dictionary/forsake">forsake</a>
<div class="definition">leave someone who needs or counts on you; leave in the lurch</div>
<div class="example">"I'm surprised," said Philip, cautiously opening fire, "that you were ever allowed to
<strong>forsake</strong> your native land."
<br> —
<a href="http://www.gutenberg.org/ebooks/38368" rel="nofollow">Hay, Ian</a></div>


</li>






<li class="entry learnable" id="entry192"
 lang="en" word="beseech" freq="420.18" prog="0">

<a class="word dynamictext" href="/dictionary/beseech">beseech</a>
<div class="definition">ask for or request earnestly</div>
<div class="example">Utterly distraught, he ran up and down the bank, hunting for his clothes, calling, crying out, imploring,
<strong>beseeching</strong> help from somewhere.
<br> —
<a href="http://www.gutenberg.org/ebooks/37419" rel="nofollow">Frank, Ulrich</a></div>


</li>






<li class="entry learnable" id="entry193"
 lang="en" word="philosophical" freq="422.14" prog="0">

<a class="word dynamictext" href="/dictionary/philosophical">philosophical</a>
<div class="definition">relating to the investigation of existence and knowledge</div>
<div class="example">His arguments, like Einstein’s, were qualitative, verging on highly
<strong>philosophical</strong>.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=c46267b88e0f2850e974deab218bab26" rel="nofollow">Scientific American (Jan 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry194"
 lang="en" word="grove" freq="422.91" prog="0">

<a class="word dynamictext" href="/dictionary/grove">grove</a>
<div class="definition">a small growth of trees without underbrush</div>
<div class="example">Soon after we came to Pasadena, father bought an orange
<strong>grove</strong> of twenty-five acres.
<br> —
<a href="http://www.gutenberg.org/ebooks/38762" rel="nofollow">Chamberlain, James Franklin</a></div>


</li>






<li class="entry learnable" id="entry195"
 lang="en" word="frustrate" freq="423.18" prog="0">

<a class="word dynamictext" href="/dictionary/frustrate">frustrate</a>
<div class="definition">hinder or prevent, as an effort, plan, or desire</div>
<div class="example"><strong>Frustrated</strong> after two years of missed budget targets, finance chiefs demanded Greek officials put their verbal commitments into law.
<br> —
<a href="http://www.businessweek.com/news/2012-02-13/europe-welcomes-greek-austerity-vote-as-bailout-edges-nearer.html" rel="nofollow">BusinessWeek (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry196"
 lang="en" word="illustrious" freq="427.71" prog="0">

<a class="word dynamictext" href="/dictionary/illustrious">illustrious</a>
<div class="definition">widely known and esteemed</div>
<div class="example">She will be joining an
<strong>illustrious</strong> list of recipients that include Winston Churchill, Nelson Mandela, Pope John Paul II and Princess Diana.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/uk-wales-south-east-wales-17151415" rel="nofollow">BBC (Feb 24, 2012)</a></div>


</li>






<li class="entry learnable" id="entry197"
 lang="en" word="device" freq="193.37" prog="0">

<a class="word dynamictext" href="/dictionary/device">device</a>
<div class="definition">an instrumentality invented for a particular purpose</div>
<div class="example">You’ve probably also noticed that the telephone and computer are no longer the only
<strong>devices</strong> on your employees’ desks.
<br> —
<a href="http://www.forbes.com/sites/ciocentral/2012/02/26/5-ways-gen-y-is-changing-your-business-like-it-or-not/" rel="nofollow">Forbes (Feb 26, 2012)</a></div>


</li>






<li class="entry learnable" id="entry198"
 lang="en" word="pomp" freq="430.54" prog="0">

<a class="word dynamictext" href="/dictionary/pomp">pomp</a>
<div class="definition">cheap or pretentious or vain display</div>
<div class="example">Throughout U.S. history, Americans have been fascinated by royal
<strong>pomp</strong> -- even on a movie screen.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/entertainment/~3/ISVYhESBZ5Q/us-oscars-brits-idUSTRE71K50P20110221" rel="nofollow">Reuters (Feb 21, 2011)</a></div>


</li>






<li class="entry learnable" id="entry199"
 lang="en" word="entreat" freq="433.99" prog="0">

<a class="word dynamictext" href="/dictionary/entreat">entreat</a>
<div class="definition">ask for or request earnestly</div>
<div class="example">"Let me go now, please," she
<strong>entreated</strong>, her eyes unable to meet his any longer.
<br> —
<a href="http://www.gutenberg.org/ebooks/38796" rel="nofollow">Hope, Anthony</a></div>


</li>






<li class="entry learnable" id="entry200"
 lang="en" word="impart" freq="435.82" prog="0">

<a class="word dynamictext" href="/dictionary/impart">impart</a>
<div class="definition">transmit, as knowledge or a skill</div>
<div class="example">Long before writing and books were in common use, proverbs were the principal means of
<strong>imparting</strong> instruction.
<br> —
<a href="http://www.gutenberg.org/ebooks/39281" rel="nofollow">Preston, Thomas</a></div>


</li>






<li class="entry learnable" id="entry201"
 lang="en" word="propriety" freq="440.15" prog="0">

<a class="word dynamictext" href="/dictionary/propriety">propriety</a>
<div class="definition">correct behavior</div>
<div class="example">I felt a trifle doubtful about the
<strong>propriety</strong> of taking a short cut across private grounds, and said as much.
<br> —
<a href="http://www.gutenberg.org/ebooks/38477" rel="nofollow">Sutphen, Van Tassel</a></div>


</li>






<li class="entry learnable" id="entry202"
 lang="en" word="consecrate" freq="449.36" prog="0">

<a class="word dynamictext" href="/dictionary/consecrate">consecrate</a>
<div class="definition">render holy by means of religious rites</div>
<div class="example">The building was
<strong>consecrated</strong> as a Protestant Episcopal church in May, 1814.
<br> —
<a href="http://www.gutenberg.org/ebooks/39068" rel="nofollow">Faris, John T. (John Thomson)</a></div>


</li>






<li class="entry learnable" id="entry203"
 lang="en" word="proceeds" freq="450.16" prog="0">

<a class="word dynamictext" href="/dictionary/proceeds">proceeds</a>
<div class="definition">the income or profit arising from a transaction</div>
<div class="example">His own share in the
<strong>proceeds</strong> was about a hundred thousand dollars.
<br> —
<a href="http://www.gutenberg.org/ebooks/39316" rel="nofollow">Stark, James H.</a></div>


</li>






<li class="entry learnable" id="entry204"
 lang="en" word="fathom" freq="450.92" prog="0">

<a class="word dynamictext" href="/dictionary/fathom">fathom</a>
<div class="definition">come to understand</div>
<div class="example">But after flying for so many years, the idea of hanging up his sparkling wings is hard for him to
<strong>fathom</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=529edbc6fd8ba453f02a48abb70b0250" rel="nofollow">New York Times (Mar 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry205"
 lang="en" word="objective" freq="454.25" prog="0">

<a class="word dynamictext" href="/dictionary/objective">objective</a>
<div class="definition">the goal intended to be attained</div>
<div class="example">The
<strong>objective</strong> was to mobilize students from 18 high schools across the city to provide community services and inspire others.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2a3f753beba955beb1e18956a4e69369" rel="nofollow">New York Times (Feb 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry206"
 lang="en" word="clad" freq="458.72" prog="0">

<a class="word dynamictext" href="/dictionary/clad">clad</a>
<div class="definition">wearing or provided with clothing</div>
<div class="example">A few of the villagers came behind,
<strong>clad</strong> in mourning robes, and bearing lighted tapers.
<br> —
<a href="http://www.gutenberg.org/ebooks/39278" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry207"
 lang="en" word="partisan" freq="460.32" prog="0">

<a class="word dynamictext" href="/dictionary/partisan">partisan</a>
<div class="definition">devoted to a cause or party</div>
<div class="example">But given the bitter
<strong>partisan</strong> divide in an election year, Democrats said they would never be able to get such legislation passed.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/business/~3/aGeMByvaozI/la-fi-demarco-mortgages-20120330,0,6780200.story" rel="nofollow">Chicago Tribune (Mar 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry208"
 lang="en" word="faction" freq="474.32" prog="0">

<a class="word dynamictext" href="/dictionary/faction">faction</a>
<div class="definition">a dissenting clique</div>
<div class="example">One
<strong>faction</strong> declared it would begin an armed struggle against the government of the United States.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/YPar8OJuZkQ/click.phdo" rel="nofollow">Slate (Feb 29, 2012)</a></div>


</li>






<li class="entry learnable" id="entry209"
 lang="en" word="contrived" freq="476.76" prog="0">

<a class="word dynamictext" href="/dictionary/contrived">contrived</a>
<div class="definition">artificially formal</div>
<div class="example">In lesser hands the story about a young man who discovers life among the dead could be impossibly cute and
<strong>contrived</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2774f7addfd4ee77ebe5aa6f06ba8e1a" rel="nofollow">New York Times (Mar 25, 2012)</a></div>


</li>






<li class="entry learnable" id="entry210"
 lang="en" word="venerable" freq="480.14" prog="0">

<a class="word dynamictext" href="/dictionary/venerable">venerable</a>
<div class="definition">impressive by reason of age</div>
<div class="example">Thus, after much more than two hundred years, the
<strong>venerable</strong> building looks almost as it did when the first students entered its doors.
<br> —
<a href="http://www.gutenberg.org/ebooks/39068" rel="nofollow">Faris, John T. (John Thomson)</a></div>


</li>






<li class="entry learnable" id="entry211"
 lang="en" word="restrained" freq="505.54" prog="0">

<a class="word dynamictext" href="/dictionary/restrained">restrained</a>
<div class="definition">not showy or obtrusive</div>
<div class="example">By contrast, Mr. Pei’s
<strong>restrained</strong> design took time to claim my attention, particularly since it sat quietly next door to Saarinen’s concrete gull wings.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=ed0792d0aed45843d55bcce9d2b9aa95" rel="nofollow">New York Times (Oct 6, 2011)</a></div>


</li>






<li class="entry learnable" id="entry212"
 lang="en" word="besiege" freq="507.72" prog="0">

<a class="word dynamictext" href="/dictionary/besiege">besiege</a>
<div class="definition">harass, as with questions or requests</div>
<div class="example">He can’t trot down the street without being
<strong>besieged</strong> by paparazzi.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=8ce6aeebafe3592eae1cc7742f437ea0" rel="nofollow">New York Times (Mar 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry213"
 lang="en" word="manifestation" freq="513.01" prog="0">

<a class="word dynamictext" href="/dictionary/manifestation">manifestation</a>
<div class="definition">a clear appearance</div>
<div class="example">Singing and dancing are
<strong>manifestations</strong> of what many Syrians describe as a much broader cultural flowering.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=a46861aa66f993ffc63db87f4b00d701" rel="nofollow">New York Times (Dec 19, 2011)</a></div>


</li>






<li class="entry learnable" id="entry214"
 lang="en" word="rebuke" freq="516.9" prog="0">

<a class="word dynamictext" href="/dictionary/rebuke">rebuke</a>
<div class="definition">an act or expression of criticism and censure</div>
<div class="example">Afterward, the leaders fought court orders to release records showing what they had done, drawing an uncommonly sharp
<strong>rebuke</strong> from a federal judge.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=ef36f49deb06152a49e657ef22b5c024" rel="nofollow">Washington Post (Mar 14, 2012)</a></div>


</li>






<li class="entry learnable" id="entry215"
 lang="en" word="insurgent" freq="518.66" prog="0">

<a class="word dynamictext" href="/dictionary/insurgent">insurgent</a>
<div class="definition">in opposition to a civil authority or government</div>
<div class="example">The Free Syrian Army, an
<strong>insurgent</strong> group made of defecting soldiers and based in southern Turkey, claimed responsibility for both attacks.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=a53a815e8be188ec034a67eb33ff59ed" rel="nofollow">New York Times (Nov 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry216"
 lang="en" word="rhetoric" freq="520.85" prog="0">

<a class="word dynamictext" href="/dictionary/rhetoric">rhetoric</a>
<div class="definition">using language effectively to please or persuade</div>
<div class="example">His fiery
<strong>rhetoric</strong> in support of limiting cuts to projected defense spending has surprised and impressed some of Obama's toughest Republican critics.
<br> —
<a href="http://feeds.reuters.com/~r/Reuters/PoliticsNews/~3/JYoM7pTVZuo/us-usa-military-idUSTRE8042A720120105" rel="nofollow">Reuters (Jan 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry217"
 lang="en" word="scrupulous" freq="524.07" prog="0">

<a class="word dynamictext" href="/dictionary/scrupulous">scrupulous</a>
<div class="definition">having ethical or moral principles</div>
<div class="example">The reason is that the vast majority of businesses are
<strong>scrupulous</strong> and treat their employees well.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2010/jun/04/vince-cable-tory-songbook" rel="nofollow">The Guardian (Jun 4, 2010)</a></div>


</li>






<li class="entry learnable" id="entry218"
 lang="en" word="ratify" freq="524.07" prog="0">

<a class="word dynamictext" href="/dictionary/ratify">ratify</a>
<div class="definition">approve and express assent, responsibility, or obligation</div>
<div class="example">Company officials at Safeway said those replacement workers will remain on standby until the agreement is
<strong>ratified</strong> by union members.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=93001a89bdfc7adbf733c24a57682367" rel="nofollow">Washington Post (Mar 29, 2012)</a></div>


</li>






<li class="entry learnable" id="entry219"
 lang="en" word="stump" freq="526.12" prog="0">

<a class="word dynamictext" href="/dictionary/stump">stump</a>
<div class="definition">cause to be perplexed or confounded</div>
<div class="example">Though family members long suspected Evans, a local handyman who frequently hired local youths, the case
<strong>stumped</strong> investigators for years.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=9d2fd1ba467c32de3ef2970d2f0ade61" rel="nofollow">Washington Post (Aug 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry220"
 lang="en" word="discreet" freq="530.94" prog="0">

<a class="word dynamictext" href="/dictionary/discreet">discreet</a>
<div class="definition">marked by prudence or modesty and wise self-restraint</div>
<div class="example">Sarkozy has attempted to tone down his image, becoming more
<strong>discreet</strong> about his private life.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/XggwWt9SaQE/sarkozy-most-unpopular-as-election-nears-sees-historic-rebound.html" rel="nofollow">BusinessWeek (Feb 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry221"
 lang="en" word="imposing" freq="532.99" prog="0">

<a class="word dynamictext" href="/dictionary/imposing">imposing</a>
<div class="definition">impressive in appearance</div>
<div class="example">These buildings were grand and stylized with intricate details and a bit of an
<strong>imposing</strong> presence.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=27b33c52b282d16ca03d1877e7467e11" rel="nofollow">Scientific American (Mar 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry222"
 lang="en" word="wistful" freq="533.09" prog="0">

<a class="word dynamictext" href="/dictionary/wistful">wistful</a>
<div class="definition">showing pensive sadness</div>
<div class="example">She turned toward him, her face troubled, her eyes most
<strong>wistful</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38689" rel="nofollow">Mason, A. E. W. (Alfred Edward Woodley)</a></div>


</li>






<li class="entry learnable" id="entry223"
 lang="en" word="mortify" freq="534.96" prog="0">

<a class="word dynamictext" href="/dictionary/mortify">mortify</a>
<div class="definition">cause to feel shame</div>
<div class="example">Intensely
<strong>mortified</strong> at this humiliation, the king fell sick, and henceforth his health failed rapidly.
<br> —
<a href="http://www.gutenberg.org/ebooks/34992" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry224"
 lang="en" word="ripple" freq="544.04" prog="0">

<a class="word dynamictext" href="/dictionary/ripple">ripple</a>
<div class="definition">stir up so as to form small waves</div>
<div class="example">That could precipitate higher interest rates that would
<strong>ripple</strong> across the economy.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=9fae23395d167983fc75af810164d170" rel="nofollow">Washington Post (Jul 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry225"
 lang="en" word="premise" freq="548.95" prog="0">

<a class="word dynamictext" href="/dictionary/premise">premise</a>
<div class="definition">a statement that is held to be true</div>
<div class="example">Success, real success, comes to the jack of all trades, a major
<strong>premise</strong> handed down from pioneer days.
<br> —
<a href="http://www.gutenberg.org/ebooks/38819" rel="nofollow">Gilbert, Clinton W. (Clinton Wallace)</a></div>


</li>






<li class="entry learnable" id="entry226"
 lang="en" word="subside" freq="551.97" prog="0">

<a class="word dynamictext" href="/dictionary/subside">subside</a>
<div class="definition">wear off or die down</div>
<div class="example">Affliction is allayed, grief
<strong>subsides</strong>, sorrow is soothed, distress is mitigated.
<br> —
<a href="http://www.gutenberg.org/ebooks/247" rel="nofollow">Webster, Noah</a></div>


</li>






<li class="entry learnable" id="entry227"
 lang="en" word="adverse" freq="552.27" prog="0">

<a class="word dynamictext" href="/dictionary/adverse">adverse</a>
<div class="definition">contrary to your interests or welfare</div>
<div class="example">High doses can have
<strong>adverse</strong> effects and even cause death.
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2017845768_apushorseracingudall.html?syndication=rss" rel="nofollow">Seattle Times (Mar 26, 2012)</a></div>


</li>






<li class="entry learnable" id="entry228"
 lang="en" word="caprice" freq="552.3" prog="0">

<a class="word dynamictext" href="/dictionary/caprice">caprice</a>
<div class="definition">a sudden desire</div>
<div class="example">Nobody is really in charge, and decisions are made on whim and
<strong>caprice</strong>.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4db6fcfad9ebad7957674da453cce315" rel="nofollow">New York Times (Apr 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry229"
 lang="en" word="muster" freq="565.38" prog="0">

<a class="word dynamictext" href="/dictionary/muster">muster</a>
<div class="definition">gather or bring together</div>
<div class="example">Yet Fox needed all the strength that he could
<strong>muster</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38452" rel="nofollow">Rosebery, Archibald Phillip Primrose</a></div>


</li>






<li class="entry learnable" id="entry230"
 lang="en" word="comprehensive" freq="568.85" prog="0">

<a class="word dynamictext" href="/dictionary/comprehensive">comprehensive</a>
<div class="definition">broad in scope</div>
<div class="example">The United States Army developed a
<strong>comprehensive</strong> plan to address problematic race relations in the 1970s, recognizing that they were hampering military effectiveness.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4ae73fc5dfb5e1f6484956818a5b3d81" rel="nofollow">New York Times (Feb 6, 2012)</a></div>


</li>






<li class="entry learnable" id="entry231"
 lang="en" word="accede" freq="569.07" prog="0">

<a class="word dynamictext" href="/dictionary/accede">accede</a>
<div class="definition">yield to another's wish or opinion</div>
<div class="example">Therefore he made up his mind to
<strong>accede</strong> to his uncle's desire.
<br> —
<a href="http://www.gutenberg.org/ebooks/34995" rel="nofollow">Streckfuss, Adolph</a></div>


</li>






<li class="entry learnable" id="entry232"
 lang="en" word="fervent" freq="570.58" prog="0">

<a class="word dynamictext" href="/dictionary/fervent">fervent</a>
<div class="definition">characterized by intense emotion</div>
<div class="example">But, to
<strong>fervent</strong> applause and scattered fist pumps from two sets of worshipers, he pledged to legally challenge the claims against him.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=09fef16a4a6734daa8955a6f5af0ca89" rel="nofollow">New York Times (Sep 26, 2010)</a></div>


</li>






<li class="entry learnable" id="entry233"
 lang="en" word="cohere" freq="571.9" prog="0">

<a class="word dynamictext" href="/dictionary/cohere">cohere</a>
<div class="definition">cause to form a united, orderly, and consistent whole</div>
<div class="example">Two antagonistic values may
<strong>cohere</strong> in the same object.
<br> —
<a href="http://www.gutenberg.org/ebooks/38047" rel="nofollow">Anderson, Benjamin M. (Benjamin McAlester)</a></div>


</li>






<li class="entry learnable" id="entry234"
 lang="en" word="tribunal" freq="580.78" prog="0">

<a class="word dynamictext" href="/dictionary/tribunal">tribunal</a>
<div class="definition">an assembly to conduct judicial business</div>
<div class="example">The military has historically been protected from civilian courts, with any crimes committed by soldiers being decided in closed military
<strong>tribunals</strong>.
<br> —
<a href="http://online.wsj.com/article/SB10001424052970204062704577223622375042352.html?mod=fox_australian" rel="nofollow">Wall Street Journal (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry235"
 lang="en" word="austere" freq="583.49" prog="0">

<a class="word dynamictext" href="/dictionary/austere">austere</a>
<div class="definition">severely simple</div>
<div class="example">A certain
<strong>austere</strong> simplicity was noticeable all over Longfellow's house.
<br> —
<a href="http://www.gutenberg.org/ebooks/37980" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry236"
 lang="en" word="recovering" freq="584.32" prog="0">

<a class="word dynamictext" href="/dictionary/recovering">recovering</a>
<div class="definition">returning to health after illness or debility</div>
<div class="example">“The
<strong>recovering</strong> economy is bringing more people back into the market.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=e9f1f5417f3c3265d47defff8b62f326" rel="nofollow">Washington Post (Mar 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry237"
 lang="en" word="stratum" freq="589.52" prog="0">

<a class="word dynamictext" href="/dictionary/stratum">stratum</a>
<div class="definition">people having the same social or economic status</div>
<div class="example">She belonged to the upper
<strong>stratum</strong> of the profession, and, knowing it, could not sink.
<br> —
<a href="http://www.gutenberg.org/ebooks/33538" rel="nofollow">George, Walter Lionel</a></div>


</li>






<li class="entry learnable" id="entry238"
 lang="en" word="conscientious" freq="596.49" prog="0">

<a class="word dynamictext" href="/dictionary/conscientious">conscientious</a>
<div class="definition">characterized by extreme care and great effort</div>
<div class="example">A
<strong>conscientious</strong> hostess would be very much mortified if she served chicken out of its proper course.
<br> —
<a href="http://www.gutenberg.org/ebooks/37680" rel="nofollow">Reed, Myrtle</a></div>


</li>






<li class="entry learnable" id="entry239"
 lang="en" word="arbitrary" freq="598.81" prog="0">

<a class="word dynamictext" href="/dictionary/arbitrary">arbitrary</a>
<div class="definition">based on or subject to individual discretion or preference</div>
<div class="example">Sandra Nurse, a member of Occupy's direct action working group, said police treated demonstrators roughly and made
<strong>arbitrary</strong> arrests.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/Zrwastc2XfY/0,8599,2109359,00.html" rel="nofollow">Time (Mar 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry240"
 lang="en" word="exasperate" freq="602.61" prog="0">

<a class="word dynamictext" href="/dictionary/exasperate">exasperate</a>
<div class="definition">irritate</div>
<div class="example">Shopkeepers,
<strong>exasperated</strong> at the impact of higher taxes and reduced consumer spending, are planning to close down for the day.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6381b2f0a6ef4db11bbcebe00f02407d" rel="nofollow">New York Times (Feb 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry241"
 lang="en" word="conjure" freq="604.12" prog="0">

<a class="word dynamictext" href="/dictionary/conjure">conjure</a>
<div class="definition">summon into action or bring into existence</div>
<div class="example">Vacation homes typically
<strong>conjure</strong> up dreams of blue skies, pristine sand and crystalline waters.
<br> —
<a href="http://online.wsj.com/article/SB10001424052970203833004577251631933309866.html?mod=rss_markets_main" rel="nofollow">Wall Street Journal (Feb 28, 2012)</a></div>


</li>






<li class="entry learnable" id="entry242"
 lang="en" word="ominous" freq="624.02" prog="0">

<a class="word dynamictext" href="/dictionary/ominous">ominous</a>
<div class="definition">threatening or foreshadowing evil or tragic developments</div>
<div class="example">The Count's words were so
<strong>ominous</strong>, so full of sinister meaning that for the moment he felt like crying out with fear.
<br> —
<a href="http://www.gutenberg.org/ebooks/39218" rel="nofollow">Hocking, Joseph</a></div>


</li>






<li class="entry learnable" id="entry243"
 lang="en" word="edifice" freq="635.83" prog="0">

<a class="word dynamictext" href="/dictionary/edifice">edifice</a>
<div class="definition">a structure that has a roof and walls</div>
<div class="example">They are here erecting a fine stone
<strong>edifice</strong> for an Episcopal Church.
<br> —
<a href="http://www.gutenberg.org/ebooks/38644" rel="nofollow">Clark, John A.</a></div>


</li>






<li class="entry learnable" id="entry244"
 lang="en" word="elude" freq="637.95" prog="0">

<a class="word dynamictext" href="/dictionary/elude">elude</a>
<div class="definition">escape, either physically or mentally</div>
<div class="example">But despite racking up world titles, Olympic gold was
<strong>eluding</strong> him.
<br> —
<a href="http://www.guardian.co.uk/sport/blog/2012/feb/10/joy-of-six-sportsmanship" rel="nofollow">The Guardian (Feb 10, 2012)</a></div>


</li>






<li class="entry learnable" id="entry245"
 lang="en" word="pervade" freq="643.46" prog="0">

<a class="word dynamictext" href="/dictionary/pervade">pervade</a>
<div class="definition">spread or diffuse through</div>
<div class="example">An air of intense anticipation
<strong>pervaded</strong> the General’s dining room.
<br> —
<a href="http://www.gutenberg.org/ebooks/37310" rel="nofollow">Burnett, Carolyn Judson</a></div>


</li>






<li class="entry learnable" id="entry246"
 lang="en" word="foster" freq="651.31" prog="0">

<a class="word dynamictext" href="/dictionary/foster">foster</a>
<div class="definition">promote the growth of</div>
<div class="example">Mr. Horne accused the district’s Mexican-American studies program of using an antiwhite curriculum to
<strong>foster</strong> social activism.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=873e4a397818f77c45a37a9e03d04699" rel="nofollow">New York Times (Mar 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry247"
 lang="en" word="admonish" freq="652.7" prog="0">

<a class="word dynamictext" href="/dictionary/admonish">admonish</a>
<div class="definition">scold or reprimand; take to task</div>
<div class="example">"Children, children, stop quarrelling, right here in public!"
<strong>admonished</strong> Mrs. Dering, in a low, shocked tone.
<br> —
<a href="http://www.gutenberg.org/ebooks/36105" rel="nofollow">Perry, Nora</a></div>


</li>






<li class="entry learnable" id="entry248"
 lang="en" word="repeal" freq="653.06" prog="0">

<a class="word dynamictext" href="/dictionary/repeal">repeal</a>
<div class="definition">cancel officially</div>
<div class="example">If Republicans
<strong>repeal</strong> the law, Ms. Schakowsky said, they would be “taking away benefits that seniors are already getting.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4907381d79dc71456fe40b4c7e6bc42b" rel="nofollow">New York Times (Mar 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry249"
 lang="en" word="retiring" freq="653.89" prog="0">

<a class="word dynamictext" href="/dictionary/retiring">retiring</a>
<div class="definition">not arrogant or presuming</div>
<div class="example">Foster was an extremely modest, unworldly,
<strong>retiring</strong> gentleman.
<br> —
<a href="http://www.gutenberg.org/ebooks/38746" rel="nofollow">Rosenbach, A. S. W.</a></div>


</li>






<li class="entry learnable" id="entry250"
 lang="en" word="incidental" freq="654.65" prog="0">

<a class="word dynamictext" href="/dictionary/incidental">incidental</a>
<div class="definition">not of prime or central importance</div>
<div class="example">The models themselves are
<strong>incidental</strong> on “Scouted,” merely empty planets around which revolve some fascinating characters and plenty more dull ones.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=588d055f1bda32f8a1f23374e853e614" rel="nofollow">New York Times (Nov 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry251"
 lang="en" word="acquiesce" freq="656.06" prog="0">

<a class="word dynamictext" href="/dictionary/acquiesce">acquiesce</a>
<div class="definition">to agree or express agreement</div>
<div class="example">American officials initially tried to resist President Karzai’s moves but eventually
<strong>acquiesced</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=05e0613f9802b31e132bfe1aef6b5832" rel="nofollow">New York Times (Mar 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry252"
 lang="en" word="slew" freq="656.5" prog="0">

<a class="word dynamictext" href="/dictionary/slew">slew</a>
<div class="definition">a large number or amount or extent</div>
<div class="example">In fact, intense focus may be one reason why so-called savants become so extraordinary at performing extensive calculations or remembering a
<strong>slew</strong> of facts.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=3b3a7596376d783c508f9eaaea837b46" rel="nofollow">Scientific American (Mar 3, 2012)</a></div>


</li>






<li class="entry learnable" id="entry253"
 lang="en" word="usurp" freq="658.69" prog="0">

<a class="word dynamictext" href="/dictionary/usurp">usurp</a>
<div class="definition">seize and take control without authority</div>
<div class="example">More than anything, though, officials expressed concern about reigniting longstanding Mexican concerns about the United States’
<strong>usurping</strong> Mexico’s authority.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=533ab23480ab86fa177896583b5be198" rel="nofollow">New York Times (Mar 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry254"
 lang="en" word="sentinel" freq="668.64" prog="0">

<a class="word dynamictext" href="/dictionary/sentinel">sentinel</a>
<div class="definition">a person employed to keep watch for some anticipated event</div>
<div class="example">The prisoners undressed themselves as usual, and went to bed, observed by the
<strong>sentinel</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38941" rel="nofollow">Drake, Samuel Adams</a></div>


</li>






<li class="entry learnable" id="entry255"
 lang="en" word="precision" freq="675.27" prog="0">

<a class="word dynamictext" href="/dictionary/precision">precision</a>
<div class="definition">the quality of being reproducible in amount or performance</div>
<div class="example">At this time, home ranges of small rodents can not be measured with great
<strong>precision</strong>, therefore any such calculations are, at best, only approximations.
<br> —
<a href="http://www.gutenberg.org/ebooks/38959" rel="nofollow">Douglas, Charles L.</a></div>


</li>






<li class="entry learnable" id="entry256"
 lang="en" word="depose" freq="678.83" prog="0">

<a class="word dynamictext" href="/dictionary/depose">depose</a>
<div class="definition">force to leave an office</div>
<div class="example">Late Wednesday, Mr. Touré, the
<strong>deposed</strong> president, spoke out from hiding for the first time.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=a5915a2b860cf638d39334066692ef60" rel="nofollow">New York Times (Mar 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry257"
 lang="en" word="wanton" freq="684.24" prog="0">

<a class="word dynamictext" href="/dictionary/wanton">wanton</a>
<div class="definition">unprovoked or without motive or justification</div>
<div class="example">I am not a sentimentalist by any means, yet I abominate
<strong>wanton</strong> cruelty.
<br> —
<a href="http://www.gutenberg.org/ebooks/37329" rel="nofollow">Stables, Gordon</a></div>


</li>






<li class="entry learnable" id="entry258"
 lang="en" word="odium" freq="688.53" prog="0">

<a class="word dynamictext" href="/dictionary/odium">odium</a>
<div class="definition">state of disgrace resulting from detestable behavior</div>
<div class="example">This was one of the men who bring
<strong>odium</strong> on the whole class of prisoners, and prejudice society against them.
<br> —
<a href="http://www.gutenberg.org/ebooks/21284" rel="nofollow">Henderson, Frank</a></div>


</li>






<li class="entry learnable" id="entry259"
 lang="en" word="precept" freq="691.78" prog="0">

<a class="word dynamictext" href="/dictionary/precept">precept</a>
<div class="definition">rule of personal conduct</div>
<div class="example">The law of nature has but one
<strong>precept</strong>, "Be strong."
<br> —
<a href="http://www.gutenberg.org/ebooks/39155" rel="nofollow">Williams, C. M.</a></div>


</li>






<li class="entry learnable" id="entry260"
 lang="en" word="deference" freq="698.55" prog="0">

<a class="word dynamictext" href="/dictionary/deference">deference</a>
<div class="definition">a courteous expression of esteem or regard</div>
<div class="example">Other rules, as indicated in Mr. Collins' book, concerned deportment, and demanded constant
<strong>deference</strong> to superiors.
<br> —
<a href="http://www.gutenberg.org/ebooks/39068" rel="nofollow">Faris, John T. (John Thomson)</a></div>


</li>






<li class="entry learnable" id="entry261"
 lang="en" word="fray" freq="711.38" prog="0">

<a class="word dynamictext" href="/dictionary/fray">fray</a>
<div class="definition">a noisy fight</div>
<div class="example">Armed rebels have joined the
<strong>fray</strong> in recent months.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/topNews/~3/uZrYfSdj50w/us-syria-idUSTRE8041A820120127" rel="nofollow">Reuters (Jan 27, 2012)</a></div>


</li>






<li class="entry learnable" id="entry262"
 lang="en" word="candid" freq="713.99" prog="0">

<a class="word dynamictext" href="/dictionary/candid">candid</a>
<div class="definition">openly straightforward and direct without secretiveness</div>
<div class="example">The actor was
<strong>candid</strong> about his own difficult childhood growing up with alcoholic parents.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2017536097_apcncanadaobitneilhope.html?syndication=rss" rel="nofollow">Seattle Times (Feb 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry263"
 lang="en" word="enduring" freq="719.89" prog="0">

<a class="word dynamictext" href="/dictionary/enduring">enduring</a>
<div class="definition">unceasing</div>
<div class="example">What makes the galumphing hubby such an
<strong>enduring</strong> stock character?
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/u82Ik2gZCrU/click.phdo" rel="nofollow">Slate (Mar 26, 2012)</a></div>


</li>






<li class="entry learnable" id="entry264"
 lang="en" word="impertinent" freq="722.35" prog="0">

<a class="word dynamictext" href="/dictionary/impertinent">impertinent</a>
<div class="definition">improperly forward or bold</div>
<div class="example">Imagine calling a famous writer by his first name—it seemed
<strong>impertinent</strong>, to say the least.
<br> —
<a href="http://www.gutenberg.org/ebooks/33554" rel="nofollow">Watkins, Shirley</a></div>


</li>






<li class="entry learnable" id="entry265"
 lang="en" word="bland" freq="731.31" prog="0">

<a class="word dynamictext" href="/dictionary/bland">bland</a>
<div class="definition">lacking stimulating characteristics; uninteresting</div>
<div class="example">Many critics were less than enamored with the kind of “easy listening” Mr. Williams embodied, deriding his approach as
<strong>bland</strong> and unchallenging.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b316c3d0f8a185995eba76a9660a3023" rel="nofollow">New York Times (Oct 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry266"
 lang="en" word="insinuate" freq="733.16" prog="0">

<a class="word dynamictext" href="/dictionary/insinuate">insinuate</a>
<div class="definition">suggest in an indirect or covert way; give to understand</div>
<div class="example">"Good heavens, do you mean to
<strong>insinuate</strong> that I did anything crooked?" said Bojo loudly, yet at the bottom ill at ease.
<br> —
<a href="http://www.gutenberg.org/ebooks/33761" rel="nofollow">Johnson, Owen</a></div>


</li>






<li class="entry learnable" id="entry267"
 lang="en" word="nominal" freq="714.94" prog="0">

<a class="word dynamictext" href="/dictionary/nominal">nominal</a>
<div class="definition">insignificantly small; a matter of form only</div>
<div class="example">He sought
<strong>nominal</strong> damages of one dollar from each defendant.
<br> —
<a href="http://feeds.reuters.com/~r/Reuters/domesticNews/~3/uvWN5QCN6sU/us-usa-security-padilla-idUSTRE80M2G920120123" rel="nofollow">Reuters (Jan 23, 2012)</a></div>


</li>






<li class="entry learnable" id="entry268"
 lang="en" word="suppliant" freq="757.92" prog="0">

<a class="word dynamictext" href="/dictionary/suppliant">suppliant</a>
<div class="definition">humbly entreating</div>
<div class="example">The colonists asked for nothing but what was clearly right and asked in the most respectful and even
<strong>suppliant</strong> manner.
<br> —
<a href="http://www.gutenberg.org/ebooks/33905" rel="nofollow">Judson, L. Carroll</a></div>


</li>






<li class="entry learnable" id="entry269"
 lang="en" word="languid" freq="767.99" prog="0">

<a class="word dynamictext" href="/dictionary/languid">languid</a>
<div class="definition">lacking spirit or liveliness</div>
<div class="example">Many viewers, bored by the
<strong>languid</strong> pace of the show, tuned out early.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=eb52b6401378f7f5e80de185a3d9071a" rel="nofollow">New York Times (Dec 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry270"
 lang="en" word="rave" freq="777.31" prog="0">

<a class="word dynamictext" href="/dictionary/rave">rave</a>
<div class="definition">praise enthusiastically</div>
<div class="example">I have heard lots of women simply
<strong>rave</strong> about him.
<br> —
<a href="http://www.gutenberg.org/ebooks/38753" rel="nofollow">Kauffman, Reginald Wright</a></div>


</li>






<li class="entry learnable" id="entry271"
 lang="en" word="monetary" freq="770.84" prog="0">

<a class="word dynamictext" href="/dictionary/monetary">monetary</a>
<div class="definition">relating to or involving money</div>
<div class="example">A hundred years ago,
<strong>monetary</strong> policy – control over interest rates and the availability of credit – was viewed as a highly contentious political issue.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=5183a28e685379d9790974f69cb53a68" rel="nofollow">New York Times (Mar 29, 2012)</a></div>


</li>






<li class="entry learnable" id="entry272"
 lang="en" word="headlong" freq="781.05" prog="0">

<a class="word dynamictext" href="/dictionary/headlong">headlong</a>
<div class="definition">in a hasty and foolhardy manner</div>
<div class="example">“They may not be wishing to rush
<strong>headlong</strong> back into the same sort of risks just yet.”
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/asiaindex/~3/ooqr-veuxFw/franc-slips-as-snb-signals-readiness-to-aid-currency-yen-falls.html" rel="nofollow">BusinessWeek (Dec 24, 2010)</a></div>


</li>






<li class="entry learnable" id="entry273"
 lang="en" word="infallible" freq="784.57" prog="0">

<a class="word dynamictext" href="/dictionary/infallible">infallible</a>
<div class="definition">incapable of failure or error</div>
<div class="example">But conductors are no more
<strong>infallible</strong> than other people, and once in a blue moon in going through a train they miss a passenger.
<br> —
<a href="http://www.gutenberg.org/ebooks/38846" rel="nofollow">Lynde, Francis</a></div>


</li>






<li class="entry learnable" id="entry274"
 lang="en" word="coax" freq="791.01" prog="0">

<a class="word dynamictext" href="/dictionary/coax">coax</a>
<div class="definition">influence or urge by gentle urging, caressing, or flattering</div>
<div class="example">He used his most enticing manner and did his best to
<strong>coax</strong> the little animal out again.
<br> —
<a href="http://www.gutenberg.org/ebooks/35957" rel="nofollow">Kay, Ross</a></div>


</li>






<li class="entry learnable" id="entry275"
 lang="en" word="explicate" freq="811.87" prog="0">

<a class="word dynamictext" href="/dictionary/explicate">explicate</a>
<div class="definition">elaborate, as of theories and hypotheses</div>
<div class="example">He urged judges to resist the rigid guidelines and to write opinions
<strong>explicating</strong> their reasons for doing so.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=8aafbde9dfd87f783b3597133578a7db" rel="nofollow">New York Times (Jan 22, 2010)</a></div>


</li>






<li class="entry learnable" id="entry276"
 lang="en" word="gaunt" freq="823.16" prog="0">

<a class="word dynamictext" href="/dictionary/gaunt">gaunt</a>
<div class="definition">very thin especially from disease or hunger or cold</div>
<div class="example"><strong>Gaunt</strong>, starved, and ragged, the men marched northwards, leaving the Touat country upon their left hand.
<br> —
<a href="http://www.gutenberg.org/ebooks/38685" rel="nofollow">Mason, A. E. W. (Alfred Edward Woodley)</a></div>


</li>






<li class="entry learnable" id="entry277"
 lang="en" word="morbid" freq="824.88" prog="0">

<a class="word dynamictext" href="/dictionary/morbid">morbid</a>
<div class="definition">suggesting the horror of death and decay</div>
<div class="example">Earlier in the day, however, his demise was watched by spectators with a
<strong>morbid</strong> fascination.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/kmFTaqxvUT4/16watney.html" rel="nofollow">New York Times (Aug 16, 2010)</a></div>


</li>






<li class="entry learnable" id="entry278"
 lang="en" word="ranging" freq="826.14" prog="0">

<a class="word dynamictext" href="/dictionary/ranging">ranging</a>
<div class="definition">wandering freely</div>
<div class="example">His detective work is fascinating and wide
<strong>ranging</strong>.
<br> —
<a href="http://seattletimes.nwsource.com/html/books/2017392666_br05wandering.html?syndication=rss" rel="nofollow">Seattle Times (Feb 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry279"
 lang="en" word="pacify" freq="826.26" prog="0">

<a class="word dynamictext" href="/dictionary/pacify">pacify</a>
<div class="definition">ease the anger, agitation, or strong emotion of</div>
<div class="example">How they
<strong>pacified</strong> him I don’t know, but at the end of two hours he had cooled off enough to let us go aboard.
<br> —
<a href="http://www.gutenberg.org/ebooks/34895" rel="nofollow">Quincy, Samuel M.</a></div>


</li>






<li class="entry learnable" id="entry280"
 lang="en" word="pastoral" freq="833.64" prog="0">

<a class="word dynamictext" href="/dictionary/pastoral">pastoral</a>
<div class="definition">idyllically rustic</div>
<div class="example">He made a considerable reputation as an accomplished painter of quiet
<strong>pastoral</strong> subjects and carefully elaborated landscapes with cattle.
<br> —
<a href="http://www.gutenberg.org/ebooks/38892" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry281"
 lang="en" word="dogged" freq="844.63" prog="0">

<a class="word dynamictext" href="/dictionary/dogged">dogged</a>
<div class="definition">stubbornly unyielding</div>
<div class="example">Some analysts expect Mr. Falcone, who is known for his
<strong>dogged</strong> determination, to just continue to limp along while slashing costs.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=7b35a4f79f7e033572e8c8ec0332002d" rel="nofollow">New York Times (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry282"
 lang="en" word="ebb" freq="847.17" prog="0">

<a class="word dynamictext" href="/dictionary/ebb">ebb</a>
<div class="definition">fall away or decline</div>
<div class="example">Although Gardner’s competitive appetite
<strong>ebbed</strong> after 2004, other cravings did not.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/gZM1I9D0YfM/wrestler-rulon-gardner-plots-comeback-at-london-olympics.html" rel="nofollow">New York Times (Jan 28, 2012)</a></div>


</li>






<li class="entry learnable" id="entry283"
 lang="en" word="aide" freq="853.27" prog="0">

<a class="word dynamictext" href="/dictionary/aide">aide</a>
<div class="definition">someone who acts as assistant</div>
<div class="example">She later found work as a teacher’s
<strong>aide</strong> in a Head Start program in Harlem.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1a1e7dddab75d55d1e77128b76241ebd" rel="nofollow">New York Times (Jan 12, 2012)</a></div>


</li>






<li class="entry learnable" id="entry284"
 lang="en" word="appease" freq="862.03" prog="0">

<a class="word dynamictext" href="/dictionary/appease">appease</a>
<div class="definition">cause to be more favorably inclined; gain the good will of</div>
<div class="example">The king also has tried to
<strong>appease</strong> public anger over corruption.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=cae6ba1521cbd30fe6a8602067e5f8e0" rel="nofollow">New York Times (Feb 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry285"
 lang="en" word="stipulate" freq="868.79" prog="0">

<a class="word dynamictext" href="/dictionary/stipulate">stipulate</a>
<div class="definition">make an express demand or provision in an agreement</div>
<div class="example">The mayor has an executive order in place
<strong>stipulating</strong> that all top officials, except those granted a waiver, live in the city.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2caed676714b86b4d1ed2639623154c0" rel="nofollow">New York Times (Sep 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry286"
 lang="en" word="recourse" freq="889.6" prog="0">

<a class="word dynamictext" href="/dictionary/recourse">recourse</a>
<div class="definition">something or someone turned to for assistance or security</div>
<div class="example">Bargain hunters and holiday shoppers are bad guys’ favorite targets and have little or no
<strong>recourse</strong> when shoddy or fake merchandise arrives.
<br> —
<a href="http://www.forbes.com/sites/davidcoursey/2011/11/22/dont-let-the-cyber-grinch-steal-christmas/" rel="nofollow">Forbes (Nov 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry287"
 lang="en" word="constrained" freq="902.41" prog="0">

<a class="word dynamictext" href="/dictionary/constrained">constrained</a>
<div class="definition">lacking spontaneity; not natural</div>
<div class="example">All his goodness, however, will be of a forced,
<strong>constrained</strong>, artificial, and at bottom unreal character.
<br> —
<a href="http://www.gutenberg.org/ebooks/39065" rel="nofollow">Hyde, William De Witt</a></div>


</li>






<li class="entry learnable" id="entry288"
 lang="en" word="bate" freq="905.59" prog="0">

<a class="word dynamictext" href="/dictionary/bate">bate</a>
<div class="definition">moderate or restrain; lessen the force of</div>
<div class="example">“You called her ‘an interfering, disagreeable old woman’!” whispered Bertha with
<strong>bated</strong> breath, glancing half fearfully at the door as she spoke.
<br> —
<a href="http://www.gutenberg.org/ebooks/36874" rel="nofollow">Vaizey, George de Horne, Mrs.</a></div>


</li>






<li class="entry learnable" id="entry289"
 lang="en" word="aversion" freq="906" prog="0">

<a class="word dynamictext" href="/dictionary/aversion">aversion</a>
<div class="definition">a feeling of intense dislike</div>
<div class="example">Already my passive dislike had grown into an active
<strong>aversion</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/39018" rel="nofollow">Oppenheim, E. Phillips (Edward Phillips)</a></div>


</li>






<li class="entry learnable" id="entry290"
 lang="en" word="conceit" freq="915.45" prog="0">

<a class="word dynamictext" href="/dictionary/conceit">conceit</a>
<div class="definition">an artistic device or effect</div>
<div class="example">An urban panorama is viewed from a high vantage point, a
<strong>conceit</strong> used in topographic art to render vast perspectives.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2fc8551293c80f50fab6137136e9c4fe" rel="nofollow">New York Times (Sep 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry291"
 lang="en" word="loath" freq="933.71" prog="0">

<a class="word dynamictext" href="/dictionary/loath">loath</a>
<div class="definition">strongly opposed</div>
<div class="example">Friends and political allies are
<strong>loath</strong> to talk about her, knowing the family’s intense obsession with privacy.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=ccc629402fc73a674370e8f52f6ecb0b" rel="nofollow">New York Times (Aug 14, 2011)</a></div>


</li>






<li class="entry learnable" id="entry292"
 lang="en" word="rampart" freq="937.78" prog="0">

<a class="word dynamictext" href="/dictionary/rampart">rampart</a>
<div class="definition">an embankment built around a space for defensive purposes</div>
<div class="example">The night was gloomy, dark, and wet; the soldiers, wearied with watching at the
<strong>ramparts</strong>, dozed, leaning on their weapons.
<br> —
<a href="http://www.gutenberg.org/ebooks/37027" rel="nofollow">Sienkiewicz, Henryk</a></div>


</li>






<li class="entry learnable" id="entry293"
 lang="en" word="extort" freq="939.71" prog="0">

<a class="word dynamictext" href="/dictionary/extort">extort</a>
<div class="definition">obtain by coercion or intimidation</div>
<div class="example">The owners, in turn, have called the lawyers shakedown artists bent on ruining their good reputations to
<strong>extort</strong> money.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/qGGs15NCt90/expert-witnesses-faulted-in-suit-against-mets-owners.html" rel="nofollow">New York Times (Jan 27, 2012)</a></div>


</li>






<li class="entry learnable" id="entry294"
 lang="en" word="tarry" freq="941.43" prog="0">

<a class="word dynamictext" href="/dictionary/tarry">tarry</a>
<div class="definition">leave slowly and hesitantly</div>
<div class="example">For two days I
<strong>tarried</strong> in Paris, settling my little property.
<br> —
<a href="http://www.gutenberg.org/ebooks/36439" rel="nofollow">Ford, Paul Leicester</a></div>


</li>






<li class="entry learnable" id="entry295"
 lang="en" word="perpetrate" freq="942.63" prog="0">

<a class="word dynamictext" href="/dictionary/perpetrate">perpetrate</a>
<div class="definition">perform an act, usually with a negative connotation</div>
<div class="example">Come on it’s just a cruel joke
<strong>perpetrated</strong> by the airline industry.”
<br> —
<a href="http://www.forbes.com/sites/erikamorphy/2011/12/11/companies-cant-win-the-twitter-wars-especially-against-the-likes-of-alec-baldwin/" rel="nofollow">Forbes (Dec 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry296"
 lang="en" word="decorum" freq="944.36" prog="0">

<a class="word dynamictext" href="/dictionary/decorum">decorum</a>
<div class="definition">propriety in manners and conduct</div>
<div class="example">Wishing to observe the rules of
<strong>decorum</strong> she invited him to stay for supper, though absolutely nothing had been prepared for a guest.
<br> —
<a href="http://www.gutenberg.org/ebooks/34791" rel="nofollow">Sudermann, Hermann</a></div>


</li>






<li class="entry learnable" id="entry297"
 lang="en" word="luxuriant" freq="951.33" prog="0">

<a class="word dynamictext" href="/dictionary/luxuriant">luxuriant</a>
<div class="definition">produced or growing in extreme abundance</div>
<div class="example">Her
<strong>luxuriant</strong> curly hair, restrained by no net, but held together simply by a flowering spray, waved over her shoulders in all its rich abundance.
<br> —
<a href="http://www.gutenberg.org/ebooks/39194" rel="nofollow">Elisabeth Burstenbinder (AKA E. Werner)</a></div>


</li>






<li class="entry learnable" id="entry298"
 lang="en" word="cant" freq="952.64" prog="0">

<a class="word dynamictext" href="/dictionary/cant">cant</a>
<div class="definition">insincere talk about religion or morals</div>
<div class="example">It was the familiar
<strong>cant</strong> of the man rich enough to affect disdain for money, and Wade was not impressed.
<br> —
<a href="http://www.gutenberg.org/ebooks/34948" rel="nofollow">Day, Holman</a></div>


</li>






<li class="entry learnable" id="entry299"
 lang="en" word="enjoin" freq="964.98" prog="0">

<a class="word dynamictext" href="/dictionary/enjoin">enjoin</a>
<div class="definition">give instructions to or direct somebody to do something</div>
<div class="example">He turned to beckon the others forward with one hand, while laying the other over his mouth in a gesture
<strong>enjoining</strong> silence.
<br> —
<a href="http://www.gutenberg.org/ebooks/36314" rel="nofollow">Breckenridge, Gerald</a></div>


</li>






<li class="entry learnable" id="entry300"
 lang="en" word="avarice" freq="965.84" prog="0">

<a class="word dynamictext" href="/dictionary/avarice">avarice</a>
<div class="definition">extreme greed for material wealth</div>
<div class="example">The old man's fears were assailed with threats, and his
<strong>avarice</strong> was approached by bribes, and he very soon capitulated.
<br> —
<a href="http://www.gutenberg.org/ebooks/32490" rel="nofollow">Abbott, John S. C. (John Stevens Cabot)</a></div>


</li>






<li class="entry learnable" id="entry301"
 lang="en" word="edict" freq="971.87" prog="0">

<a class="word dynamictext" href="/dictionary/edict">edict</a>
<div class="definition">a formal or authoritative proclamation</div>
<div class="example">An
<strong>edict</strong> was issued by him forbidding any Christian to give instruction in Greek literature under any circumstances.
<br> —
<a href="http://www.gutenberg.org/ebooks/37527" rel="nofollow">Lightfoot, J. B.</a></div>


</li>






<li class="entry learnable" id="entry302"
 lang="en" word="disconcert" freq="977.24" prog="0">

<a class="word dynamictext" href="/dictionary/disconcert">disconcert</a>
<div class="definition">cause to lose one's composure</div>
<div class="example">Perplexed and
<strong>disconcerted</strong>, I found no words to answer such an amazing sally.
<br> —
<a href="http://www.gutenberg.org/ebooks/38958" rel="nofollow">Chambers, Robert W. (Robert William)</a></div>


</li>






<li class="entry learnable" id="entry303"
 lang="en" word="symmetry" freq="989.15" prog="0">

<a class="word dynamictext" href="/dictionary/symmetry">symmetry</a>
<div class="definition">balance among the parts of something</div>
<div class="example">Even the staging displays
<strong>symmetry</strong>, with actors lined up on either side in formal precision.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1ffe2a961cc61855960b859f52ad9ced" rel="nofollow">New York Times (Jan 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry304"
 lang="en" word="capitulate" freq="999.17" prog="0">

<a class="word dynamictext" href="/dictionary/capitulate">capitulate</a>
<div class="definition">surrender under agreed conditions</div>
<div class="example">"Alas, no," said Bergfeld, mournfully, "the day after the battle our brave soldiers were surrounded by overwhelming forces and obliged to
<strong>capitulate</strong>."
<br> —
<a href="http://www.gutenberg.org/ebooks/37724" rel="nofollow">Meding, Johann Ferdinand Martin Oskar</a></div>


</li>






<li class="entry learnable" id="entry305"
 lang="en" word="arbitrate" freq="1000.35" prog="0">

<a class="word dynamictext" href="/dictionary/arbitrate">arbitrate</a>
<div class="definition">act between parties with a view to reconciling differences</div>
<div class="example">The Scottish throne was now disputed by many claimants, and the Scots asked Edward to
<strong>arbitrate</strong> between them.
<br> —
<a href="http://www.gutenberg.org/ebooks/34992" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry306"
 lang="en" word="cleave" freq="1009.22" prog="0">

<a class="word dynamictext" href="/dictionary/cleave">cleave</a>
<div class="definition">separate or cut with a tool, such as a sharp instrument</div>
<div class="example">Instead someone shouts "Go" and he is bearing down on me and almost
<strong>cleaves</strong> my shield in two with his first blow.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-europe-14378984" rel="nofollow">BBC (Aug 7, 2011)</a></div>


</li>






<li class="entry learnable" id="entry307"
 lang="en" word="append" freq="1015.01" prog="0">

<a class="word dynamictext" href="/dictionary/append">append</a>
<div class="definition">add to the very end</div>
<div class="example">Some specimens will appear in the papers
<strong>appended</strong> to this report.
<br> —
<a href="http://www.gutenberg.org/ebooks/32938" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry308"
 lang="en" word="visage" freq="1028.32" prog="0">

<a class="word dynamictext" href="/dictionary/visage">visage</a>
<div class="definition">the human face</div>
<div class="example">An honest, quiet laugh often mantled his pale earnest
<strong>visage</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38822" rel="nofollow">Turnbull, Robert</a></div>


</li>






<li class="entry learnable" id="entry309"
 lang="en" word="horde" freq="1028.68" prog="0">

<a class="word dynamictext" href="/dictionary/horde">horde</a>
<div class="definition">a moving crowd</div>
<div class="example"><strong>Hordes</strong> of puzzled tourists, many with rolling suitcases attached, poured down the staircases.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=23d0ffb2f81e6ac4ef8542696bf49c53" rel="nofollow">New York Times (Jan 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry310"
 lang="en" word="parable" freq="1092.35" prog="0">

<a class="word dynamictext" href="/dictionary/parable">parable</a>
<div class="definition">a short moral story </div>
<div class="example">In most instances, I have closed my visits by reading some interesting story or
<strong>parable</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38907" rel="nofollow">Frothingham, Octavius Brooks</a></div>


</li>






<li class="entry learnable" id="entry311"
 lang="en" word="chastise" freq="1031.27" prog="0">

<a class="word dynamictext" href="/dictionary/chastise">chastise</a>
<div class="definition">censure severely</div>
<div class="example">She remembers an upsetting incident when a headmistress
<strong>chastised</strong> her for working too much.
<br> —
<a href="http://www.guardian.co.uk/lifeandstyle/2011/jan/14/christine-lagarde-french-finance-minister-g8" rel="nofollow">The Guardian (Jan 14, 2011)</a></div>


</li>






<li class="entry learnable" id="entry312"
 lang="en" word="foil" freq="1033.98" prog="0">

<a class="word dynamictext" href="/dictionary/foil">foil</a>
<div class="definition">hinder or prevent, as an effort, plan, or desire</div>
<div class="example">On March 1st, a Turkish newspaper reported that the country's intelligence service had
<strong>foiled</strong> an attempt by Syrian agents to kidnap the colonel.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/aIu9U0Mn4Lc/0,8599,2108668,00.html" rel="nofollow">Time (Mar 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry313"
 lang="en" word="veritable" freq="1037.87" prog="0">

<a class="word dynamictext" href="/dictionary/veritable">veritable</a>
<div class="definition">being truly so called; real or genuine</div>
<div class="example">The heavy rain had reduced this low-lying ground to a
<strong>veritable</strong> quagmire, making progress very difficult even for one as unburdened as he was.
<br> —
<a href="http://www.gutenberg.org/ebooks/37376" rel="nofollow">Putnam Weale, B. L. (Bertram Lenox)</a></div>


</li>






<li class="entry learnable" id="entry314"
 lang="en" word="grapple" freq="1043.27" prog="0">

<a class="word dynamictext" href="/dictionary/grapple">grapple</a>
<div class="definition">come to terms with</div>
<div class="example">But, he said, all coastal communities will have to
<strong>grapple</strong> with rising seas.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e48b9da01b674eea0a158e25adbf6e5c" rel="nofollow">New York Times (Mar 24, 2012)</a></div>


</li>






<li class="entry learnable" id="entry315"
 lang="en" word="gentry" freq="1048.53" prog="0">

<a class="word dynamictext" href="/dictionary/gentry">gentry</a>
<div class="definition">the most powerful members of a society</div>
<div class="example">The mode of travel of the
<strong>gentry</strong> was riding horses, but most people traveled by walking.
<br> —
<a href="http://www.gutenberg.org/ebooks/36299" rel="nofollow">Reilly, S. A.</a></div>


</li>






<li class="entry learnable" id="entry316"
 lang="en" word="pall" freq="1049" prog="0">

<a class="word dynamictext" href="/dictionary/pall">pall</a>
<div class="definition">a sudden numbing dread</div>
<div class="example">Residents who fled in recent days spoke of the smell of death and piles of garbage drifting like snowbanks, casting a
<strong>pall</strong> over the city.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=70a5b2d116d1b3da0bb5f34ee176ea25" rel="nofollow">New York Times (Mar 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry317"
 lang="en" word="maxim" freq="1049.28" prog="0">

<a class="word dynamictext" href="/dictionary/maxim">maxim</a>
<div class="definition">a saying that is widely accepted on its own merits</div>
<div class="example">The
<strong>maxim</strong> "All is fair in love and war" was applied literally.
<br> —
<a href="http://www.gutenberg.org/ebooks/38432" rel="nofollow">Thomson, Basil</a></div>


</li>






<li class="entry learnable" id="entry318"
 lang="en" word="projection" freq="1050.77" prog="0">

<a class="word dynamictext" href="/dictionary/projection">projection</a>
<div class="definition">a prediction made by extrapolating from past observations</div>
<div class="example">Volume is down 25 percent from five years ago, and
<strong>projections</strong> show even further declines, said Postmaster General Patrick R. Donahoe.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=eeef827f03e5d2fe6733e243719483b8" rel="nofollow">New York Times (Mar 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry319"
 lang="en" word="prowess" freq="1067.82" prog="0">

<a class="word dynamictext" href="/dictionary/prowess">prowess</a>
<div class="definition">a superior skill learned by study and practice </div>
<div class="example">While our engineering
<strong>prowess</strong> has advanced a great deal over the past sixty years, the principles of innovation largely have not.
<br> —
<a href="http://feedproxy.google.com/~r/time/business/~3/44sJvpiPEUI/" rel="nofollow">Time (Mar 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry320"
 lang="en" word="dingy" freq="1075.68" prog="0">

<a class="word dynamictext" href="/dictionary/dingy">dingy</a>
<div class="definition">thickly covered with ingrained dirt or soot</div>
<div class="example">Though composed amid the unromantic surroundings of a
<strong>dingy</strong>, dusty, and neglected back room, the speech has become a memorable document.
<br> —
<a href="http://www.gutenberg.org/ebooks/38484" rel="nofollow">Herndon, William H.</a></div>


</li>






<li class="entry learnable" id="entry321"
 lang="en" word="semblance" freq="1083.35" prog="0">

<a class="word dynamictext" href="/dictionary/semblance">semblance</a>
<div class="definition">an outward appearance that is deliberately misleading</div>
<div class="example">He was perceptibly older, in the way in which people look older all at once after having long kept the
<strong>semblance</strong> of youth.
<br> —
<a href="http://www.gutenberg.org/ebooks/35463" rel="nofollow">King, Basil</a></div>


</li>






<li class="entry learnable" id="entry322"
 lang="en" word="tout" freq="1089.53" prog="0">

<a class="word dynamictext" href="/dictionary/tout">tout</a>
<div class="definition">advertise in strongly positive terms</div>
<div class="example">Testing is being
<strong>touted</strong> as the means of making the U.S. education system competitive, even world-class.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=5dd828f0ea6bc3bbf059a80a43c69558" rel="nofollow">Washington Post (Mar 23, 2012)</a></div>


</li>






<li class="entry learnable" id="entry323"
 lang="en" word="fortitude" freq="1090.74" prog="0">

<a class="word dynamictext" href="/dictionary/fortitude">fortitude</a>
<div class="definition">strength of mind that enables one to endure adversity</div>
<div class="example">Leigh Hunt bore himself in his captivity with cheerful
<strong>fortitude</strong>, suffering severely in health but flagging little in spirits or industry.
<br> —
<a href="http://www.gutenberg.org/ebooks/36356" rel="nofollow">Colvin, Sidney</a></div>


</li>






<li class="entry learnable" id="entry324"
 lang="en" word="asunder" freq="1094.47" prog="0">

<a class="word dynamictext" href="/dictionary/asunder">asunder</a>
<div class="definition">into parts or pieces</div>
<div class="example">In 1854, as I have already remarked, Nicaragua was split
<strong>asunder</strong> by civil war.
<br> —
<a href="http://www.gutenberg.org/ebooks/37812" rel="nofollow">Powell, E. Alexander (Edward Alexander)</a></div>


</li>






<li class="entry learnable" id="entry325"
 lang="en" word="rout" freq="1095.38" prog="0">

<a class="word dynamictext" href="/dictionary/rout">rout</a>
<div class="definition">an overwhelming defeat</div>
<div class="example">It's how Seattle won Sunday's game in Chicago, scoring 31 consecutive second-half points as an impressive comeback became an overwhelming
<strong>rout</strong>.
<br> —
<a href="http://seattletimes.nwsource.com/html/seahawks/2017052106_hawk20.html?syndication=rss" rel="nofollow">Seattle Times (Dec 19, 2011)</a></div>


</li>






<li class="entry learnable" id="entry326"
 lang="en" word="staid" freq="1098.73" prog="0">

<a class="word dynamictext" href="/dictionary/staid">staid</a>
<div class="definition">characterized by dignity and propriety</div>
<div class="example">He was prim and
<strong>staid</strong> and liked to do things in an orderly fashion.
<br> —
<a href="http://www.gutenberg.org/ebooks/34797" rel="nofollow">Doyle, A. Conan</a></div>


</li>






<li class="entry learnable" id="entry327"
 lang="en" word="beguile" freq="1103.65" prog="0">

<a class="word dynamictext" href="/dictionary/beguile">beguile</a>
<div class="definition">influence by slyness</div>
<div class="example">I can no longer remain silent in the presence of the schemers who seek to
<strong>beguile</strong> you.
<br> —
<a href="http://www.gutenberg.org/ebooks/33487" rel="nofollow">Bolanden, Conrad von</a></div>


</li>






<li class="entry learnable" id="entry328"
 lang="en" word="purport" freq="1106.02" prog="0">

<a class="word dynamictext" href="/dictionary/purport">purport</a>
<div class="definition">have the often specious appearance of being or intending</div>
<div class="example">Of course, none of these
<strong>purported</strong> medical benefits have any grounding in science.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=11f9c201d527cfe1bbc02745e6085881" rel="nofollow">Scientific American (Jan 28, 2012)</a></div>


</li>






<li class="entry learnable" id="entry329"
 lang="en" word="deprave" freq="1112.57" prog="0">

<a class="word dynamictext" href="/dictionary/deprave">deprave</a>
<div class="definition">corrupt morally or by intemperance or sensuality</div>
<div class="example">The people who make up this typical Gorky offering are drunkards, thieves,
<strong>depraved</strong> creatures of every kind.
<br> —
<a href="http://www.gutenberg.org/ebooks/39103" rel="nofollow">Kilmer, Joyce</a></div>


</li>






<li class="entry learnable" id="entry330"
 lang="en" word="bequeath" freq="1113.72" prog="0">

<a class="word dynamictext" href="/dictionary/bequeath">bequeath</a>
<div class="definition">leave or give by will after one's death</div>
<div class="example">No matter how often she changed her will, she told me, that diamond pin was always
<strong>bequeathed</strong> to me.
<br> —
<a href="http://www.gutenberg.org/ebooks/35022" rel="nofollow">Wells, Carolyn</a></div>


</li>






<li class="entry learnable" id="entry331"
 lang="en" word="enigma" freq="1126.43" prog="0">

<a class="word dynamictext" href="/dictionary/enigma">enigma</a>
<div class="definition">something that baffles understanding and cannot be explained</div>
<div class="example">Tails are often an
<strong>enigma</strong>; many creatures have them, but scientists know little about their function, particularly for extinct species.
<br> —
<a href="http://news.sciencemag.org/sciencenow/2012/01/tails-guided-leaping-dinosaurs-t.html?rss=1" rel="nofollow">Science Magazine (Jan 4, 2012)</a></div>


</li>






<li class="entry learnable" id="entry332"
 lang="en" word="assiduous" freq="1132.58" prog="0">

<a class="word dynamictext" href="/dictionary/assiduous">assiduous</a>
<div class="definition">marked by care and persistent effort</div>
<div class="example">He's an
<strong>assiduous</strong> diary-keeper and regularly rereads ancient entries to check up on himself.
<br> —
<a href="http://www.guardian.co.uk/film/2010/jul/18/oliver-stone-chavez-wall-street" rel="nofollow">The Guardian (Jul 17, 2010)</a></div>


</li>






<li class="entry learnable" id="entry333"
 lang="en" word="vassal" freq="1135.62" prog="0">

<a class="word dynamictext" href="/dictionary/vassal">vassal</a>
<div class="definition">a person holding a fief</div>
<div class="example">And what was of still greater importance, he could only obtain taxes and soldiers from among the
<strong>vassals</strong>, by the consent of their feudal lords.
<br> —
<a href="http://www.gutenberg.org/ebooks/33794" rel="nofollow">Freytag, Gustav</a></div>


</li>






<li class="entry learnable" id="entry334"
 lang="en" word="quail" freq="1141.86" prog="0">

<a class="word dynamictext" href="/dictionary/quail">quail</a>
<div class="definition">draw back, as with fear or pain</div>
<div class="example">He
<strong>quailed</strong> before me, and forgetting his new part in old habits, muttered an apology.
<br> —
<a href="http://www.gutenberg.org/ebooks/39297" rel="nofollow">Weyman, Stanley John</a></div>


</li>






<li class="entry learnable" id="entry335"
 lang="en" word="outskirts" freq="1142.19" prog="0">

<a class="word dynamictext" href="/dictionary/outskirts">outskirts</a>
<div class="definition">outlying areas, as of a city or town</div>
<div class="example">Ms. Waters talked about how she had spent the day at an organic farm on the
<strong>outskirts</strong> of Beijing looking at vegetables for the dinner.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e1ce95242800968e217dc205a0eebc9e" rel="nofollow">New York Times (Nov 14, 2011)</a></div>


</li>






<li class="entry learnable" id="entry336"
 lang="en" word="bulwark" freq="1142.52" prog="0">

<a class="word dynamictext" href="/dictionary/bulwark">bulwark</a>
<div class="definition">a protective structure of stone or concrete</div>
<div class="example">The cliffs are of imposing height, nearly three hundred feet: a formidable
<strong>bulwark</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/35933" rel="nofollow">White, Walter</a></div>


</li>






<li class="entry learnable" id="entry337"
 lang="en" word="swerve" freq="1152.42" prog="0">

<a class="word dynamictext" href="/dictionary/swerve">swerve</a>
<div class="definition">an erratic turn from an intended course</div>
<div class="example">However, I was not going to
<strong>swerve</strong> from my word.
<br> —
<a href="http://www.gutenberg.org/ebooks/37839" rel="nofollow">Johnstone, James Johnstone, chevalier de</a></div>


</li>






<li class="entry learnable" id="entry338"
 lang="en" word="gird" freq="1153.77" prog="0">

<a class="word dynamictext" href="/dictionary/gird">gird</a>
<div class="definition">prepare oneself for a military confrontation</div>
<div class="example">Protesters are
<strong>girding</strong> for another police raid as several City Council members have called on protesters to leave.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=7c2a388f5bb10233968059a2b4769d99" rel="nofollow">Washington Post (Nov 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry339"
 lang="en" word="betrothed" freq="1155" prog="0">

<a class="word dynamictext" href="/dictionary/betrothed">betrothed</a>
<div class="definition">pledged to be married</div>
<div class="example">We are not
<strong>betrothed</strong>'—her eyes filled with tears,—'he can never marry me; and he and my father have quarrelled.
<br> —
<a href="http://www.gutenberg.org/ebooks/34686" rel="nofollow">Fleming, George</a></div>


</li>






<li class="entry learnable" id="entry340"
 lang="en" word="prospective" freq="1160.55" prog="0">

<a class="word dynamictext" href="/dictionary/prospective">prospective</a>
<div class="definition">of or concerned with or related to the future</div>
<div class="example">Most
<strong>prospective</strong> homesteaders make the same mistake I did in buying horses, unless they are experienced.
<br> —
<a href="http://www.gutenberg.org/ebooks/39237" rel="nofollow">Micheaux, Oscar</a></div>


</li>






<li class="entry learnable" id="entry341"
 lang="en" word="advert" freq="1165.12" prog="0">

<a class="word dynamictext" href="/dictionary/advert">advert</a>
<div class="definition">make reference to</div>
<div class="example">In the family circle it was rarely
<strong>adverted</strong> to, and never except when some allusion to the approaching separation had to be made.
<br> —
<a href="http://www.gutenberg.org/ebooks/35032" rel="nofollow">Werner, E. T. C. (Edward Theodore Chalmers)</a></div>


</li>






<li class="entry learnable" id="entry342"
 lang="en" word="peremptory" freq="1166.38" prog="0">

<a class="word dynamictext" href="/dictionary/peremptory">peremptory</a>
<div class="definition">not allowing contradiction or refusal</div>
<div class="example">This time it was not a request but a
<strong>peremptory</strong> order to go at once to Cuba and undertake the work.
<br> —
<a href="http://www.gutenberg.org/ebooks/33847" rel="nofollow">Johnson, Willis Fletcher</a></div>


</li>






<li class="entry learnable" id="entry343"
 lang="en" word="rudiment" freq="1181.51" prog="0">

<a class="word dynamictext" href="/dictionary/rudiment">rudiment</a>
<div class="definition">the elementary stage of any subject</div>
<div class="example">He retraced his steps, and came to Cape Girardeau, in Missouri, where he remained some time, acquiring the
<strong>rudiments</strong> of the English language.
<br> —
<a href="http://www.gutenberg.org/ebooks/39333" rel="nofollow">Anonymous</a></div>


</li>






<li class="entry learnable" id="entry344"
 lang="en" word="deduce" freq="1181.87" prog="0">

<a class="word dynamictext" href="/dictionary/deduce">deduce</a>
<div class="definition">reason from the general to the particular</div>
<div class="example">They then used models of global wind circulation to
<strong>deduce</strong> which dust sources have become stronger and which weaker.
<br> —
<a href="http://www.economist.com/sciencetechnology/displaystory.cfm?story_id=17848493&amp;fsrc=rss" rel="nofollow">Economist (Jan 6, 2011)</a></div>


</li>






<li class="entry learnable" id="entry345"
 lang="en" word="halting" freq="1191.02" prog="0">

<a class="word dynamictext" href="/dictionary/halting">halting</a>
<div class="definition">fragmentary or broken from emotional strain</div>
<div class="example">“I so much love cricket,” he said, shyly, in
<strong>halting</strong> English.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=109fcf4fc708f18fdd375aa77595e1ed" rel="nofollow">New York Times (Feb 22, 2012)</a></div>


</li>






<li class="entry learnable" id="entry346"
 lang="en" word="ignominy" freq="1197.89" prog="0">

<a class="word dynamictext" href="/dictionary/ignominy">ignominy</a>
<div class="definition">a state of dishonor</div>
<div class="example">After all, we love nothing better than seeing the powerful and formerly smug dragged across the front pages in
<strong>ignominy</strong>.
<br> —
<a href="http://feedproxy.google.com/~r/time/nation/~3/e2gdi4ZAk4U/0,8599,2076113,00.html" rel="nofollow">Time (Jun 7, 2011)</a></div>


</li>






<li class="entry learnable" id="entry347"
 lang="en" word="ideology" freq="1209.52" prog="0">

<a class="word dynamictext" href="/dictionary/ideology">ideology</a>
<div class="definition">an orientation that characterizes the thinking of a group</div>
<div class="example">Bill O’Reilly and others picked up on the theme, summing up left-wing
<strong>ideology</strong> as “San Francisco values.”
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/r027Kox7-Tg/click.phdo" rel="nofollow">Slate (Jan 19, 2012)</a></div>


</li>






<li class="entry learnable" id="entry348"
 lang="en" word="pallid" freq="1209.52" prog="0">

<a class="word dynamictext" href="/dictionary/pallid">pallid</a>
<div class="definition">lacking in vitality or interest or effectiveness</div>
<div class="example">But too often the music sounded thin and
<strong>pallid</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=7d802772ad1df388e1321fd9748c8fd6" rel="nofollow">New York Times (Apr 25, 2010)</a></div>


</li>






<li class="entry learnable" id="entry349"
 lang="en" word="chagrin" freq="1222.13" prog="0">

<a class="word dynamictext" href="/dictionary/chagrin">chagrin</a>
<div class="definition">strong feelings of embarrassment</div>
<div class="example">But he was feeling deeply
<strong>chagrined</strong> and mortified over his last escapade.
<br> —
<a href="http://www.gutenberg.org/ebooks/36511" rel="nofollow">White, Fred M. (Fred Merrick)</a></div>


</li>






<li class="entry learnable" id="entry350"
 lang="en" word="obtrude" freq="1230.26" prog="0">

<a class="word dynamictext" href="/dictionary/obtrude">obtrude</a>
<div class="definition">thrust oneself in as if by force</div>
<div class="example">She had no right to
<strong>obtrude</strong> herself into his life and to disturb it.
<br> —
<a href="http://www.gutenberg.org/ebooks/34034" rel="nofollow">Packard, Frank L. (Frank Lucius)</a></div>


</li>






<li class="entry learnable" id="entry351"
 lang="en" word="audacious" freq="1243.31" prog="0">

<a class="word dynamictext" href="/dictionary/audacious">audacious</a>
<div class="definition">disposed to venture or take risks</div>
<div class="example">In an
<strong>audacious</strong> operation that unfolded like a Hollywood thriller, the Navy Seals executed a daring raid deep into Pakistan to kill Osama bin Laden.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=053b81821103426a699e8d4560bafc50" rel="nofollow">New York Times (Sep 4, 2011)</a></div>


</li>






<li class="entry learnable" id="entry352"
 lang="en" word="construe" freq="1245.92" prog="0">

<a class="word dynamictext" href="/dictionary/construe">construe</a>
<div class="definition">make sense of; assign a meaning to</div>
<div class="example">But nothing that was said Tuesday can be
<strong>construed</strong> as good news.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=931358086b2362583232de60964b66a7" rel="nofollow">Washington Post (Sep 14, 2011)</a></div>


</li>






<li class="entry learnable" id="entry353"
 lang="en" word="ford" freq="1250.66" prog="0">

<a class="word dynamictext" href="/dictionary/ford">ford</a>
<div class="definition">cross a river where it's shallow</div>
<div class="example">Sometimes they drive their teams through unsettled country, without roads, swimming and
<strong>fording</strong> streams, clearing away obstructions, and camping where night overtakes them.
<br> —
<a href="http://www.gutenberg.org/ebooks/36375" rel="nofollow">Folsom, William Henry Carman</a></div>


</li>






<li class="entry learnable" id="entry354"
 lang="en" word="repast" freq="1251.19" prog="0">

<a class="word dynamictext" href="/dictionary/repast">repast</a>
<div class="definition">the food served and eaten at one time</div>
<div class="example">Fragrant coffee, light rolls, fresh butter, ham and eggs, fried crocuses and soft crabs, formed the
<strong>repast</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/35195" rel="nofollow">Reid, Mayne</a></div>


</li>






<li class="entry learnable" id="entry355"
 lang="en" word="stint" freq="1251.19" prog="0">

<a class="word dynamictext" href="/dictionary/stint">stint</a>
<div class="definition">an unbroken period of time during which you do something</div>
<div class="example">He found his unionized warehouse job after a
<strong>stint</strong> working for his father, an accountant.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6ddedf3182bbfc9d11f854c8e8828d3b" rel="nofollow">New York Times (Mar 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry356"
 lang="en" word="fresco" freq="1251.46" prog="0">

<a class="word dynamictext" href="/dictionary/fresco">fresco</a>
<div class="definition">a mural done with watercolors on wet plaster</div>
<div class="example">The little church has an ancient
<strong>fresco</strong> of St. Christopher, placed, as usual, opposite the entrance.
<br> —
<a href="http://www.gutenberg.org/ebooks/38735" rel="nofollow">Conybeare, Edward</a></div>


</li>






<li class="entry learnable" id="entry357"
 lang="en" word="dutiful" freq="1253.71" prog="0">

<a class="word dynamictext" href="/dictionary/dutiful">dutiful</a>
<div class="definition">willingly obedient out of a sense of respect</div>
<div class="example">Perhaps he thinks an engaged young lady should be demure and
<strong>dutiful</strong>, having no eyes or ears for any one except her betrothed.
<br> —
<a href="http://www.gutenberg.org/ebooks/36414" rel="nofollow">Harland, Marion</a></div>


</li>






<li class="entry learnable" id="entry358"
 lang="en" word="hew" freq="1257.04" prog="0">

<a class="word dynamictext" href="/dictionary/hew">hew</a>
<div class="definition">make or shape as with an axe</div>
<div class="example">They bought a log chain, and lumber for a door; the window frames were
<strong>hewed</strong> from logs.
<br> —
<a href="http://www.gutenberg.org/ebooks/34844" rel="nofollow">Daughters of the American Revolution. Nebraska</a></div>


</li>






<li class="entry learnable" id="entry359"
 lang="en" word="parity" freq="1257.44" prog="0">

<a class="word dynamictext" href="/dictionary/parity">parity</a>
<div class="definition">functional equality</div>
<div class="example">How many of the world’s problems would be solved, or at least greatly reduced, if women had true
<strong>parity</strong> with men?
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=9246dee8f4b0d92ad6e316bd260bc89c" rel="nofollow">New York Times (Dec 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry360"
 lang="en" word="affable" freq="1259.98" prog="0">

<a class="word dynamictext" href="/dictionary/affable">affable</a>
<div class="definition">diffusing warmth and friendliness</div>
<div class="example">He was well liked and respected in these islands, for his
<strong>affable</strong> manners had obtained for him much popularity.
<br> —
<a href="http://www.gutenberg.org/ebooks/38748" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry361"
 lang="en" word="interminable" freq="1282.37" prog="0">

<a class="word dynamictext" href="/dictionary/interminable">interminable</a>
<div class="definition">tiresomely long; seemingly without end</div>
<div class="example">All was going well, but slowly, the time taken for the last few feet seeming to be
<strong>interminable</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38542" rel="nofollow">Cumberland, Barlow</a></div>


</li>






<li class="entry learnable" id="entry362"
 lang="en" word="pillage" freq="1283.34" prog="0">

<a class="word dynamictext" href="/dictionary/pillage">pillage</a>
<div class="definition">steal goods; take as spoils</div>
<div class="example">In addition great material losses were inflicted: seven hundred houses were destroyed, six hundred stores
<strong>pillaged</strong>, and thousands of families utterly ruined.
<br> —
<a href="http://www.gutenberg.org/ebooks/39144" rel="nofollow">Straus, Oscar S.</a></div>


</li>






<li class="entry learnable" id="entry363"
 lang="en" word="foreboding" freq="1284.45" prog="0">

<a class="word dynamictext" href="/dictionary/foreboding">foreboding</a>
<div class="definition">a feeling of evil to come</div>
<div class="example">Mr. Harding had strong
<strong>forebodings</strong> that the trouble, so far from being ended, was only just beginning.
<br> —
<a href="http://www.gutenberg.org/ebooks/37966" rel="nofollow">Marsh, Richard</a></div>


</li>






<li class="entry learnable" id="entry364"
 lang="en" word="rend" freq="1284.59" prog="0">

<a class="word dynamictext" href="/dictionary/rend">rend</a>
<div class="definition">tear or be torn violently</div>
<div class="example">In the distance heavy artillery was growling, and high explosive shells were bursting with a violence that seemed to
<strong>rend</strong> the sky.
<br> —
<a href="http://www.gutenberg.org/ebooks/33622" rel="nofollow">Tracy, Louis</a></div>


</li>






<li class="entry learnable" id="entry365"
 lang="en" word="livelihood" freq="1291.88" prog="0">

<a class="word dynamictext" href="/dictionary/livelihood">livelihood</a>
<div class="definition">the financial means whereby one lives</div>
<div class="example">With businesses shut, fields untended and fishing abandoned many have lost their
<strong>livelihoods</strong> as well as their homes, our correspondent says.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-asia-pacific-13090304" rel="nofollow">BBC (Apr 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry366"
 lang="en" word="deign" freq="1299.25" prog="0">

<a class="word dynamictext" href="/dictionary/deign">deign</a>
<div class="definition">do something that one considers to be below one's dignity</div>
<div class="example">To Mr. Gompers' courteous letter Czar Gary did not
<strong>deign</strong> to reply.
<br> —
<a href="http://www.gutenberg.org/ebooks/36032" rel="nofollow">Foster, William Z.</a></div>


</li>






<li class="entry learnable" id="entry367"
 lang="en" word="capricious" freq="1316.6" prog="0">

<a class="word dynamictext" href="/dictionary/capricious">capricious</a>
<div class="definition">determined by chance or impulse rather than by necessity</div>
<div class="example">Her admirers were
<strong>capricious</strong>, returning to her at times, and then holding aloof again; and as for suitors, they entirely disappeared.
<br> —
<a href="http://www.gutenberg.org/ebooks/35531" rel="nofollow">Schubin, Ossip</a></div>


</li>






<li class="entry learnable" id="entry368"
 lang="en" word="stupendous" freq="1318.06" prog="0">

<a class="word dynamictext" href="/dictionary/stupendous">stupendous</a>
<div class="definition">so great in size or force or extent as to elicit awe</div>
<div class="example">The fact was so
<strong>stupendous</strong> that Terry felt almost frightened over the great good fortune.
<br> —
<a href="http://www.gutenberg.org/ebooks/37943" rel="nofollow">Sabin, Edwin L. (Edwin Legrand)</a></div>


</li>






<li class="entry learnable" id="entry369"
 lang="en" word="chaff" freq="1318.5" prog="0">

<a class="word dynamictext" href="/dictionary/chaff">chaff</a>
<div class="definition">material consisting of seed coverings and pieces of stem</div>
<div class="example">The wheat, being heavy, falls, while the
<strong>chaff</strong> is blown away.
<br> —
<a href="http://www.gutenberg.org/ebooks/35915" rel="nofollow">Starr, Frederick</a></div>


</li>






<li class="entry learnable" id="entry370"
 lang="en" word="innate" freq="1325.44" prog="0">

<a class="word dynamictext" href="/dictionary/innate">innate</a>
<div class="definition">not established by conditioning or learning</div>
<div class="example">In other words, one of our most essential abilities as humans--reading--is the product of a combination of
<strong>innate</strong> and learned traits.
<br> —
<a href="http://feedproxy.google.com/~r/time/columnists/~3/pJ8iTouUzkE/0,9171,2101856,00.html" rel="nofollow">Time (Dec 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry371"
 lang="en" word="reverie" freq="1330.81" prog="0">

<a class="word dynamictext" href="/dictionary/reverie">reverie</a>
<div class="definition">an abstracted state of absorption</div>
<div class="example">He stood still, seemingly lost in
<strong>reverie</strong>, and quite oblivious to the group about him.
<br> —
<a href="http://www.gutenberg.org/ebooks/38983" rel="nofollow">Frey, Hildegard G. (Hildegard Gertrude)</a></div>


</li>






<li class="entry learnable" id="entry372"
 lang="en" word="wrangle" freq="1334.86" prog="0">

<a class="word dynamictext" href="/dictionary/wrangle">wrangle</a>
<div class="definition">quarrel noisily, angrily, or disruptively</div>
<div class="example">Here were many fierce and bitter
<strong>wrangles</strong> over vexed questions, turbulent scenes, displays of sectional feelings.
<br> —
<a href="http://www.gutenberg.org/ebooks/32556" rel="nofollow">Raymond, Evelyn</a></div>


</li>






<li class="entry learnable" id="entry373"
 lang="en" word="crevice" freq="1349.01" prog="0">

<a class="word dynamictext" href="/dictionary/crevice">crevice</a>
<div class="definition">a long narrow opening</div>
<div class="example">The disruptive power of tree roots, growing in the
<strong>crevices</strong> of rocks, is well known.
<br> —
<a href="http://www.gutenberg.org/ebooks/38482" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry374"
 lang="en" word="ostensible" freq="1349.62" prog="0">

<a class="word dynamictext" href="/dictionary/ostensible">ostensible</a>
<div class="definition">appearing as such but not necessarily so</div>
<div class="example">This already-exhaustive book is studded with diary entries, academic papers and other
<strong>ostensible</strong> evidence that its fictitious stories of destruction are true.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=595541f743c645c578e4fadd95ea2bea" rel="nofollow">New York Times (Jun 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry375"
 lang="en" word="craven" freq="1366.6" prog="0">

<a class="word dynamictext" href="/dictionary/craven">craven</a>
<div class="definition">lacking even the rudiments of courage; abjectly fearful</div>
<div class="example">Was it for them to follow the
<strong>craven</strong> footsteps of a cowardly generation?
<br> —
<a href="http://www.gutenberg.org/ebooks/34745" rel="nofollow">Robinson, Victor</a></div>


</li>






<li class="entry learnable" id="entry376"
 lang="en" word="vestige" freq="1369.29" prog="0">

<a class="word dynamictext" href="/dictionary/vestige">vestige</a>
<div class="definition">an indication that something has been present</div>
<div class="example">Now, there was no
<strong>vestige</strong> of vegetation; no living thing.
<br> —
<a href="http://www.gutenberg.org/ebooks/37118" rel="nofollow">Hopkins, William John</a></div>


</li>






<li class="entry learnable" id="entry377"
 lang="en" word="plumb" freq="1369.61" prog="0">

<a class="word dynamictext" href="/dictionary/plumb">plumb</a>
<div class="definition">examine thoroughly and in great depth</div>
<div class="example">Tellingly, Ms. Liao said she had great difficulty finding three actors willing to
<strong>plumb</strong> their own personalities.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=49734015153533da2fa0121e6907ede2" rel="nofollow">New York Times (Jun 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry378"
 lang="en" word="reticent" freq="1374.54" prog="0">

<a class="word dynamictext" href="/dictionary/reticent">reticent</a>
<div class="definition">temperamentally disinclined to talk</div>
<div class="example">No questions were asked, and few indeed were the words spoken, his
<strong>reticent</strong> manner preventing any undue familiarity.
<br> —
<a href="http://www.gutenberg.org/ebooks/36578" rel="nofollow">Maclean, John</a></div>


</li>






<li class="entry learnable" id="entry379"
 lang="en" word="propensity" freq="1375.98" prog="0">

<a class="word dynamictext" href="/dictionary/propensity">propensity</a>
<div class="definition">an inclination to do something</div>
<div class="example">A longtime colleague, Gate Theatre director Michael Colgan, noted Kelly's old-school charms, punctuated by his
<strong>propensity</strong> for bow ties and smart suits.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2017508687_apeuirelandobitkelly.html?syndication=rss" rel="nofollow">Seattle Times (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry380"
 lang="en" word="chide" freq="1379.67" prog="0">

<a class="word dynamictext" href="/dictionary/chide">chide</a>
<div class="definition">censure severely or angrily</div>
<div class="example">He
<strong>chided</strong> reporters as having “stalked” family members, demanding that his relatives be left alone.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c431945464805fe25171564c3d2b007a" rel="nofollow">New York Times (Nov 8, 2011)</a></div>


</li>






<li class="entry learnable" id="entry381"
 lang="en" word="espouse" freq="1387.1" prog="0">

<a class="word dynamictext" href="/dictionary/espouse">espouse</a>
<div class="definition">choose and follow</div>
<div class="example">He said Islam should not be equated with terrorism or the kind of violence
<strong>espoused</strong> by Bin Laden.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/worldNews/~3/hKhwxA1THFI/us-binladen-brotherhood-idUSTRE7411V920110502" rel="nofollow">Reuters (May 2, 2011)</a></div>


</li>






<li class="entry learnable" id="entry382"
 lang="en" word="raiment" freq="1387.92" prog="0">

<a class="word dynamictext" href="/dictionary/raiment">raiment</a>
<div class="definition">especially fine or decorative clothing</div>
<div class="example">Clothed in fine
<strong>raiment</strong> and faring sumptuously every day, he soon developed into a handsome lad.
<br> —
<a href="http://www.gutenberg.org/ebooks/33753" rel="nofollow">Oxley, J. Macdonald (James Macdonald)</a></div>


</li>






<li class="entry learnable" id="entry383"
 lang="en" word="intrepid" freq="1387.92" prog="0">

<a class="word dynamictext" href="/dictionary/intrepid">intrepid</a>
<div class="definition">invulnerable to fear or intimidation</div>
<div class="example">There are some very courageous and
<strong>intrepid</strong> reporters in Afghanistan, including some who work for American media outlets.
<br> —
<a href="http://www.salon.com/opinion/greenwald/2010/04/05/afghanistan/index.html" rel="nofollow">Salon (Apr 5, 2010)</a></div>


</li>






<li class="entry learnable" id="entry384"
 lang="en" word="seemly" freq="1403.05" prog="0">

<a class="word dynamictext" href="/dictionary/seemly">seemly</a>
<div class="definition">according with custom or propriety</div>
<div class="example">The Baron was less conscientious, for he ate more beefsteak than was
<strong>seemly</strong>, and talked a great deal of stupid nonsense, as was his wont.
<br> —
<a href="http://www.gutenberg.org/ebooks/31668" rel="nofollow">Hoffmann, Ernst Theordor Wilhelm</a></div>


</li>






<li class="entry learnable" id="entry385"
 lang="en" word="allay" freq="1403.89" prog="0">

<a class="word dynamictext" href="/dictionary/allay">allay</a>
<div class="definition">lessen the intensity of or calm</div>
<div class="example">Our boy was scared and confused; we tried to
<strong>allay</strong> his fears.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=879ac49b57539333110b91359e9ca6e1" rel="nofollow">New York Times (Mar 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry386"
 lang="en" word="fitful" freq="1409.07" prog="0">

<a class="word dynamictext" href="/dictionary/fitful">fitful</a>
<div class="definition">occurring in spells and often abruptly</div>
<div class="example">She had lost her composure, her breath came in
<strong>fitful</strong>, uneven gasps, and as she sat there she pressed one hand over her heart.
<br> —
<a href="http://www.gutenberg.org/ebooks/34724" rel="nofollow">Davis, Owen</a></div>


</li>






<li class="entry learnable" id="entry387"
 lang="en" word="erode" freq="1420.57" prog="0">

<a class="word dynamictext" href="/dictionary/erode">erode</a>
<div class="definition">become ground down or deteriorate</div>
<div class="example">Another report today showed home prices fell more than forecast in November,
<strong>eroding</strong> the wealth of families as they seek to rebuild savings.
<br> —
<a href="http://www.businessweek.com/news/2012-01-31/confidence-decline-points-to-cooling-u-s-growth-economy.html" rel="nofollow">BusinessWeek (Jan 31, 2012)</a></div>


</li>






<li class="entry learnable" id="entry388"
 lang="en" word="unaffected" freq="1426.73" prog="0">

<a class="word dynamictext" href="/dictionary/unaffected">unaffected</a>
<div class="definition">free of artificiality; sincere and genuine</div>
<div class="example">His conversation was
<strong>unaffectedly</strong> simple and frank; his language natural; always abounding in curious anecdotes.
<br> —
<a href="http://www.gutenberg.org/ebooks/37702" rel="nofollow">Conway, Moncure Daniel</a></div>


</li>






<li class="entry learnable" id="entry389"
 lang="en" word="canto" freq="1437.3" prog="0">

<a class="word dynamictext" href="/dictionary/canto">canto</a>
<div class="definition">a major division of a long poem</div>
<div class="example">Folengo’s next production was the Orlandino, an Italian poem of eight
<strong>cantos</strong>, written in rhymed octaves.
<br> —
<a href="http://www.gutenberg.org/ebooks/35747" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry390"
 lang="en" word="docile" freq="1452.29" prog="0">

<a class="word dynamictext" href="/dictionary/docile">docile</a>
<div class="definition">easily handled or managed</div>
<div class="example">Time and again humans have domesticated wild , producing tame individuals with softer appearances and more
<strong>docile</strong> temperaments, such as dogs and guinea pigs.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=17c7ccd39297086c3f295e98fd8066fc" rel="nofollow">Scientific American (Jan 25, 2012)</a></div>


</li>






<li class="entry learnable" id="entry391"
 lang="en" word="patronize" freq="1453" prog="0">

<a class="word dynamictext" href="/dictionary/patronize">patronize</a>
<div class="definition">treat condescendingly</div>
<div class="example">Ms. Paul herself noted that “glib talk about appreciating dyslexia as a ‘gift’ is unhelpful at best and
<strong>patronizing</strong> at worst.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=bfb609e813b72f1f4f72952de4d43458" rel="nofollow">New York Times (Feb 6, 2012)</a></div>


</li>






<li class="entry learnable" id="entry392"
 lang="en" word="teem" freq="1456.58" prog="0">

<a class="word dynamictext" href="/dictionary/teem">teem</a>
<div class="definition">be abuzz</div>
<div class="example">The coast, once
<strong>teeming</strong> with traffic, is now lonely and deserted.
<br> —
<a href="http://www.gutenberg.org/ebooks/35298" rel="nofollow">Mahaffy, J. P.</a></div>


</li>






<li class="entry learnable" id="entry393"
 lang="en" word="estrange" freq="1463.6" prog="0">

<a class="word dynamictext" href="/dictionary/estrange">estrange</a>
<div class="definition">arouse hostility or indifference in</div>
<div class="example">An atmosphere of distrust, suspicion and fear can cause workers to feel
<strong>estranged</strong> from one another, Dr. Wright has written.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c529b1797671589aa67a53876fd706bf" rel="nofollow">New York Times (Jan 28, 2012)</a></div>


</li>






<li class="entry learnable" id="entry394"
 lang="en" word="spat" freq="1465.05" prog="0">

<a class="word dynamictext" href="/dictionary/spat">spat</a>
<div class="definition">a quarrel about petty points</div>
<div class="example">Public
<strong>spats</strong> are rare in the asset-management industry, where companies typically resolve disputes behind closed doors.
<br> —
<a href="http://www.businessweek.com/news/2011-09-16/cutting-gundlach-cancer-at-tcw-followed-decade-of-tensions.html" rel="nofollow">BusinessWeek (Sep 16, 2011)</a></div>


</li>






<li class="entry learnable" id="entry395"
 lang="en" word="warble" freq="1466.69" prog="0">

<a class="word dynamictext" href="/dictionary/warble">warble</a>
<div class="definition">sing or play with trills</div>
<div class="example">Meadow larks, as you have undoubtedly noticed,
<strong>warble</strong> many different songs.
<br> —
<a href="http://www.gutenberg.org/ebooks/36785" rel="nofollow">Barrett, R. E.</a></div>


</li>






<li class="entry learnable" id="entry396"
 lang="en" word="mien" freq="1471.43" prog="0">

<a class="word dynamictext" href="/dictionary/mien">mien</a>
<div class="definition">a person's appearance, manner, or demeanor</div>
<div class="example">Nevertheless, before going to meet Samuel, she assumed a calm and dignified
<strong>mien</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/37621" rel="nofollow">Kraszewski, Jo?zef Ignacy</a></div>


</li>






<li class="entry learnable" id="entry397"
 lang="en" word="sate" freq="1490.7" prog="0">

<a class="word dynamictext" href="/dictionary/sate">sate</a>
<div class="definition">fill to contentment</div>
<div class="example">His appetite was not
<strong>sated</strong> by any means, but he knew the danger of overloading his stomach, so he stopped.
<br> —
<a href="http://www.gutenberg.org/ebooks/27128" rel="nofollow">Dewey, Edward Hooker</a></div>


</li>






<li class="entry learnable" id="entry398"
 lang="en" word="constituency" freq="1492.21" prog="0">

<a class="word dynamictext" href="/dictionary/constituency">constituency</a>
<div class="definition">the body of voters who elect a representative for their area</div>
<div class="example">Each posited that the blue-collar Democratic
<strong>constituency</strong> rooted in the New Deal had grown increasingly conservative, alienated from “big government.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=fe22a21b5428e586621c232dcf0d7ce9" rel="nofollow">New York Times (Jan 14, 2012)</a></div>


</li>






<li class="entry learnable" id="entry399"
 lang="en" word="patrician" freq="1492.21" prog="0">

<a class="word dynamictext" href="/dictionary/patrician">patrician</a>
<div class="definition">characteristic of the nobility or aristocracy</div>
<div class="example">Respectable ladies, long resident, wearing black poke bonnets and camel's-hair shawls, lifted their
<strong>patrician</strong> eyebrows with disapproval.
<br> —
<a href="http://www.gutenberg.org/ebooks/37105" rel="nofollow">Brooks, Charles Stephen</a></div>


</li>






<li class="entry learnable" id="entry400"
 lang="en" word="parry" freq="1495.79" prog="0">

<a class="word dynamictext" href="/dictionary/parry">parry</a>
<div class="definition">avoid or try to avoid fulfilling, answering, or performing</div>
<div class="example">The boys asked a few guarded questions, but gained no information whatever, their questions being
<strong>parried</strong> in every instance.
<br> —
<a href="http://www.gutenberg.org/ebooks/38994" rel="nofollow">Mears, James R.</a></div>


</li>






<li class="entry learnable" id="entry401"
 lang="en" word="practitioner" freq="1497.68" prog="0">

<a class="word dynamictext" href="/dictionary/practitioner">practitioner</a>
<div class="definition">someone who carries out a learned profession</div>
<div class="example">In particular, modern medical
<strong>practitioners</strong> are coming around to the idea that certain illnesses cannot be reduced to one isolatable, treatable cause.
<br> —
<a href="http://feeds.nature.com/~r/nature/rss/current/~3/TqitxKlcKRg/480S81a" rel="nofollow">Nature (Dec 21, 2011)</a></div>


</li>






<li class="entry learnable" id="entry402"
 lang="en" word="ravel" freq="1501.1" prog="0">

<a class="word dynamictext" href="/dictionary/ravel">ravel</a>
<div class="definition">disentangle</div>
<div class="example">Overcasting is done by taking loose stitches over the raw edge of the cloth, to keep it from
<strong>ravelling</strong> or fraying.
<br> —
<a href="http://www.gutenberg.org/ebooks/20557" rel="nofollow">Ontario. Ministry of Education</a></div>


</li>






<li class="entry learnable" id="entry403"
 lang="en" word="infest" freq="1504.35" prog="0">

<a class="word dynamictext" href="/dictionary/infest">infest</a>
<div class="definition">occupy in large numbers or live on a host</div>
<div class="example">Many lived in dilapidated apartments with leaky pipes, broken windows, rooms full of mold, and walls
<strong>infested</strong> with cockroaches and rats.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=75490d86a1b5b181df156ef5bed34205" rel="nofollow">New York Times (Jul 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry404"
 lang="en" word="actuate" freq="1512.42" prog="0">

<a class="word dynamictext" href="/dictionary/actuate">actuate</a>
<div class="definition">give an incentive for doing something</div>
<div class="example">He knew that men were
<strong>actuated</strong> by other motives, good and bad, than self-interest.
<br> —
<a href="http://www.gutenberg.org/ebooks/34713" rel="nofollow">Blease, Walter Lyon</a></div>


</li>






<li class="entry learnable" id="entry405"
 lang="en" word="surly" freq="1518.83" prog="0">

<a class="word dynamictext" href="/dictionary/surly">surly</a>
<div class="definition">unfriendly and inclined toward anger or irritation</div>
<div class="example">But Blake, being
<strong>surly</strong> and quarrelsome even when sober, gave the lapel a savage jerk, and reached out with his other hand.
<br> —
<a href="http://www.gutenberg.org/ebooks/33612" rel="nofollow">Chisholm, A. M. (Arthur Murray)</a></div>


</li>






<li class="entry learnable" id="entry406"
 lang="en" word="convalesce" freq="1519.22" prog="0">

<a class="word dynamictext" href="/dictionary/convalesce">convalesce</a>
<div class="definition">get over an illness or shock</div>
<div class="example">Patients
<strong>convalescing</strong> from pneumonia were evacuated to England or given Base Duty.
<br> —
<a href="http://www.gutenberg.org/ebooks/22523" rel="nofollow">Jahns, Lewis E.</a></div>


</li>






<li class="entry learnable" id="entry407"
 lang="en" word="demoralize" freq="1521.36" prog="0">

<a class="word dynamictext" href="/dictionary/demoralize">demoralize</a>
<div class="definition">lower someone's spirits; make downhearted</div>
<div class="example">The storm clobbered many communities still recovering from the flooding two months ago caused by Hurricane Irene, leaving weary homeowners exhausted and
<strong>demoralized</strong>.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=2f958b9a6532945242c5a42ecf4ebead" rel="nofollow">Washington Post (Nov 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry408"
 lang="en" word="devolve" freq="1531.21" prog="0">

<a class="word dynamictext" href="/dictionary/devolve">devolve</a>
<div class="definition">grow worse</div>
<div class="example">As the rhetoric heated up inside, the violence outside
<strong>devolved</strong> into chaos.
<br> —
<a href="http://feedproxy.google.com/~r/time/world/~3/dt5tzD2keNs/0,8599,2106692,00.html" rel="nofollow">Time (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry409"
 lang="en" word="alacrity" freq="1532" prog="0">

<a class="word dynamictext" href="/dictionary/alacrity">alacrity</a>
<div class="definition">liveliness and eagerness</div>
<div class="example">Every one exerted himself not only without murmuring and discontent, but even with an
<strong>alacrity</strong> which almost approached to cheerfulness.
<br> —
<a href="http://www.gutenberg.org/ebooks/7777" rel="nofollow">Kippis, Andrew</a></div>


</li>






<li class="entry learnable" id="entry410"
 lang="en" word="waive" freq="1539.17" prog="0">

<a class="word dynamictext" href="/dictionary/waive">waive</a>
<div class="definition">do without or cease to hold or adhere to</div>
<div class="example">Low rates have also led retail brokerages to
<strong>waive</strong> fees on money market funds to avoid negative returns for their clients.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/businessNews/~3/8EnT_dth0Kk/us-discountbrokers-idUSTRE80C2CP20120113" rel="nofollow">Reuters (Jan 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry411"
 lang="en" word="unwonted" freq="1543.59" prog="0">

<a class="word dynamictext" href="/dictionary/unwonted">unwonted</a>
<div class="definition">out of the ordinary</div>
<div class="example">He must rush off to see his people, who no doubt were quite confounded by his
<strong>unwonted</strong> energy.
<br> —
<a href="http://www.gutenberg.org/ebooks/36671" rel="nofollow">Speed, Nell</a></div>


</li>






<li class="entry learnable" id="entry412"
 lang="en" word="seethe" freq="1543.79" prog="0">

<a class="word dynamictext" href="/dictionary/seethe">seethe</a>
<div class="definition">be in an agitated emotional state</div>
<div class="example">Outwardly quite calm and matter-of-fact, his mind was in a
<strong>seething</strong> turmoil.
<br> —
<a href="http://www.gutenberg.org/ebooks/39066" rel="nofollow">Douglas, Hudson</a></div>


</li>






<li class="entry learnable" id="entry413"
 lang="en" word="scrutinize" freq="1557.4" prog="0">

<a class="word dynamictext" href="/dictionary/scrutinize">scrutinize</a>
<div class="definition">look at critically or searchingly, or in minute detail</div>
<div class="example">Fans and commentators are
<strong>scrutinizing</strong> every blemish: his turnovers, his weak left hand, his jump shot.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/vqWkNWm_CLc/star-turn-leaves-the-knicks-lin-to-learn-in-the-spotlight.html" rel="nofollow">New York Times (Mar 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry414"
 lang="en" word="diffident" freq="1563.78" prog="0">

<a class="word dynamictext" href="/dictionary/diffident">diffident</a>
<div class="definition">lacking self-confidence</div>
<div class="example">Shyly
<strong>diffident</strong> in the presence of strangers, her head was lowered.
<br> —
<a href="http://www.gutenberg.org/ebooks/34034" rel="nofollow">Packard, Frank L. (Frank Lucius)</a></div>


</li>






<li class="entry learnable" id="entry415"
 lang="en" word="execrate" freq="1566.68" prog="0">

<a class="word dynamictext" href="/dictionary/execrate">execrate</a>
<div class="definition">curse or declare to be evil or anathema</div>
<div class="example">When all Great Britain was
<strong>execrating</strong> Napoleon, picturing him as a devil with horns and hoofs, Byron looked upon him as the world's hero.
<br> —
<a href="http://www.gutenberg.org/ebooks/13619" rel="nofollow">Hubbard, Elbert</a></div>


</li>






<li class="entry learnable" id="entry416"
 lang="en" word="implacable" freq="1576.7" prog="0">

<a class="word dynamictext" href="/dictionary/implacable">implacable</a>
<div class="definition">incapable of being appeased or pacified</div>
<div class="example">This man was a savage in his
<strong>implacable</strong> desire for revenge.
<br> —
<a href="http://www.gutenberg.org/ebooks/34996" rel="nofollow">Kelly, Florence Finch</a></div>


</li>






<li class="entry learnable" id="entry417"
 lang="en" word="pique" freq="1591.54" prog="0">

<a class="word dynamictext" href="/dictionary/pique">pique</a>
<div class="definition">a sudden outburst of anger</div>
<div class="example">A talented youngster who smashes his guitar in a fit of
<strong>pique</strong> finds it magically reassembled just in time for a crucial concert.
<br> —
<a href="http://www.guardian.co.uk/film/filmblog/2010/may/31/tooth-fairy-the-rock" rel="nofollow">The Guardian (May 31, 2010)</a></div>


</li>






<li class="entry learnable" id="entry418"
 lang="en" word="mite" freq="1599.5" prog="0">

<a class="word dynamictext" href="/dictionary/mite">mite</a>
<div class="definition">a slight but appreciable amount</div>
<div class="example">I never saw anybody so pleased with monkeys as she is, and not one
<strong>mite</strong> afraid.
<br> —
<a href="http://www.gutenberg.org/ebooks/32606" rel="nofollow">Raymond, Evelyn</a></div>


</li>






<li class="entry learnable" id="entry419"
 lang="en" word="encumber" freq="1607.32" prog="0">

<a class="word dynamictext" href="/dictionary/encumber">encumber</a>
<div class="definition">hold back</div>
<div class="example">Two others were making slower progress for the reason that each was
<strong>encumbered</strong> by supporting a disabled man.
<br> —
<a href="http://www.gutenberg.org/ebooks/37824" rel="nofollow">Westerman, Percy F. (Percy Francis)</a></div>


</li>






<li class="entry learnable" id="entry420"
 lang="en" word="uncouth" freq="1612.58" prog="0">

<a class="word dynamictext" href="/dictionary/uncouth">uncouth</a>
<div class="definition">lacking refinement or cultivation or taste</div>
<div class="example">He had not stopped to consider her rough speech and
<strong>uncouth</strong> manners.
<br> —
<a href="http://www.gutenberg.org/ebooks/39090" rel="nofollow">Johnston, Annie F. (Annie Fellows)</a></div>


</li>






<li class="entry learnable" id="entry421"
 lang="en" word="petulant" freq="1613.24" prog="0">

<a class="word dynamictext" href="/dictionary/petulant">petulant</a>
<div class="definition">easily irritated or annoyed</div>
<div class="example">The black eyes emitted an angry flash, the voice that answered was sharp and
<strong>petulant</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/33664" rel="nofollow">Fleming, May Agnes</a></div>


</li>






<li class="entry learnable" id="entry422"
 lang="en" word="expiate" freq="1633.95" prog="0">

<a class="word dynamictext" href="/dictionary/expiate">expiate</a>
<div class="definition">make amends for</div>
<div class="example">Wulphere was absolved on condition that he should
<strong>expiate</strong> his crime by founding churches and monasteries all over his kingdom.
<br> —
<a href="http://www.gutenberg.org/ebooks/37049" rel="nofollow">Clifton, A. B.</a></div>


</li>






<li class="entry learnable" id="entry423"
 lang="en" word="cavalier" freq="1648.06" prog="0">

<a class="word dynamictext" href="/dictionary/cavalier">cavalier</a>
<div class="definition">given to haughty disregard of others</div>
<div class="example">Some would have given Nicklaus a
<strong>cavalier</strong> response: polite nod while thinking, “Yeah, whatever.”
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/7EpcNCR7XTc/us-open-2011-rory-mcilroy-third-round.html" rel="nofollow">New York Times (Jun 18, 2011)</a></div>


</li>






<li class="entry learnable" id="entry424"
 lang="en" word="banter" freq="1652.9" prog="0">

<a class="word dynamictext" href="/dictionary/banter">banter</a>
<div class="definition">light teasing repartee</div>
<div class="example">Our easy
<strong>banter</strong> had suddenly been replaced by strained and awkward interaction.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/V-ojZfQ9tZo/click.phdo" rel="nofollow">Slate (Feb 15, 2012)</a></div>


</li>






<li class="entry learnable" id="entry425"
 lang="en" word="bluster" freq="1652.9" prog="0">

<a class="word dynamictext" href="/dictionary/bluster">bluster</a>
<div class="definition">act in an arrogant, overly self-assured, or conceited manner</div>
<div class="example">Slade, despite his swaggers and
<strong>blustering</strong>, was at heart a coward.
<br> —
<a href="http://www.gutenberg.org/ebooks/37913" rel="nofollow">Landon, Herman</a></div>


</li>






<li class="entry learnable" id="entry426"
 lang="en" word="debase" freq="1656.83" prog="0">

<a class="word dynamictext" href="/dictionary/debase">debase</a>
<div class="definition">corrupt morally or by intemperance or sensuality</div>
<div class="example">Long oppression had not, on the whole, either blunted their intellects or
<strong>debased</strong> their morals.
<br> —
<a href="http://www.gutenberg.org/ebooks/37697" rel="nofollow">Adler, Felix</a></div>


</li>






<li class="entry learnable" id="entry427"
 lang="en" word="retainer" freq="1656.83" prog="0">

<a class="word dynamictext" href="/dictionary/retainer">retainer</a>
<div class="definition">a person working in the service of another</div>
<div class="example">This faithful and trusted
<strong>retainer</strong> is greatly valued by his employers.
<br> —
<a href="http://www.gutenberg.org/ebooks/38596" rel="nofollow">Black, Helen C.</a></div>


</li>






<li class="entry learnable" id="entry428"
 lang="en" word="subjugate" freq="1676.07" prog="0">

<a class="word dynamictext" href="/dictionary/subjugate">subjugate</a>
<div class="definition">make subservient; force to submit or subdue</div>
<div class="example">The Confederacy was led by thoroughgoing racists who wanted to keep blacks
<strong>subjugated</strong> for all time because of the color of their skin.
<br> —
<a href="http://feeds.slate.com/click.phdo?i=33beff1fa74a6af8ed9547dbabfb57e4" rel="nofollow">Slate (Apr 7, 2010)</a></div>


</li>






<li class="entry learnable" id="entry429"
 lang="en" word="extol" freq="1676.31" prog="0">

<a class="word dynamictext" href="/dictionary/extol">extol</a>
<div class="definition">praise, glorify, or honor</div>
<div class="example">How I praised the duck at that first dinner, and
<strong>extolled</strong> Madame's skill in cookery!
<br> —
<a href="http://www.gutenberg.org/ebooks/34812" rel="nofollow">Warren, Arthur</a></div>


</li>






<li class="entry learnable" id="entry430"
 lang="en" word="fraught" freq="1679.64" prog="0">

<a class="word dynamictext" href="/dictionary/fraught">fraught</a>
<div class="definition">filled with or attended with</div>
<div class="example">But the ocean remains an unpredictable place,
<strong>fraught</strong> with hazards.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=8d159a8b190b1cf5855f37e2e0a84966" rel="nofollow">Scientific American (Apr 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry431"
 lang="en" word="august" freq="1688.51" prog="0">

<a class="word dynamictext" href="/dictionary/august">august</a>
<div class="definition">profoundly honored</div>
<div class="example">At all times reserved in his manner and his bearing full of dignity, never before had she realized the majesty of General Washington’s
<strong>august</strong> presence.
<br> —
<a href="http://www.gutenberg.org/ebooks/36740" rel="nofollow">Madison, Lucy Foster</a></div>


</li>






<li class="entry learnable" id="entry432"
 lang="en" word="fissure" freq="1689.71" prog="0">

<a class="word dynamictext" href="/dictionary/fissure">fissure</a>
<div class="definition">a long narrow depression in a surface</div>
<div class="example">The brown bark is not very rough, though its numerous
<strong>fissures</strong> and cracks give it a rugged appearance.
<br> —
<a href="http://www.gutenberg.org/ebooks/34740" rel="nofollow">Step, Edward</a></div>


</li>






<li class="entry learnable" id="entry433"
 lang="en" word="knoll" freq="1712.95" prog="0">

<a class="word dynamictext" href="/dictionary/knoll">knoll</a>
<div class="definition">a small natural hill</div>
<div class="example">Opened in 2008, the park serves as a true public space; elderly couples stroll around the artificial lake as toddlers roll down grassy
<strong>knolls</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6cf480b42bac07cb4a03bd02e15588de" rel="nofollow">New York Times (May 7, 2010)</a></div>


</li>






<li class="entry learnable" id="entry434"
 lang="en" word="callous" freq="1717.43" prog="0">

<a class="word dynamictext" href="/dictionary/callous">callous</a>
<div class="definition">emotionally hardened</div>
<div class="example">Outwardly merry and good-humoured, he was by nature coldly fierce, calculating,
<strong>callous</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38863" rel="nofollow">Wingfield, Lewis</a></div>


</li>






<li class="entry learnable" id="entry435"
 lang="en" word="inculcate" freq="1718.17" prog="0">

<a class="word dynamictext" href="/dictionary/inculcate">inculcate</a>
<div class="definition">teach and impress by frequent repetitions or admonitions</div>
<div class="example">But instruction in history has been for a long time systematically used to
<strong>inculcate</strong> certain political sentiments in the pupils.
<br> —
<a href="http://www.gutenberg.org/ebooks/39023" rel="nofollow">Liebknecht, Karl Paul August Friedrich</a></div>


</li>






<li class="entry learnable" id="entry436"
 lang="en" word="nettle" freq="1725.94" prog="0">

<a class="word dynamictext" href="/dictionary/nettle">nettle</a>
<div class="definition">disturb, especially by minor irritations</div>
<div class="example">Lincoln began these remarks by good-humored but
<strong>nettling</strong> chaffing of his opponent.
<br> —
<a href="http://www.gutenberg.org/ebooks/14319" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry437"
 lang="en" word="blanch" freq="1727.45" prog="0">

<a class="word dynamictext" href="/dictionary/blanch">blanch</a>
<div class="definition">turn pale, as if in fear</div>
<div class="example">He is silent, as if struck dumb, his face showing
<strong>blanched</strong> and bloodless, while she utters a shriek, half terrified, half in frenzied anger.
<br> —
<a href="http://www.gutenberg.org/ebooks/35784" rel="nofollow">Reid, Mayne</a></div>


</li>






<li class="entry learnable" id="entry438"
 lang="en" word="inscrutable" freq="1732.01" prog="0">

<a class="word dynamictext" href="/dictionary/inscrutable">inscrutable</a>
<div class="definition">of an obscure nature</div>
<div class="example">The fashion industry is notoriously opaque and often
<strong>inscrutable</strong> for outsiders, even ones as well connected as him.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2016379017_apeufrancefashionkanyewest.html?syndication=rss" rel="nofollow">Seattle Times (Oct 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry439"
 lang="en" word="tenacious" freq="1741.95" prog="0">

<a class="word dynamictext" href="/dictionary/tenacious">tenacious</a>
<div class="definition">stubbornly unyielding</div>
<div class="example">She was a
<strong>tenacious</strong> woman, one who would even hold fast a thing which she no longer valued, simply because it belonged to her.
<br> —
<a href="http://www.gutenberg.org/ebooks/35055" rel="nofollow">Morris, Clara</a></div>


</li>






<li class="entry learnable" id="entry440"
 lang="en" word="thrall" freq="1744" prog="0">

<a class="word dynamictext" href="/dictionary/thrall">thrall</a>
<div class="definition">the state of being under the control of another person</div>
<div class="example">Then Kiss commenced in earnest, and quickly held his audience in
<strong>thrall</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/39111" rel="nofollow">Farjeon, Benjamin Leopold</a></div>


</li>






<li class="entry learnable" id="entry441"
 lang="en" word="exigency" freq="1756.17" prog="0">

<a class="word dynamictext" href="/dictionary/exigency">exigency</a>
<div class="definition">a pressing or urgent situation</div>
<div class="example">The
<strong>exigency</strong> of the situation roused Mr. Popkiss' sluggish faculties into prompt action.
<br> —
<a href="http://www.gutenberg.org/ebooks/34088" rel="nofollow">Magnay, William</a></div>


</li>






<li class="entry learnable" id="entry442"
 lang="en" word="disconsolate" freq="1775.94" prog="0">

<a class="word dynamictext" href="/dictionary/disconsolate">disconsolate</a>
<div class="definition">sad beyond comforting; incapable of being consoled</div>
<div class="example">Was there a bereaved mother or
<strong>disconsolate</strong> sister weeping over their dead?
<br> —
<a href="http://www.gutenberg.org/ebooks/38383" rel="nofollow">Steward, T. G. (Theophilus Gould)</a></div>


</li>






<li class="entry learnable" id="entry443"
 lang="en" word="impetus" freq="1779.41" prog="0">

<a class="word dynamictext" href="/dictionary/impetus">impetus</a>
<div class="definition">a force that makes something happen</div>
<div class="example">Critics say it has known mixed success at best, although supporters hope the U.S. drawdown could provide just the
<strong>impetus</strong> it needs to thrive.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/topNews/~3/XFkfS7-dMAE/us-europe-defence-idUSTRE8091MH20120110" rel="nofollow">Reuters (Jan 10, 2012)</a></div>


</li>






<li class="entry learnable" id="entry444"
 lang="en" word="imposition" freq="1784.78" prog="0">

<a class="word dynamictext" href="/dictionary/imposition">imposition</a>
<div class="definition">an uncalled-for burden</div>
<div class="example">On that far-away day he had considered the little, lost girl a nuisance and an
<strong>imposition</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/33612" rel="nofollow">Chisholm, A. M. (Arthur Murray)</a></div>


</li>






<li class="entry learnable" id="entry445"
 lang="en" word="auspices" freq="1787.2" prog="0">

<a class="word dynamictext" href="/dictionary/auspices">auspices</a>
<div class="definition">kindly endorsement and guidance</div>
<div class="example">In March 2009, negotiations between Israel and Hamas were held in Cairo, under the
<strong>auspices</strong> of the Egyptian intelligence agency.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=ed000fcc0e80ab50771bc56203a570e4" rel="nofollow">New York Times (Nov 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry446"
 lang="en" word="sonorous" freq="1799.71" prog="0">

<a class="word dynamictext" href="/dictionary/sonorous">sonorous</a>
<div class="definition">full and loud and deep</div>
<div class="example">His voice rang out firmly now, a deep and
<strong>sonorous</strong> bass.
<br> —
<a href="http://www.gutenberg.org/ebooks/35078" rel="nofollow">Bedford-Jones, H.</a></div>


</li>






<li class="entry learnable" id="entry447"
 lang="en" word="exploitation" freq="1807.13" prog="0">

<a class="word dynamictext" href="/dictionary/exploitation">exploitation</a>
<div class="definition">an act that victimizes someone </div>
<div class="example">In a scathing report released last year, Amnesty International found there was widespread
<strong>exploitation</strong> of migrants in Malaysia.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/business-12931526" rel="nofollow">BBC (Apr 4, 2011)</a></div>


</li>






<li class="entry learnable" id="entry448"
 lang="en" word="bane" freq="1815.73" prog="0">

<a class="word dynamictext" href="/dictionary/bane">bane</a>
<div class="definition">something causing misery or death</div>
<div class="example">Knee pain is the
<strong>bane</strong> of many runners, sometimes causing them to give up altogether.
<br> —
<a href="http://seattletimes.nwsource.com/html/health/2012052211_knees08.html?syndication=rss" rel="nofollow">Seattle Times (Jun 7, 2010)</a></div>


</li>






<li class="entry learnable" id="entry449"
 lang="en" word="dint" freq="1815.73" prog="0">

<a class="word dynamictext" href="/dictionary/dint">dint</a>
<div class="definition">force or effort</div>
<div class="example">If only certain puzzles could be solved by
<strong>dint</strong> of sheer hard thinking!
<br> —
<a href="http://www.gutenberg.org/ebooks/37963" rel="nofollow">Marsh, Richard</a></div>


</li>






<li class="entry learnable" id="entry450"
 lang="en" word="ignominious" freq="1823.56" prog="0">

<a class="word dynamictext" href="/dictionary/ignominious">ignominious</a>
<div class="definition">deserving or bringing disgrace or shame</div>
<div class="example">The great Ottawa chief saw his partially accomplished scheme withering into
<strong>ignominious</strong> failure.
<br> —
<a href="http://www.gutenberg.org/ebooks/30186" rel="nofollow">Rudd, John</a></div>


</li>






<li class="entry learnable" id="entry451"
 lang="en" word="amicable" freq="1835.73" prog="0">

<a class="word dynamictext" href="/dictionary/amicable">amicable</a>
<div class="definition">characterized by friendship and good will</div>
<div class="example">After a short colloquy the two men evidently came to an
<strong>amicable</strong> understanding, for they shook hands.
<br> —
<a href="http://www.gutenberg.org/ebooks/37621" rel="nofollow">Kraszewski, Jo?zef Ignacy</a></div>


</li>






<li class="entry learnable" id="entry452"
 lang="en" word="onset" freq="1840.58" prog="0">

<a class="word dynamictext" href="/dictionary/onset">onset</a>
<div class="definition">the beginning or early stages</div>
<div class="example">Thousands of families are living in makeshift camps as temperatures fall to freezing with the
<strong>onset</strong> of winter.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=d2dd2ebd9ecb11dfe0a52f651a39c725" rel="nofollow">New York Times (Nov 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry453"
 lang="en" word="conservatory" freq="1841.15" prog="0">

<a class="word dynamictext" href="/dictionary/conservatory">conservatory</a>
<div class="definition">a schoolhouse with special facilities for fine arts</div>
<div class="example">The young instrumental talent that is coming out of local music schools and
<strong>conservatories</strong> is as amazingly good as you are going to find anywhere.
<br> —
<a href="http://feeds.chicagotribune.com/~r/chicagotribune/arts/~3/jxCOeeqMYG0/ct-live-0602-classical-20110601,0,6627122.column" rel="nofollow">Chicago Tribune (Jun 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry454"
 lang="en" word="zenith" freq="1862.31" prog="0">

<a class="word dynamictext" href="/dictionary/zenith">zenith</a>
<div class="definition">the point above the observer directly opposite the nadir</div>
<div class="example">In other words it never reaches the
<strong>zenith</strong>, a point directly overhead.
<br> —
<a href="http://www.gutenberg.org/ebooks/37894" rel="nofollow">George H. Lowery.</a></div>


</li>






<li class="entry learnable" id="entry455"
 lang="en" word="voluble" freq="1862.9" prog="0">

<a class="word dynamictext" href="/dictionary/voluble">voluble</a>
<div class="definition">marked by a ready flow of speech</div>
<div class="example">I find him charming: shy – yet easy to talk to –
<strong>voluble</strong> and funny once he gets going.
<br> —
<a href="http://www.guardian.co.uk/artanddesign/2010/aug/22/picasso-lee-miller-tony-penrose" rel="nofollow">The Guardian (Aug 21, 2010)</a></div>


</li>






<li class="entry learnable" id="entry456"
 lang="en" word="yeoman" freq="1863.78" prog="0">

<a class="word dynamictext" href="/dictionary/yeoman">yeoman</a>
<div class="definition">a free man who cultivates his own land</div>
<div class="example">On one extreme was the well-to-do
<strong>yeoman</strong> farmer farming his own land.
<br> —
<a href="http://www.gutenberg.org/ebooks/36299" rel="nofollow">Reilly, S. A.</a></div>


</li>






<li class="entry learnable" id="entry457"
 lang="en" word="levity" freq="1864.07" prog="0">

<a class="word dynamictext" href="/dictionary/levity">levity</a>
<div class="definition">a manner lacking seriousness</div>
<div class="example">The same balance of seriousness and
<strong>levity</strong> runs through her plays, which put an absurdist spin on everyday problems.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=519f010f1f1fa03eb68ed4ceb4b8b4a7" rel="nofollow">New York Times (May 7, 2010)</a></div>


</li>






<li class="entry learnable" id="entry458"
 lang="en" word="rapt" freq="1867.31" prog="0">

<a class="word dynamictext" href="/dictionary/rapt">rapt</a>
<div class="definition">feeling great delight</div>
<div class="example">She was watching the development of the investigation with
<strong>rapt</strong>, eager attention.
<br> —
<a href="http://www.gutenberg.org/ebooks/32896" rel="nofollow">Mitford, Bertram</a></div>


</li>






<li class="entry learnable" id="entry459"
 lang="en" word="sultry" freq="1876.49" prog="0">

<a class="word dynamictext" href="/dictionary/sultry">sultry</a>
<div class="definition">characterized by oppressive heat and humidity</div>
<div class="example">New guidelines from the American Academy of Pediatrics arrive just as school sports ramp up in
<strong>sultry</strong> August temperatures.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=983eeac53b048815c9d7d0403f1d5156" rel="nofollow">Washington Post (Aug 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry460"
 lang="en" word="pinion" freq="1885.46" prog="0">

<a class="word dynamictext" href="/dictionary/pinion">pinion</a>
<div class="definition">bind the arms of</div>
<div class="example">The prisoners having dismounted, were placed in a line on the ground facing the guillotine, their arms
<strong>pinioned</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38787" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry461"
 lang="en" word="axiom" freq="1886.36" prog="0">

<a class="word dynamictext" href="/dictionary/axiom">axiom</a>
<div class="definition">a proposition that is not susceptible of proof or disproof</div>
<div class="example">The fundamental
<strong>axiom</strong> of scientific thought is that there is not, never has been, and never will be, any disorder in nature.
<br> —
<a href="http://www.gutenberg.org/ebooks/34698" rel="nofollow">Huxley, Thomas H.</a></div>


</li>






<li class="entry learnable" id="entry462"
 lang="en" word="descry" freq="1898.77" prog="0">

<a class="word dynamictext" href="/dictionary/descry">descry</a>
<div class="definition">catch sight of</div>
<div class="example">Looking off seaward, I could
<strong>descry</strong> no sails.
<br> —
<a href="http://www.gutenberg.org/ebooks/38941" rel="nofollow">Drake, Samuel Adams</a></div>


</li>






<li class="entry learnable" id="entry463"
 lang="en" word="retinue" freq="1902.74" prog="0">

<a class="word dynamictext" href="/dictionary/retinue">retinue</a>
<div class="definition">the group following and attending to some important person</div>
<div class="example">Despite his
<strong>retinue</strong> of security personnel, Atambaev had been poisoned during his short tenure as prime minister.
<br> —
<a href="http://www.salon.com/news/feature/2010/04/09/guide_to_kyrgyzstan_uprising/index.html" rel="nofollow">Salon (Apr 9, 2010)</a></div>


</li>






<li class="entry learnable" id="entry464"
 lang="en" word="functionary" freq="1907.03" prog="0">

<a class="word dynamictext" href="/dictionary/functionary">functionary</a>
<div class="definition">a worker who holds or is invested with an office</div>
<div class="example">He was the
<strong>functionary</strong> of the assize court, impaneling its juries, bringing accused men before it, and carrying out its penalties.
<br> —
<a href="http://www.gutenberg.org/ebooks/36299" rel="nofollow">Reilly, S. A.</a></div>


</li>






<li class="entry learnable" id="entry465"
 lang="en" word="imbibe" freq="1915.37" prog="0">

<a class="word dynamictext" href="/dictionary/imbibe">imbibe</a>
<div class="definition">take in liquids</div>
<div class="example">"We're cornered at last," he said suddenly, as the old man set the bottle down after having
<strong>imbibed</strong> the best half of its contents.
<br> —
<a href="http://www.gutenberg.org/ebooks/39066" rel="nofollow">Douglas, Hudson</a></div>


</li>






<li class="entry learnable" id="entry466"
 lang="en" word="diversified" freq="1918.16" prog="0">

<a class="word dynamictext" href="/dictionary/diversified">diversified</a>
<div class="definition">having variety of character or form or components</div>
<div class="example">Funds in both categories tend to be highly
<strong>diversified</strong>, typically with 100 or more stocks across at least 10 industries.
<br> —
<a href="http://online.wsj.com/article/SB10001424052970204778604577243302119518244.html?mod=rss_markets_main" rel="nofollow">Wall Street Journal (Feb 24, 2012)</a></div>


</li>






<li class="entry learnable" id="entry467"
 lang="en" word="maraud" freq="1919.72" prog="0">

<a class="word dynamictext" href="/dictionary/maraud">maraud</a>
<div class="definition">raid and rove in search of booty</div>
<div class="example">Its reporter says armed gangs and looters are
<strong>marauding</strong> the streets.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/uk-13009028" rel="nofollow">BBC (Apr 8, 2011)</a></div>


</li>






<li class="entry learnable" id="entry468"
 lang="en" word="grudging" freq="1935.1" prog="0">

<a class="word dynamictext" href="/dictionary/grudging">grudging</a>
<div class="definition">petty or reluctant in giving or spending</div>
<div class="example">Expect delays, scattered outages and surly,
<strong>grudging</strong> customer service in the interim.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/qSHcw1xQqEg/" rel="nofollow">Time (Aug 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry469"
 lang="en" word="partiality" freq="1944.65" prog="0">

<a class="word dynamictext" href="/dictionary/partiality">partiality</a>
<div class="definition">a predisposition to like something</div>
<div class="example">She still showed a
<strong>partiality</strong> for bright colors, by her gown of deep crimson.
<br> —
<a href="http://www.gutenberg.org/ebooks/34846" rel="nofollow">Sage, William</a></div>


</li>






<li class="entry learnable" id="entry470"
 lang="en" word="philology" freq="1945.61" prog="0">

<a class="word dynamictext" href="/dictionary/philology">philology</a>
<div class="definition">the humanistic study of language and literature</div>
<div class="example">I had determined to study
<strong>philology</strong>, chiefly Greek and Latin, but the fare spread out by the professors was much too tempting.
<br> —
<a href="http://www.gutenberg.org/ebooks/30269" rel="nofollow">Müller, F. Max (Friedrich Max)</a></div>


</li>






<li class="entry learnable" id="entry471"
 lang="en" word="wry" freq="2005.97" prog="0">

<a class="word dynamictext" href="/dictionary/wry">wry</a>
<div class="definition">humorously sarcastic or mocking</div>
<div class="example">She also has a very understated but very
<strong>wry</strong> sense of humour; watch out for it.
<br> —
<a href="http://www.guardian.co.uk/stage/2010/oct/13/step-by-step-trisha-brown" rel="nofollow">The Guardian (Oct 13, 2010)</a></div>


</li>






<li class="entry learnable" id="entry472"
 lang="en" word="caucus" freq="2007.33" prog="0">

<a class="word dynamictext" href="/dictionary/caucus">caucus</a>
<div class="definition">meet to select a candidate or promote a policy</div>
<div class="example">Representative Ron Paul of Texas isn’t campaigning in Florida, instead focusing on Maine, which will
<strong>caucus</strong> in late February.
<br> —
<a href="http://rss.businessweek.com/~r/bw_rss/europeindex/~3/cW756DLCV6c/gingrich-says-he-needs-strong-florida-finish-to-save-campaign.html" rel="nofollow">BusinessWeek (Feb 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry473"
 lang="en" word="permeate" freq="2013.14" prog="0">

<a class="word dynamictext" href="/dictionary/permeate">permeate</a>
<div class="definition">spread or diffuse through</div>
<div class="example">Florida’s summertime heat
<strong>permeates</strong> almost every scene, becoming something like a character.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c6fa5cbe12578784feda4e3b125bdd76" rel="nofollow">New York Times (Mar 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry474"
 lang="en" word="propitious" freq="2016.57" prog="0">

<a class="word dynamictext" href="/dictionary/propitious">propitious</a>
<div class="definition">presenting favorable circumstances</div>
<div class="example">With the Athens stock market down nearly 30 percent so far this year, it would not seem a
<strong>propitious</strong> time for initial public offerings.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=48e5fcffdaf7f3814038a9ffc6678570" rel="nofollow">New York Times (Jun 2, 2010)</a></div>


</li>






<li class="entry learnable" id="entry475"
 lang="en" word="salient" freq="2023.82" prog="0">

<a class="word dynamictext" href="/dictionary/salient">salient</a>
<div class="definition">having a quality that thrusts itself into attention</div>
<div class="example">Bullying has become an increasingly
<strong>salient</strong> problem for school-age children, and in rare cases has ended tragically with victims committing suicide.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/healthNews/~3/PesfGpBe714/us-school-bullying-idUSTRE8171YA20120208" rel="nofollow">Reuters (Feb 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry476"
 lang="en" word="propitiate" freq="2029.37" prog="0">

<a class="word dynamictext" href="/dictionary/propitiate">propitiate</a>
<div class="definition">make peace with</div>
<div class="example">King Edward, having subdued the Welsh, “endeavoured to
<strong>propitiate</strong> his newly acquired subjects by becoming a resident in the conquered country.
<br> —
<a href="http://www.gutenberg.org/ebooks/36663" rel="nofollow">Frith, William Powell</a></div>


</li>






<li class="entry learnable" id="entry477"
 lang="en" word="excise" freq="2037.41" prog="0">

<a class="word dynamictext" href="/dictionary/excise">excise</a>
<div class="definition">remove by cutting</div>
<div class="example">Wielding a razor, Jefferson
<strong>excised</strong> all passages containing supernaturalistic elements from the gospels, extracting what he took to be Jesus's pure ethical teachings.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2011/apr/08/religion-ethics-bible-moral-doctrine" rel="nofollow">The Guardian (Apr 8, 2011)</a></div>


</li>






<li class="entry learnable" id="entry478"
 lang="en" word="betoken" freq="2042.33" prog="0">

<a class="word dynamictext" href="/dictionary/betoken">betoken</a>
<div class="definition">be a signal for or a symptom of</div>
<div class="example">The haggard face and sombre eyes
<strong>betokened</strong> considerable mental anguish.
<br> —
<a href="http://www.gutenberg.org/ebooks/38176" rel="nofollow">Young, F.E. Mills</a></div>


</li>






<li class="entry learnable" id="entry479"
 lang="en" word="palatable" freq="2043.04" prog="0">

<a class="word dynamictext" href="/dictionary/palatable">palatable</a>
<div class="definition">acceptable to the taste or mind</div>
<div class="example">If nicely cooked in this way, cabbage is as
<strong>palatable</strong> and as digestible as cauliflower.
<br> —
<a href="http://www.gutenberg.org/ebooks/34822" rel="nofollow">Ronald, Mary</a></div>


</li>






<li class="entry learnable" id="entry480"
 lang="en" word="upbraid" freq="2043.39" prog="0">

<a class="word dynamictext" href="/dictionary/upbraid">upbraid</a>
<div class="definition">express criticism towards</div>
<div class="example">When Kahn warned of a serious economic "depression", he was
<strong>upbraided</strong> by the White House for using such language.
<br> —
<a href="http://www.guardian.co.uk/business/2011/jan/12/alfred-kahn-obituary" rel="nofollow">The Guardian (Jan 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry481"
 lang="en" word="renegade" freq="2049.41" prog="0">

<a class="word dynamictext" href="/dictionary/renegade">renegade</a>
<div class="definition">someone who rebels and becomes an outlaw</div>
<div class="example">If he went off to another people he lost all standing among the Sioux and was thereafter treated as an outlaw and a
<strong>renegade</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/26021" rel="nofollow">Robinson, Doane</a></div>


</li>






<li class="entry learnable" id="entry482"
 lang="en" word="hoary" freq="2064.79" prog="0">

<a class="word dynamictext" href="/dictionary/hoary">hoary</a>
<div class="definition">ancient</div>
<div class="example">The device of the trapped young person saved by books is a
<strong>hoary</strong> one, but Ms. Winterson makes it seem new, and sulfurous.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=0712d31a642c45a688692a09c3cf607f" rel="nofollow">New York Times (Mar 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry483"
 lang="en" word="pedantic" freq="2101.09" prog="0">

<a class="word dynamictext" href="/dictionary/pedantic">pedantic</a>
<div class="definition">marked by a narrow focus on or display of learning</div>
<div class="example">The reader is treated to
<strong>pedantic</strong> little footnotes, and given a good deal of information which is either gratuitous or uninteresting.
<br> —
<a href="http://www.gutenberg.org/ebooks/34721" rel="nofollow">Hay, Ian</a></div>


</li>






<li class="entry learnable" id="entry484"
 lang="en" word="coy" freq="2112.72" prog="0">

<a class="word dynamictext" href="/dictionary/coy">coy</a>
<div class="definition">showing marked and often playful evasiveness or reluctance</div>
<div class="example">It was funny watching such a solid person, based in faith and education, grow a trifle
<strong>coy</strong> about the year of his birth.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/XbjdYO83FeY/12shepfriend.html" rel="nofollow">New York Times (Jul 11, 2010)</a></div>


</li>






<li class="entry learnable" id="entry485"
 lang="en" word="troth" freq="2140.24" prog="0">

<a class="word dynamictext" href="/dictionary/troth">troth</a>
<div class="definition">a solemn pledge of fidelity</div>
<div class="example">She had pledged to him her
<strong>troth</strong>, and she would not attempt to go back from her pledge at the first appearance of a difficulty.
<br> —
<a href="http://www.gutenberg.org/ebooks/34000" rel="nofollow">Trollope, Anthony</a></div>


</li>






<li class="entry learnable" id="entry486"
 lang="en" word="encroachment" freq="2149.57" prog="0">

<a class="word dynamictext" href="/dictionary/encroachment">encroachment</a>
<div class="definition">entry to another's property without right or permission</div>
<div class="example">The move may mark yet another attempt by France to rein in what it sees as the
<strong>encroachment</strong> of online services on the country's culture.
<br> —
<a href="http://www.businessweek.com/globalbiz/content/jan2010/gb2010018_857194.htm" rel="nofollow">BusinessWeek (Jan 8, 2010)</a></div>


</li>






<li class="entry learnable" id="entry487"
 lang="en" word="belie" freq="2163.33" prog="0">

<a class="word dynamictext" href="/dictionary/belie">belie</a>
<div class="definition">be in contradiction with</div>
<div class="example">"It is a fine morning," he said, taken aback by my sudden movement, but affecting an indifference which the sparkle in his eye
<strong>belied</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/39296" rel="nofollow">Weyman, Stanley John</a></div>


</li>






<li class="entry learnable" id="entry488"
 lang="en" word="armada" freq="2176.07" prog="0">

<a class="word dynamictext" href="/dictionary/armada">armada</a>
<div class="definition">a large fleet</div>
<div class="example">An
<strong>armada</strong> of three hundred ships manned by eighteen thousand marines assembled in the bay on their way to the conquest of Algiers.
<br> —
<a href="http://www.gutenberg.org/ebooks/27068" rel="nofollow">Douglas, Frances</a></div>


</li>






<li class="entry learnable" id="entry489"
 lang="en" word="succor" freq="2193.01" prog="0">

<a class="word dynamictext" href="/dictionary/succor">succor</a>
<div class="definition">assistance in time of difficulty</div>
<div class="example">Given his health woes, succession worries and persistent isolation, Mr. Kim may simply be seeking
<strong>succor</strong> from what may be his last friend on earth.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=da4c903d0c741160350230da6b4b9606" rel="nofollow">New York Times (May 5, 2010)</a></div>


</li>






<li class="entry learnable" id="entry490"
 lang="en" word="imperturbable" freq="2194.23" prog="0">

<a class="word dynamictext" href="/dictionary/imperturbable">imperturbable</a>
<div class="definition">marked by extreme calm and composure</div>
<div class="example">Ordinarily
<strong>imperturbable</strong>, even in the face of unexpected situations, he was now visibly agitated.
<br> —
<a href="http://www.gutenberg.org/ebooks/38830" rel="nofollow">Griggs, Sutton E. (Sutton Elbert)</a></div>


</li>






<li class="entry learnable" id="entry491"
 lang="en" word="irresolute" freq="2199.53" prog="0">

<a class="word dynamictext" href="/dictionary/irresolute">irresolute</a>
<div class="definition">uncertain how to act or proceed</div>
<div class="example">I stood for a moment before I entered on my arduous undertaking,
<strong>irresolute</strong> and hesitating, swayed by two conflicting impulses.
<br> —
<a href="http://www.gutenberg.org/ebooks/35356" rel="nofollow">Waugh, Joseph Laing</a></div>


</li>






<li class="entry learnable" id="entry492"
 lang="en" word="knack" freq="2203.22" prog="0">

<a class="word dynamictext" href="/dictionary/knack">knack</a>
<div class="definition">a special way of doing something</div>
<div class="example">He had a special
<strong>knack</strong> of hunting out farm houses, engaging madame in conversation, and coming away with bread, eggs, or cheese in his knapsack.
<br> —
<a href="http://www.gutenberg.org/ebooks/39330" rel="nofollow">Price, Lucien</a></div>


</li>






<li class="entry learnable" id="entry493"
 lang="en" word="unseemly" freq="2209.39" prog="0">

<a class="word dynamictext" href="/dictionary/unseemly">unseemly</a>
<div class="definition">not in keeping with accepted standards of what is proper</div>
<div class="example">The square mile's upbeat mood may strike some as
<strong>unseemly</strong> at a time of national gloom.
<br> —
<a href="http://www.guardian.co.uk/business/2011/jan/02/stock-market-recovery-recession" rel="nofollow">The Guardian (Jan 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry494"
 lang="en" word="accentuate" freq="2218.51" prog="0">

<a class="word dynamictext" href="/dictionary/accentuate">accentuate</a>
<div class="definition">to stress, single out as important</div>
<div class="example">This sparkling marvel lies modestly nestled among the law courts, whose plainer modern buildings serve but to
<strong>accentuate</strong> its wonderful beauty.
<br> —
<a href="http://www.gutenberg.org/ebooks/34772" rel="nofollow">Sherrill, Charles Hitchcock</a></div>


</li>






<li class="entry learnable" id="entry495"
 lang="en" word="divulge" freq="2227.28" prog="0">

<a class="word dynamictext" href="/dictionary/divulge">divulge</a>
<div class="definition">make known to the public information previously kept secret</div>
<div class="example">She hectors her children not to
<strong>divulge</strong> personal information like phone numbers online.
<br> —
<a href="http://seattletimes.nwsource.com/html/homegarden/2016769753_klout14.html?syndication=rss" rel="nofollow">Seattle Times (Nov 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry496"
 lang="en" word="brawn" freq="2239.08" prog="0">

<a class="word dynamictext" href="/dictionary/brawn">brawn</a>
<div class="definition">possessing muscular strength</div>
<div class="example">He believes Hollywood has often have had an over-reliance on physical
<strong>brawn</strong> as the deciding factor for portraying a strong man.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/entertainment/~3/qZLlQc71JiE/idUSTRE66902W20100710" rel="nofollow">Reuters (Jul 9, 2010)</a></div>


</li>






<li class="entry learnable" id="entry497"
 lang="en" word="burnish" freq="2239.93" prog="0">

<a class="word dynamictext" href="/dictionary/burnish">burnish</a>
<div class="definition">polish and make shiny</div>
<div class="example">Great cleanliness is enforced in all that belongs to a lighthouse, the reflectors and lenses being constantly
<strong>burnished</strong>, polished, and cleansed.
<br> —
<a href="http://www.gutenberg.org/ebooks/39342" rel="nofollow">Whymper, Frederick</a></div>


</li>






<li class="entry learnable" id="entry498"
 lang="en" word="palpitate" freq="2251.01" prog="0">

<a class="word dynamictext" href="/dictionary/palpitate">palpitate</a>
<div class="definition">beat rapidly</div>
<div class="example">After supper my heart started racing,
<strong>palpitating</strong> like a tick.
<br> —
<a href="http://www.gutenberg.org/ebooks/37060" rel="nofollow">Isaacson, Lauren Ann</a></div>


</li>






<li class="entry learnable" id="entry499"
 lang="en" word="promiscuous" freq="2278.32" prog="0">

<a class="word dynamictext" href="/dictionary/promiscuous">promiscuous</a>
<div class="definition">not selective of a single class or person</div>
<div class="example">A
<strong>promiscuous</strong> assembly had gathered there—men of all creeds and opinions—and an "open-air" meeting was in progress.
<br> —
<a href="http://www.gutenberg.org/ebooks/35333" rel="nofollow">Whitney, Orson F.</a></div>


</li>






<li class="entry learnable" id="entry500"
 lang="en" word="dissemble" freq="2283.6" prog="0">

<a class="word dynamictext" href="/dictionary/dissemble">dissemble</a>
<div class="definition">make believe with the intent to deceive</div>
<div class="example">Pictures have always
<strong>dissembled</strong> – there are millions of snaps of miserable families grinning bravely – but now they directly lie.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2010/dec/05/david-mitchell-weather-forecasts-met-office" rel="nofollow">The Guardian (Dec 4, 2010)</a></div>


</li>






<li class="entry learnable" id="entry501"
 lang="en" word="flotilla" freq="2287.58" prog="0">

<a class="word dynamictext" href="/dictionary/flotilla">flotilla</a>
<div class="definition">a fleet of small craft</div>
<div class="example">She was guarded by a
<strong>flotilla</strong> of boats equipped with satellites, Global Positioning System devices, advanced navigation systems and shark shields.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=54c6fb827305741b29a967a2d3a14dd3" rel="nofollow">New York Times (Aug 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry502"
 lang="en" word="invective" freq="2300.48" prog="0">

<a class="word dynamictext" href="/dictionary/invective">invective</a>
<div class="definition">abusive language used to express blame or censure</div>
<div class="example">There's much more name-calling, shouting and personal
<strong>invective</strong> in American life than anywhere I've ever traveled outside the United States.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=fe752144e9fa2927cb3f98520858502a" rel="nofollow">Washington Post (Jan 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry503"
 lang="en" word="hermitage" freq="2309.46" prog="0">

<a class="word dynamictext" href="/dictionary/hermitage">hermitage</a>
<div class="definition">the abode of a recluse</div>
<div class="example">All the rest of their time is passed in solitude in their
<strong>hermitages</strong>, which are built quite separate from one another.
<br> —
<a href="http://www.gutenberg.org/ebooks/33189" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry504"
 lang="en" word="despoil" freq="2316.24" prog="0">

<a class="word dynamictext" href="/dictionary/despoil">despoil</a>
<div class="definition">destroy and strip of its possession</div>
<div class="example">Wherever his lordship's army went, plantations were
<strong>despoiled</strong>, and private houses plundered.
<br> —
<a href="http://www.gutenberg.org/ebooks/32573" rel="nofollow">Campbell, Charles</a></div>


</li>






<li class="entry learnable" id="entry505"
 lang="en" word="sully" freq="2357.32" prog="0">

<a class="word dynamictext" href="/dictionary/sully">sully</a>
<div class="definition">make dirty or spotty</div>
<div class="example">Why
<strong>sully</strong> the reputation of an otherwise fascinating online community with really deeply questionable, troubling content?
<br> —
<a href="http://www.forbes.com/sites/erikkain/2012/02/13/reddit-bans-sexual-content-featuring-minors/" rel="nofollow">Forbes (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry506"
 lang="en" word="malevolent" freq="2360.14" prog="0">

<a class="word dynamictext" href="/dictionary/malevolent">malevolent</a>
<div class="definition">having or exerting a malignant influence</div>
<div class="example">So you don’t believe in evil, as an actual
<strong>malevolent</strong> force?
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=352f3603afd7ef3ffc1d8bac56cab236" rel="nofollow">New York Times (Oct 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry507"
 lang="en" word="irksome" freq="2365.81" prog="0">

<a class="word dynamictext" href="/dictionary/irksome">irksome</a>
<div class="definition">tedious or irritating</div>
<div class="example">It was pretty
<strong>irksome</strong> passing the time in his enforced prison, and finally Andy went to sleep.
<br> —
<a href="http://www.gutenberg.org/ebooks/36388" rel="nofollow">Webster, Frank V.</a></div>


</li>






<li class="entry learnable" id="entry508"
 lang="en" word="prattle" freq="2371.5" prog="0">

<a class="word dynamictext" href="/dictionary/prattle">prattle</a>
<div class="definition">speak about unimportant matters rapidly and incessantly</div>
<div class="example">She
<strong>prattled</strong> on about the gossip of the town until Penny and her father were thoroughly bored.
<br> —
<a href="http://www.gutenberg.org/ebooks/33383" rel="nofollow">Clark, Joan</a></div>


</li>






<li class="entry learnable" id="entry509"
 lang="en" word="subaltern" freq="2379.13" prog="0">

<a class="word dynamictext" href="/dictionary/subaltern">subaltern</a>
<div class="definition">inferior in rank or status</div>
<div class="example">The careful commanding officer of a regiment discourages his young
<strong>subalterns</strong> from taking leave to Hill Stations.
<br> —
<a href="http://www.gutenberg.org/ebooks/37782" rel="nofollow">Casserly, Gordon</a></div>


</li>






<li class="entry learnable" id="entry510"
 lang="en" word="welt" freq="2388.26" prog="0">

<a class="word dynamictext" href="/dictionary/welt">welt</a>
<div class="definition">a raised mark on the skin </div>
<div class="example">But red, itchy
<strong>welts</strong> typically appear within 24 to 48 hours of being bitten.
<br> —
<a href="http://health.usnews.com/articles/health-news/family-health/2010/11/23/attention-travelers-is-the-bedbug-threat-real.html?s_cid=rss:attention-travelers-is-the-bedbug-threat-real" rel="nofollow">US News (Nov 23, 2010)</a></div>


</li>






<li class="entry learnable" id="entry511"
 lang="en" word="wreak" freq="2397.94" prog="0">

<a class="word dynamictext" href="/dictionary/wreak">wreak</a>
<div class="definition">cause to happen or to occur as a consequence</div>
<div class="example">The burden of paying for college is
<strong>wreaking</strong> havoc on the finances of an unexpected demographic: senior citizens.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=e07c3b603668e4cab3ab8619ed83e902" rel="nofollow">Washington Post (Apr 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry512"
 lang="en" word="tenable" freq="2400.86" prog="0">

<a class="word dynamictext" href="/dictionary/tenable">tenable</a>
<div class="definition">based on sound reasoning or evidence</div>
<div class="example">First, it is no longer really
<strong>tenable</strong> – and in fact a bit disrespectful – to call a country like China an emerging economy.
<br> —
<a href="http://www.guardian.co.uk/global-development/poverty-matters/2011/feb/18/brics-next-11-economy-transformation-uk" rel="nofollow">The Guardian (Feb 18, 2011)</a></div>


</li>






<li class="entry learnable" id="entry513"
 lang="en" word="inimitable" freq="2413.6" prog="0">

<a class="word dynamictext" href="/dictionary/inimitable">inimitable</a>
<div class="definition">matchless</div>
<div class="example">Leave aside Spain, where Barcelona breeds its own,
<strong>inimitable</strong> style, and the answer might be that we are rushing toward uniformity.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/tmbUP65z4ek/27iht-SOCCER.html" rel="nofollow">New York Times (Sep 26, 2010)</a></div>


</li>






<li class="entry learnable" id="entry514"
 lang="en" word="depredation" freq="2415.07" prog="0">

<a class="word dynamictext" href="/dictionary/depredation">depredation</a>
<div class="definition">a destructive action</div>
<div class="example">Wild elephants abound and commit many
<strong>depredations</strong>, entering villages in large herds, and consuming everything suitable to their tastes.
<br> —
<a href="http://www.gutenberg.org/ebooks/34209" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry515"
 lang="en" word="amalgamate" freq="2430.46" prog="0">

<a class="word dynamictext" href="/dictionary/amalgamate">amalgamate</a>
<div class="definition">to bring or combine together or with something else</div>
<div class="example">Where two weak tribes
<strong>amalgamated</strong> into one, there it exceptionally happened that two closely related dialects were simultaneously spoken in the same tribe.
<br> —
<a href="http://www.gutenberg.org/ebooks/33111" rel="nofollow">Engels, Friedrich</a></div>


</li>






<li class="entry learnable" id="entry516"
 lang="en" word="immutable" freq="2447.56" prog="0">

<a class="word dynamictext" href="/dictionary/immutable">immutable</a>
<div class="definition">not subject or susceptible to change or variation</div>
<div class="example">We are mistaken to imagine a work of literature is or should be
<strong>immutable</strong>, sculpted in marble and similarly impervious to change.
<br> —
<a href="http://www.guardian.co.uk/stage/theatreblog/2010/may/27/are-plays-proper-literature" rel="nofollow">The Guardian (May 27, 2010)</a></div>


</li>






<li class="entry learnable" id="entry517"
 lang="en" word="proxy" freq="2449.08" prog="0">

<a class="word dynamictext" href="/dictionary/proxy">proxy</a>
<div class="definition">a person authorized to act for another</div>
<div class="example">Ideally, everybody over 18 should execute a living will and select a health care
<strong>proxy</strong> — someone to represent you in medical matters.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4962682223fd277433c147025ed2e27d" rel="nofollow">New York Times (Jan 17, 2011)</a></div>


</li>






<li class="entry learnable" id="entry518"
 lang="en" word="dote" freq="2450.6" prog="0">

<a class="word dynamictext" href="/dictionary/dote">dote</a>
<div class="definition">shower with love; show excessive affection for</div>
<div class="example">He
<strong>doted</strong> on him, just dearly loved him, and thought he could do no wrong,” Kredell said.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=d4713ed31d7aaf9c7e256560977d41e4" rel="nofollow">Washington Post (Oct 17, 2011)</a></div>


</li>






<li class="entry learnable" id="entry519"
 lang="en" word="reactionary" freq="2457.22" prog="0">

<a class="word dynamictext" href="/dictionary/reactionary">reactionary</a>
<div class="definition">extremely conservative</div>
<div class="example">Old people are often accused of being too conservative, and even
<strong>reactionary</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38073" rel="nofollow">Chinard, Gilbert</a></div>


</li>






<li class="entry learnable" id="entry520"
 lang="en" word="rationalism" freq="2461.31" prog="0">

<a class="word dynamictext" href="/dictionary/rationalism">rationalism</a>
<div class="definition">the doctrine that reason is the basis for regulating conduct</div>
<div class="example">Offering a religious rationale for policy goals threatens what for many has become the cherished principle of secular
<strong>rationalism</strong> in public life.
<br> —
<a href="http://www.salon.com/news/politics/war_room/2011/04/24/brad_martin_jesus_budget" rel="nofollow">Salon (Apr 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry521"
 lang="en" word="endue" freq="2476.77" prog="0">

<a class="word dynamictext" href="/dictionary/endue">endue</a>
<div class="definition">give qualities or abilities to</div>
<div class="example">To say the least of it, he was
<strong>endued</strong> with sufficient intelligence to acquire an ordinary knowledge of such matters.
<br> —
<a href="http://www.gutenberg.org/ebooks/27605" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry522"
 lang="en" word="discriminating" freq="2481.96" prog="0">

<a class="word dynamictext" href="/dictionary/discriminating">discriminating</a>
<div class="definition">showing or indicating careful judgment and discernment</div>
<div class="example">Jobs’ Apple specializes in delighting the most
<strong>discriminating</strong>, hard-to-please customers.
<br> —
<a href="http://www.forbes.com/sites/scottcleland/2011/10/12/jobs-apple-standard-vs-pages-google-standard/" rel="nofollow">Forbes (Oct 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry523"
 lang="en" word="brooch" freq="2498.74" prog="0">

<a class="word dynamictext" href="/dictionary/brooch">brooch</a>
<div class="definition">a decorative pin worn by women</div>
<div class="example">Upon her breast she wore a
<strong>brooch</strong> of gold set with many precious stones.
<br> —
<a href="http://www.gutenberg.org/ebooks/32695" rel="nofollow">Butler, Pierce</a></div>


</li>






<li class="entry learnable" id="entry524"
 lang="en" word="pert" freq="2503.5" prog="0">

<a class="word dynamictext" href="/dictionary/pert">pert</a>
<div class="definition">characterized by a lightly exuberant quality</div>
<div class="example">Her
<strong>pert</strong>, lively manner said she hadn't taken any wooden nickels lately.
<br> —
<a href="http://www.gutenberg.org/ebooks/30679" rel="nofollow">Schoenherr, John</a></div>


</li>






<li class="entry learnable" id="entry525"
 lang="en" word="disembark" freq="2504.03" prog="0">

<a class="word dynamictext" href="/dictionary/disembark">disembark</a>
<div class="definition">go ashore</div>
<div class="example">The immigrants
<strong>disembarked</strong> from their ships tired and underfed—generally in poor health.
<br> —
<a href="http://www.gutenberg.org/ebooks/28390" rel="nofollow">Hughes, Thomas Proctor</a></div>


</li>






<li class="entry learnable" id="entry526"
 lang="en" word="aria" freq="2528.11" prog="0">

<a class="word dynamictext" href="/dictionary/aria">aria</a>
<div class="definition">an elaborate song for solo voice</div>
<div class="example">Ms. Netrebko sang an elegantly sad
<strong>aria</strong> with lustrous warmth, aching vulnerability and floating high notes.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=7c1e84f36c235b6801d56bb15b1616d0" rel="nofollow">New York Times (Sep 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry527"
 lang="en" word="trappings" freq="2530.82" prog="0">

<a class="word dynamictext" href="/dictionary/trappings">trappings</a>
<div class="definition">ornaments; embellishments to or characteristic signs of</div>
<div class="example">They were caparisoned in Indian fashion with gay colors and fancy
<strong>trappings</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38018" rel="nofollow">Roy, Lillian Elizabeth</a></div>


</li>






<li class="entry learnable" id="entry528"
 lang="en" word="abet" freq="2534.07" prog="0">

<a class="word dynamictext" href="/dictionary/abet">abet</a>
<div class="definition">assist or encourage, usually in some wrongdoing</div>
<div class="example">"Since YouTube, digital culture has aided and enhanced -- or maybe the better word is
<strong>abetted</strong> -- the celebrity meltdown," said Wired magazine senior editor Nancy Miller.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/entertainment/~3/pa2c8Aay7kU/us-charliesheen-internet-idUSTRE7287AT20110309" rel="nofollow">Reuters (Mar 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry529"
 lang="en" word="clandestine" freq="2539.51" prog="0">

<a class="word dynamictext" href="/dictionary/clandestine">clandestine</a>
<div class="definition">conducted with or marked by hidden aims or methods</div>
<div class="example">For Jordan, this is a
<strong>clandestine</strong> relationship it would much prefer to have kept secret.
<br> —
<a href="http://news.bbc.co.uk/go/rss/-/2/hi/americas/8442473.stm" rel="nofollow">BBC (Jan 5, 2010)</a></div>


</li>






<li class="entry learnable" id="entry530"
 lang="en" word="distend" freq="2543.33" prog="0">

<a class="word dynamictext" href="/dictionary/distend">distend</a>
<div class="definition">swell from or as if from internal pressure</div>
<div class="example">Some kids said LaNiyah's
<strong>distended</strong> abdomen looked like she was carrying a baby.
<br> —
<a href="http://seattletimes.nwsource.com/html/books/2014710001_webbully09.html?syndication=rss" rel="nofollow">Seattle Times (Apr 7, 2011)</a></div>


</li>






<li class="entry learnable" id="entry531"
 lang="en" word="glib" freq="2543.88" prog="0">

<a class="word dynamictext" href="/dictionary/glib">glib</a>
<div class="definition">having only superficial plausibility</div>
<div class="example">The other sort of engineer understands that
<strong>glib</strong> comparisons between computers and humans don't do justice to the complexities of either.
<br> —
<a href="http://www.forbes.com/forbes/2010/0809/technology-computer-learning-google-translate.html?feed=rss_technology" rel="nofollow">Forbes (Jul 22, 2010)</a></div>


</li>






<li class="entry learnable" id="entry532"
 lang="en" word="pucker" freq="2548.27" prog="0">

<a class="word dynamictext" href="/dictionary/pucker">pucker</a>
<div class="definition">gather something into small wrinkles or folds</div>
<div class="example">Godmother,' she went on,
<strong>puckering</strong> her forehead again in perplexity, 'it almost feels like feathers.
<br> —
<a href="http://www.gutenberg.org/ebooks/39375" rel="nofollow">Molesworth, Mrs. (Mary Louisa)</a></div>


</li>






<li class="entry learnable" id="entry533"
 lang="en" word="rejoinder" freq="2553.22" prog="0">

<a class="word dynamictext" href="/dictionary/rejoinder">rejoinder</a>
<div class="definition">a quick reply to a question or remark</div>
<div class="example">"Not at all!" was Aunt Susannah's brisk
<strong>rejoinder</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38683" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry534"
 lang="en" word="spangle" freq="2554.87" prog="0">

<a class="word dynamictext" href="/dictionary/spangle">spangle</a>
<div class="definition">adornment consisting of a small piece of shiny material</div>
<div class="example">Magdalen's garments are rich with
<strong>spangles</strong>; her mantle is scarlet; she has flowers in her luxuriant tresses, and looks a vain creature.
<br> —
<a href="http://www.gutenberg.org/ebooks/34753" rel="nofollow">O'Shea, John Augustus</a></div>


</li>






<li class="entry learnable" id="entry535"
 lang="en" word="blighted" freq="2568.74" prog="0">

<a class="word dynamictext" href="/dictionary/blighted">blighted</a>
<div class="definition">affected by something that prevents growth or prosperity</div>
<div class="example">Hudec, whose career has been
<strong>blighted</strong> by knee injuries and operations, won for the first time in more than four years.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/GuGzHkZ-R1A/vonn-beats-the-cold-and-the-clock-in-downhill-for-50th-career-win.html" rel="nofollow">New York Times (Feb 4, 2012)</a></div>


</li>






<li class="entry learnable" id="entry536"
 lang="en" word="nicety" freq="2569.86" prog="0">

<a class="word dynamictext" href="/dictionary/nicety">nicety</a>
<div class="definition">conformity with some aesthetic standard of correctness</div>
<div class="example">They accepted the invitation; but Mrs. Rowlandson did not appreciate the
<strong>niceties</strong> of Indian etiquette.
<br> —
<a href="http://www.gutenberg.org/ebooks/29494" rel="nofollow">Abbott, John S. C. (John Stevens Cabot)</a></div>


</li>






<li class="entry learnable" id="entry537"
 lang="en" word="aggrieve" freq="2590.12" prog="0">

<a class="word dynamictext" href="/dictionary/aggrieve">aggrieve</a>
<div class="definition">infringe on the rights of</div>
<div class="example">Some fallout appears evident in donations from Wall Street executives, who feel particularly
<strong>aggrieved</strong> by Mr. Obama’s criticisms and policies.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6860076e1fff79bd9a5cc276a0d3e4da" rel="nofollow">New York Times (Feb 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry538"
 lang="en" word="vestment" freq="2602.65" prog="0">

<a class="word dynamictext" href="/dictionary/vestment">vestment</a>
<div class="definition">a gown worn by the clergy</div>
<div class="example">And then a priest, arrayed in all his
<strong>vestments</strong>, came in at the open door, and the prince and princess exchanged rings, and were married.
<br> —
<a href="http://www.gutenberg.org/ebooks/36668" rel="nofollow">Glinski, A. J.</a></div>


</li>






<li class="entry learnable" id="entry539"
 lang="en" word="urbane" freq="2611.27" prog="0">

<a class="word dynamictext" href="/dictionary/urbane">urbane</a>
<div class="definition">showing a high degree of refinement</div>
<div class="example">Polished,
<strong>urbane</strong> and gentlemanly—his manners were calculated to refine all around him.
<br> —
<a href="http://www.gutenberg.org/ebooks/33905" rel="nofollow">Judson, L. Carroll</a></div>


</li>






<li class="entry learnable" id="entry540"
 lang="en" word="defray" freq="2631.02" prog="0">

<a class="word dynamictext" href="/dictionary/defray">defray</a>
<div class="definition">bear the expenses of</div>
<div class="example">The legislation also calls for $1.6 billion in spending cuts to help
<strong>defray</strong> the disaster costs.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=850f57535113a20c17c8b53adf1f47b8" rel="nofollow">Washington Post (Sep 26, 2011)</a></div>


</li>






<li class="entry learnable" id="entry541"
 lang="en" word="spectral" freq="2670.82" prog="0">

<a class="word dynamictext" href="/dictionary/spectral">spectral</a>
<div class="definition">resembling or characteristic of a phantom</div>
<div class="example">Hawthorne’s figures are somewhat
<strong>spectral</strong>; they lack flesh and blood.
<br> —
<a href="http://www.gutenberg.org/ebooks/34940" rel="nofollow">Merwin, Henry Childs</a></div>


</li>






<li class="entry learnable" id="entry542"
 lang="en" word="munificent" freq="2673.24" prog="0">

<a class="word dynamictext" href="/dictionary/munificent">munificent</a>
<div class="definition">very generous</div>
<div class="example">They have shown themselves very loving and generous lately, in making a quite
<strong>munificent</strong> provision for his traveling.
<br> —
<a href="http://www.gutenberg.org/ebooks/13660" rel="nofollow">Carlyle, Thomas</a></div>


</li>






<li class="entry learnable" id="entry543"
 lang="en" word="dictum" freq="2674.45" prog="0">

<a class="word dynamictext" href="/dictionary/dictum">dictum</a>
<div class="definition">an authoritative declaration</div>
<div class="example">In other words, they seemed fully subscribed to Andy Warhol’s
<strong>dictum</strong> that business art is the best art.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=398450602cdf3e907d208593953842df" rel="nofollow">New York Times (Dec 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry544"
 lang="en" word="fad" freq="2675.05" prog="0">

<a class="word dynamictext" href="/dictionary/fad">fad</a>
<div class="definition">an interest followed with exaggerated zeal</div>
<div class="example">According to Chinese media, the hottest new
<strong>fad</strong> in China involves selling small live-animal key chains.
<br> —
<a href="http://feedproxy.google.com/~r/time/world/~3/rTNNVo1KnkM/0,8599,2063334,00.html" rel="nofollow">Time (Apr 5, 2011)</a></div>


</li>






<li class="entry learnable" id="entry545"
 lang="en" word="scabbard" freq="2688.43" prog="0">

<a class="word dynamictext" href="/dictionary/scabbard">scabbard</a>
<div class="definition">a sheath for a sword or dagger or bayonet</div>
<div class="example">Drawing his own sabre from its
<strong>scabbard</strong>, he pointed to a stain on it, saying, "This is the blood of an Englishman."
<br> —
<a href="http://www.gutenberg.org/ebooks/35037" rel="nofollow">Reed, Helen Leah</a></div>


</li>






<li class="entry learnable" id="entry546"
 lang="en" word="adulterate" freq="2689.04" prog="0">

<a class="word dynamictext" href="/dictionary/adulterate">adulterate</a>
<div class="definition">make impure by adding a foreign or inferior substance</div>
<div class="example">Shady dealers along the supply chain frequently
<strong>adulterate</strong> olive oil with low-grade vegetable oils and add artificial coloring.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=d436ecbf1ffe5ecc241f254422fda149" rel="nofollow">New York Times (Dec 7, 2011)</a></div>


</li>






<li class="entry learnable" id="entry547"
 lang="en" word="beleaguer" freq="2692.1" prog="0">

<a class="word dynamictext" href="/dictionary/beleaguer">beleaguer</a>
<div class="definition">annoy persistently</div>
<div class="example">Rock concert ticket sales dropped sharply last year, sounding another sour note for the
<strong>beleaguered</strong> music industry.
<br> —
<a href="http://www.guardian.co.uk/business/2010/dec/30/rock-concert-sales-plunge" rel="nofollow">The Guardian (Dec 30, 2010)</a></div>


</li>






<li class="entry learnable" id="entry548"
 lang="en" word="gripe" freq="2693.33" prog="0">

<a class="word dynamictext" href="/dictionary/gripe">gripe</a>
<div class="definition">complain</div>
<div class="example">If America is going to
<strong>gripe</strong> about the yuan’s rate, then China will complain about the dollar’s role.
<br> —
<a href="http://www.economist.com/businessfinance/displaystory.cfm?story_id=17965485&amp;fsrc=rss" rel="nofollow">Economist (Jan 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry549"
 lang="en" word="remission" freq="2701.32" prog="0">

<a class="word dynamictext" href="/dictionary/remission">remission</a>
<div class="definition">an abatement in intensity or degree</div>
<div class="example">After a few hours there is a
<strong>remission</strong> of the pain, slight perspiration takes place, and the patient may fall asleep.
<br> —
<a href="http://www.gutenberg.org/ebooks/37984" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry550"
 lang="en" word="exorbitant" freq="2706.89" prog="0">

<a class="word dynamictext" href="/dictionary/exorbitant">exorbitant</a>
<div class="definition">greatly exceeding bounds of reason or moderation</div>
<div class="example">Soon, stories began trickling across the Atlantic of crazed fans paying
<strong>exorbitant</strong> sums to get into London gigs.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/KaTDQWOWrn0/click.phdo" rel="nofollow">Slate (Oct 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry551"
 lang="en" word="invocation" freq="2710.61" prog="0">

<a class="word dynamictext" href="/dictionary/invocation">invocation</a>
<div class="definition">the act of appealing for help</div>
<div class="example">These dances are prayers or
<strong>invocations</strong> for rain, the crowning blessing in this dry land.
<br> —
<a href="http://www.gutenberg.org/ebooks/34135" rel="nofollow">Roosevelt, Theodore</a></div>


</li>






<li class="entry learnable" id="entry552"
 lang="en" word="cajole" freq="2719.33" prog="0">

<a class="word dynamictext" href="/dictionary/cajole">cajole</a>
<div class="definition">influence or urge by gentle urging, caressing, or flattering</div>
<div class="example">Hamilton, however, was not to be
<strong>cajoled</strong> into friendliness by superficial compliment.
<br> —
<a href="http://www.gutenberg.org/ebooks/27888" rel="nofollow">Fisher, Harrison</a></div>


</li>






<li class="entry learnable" id="entry553"
 lang="en" word="inclusive" freq="2756.08" prog="0">

<a class="word dynamictext" href="/dictionary/inclusive">inclusive</a>
<div class="definition">encompassing much or everything</div>
<div class="example">We are going to adhere to our basic programing strategy of nonpartisan information
<strong>inclusive</strong> of all different points of view.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/entertainment/~3/yzSgmLw4sBA/idUSTRE68N37A20100927" rel="nofollow">Reuters (Sep 27, 2010)</a></div>


</li>






<li class="entry learnable" id="entry554"
 lang="en" word="interdict" freq="2767.05" prog="0">

<a class="word dynamictext" href="/dictionary/interdict">interdict</a>
<div class="definition">command against</div>
<div class="example">Failing to satisfy his examiners, he was
<strong>interdicted</strong> from practice, but ignored the prohibition, and suffered more than one imprisonment in consequence.
<br> —
<a href="http://www.gutenberg.org/ebooks/21511" rel="nofollow">Worley, George</a></div>


</li>






<li class="entry learnable" id="entry555"
 lang="en" word="abase" freq="2768.34" prog="0">

<a class="word dynamictext" href="/dictionary/abase">abase</a>
<div class="definition">cause to feel shame</div>
<div class="example">Ashamed,
<strong>abased</strong>, degraded in his own eyes, he turned away his head.
<br> —
<a href="http://www.gutenberg.org/ebooks/25570" rel="nofollow">Caine, Hall, Sir</a></div>


</li>






<li class="entry learnable" id="entry556"
 lang="en" word="obviate" freq="2798.47" prog="0">

<a class="word dynamictext" href="/dictionary/obviate">obviate</a>
<div class="definition">do away with</div>
<div class="example">Comfortable sleeping-cars
<strong>obviate</strong> the necessity of stopping by the way for bodily rest, provided the traveller be physically strong and in good health.
<br> —
<a href="http://www.gutenberg.org/ebooks/34037" rel="nofollow">Ballou, Maturin Murray</a></div>


</li>






<li class="entry learnable" id="entry557"
 lang="en" word="hurtle" freq="2799.79" prog="0">

<a class="word dynamictext" href="/dictionary/hurtle">hurtle</a>
<div class="definition">move with or as if with a rushing sound</div>
<div class="example">The hurricane was expected to hit Washington in the early hours of Sunday before
<strong>hurtling</strong> toward New York City.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/topNews/~3/OQ8jTKAkw2g/us-storm-irene-obama-idUSTRE77Q2K020110828" rel="nofollow">Reuters (Aug 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry558"
 lang="en" word="unanimity" freq="2801.78" prog="0">

<a class="word dynamictext" href="/dictionary/unanimity">unanimity</a>
<div class="definition">everyone being of one mind</div>
<div class="example">On all other points of colonial policy, Mackenzie declared, people would be found to differ, but as regards the post office there was absolute
<strong>unanimity</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/37238" rel="nofollow">Smith, William, Sir</a></div>


</li>






<li class="entry learnable" id="entry559"
 lang="en" word="mettle" freq="2804.44" prog="0">

<a class="word dynamictext" href="/dictionary/mettle">mettle</a>
<div class="definition">the courage to carry on</div>
<div class="example">The deployment will also test the emotional
<strong>mettle</strong> of soldiers and their families.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=f1e8cb3b0d772dbadd9251c8a2ad84c2" rel="nofollow">New York Times (Jun 26, 2010)</a></div>


</li>






<li class="entry learnable" id="entry560"
 lang="en" word="interpolate" freq="2810.44" prog="0">

<a class="word dynamictext" href="/dictionary/interpolate">interpolate</a>
<div class="definition">insert words into texts, often falsifying it thereby</div>
<div class="example">Most scholars agree that these lines are
<strong>interpolated</strong>, since they do not fit in with the rest of the poem.
<br> —
<a href="http://www.gutenberg.org/ebooks/31172" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry561"
 lang="en" word="surreptitious" freq="2813.78" prog="0">

<a class="word dynamictext" href="/dictionary/surreptitious">surreptitious</a>
<div class="definition">marked by quiet and caution and secrecy</div>
<div class="example">He noticed that the peddler was eying the bag Scotty had picked up, and was trying to be
<strong>surreptitious</strong> about it.
<br> —
<a href="http://www.gutenberg.org/ebooks/31589" rel="nofollow">Goodwin, Harold L. (Harold Leland)</a></div>


</li>






<li class="entry learnable" id="entry562"
 lang="en" word="dissimulate" freq="2814.45" prog="0">

<a class="word dynamictext" href="/dictionary/dissimulate">dissimulate</a>
<div class="definition">hide feelings from other people</div>
<div class="example">From infancy these people have been schooled to
<strong>dissimulate</strong> and hide emotion, and ordinarily their faces are as opaque as those of veteran poker players.
<br> —
<a href="http://www.gutenberg.org/ebooks/31709" rel="nofollow">Kephart, Horace</a></div>


</li>






<li class="entry learnable" id="entry563"
 lang="en" word="ruse" freq="2815.12" prog="0">

<a class="word dynamictext" href="/dictionary/ruse">ruse</a>
<div class="definition">a deceptive maneuver, especially to avoid capture</div>
<div class="example">Overseas criminals use elaborate
<strong>ruses</strong>, including phony websites, to trick job-seekers into helping transfer stolen funds.
<br> —
<a href="http://www.businessweek.com/magazine/hackers-target-the-unemployed-as-money-mules-08042011.html" rel="nofollow">BusinessWeek (Aug 4, 2011)</a></div>


</li>






<li class="entry learnable" id="entry564"
 lang="en" word="specious" freq="2838.09" prog="0">

<a class="word dynamictext" href="/dictionary/specious">specious</a>
<div class="definition">plausible but false</div>
<div class="example">You might be tempted to think of the biggest airline as the one with the most aircraft, but capacity differences make this reasoning
<strong>specious</strong>.
<br> —
<a href="http://www.salon.com/tech/col/smith/2010/05/06/worlds_biggest_best_worst_airlines/index.html" rel="nofollow">Salon (May 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry565"
 lang="en" word="revulsion" freq="2845.6" prog="0">

<a class="word dynamictext" href="/dictionary/revulsion">revulsion</a>
<div class="definition">intense aversion</div>
<div class="example">After a first instinctive cry of horrified
<strong>revulsion</strong>, the men reached down under water with their hands and drew out—a corpse.
<br> —
<a href="http://www.gutenberg.org/ebooks/29577" rel="nofollow">Livingston, Arthur</a></div>


</li>






<li class="entry learnable" id="entry566"
 lang="en" word="hale" freq="2854.53" prog="0">

<a class="word dynamictext" href="/dictionary/hale">hale</a>
<div class="definition">exhibiting or restored to vigorous good health</div>
<div class="example">From a hearty,
<strong>hale</strong>, corn-fed boy, he has become pale, lean, and wan.
<br> —
<a href="http://www.gutenberg.org/ebooks/34123" rel="nofollow">Adams, Abigail</a></div>


</li>






<li class="entry learnable" id="entry567"
 lang="en" word="palliate" freq="2871.86" prog="0">

<a class="word dynamictext" href="/dictionary/palliate">palliate</a>
<div class="definition">lessen or to try to lessen the seriousness or extent of</div>
<div class="example">Divisions and inequalities persist, but government can
<strong>palliate</strong> their effects with hard cash.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2010/aug/15/rafael-behr-cameron-benefits-cheats" rel="nofollow">The Guardian (Aug 14, 2010)</a></div>


</li>






<li class="entry learnable" id="entry568"
 lang="en" word="obtuse" freq="2876.05" prog="0">

<a class="word dynamictext" href="/dictionary/obtuse">obtuse</a>
<div class="definition">lacking in insight or discernment</div>
<div class="example">The affair had been mentioned so plainly that it was impossible for the most dense and
<strong>obtuse</strong> person not to have understood the allusion.
<br> —
<a href="http://www.gutenberg.org/ebooks/32524" rel="nofollow">Brazil, Angela</a></div>


</li>






<li class="entry learnable" id="entry569"
 lang="en" word="querulous" freq="2885.17" prog="0">

<a class="word dynamictext" href="/dictionary/querulous">querulous</a>
<div class="definition">habitually complaining</div>
<div class="example">He was, at times, as
<strong>querulous</strong> as a complaining old man.
<br> —
<a href="http://www.gutenberg.org/ebooks/36881" rel="nofollow">Williams, Ben Ames</a></div>


</li>






<li class="entry learnable" id="entry570"
 lang="en" word="vagary" freq="2887.28" prog="0">

<a class="word dynamictext" href="/dictionary/vagary">vagary</a>
<div class="definition">an unexpected and inexplicable change in something</div>
<div class="example">Today such acquisitions are more likely to stay put, destined to survive both market fluctuations and the
<strong>vagaries</strong> of style.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=727b6da10aeb54959799552f787506cd" rel="nofollow">New York Times (Sep 29, 2010)</a></div>


</li>






<li class="entry learnable" id="entry571"
 lang="en" word="incipient" freq="2890.1" prog="0">

<a class="word dynamictext" href="/dictionary/incipient">incipient</a>
<div class="definition">only partly in existence; imperfectly formed</div>
<div class="example">Above all, medical teams will need to establish quick surveillance to identify health needs and pinpoint
<strong>incipient</strong> outbreaks before they explode.
<br> —
<a href="http://feedproxy.google.com/~r/time/world/~3/jo5Avlntg8k/0,8599,1953429,00.html" rel="nofollow">Time (Jan 13, 2010)</a></div>


</li>






<li class="entry learnable" id="entry572"
 lang="en" word="obdurate" freq="2891.51" prog="0">

<a class="word dynamictext" href="/dictionary/obdurate">obdurate</a>
<div class="definition">stubbornly persistent in wrongdoing</div>
<div class="example">Several appeared deeply affected, with tears of repentance standing in their eyes, others sullen and
<strong>obdurate</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/34817" rel="nofollow">Huth, Alexander</a></div>


</li>






<li class="entry learnable" id="entry573"
 lang="en" word="grovel" freq="2912.88" prog="0">

<a class="word dynamictext" href="/dictionary/grovel">grovel</a>
<div class="definition">show submission or fear</div>
<div class="example">The two young men who drove them had fallen flat and were
<strong>grovelling</strong> and wailing for mercy.
<br> —
<a href="http://www.gutenberg.org/ebooks/36605" rel="nofollow">Mitford, Bertram</a></div>


</li>






<li class="entry learnable" id="entry574"
 lang="en" word="refractory" freq="2923.68" prog="0">

<a class="word dynamictext" href="/dictionary/refractory">refractory</a>
<div class="definition">stubbornly resistant to authority or control</div>
<div class="example">Beyond them the gardener struggled with a
<strong>refractory</strong> horse that refused to draw his load of brush and dead leaves.
<br> —
<a href="http://www.gutenberg.org/ebooks/31202" rel="nofollow">Bacon, Josephine Dodge Daskam</a></div>


</li>






<li class="entry learnable" id="entry575"
 lang="en" word="dregs" freq="2944.06" prog="0">

<a class="word dynamictext" href="/dictionary/dregs">dregs</a>
<div class="definition">sediment that has settled at the bottom of a liquid</div>
<div class="example">"Right got to go," Ali says, draining the
<strong>dregs</strong> of his beer.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/magazine-17156674" rel="nofollow">BBC (Feb 25, 2012)</a></div>


</li>






<li class="entry learnable" id="entry576"
 lang="en" word="ascendancy" freq="2944.06" prog="0">

<a class="word dynamictext" href="/dictionary/ascendancy">ascendancy</a>
<div class="definition">the state when one person or group has power over another</div>
<div class="example">But in a few days he had secured an almost incredible
<strong>ascendancy</strong> over the sullen, starved, half-clothed army.
<br> —
<a href="http://www.gutenberg.org/ebooks/37736" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry577"
 lang="en" word="supercilious" freq="2946.99" prog="0">

<a class="word dynamictext" href="/dictionary/supercilious">supercilious</a>
<div class="definition">having or showing arrogant superiority to</div>
<div class="example">A
<strong>supercilious</strong>, patronizing person—son of a wretched country parson—used to loll against the wall of your salon—with his nose in the air.
<br> —
<a href="http://www.gutenberg.org/ebooks/25984" rel="nofollow">Pinero, Arthur Wing, Sir</a></div>


</li>






<li class="entry learnable" id="entry578"
 lang="en" word="pundit" freq="2961.01" prog="0">

<a class="word dynamictext" href="/dictionary/pundit">pundit</a>
<div class="definition">someone who has been admitted to membership in a field</div>
<div class="example"><strong>Pundits</strong> of agricultural science explore the sheds, I believe, the barns, stables, machine-rooms, and so forth, before inspecting the crops.
<br> —
<a href="http://www.gutenberg.org/ebooks/17155" rel="nofollow">Boyle, Frederick</a></div>


</li>






<li class="entry learnable" id="entry579"
 lang="en" word="commiserate" freq="2973.66" prog="0">

<a class="word dynamictext" href="/dictionary/commiserate">commiserate</a>
<div class="definition">to feel or express sympathy or compassion</div>
<div class="example">We had spent countless hours together drinking wine and
<strong>commiserating</strong> about child-rearing, long Wisconsin winters and interrupted sleep.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=7eb6ae760e4cb3eadb45e9d5c34765d4" rel="nofollow">New York Times (Mar 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry580"
 lang="en" word="alcove" freq="2974.41" prog="0">

<a class="word dynamictext" href="/dictionary/alcove">alcove</a>
<div class="definition">a small recess opening off a larger room</div>
<div class="example">They showed him where he would sleep, in a little closet-like
<strong>alcove</strong> screened from the big room by a gay curtain.
<br> —
<a href="http://www.gutenberg.org/ebooks/32988" rel="nofollow">Wilson, Harry Leon</a></div>


</li>






<li class="entry learnable" id="entry581"
 lang="en" word="assay" freq="2977.41" prog="0">

<a class="word dynamictext" href="/dictionary/assay">assay</a>
<div class="definition">make an effort or attempt</div>
<div class="example">He decided to
<strong>assay</strong> one last project before giving up.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=128458003bee431d66bd293f4466ace8" rel="nofollow">New York Times (Mar 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry582"
 lang="en" word="parochial" freq="2906.44" prog="0">

<a class="word dynamictext" href="/dictionary/parochial">parochial</a>
<div class="definition">narrowly restricted in outlook or scope</div>
<div class="example">But Republicans in Pennsylvania also have narrower and more
<strong>parochial</strong> things to worry about.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e0832172bf15f2c5fe67cff96f971ba3" rel="nofollow">New York Times (Sep 17, 2011)</a></div>


</li>






<li class="entry learnable" id="entry583"
 lang="en" word="conjugal" freq="2999.3" prog="0">

<a class="word dynamictext" href="/dictionary/conjugal">conjugal</a>
<div class="definition">relating to the relationship between a wife and husband</div>
<div class="example">They even had
<strong>conjugal</strong> visits for prisoners — five hours in a private room every three months with your wife.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e8e68fb09a474c2b4abc99698795a19f" rel="nofollow">New York Times (Nov 23, 2010)</a></div>


</li>






<li class="entry learnable" id="entry584"
 lang="en" word="abjure" freq="3003.11" prog="0">

<a class="word dynamictext" href="/dictionary/abjure">abjure</a>
<div class="definition">formally reject or disavow a formerly held belief</div>
<div class="example">The caste abstain from liquor, and some of them have
<strong>abjured</strong> all flesh food while others partake of it.
<br> —
<a href="http://www.gutenberg.org/ebooks/20668" rel="nofollow">Russell, R. V. (Robert Vane)</a></div>


</li>






<li class="entry learnable" id="entry585"
 lang="en" word="frieze" freq="3008.46" prog="0">

<a class="word dynamictext" href="/dictionary/frieze">frieze</a>
<div class="definition">an ornament consisting of a horizontal sculptured band</div>
<div class="example">All the doorways mentioned above have cornices, and in those at Palmyra and Baalbec richly carved
<strong>friezes</strong> with side corbels.
<br> —
<a href="http://www.gutenberg.org/ebooks/32758" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry586"
 lang="en" word="ornate" freq="3016.9" prog="0">

<a class="word dynamictext" href="/dictionary/ornate">ornate</a>
<div class="definition">marked by complexity and richness of detail</div>
<div class="example">Unlike his literary icon, Herman Melville, he doesn’t adorn his writing with
<strong>ornate</strong> flourishes or complicated scaffolding.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=99e7be2164a410194534ced785279ad6" rel="nofollow">Scientific American (Dec 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry587"
 lang="en" word="inflammatory" freq="3019.98" prog="0">

<a class="word dynamictext" href="/dictionary/inflammatory">inflammatory</a>
<div class="definition">arousing to action or rebellion</div>
<div class="example">We don't know whether
<strong>inflammatory</strong> language or images can incite the mentally ill to commit acts of violence.
<br> —
<a href="http://feedproxy.google.com/~r/time/nation/~3/LwN-HhkjaUo/0,8599,2042172,00.html" rel="nofollow">Time (Jan 13, 2011)</a></div>


</li>






<li class="entry learnable" id="entry588"
 lang="en" word="machination" freq="3026.94" prog="0">

<a class="word dynamictext" href="/dictionary/machination">machination</a>
<div class="definition">a crafty and involved plot to achieve your ends</div>
<div class="example">He was continued a member of Congress until 1777 when his enemies succeeded in their long nursed
<strong>machinations</strong> against him.
<br> —
<a href="http://www.gutenberg.org/ebooks/33905" rel="nofollow">Judson, L. Carroll</a></div>


</li>






<li class="entry learnable" id="entry589"
 lang="en" word="mendicant" freq="3028.49" prog="0">

<a class="word dynamictext" href="/dictionary/mendicant">mendicant</a>
<div class="definition">a pauper who lives by begging</div>
<div class="example">In others are the broken-down
<strong>mendicants</strong> who live on soup-kitchens and begging.&nbsp;
<br> —
<a href="http://www.gutenberg.org/ebooks/36683" rel="nofollow">Ritchie, J. Ewing (James Ewing)</a></div>


</li>






<li class="entry learnable" id="entry590"
 lang="en" word="meander" freq="3045.64" prog="0">

<a class="word dynamictext" href="/dictionary/meander">meander</a>
<div class="definition">move or cause to move in a sinuous or circular course</div>
<div class="example">They paused beside one of the low stone walls that
<strong>meandered</strong> in a meaningless fashion this way and that over the uplands.
<br> —
<a href="http://www.gutenberg.org/ebooks/32302" rel="nofollow">Vance, Louis Joseph</a></div>


</li>






<li class="entry learnable" id="entry591"
 lang="en" word="bullion" freq="3045.64" prog="0">

<a class="word dynamictext" href="/dictionary/bullion">bullion</a>
<div class="definition">gold or silver in bars or ingots</div>
<div class="example">In times of economic turmoil, more people tend to invest in
<strong>bullion</strong> gold.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=edb3c52281ba9549c0a36f1d2d1b6cbc" rel="nofollow">Washington Post (Mar 30, 2012)</a></div>


</li>






<li class="entry learnable" id="entry592"
 lang="en" word="diffidence" freq="3046.43" prog="0">

<a class="word dynamictext" href="/dictionary/diffidence">diffidence</a>
<div class="definition">lack of self-assurance</div>
<div class="example">His grave
<strong>diffidence</strong> and continued hesitation in offering an opinion confirmed me in my own.
<br> —
<a href="http://www.gutenberg.org/ebooks/32728" rel="nofollow">Froude, James Anthony</a></div>


</li>






<li class="entry learnable" id="entry593"
 lang="en" word="makeshift" freq="3048" prog="0">

<a class="word dynamictext" href="/dictionary/makeshift">makeshift</a>
<div class="definition">done or made using whatever is available</div>
<div class="example">The house was still under construction, so he climbed up a ladder being used as a
<strong>makeshift</strong> stairway, fell and injured his leg.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=92b1430f16b36b8013c0abfecd46a3f3" rel="nofollow">New York Times (Apr 12, 2012)</a></div>


</li>






<li class="entry learnable" id="entry594"
 lang="en" word="husbandry" freq="3053.51" prog="0">

<a class="word dynamictext" href="/dictionary/husbandry">husbandry</a>
<div class="definition">the practice of cultivating the land or raising stock</div>
<div class="example">The U.S. can take a lesson from Denmark, which has efficiently raised livestock without hurting farmers, by using better animal
<strong>husbandry</strong> practices.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=d320bc4d80a5131cc24072c411c33461" rel="nofollow">Scientific American (Mar 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry595"
 lang="en" word="podium" freq="3058.25" prog="0">

<a class="word dynamictext" href="/dictionary/podium">podium</a>
<div class="definition">a platform raised above the surrounding level</div>
<div class="example">Leyva beamed as he stood atop the
<strong>podium</strong>, nodding as the American flag was raised and “The Star-Spangled Banner” played in his honor.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/Efu-k0CsuFY/danell-leyva-parallel-bars-gold-fled-cuba.html" rel="nofollow">New York Times (Oct 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry596"
 lang="en" word="dearth" freq="3059.04" prog="0">

<a class="word dynamictext" href="/dictionary/dearth">dearth</a>
<div class="definition">an insufficient quantity or number</div>
<div class="example">A continuing
<strong>dearth</strong> of snow in many U.S. spots usually buried by this time of year has turned life upside down.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=11b1250064b626fb6b2c16b9be537af4" rel="nofollow">Washington Post (Jan 5, 2012)</a></div>


</li>






<li class="entry learnable" id="entry597"
 lang="en" word="granary" freq="3065.38" prog="0">

<a class="word dynamictext" href="/dictionary/granary">granary</a>
<div class="definition">a storehouse for threshed grain or animal feed</div>
<div class="example">Here is where he does his husking, and the "clear corn" produced is stored away in some underground
<strong>granary</strong> till It is needed.
<br> —
<a href="http://www.gutenberg.org/ebooks/27887" rel="nofollow">Seton, Ernest Thompson</a></div>


</li>






<li class="entry learnable" id="entry598"
 lang="en" word="whet" freq="3073.34" prog="0">

<a class="word dynamictext" href="/dictionary/whet">whet</a>
<div class="definition">make keen or more acute</div>
<div class="example">While he described the fishing as “pretty good,” the silver salmon running in the creek only
<strong>whetted</strong> his appetite to return to Alaska.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=497279566e22212aa223b6590b35527b" rel="nofollow">Washington Post (Aug 17, 2011)</a></div>


</li>






<li class="entry learnable" id="entry599"
 lang="en" word="imposture" freq="3077.34" prog="0">

<a class="word dynamictext" href="/dictionary/imposture">imposture</a>
<div class="definition">pretending to be another person</div>
<div class="example">He got somebody to prosecute him for false pretences and
<strong>imposture</strong>, on the ground that Madame was a man.&nbsp;
<br> —
<a href="http://www.gutenberg.org/ebooks/22030" rel="nofollow">Leland, Charles Godfrey</a></div>


</li>






<li class="entry learnable" id="entry600"
 lang="en" word="diadem" freq="3079.75" prog="0">

<a class="word dynamictext" href="/dictionary/diadem">diadem</a>
<div class="definition">an ornamental jeweled headdress signifying sovereignty</div>
<div class="example">I dethrone monarchs and the people rejoicing crown me instead, showering
<strong>diadems</strong> upon my head.
<br> —
<a href="http://www.gutenberg.org/ebooks/15946" rel="nofollow">Tilney, Frederick Colin</a></div>


</li>






<li class="entry learnable" id="entry601"
 lang="en" word="fallow" freq="3081.35" prog="0">

<a class="word dynamictext" href="/dictionary/fallow">fallow</a>
<div class="definition">undeveloped but potentially useful</div>
<div class="example">Several new prostate cancer drugs have been approved in the last couple of years, after a long
<strong>fallow</strong> period, and others are in advanced development.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=9195cbb2ef59dea4ad148b884b7bcd2d" rel="nofollow">New York Times (Nov 3, 2011)</a></div>


</li>






<li class="entry learnable" id="entry602"
 lang="en" word="hubbub" freq="3117.91" prog="0">

<a class="word dynamictext" href="/dictionary/hubbub">hubbub</a>
<div class="definition">loud confused noise from many sources</div>
<div class="example">There was some good-humoured pushing and thrusting, the drum beating and the church bells jangling bravely above the
<strong>hubbub</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38871" rel="nofollow">Weyman, Stanley J.</a></div>


</li>






<li class="entry learnable" id="entry603"
 lang="en" word="dispassionate" freq="3120.37" prog="0">

<a class="word dynamictext" href="/dictionary/dispassionate">dispassionate</a>
<div class="definition">unaffected by strong emotion or prejudice</div>
<div class="example">The commission sitting by, judicial,
<strong>dispassionate</strong>, presided with cold dignity over the sacrifice, and pronounced it good.
<br> —
<a href="http://www.gutenberg.org/ebooks/26151" rel="nofollow">Candee, Helen Churchill Hungerford, Mrs.</a></div>


</li>






<li class="entry learnable" id="entry604"
 lang="en" word="harrowing" freq="3126.97" prog="0">

<a class="word dynamictext" href="/dictionary/harrowing">harrowing</a>
<div class="definition">causing extreme distress</div>
<div class="example">Belgium found itself in turmoil as hundreds of people came forward to offer
<strong>harrowing</strong> accounts of abuse over several decades.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=70b4a485dc3106339eb0123f1977daa7" rel="nofollow">New York Times (Jan 16, 2012)</a></div>


</li>






<li class="entry learnable" id="entry605"
 lang="en" word="askance" freq="3136.1" prog="0">

<a class="word dynamictext" href="/dictionary/askance">askance</a>
<div class="definition">with suspicion or disapproval</div>
<div class="example">A secret marriage in these days would be looked upon
<strong>askance</strong> by most people.
<br> —
<a href="http://www.gutenberg.org/ebooks/38832" rel="nofollow">Wood, Mrs. Henry</a></div>


</li>






<li class="entry learnable" id="entry606"
 lang="en" word="lancet" freq="3162.09" prog="0">

<a class="word dynamictext" href="/dictionary/lancet">lancet</a>
<div class="definition">a surgical knife with a pointed double-edged blade</div>
<div class="example">His left arm was held by the second physician, while the chief surgeon bent over it,
<strong>lancet</strong> in hand.
<br> —
<a href="http://www.gutenberg.org/ebooks/25758" rel="nofollow">Hay, Marie, Hon. (Agnes Blanche Marie)</a></div>


</li>






<li class="entry learnable" id="entry607"
 lang="en" word="rankle" freq="3168.02" prog="0">

<a class="word dynamictext" href="/dictionary/rankle">rankle</a>
<div class="definition">gnaw into; make resentful or angry</div>
<div class="example">He was feeling more like himself now, though the memory of the bully’s sneering words
<strong>rankled</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/38897" rel="nofollow">Chadwick, Lester</a></div>


</li>






<li class="entry learnable" id="entry608"
 lang="en" word="ramify" freq="3168.87" prog="0">

<a class="word dynamictext" href="/dictionary/ramify">ramify</a>
<div class="definition">have or develop complicating consequences</div>
<div class="example">Cometary science has
<strong>ramified</strong> in unexpected ways during the last hundred years.
<br> —
<a href="http://www.gutenberg.org/ebooks/34209" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry609"
 lang="en" word="gainsay" freq="3172.27" prog="0">

<a class="word dynamictext" href="/dictionary/gainsay">gainsay</a>
<div class="definition">take exception to</div>
<div class="example">That Whitman entertained a genuine affection for men and women is, of course, too obvious to be
<strong>gainsaid</strong>.&nbsp;
<br> —
<a href="http://www.gutenberg.org/ebooks/33356" rel="nofollow">Rickett, Arthur</a></div>


</li>






<li class="entry learnable" id="entry610"
 lang="en" word="polity" freq="3194.55" prog="0">

<a class="word dynamictext" href="/dictionary/polity">polity</a>
<div class="definition">a governmentally organized unit</div>
<div class="example">China needs a
<strong>polity</strong> that can address its increasingly sophisticated society, and to achieve that there must be political reform, Mr. Sun said.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=0c33ef14c46763acfc755d48184ba417" rel="nofollow">New York Times (Mar 21, 2012)</a></div>


</li>






<li class="entry learnable" id="entry611"
 lang="en" word="credence" freq="3196.27" prog="0">

<a class="word dynamictext" href="/dictionary/credence">credence</a>
<div class="definition">the mental attitude that something is believable</div>
<div class="example">"Well-known brand names that promote new products receive more
<strong>credence</strong> than newcomers that people don't know about."
<br> —
<a href="http://health.usnews.com/articles/health-news/diet-fitness/2010/10/6/7-marketing-claims-that-took-heat.html?s_cid=rss:7-marketing-claims-that-took-heat" rel="nofollow">US News (Oct 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry612"
 lang="en" word="indemnify" freq="3204.07" prog="0">

<a class="word dynamictext" href="/dictionary/indemnify">indemnify</a>
<div class="definition">make amends for; pay compensation for</div>
<div class="example">She put her affairs in order and left instructions that those whom she had unwittingly wronged should be
<strong>indemnified</strong> out of her private fortune.
<br> —
<a href="http://www.gutenberg.org/ebooks/32695" rel="nofollow">Butler, Pierce</a></div>


</li>






<li class="entry learnable" id="entry613"
 lang="en" word="ingratiate" freq="3213.64" prog="0">

<a class="word dynamictext" href="/dictionary/ingratiate">ingratiate</a>
<div class="definition">gain favor with somebody by deliberate efforts</div>
<div class="example">He became kindly and coaxing, leaning across the table with an
<strong>ingratiating</strong> smile.
<br> —
<a href="http://www.gutenberg.org/ebooks/35463" rel="nofollow">King, Basil</a></div>


</li>






<li class="entry learnable" id="entry614"
 lang="en" word="declivity" freq="3222.4" prog="0">

<a class="word dynamictext" href="/dictionary/declivity">declivity</a>
<div class="definition">a downward slope or bend</div>
<div class="example">In this frightful condition, the hunter grappled with the raging beast, and, struggling for life, they rolled together down a steep
<strong>declivity</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/33687" rel="nofollow">Goodrich, Samuel G. (Samuel Griswold)</a></div>


</li>






<li class="entry learnable" id="entry615"
 lang="en" word="importunate" freq="3228.56" prog="0">

<a class="word dynamictext" href="/dictionary/importunate">importunate</a>
<div class="definition">making persistent or urgent requests</div>
<div class="example">The young man was then passionately
<strong>importunate</strong> in the protestations of his love.
<br> —
<a href="http://www.gutenberg.org/ebooks/32085" rel="nofollow">Barr, Amelia Edith Huddleston</a></div>


</li>






<li class="entry learnable" id="entry616"
 lang="en" word="passe" freq="3242.72" prog="0">

<a class="word dynamictext" href="/dictionary/passe">passe</a>
<div class="definition">out of fashion</div>
<div class="example">My friend is very keen on the new crowd; everything else he declares is "
<strong>passe</strong>."
<br> —
<a href="http://www.gutenberg.org/ebooks/13708" rel="nofollow">Holliday, Robert Cortes</a></div>


</li>






<li class="entry learnable" id="entry617"
 lang="en" word="whittle" freq="3248.06" prog="0">

<a class="word dynamictext" href="/dictionary/whittle">whittle</a>
<div class="definition">cut small bits or pare shavings from</div>
<div class="example">Tad followed,
<strong>whittling</strong> on a stick with his knife and kicking at the shavings as they fell.
<br> —
<a href="http://www.gutenberg.org/ebooks/34697" rel="nofollow">Kjelgaard, James Arthur</a></div>


</li>






<li class="entry learnable" id="entry618"
 lang="en" word="repine" freq="3268.71" prog="0">

<a class="word dynamictext" href="/dictionary/repine">repine</a>
<div class="definition">express discontent</div>
<div class="example">Those poor fellows above, accustomed to the wild freshness and freedom of the sea, how they must mourn and
<strong>repine</strong>!
<br> —
<a href="http://www.gutenberg.org/ebooks/31532" rel="nofollow">O'Shea, John Augustus</a></div>


</li>






<li class="entry learnable" id="entry619"
 lang="en" word="flay" freq="3274.14" prog="0">

<a class="word dynamictext" href="/dictionary/flay">flay</a>
<div class="definition">strip the skin off</div>
<div class="example">Once at the moose and hastily
<strong>flaying</strong> the hide from the steaming meat my attention became centered on the task.
<br> —
<a href="http://www.gutenberg.org/ebooks/35031" rel="nofollow">Sinclair, Bertrand W.</a></div>


</li>






<li class="entry learnable" id="entry620"
 lang="en" word="larder" freq="3284.14" prog="0">

<a class="word dynamictext" href="/dictionary/larder">larder</a>
<div class="definition">a small storeroom for storing foods or wines</div>
<div class="example">Mr. Goncalves’s
<strong>larder</strong> holds staples like beefsteak, salt cod, sardines, olives, artichokes, hot and sweet peppers and plenty of garlic.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=5aa475006a6d6795c222dec93f8d11d6" rel="nofollow">New York Times (Feb 18, 2011)</a></div>


</li>






<li class="entry learnable" id="entry621"
 lang="en" word="threadbare" freq="3286.88" prog="0">

<a class="word dynamictext" href="/dictionary/threadbare">threadbare</a>
<div class="definition">thin and tattered with age</div>
<div class="example">They were all poor folk, wrapped in
<strong>threadbare</strong> cloaks or tattered leather.
<br> —
<a href="http://www.gutenberg.org/ebooks/32664" rel="nofollow">Brackett, Leigh Douglass</a></div>


</li>






<li class="entry learnable" id="entry622"
 lang="en" word="grisly" freq="3296.04" prog="0">

<a class="word dynamictext" href="/dictionary/grisly">grisly</a>
<div class="definition">shockingly repellent; inspiring horror</div>
<div class="example">Television video showed a heavily damaged building and a
<strong>grisly</strong> scene inside, with clothing and prayer mats scattered across a blood-splattered floor.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4fdb0581fce49a80578f4da715b5f09f" rel="nofollow">New York Times (Aug 19, 2011)</a></div>


</li>






<li class="entry learnable" id="entry623"
 lang="en" word="untoward" freq="3306.18" prog="0">

<a class="word dynamictext" href="/dictionary/untoward">untoward</a>
<div class="definition">not in keeping with accepted standards of what is proper</div>
<div class="example">Responding to criticism that cash payments are a classic means of tax evasion, he said he had done nothing
<strong>untoward</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=cabfe85dce2b638891b12b0e0bb205bb" rel="nofollow">New York Times (Aug 2, 2011)</a></div>


</li>






<li class="entry learnable" id="entry624"
 lang="en" word="idiosyncrasy" freq="3312.66" prog="0">

<a class="word dynamictext" href="/dictionary/idiosyncrasy">idiosyncrasy</a>
<div class="definition">a behavioral attribute peculiar to an individual</div>
<div class="example">One of his well-known
<strong>idiosyncrasies</strong> was that he would never allow himself to be photographed.
<br> —
<a href="http://www.gutenberg.org/ebooks/27147" rel="nofollow">Le Queux, William</a></div>


</li>






<li class="entry learnable" id="entry625"
 lang="en" word="quip" freq="3314.52" prog="0">

<a class="word dynamictext" href="/dictionary/quip">quip</a>
<div class="definition">make jokes</div>
<div class="example">"I could have joined the FBI in a shorter period of time and with less documentation than it took to get that mortgage," she
<strong>quipped</strong>.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/topNews/~3/2rPI38wUawA/idUSTRE69C2OU20101013" rel="nofollow">Reuters (Oct 13, 2010)</a></div>


</li>






<li class="entry learnable" id="entry626"
 lang="en" word="blatant" freq="3325.7" prog="0">

<a class="word dynamictext" href="/dictionary/blatant">blatant</a>
<div class="definition">without any attempt at concealment; completely obvious</div>
<div class="example">There was no
<strong>blatant</strong> display of wealth, and every article of furniture bore signs of long though careful use.
<br> —
<a href="http://www.gutenberg.org/ebooks/29695" rel="nofollow">Bull, Charles Livingston</a></div>


</li>






<li class="entry learnable" id="entry627"
 lang="en" word="stanch" freq="3354.95" prog="0">

<a class="word dynamictext" href="/dictionary/stanch">stanch</a>
<div class="definition">stop the flow of a liquid</div>
<div class="example">She did not attempt to
<strong>stanch</strong> her tears, but sat looking at him with a smiling mouth, while the heavy drops fell down her cheeks.
<br> —
<a href="http://www.gutenberg.org/ebooks/36138" rel="nofollow">Stockley, Cynthia</a></div>


</li>






<li class="entry learnable" id="entry628"
 lang="en" word="incongruity" freq="3365.45" prog="0">

<a class="word dynamictext" href="/dictionary/incongruity">incongruity</a>
<div class="definition">the quality of disagreeing</div>
<div class="example">Hanging out wet clothes and an American flag at the North Pole seemed an amusing
<strong>incongruity</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/36962" rel="nofollow">Cook, Frederick A.</a></div>


</li>






<li class="entry learnable" id="entry629"
 lang="en" word="perfidious" freq="3367.37" prog="0">

<a class="word dynamictext" href="/dictionary/perfidious">perfidious</a>
<div class="definition">tending to betray</div>
<div class="example">The
<strong>perfidious</strong> Italian at length confessed that it was his intention to murder his master, and then rob the house.
<br> —
<a href="http://www.gutenberg.org/ebooks/24263" rel="nofollow">Billinghurst, Percy J.</a></div>


</li>






<li class="entry learnable" id="entry630"
 lang="en" word="platitude" freq="3370.24" prog="0">

<a class="word dynamictext" href="/dictionary/platitude">platitude</a>
<div class="definition">a trite or obvious remark</div>
<div class="example">But details are fuzzy and rebel leaders often resort to
<strong>platitudes</strong> when dismissing suggestions of discord, saying simply that "Libya is one tribe."
<br> —
<a href="http://online.wsj.com/article/SB10001424052702304887904576395143328336026.html?mod=fox_australian" rel="nofollow">Wall Street Journal (Jun 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry631"
 lang="en" word="revelry" freq="3374.09" prog="0">

<a class="word dynamictext" href="/dictionary/revelry">revelry</a>
<div class="definition">unrestrained merrymaking</div>
<div class="example">But all this
<strong>revelry</strong> — dancing, drinks, exuberant youth — can be hard to manage.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=a7b0c71e85ba7d3d881763c8ee78e2c8" rel="nofollow">New York Times (Jun 3, 2010)</a></div>


</li>






<li class="entry learnable" id="entry632"
 lang="en" word="delve" freq="3380.84" prog="0">

<a class="word dynamictext" href="/dictionary/delve">delve</a>
<div class="definition">turn up, loosen, or remove earth</div>
<div class="example">So she did what any reporter would do: she
<strong>delved</strong> into the scientific literature and talked to investigators.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=02ddc91106eba77ee0530e73729ea899" rel="nofollow">New York Times (Dec 27, 2010)</a></div>


</li>






<li class="entry learnable" id="entry633"
 lang="en" word="extenuate" freq="3386.65" prog="0">

<a class="word dynamictext" href="/dictionary/extenuate">extenuate</a>
<div class="definition">lessen or to try to lessen the seriousness or extent of</div>
<div class="example">Prosecutors often spend time weighing mitigating and
<strong>extenuating</strong> circumstances before deciding to seek the death penalty.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=9a6058b0f135758a48e101688a0c5739" rel="nofollow">Washington Post (Oct 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry634"
 lang="en" word="polemic" freq="3391.51" prog="0">

<a class="word dynamictext" href="/dictionary/polemic">polemic</a>
<div class="definition">a controversy, especially over a belief or dogma</div>
<div class="example">Would it be a
<strong>polemic</strong> that denounced Western imperialism for using cinema to undermine emerging nations like Kazakhstan?
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=bb986f3f6202fdc898243b216540dddb" rel="nofollow">New York Times (Oct 4, 2010)</a></div>


</li>






<li class="entry learnable" id="entry635"
 lang="en" word="enrapture" freq="3396.38" prog="0">

<a class="word dynamictext" href="/dictionary/enrapture">enrapture</a>
<div class="definition">hold spellbound</div>
<div class="example">I was delighted,
<strong>enraptured</strong>, beside myself--the world had disappeared in an instant.
<br> —
<a href="http://www.gutenberg.org/ebooks/34748" rel="nofollow">Spielhagen, Friedrich</a></div>


</li>






<li class="entry learnable" id="entry636"
 lang="en" word="virtuoso" freq="3403.22" prog="0">

<a class="word dynamictext" href="/dictionary/virtuoso">virtuoso</a>
<div class="definition">someone who is dazzlingly skilled in any field</div>
<div class="example">Each of the seven instrumentalists was a
<strong>virtuoso</strong> in his own right and had ample opportunity to prove it, often in long, soulful solos.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=3f00407ce1fbd757fd73b02b4fe924c9" rel="nofollow">New York Times (May 3, 2010)</a></div>


</li>






<li class="entry learnable" id="entry637"
 lang="en" word="glower" freq="3404.2" prog="0">

<a class="word dynamictext" href="/dictionary/glower">glower</a>
<div class="definition">look angry or sullen as if to signal disapproval</div>
<div class="example">A moment later he would collapse, sit
<strong>glowering</strong> in his chair, looking angrily at the carpet.
<br> —
<a href="http://www.gutenberg.org/ebooks/38489" rel="nofollow">Hecht, Ben</a></div>


</li>






<li class="entry learnable" id="entry638"
 lang="en" word="mundane" freq="3411.07" prog="0">

<a class="word dynamictext" href="/dictionary/mundane">mundane</a>
<div class="definition">found in the ordinary course of events</div>
<div class="example">Now, it would seem, that the Chinese are getting back to their everyday concerns, paying attention to events more
<strong>mundane</strong> and less cataclysmic.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6272e7ce4429a30b6ca8d955d43332df" rel="nofollow">New York Times (Mar 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry639"
 lang="en" word="fatuous" freq="3416.99" prog="0">

<a class="word dynamictext" href="/dictionary/fatuous">fatuous</a>
<div class="definition">devoid of intelligence</div>
<div class="example">They're too stupid, for one thing; they go on burning houses and breaking windows in their old
<strong>fatuous</strong> way.
<br> —
<a href="http://www.gutenberg.org/ebooks/37164" rel="nofollow">McKenna, Stephen</a></div>


</li>






<li class="entry learnable" id="entry640"
 lang="en" word="incorrigible" freq="3417.97" prog="0">

<a class="word dynamictext" href="/dictionary/incorrigible">incorrigible</a>
<div class="definition">impervious to correction by punishment</div>
<div class="example">She scolded and lectured her sister in vain; Cynthia was
<strong>incorrigible</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/33071" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry641"
 lang="en" word="postulate" freq="3420.94" prog="0">

<a class="word dynamictext" href="/dictionary/postulate">postulate</a>
<div class="definition">maintain or assert</div>
<div class="example">In fact, when Einstein formulated his cosmological vision, based on his theory of gravitation, he
<strong>postulated</strong> that the universe was finite.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=83e2f9846a500fbb013d3cc8fae43f22" rel="nofollow">Scientific American (Jul 26, 2011)</a></div>


</li>






<li class="entry learnable" id="entry642"
 lang="en" word="gist" freq="3440.85" prog="0">

<a class="word dynamictext" href="/dictionary/gist">gist</a>
<div class="definition">the central meaning or theme of a speech or literary work</div>
<div class="example">The syntax was a little off, even comical at times, but I got the
<strong>gist</strong> of what was going on.
<br> —
<a href="http://feedproxy.google.com/~r/time/business/~3/iHcQWUyymzU/0,8599,1987492,00.html" rel="nofollow">Time (May 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry643"
 lang="en" word="vociferous" freq="3451.89" prog="0">

<a class="word dynamictext" href="/dictionary/vociferous">vociferous</a>
<div class="definition">conspicuously and offensively loud</div>
<div class="example">The complaints grew so loud and
<strong>vociferous</strong> that even President Obama was forced to address the backlash from Lisbon on Saturday.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=12a1730d83b3c97d956ee62db5219d8d" rel="nofollow">New York Times (Nov 23, 2010)</a></div>


</li>






<li class="entry learnable" id="entry644"
 lang="en" word="purvey" freq="3466.06" prog="0">

<a class="word dynamictext" href="/dictionary/purvey">purvey</a>
<div class="definition">supply with provisions</div>
<div class="example">And we will agree also to
<strong>purvey</strong> food for these horses and people during nine months.
<br> —
<a href="http://www.gutenberg.org/ebooks/6032" rel="nofollow">Villehardouin, Geoffroi de</a></div>


</li>






<li class="entry learnable" id="entry645"
 lang="en" word="baleful" freq="3466.06" prog="0">

<a class="word dynamictext" href="/dictionary/baleful">baleful</a>
<div class="definition">deadly or sinister</div>
<div class="example">“But he is dead,” put in Fanning, wondering at the
<strong>baleful</strong> expression of hatred that had come into the man’s face.
<br> —
<a href="http://www.gutenberg.org/ebooks/33605" rel="nofollow">Burnham, Margaret</a></div>


</li>






<li class="entry learnable" id="entry646"
 lang="en" word="gibe" freq="3472.16" prog="0">

<a class="word dynamictext" href="/dictionary/gibe">gibe</a>
<div class="definition">laugh at with contempt and derision</div>
<div class="example">So much did their taunts prey upon him that he ran away from school to escape their
<strong>gibes</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/23595" rel="nofollow">Hubbard, Elbert</a></div>


</li>






<li class="entry learnable" id="entry647"
 lang="en" word="dyspeptic" freq="3473.18" prog="0">

<a class="word dynamictext" href="/dictionary/dyspeptic">dyspeptic</a>
<div class="definition">irritable as if suffering from indigestion</div>
<div class="example">One may begin with heroic renunciations and end in undignified envy and
<strong>dyspeptic</strong> comments outside the door one has slammed on one's self.
<br> —
<a href="http://www.gutenberg.org/ebooks/7058" rel="nofollow">Wells, H. G. (Herbert George)</a></div>


</li>






<li class="entry learnable" id="entry648"
 lang="en" word="prude" freq="3475.22" prog="0">

<a class="word dynamictext" href="/dictionary/prude">prude</a>
<div class="definition">a person excessively concerned about propriety and decorum</div>
<div class="example">Criticising high-profile programmes about teenage sex education often means risking being written off as a
<strong>prude</strong>.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2011/feb/11/joy-of-teen-sex-channel-4" rel="nofollow">The Guardian (Feb 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry649"
 lang="en" word="luminary" freq="3477.27" prog="0">

<a class="word dynamictext" href="/dictionary/luminary">luminary</a>
<div class="definition">a celebrity who is an inspiration to others</div>
<div class="example">Founded in 1947, the group's members have included such
<strong>luminaries</strong> as Walt Disney, Spencer Tracy and another American president, Ronald Reagan.
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2014741180_apusamericanfoxhunting.html?syndication=rss" rel="nofollow">Seattle Times (Apr 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry650"
 lang="en" word="amenable" freq="3480.34" prog="0">

<a class="word dynamictext" href="/dictionary/amenable">amenable</a>
<div class="definition">disposed or willing to comply</div>
<div class="example">He, Jean Boulot, being so
<strong>amenable</strong> to sensible argument, would at once fall in with his views.
<br> —
<a href="http://www.gutenberg.org/ebooks/38854" rel="nofollow">Wingfield, Lewis</a></div>


</li>






<li class="entry learnable" id="entry651"
 lang="en" word="willful" freq="3493.7" prog="0">

<a class="word dynamictext" href="/dictionary/willful">willful</a>
<div class="definition">habitually disposed to disobedience and opposition</div>
<div class="example">I crossed my arms like a
<strong>willful</strong> child.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=65d7e9a510cdeb29afd2e92a8aa7f9c5" rel="nofollow">New York Times (Aug 18, 2011)</a></div>


</li>






<li class="entry learnable" id="entry652"
 lang="en" word="overbearing" freq="3504.06" prog="0">

<a class="word dynamictext" href="/dictionary/overbearing">overbearing</a>
<div class="definition">having or showing arrogant superiority to</div>
<div class="example">"True; but——" "Just so," interrupted Mr. Fauntleroy, in his decisive and rather
<strong>overbearing</strong> manner.
<br> —
<a href="http://www.gutenberg.org/ebooks/39377" rel="nofollow">Wood, Mrs. Henry</a></div>


</li>






<li class="entry learnable" id="entry653"
 lang="en" word="dais" freq="3514.47" prog="0">

<a class="word dynamictext" href="/dictionary/dais">dais</a>
<div class="definition">a platform raised above the surrounding level</div>
<div class="example">The throne was elevated on a
<strong>dais</strong> of silver steps.
<br> —
<a href="http://www.gutenberg.org/ebooks/34134" rel="nofollow">Tracy, Louis</a></div>


</li>






<li class="entry learnable" id="entry654"
 lang="en" word="automate" freq="3516.56" prog="0">

<a class="word dynamictext" href="/dictionary/automate">automate</a>
<div class="definition">operate or make run by machines rather than human action</div>
<div class="example">And because leap seconds are needed irregularly their insertion cannot be
<strong>automated</strong>, which means that fallible humans must insert them by hand.
<br> —
<a href="http://www.economist.com/node/21542717?fsrc=rss|sct" rel="nofollow">Economist (Jan 12, 2012)</a></div>


</li>






<li class="entry learnable" id="entry655"
 lang="en" word="enervate" freq="3523.89" prog="0">

<a class="word dynamictext" href="/dictionary/enervate">enervate</a>
<div class="definition">weaken mentally or morally</div>
<div class="example">The reviewers have
<strong>enervated</strong> men’s minds, and made them indolent; few think for themselves.
<br> —
<a href="http://www.gutenberg.org/ebooks/31682" rel="nofollow">Rossetti, William Michael</a></div>


</li>






<li class="entry learnable" id="entry656"
 lang="en" word="wheedle" freq="3530.21" prog="0">

<a class="word dynamictext" href="/dictionary/wheedle">wheedle</a>
<div class="definition">influence or urge by gentle urging, caressing, or flattering</div>
<div class="example">On one level, I expected incessant flattery in attempts to
<strong>wheedle</strong> equipment or even money from American forces.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=35a86709a8525a925d1fc71cc8f0bf39" rel="nofollow">New York Times (Aug 16, 2010)</a></div>


</li>






<li class="entry learnable" id="entry657"
 lang="en" word="gusto" freq="3549.28" prog="0">

<a class="word dynamictext" href="/dictionary/gusto">gusto</a>
<div class="definition">vigorous and enthusiastic enjoyment</div>
<div class="example">The audience, surprisingly large given the inclement weather, responded with
<strong>gusto</strong>, applauding each song, including those within the Shostakovich cycle.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4d9d3201c9545f7bcbdf2a19d88a775f" rel="nofollow">New York Times (Mar 2, 2010)</a></div>


</li>






<li class="entry learnable" id="entry658"
 lang="en" word="bouillon" freq="3551.41" prog="0">

<a class="word dynamictext" href="/dictionary/bouillon">bouillon</a>
<div class="definition">a clear seasoned broth</div>
<div class="example">The meat soups are called broths,
<strong>bouillon</strong>, or consommé, according to their richness.
<br> —
<a href="http://www.gutenberg.org/ebooks/34822" rel="nofollow">Ronald, Mary</a></div>


</li>






<li class="entry learnable" id="entry659"
 lang="en" word="omniscient" freq="3562.11" prog="0">

<a class="word dynamictext" href="/dictionary/omniscient">omniscient</a>
<div class="definition">infinitely wise</div>
<div class="example">Robbe-Grillet responds that his work is in fact far less objective than the godlike,
<strong>omniscient</strong> narrator who presides over so many traditional novels.
<br> —
<a href="http://www.guardian.co.uk/books/booksblog/2010/may/13/in-theory-alain-robbe-grillet-fiction" rel="nofollow">The Guardian (May 13, 2010)</a></div>


</li>






<li class="entry learnable" id="entry660"
 lang="en" word="apostate" freq="3579.36" prog="0">

<a class="word dynamictext" href="/dictionary/apostate">apostate</a>
<div class="definition">not faithful to religion or party or cause</div>
<div class="example">They are atheist conservatives — Mr. Khan an
<strong>apostate</strong> to his family’s Islamic faith, Ms. Mac Donald to her left-wing education.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=55d71e8323220e5f21469e8cf6309fa9" rel="nofollow">New York Times (Feb 18, 2011)</a></div>


</li>






<li class="entry learnable" id="entry661"
 lang="en" word="carrion" freq="3589.13" prog="0">

<a class="word dynamictext" href="/dictionary/carrion">carrion</a>
<div class="definition">the dead and rotting body of an animal; unfit for human food</div>
<div class="example">Habitually his diet is not carnivorous, but he will eat at times either
<strong>carrion</strong> or living flesh.
<br> —
<a href="http://www.gutenberg.org/ebooks/23499" rel="nofollow">Reid, Mayne</a></div>


</li>






<li class="entry learnable" id="entry662"
 lang="en" word="emolument" freq="3601.16" prog="0">

<a class="word dynamictext" href="/dictionary/emolument">emolument</a>
<div class="definition">compensation received by virtue of holding an office</div>
<div class="example">As the TUC has pointed out, those incomes – except for senior executives, whose
<strong>emoluments</strong> seem to know few bounds – are rising more slowly than prices.
<br> —
<a href="http://www.guardian.co.uk/business/2011/jan/09/william-keegan-tory-policy-on-tax" rel="nofollow">The Guardian (Jan 8, 2011)</a></div>


</li>






<li class="entry learnable" id="entry663"
 lang="en" word="ungainly" freq="3603.35" prog="0">

<a class="word dynamictext" href="/dictionary/ungainly">ungainly</a>
<div class="definition">lacking grace in movement or posture</div>
<div class="example">Thomas looked up furtively and saw that an
<strong>ungainly</strong> human figure with crooked legs was being led into the church.
<br> —
<a href="http://www.gutenberg.org/ebooks/36238" rel="nofollow">Gogol, Nikolai Vasilievich</a></div>


</li>






<li class="entry learnable" id="entry664"
 lang="en" word="impiety" freq="3634.36" prog="0">

<a class="word dynamictext" href="/dictionary/impiety">impiety</a>
<div class="definition">unrighteousness by virtue of lacking respect for a god</div>
<div class="example">That, however, is unbelief, extreme
<strong>impiety</strong>, and a denial of the most high God.
<br> —
<a href="http://www.gutenberg.org/ebooks/26909" rel="nofollow">Bente, F. (Friedrich)</a></div>


</li>






<li class="entry learnable" id="entry665"
 lang="en" word="decadence" freq="3636.59" prog="0">

<a class="word dynamictext" href="/dictionary/decadence">decadence</a>
<div class="definition">the state of being degenerate in mental or moral qualities</div>
<div class="example">But there are people who really do not want to import what they regard as Western
<strong>decadence</strong>, especially public drunkenness.
<br> —
<a href="http://news.bbc.co.uk/go/rss/int/news/-/2/hi/programmes/from_our_own_correspondent/9510135.stm" rel="nofollow">BBC (Jun 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry666"
 lang="en" word="homily" freq="3642.19" prog="0">

<a class="word dynamictext" href="/dictionary/homily">homily</a>
<div class="definition">a sermon on a moral or religious topic</div>
<div class="example">In his New Year's
<strong>homily</strong>, the pope said "words were not enough" to bring about peace, particularly in the Middle East.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/topNews/~3/VNxXhOy64jE/idUSTRE7010GO20110102" rel="nofollow">Reuters (Jan 2, 2011)</a></div>


</li>






<li class="entry learnable" id="entry667"
 lang="en" word="avocation" freq="3657.96" prog="0">

<a class="word dynamictext" href="/dictionary/avocation">avocation</a>
<div class="definition">an auxiliary activity</div>
<div class="example">Unlike many retired doctors, whom he says often have no life outside their profession, he always knew sailing would become his
<strong>avocation</strong>.
<br> —
<a href="http://feeds.newsweek.com/~r/newsweek/NationalNews/~3/m9gUkJaGk4E/firms-help-retirees-plan-second-careers" rel="nofollow">Newsweek (Nov 17, 2010)</a></div>


</li>






<li class="entry learnable" id="entry668"
 lang="en" word="circumvent" freq="3692.23" prog="0">

<a class="word dynamictext" href="/dictionary/circumvent">circumvent</a>
<div class="definition">avoid or try to avoid fulfilling, answering, or performing</div>
<div class="example">Mr. Bloomberg said he would take several steps to
<strong>circumvent</strong> obstacles to his proposals posed by city labor unions.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e668f6ae6ba0ae8e359ac5aa88258565" rel="nofollow">New York Times (Jan 12, 2012)</a></div>


</li>






<li class="entry learnable" id="entry669"
 lang="en" word="syllogism" freq="3695.69" prog="0">

<a class="word dynamictext" href="/dictionary/syllogism">syllogism</a>
<div class="definition">reasoning in which a conclusion is derived from two premises</div>
<div class="example">The conclusions arrived at by means of
<strong>syllogisms</strong> are irresistible, provided the form be correct and the premises be true.
<br> —
<a href="http://www.gutenberg.org/ebooks/28097" rel="nofollow">Webster, W. F. (William Franklin)</a></div>


</li>






<li class="entry learnable" id="entry670"
 lang="en" word="collation" freq="3718.93" prog="0">

<a class="word dynamictext" href="/dictionary/collation">collation</a>
<div class="definition">assembling in proper numerical or logical sequence</div>
<div class="example">In the case of early printed books or manuscripts, which are often not paged, special knowledge is needed for their
<strong>collation</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/26672" rel="nofollow">Rooke, Noel</a></div>


</li>






<li class="entry learnable" id="entry671"
 lang="en" word="haggle" freq="3721.27" prog="0">

<a class="word dynamictext" href="/dictionary/haggle">haggle</a>
<div class="definition">wrangle, as over a price or terms of an agreement</div>
<div class="example">Obama said while officials can
<strong>haggle</strong> over the makeup of spending cuts, the policy issues have no place in the measure.
<br> —
<a href="http://www.businessweek.com/news/2011-04-06/congress-leaders-fight-clock-for-spending-deal-to-avert-shutdown.html" rel="nofollow">BusinessWeek (Apr 6, 2011)</a></div>


</li>






<li class="entry learnable" id="entry672"
 lang="en" word="waylay" freq="3728.31" prog="0">

<a class="word dynamictext" href="/dictionary/waylay">waylay</a>
<div class="definition">wait in hiding to attack</div>
<div class="example">Sir Samuel Clithering was not, of course, a member of it; but he lurked about outside and
<strong>waylaid</strong> us as we went in.
<br> —
<a href="http://www.gutenberg.org/ebooks/29533" rel="nofollow">Birmingham, George A.</a></div>


</li>






<li class="entry learnable" id="entry673"
 lang="en" word="savant" freq="3731.84" prog="0">

<a class="word dynamictext" href="/dictionary/savant">savant</a>
<div class="definition">a learned person</div>
<div class="example">Frank had studied something of almost everything and imagined himself a
<strong>savant</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/27798" rel="nofollow">Roussel, John</a></div>


</li>






<li class="entry learnable" id="entry674"
 lang="en" word="cohort" freq="3733.02" prog="0">

<a class="word dynamictext" href="/dictionary/cohort">cohort</a>
<div class="definition">a group of people having approximately the same age</div>
<div class="example">The current
<strong>cohort</strong> of college students is, as many have pointed out, the first truly digital generation.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=92151e2d2deb97d3c861ff4ffc8caf91" rel="nofollow">Washington Post (Dec 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry675"
 lang="en" word="unction" freq="3736.56" prog="0">

<a class="word dynamictext" href="/dictionary/unction">unction</a>
<div class="definition">excessive but superficial compliments with affected charm</div>
<div class="example">"You couldn't ask too much of me," he returned, with no
<strong>unction</strong> of flattery, but the cheerfully frank expression of an ingenuous heart.
<br> —
<a href="http://www.gutenberg.org/ebooks/20712" rel="nofollow">Ogden, George W. (George Washington)</a></div>


</li>






<li class="entry learnable" id="entry676"
 lang="en" word="adjure" freq="3740.1" prog="0">

<a class="word dynamictext" href="/dictionary/adjure">adjure</a>
<div class="definition">command solemnly</div>
<div class="example">“I
<strong>adjure</strong> thee,” she said, “swear to me that you will never go near those Christians again or read their books.”
<br> —
<a href="http://www.gutenberg.org/ebooks/32231" rel="nofollow">Pennell, T. L. (Theodore Leighton)</a></div>


</li>






<li class="entry learnable" id="entry677"
 lang="en" word="acrimony" freq="3742.47" prog="0">

<a class="word dynamictext" href="/dictionary/acrimony">acrimony</a>
<div class="definition">a rough and bitter manner</div>
<div class="example">Relations with India have been slowly improving, although talks ended in
<strong>acrimony</strong> last July with the two sides indulging in a public spat over Kashmir.
<br> —
<a href="http://www.bbc.co.uk/go/rss/int/news/-/news/world-south-asia-12416441" rel="nofollow">BBC (Feb 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry678"
 lang="en" word="clarion" freq="3744.84" prog="0">

<a class="word dynamictext" href="/dictionary/clarion">clarion</a>
<div class="definition">loud and clear</div>
<div class="example">“He has been the single,
<strong>clarion</strong> voice for commuter rail in central Florida for 20 years,” said Mayor Ken Bradley of Winter Park.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=5b1526ff538f5c7e02dd025de9b9017f" rel="nofollow">New York Times (Jun 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry679"
 lang="en" word="turbid" freq="3753.16" prog="0">

<a class="word dynamictext" href="/dictionary/turbid">turbid</a>
<div class="definition">clouded as with sediment</div>
<div class="example">The thick
<strong>turbid</strong> sea rolled in, casting up mire and dirt from its depths.
<br> —
<a href="http://www.gutenberg.org/ebooks/39366" rel="nofollow">Reynolds, Mrs. Baillie</a></div>


</li>






<li class="entry learnable" id="entry680"
 lang="en" word="cupidity" freq="3756.74" prog="0">

<a class="word dynamictext" href="/dictionary/cupidity">cupidity</a>
<div class="definition">extreme greed for material wealth</div>
<div class="example">Well educated, but very corrupt at heart, he found in his insatiable
<strong>cupidity</strong> many ways of gaining money.
<br> —
<a href="http://www.gutenberg.org/ebooks/37621" rel="nofollow">Kraszewski, Jozef Ignacy</a></div>


</li>






<li class="entry learnable" id="entry681"
 lang="en" word="disaffected" freq="3766.31" prog="0">

<a class="word dynamictext" href="/dictionary/disaffected">disaffected</a>
<div class="definition">discontented as toward authority</div>
<div class="example">The financial crisis, largely caused by banker incompetence, has created legions of
<strong>disaffected</strong> customers.
<br> —
<a href="http://www.forbes.com/sites/tomanderson/2011/09/15/welcome-to-the-moneyness/" rel="nofollow">Forbes (Sep 15, 2011)</a></div>


</li>






<li class="entry learnable" id="entry682"
 lang="en" word="preternatural" freq="3767.51" prog="0">

<a class="word dynamictext" href="/dictionary/preternatural">preternatural</a>
<div class="definition">surpassing the ordinary or normal</div>
<div class="example">In fact, they regarded the Spaniards as superior beings endowed with
<strong>preternatural</strong> gifts.
<br> —
<a href="http://www.gutenberg.org/ebooks/23546" rel="nofollow">Gilson, Jewett Castello</a></div>


</li>






<li class="entry learnable" id="entry683"
 lang="en" word="eschew" freq="3772.32" prog="0">

<a class="word dynamictext" href="/dictionary/eschew">eschew</a>
<div class="definition">avoid and stay away from deliberately</div>
<div class="example">Morrissey is among those seniors who are
<strong>eschewing</strong> nursing homes in favor of independent living.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=afbe761baff8ce39b86956b148f46aac" rel="nofollow">Washington Post (Mar 23, 2012)</a></div>


</li>






<li class="entry learnable" id="entry684"
 lang="en" word="expatiate" freq="3779.55" prog="0">

<a class="word dynamictext" href="/dictionary/expatiate">expatiate</a>
<div class="definition">add details, as to an account or idea</div>
<div class="example">He then
<strong>expatiated</strong> on his own miseries, which he detailed at full length.
<br> —
<a href="http://www.gutenberg.org/ebooks/35155" rel="nofollow">Manzoni, Alessandro</a></div>


</li>






<li class="entry learnable" id="entry685"
 lang="en" word="didactic" freq="3784.39" prog="0">

<a class="word dynamictext" href="/dictionary/didactic">didactic</a>
<div class="definition">instructive, especially excessively</div>
<div class="example">Let us have a book so full of good illustrations that
<strong>didactic</strong> instruction shall not be needed.
<br> —
<a href="http://www.gutenberg.org/ebooks/32617" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry686"
 lang="en" word="sinuous" freq="3788.03" prog="0">

<a class="word dynamictext" href="/dictionary/sinuous">sinuous</a>
<div class="definition">curved or curving in and out</div>
<div class="example">In origami parlance, Mr. Joisel was a wet-folder, dampening his paper so that he could coax it into
<strong>sinuous</strong> curves.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1e518ec15bc1d00a016d625c536094f4" rel="nofollow">New York Times (Oct 20, 2010)</a></div>


</li>






<li class="entry learnable" id="entry687"
 lang="en" word="rancor" freq="3788.03" prog="0">

<a class="word dynamictext" href="/dictionary/rancor">rancor</a>
<div class="definition">a feeling of deep and bitter anger and ill-will</div>
<div class="example">The current session of Parliament has so far produced only
<strong>rancor</strong>, as opposition parties have shut down proceedings with angry, theatrical protests against corruption.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=ccc629402fc73a674370e8f52f6ecb0b" rel="nofollow">New York Times (Aug 14, 2011)</a></div>


</li>






<li class="entry learnable" id="entry688"
 lang="en" word="puissant" freq="3794.1" prog="0">

<a class="word dynamictext" href="/dictionary/puissant">puissant</a>
<div class="definition">powerful</div>
<div class="example">The ship was not fighting now, but yielding—a complacent leviathan held captive by a most
<strong>puissant</strong> and ruthless enemy.
<br> —
<a href="http://www.gutenberg.org/ebooks/35074" rel="nofollow">Tracy, Louis</a></div>


</li>






<li class="entry learnable" id="entry689"
 lang="en" word="homespun" freq="3801.42" prog="0">

<a class="word dynamictext" href="/dictionary/homespun">homespun</a>
<div class="definition">characteristic of country life</div>
<div class="example">His rural,
<strong>homespun</strong> demeanor ordinarily might elicit snickers from India’s urban elite.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e55a98bb055a0cc09bd4d96f63e0beea" rel="nofollow">New York Times (Aug 18, 2011)</a></div>


</li>






<li class="entry learnable" id="entry690"
 lang="en" word="embroil" freq="3845.93" prog="0">

<a class="word dynamictext" href="/dictionary/embroil">embroil</a>
<div class="definition">force into some kind of situation or course of action</div>
<div class="example">But Mr. Marbury, often
<strong>embroiled</strong> in controversy during his N.B.A. days, seems to have found some measure of peace in China.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=3304e59ad32e560403e3d6c37903c769" rel="nofollow">New York Times (Apr 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry691"
 lang="en" word="pathological" freq="3848.43" prog="0">

<a class="word dynamictext" href="/dictionary/pathological">pathological</a>
<div class="definition">caused by or evidencing a mentally disturbed condition</div>
<div class="example">"Fixated individuals" — mentally ill people with a
<strong>pathological</strong> focus on someone, often a stranger — make up the first group.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/8iDHl0rvZlw/0,8599,2067303,00.html" rel="nofollow">Time (Apr 26, 2011)</a></div>


</li>






<li class="entry learnable" id="entry692"
 lang="en" word="resonant" freq="2023.82" prog="0">

<a class="word dynamictext" href="/dictionary/resonant">resonant</a>
<div class="definition">characterized by a loud deep sound</div>
<div class="example">His eyes were piercing but sad, his voice grand and
<strong>resonant</strong>, suiting well the wrathful, impassioned Calvinism of his sermons.
<br> —
<a href="http://www.gutenberg.org/ebooks/36538" rel="nofollow">Barr, Amelia Edith Huddleston</a></div>


</li>






<li class="entry learnable" id="entry693"
 lang="en" word="libretto" freq="3877.45" prog="0">

<a class="word dynamictext" href="/dictionary/libretto">libretto</a>
<div class="definition">the words of an opera or musical play</div>
<div class="example">In many great operas, composers have had to whittle down an epic literary work into a suitable
<strong>libretto</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4f637373e2bf80fb5e06c440478b21cf" rel="nofollow">New York Times (Mar 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry694"
 lang="en" word="flail" freq="3886.38" prog="0">

<a class="word dynamictext" href="/dictionary/flail">flail</a>
<div class="definition">thresh about</div>
<div class="example">Exercise is prescribed, but when she joins an aqua aerobics class, she
<strong>flails</strong> embarrassingly.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=6cc29a41f32580aa19f81acd0bda6e6d" rel="nofollow">New York Times (Apr 12, 2012)</a></div>


</li>






<li class="entry learnable" id="entry695"
 lang="en" word="bandy" freq="3888.93" prog="0">

<a class="word dynamictext" href="/dictionary/bandy">bandy</a>
<div class="definition">discuss lightly</div>
<div class="example">Hillary Clinton’s name has been
<strong>bandied</strong> about, but she’s made it clear she’s not interested.
<br> —
<a href="http://feedproxy.google.com/~r/time/business/~3/ZQa9JBjr3d0/" rel="nofollow">Time (Mar 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry696"
 lang="en" word="gratis" freq="3906.92" prog="0">

<a class="word dynamictext" href="/dictionary/gratis">gratis</a>
<div class="definition">costing nothing</div>
<div class="example">"Would you admit them
<strong>gratis</strong>?" asked Mr. Castlemaine with a smile, "or would they have to pay, like ordinary residents in an hotel?"
<br> —
<a href="http://www.gutenberg.org/ebooks/33964" rel="nofollow">Hocking, Joseph</a></div>


</li>






<li class="entry learnable" id="entry697"
 lang="en" word="upshot" freq="3912.09" prog="0">

<a class="word dynamictext" href="/dictionary/upshot">upshot</a>
<div class="definition">a phenomenon that is caused by some previous phenomenon</div>
<div class="example">The inevitable
<strong>upshot</strong> of their growing social power was that brands wanted an expanded visual presence.
<br> —
<a href="http://www.guardian.co.uk/artanddesign/2010/jul/27/boris-johnson-london-cycle-hire-barclays" rel="nofollow">The Guardian (Jul 27, 2010)</a></div>


</li>






<li class="entry learnable" id="entry698"
 lang="en" word="aphorism" freq="3918.57" prog="0">

<a class="word dynamictext" href="/dictionary/aphorism">aphorism</a>
<div class="definition">a short pithy instructive saying</div>
<div class="example">General Sherman's famous
<strong>aphorism</strong> that "War is Hell," has become classic.
<br> —
<a href="http://www.gutenberg.org/ebooks/35692" rel="nofollow">Fletcher, Samuel H.</a></div>


</li>






<li class="entry learnable" id="entry699"
 lang="en" word="redoubtable" freq="3922.47" prog="0">

<a class="word dynamictext" href="/dictionary/redoubtable">redoubtable</a>
<div class="definition">worthy of respect or honor</div>
<div class="example">Captain Miles Standish was a
<strong>redoubtable</strong> soldier, small in person, but of great activity and courage.
<br> —
<a href="http://www.gutenberg.org/ebooks/20105" rel="nofollow">Mann, Henry</a></div>


</li>






<li class="entry learnable" id="entry700"
 lang="en" word="corpulent" freq="3951.3" prog="0">

<a class="word dynamictext" href="/dictionary/corpulent">corpulent</a>
<div class="definition">excessively fat</div>
<div class="example">Obesity is very common, but chiefly among the women, who while still quite young often become enormously
<strong>corpulent</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/26658" rel="nofollow">D'Anvers, N.</a></div>


</li>






<li class="entry learnable" id="entry701"
 lang="en" word="benighted" freq="3965.88" prog="0">

<a class="word dynamictext" href="/dictionary/benighted">benighted</a>
<div class="definition">lacking enlightenment or knowledge or culture</div>
<div class="example">I alone was magnificently and absurdly aware—everyone else was
<strong>benightedly</strong> out of it.
<br> —
<a href="http://www.gutenberg.org/ebooks/32939" rel="nofollow">James, Henry</a></div>


</li>






<li class="entry learnable" id="entry702"
 lang="en" word="sententious" freq="3968.54" prog="0">

<a class="word dynamictext" href="/dictionary/sententious">sententious</a>
<div class="definition">abounding in or given to pompous or aphoristic moralizing</div>
<div class="example">He is the village wise man; very
<strong>sententious</strong>; and full of profound remarks on shallow subjects.
<br> —
<a href="http://www.gutenberg.org/ebooks/14228" rel="nofollow">Irving, Washington</a></div>


</li>






<li class="entry learnable" id="entry703"
 lang="en" word="cabal" freq="3013.82" prog="0">

<a class="word dynamictext" href="/dictionary/cabal">cabal</a>
<div class="definition">a clique that seeks power usually through intrigue</div>
<div class="example">Supposedly, see, there's this global
<strong>cabal</strong> of scientists conspiring to bring about socialist one-world government.
<br> —
<a href="http://www.salon.com/news/feature/2010/07/07/gene_lyons_climategate/index.html" rel="nofollow">Salon (Jul 7, 2010)</a></div>


</li>






<li class="entry learnable" id="entry704"
 lang="en" word="paraphernalia" freq="3994.01" prog="0">

<a class="word dynamictext" href="/dictionary/paraphernalia">paraphernalia</a>
<div class="definition">equipment consisting of miscellaneous articles</div>
<div class="example">It's outfitted with cricket bats and other antique sports
<strong>paraphernalia</strong>.
<br> —
<a href="http://seattletimes.nwsource.com/html/restaurants/2016336267_happyhour28.html?syndication=rss" rel="nofollow">Seattle Times (Sep 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry705"
 lang="en" word="vitiate" freq="4008.9" prog="0">

<a class="word dynamictext" href="/dictionary/vitiate">vitiate</a>
<div class="definition">make imperfect</div>
<div class="example">His talent in writing is
<strong>vitiated</strong> by his affectation and other faults.
<br> —
<a href="http://www.gutenberg.org/ebooks/30253" rel="nofollow">Blair, Emma Helen</a></div>


</li>






<li class="entry learnable" id="entry706"
 lang="en" word="adulation" freq="4008.9" prog="0">

<a class="word dynamictext" href="/dictionary/adulation">adulation</a>
<div class="definition">servile flattery; exaggerated and hypocritical praise</div>
<div class="example">And celebrities get all this
<strong>adulation</strong> for something that is not about character, it's about talent.
<br> —
<a href="http://www.salon.com/news/feature/2011/01/10/child_health_poverty_genetics/index.html" rel="nofollow">Salon (Jan 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry707"
 lang="en" word="quaff" freq="4019.81" prog="0">

<a class="word dynamictext" href="/dictionary/quaff">quaff</a>
<div class="definition">to swallow hurriedly or greedily or in one draught</div>
<div class="example">Meanwhile the officers under the tree had got served, and, cups in hand, were
<strong>quaffing</strong> joyously.
<br> —
<a href="http://www.gutenberg.org/ebooks/35670" rel="nofollow">Reid, Mayne</a></div>


</li>






<li class="entry learnable" id="entry708"
 lang="en" word="unassuming" freq="4019.81" prog="0">

<a class="word dynamictext" href="/dictionary/unassuming">unassuming</a>
<div class="definition">not arrogant</div>
<div class="example">Parr's conduct after his most heroic actions was thoroughly modest and
<strong>unassuming</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/39108" rel="nofollow">Greely, Adolphus W.</a></div>


</li>






<li class="entry learnable" id="entry709"
 lang="en" word="libertine" freq="4026.65" prog="0">

<a class="word dynamictext" href="/dictionary/libertine">libertine</a>
<div class="definition">a dissolute person</div>
<div class="example">Still, Mr. Awlaki was neither among the most conservative Muslim students nor among the
<strong>libertines</strong> who tossed aside religious restrictions on drinking and sex.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=256857a404ae7bc7daa7fe63e3277660" rel="nofollow">New York Times (May 8, 2010)</a></div>


</li>






<li class="entry learnable" id="entry710"
 lang="en" word="maul" freq="4033.52" prog="0">

<a class="word dynamictext" href="/dictionary/maul">maul</a>
<div class="definition">injure badly</div>
<div class="example">Hundreds of concert goers were
<strong>mauled</strong> as they left by what The New York Times called “bands of roving youths.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4c68082ffbd862eb1f2660e34312bda5" rel="nofollow">New York Times (Aug 17, 2011)</a></div>


</li>






<li class="entry learnable" id="entry711"
 lang="en" word="adage" freq="4039.03" prog="0">

<a class="word dynamictext" href="/dictionary/adage">adage</a>
<div class="definition">a condensed but memorable saying embodying an important fact</div>
<div class="example">So he focuses on the fans and embraces the
<strong>adage</strong>, “Living well is the best revenge.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1a60e054d6b1c66e703234631ba12541" rel="nofollow">New York Times (Mar 25, 2011)</a></div>


</li>






<li class="entry learnable" id="entry712"
 lang="en" word="expostulation" freq="4040.41" prog="0">

<a class="word dynamictext" href="/dictionary/expostulation">expostulation</a>
<div class="definition">the act of expressing earnest opposition or protest</div>
<div class="example">He even believed he saw visions with his own bodily eyes, and no
<strong>expostulations</strong> of his friends could drive this belief out of his head.
<br> —
<a href="http://www.gutenberg.org/ebooks/31439" rel="nofollow">Hoffmann, E. T. A. (Ernst Theodor Amadeus)</a></div>


</li>






<li class="entry learnable" id="entry713"
 lang="en" word="tawdry" freq="4048.71" prog="0">

<a class="word dynamictext" href="/dictionary/tawdry">tawdry</a>
<div class="definition">tastelessly showy</div>
<div class="example">It was a
<strong>tawdry</strong> affair, all Cupids and cornucopias, like a third-rate wedding cake.
<br> —
<a href="http://www.gutenberg.org/ebooks/26740" rel="nofollow">Wilde, Oscar</a></div>


</li>






<li class="entry learnable" id="entry714"
 lang="en" word="trite" freq="4050.1" prog="0">

<a class="word dynamictext" href="/dictionary/trite">trite</a>
<div class="definition">repeated too often; overfamiliar through overuse</div>
<div class="example">The subject—a deathbed scene—might seem at first sight to be a
<strong>trite</strong> and common one.
<br> —
<a href="http://www.gutenberg.org/ebooks/31517" rel="nofollow">Lancey, Magdalene de</a></div>


</li>






<li class="entry learnable" id="entry715"
 lang="en" word="hireling" freq="4052.87" prog="0">

<a class="word dynamictext" href="/dictionary/hireling">hireling</a>
<div class="definition">a person who works only for money</div>
<div class="example">Why should I?—a mere police detective, who had been hired to do a service and paid for it like any other
<strong>hireling</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/32198" rel="nofollow">Hanshew, Thomas W.</a></div>


</li>






<li class="entry learnable" id="entry716"
 lang="en" word="ensconce" freq="4057.04" prog="0">

<a class="word dynamictext" href="/dictionary/ensconce">ensconce</a>
<div class="definition">fix firmly</div>
<div class="example">Though she is firmly
<strong>ensconced</strong> in a writing career, Ms. Freud, 48, said that in the early days she missed acting terribly.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=d9ec7bbf0ac5701ac421b500e6504890" rel="nofollow">New York Times (Oct 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry717"
 lang="en" word="egregious" freq="4086.49" prog="0">

<a class="word dynamictext" href="/dictionary/egregious">egregious</a>
<div class="definition">conspicuously and outrageously bad or reprehensible</div>
<div class="example">“These offenses are very serious, even
<strong>egregious</strong>,” the judge said.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=41d96f4ef1393e6fecf3bbeb8dffc8c9" rel="nofollow">Washington Post (Sep 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry718"
 lang="en" word="cogent" freq="4099.24" prog="0">

<a class="word dynamictext" href="/dictionary/cogent">cogent</a>
<div class="definition">powerfully persuasive</div>
<div class="example">His thesis was too
<strong>cogent</strong>, and appealed too powerfully to all classes of the Upper Canada community, to be anything but irresistible.
<br> —
<a href="http://www.gutenberg.org/ebooks/31363" rel="nofollow">Morison, J. L. (John Lyle)</a></div>


</li>






<li class="entry learnable" id="entry719"
 lang="en" word="incisive" freq="4100.66" prog="0">

<a class="word dynamictext" href="/dictionary/incisive">incisive</a>
<div class="definition">demonstrating ability to recognize or draw fine distinctions</div>
<div class="example">A half-hour of informed and
<strong>incisive</strong> questioning by Mr. Russert would have demolished Mr. Trump.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=27b21cde2d8856b506811e711b44b957" rel="nofollow">New York Times (May 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry720"
 lang="en" word="errant" freq="4102.08" prog="0">

<a class="word dynamictext" href="/dictionary/errant">errant</a>
<div class="definition">straying from the right course or from accepted standards</div>
<div class="example">As the crowd voiced its displeasure, the referees made sure Wisconsin got the ball, but pass was
<strong>errant</strong> and rolled out of bounds at midcourt.
<br> —
<a href="http://seattletimes.nwsource.com/html/sports/2017620511_apbkct25minnesota.html?syndication=rss" rel="nofollow">Seattle Times (Feb 28, 2012)</a></div>


</li>






<li class="entry learnable" id="entry721"
 lang="en" word="sedulous" freq="4112.06" prog="0">

<a class="word dynamictext" href="/dictionary/sedulous">sedulous</a>
<div class="definition">marked by care and persistent effort</div>
<div class="example"><strong>Sedulous</strong> attention and painstaking industry always mark the true worker.
<br> —
<a href="http://www.gutenberg.org/ebooks/20608" rel="nofollow">Calhoon, Major A.R.</a></div>


</li>






<li class="entry learnable" id="entry722"
 lang="en" word="incandescent" freq="4122.1" prog="0">

<a class="word dynamictext" href="/dictionary/incandescent">incandescent</a>
<div class="definition">characterized by ardent emotion, intensity, or brilliance</div>
<div class="example">Kirkwood's anger cooled apace; at worst it had been a flare of passion—
<strong>incandescent</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/9779" rel="nofollow">Vance, Louis Joseph</a></div>


</li>






<li class="entry learnable" id="entry723"
 lang="en" word="derelict" freq="4124.97" prog="0">

<a class="word dynamictext" href="/dictionary/derelict">derelict</a>
<div class="definition">in deplorable condition</div>
<div class="example">Others are clustered under a tin awning by a
<strong>derelict</strong> railway station or in similarly run-down school buildings.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/IJmgsDZO_48/" rel="nofollow">Time (Jan 5, 2011)</a></div>


</li>






<li class="entry learnable" id="entry724"
 lang="en" word="entomology" freq="4153.96" prog="0">

<a class="word dynamictext" href="/dictionary/entomology">entomology</a>
<div class="definition">the branch of zoology that studies insects</div>
<div class="example">From the department of
<strong>entomology</strong> you expect to learn something about the troublesome insects, which are so universal an annoyance.
<br> —
<a href="http://www.gutenberg.org/ebooks/18183" rel="nofollow">Latham, A. W.</a></div>


</li>






<li class="entry learnable" id="entry725"
 lang="en" word="execrable" freq="4164.2" prog="0">

<a class="word dynamictext" href="/dictionary/execrable">execrable</a>
<div class="definition">unequivocally detestable</div>
<div class="example">But minds were so overexcited at the time that the parties mutually accused each other, on all occasions, of the most
<strong>execrable</strong> crimes.
<br> —
<a href="http://www.gutenberg.org/ebooks/32408" rel="nofollow">Imbert de Saint-Amand, Arthur Léon, baron</a></div>


</li>






<li class="entry learnable" id="entry726"
 lang="en" word="sluice" freq="4168.6" prog="0">

<a class="word dynamictext" href="/dictionary/sluice">sluice</a>
<div class="definition">pour as if from a conduit that carries a rapid flow of water</div>
<div class="example">At 4:15 p.m., as the rain was
<strong>sluicing</strong> off roofs in sheets, the firemen moved the trucks to higher ground.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1b83fe19cfd929627fce62028a77f88b" rel="nofollow">New York Times (Aug 31, 2011)</a></div>


</li>






<li class="entry learnable" id="entry727"
 lang="en" word="moot" freq="4170.07" prog="0">

<a class="word dynamictext" href="/dictionary/moot">moot</a>
<div class="definition">of no legal significance, as having been previously decided</div>
<div class="example">The statement from Hermitage said even in the Soviet period no defendant had been tried after death, when charges were generally considered
<strong>moot</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c8420ce30feb091df85b8f2149e8c7a2" rel="nofollow">New York Times (Feb 7, 2012)</a></div>


</li>






<li class="entry learnable" id="entry728"
 lang="en" word="evanescent" freq="4171.54" prog="0">

<a class="word dynamictext" href="/dictionary/evanescent">evanescent</a>
<div class="definition">tending to vanish like vapor</div>
<div class="example">Time seems stopped but it is moving on, and every glimmer of light is
<strong>evanescent</strong>, flitting.
<br> —
<a href="http://www.guardian.co.uk/artanddesign/jonathanjonesblog/2010/apr/14/george-seurat-bathers-at-asnieres-art" rel="nofollow">The Guardian (Apr 15, 2010)</a></div>


</li>






<li class="entry learnable" id="entry729"
 lang="en" word="vat" freq="4187.79" prog="0">

<a class="word dynamictext" href="/dictionary/vat">vat</a>
<div class="definition">a large open vessel for holding or storing liquids</div>
<div class="example">The cream remains in the large
<strong>vat</strong> about twenty-four hours before it is churned.
<br> —
<a href="http://www.gutenberg.org/ebooks/38762" rel="nofollow">Chamberlain, James Franklin</a></div>


</li>






<li class="entry learnable" id="entry730"
 lang="en" word="dapper" freq="4207.16" prog="0">

<a class="word dynamictext" href="/dictionary/dapper">dapper</a>
<div class="definition">marked by up-to-dateness in dress and manners</div>
<div class="example">Thoroughly
<strong>dapper</strong>, he took off his black-and-white pinstriped suit jacket — with its pocket-square flair — and weaved in and out among them, his voice ever rising.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=9f46e0bfe40d6a1f0d50de1a6c8586bd" rel="nofollow">New York Times (Jan 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry731"
 lang="en" word="asperity" freq="4217.66" prog="0">

<a class="word dynamictext" href="/dictionary/asperity">asperity</a>
<div class="definition">harshness of manner</div>
<div class="example">All this proceeds from the old man, whose proper character it is to be angry and bitter, and to exhibit rancor and
<strong>asperity</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/34736" rel="nofollow">Arndt, Johann</a></div>


</li>






<li class="entry learnable" id="entry732"
 lang="en" word="flair" freq="4225.2" prog="0">

<a class="word dynamictext" href="/dictionary/flair">flair</a>
<div class="definition">a natural talent</div>
<div class="example">In fact, while Lamarr qualified as an inventive genius for her artistic
<strong>flair</strong>, she fell somewhat short on her scientific acumen.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/FRTOO5fI7j8/click.phdo" rel="nofollow">Slate (Nov 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry733"
 lang="en" word="mote" freq="4226.71" prog="0">

<a class="word dynamictext" href="/dictionary/mote">mote</a>
<div class="definition">a tiny piece of anything</div>
<div class="example">He took his discharge out of his pocket, brushed every
<strong>mote</strong> of dust from the table, and spread the document before their eyes.
<br> —
<a href="http://www.gutenberg.org/ebooks/32517" rel="nofollow">Auerbach, Berthold</a></div>


</li>






<li class="entry learnable" id="entry734"
 lang="en" word="circumspect" freq="4243.39" prog="0">

<a class="word dynamictext" href="/dictionary/circumspect">circumspect</a>
<div class="definition">heedful of potential consequences</div>
<div class="example">Obama administration officials argue that new regulations are forcing insurers to be more
<strong>circumspect</strong> about raising rates.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=1321c7efee831dc6867c7c67ccb94b50" rel="nofollow">New York Times (Sep 27, 2011)</a></div>


</li>






<li class="entry learnable" id="entry735"
 lang="en" word="inimical" freq="4274.07" prog="0">

<a class="word dynamictext" href="/dictionary/inimical">inimical</a>
<div class="definition">not friendly</div>
<div class="example">The Hindu idea is that so long as justice and equity characterise a king’s rule, even beasts naturally
<strong>inimical</strong> are disposed to live in friendship.
<br> —
<a href="http://www.gutenberg.org/ebooks/37002" rel="nofollow">Kingscote, Mrs. Howard</a></div>


</li>






<li class="entry learnable" id="entry736"
 lang="en" word="apropos" freq="4284.91" prog="0">

<a class="word dynamictext" href="/dictionary/apropos">apropos</a>
<div class="definition">of an appropriate or pertinent nature</div>
<div class="example">I found myself thinking vaguely about things that were not at all
<strong>apropos</strong> to the situation.
<br> —
<a href="http://www.gutenberg.org/ebooks/37257" rel="nofollow">Stockley, Cynthia</a></div>


</li>






<li class="entry learnable" id="entry737"
 lang="en" word="gruel" freq="4284.91" prog="0">

<a class="word dynamictext" href="/dictionary/gruel">gruel</a>
<div class="definition">a thin porridge</div>
<div class="example">He says, keep them on just two pints of Indian-meal
<strong>gruel</strong>—by which he appears to mean thin hasty pudding—a day, and no more.
<br> —
<a href="http://www.gutenberg.org/ebooks/34038" rel="nofollow">Alcott, William A. (William Andrus)</a></div>


</li>






<li class="entry learnable" id="entry738"
 lang="en" word="gentility" freq="4289.57" prog="0">

<a class="word dynamictext" href="/dictionary/gentility">gentility</a>
<div class="definition">elegance by virtue of fineness of manner and expression</div>
<div class="example">This was no rough bully of the seas; Carew's bearing and dandified apparel bespoke
<strong>gentility</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/30496" rel="nofollow">Springer, Norman</a></div>


</li>






<li class="entry learnable" id="entry739"
 lang="en" word="disapprobation" freq="4338.36" prog="0">

<a class="word dynamictext" href="/dictionary/disapprobation">disapprobation</a>
<div class="definition">pronouncing as wrong or morally culpable</div>
<div class="example">Mr Ruthven shook his head and declared that he regarded the conduct of her persecutors with grave moral
<strong>disapprobation</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/23115" rel="nofollow">Wheeler, E.J.</a></div>


</li>






<li class="entry learnable" id="entry740"
 lang="en" word="cameo" freq="4349.53" prog="0">

<a class="word dynamictext" href="/dictionary/cameo">cameo</a>
<div class="definition">engraving or carving in low relief on a stone</div>
<div class="example">The trinket was a small round
<strong>cameo</strong> cut out of mother-of-pearl and set in gold; it represented St. George and the dragon.
<br> —
<a href="http://www.gutenberg.org/ebooks/34674" rel="nofollow">J?kai, M?r</a></div>


</li>






<li class="entry learnable" id="entry741"
 lang="en" word="gouge" freq="4355.94" prog="0">

<a class="word dynamictext" href="/dictionary/gouge">gouge</a>
<div class="definition">swindle; obtain by coercion</div>
<div class="example">Shortages also have raised concerns about higher prices and
<strong>gouging</strong> by wholesale drug companies that obtain supplies of hard-to-get drugs and jack up the costs.
<br> —
<a href="http://seattletimes.nwsource.com/html/health/2017293495_drugshortage22.html?syndication=rss" rel="nofollow">Seattle Times (Jan 20, 2012)</a></div>


</li>






<li class="entry learnable" id="entry742"
 lang="en" word="oratorio" freq="4370.43" prog="0">

<a class="word dynamictext" href="/dictionary/oratorio">oratorio</a>
<div class="definition">a musical composition for voices and orchestra</div>
<div class="example">Mendelssohn had no sooner completed his first
<strong>oratorio</strong>, "St. Paul," than he began to think about setting another Bible story to music.
<br> —
<a href="http://www.gutenberg.org/ebooks/38223" rel="nofollow">Edwards, Frederick George</a></div>


</li>






<li class="entry learnable" id="entry743"
 lang="en" word="inclement" freq="4383.39" prog="0">

<a class="word dynamictext" href="/dictionary/inclement">inclement</a>
<div class="definition">severe, of weather</div>
<div class="example">Be prepared for
<strong>inclement</strong> weather and possible ice and snow on park roads.
<br> —
<a href="http://seattletimes.nwsource.com/html/reeltimenorthwest/2016519820_mount_rainier_national_park_go.html?syndication=rss" rel="nofollow">Seattle Times (Oct 16, 2011)</a></div>


</li>






<li class="entry learnable" id="entry744"
 lang="en" word="scintilla" freq="4406.26" prog="0">

<a class="word dynamictext" href="/dictionary/scintilla">scintilla</a>
<div class="definition">a tiny or scarcely detectable amount</div>
<div class="example">Gardner "never expressed one
<strong>scintilla</strong> of remorse for his attack upon the victim" despite overwhelming evidence, prosecutors wrote in a sentencing memo.
<br> —
<a href="http://www.salon.com/news/2010/03/03/us_missing_teen_1/index.html?source=rss&amp;aim=/news" rel="nofollow">Salon (Mar 3, 2010)</a></div>


</li>






<li class="entry learnable" id="entry745"
 lang="en" word="confluence" freq="4429.37" prog="0">

<a class="word dynamictext" href="/dictionary/confluence">confluence</a>
<div class="definition">a flowing together</div>
<div class="example">And indeed, before the 13th century, there was an extraordinary
<strong>confluence</strong> of genius and innovation, particularly around Baghdad.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=9c96c55a96528d552d26d9e35fbd5630" rel="nofollow">New York Times (Dec 28, 2010)</a></div>


</li>






<li class="entry learnable" id="entry746"
 lang="en" word="squalor" freq="4439.34" prog="0">

<a class="word dynamictext" href="/dictionary/squalor">squalor</a>
<div class="definition">sordid dirtiness</div>
<div class="example">What can be expected of human beings, crowded in such miserable habitations, living in filth and
<strong>squalor</strong>, and often pinched with hunger?
<br> —
<a href="http://www.gutenberg.org/ebooks/38869" rel="nofollow">Field, Henry M. (Henry Martyn)</a></div>


</li>






<li class="entry learnable" id="entry747"
 lang="en" word="stricture" freq="4451.04" prog="0">

<a class="word dynamictext" href="/dictionary/stricture">stricture</a>
<div class="definition">severe criticism</div>
<div class="example">While gratefully accepting the generous praises of our friends, we must briefly reply to some
<strong>strictures</strong> by our critics.
<br> —
<a href="http://www.gutenberg.org/ebooks/28039" rel="nofollow">Stanton, Elizabeth Cady</a></div>


</li>






<li class="entry learnable" id="entry748"
 lang="en" word="emblazon" freq="4479.71" prog="0">

<a class="word dynamictext" href="/dictionary/emblazon">emblazon</a>
<div class="definition">decorate with heraldic arms</div>
<div class="example">His coat of arms was
<strong>emblazoned</strong> on the cover.
<br> —
<a href="http://www.gutenberg.org/ebooks/38665" rel="nofollow">Mason, A. E. W. (Alfred Edward Woodley)</a></div>


</li>






<li class="entry learnable" id="entry749"
 lang="en" word="augury" freq="4479.71" prog="0">

<a class="word dynamictext" href="/dictionary/augury">augury</a>
<div class="definition">an event indicating important things to come</div>
<div class="example">This is always an encouraging sign, and an
<strong>augury</strong> of success.
<br> —
<a href="http://www.gutenberg.org/ebooks/26043" rel="nofollow">Alger, Horatio</a></div>


</li>






<li class="entry learnable" id="entry750"
 lang="en" word="abut" freq="4500.17" prog="0">

<a class="word dynamictext" href="/dictionary/abut">abut</a>
<div class="definition">lie adjacent to another or share a boundary</div>
<div class="example">It depicts a mountain landscape near Kingston, a historic town
<strong>abutting</strong> the Hudson River.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=035d2e559f693b7db43887ad09c10d22" rel="nofollow">New York Times (Jan 8, 2010)</a></div>


</li>






<li class="entry learnable" id="entry751"
 lang="en" word="banal" freq="4510.47" prog="0">

<a class="word dynamictext" href="/dictionary/banal">banal</a>
<div class="definition">repeated too often; overfamiliar through overuse</div>
<div class="example">Highly dramatic incidents are juxtaposed with comparatively
<strong>banal</strong> ones; particular attention is given to tales of doomed love affairs.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=f482d62b613b084e17f3c33bb96a21ee" rel="nofollow">New York Times (Dec 4, 2011)</a></div>


</li>






<li class="entry learnable" id="entry752"
 lang="en" word="congeal" freq="4513.91" prog="0">

<a class="word dynamictext" href="/dictionary/congeal">congeal</a>
<div class="definition">become gelatinous</div>
<div class="example">Boil down the syrup to half its original quantity, but take care that it does not boil long enough to
<strong>congeal</strong> or become thick.
<br> —
<a href="http://www.gutenberg.org/ebooks/34837" rel="nofollow">Baru?, Sulpice</a></div>


</li>






<li class="entry learnable" id="entry753"
 lang="en" word="pilfer" freq="4567.97" prog="0">

<a class="word dynamictext" href="/dictionary/pilfer">pilfer</a>
<div class="definition">make off with belongings of others</div>
<div class="example">Many young people scavenge for reusable garbage, living on proceeds from
<strong>pilfered</strong> construction material and other recyclables.
<br> —
<a href="http://seattletimes.nwsource.com/html/books/2017459626_br12boo.html?syndication=rss" rel="nofollow">Seattle Times (Feb 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry754"
 lang="en" word="malcontent" freq="4571.5" prog="0">

<a class="word dynamictext" href="/dictionary/malcontent">malcontent</a>
<div class="definition">a person who is unsatisfied or disgusted</div>
<div class="example">Now, unfortunately, some
<strong>malcontents</strong> among the hands here have spread their ideas, and a strike has been called.
<br> —
<a href="http://www.gutenberg.org/ebooks/26875" rel="nofollow">Maitland, Robert</a></div>


</li>






<li class="entry learnable" id="entry755"
 lang="en" word="sublimate" freq="4571.5" prog="0">

<a class="word dynamictext" href="/dictionary/sublimate">sublimate</a>
<div class="definition">direct energy or urges into useful activities</div>
<div class="example">They might instead have passionate friendships, or
<strong>sublimate</strong> their urges into other pursuits.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=64fb0fe3abe1102b01ff1db778e9113c" rel="nofollow">New York Times (Jun 4, 2010)</a></div>


</li>






<li class="entry learnable" id="entry756"
 lang="en" word="eugenic" freq="4592.81" prog="0">

<a class="word dynamictext" href="/dictionary/eugenic">eugenic</a>
<div class="definition">causing improvement in the offspring produced</div>
<div class="example"><strong>Eugenics</strong> was aimed at creating a better society by filtering out people considered undesirable, ranging from criminals to those imprecisely designated as “feeble-minded.”
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=182dc6dcb656267544c4c7e48bf07aca" rel="nofollow">Washington Post (Aug 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry757"
 lang="en" word="lineament" freq="4603.54" prog="0">

<a class="word dynamictext" href="/dictionary/lineament">lineament</a>
<div class="definition">the characteristic parts of a person's face</div>
<div class="example">The tears stood in Muriel's eyes, and her face was very pale, but serenity marked every
<strong>lineament</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/35313" rel="nofollow">Davidson, John</a></div>


</li>






<li class="entry learnable" id="entry758"
 lang="en" word="firebrand" freq="4610.72" prog="0">

<a class="word dynamictext" href="/dictionary/firebrand">firebrand</a>
<div class="definition">someone who deliberately foments trouble</div>
<div class="example">But Hassan is not some teenage
<strong>firebrand</strong> hurling rocks; he’s a slight, graying scholar committed to peace.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=bcaa74f21a0def2fd809540e18180de1" rel="nofollow">New York Times (Jun 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry759"
 lang="en" word="fiasco" freq="4628.76" prog="0">

<a class="word dynamictext" href="/dictionary/fiasco">fiasco</a>
<div class="definition">a complete failure or collapse</div>
<div class="example">The Stuttgart protests became a national
<strong>fiasco</strong> in late September, when protesters clashed with police wielding batons and water cannons.
<br> —
<a href="http://www.newsweek.com/2010/12/14/hydra-without-a-head.html?from=rss" rel="nofollow">Newsweek (Dec 14, 2010)</a></div>


</li>






<li class="entry learnable" id="entry760"
 lang="en" word="foolhardy" freq="4634.21" prog="0">

<a class="word dynamictext" href="/dictionary/foolhardy">foolhardy</a>
<div class="definition">marked by defiant disregard for danger or consequences</div>
<div class="example">Many mistakes—extravagant purchases,
<strong>foolhardy</strong> investments—are made in the first months after a windfall.
<br> —
<a href="http://online.wsj.com/article/SB10001424052970204131004577235252437857234.html?mod=rss_markets_main" rel="nofollow">Wall Street Journal (Feb 24, 2012)</a></div>


</li>






<li class="entry learnable" id="entry761"
 lang="en" word="retrench" freq="4652.44" prog="0">

<a class="word dynamictext" href="/dictionary/retrench">retrench</a>
<div class="definition">tighten one's belt; use resources carefully</div>
<div class="example">But there was only one way open to me at present—and that was to
<strong>retrench</strong> my expenses.
<br> —
<a href="http://www.gutenberg.org/ebooks/14597" rel="nofollow">Caine, Hall, Sir</a></div>


</li>






<li class="entry learnable" id="entry762"
 lang="en" word="ulterior" freq="4659.77" prog="0">

<a class="word dynamictext" href="/dictionary/ulterior">ulterior</a>
<div class="definition">lying beyond what is openly revealed or avowed</div>
<div class="example">Shop window displays may help prettify shopping thoroughfares, but any savvy retailer has the
<strong>ulterior</strong> motive of self promotion.
<br> —
<a href="http://news.bbc.co.uk/go/rss/-/2/hi/uk_news/magazine/8494143.stm" rel="nofollow">BBC (Feb 3, 2010)</a></div>


</li>






<li class="entry learnable" id="entry763"
 lang="en" word="equable" freq="4663.45" prog="0">

<a class="word dynamictext" href="/dictionary/equable">equable</a>
<div class="definition">not varying</div>
<div class="example">His must have been that calm,
<strong>equable</strong> temperament not easily ruffled, which goes with the self-respecting nature.
<br> —
<a href="http://www.gutenberg.org/ebooks/34842" rel="nofollow">Hurll, Estelle M. (Estelle May)</a></div>


</li>






<li class="entry learnable" id="entry764"
 lang="en" word="inured" freq="4702.4" prog="0">

<a class="word dynamictext" href="/dictionary/inured">inured</a>
<div class="definition">made tough by habitual exposure</div>
<div class="example">But he had become
<strong>inured</strong> to the rush and whirr of missiles, and now paid no heed whatever to them.
<br> —
<a href="http://www.gutenberg.org/ebooks/32565" rel="nofollow">Mitford, Bertram</a></div>


</li>






<li class="entry learnable" id="entry765"
 lang="en" word="invidious" freq="4702.4" prog="0">

<a class="word dynamictext" href="/dictionary/invidious">invidious</a>
<div class="definition">containing or implying a slight or showing prejudice</div>
<div class="example">"After an old-fashioned, all-round team performance … it might seem
<strong>invidious</strong> to single out one player," admits the paper before singling out one player.
<br> —
<a href="http://www.guardian.co.uk/football/2010/jun/24/world-cup-2010-england-slovenia-paul-doyle" rel="nofollow">The Guardian (Jun 24, 2010)</a></div>


</li>






<li class="entry learnable" id="entry766"
 lang="en" word="unmitigated" freq="4709.89" prog="0">

<a class="word dynamictext" href="/dictionary/unmitigated">unmitigated</a>
<div class="definition">not diminished or moderated in intensity or severity</div>
<div class="example">In order to be well directed, sympathy must consider all men, and not the individual alone; only then is it an
<strong>unmitigated</strong> good.
<br> —
<a href="http://www.gutenberg.org/ebooks/39155" rel="nofollow">Williams, C. M.</a></div>


</li>






<li class="entry learnable" id="entry767"
 lang="en" word="concomitant" freq="4766.85" prog="0">

<a class="word dynamictext" href="/dictionary/concomitant">concomitant</a>
<div class="definition">an event or situation that happens at the same time</div>
<div class="example">The conclusion must be drawn that every epidemic of bubonic plague is caused by the
<strong>concomitant</strong> rat plague.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=72fdaa2df764399bda58fb4644e96c00" rel="nofollow">Scientific American (Jan 21, 2011)</a></div>


</li>






<li class="entry learnable" id="entry768"
 lang="en" word="cozen" freq="4805.6" prog="0">

<a class="word dynamictext" href="/dictionary/cozen">cozen</a>
<div class="definition">cheat or trick</div>
<div class="example">Dicing-houses, where cheaters meet, and
<strong>cozen</strong> young men out of their money.
<br> —
<a href="http://www.gutenberg.org/ebooks/16098" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry769"
 lang="en" word="phlegmatic" freq="4823.24" prog="0">

<a class="word dynamictext" href="/dictionary/phlegmatic">phlegmatic</a>
<div class="definition">showing little emotion</div>
<div class="example">Humanity, when surfeited with emotion, becomes calm, almost
<strong>phlegmatic</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/33622" rel="nofollow">Tracy, Louis</a></div>


</li>






<li class="entry learnable" id="entry770"
 lang="en" word="dormer" freq="4825.21" prog="0">

<a class="word dynamictext" href="/dictionary/dormer">dormer</a>
<div class="definition">a gabled extension built out from a sloping roof</div>
<div class="example">Other features, such as the front French doors and two roof
<strong>dormers</strong> with curved-top windows and operable shutters, give this home a pleasing, well-balanced presence.
<br> —
<a href="http://feeds.southernliving.com/~r/southernliving/homeandgarden/~3/DxDzl1Nk6O8/" rel="nofollow">Southern Living (Apr 14, 2010)</a></div>


</li>






<li class="entry learnable" id="entry771"
 lang="en" word="pontifical" freq="4837.05" prog="0">

<a class="word dynamictext" href="/dictionary/pontifical">pontifical</a>
<div class="definition">denoting or governed by or relating to a bishop or bishops</div>
<div class="example">The high priest made no resistance, but went forth in his
<strong>pontifical</strong> robes, followed by the people in white garments, to meet the mighty warrior.
<br> —
<a href="http://www.gutenberg.org/ebooks/27114" rel="nofollow">Lord, John</a></div>


</li>






<li class="entry learnable" id="entry772"
 lang="en" word="disport" freq="4837.05" prog="0">

<a class="word dynamictext" href="/dictionary/disport">disport</a>
<div class="definition">occupy in an agreeable, entertaining or pleasant fashion</div>
<div class="example">Straightway the glade in which they sat was filled with knights, ladies, maidens, and esquires, who danced and
<strong>disported</strong> themselves right joyously.
<br> —
<a href="http://www.gutenberg.org/ebooks/30871" rel="nofollow">Spence, Lewis</a></div>


</li>






<li class="entry learnable" id="entry773"
 lang="en" word="apologist" freq="4854.93" prog="0">

<a class="word dynamictext" href="/dictionary/apologist">apologist</a>
<div class="definition">a person who argues to defend some policy or institution</div>
<div class="example">Tories, and
<strong>apologists</strong> for Great Britain, have written much about a justification for this action, but there is no real justification.
<br> —
<a href="http://www.gutenberg.org/ebooks/30244" rel="nofollow">Barce, Elmore</a></div>


</li>






<li class="entry learnable" id="entry774"
 lang="en" word="abeyance" freq="4862.91" prog="0">

<a class="word dynamictext" href="/dictionary/abeyance">abeyance</a>
<div class="definition">temporary cessation or suspension</div>
<div class="example">My feelings of home-sickness had returned with redoubled strength after being long in
<strong>abeyance</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/35431" rel="nofollow">Boldrewood, Rolf</a></div>


</li>






<li class="entry learnable" id="entry775"
 lang="en" word="enclave" freq="4880.98" prog="0">

<a class="word dynamictext" href="/dictionary/enclave">enclave</a>
<div class="definition">an enclosed territory that is culturally distinct</div>
<div class="example">And its suburban schools, rather than being exclusive
<strong>enclaves</strong>, include children whose parents can't afford a house in the neighborhood.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=803dea3c67e480b150a5b2ec4eeb8fbc" rel="nofollow">Washington Post (Jan 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry776"
 lang="en" word="improvident" freq="4899.18" prog="0">

<a class="word dynamictext" href="/dictionary/improvident">improvident</a>
<div class="definition">not supplying something useful for the future</div>
<div class="example">He was industrious but
<strong>improvident</strong>; he made money and he lost it.
<br> —
<a href="http://www.gutenberg.org/ebooks/23595" rel="nofollow">Hubbard, Elbert</a></div>


</li>






<li class="entry learnable" id="entry777"
 lang="en" word="disquisition" freq="4913.43" prog="0">

<a class="word dynamictext" href="/dictionary/disquisition">disquisition</a>
<div class="definition">an elaborate analytical or explanatory essay or discussion</div>
<div class="example">Cumulatively, what emerges from To Kill a Mockingbird is a thoughtful
<strong>disquisition</strong> that encompasses – and goes beyond – the question of racial bias at its worst.
<br> —
<a href="http://www.guardian.co.uk/books/booksblog/2010/jul/09/kill-a-mockingbird-racism" rel="nofollow">The Guardian (Jul 9, 2010)</a></div>


</li>






<li class="entry learnable" id="entry778"
 lang="en" word="categorical" freq="4917.52" prog="0">

<a class="word dynamictext" href="/dictionary/categorical">categorical</a>
<div class="definition">not modified or restricted by reservations</div>
<div class="example">"European leaders were united,
<strong>categorical</strong> and crystal clear: Gaddafi must go," British Prime Minister David Cameron said.
<br> —
<a href="http://feedproxy.google.com/~r/time/world/~3/st3WFold0aM/0,8599,2058534,00.html" rel="nofollow">Time (Mar 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry779"
 lang="en" word="placate" freq="1133.44" prog="0">

<a class="word dynamictext" href="/dictionary/placate">placate</a>
<div class="definition">cause to be more favorably inclined</div>
<div class="example">The East India Company was
<strong>placated</strong> by the concession of further exemptions in its favour.
<br> —
<a href="http://www.gutenberg.org/ebooks/34011" rel="nofollow">Smith, A. D.</a></div>


</li>






<li class="entry learnable" id="entry780"
 lang="en" word="redolent" freq="4927.77" prog="0">

<a class="word dynamictext" href="/dictionary/redolent">redolent</a>
<div class="definition">serving to bring to mind</div>
<div class="example">Here, however, are congregated a vast number of curious and interesting objects, while the place is
<strong>redolent</strong> of vivid historical associations.
<br> —
<a href="http://www.gutenberg.org/ebooks/28222" rel="nofollow">Ballou, Maturin Murray</a></div>


</li>






<li class="entry learnable" id="entry781"
 lang="en" word="felicitous" freq="4948.39" prog="0">

<a class="word dynamictext" href="/dictionary/felicitous">felicitous</a>
<div class="definition">exhibiting an agreeably appropriate manner or style</div>
<div class="example">The first book is the finest, sparkling with
<strong>felicitous</strong> expressions and rising frequently to true poetry.
<br> —
<a href="http://www.gutenberg.org/ebooks/30421" rel="nofollow">Dennis, John</a></div>


</li>






<li class="entry learnable" id="entry782"
 lang="en" word="gusty" freq="4954.61" prog="0">

<a class="word dynamictext" href="/dictionary/gusty">gusty</a>
<div class="definition">blowing in puffs or short intermittent blasts</div>
<div class="example">Winds could get
<strong>gusty</strong>, occasionally blowing at more than 30 miles per hour.
<br> —
<a href="http://feeds.reuters.com/~r/Reuters/domesticNews/~3/W0iIbJkXUvA/us-weather-us-watch-idUSTRE72S2VW20110329" rel="nofollow">Reuters (Mar 29, 2011)</a></div>


</li>






<li class="entry learnable" id="entry783"
 lang="en" word="natty" freq="4962.93" prog="0">

<a class="word dynamictext" href="/dictionary/natty">natty</a>
<div class="definition">marked by up-to-dateness in dress and manners</div>
<div class="example">He wore a checked suit, very
<strong>natty</strong>, and was more than usually tall and fine-looking.
<br> —
<a href="http://www.gutenberg.org/ebooks/18761" rel="nofollow">Green, Anna Katharine</a></div>


</li>






<li class="entry learnable" id="entry784"
 lang="en" word="pacifist" freq="4965.01" prog="0">

<a class="word dynamictext" href="/dictionary/pacifist">pacifist</a>
<div class="definition">opposed to war</div>
<div class="example">He was, furthermore, a real
<strong>pacifist</strong>, believing that war is debasing morally and disastrous economically.
<br> —
<a href="http://www.gutenberg.org/ebooks/21877" rel="nofollow">Seymour, Charles</a></div>


</li>






<li class="entry learnable" id="entry785"
 lang="en" word="buxom" freq="4975.46" prog="0">

<a class="word dynamictext" href="/dictionary/buxom">buxom</a>
<div class="definition">healthily plump and vigorous</div>
<div class="example">Mrs. Connelly—a round, rosy,
<strong>buxom</strong> Irishwoman, with a mellow voice, laughing eye, and artist-red hair—was very much taken with their plan.
<br> —
<a href="http://www.gutenberg.org/ebooks/30436" rel="nofollow">Douglas, Amanda Minnie</a></div>


</li>






<li class="entry learnable" id="entry786"
 lang="en" word="heyday" freq="4988.05" prog="0">

<a class="word dynamictext" href="/dictionary/heyday">heyday</a>
<div class="definition">the period of greatest prosperity or productivity</div>
<div class="example">Playboy's most popular years are well behind it - the magazine enjoyed its
<strong>heyday</strong> in the 1970s.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=3137342954608621e220caea71b35b90" rel="nofollow">Washington Post (Jan 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry787"
 lang="en" word="herculean" freq="5004.94" prog="0">

<a class="word dynamictext" href="/dictionary/herculean">herculean</a>
<div class="definition">displaying superhuman strength or power</div>
<div class="example">He made
<strong>herculean</strong> efforts to get on terms with his examination subjects, and worked harder than he had ever done in his life before.
<br> —
<a href="http://www.gutenberg.org/ebooks/38694" rel="nofollow">Marshall, Archibald</a></div>


</li>






<li class="entry learnable" id="entry788"
 lang="en" word="burgeon" freq="5041.22" prog="0">

<a class="word dynamictext" href="/dictionary/burgeon">burgeon</a>
<div class="definition">grow and flourish</div>
<div class="example">Brooklyn's
<strong>burgeoning</strong> dining scene has even developed a following among Manhattan food lovers.
<br> —
<a href="http://feeds.reuters.com/~r/Reuters/domesticNews/~3/4QY_dB2K7lA/us-food-brooklyn-idUSTRE7932NY20111004" rel="nofollow">Reuters (Oct 4, 2011)</a></div>


</li>






<li class="entry learnable" id="entry789"
 lang="en" word="crone" freq="5086.76" prog="0">

<a class="word dynamictext" href="/dictionary/crone">crone</a>
<div class="definition">an ugly, evil-looking old woman</div>
<div class="example">The aged
<strong>crone</strong> wrinkled her forehead and lifted her grizzled eyebrows, still without looking at him.
<br> —
<a href="http://www.gutenberg.org/ebooks/29005" rel="nofollow">Myrick, Frank</a></div>


</li>






<li class="entry learnable" id="entry790"
 lang="en" word="prognosticate" freq="5106.53" prog="0">

<a class="word dynamictext" href="/dictionary/prognosticate">prognosticate</a>
<div class="definition">make a prediction about; tell in advance</div>
<div class="example">How strange it is that our dreams often
<strong>prognosticate</strong> coming events!
<br> —
<a href="http://www.gutenberg.org/ebooks/34817" rel="nofollow">Huth, Alexander</a></div>


</li>






<li class="entry learnable" id="entry791"
 lang="en" word="lout" freq="5117.58" prog="0">

<a class="word dynamictext" href="/dictionary/lout">lout</a>
<div class="definition">an awkward stupid person</div>
<div class="example">But this question was beyond the poor
<strong>lout</strong>'s intelligence; he could only blubber and fend off possible chastisement.
<br> —
<a href="http://www.gutenberg.org/ebooks/26277" rel="nofollow">Williams, J. Scott (John Scott)</a></div>


</li>






<li class="entry learnable" id="entry792"
 lang="en" word="simper" freq="5126.46" prog="0">

<a class="word dynamictext" href="/dictionary/simper">simper</a>
<div class="definition">smile affectedly or derisively</div>
<div class="example">Mrs. Barnett's mouth
<strong>simpered</strong> at the implied flattery; but her eyes, always looking calculatingly for substantial results, were studying Reedy Jenkins.
<br> —
<a href="http://www.gutenberg.org/ebooks/25960" rel="nofollow">Hamby, William H. (William Henry)</a></div>


</li>






<li class="entry learnable" id="entry793"
 lang="en" word="iniquitous" freq="5128.68" prog="0">

<a class="word dynamictext" href="/dictionary/iniquitous">iniquitous</a>
<div class="definition">characterized by injustice or wickedness</div>
<div class="example">This was some piece of wickedness concocted by the venomous brain of the
<strong>iniquitous</strong> Vicar, more abominable than all his other wickednesses.
<br> —
<a href="http://www.gutenberg.org/ebooks/26541" rel="nofollow">Trollope, Anthony</a></div>


</li>






<li class="entry learnable" id="entry794"
 lang="en" word="rile" freq="5146.54" prog="0">

<a class="word dynamictext" href="/dictionary/rile">rile</a>
<div class="definition">disturb, especially by minor irritations</div>
<div class="example">The prospect of seeing Ms. Palin tour Alaska’s wild habitats may
<strong>rile</strong> some people who oppose her opinions about climate change.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=bfd366bfb34c5280b73f30abf691184c" rel="nofollow">New York Times (Mar 25, 2010)</a></div>


</li>






<li class="entry learnable" id="entry795"
 lang="en" word="sentient" freq="5160.02" prog="0">

<a class="word dynamictext" href="/dictionary/sentient">sentient</a>
<div class="definition">endowed with feeling and unstructured consciousness</div>
<div class="example">The money fluttered from his hand to the floor, where it lay like a
<strong>sentient</strong> thing, staring back as if mocking him.
<br> —
<a href="http://www.gutenberg.org/ebooks/20548" rel="nofollow">Hitchcock, Lucius W.</a></div>


</li>






<li class="entry learnable" id="entry796"
 lang="en" word="garish" freq="5198.59" prog="0">

<a class="word dynamictext" href="/dictionary/garish">garish</a>
<div class="definition">tastelessly showy</div>
<div class="example">With its opulently
<strong>garish</strong> sets and knee-jerk realism, the production dwarfed the cast, no matter what stars were singing.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=431f501088407ed6567b9514b2e7a614" rel="nofollow">New York Times (Jan 2, 2011)</a></div>


</li>






<li class="entry learnable" id="entry797"
 lang="en" word="readjustment" freq="5200.87" prog="0">

<a class="word dynamictext" href="/dictionary/readjustment">readjustment</a>
<div class="definition">the act of correcting again </div>
<div class="example">While earpieces are not uncomfortable, they do sometimes come loose, requiring
<strong>readjustment</strong>.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/EDzQqg4VKIc/click.phdo" rel="nofollow">Slate (Apr 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry798"
 lang="en" word="erstwhile" freq="5235.42" prog="0">

<a class="word dynamictext" href="/dictionary/erstwhile">erstwhile</a>
<div class="definition">belonging to some prior time</div>
<div class="example">Sony, whose
<strong>erstwhile</strong> dominance in consumer electronics has been eroded by the likes of Samsung, could beat rivals to a potentially new generation of devices.
<br> —
<a href="http://feeds.reuters.com/~r/reuters/technologyNews/~3/fKVHEnPta18/idUSTRE64I67J20100520" rel="nofollow">Reuters (May 20, 2010)</a></div>


</li>






<li class="entry learnable" id="entry799"
 lang="en" word="aquiline" freq="5251.69" prog="0">

<a class="word dynamictext" href="/dictionary/aquiline">aquiline</a>
<div class="definition">curved down like an eagle's beak</div>
<div class="example">The nose slightly
<strong>aquiline</strong>, curving at the nostril; while luxuriant hair, in broad plaits, fell far below her waist.
<br> —
<a href="http://www.gutenberg.org/ebooks/35271" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry800"
 lang="en" word="bilious" freq="5261.04" prog="0">

<a class="word dynamictext" href="/dictionary/bilious">bilious</a>
<div class="definition">irritable as if suffering from indigestion</div>
<div class="example">But his sleep had not refreshed him; he waked up
<strong>bilious</strong>, irritable, ill-tempered, and looked with hatred at his room.
<br> —
<a href="http://www.gutenberg.org/ebooks/2554" rel="nofollow">Garnett, Constance</a></div>


</li>






<li class="entry learnable" id="entry801"
 lang="en" word="vilify" freq="5277.48" prog="0">

<a class="word dynamictext" href="/dictionary/vilify">vilify</a>
<div class="definition">spread negative information about</div>
<div class="example">The trial was televised and the victim's identity became known, resulting in her being
<strong>vilified</strong> by almost the entire town.
<br> —
<a href="http://www.guardian.co.uk/commentisfree/2011/jan/19/wrong-about-spit-on-your-grave" rel="nofollow">The Guardian (Jan 19, 2011)</a></div>


</li>






<li class="entry learnable" id="entry802"
 lang="en" word="nuance" freq="5289.28" prog="0">

<a class="word dynamictext" href="/dictionary/nuance">nuance</a>
<div class="definition">a subtle difference in meaning or opinion or attitude</div>
<div class="example">By working so hard to simplify things, we lose any
<strong>nuance</strong> or ability to deal with folks’ individual circumstances.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=c1b24aebf37fa64994923ac9442f2292" rel="nofollow">Washington Post (Oct 3, 2011)</a></div>


</li>






<li class="entry learnable" id="entry803"
 lang="en" word="gawk" freq="5322.62" prog="0">

<a class="word dynamictext" href="/dictionary/gawk">gawk</a>
<div class="definition">look with amazement</div>
<div class="example">He speaks mainly of his humiliation at lying on the sidewalk as hipsters
<strong>gawked</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=50b222d3b67ef1792bac5a1fef1b689f" rel="nofollow">New York Times (Apr 9, 2012)</a></div>


</li>






<li class="entry learnable" id="entry804"
 lang="en" word="refectory" freq="5327.41" prog="0">

<a class="word dynamictext" href="/dictionary/refectory">refectory</a>
<div class="definition">a communal dining-hall, usually in a monastery</div>
<div class="example">Meanwhile, the soup was getting cold in the
<strong>refectory</strong>, so that the assembled brotherhood at last fell to, without waiting any longer for the Abbot.
<br> —
<a href="http://www.gutenberg.org/ebooks/35847" rel="nofollow">Scheffel, Joseph Victor von</a></div>


</li>






<li class="entry learnable" id="entry805"
 lang="en" word="palatial" freq="5339.44" prog="0">

<a class="word dynamictext" href="/dictionary/palatial">palatial</a>
<div class="definition">suitable for or like a large and stately mansion</div>
<div class="example">The house was very large; its rooms almost
<strong>palatial</strong> in size, had been finished in richly carved hardwood panels and wainscoting, mostly polished mahogany.
<br> —
<a href="http://www.gutenberg.org/ebooks/29313" rel="nofollow">Hitchcock, Frederick L. (Frederick Lyman)</a></div>


</li>






<li class="entry learnable" id="entry806"
 lang="en" word="mincing" freq="5344.27" prog="0">

<a class="word dynamictext" href="/dictionary/mincing">mincing</a>
<div class="definition">affectedly dainty or refined</div>
<div class="example">She went, carrying her little head very high indeed, and taking dainty,
<strong>mincing</strong> steps.
<br> —
<a href="http://www.gutenberg.org/ebooks/35239" rel="nofollow">Banks, Nancy Huston</a></div>


</li>






<li class="entry learnable" id="entry807"
 lang="en" word="trenchant" freq="5400.41" prog="0">

<a class="word dynamictext" href="/dictionary/trenchant">trenchant</a>
<div class="definition">having keenness and forcefulness and penetration in thought</div>
<div class="example">They are written in a serio-comic tone, and for sparkling wit,
<strong>trenchant</strong> sarcasm, and dramatic dialectics surpass anything ever penned by Lessing.
<br> —
<a href="http://www.gutenberg.org/ebooks/33435" rel="nofollow">Lessing, Gotthold Ephraim</a></div>


</li>






<li class="entry learnable" id="entry808"
 lang="en" word="emboss" freq="5407.82" prog="0">

<a class="word dynamictext" href="/dictionary/emboss">emboss</a>
<div class="definition">raise in a relief</div>
<div class="example">Requests may also be made of the stationer to use an
<strong>embossed</strong> plate so that the letters stand out in relief.
<br> —
<a href="http://www.gutenberg.org/ebooks/35975" rel="nofollow">Eichler, Lillian</a></div>


</li>






<li class="entry learnable" id="entry809"
 lang="en" word="proletarian" freq="5410.3" prog="0">

<a class="word dynamictext" href="/dictionary/proletarian">proletarian</a>
<div class="definition">a member of the working class</div>
<div class="example">As yet, the true
<strong>proletarian</strong> wage-earner, uprooted from his native village and broken away from the organization of Indian society, is but insignificant.
<br> —
<a href="http://www.gutenberg.org/ebooks/24107" rel="nofollow">Stoddard, Lothrop</a></div>


</li>






<li class="entry learnable" id="entry810"
 lang="en" word="careen" freq="5420.22" prog="0">

<a class="word dynamictext" href="/dictionary/careen">careen</a>
<div class="definition">pitching dangerously to one side</div>
<div class="example">I turned the steering wheel all the way to one side, and found myself
<strong>careening</strong> backward in a violent arc.
<br> —
<a href="http://www.gutenberg.org/ebooks/35703" rel="nofollow">Vogel, Nancy</a></div>


</li>






<li class="entry learnable" id="entry811"
 lang="en" word="debacle" freq="5420.22" prog="0">

<a class="word dynamictext" href="/dictionary/debacle">debacle</a>
<div class="definition">a sound defeat</div>
<div class="example">The Broncos are coming off their worst season in franchise history, a 4-12
<strong>debacle</strong> that included issues on and off the field.
<br> —
<a href="http://nbcsports.msnbc.com/id/40990139/ns/sports-nfl/" rel="nofollow">Newsweek (Jan 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry812"
 lang="en" word="sycophant" freq="5425.19" prog="0">

<a class="word dynamictext" href="/dictionary/sycophant">sycophant</a>
<div class="definition">a person who tries to please someone to gain an advantage</div>
<div class="example">The people around the king are
<strong>sycophants</strong> who are looking after their own personal advantage.
<br> —
<a href="http://www.gutenberg.org/ebooks/29849" rel="nofollow">Coffin, Charles Carleton</a></div>


</li>






<li class="entry learnable" id="entry813"
 lang="en" word="crabbed" freq="5437.67" prog="0">

<a class="word dynamictext" href="/dictionary/crabbed">crabbed</a>
<div class="definition">annoyed and irritable</div>
<div class="example">He grew
<strong>crabbed</strong> and soured, his temper flashing out on small provocation.
<br> —
<a href="http://www.gutenberg.org/ebooks/38990" rel="nofollow">Weyman, Stanley J.</a></div>


</li>






<li class="entry learnable" id="entry814"
 lang="en" word="archetype" freq="5457.75" prog="0">

<a class="word dynamictext" href="/dictionary/archetype">archetype</a>
<div class="definition">something that serves as a model</div>
<div class="example">Newport, R.I., looks like a perfect
<strong>archetype</strong> of a small, seaside New England town.
<br> —
<a href="http://www.forbes.com/2010/11/02/small-town-getaways-trips-lifestyle-travel-vacation.html?feed=rss_forbeslife" rel="nofollow">Forbes (Nov 3, 2010)</a></div>


</li>






<li class="entry learnable" id="entry815"
 lang="en" word="cryptic" freq="5477.97" prog="0">

<a class="word dynamictext" href="/dictionary/cryptic">cryptic</a>
<div class="definition">of an obscure nature</div>
<div class="example">The authorities, beyond some
<strong>cryptic</strong> language about the death being sudden but not suspicious, have released no details.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/Zqf3MZ1Xi9M/after-rick-rypiens-death-a-question-of-privacy.html" rel="nofollow">New York Times (Aug 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry816"
 lang="en" word="penchant" freq="5485.6" prog="0">

<a class="word dynamictext" href="/dictionary/penchant">penchant</a>
<div class="definition">a strong liking</div>
<div class="example">But sometimes, old Wall Street habits — including a
<strong>penchant</strong> for expensive luxuries — are hard to break.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=d144ae1e92c0841a207a808ff0e7e79b" rel="nofollow">New York Times (Mar 31, 2012)</a></div>


</li>






<li class="entry learnable" id="entry817"
 lang="en" word="bauble" freq="5488.15" prog="0">

<a class="word dynamictext" href="/dictionary/bauble">bauble</a>
<div class="definition">cheap showy jewelry or ornament on clothing</div>
<div class="example">But men were buying Valentine's
<strong>baubles</strong> for their honeys long before the first Zales ever opened its doors in a suburban shopping mall.
<br> —
<a href="http://feedproxy.google.com/~r/slate-1696/~3/TRBvMwsd1AQ/click.phdo" rel="nofollow">Slate (Feb 14, 2012)</a></div>


</li>






<li class="entry learnable" id="entry818"
 lang="en" word="mountebank" freq="5493.24" prog="0">

<a class="word dynamictext" href="/dictionary/mountebank">mountebank</a>
<div class="definition">a flamboyant deceiver</div>
<div class="example">They are singularly clever, these Indian
<strong>mountebanks</strong>, especially in sleight of hand tricks.
<br> —
<a href="http://www.gutenberg.org/ebooks/28222" rel="nofollow">Ballou, Maturin Murray</a></div>


</li>






<li class="entry learnable" id="entry819"
 lang="en" word="fawning" freq="5518.89" prog="0">

<a class="word dynamictext" href="/dictionary/fawning">fawning</a>
<div class="definition">attempting to win favor by flattery</div>
<div class="example">“As any cult leader, he was extremely good at milking the rich, at flattering and
<strong>fawning</strong>,” Ms. Gordon said.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=8f82b95676e458e8d46a224ad9753343" rel="nofollow">New York Times (Apr 16, 2010)</a></div>


</li>






<li class="entry learnable" id="entry820"
 lang="en" word="hummock" freq="5555.19" prog="0">

<a class="word dynamictext" href="/dictionary/hummock">hummock</a>
<div class="definition">a small natural hill</div>
<div class="example">Captain Bill leaned back on a
<strong>hummock</strong> of earth, his arms folded behind his head.
<br> —
<a href="http://www.gutenberg.org/ebooks/34593" rel="nofollow">Grayson, J. J.</a></div>


</li>






<li class="entry learnable" id="entry821"
 lang="en" word="apotheosis" freq="5573.52" prog="0">

<a class="word dynamictext" href="/dictionary/apotheosis">apotheosis</a>
<div class="definition">model of excellence or perfection of a kind</div>
<div class="example">Contrary to popular belief, however, she said Ms. Deen’s fat-laden cooking does not in fact represent the
<strong>apotheosis</strong> of Southern cuisine.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2409408a4d502c5a3cc808e9ab0c10a9" rel="nofollow">New York Times (Jan 17, 2012)</a></div>


</li>






<li class="entry learnable" id="entry822"
 lang="en" word="discretionary" freq="5584.05" prog="0">

<a class="word dynamictext" href="/dictionary/discretionary">discretionary</a>
<div class="definition">not earmarked; available for use as needed</div>
<div class="example">Steeper prices for basic necessities have forced many to cut back on more
<strong>discretionary</strong> purchases.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=dcba40fa315fd2fa68b234d67250886b" rel="nofollow">Washington Post (Oct 19, 2011)</a></div>


</li>






<li class="entry learnable" id="entry823"
 lang="en" word="pithy" freq="5634.61" prog="0">

<a class="word dynamictext" href="/dictionary/pithy">pithy</a>
<div class="definition">concise and full of meaning</div>
<div class="example">As Moore isolated finer points of the passing game, Keller in neat penmanship jotted down
<strong>pithy</strong> phrases and punchy quotes, basic ideas and specific concepts.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/FlIr088CaBY/dustin-keller-an-eager-protege-of-jets-consultant-tom-moore.html" rel="nofollow">New York Times (Dec 10, 2011)</a></div>


</li>






<li class="entry learnable" id="entry824"
 lang="en" word="comport" freq="5634.61" prog="0">

<a class="word dynamictext" href="/dictionary/comport">comport</a>
<div class="definition">behave in a certain manner</div>
<div class="example">Ironically, the one man on stage who did
<strong>comport</strong> himself with dignity, John Huntsman, is now being dismissed as having not made an impact.
<br> —
<a href="http://feedproxy.google.com/~r/time/nation/~3/VKIqJfcRfRA/0,8599,2092425,00.html" rel="nofollow">Time (Sep 8, 2011)</a></div>


</li>






<li class="entry learnable" id="entry825"
 lang="en" word="checkered" freq="5637.3" prog="0">

<a class="word dynamictext" href="/dictionary/checkered">checkered</a>
<div class="definition">marked by changeable fortune</div>
<div class="example">Both restaurants have
<strong>checkered</strong> histories with the health department; they were temporarily shut down for sanitary violations that included evidence of rodents.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=38bddb5c0bc82534eba49eb566ada5bc" rel="nofollow">New York Times (Aug 22, 2010)</a></div>


</li>






<li class="entry learnable" id="entry826"
 lang="en" word="ambrosia" freq="5639.98" prog="0">

<a class="word dynamictext" href="/dictionary/ambrosia">ambrosia</a>
<div class="definition">the food and drink of the gods</div>
<div class="example">"Frieda represents the lovely goddess, Hebe, who served nectar and
<strong>ambrosia</strong> to the high gods on Mount Olympus," she explained.
<br> —
<a href="http://www.gutenberg.org/ebooks/34929" rel="nofollow">Vandercook, Margaret</a></div>


</li>






<li class="entry learnable" id="entry827"
 lang="en" word="factious" freq="5677.9" prog="0">

<a class="word dynamictext" href="/dictionary/factious">factious</a>
<div class="definition">dissenting with the majority opinion</div>
<div class="example">Will it be answered that we are
<strong>factious</strong>, discontented spirits, striving to disturb the public order, and tear up the old fastnesses of society?
<br> —
<a href="http://www.gutenberg.org/ebooks/28020" rel="nofollow">Stanton, Elizabeth Cady</a></div>


</li>






<li class="entry learnable" id="entry828"
 lang="en" word="disgorge" freq="5680.63" prog="0">

<a class="word dynamictext" href="/dictionary/disgorge">disgorge</a>
<div class="definition">cause or allow to flow or run out or over</div>
<div class="example">There are telephone poles and cinder blocks and living room chairs and large trash bins, overturned and
<strong>disgorging</strong> their soggy contents.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=e8b5b80da3d3472192b6df796cacb01d" rel="nofollow">New York Times (Oct 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry829"
 lang="en" word="filch" freq="5749.69" prog="0">

<a class="word dynamictext" href="/dictionary/filch">filch</a>
<div class="definition">make off with belongings of others</div>
<div class="example">Then, in place of the real site, it displays a fake site created&nbsp; to
<strong>filch</strong> account numbers, login names and passwords.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b77698a4ad3edf466d4ddfcbaeb8feb2" rel="nofollow">New York Times (Jul 13, 2010)</a></div>


</li>






<li class="entry learnable" id="entry830"
 lang="en" word="wraith" freq="5783.44" prog="0">

<a class="word dynamictext" href="/dictionary/wraith">wraith</a>
<div class="definition">a mental representation of some haunting experience</div>
<div class="example">Whichever way he turns there loom past
<strong>wraiths</strong>, restless as ghosts of unburied Grecian slain.
<br> —
<a href="http://www.gutenberg.org/ebooks/22221" rel="nofollow">Lee, Carson Jay</a></div>


</li>






<li class="entry learnable" id="entry831"
 lang="en" word="demonstrable" freq="5789.11" prog="0">

<a class="word dynamictext" href="/dictionary/demonstrable">demonstrable</a>
<div class="definition">capable of being proved</div>
<div class="example">The linkage between deposits and trade is definite, causal, positive, statistically
<strong>demonstrable</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/34823" rel="nofollow">Anderson, Benjamin M.</a></div>


</li>






<li class="entry learnable" id="entry832"
 lang="en" word="pertinacious" freq="5826.19" prog="0">

<a class="word dynamictext" href="/dictionary/pertinacious">pertinacious</a>
<div class="definition">stubbornly unyielding</div>
<div class="example">His temper, though yielding and easy in appearance, was in reality most obstinate and
<strong>pertinacious</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/36157" rel="nofollow">Kavanagh, Julia</a></div>


</li>






<li class="entry learnable" id="entry833"
 lang="en" word="emend" freq="5855.04" prog="0">

<a class="word dynamictext" href="/dictionary/emend">emend</a>
<div class="definition">make corrections to</div>
<div class="example">The following were identified as spelling or typographic errors and have been
<strong>emended</strong> as noted.
<br> —
<a href="http://www.gutenberg.org/ebooks/29319" rel="nofollow">Hopper, James</a></div>


</li>






<li class="entry learnable" id="entry834"
 lang="en" word="laggard" freq="5890.04" prog="0">

<a class="word dynamictext" href="/dictionary/laggard">laggard</a>
<div class="definition">someone who takes more time than necessary</div>
<div class="example">Corporate data centers are the slowpoke
<strong>laggards</strong> of information technology.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=36fd889ee155aae610e04c04e6ce12b3" rel="nofollow">New York Times (Apr 10, 2012)</a></div>


</li>






<li class="entry learnable" id="entry835"
 lang="en" word="waffle" freq="5895.92" prog="0">

<a class="word dynamictext" href="/dictionary/waffle">waffle</a>
<div class="definition">pause or hold back in uncertainty or unwillingness</div>
<div class="example">A few days of
<strong>waffling</strong> back and forth and I ended up going out to a mediocre bistro with my parents.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=987cfa57274dc2591615c0872117cebc" rel="nofollow">Scientific American (Feb 8, 2011)</a></div>


</li>






<li class="entry learnable" id="entry836"
 lang="en" word="loquacious" freq="5895.92" prog="0">

<a class="word dynamictext" href="/dictionary/loquacious">loquacious</a>
<div class="definition">full of trivial conversation</div>
<div class="example">Pan soon found it needful to make conversation, in order to keep the
<strong>loquacious</strong> old stage driver from talking too much.
<br> —
<a href="http://www.gutenberg.org/ebooks/29080" rel="nofollow">Grey, Zane</a></div>


</li>






<li class="entry learnable" id="entry837"
 lang="en" word="venial" freq="5922.5" prog="0">

<a class="word dynamictext" href="/dictionary/venial">venial</a>
<div class="definition">easily excused or forgiven</div>
<div class="example">The confidence of ignorance, however
<strong>venial</strong> in youth, is not altogether so excusable, in full grown men.
<br> —
<a href="http://www.gutenberg.org/ebooks/38588" rel="nofollow">School, A Sexton of the Old</a></div>


</li>






<li class="entry learnable" id="entry838"
 lang="en" word="peon" freq="5952.31" prog="0">

<a class="word dynamictext" href="/dictionary/peon">peon</a>
<div class="definition">a laborer who is obliged to do menial work</div>
<div class="example">For the most part, the men were wiry
<strong>peons</strong>, some toiling half naked, but there were a number who looked like prosperous citizens.
<br> —
<a href="http://www.gutenberg.org/ebooks/37582" rel="nofollow">Bindloss, Harold</a></div>


</li>






<li class="entry learnable" id="entry839"
 lang="en" word="effulgence" freq="5985.46" prog="0">

<a class="word dynamictext" href="/dictionary/effulgence">effulgence</a>
<div class="definition">the quality of being bright and sending out rays of light</div>
<div class="example">Then, all at once, in a way that seemed to frighten her, the sunshine had burst the clouds, and dazzled her with its
<strong>effulgence</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/34664" rel="nofollow">Fenn, George Manville</a></div>


</li>






<li class="entry learnable" id="entry840"
 lang="en" word="lode" freq="6003.7" prog="0">

<a class="word dynamictext" href="/dictionary/lode">lode</a>
<div class="definition">a deposit of valuable ore</div>
<div class="example">Such local perturbations are regularly used in Sweden for tracing out the position of underground
<strong>lodes</strong> of iron ore.
<br> —
<a href="http://www.gutenberg.org/ebooks/33810" rel="nofollow">Gilbert, William</a></div>


</li>






<li class="entry learnable" id="entry841"
 lang="en" word="fanfare" freq="6009.8" prog="0">

<a class="word dynamictext" href="/dictionary/fanfare">fanfare</a>
<div class="definition">a gaudy outward display</div>
<div class="example">It opened a month ago to considerable
<strong>fanfare</strong>, with television cameras trailing government officials meandering proudly around the bright new stores filled with imported goods.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=139e533772f86ecc1531f7c65fad466f" rel="nofollow">New York Times (Aug 22, 2010)</a></div>


</li>






<li class="entry learnable" id="entry842"
 lang="en" word="dilettante" freq="6015.92" prog="0">

<a class="word dynamictext" href="/dictionary/dilettante">dilettante</a>
<div class="definition">showing frivolous or superficial interest; amateurish</div>
<div class="example">They dabbled in politics and art in the same
<strong>dilettante</strong> fashion.
<br> —
<a href="http://www.gutenberg.org/ebooks/7967" rel="nofollow">Cannan, Gilbert</a></div>


</li>






<li class="entry learnable" id="entry843"
 lang="en" word="pusillanimous" freq="6028.19" prog="0">

<a class="word dynamictext" href="/dictionary/pusillanimous">pusillanimous</a>
<div class="definition">lacking in courage and manly strength and resolution</div>
<div class="example">He was described by his friends as
<strong>pusillanimous</strong> to an incredible extent, timid from excess of riches, afraid of his own shadow.
<br> —
<a href="http://www.gutenberg.org/ebooks/4900" rel="nofollow">Motley, John Lothrop</a></div>


</li>






<li class="entry learnable" id="entry844"
 lang="en" word="ingrained" freq="6034.34" prog="0">

<a class="word dynamictext" href="/dictionary/ingrained">ingrained</a>
<div class="definition">deeply rooted; firmly fixed or held</div>
<div class="example">The narrow prejudices of his country were
<strong>ingrained</strong> too deeply in his character to be disturbed by any change of surroundings.
<br> —
<a href="http://www.gutenberg.org/ebooks/37576" rel="nofollow">Fuller, Robert H.</a></div>


</li>






<li class="entry learnable" id="entry845"
 lang="en" word="quagmire" freq="6043.59" prog="0">

<a class="word dynamictext" href="/dictionary/quagmire">quagmire</a>
<div class="definition">a soft wet area of low-lying land that sinks underfoot</div>
<div class="example">The heavy rain had reduced this low-lying ground to a veritable
<strong>quagmire</strong>, making progress very difficult even for one as unburdened as he was.
<br> —
<a href="http://www.gutenberg.org/ebooks/37376" rel="nofollow">Putnam Weale, B. L. (Bertram Lenox)</a></div>


</li>






<li class="entry learnable" id="entry846"
 lang="en" word="reprobation" freq="6071.52" prog="0">

<a class="word dynamictext" href="/dictionary/reprobation">reprobation</a>
<div class="definition">severe disapproval</div>
<div class="example">Mr. Conway denounced this scheme as "utterly and flagrantly unconstitutional, as radically revolutionary in character and deserving the
<strong>reprobation</strong> of every loyal citizen."
<br> —
<a href="http://www.gutenberg.org/ebooks/21128" rel="nofollow">Blaine, James Gillespie</a></div>


</li>






<li class="entry learnable" id="entry847"
 lang="en" word="mannered" freq="6090.29" prog="0">

<a class="word dynamictext" href="/dictionary/mannered">mannered</a>
<div class="definition">having unnatural behavioral attributes</div>
<div class="example">Nothing was
<strong>mannered</strong> or pretentious; the texts came through with utter naturalness.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=858f378f393f8b1804e5bc0f1d6f5e4c" rel="nofollow">New York Times (May 29, 2011)</a></div>


</li>






<li class="entry learnable" id="entry848"
 lang="en" word="squeamish" freq="6137.71" prog="0">

<a class="word dynamictext" href="/dictionary/squeamish">squeamish</a>
<div class="definition">excessively fastidious and easily disgusted</div>
<div class="example">But please note that this gunfire-fueled film is for mature audiences; given its content, young and/or
<strong>squeamish</strong> viewers should avoid this one.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=5013f795a7df4e38d298096062d53eb2" rel="nofollow">Washington Post (Aug 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry849"
 lang="en" word="proclivity" freq="6169.74" prog="0">

<a class="word dynamictext" href="/dictionary/proclivity">proclivity</a>
<div class="definition">a natural inclination</div>
<div class="example">She received, under her father's supervision, a very careful education, and developed her
<strong>proclivities</strong> for literary composition at an early age.
<br> —
<a href="http://www.gutenberg.org/ebooks/31479" rel="nofollow">Adams, W. H. Davenport</a></div>


</li>






<li class="entry learnable" id="entry850"
 lang="en" word="miserly" freq="6202.11" prog="0">

<a class="word dynamictext" href="/dictionary/miserly">miserly</a>
<div class="definition">characterized by or indicative of lack of generosity</div>
<div class="example">Now, my uncle seemed so
<strong>miserly</strong> that I was struck dumb by this sudden generosity, and could find no words in which to thank him.
<br> —
<a href="http://www.gutenberg.org/ebooks/31916" rel="nofollow">Stevenson, Robert Louis</a></div>


</li>






<li class="entry learnable" id="entry851"
 lang="en" word="vapid" freq="6238.1" prog="0">

<a class="word dynamictext" href="/dictionary/vapid">vapid</a>
<div class="definition">lacking significance or liveliness or spirit or zest</div>
<div class="example">How
<strong>vapid</strong> was the talk of my remaining fellow-passengers; how slow of understanding, and how preoccupied with petty things they seemed!
<br> —
<a href="http://www.gutenberg.org/ebooks/30704" rel="nofollow">Dawson, A. J. (Alec John)</a></div>


</li>






<li class="entry learnable" id="entry852"
 lang="en" word="mercurial" freq="6241.4" prog="0">

<a class="word dynamictext" href="/dictionary/mercurial">mercurial</a>
<div class="definition">liable to sudden unpredictable change</div>
<div class="example">Wind energy is notoriously
<strong>mercurial</strong>, with patterns shifting drastically over the course of years, days, even minutes.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=9a165be250b8c0d3d54d7c2a44e78df8" rel="nofollow">Scientific American (Jan 4, 2012)</a></div>


</li>






<li class="entry learnable" id="entry853"
 lang="en" word="perspicuous" freq="6277.85" prog="0">

<a class="word dynamictext" href="/dictionary/perspicuous">perspicuous</a>
<div class="definition">transparently clear; easily understandable</div>
<div class="example">The statements are plain and simple, a perfect model of
<strong>perspicuous</strong> narrative.
<br> —
<a href="http://www.gutenberg.org/ebooks/27197" rel="nofollow">Smith, Uriah</a></div>


</li>






<li class="entry learnable" id="entry854"
 lang="en" word="nonplus" freq="6308" prog="0">

<a class="word dynamictext" href="/dictionary/nonplus">nonplus</a>
<div class="definition">be a mystery or bewildering to</div>
<div class="example">I shook my head and rushed from his presence, completely
<strong>nonplussed</strong>, bewildered, frantic.
<br> —
<a href="http://www.gutenberg.org/ebooks/30726" rel="nofollow">Cole, E. W. (Edward William)</a></div>


</li>






<li class="entry learnable" id="entry855"
 lang="en" word="enamor" freq="6321.49" prog="0">

<a class="word dynamictext" href="/dictionary/enamor">enamor</a>
<div class="definition">attract</div>
<div class="example">Young Indian audiences are so
<strong>enamored</strong> with reality television that they will not watch the soap operas and dramas that their parents or grandparents watch.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b657f3c7d652afd0591c18f96601f138" rel="nofollow">New York Times (Jan 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry856"
 lang="en" word="hackneyed" freq="6328.25" prog="0">

<a class="word dynamictext" href="/dictionary/hackneyed">hackneyed</a>
<div class="definition">repeated too often; overfamiliar through overuse</div>
<div class="example">Many speakers become so addicted to certain
<strong>hackneyed</strong> phrases that those used to hearing them speak can see them coming sentences away.
<br> —
<a href="http://www.gutenberg.org/ebooks/30565" rel="nofollow">Lewis, Arthur M. (Arthur Morrow)</a></div>


</li>






<li class="entry learnable" id="entry857"
 lang="en" word="spate" freq="6345.24" prog="0">

<a class="word dynamictext" href="/dictionary/spate">spate</a>
<div class="definition">a large number or amount or extent</div>
<div class="example">French authorities are already reporting a rising
<strong>spate</strong> of calls to emergency services by homeowners whose once-frozen water mains have now burst.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/oiVfXROhnls/" rel="nofollow">Time (Feb 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry858"
 lang="en" word="pedagogue" freq="6376.03" prog="0">

<a class="word dynamictext" href="/dictionary/pedagogue">pedagogue</a>
<div class="definition">someone who educates young people</div>
<div class="example">His old
<strong>pedagogue</strong>, Mr. Brownell, had been unable to teach him mathematics.
<br> —
<a href="http://www.gutenberg.org/ebooks/26442" rel="nofollow">Pierce, H. Winthrop</a></div>


</li>






<li class="entry learnable" id="entry859"
 lang="en" word="acme" freq="6424.54" prog="0">

<a class="word dynamictext" href="/dictionary/acme">acme</a>
<div class="definition">the highest level or degree attainable</div>
<div class="example">Scientifically speaking, it is the
<strong>acme</strong> of absurdity to talk of a man defying the law of gravitation when he lifts his arm.
<br> —
<a href="http://www.gutenberg.org/ebooks/34698" rel="nofollow">Huxley, Thomas H.</a></div>


</li>






<li class="entry learnable" id="entry860"
 lang="en" word="masticate" freq="6424.54" prog="0">

<a class="word dynamictext" href="/dictionary/masticate">masticate</a>
<div class="definition">bite and grind with the teeth</div>
<div class="example">Food should be
<strong>masticated</strong> quietly, and with the lips closed.
<br> —
<a href="http://www.gutenberg.org/ebooks/28998" rel="nofollow">Cooke, Maud C.</a></div>


</li>






<li class="entry learnable" id="entry861"
 lang="en" word="sinecure" freq="6495.13" prog="0">

<a class="word dynamictext" href="/dictionary/sinecure">sinecure</a>
<div class="definition">a job that involves minimal duties</div>
<div class="example">He would have repudiated the notion that he was looking for a
<strong>sinecure</strong>, but no doubt considered that the duties would be easy and light.
<br> —
<a href="http://www.gutenberg.org/ebooks/18645" rel="nofollow">Trollope, Anthony</a></div>


</li>






<li class="entry learnable" id="entry862"
 lang="en" word="indite" freq="6513.02" prog="0">

<a class="word dynamictext" href="/dictionary/indite">indite</a>
<div class="definition">produce a literary work</div>
<div class="example">She
<strong>indited</strong> religious poems which were the admiration of the age.
<br> —
<a href="http://www.gutenberg.org/ebooks/32451" rel="nofollow">Brittain, Alfred</a></div>


</li>






<li class="entry learnable" id="entry863"
 lang="en" word="emetic" freq="6541.85" prog="0">

<a class="word dynamictext" href="/dictionary/emetic">emetic</a>
<div class="definition">a medicine that induces nausea and vomiting</div>
<div class="example">The juice of this herb, taken in ale, is esteemed a gentle and very good
<strong>emetic</strong>, bringing on vomiting without any great irritation or pain.
<br> —
<a href="http://www.gutenberg.org/ebooks/37817" rel="nofollow">Smith, John Thomas</a></div>


</li>






<li class="entry learnable" id="entry864"
 lang="en" word="temporize" freq="6545.47" prog="0">

<a class="word dynamictext" href="/dictionary/temporize">temporize</a>
<div class="definition">draw out a discussion or process in order to gain time</div>
<div class="example">So he
<strong>temporized</strong> and beat about the bush, and did not touch first on that which was nearest his heart.
<br> —
<a href="http://www.gutenberg.org/ebooks/30031" rel="nofollow">Erskine, Payne</a></div>


</li>






<li class="entry learnable" id="entry865"
 lang="en" word="unimpeachable" freq="6570.93" prog="0">

<a class="word dynamictext" href="/dictionary/unimpeachable">unimpeachable</a>
<div class="definition">beyond doubt or reproach</div>
<div class="example">Whether we agree with the conclusions of these writers or not, the method of critical investigation which they adopt is
<strong>unimpeachable</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/34698" rel="nofollow">Huxley, Thomas H.</a></div>


</li>






<li class="entry learnable" id="entry866"
 lang="en" word="genesis" freq="6581.91" prog="0">

<a class="word dynamictext" href="/dictionary/genesis">genesis</a>
<div class="definition">a coming into being</div>
<div class="example">He found himself speculating on the
<strong>genesis</strong> of the moral sense, how it developed in difficulties rather than in ease.
<br> —
<a href="http://www.gutenberg.org/ebooks/33145" rel="nofollow">Miller, Alice Duer</a></div>


</li>






<li class="entry learnable" id="entry867"
 lang="en" word="mordant" freq="6589.24" prog="0">

<a class="word dynamictext" href="/dictionary/mordant">mordant</a>
<div class="definition">harshly ironic or sinister</div>
<div class="example">Even Morgan himself, intrepid as he was, shrank from the awful menace of the
<strong>mordant</strong> words.
<br> —
<a href="http://www.gutenberg.org/ebooks/29316" rel="nofollow">Crawford, Will</a></div>


</li>






<li class="entry learnable" id="entry868"
 lang="en" word="smattering" freq="6603.97" prog="0">

<a class="word dynamictext" href="/dictionary/smattering">smattering</a>
<div class="definition">a small number or amount</div>
<div class="example">Only a
<strong>smattering</strong> of fans remained for all four ghastly quarters.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=edbaf8d353278c60b70728d00710879d" rel="nofollow">Washington Post (Sep 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry869"
 lang="en" word="suavity" freq="6626.17" prog="0">

<a class="word dynamictext" href="/dictionary/suavity">suavity</a>
<div class="definition">the quality of being charming and gracious in manner</div>
<div class="example">His combativeness was harnessed to his
<strong>suavity</strong>, and he could be forcible and at the same time persuasive.
<br> —
<a href="http://www.gutenberg.org/ebooks/21646" rel="nofollow">Windsor, William</a></div>


</li>






<li class="entry learnable" id="entry870"
 lang="en" word="stentorian" freq="6644.79" prog="0">

<a class="word dynamictext" href="/dictionary/stentorian">stentorian</a>
<div class="definition">very loud or booming</div>
<div class="example">If a hundred voices shouted in opposition, his
<strong>stentorian</strong> tones still made themselves heard above the uproar.
<br> —
<a href="http://www.gutenberg.org/ebooks/34674" rel="nofollow">J?kai, M?r</a></div>


</li>






<li class="entry learnable" id="entry871"
 lang="en" word="junket" freq="6671.04" prog="0">

<a class="word dynamictext" href="/dictionary/junket">junket</a>
<div class="definition">a trip taken by an official at public expense</div>
<div class="example">Mr. Abramoff arranged for
<strong>junkets</strong>, including foreign golfing destinations, for the members of Congress he was trying to influence.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4fcef54523141503c2dfaf3086e2d938" rel="nofollow">New York Times (Feb 26, 2010)</a></div>


</li>






<li class="entry learnable" id="entry872"
 lang="en" word="appurtenance" freq="6686.13" prog="0">

<a class="word dynamictext" href="/dictionary/appurtenance">appurtenance</a>
<div class="definition">a supplementary component that improves capability</div>
<div class="example">In the center of this space stood a large frame building whose courtyard, stables, and other
<strong>appurtenances</strong> proclaimed it an inn.
<br> —
<a href="http://www.gutenberg.org/ebooks/30940" rel="nofollow">Madison, Lucy Foster</a></div>


</li>






<li class="entry learnable" id="entry873"
 lang="en" word="nostrum" freq="6712.7" prog="0">

<a class="word dynamictext" href="/dictionary/nostrum">nostrum</a>
<div class="definition">patent medicine whose efficacy is questionable</div>
<div class="example">Just here a native "medicine man" dispenses
<strong>nostrums</strong> of doubtful efficacy, and in front a quantity of red Moorish pottery is exposed for sale.
<br> —
<a href="http://www.gutenberg.org/ebooks/18764" rel="nofollow">Meakin, Budgett</a></div>


</li>






<li class="entry learnable" id="entry874"
 lang="en" word="immure" freq="6739.49" prog="0">

<a class="word dynamictext" href="/dictionary/immure">immure</a>
<div class="definition">lock up or confine, in or as in a jail</div>
<div class="example">Political prisoners, numbering as many as three or four hundred at a time, have been
<strong>immured</strong> within its massive walls.
<br> —
<a href="http://www.gutenberg.org/ebooks/39199" rel="nofollow">Boyd, Mary Stuart</a></div>


</li>






<li class="entry learnable" id="entry875"
 lang="en" word="astringent" freq="6754.89" prog="0">

<a class="word dynamictext" href="/dictionary/astringent">astringent</a>
<div class="definition">sour or bitter in taste</div>
<div class="example">There was something sharply
<strong>astringent</strong> about her then, like biting inadvertently into a green banana.
<br> —
<a href="http://www.gutenberg.org/ebooks/32042" rel="nofollow">McFee, William</a></div>


</li>






<li class="entry learnable" id="entry876"
 lang="en" word="unfaltering" freq="6766.49" prog="0">

<a class="word dynamictext" href="/dictionary/unfaltering">unfaltering</a>
<div class="definition">marked by firm determination or resolution; not shakable</div>
<div class="example">Still
<strong>unfaltering</strong>, the procession commenced to trudge back, the littlest boy and girl bearing themselves bravely, with lips tight pressed.
<br> —
<a href="http://www.gutenberg.org/ebooks/31130" rel="nofollow">Sabin, Edwin L. (Edwin Legrand)</a></div>


</li>






<li class="entry learnable" id="entry877"
 lang="en" word="tutelage" freq="6809.36" prog="0">

<a class="word dynamictext" href="/dictionary/tutelage">tutelage</a>
<div class="definition">attention and management implying responsibility for safety</div>
<div class="example">It will do so under German leadership that grows less hesitant with each crisis, and without the American
<strong>tutelage</strong> it enjoyed for so many decades.
<br> —
<a href="http://www.newsweek.com/2011/01/23/to-rule-the-euro-zone.html" rel="nofollow">Newsweek (Jan 23, 2011)</a></div>


</li>






<li class="entry learnable" id="entry878"
 lang="en" word="testator" freq="6825.08" prog="0">

<a class="word dynamictext" href="/dictionary/testator">testator</a>
<div class="definition">a person who makes a will</div>
<div class="example">This will was drawn up by me some years since at the request of the
<strong>testator</strong>, who was in good health, mentally and bodily.
<br> —
<a href="http://www.gutenberg.org/ebooks/35012" rel="nofollow">Henty, G. A. (George Alfred)</a></div>


</li>






<li class="entry learnable" id="entry879"
 lang="en" word="elysian" freq="6832.97" prog="0">

<a class="word dynamictext" href="/dictionary/elysian">elysian</a>
<div class="definition">of such excellence as to suggest inspiration by the gods</div>
<div class="example">Life seemed an
<strong>elysian</strong> dream, from which care and sorrow must be for ever banished.
<br> —
<a href="http://www.gutenberg.org/ebooks/20462" rel="nofollow">Hentz, Caroline Lee</a></div>


</li>






<li class="entry learnable" id="entry880"
 lang="en" word="fulminate" freq="6840.88" prog="0">

<a class="word dynamictext" href="/dictionary/fulminate">fulminate</a>
<div class="definition">criticize severely</div>
<div class="example">But with people looking for almost any excuse to
<strong>fulminate</strong> against airlines these days, there's a certain risk of embellishment.
<br> —
<a href="http://www.salon.com/tech/col/smith/2010/06/25/virgin_atlantic_stranding/index.html" rel="nofollow">Salon (Jun 25, 2010)</a></div>


</li>






<li class="entry learnable" id="entry881"
 lang="en" word="fractious" freq="6848.8" prog="0">

<a class="word dynamictext" href="/dictionary/fractious">fractious</a>
<div class="definition">easily irritated or annoyed</div>
<div class="example">He was a
<strong>fractious</strong> invalid, and spared his wife neither time nor trouble in attending to his wants.
<br> —
<a href="http://www.gutenberg.org/ebooks/33910" rel="nofollow">Brazil, Angela</a></div>


</li>






<li class="entry learnable" id="entry882"
 lang="en" word="pummel" freq="6852.77" prog="0">

<a class="word dynamictext" href="/dictionary/pummel">pummel</a>
<div class="definition">strike, usually with the fist</div>
<div class="example">Another, with rubber bands wrapped tightly around his face, is
<strong>pummelled</strong> by a plastic boxing kangaroo.
<br> —
<a href="http://www.guardian.co.uk/stage/2011/jan/23/gobo-digital-glossary-giselle-review" rel="nofollow">The Guardian (Jan 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry883"
 lang="en" word="manumit" freq="6856.75" prog="0">

<a class="word dynamictext" href="/dictionary/manumit">manumit</a>
<div class="definition">free from slavery or servitude</div>
<div class="example">Moreover,
<strong>manumitted</strong> slaves enjoyed the same rights, privileges and immunities that were enjoyed by those born free.
<br> —
<a href="http://www.gutenberg.org/ebooks/13642" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry884"
 lang="en" word="unexceptionable" freq="6864.71" prog="0">

<a class="word dynamictext" href="/dictionary/unexceptionable">unexceptionable</a>
<div class="definition">completely acceptable; not open to reproach</div>
<div class="example">All cowboys are from necessity good cooks, and the fluffy, golden brown biscuits and fragrant coffee of Red's making were
<strong>unexceptionable</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/31930" rel="nofollow">Mayer, Frank</a></div>


</li>






<li class="entry learnable" id="entry885"
 lang="en" word="triumvirate" freq="6888.71" prog="0">

<a class="word dynamictext" href="/dictionary/triumvirate">triumvirate</a>
<div class="definition">a group of three people responsible for civil authority</div>
<div class="example">This
<strong>triumvirate</strong> approach has real benefits in terms of shared wisdom, and we will continue to discuss the big decisions among the three of us.
<br> —
<a href="http://www.salon.com/tech/feature/2011/01/20/new_google_ceo_page/index.html" rel="nofollow">Salon (Jan 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry886"
 lang="en" word="sybarite" freq="6920.97" prog="0">

<a class="word dynamictext" href="/dictionary/sybarite">sybarite</a>
<div class="definition">a person addicted to luxury and pleasures of the senses</div>
<div class="example">He was not used to travelling on omnibuses, being something of a
<strong>sybarite</strong> who spared nothing to ensure his own comfort.
<br> —
<a href="http://www.gutenberg.org/ebooks/20912" rel="nofollow">Wallace, Edgar</a></div>


</li>






<li class="entry learnable" id="entry887"
 lang="en" word="jibe" freq="6949.45" prog="0">

<a class="word dynamictext" href="/dictionary/jibe">jibe</a>
<div class="definition">be compatible, similar or consistent</div>
<div class="example">Contemporary art has never quite
<strong>jibed</strong> with mainstream media.
<br> —
<a href="http://www.salon.com/ent/tv/2010/07/06/work_of_art_glen_helfand/index.html" rel="nofollow">Salon (Jul 6, 2010)</a></div>


</li>






<li class="entry learnable" id="entry888"
 lang="en" word="magisterial" freq="6953.54" prog="0">

<a class="word dynamictext" href="/dictionary/magisterial">magisterial</a>
<div class="definition">offensively self-assured or exercising unwarranted power</div>
<div class="example">“Now look here,” he said, making believe to take down my words and shaking his pencil at me in a
<strong>magisterial</strong> way.
<br> —
<a href="http://www.gutenberg.org/ebooks/36852" rel="nofollow">Fenn, George Manville</a></div>


</li>






<li class="entry learnable" id="entry889"
 lang="en" word="roseate" freq="6969.93" prog="0">

<a class="word dynamictext" href="/dictionary/roseate">roseate</a>
<div class="definition">of something having a dusty purplish pink color</div>
<div class="example">Behind the trees rough, lichened rock and stony slopes ran up to a bare ridge, silhouetted against the
<strong>roseate</strong> glow of the morning sky.
<br> —
<a href="http://www.gutenberg.org/ebooks/25910" rel="nofollow">Bindloss, Harold</a></div>


</li>






<li class="entry learnable" id="entry890"
 lang="en" word="obloquy" freq="7011.27" prog="0">

<a class="word dynamictext" href="/dictionary/obloquy">obloquy</a>
<div class="definition">a false accusation of an offense</div>
<div class="example">This is the real history of a transaction which, by frequent misrepresentation, has brought undeserved
<strong>obloquy</strong> upon a generous man.
<br> —
<a href="http://www.gutenberg.org/ebooks/31234" rel="nofollow">Purchas, H. T. (Henry Thomas)</a></div>


</li>






<li class="entry learnable" id="entry891"
 lang="en" word="hoodwink" freq="7023.76" prog="0">

<a class="word dynamictext" href="/dictionary/hoodwink">hoodwink</a>
<div class="definition">influence by slyness</div>
<div class="example">The stories of the saints he regarded as preposterous fables invented to
<strong>hoodwink</strong> a gullible and illiterate populace.
<br> —
<a href="http://www.guardian.co.uk/artanddesign/2010/sep/19/germaine-greer-catholic-art-papal-visit" rel="nofollow">The Guardian (Sep 19, 2010)</a></div>


</li>






<li class="entry learnable" id="entry892"
 lang="en" word="striate" freq="7078.43" prog="0">

<a class="word dynamictext" href="/dictionary/striate">striate</a>
<div class="definition">mark with stripes of contrasting color</div>
<div class="example">The body is
<strong>striated</strong> with clearly defined, often depressed lines, which run longitudinally and sometimes spirally.
<br> —
<a href="http://www.gutenberg.org/ebooks/18320" rel="nofollow">Calkins, Gary N. (Gary Nathan)</a></div>


</li>






<li class="entry learnable" id="entry893"
 lang="en" word="arrogate" freq="7086.92" prog="0">

<a class="word dynamictext" href="/dictionary/arrogate">arrogate</a>
<div class="definition">seize and take control without authority</div>
<div class="example">Japanese manufacturers were accused of
<strong>arrogating</strong> American technologies to churn out low-cost electronics.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=56eda0cae3ca151e5925695d189d42d6" rel="nofollow">New York Times (May 25, 2010)</a></div>


</li>






<li class="entry learnable" id="entry894"
 lang="en" word="rarefied" freq="7142.58" prog="0">

<a class="word dynamictext" href="/dictionary/rarefied">rarefied</a>
<div class="definition">of high moral or intellectual value</div>
<div class="example">The debate over climate science has involved very complex physical models and
<strong>rarefied</strong> areas of scientific knowledge.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=57078153cac95953eb40f34b1d0145c9" rel="nofollow">New York Times (Apr 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry895"
 lang="en" word="chary" freq="7296.87" prog="0">

<a class="word dynamictext" href="/dictionary/chary">chary</a>
<div class="definition">characterized by great caution</div>
<div class="example">There was no independent verification of the figure; the authorities have been
<strong>chary</strong> of releasing death tolls for fear of inflaming further violence.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=a40c6d71ed1613cff14ba7d900dd439f" rel="nofollow">New York Times (Apr 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry896"
 lang="en" word="credo" freq="7305.89" prog="0">

<a class="word dynamictext" href="/dictionary/credo">credo</a>
<div class="definition">any system of principles or beliefs</div>
<div class="example">She preferred to hang out with everyone but was best friends with no one, holding to the
<strong>credo</strong>: “You should be nice to people.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=7d4ee5126e489c267fe5dad63fde2683" rel="nofollow">New York Times (Jan 21, 2011)</a></div>


</li>






<li class="entry learnable" id="entry897"
 lang="en" word="superannuated" freq="7319.46" prog="0">

<a class="word dynamictext" href="/dictionary/superannuated">superannuated</a>
<div class="definition">too old to be useful</div>
<div class="example">Civil servants are
<strong>superannuated</strong> at fifty-five years of age and are sent home on a pension, seldom enjoying life longer than two years afterward.
<br> —
<a href="http://www.gutenberg.org/ebooks/33079" rel="nofollow">Hunt, Eleonora</a></div>


</li>






<li class="entry learnable" id="entry898"
 lang="en" word="impolitic" freq="7333.08" prog="0">

<a class="word dynamictext" href="/dictionary/impolitic">impolitic</a>
<div class="definition">not marked by artful prudence</div>
<div class="example">Bill Maher has always been a vocal critic of Islam, even at times making
<strong>impolitic</strong> statements about the religion.
<br> —
<a href="http://www.salon.com/news/feature/2011/03/16/james_madison_birthday/index.html" rel="nofollow">Salon (Mar 16, 2011)</a></div>


</li>






<li class="entry learnable" id="entry899"
 lang="en" word="aspersion" freq="7342.19" prog="0">

<a class="word dynamictext" href="/dictionary/aspersion">aspersion</a>
<div class="definition">a disparaging remark</div>
<div class="example">Lord Sanquhar then proceeded to deny the
<strong>aspersion</strong> that he was an ill-natured fellow, ever revengeful, and delighting in blood.
<br> —
<a href="http://www.gutenberg.org/ebooks/31412" rel="nofollow">Thornbury, Walter</a></div>


</li>






<li class="entry learnable" id="entry900"
 lang="en" word="abysmal" freq="7346.75" prog="0">

<a class="word dynamictext" href="/dictionary/abysmal">abysmal</a>
<div class="definition">resembling an abyss in depth; so deep as to be immeasurable</div>
<div class="example">After all, many Americans regard this Congress as dysfunctional, with
<strong>abysmal</strong> approval ratings.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=b8eb78d7ecb2b00d1cc4113e87457c54" rel="nofollow">New York Times (Dec 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry901"
 lang="en" word="poignancy" freq="7365.06" prog="0">

<a class="word dynamictext" href="/dictionary/poignancy">poignancy</a>
<div class="definition">a quality that arouses emotions, especially pity or sorrow</div>
<div class="example">They were curious about the “near loss” experience—specifically the feelings of
<strong>poignancy</strong> that occur when what we cherish disappears.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=6f1ccfdabd24cabeebd140235c6e655f" rel="nofollow">Scientific American (Jan 17, 2011)</a></div>


</li>






<li class="entry learnable" id="entry902"
 lang="en" word="stilted" freq="7411.23" prog="0">

<a class="word dynamictext" href="/dictionary/stilted">stilted</a>
<div class="definition">artificially formal</div>
<div class="example">But thanks to the
<strong>stilted</strong> writing and stiff acting, the characters still feel very much like one-dimensional figures from a dutiful fable.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=f7868024490f53f6cb4cf02a0206762c" rel="nofollow">New York Times (Jul 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry903"
 lang="en" word="effete" freq="7420.53" prog="0">

<a class="word dynamictext" href="/dictionary/effete">effete</a>
<div class="definition">excessively self-indulgent, affected, or decadent</div>
<div class="example">John Bull was an
<strong>effete</strong> old plutocrat whose sons and daughters were given up to sport and amusement.
<br> —
<a href="http://www.gutenberg.org/ebooks/8684" rel="nofollow">Moffett, Cleveland</a></div>


</li>






<li class="entry learnable" id="entry904"
 lang="en" word="provender" freq="7420.53" prog="0">

<a class="word dynamictext" href="/dictionary/provender">provender</a>
<div class="definition">food for domestic livestock</div>
<div class="example">"Fools!" she cried, looking in her magic crystal, "he was in the big sycamore under which you stopped to give your horses
<strong>provender</strong>!"
<br> —
<a href="http://www.gutenberg.org/ebooks/34852" rel="nofollow">Housman, Laurence</a></div>


</li>






<li class="entry learnable" id="entry905"
 lang="en" word="endemic" freq="7425.19" prog="0">

<a class="word dynamictext" href="/dictionary/endemic">endemic</a>
<div class="definition">of a disease constantly present in a particular locality</div>
<div class="example">Mean-spirited chants and songs are also
<strong>endemic</strong> in British soccer.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/8IXLaIwbCKk/taking-on-soccer-violence-one-derogatory-chant-at-a-time.html" rel="nofollow">New York Times (Jan 27, 2012)</a></div>


</li>






<li class="entry learnable" id="entry906"
 lang="en" word="jocund" freq="7491.06" prog="0">

<a class="word dynamictext" href="/dictionary/jocund">jocund</a>
<div class="definition">full of or showing high-spirited merriment</div>
<div class="example">Her
<strong>jocund</strong> laugh and merry voice, indeed, first attracted my attention.
<br> —
<a href="http://www.gutenberg.org/ebooks/33082" rel="nofollow">Lever, Charles James</a></div>


</li>






<li class="entry learnable" id="entry907"
 lang="en" word="procedural" freq="7500.56" prog="0">

<a class="word dynamictext" href="/dictionary/procedural">procedural</a>
<div class="definition">of or relating to processes</div>
<div class="example">In other words, the rejection was a bureaucratic/
<strong>procedural</strong> decision.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=9f8f694e6286ce68f0ba6fa2f11bd52f" rel="nofollow">Scientific American (Feb 1, 2012)</a></div>


</li>






<li class="entry learnable" id="entry908"
 lang="en" word="rakish" freq="7505.32" prog="0">

<a class="word dynamictext" href="/dictionary/rakish">rakish</a>
<div class="definition">marked by a carefree unconventionality or disreputableness</div>
<div class="example">She wore her red cap in a
<strong>rakish</strong> manner on the side of her head, its tassel falling down over her forehead between her eyes.
<br> —
<a href="http://www.gutenberg.org/ebooks/34846" rel="nofollow">Sage, William</a></div>


</li>






<li class="entry learnable" id="entry909"
 lang="en" word="skittish" freq="7514.87" prog="0">

<a class="word dynamictext" href="/dictionary/skittish">skittish</a>
<div class="definition">unpredictably excitable, especially of horses</div>
<div class="example">That combined with his calm and reassuring tone made me think of an animal trainer trying to woo
<strong>skittish</strong> wild animals.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/quvgMUA-3Fs/" rel="nofollow">Time (May 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry910"
 lang="en" word="peroration" freq="7543.64" prog="0">

<a class="word dynamictext" href="/dictionary/peroration">peroration</a>
<div class="definition">a flowery and highly rhetorical address</div>
<div class="example">He had little hope that Gallagher, once embarked on a
<strong>peroration</strong>, would stop until he had used up all the words at his command.
<br> —
<a href="http://www.gutenberg.org/ebooks/24073" rel="nofollow">Birmingham, George A.</a></div>


</li>






<li class="entry learnable" id="entry911"
 lang="en" word="nonentity" freq="7553.28" prog="0">

<a class="word dynamictext" href="/dictionary/nonentity">nonentity</a>
<div class="definition">a person of no influence</div>
<div class="example">Was he such a
<strong>nonentity</strong> in every way that she could remain unconcerned as to any fear of danger from him?
<br> —
<a href="http://www.gutenberg.org/ebooks/33143" rel="nofollow">Woolson, Constance Fenimore</a></div>


</li>






<li class="entry learnable" id="entry912"
 lang="en" word="abstemious" freq="7558.1" prog="0">

<a class="word dynamictext" href="/dictionary/abstemious">abstemious</a>
<div class="definition">marked by temperance in indulgence</div>
<div class="example">Raw, boozy, untethered performances are heralded as real; the
<strong>abstemious</strong> professional is yawned off the stage.
<br> —
<a href="http://www.salon.com/ent/music/feature/2011/07/25/amy_winehouse_authenticity_trap/index.html" rel="nofollow">Salon (Jul 25, 2011)</a></div>


</li>






<li class="entry learnable" id="entry913"
 lang="en" word="viscid" freq="7562.94" prog="0">

<a class="word dynamictext" href="/dictionary/viscid">viscid</a>
<div class="definition">having the sticky properties of an adhesive</div>
<div class="example">Roads were quagmires where travellers slipped and laboured through
<strong>viscid</strong> mud and over icy fords.
<br> —
<a href="http://www.gutenberg.org/ebooks/33736" rel="nofollow">Buck, Charles Neville</a></div>


</li>






<li class="entry learnable" id="entry914"
 lang="en" word="doggerel" freq="7592.08" prog="0">

<a class="word dynamictext" href="/dictionary/doggerel">doggerel</a>
<div class="definition">a comic verse of irregular measure</div>
<div class="example">He sang, with accompanying action, some dozen verses of
<strong>doggerel</strong>, remarkable for obscenity and imbecility.&nbsp;
<br> —
<a href="http://www.gutenberg.org/ebooks/32774" rel="nofollow">Ritchie, J. Ewing (James Ewing)</a></div>


</li>






<li class="entry learnable" id="entry915"
 lang="en" word="sleight" freq="7596.96" prog="0">

<a class="word dynamictext" href="/dictionary/sleight">sleight</a>
<div class="definition">adroitness in using the hands</div>
<div class="example">The trick was performed Tuesday by Russell Fitzgerald, an amateur magician known to open meetings with a little
<strong>sleight</strong> of hand.
<br> —
<a href="http://feeds.washingtonpost.com/click.phdo?i=d9b43eba0d57230b2427aa8b55fa85f9" rel="nofollow">Washington Post (Sep 29, 2011)</a></div>


</li>






<li class="entry learnable" id="entry916"
 lang="en" word="rubric" freq="7636.21" prog="0">

<a class="word dynamictext" href="/dictionary/rubric">rubric</a>
<div class="definition">category name</div>
<div class="example">Ms. Moss took issue, not surprisingly, with the notion that grouping the performances under the
<strong>rubric</strong> of spirituality was a marketing ploy.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=7db171adebeeef3a222bf4f4d19865e4" rel="nofollow">New York Times (Nov 22, 2010)</a></div>


</li>






<li class="entry learnable" id="entry917"
 lang="en" word="plenitude" freq="7675.88" prog="0">

<a class="word dynamictext" href="/dictionary/plenitude">plenitude</a>
<div class="definition">a full supply</div>
<div class="example">Of course at that season, amid the
<strong>plenitude</strong> of seeds, nuts, and berries, they were as plump as partridges.
<br> —
<a href="http://www.gutenberg.org/ebooks/23499" rel="nofollow">Reid, Mayne</a></div>


</li>






<li class="entry learnable" id="entry918"
 lang="en" word="rebus" freq="7705.9" prog="0">

<a class="word dynamictext" href="/dictionary/rebus">rebus</a>
<div class="definition">a puzzle consisting of pictures representing words</div>
<div class="example">They wrote at times with pictures standing for sounds, as we now write in
<strong>rebus</strong> puzzles.
<br> —
<a href="http://www.gutenberg.org/ebooks/28496" rel="nofollow">Park, Robert Ezra</a></div>


</li>






<li class="entry learnable" id="entry919"
 lang="en" word="wizened" freq="7715.95" prog="0">

<a class="word dynamictext" href="/dictionary/wizened">wizened</a>
<div class="definition">lean and wrinkled by shrinkage as from age or illness</div>
<div class="example">Kim Jong Il may be increasingly
<strong>wizened</strong> and frail, with fingernails white from kidney disease, but his propaganda apparatus is as vigorous as ever.
<br> —
<a href="http://online.wsj.com/article/SB10001424052748704100604575145672974954144.html?mod=fox_australian" rel="nofollow">Wall Street Journal (Mar 26, 2010)</a></div>


</li>






<li class="entry learnable" id="entry920"
 lang="en" word="whorl" freq="7731.09" prog="0">

<a class="word dynamictext" href="/dictionary/whorl">whorl</a>
<div class="definition">a round shape formed by a series of concentric circles</div>
<div class="example">The flowers are waxy, tubular, fragrant, turning their yellow petals backward in a
<strong>whorl</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/37717" rel="nofollow">Rogers, Julia Ellen</a></div>


</li>






<li class="entry learnable" id="entry921"
 lang="en" word="fracas" freq="7736.15" prog="0">

<a class="word dynamictext" href="/dictionary/fracas">fracas</a>
<div class="definition">noisy quarrel</div>
<div class="example">Other cops were battling each other, going after the kids and clutching empty air, cursing and screaming unheard orders in the
<strong>fracas</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/24444" rel="nofollow">Freas, Kelly</a></div>


</li>






<li class="entry learnable" id="entry922"
 lang="en" word="iconoclast" freq="7766.64" prog="0">

<a class="word dynamictext" href="/dictionary/iconoclast">iconoclast</a>
<div class="definition">someone who attacks cherished ideas or institutions</div>
<div class="example">Jobs is a classic
<strong>iconoclast</strong>, one who aggressively seeks out, attacks, and overthrows conventional ideas.
<br> —
<a href="http://www.businessweek.com/smallbiz/content/oct2010/sb20101011_324657.htm" rel="nofollow">BusinessWeek (Oct 12, 2010)</a></div>


</li>






<li class="entry learnable" id="entry923"
 lang="en" word="saturnine" freq="7828.36" prog="0">

<a class="word dynamictext" href="/dictionary/saturnine">saturnine</a>
<div class="definition">bitter or scornful</div>
<div class="example">Only when Bill Lightfoot spoke did he look up, and then with a set sneer, growing daily more
<strong>saturnine</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/29642" rel="nofollow">Dixon, Maynard</a></div>


</li>






<li class="entry learnable" id="entry924"
 lang="en" word="madrigal" freq="7864.81" prog="0">

<a class="word dynamictext" href="/dictionary/madrigal">madrigal</a>
<div class="definition">an unaccompanied partsong for several voices</div>
<div class="example">Nevertheless we learn from Malvezzi's publication that the pieces were all written in the
<strong>madrigal</strong> style, frequently in numerous voice parts.
<br> —
<a href="http://www.gutenberg.org/ebooks/19958" rel="nofollow">Henderson, W. J. (William James)</a></div>


</li>






<li class="entry learnable" id="entry925"
 lang="en" word="discursive" freq="7875.29" prog="0">

<a class="word dynamictext" href="/dictionary/discursive">discursive</a>
<div class="definition">tending to cover a wide range of subjects</div>
<div class="example">“Tabloid,” like his previous films, consists largely of long,
<strong>discursive</strong> conversations — in effect monologues directed at an unseen, mostly unheard interlocutor.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=05334258d1389cc7ccdf7c0a4c42378c" rel="nofollow">New York Times (Jul 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry926"
 lang="en" word="zealot" freq="7928.1" prog="0">

<a class="word dynamictext" href="/dictionary/zealot">zealot</a>
<div class="definition">a fervent and even militant proponent of something</div>
<div class="example">"The public is going to just think of us as these
<strong>zealots</strong> who want to ban smoking everywhere," he said.
<br> —
<a href="http://seattletimes.nwsource.com/html/health/2014284991_apusnycsmokingban.html?syndication=rss" rel="nofollow">Seattle Times (Feb 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry927"
 lang="en" word="moribund" freq="7944.09" prog="0">

<a class="word dynamictext" href="/dictionary/moribund">moribund</a>
<div class="definition">not growing or changing; without force or vitality</div>
<div class="example">The entertainment sector there is booming, while Pakistan's is
<strong>moribund</strong>.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2016924304_apaspakistanindiaphoto.html?syndication=rss" rel="nofollow">Seattle Times (Dec 3, 2011)</a></div>


</li>






<li class="entry learnable" id="entry928"
 lang="en" word="modicum" freq="7944.09" prog="0">

<a class="word dynamictext" href="/dictionary/modicum">modicum</a>
<div class="definition">a small or moderate or token amount</div>
<div class="example">He volunteered a
<strong>modicum</strong> of advice, limited in quantity, but valuable.
<br> —
<a href="http://www.gutenberg.org/ebooks/34240" rel="nofollow">Bolderwood, Rolf</a></div>


</li>






<li class="entry learnable" id="entry929"
 lang="en" word="connotation" freq="7949.43" prog="0">

<a class="word dynamictext" href="/dictionary/connotation">connotation</a>
<div class="definition">an idea that is implied or suggested</div>
<div class="example">In Arabic, the word “bayt” translates literally as house, but its
<strong>connotations</strong> resonate beyond rooms and walls, summoning longings gathered about family and home.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=5e3a5cba9b72f041b382d86c58442a8a" rel="nofollow">New York Times (Feb 18, 2012)</a></div>


</li>






<li class="entry learnable" id="entry930"
 lang="en" word="adventitious" freq="7965.5" prog="0">

<a class="word dynamictext" href="/dictionary/adventitious">adventitious</a>
<div class="definition">associated by chance and not an integral part</div>
<div class="example">The derivation of the word thus appears to be merely accidental and
<strong>adventitious</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/33411" rel="nofollow">Stace, W. T. (Walter Terence)</a></div>


</li>






<li class="entry learnable" id="entry931"
 lang="en" word="recondite" freq="8008.66" prog="0">

<a class="word dynamictext" href="/dictionary/recondite">recondite</a>
<div class="definition">difficult to penetrate</div>
<div class="example">The mystery of verse is like other abstruse and
<strong>recondite</strong> mysteries—it strikes the ordinary fleshly man as absurd.
<br> —
<a href="http://www.gutenberg.org/ebooks/18649" rel="nofollow">Gosse, Edmund</a></div>


</li>






<li class="entry learnable" id="entry932"
 lang="en" word="zephyr" freq="8052.3" prog="0">

<a class="word dynamictext" href="/dictionary/zephyr">zephyr</a>
<div class="definition">a slight wind</div>
<div class="example">The dwellings and public buildings throughout Cuba are planned to give free passage to every
<strong>zephyr</strong> that wafts relief from the oppressive heat.
<br> —
<a href="http://www.gutenberg.org/ebooks/31908" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry933"
 lang="en" word="countermand" freq="8057.79" prog="0">

<a class="word dynamictext" href="/dictionary/countermand">countermand</a>
<div class="definition">cancel officially</div>
<div class="example">In the midst of executing this order, he got another order
<strong>countermanding</strong> it, and proceeding directly from his direct superior.
<br> —
<a href="http://www.gutenberg.org/ebooks/32332" rel="nofollow">Belloc, Hilaire</a></div>


</li>






<li class="entry learnable" id="entry934"
 lang="en" word="captious" freq="8063.29" prog="0">

<a class="word dynamictext" href="/dictionary/captious">captious</a>
<div class="definition">tending to find and call attention to faults</div>
<div class="example">Miss Burton had been very irritable and
<strong>captious</strong> in class, more so even than usual, and most of her anger was vented upon Gerry.
<br> —
<a href="http://www.gutenberg.org/ebooks/33270" rel="nofollow">Chaundler, Christine</a></div>


</li>






<li class="entry learnable" id="entry935"
 lang="en" word="cognate" freq="8079.82" prog="0">

<a class="word dynamictext" href="/dictionary/cognate">cognate</a>
<div class="definition">having the same ancestral language</div>
<div class="example">The synonyms are also given in the
<strong>cognate</strong> dialects of Welsh, Armoric, Irish, Gaelic, and Manx, showing at one view the connection between them.&nbsp;
<br> —
<a href="http://www.gutenberg.org/ebooks/26192" rel="nofollow">Jenner, Henry</a></div>


</li>






<li class="entry learnable" id="entry936"
 lang="en" word="forebear" freq="8124.24" prog="0">

<a class="word dynamictext" href="/dictionary/forebear">forebear</a>
<div class="definition">a person from whom you are descended</div>
<div class="example">His
<strong>forebears</strong> were Greek immigrants who opened a small sandwich shop in Brooklyn, then moved, one after another, to Providence, to sell distinct, delectable wieners.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=134ec6ef707ceedc3971736474a77948" rel="nofollow">New York Times (Sep 24, 2010)</a></div>


</li>






<li class="entry learnable" id="entry937"
 lang="en" word="cadaverous" freq="8146.63" prog="0">

<a class="word dynamictext" href="/dictionary/cadaverous">cadaverous</a>
<div class="definition">very thin especially from disease or hunger or cold</div>
<div class="example">He looked gaunt and
<strong>cadaverous</strong>, and much of his old reckless joyousness had left him, though he brightened up wonderfully on seeing an old friend.
<br> —
<a href="http://www.gutenberg.org/ebooks/34797" rel="nofollow">Doyle, A. Conan</a></div>


</li>






<li class="entry learnable" id="entry938"
 lang="en" word="foist" freq="8157.87" prog="0">

<a class="word dynamictext" href="/dictionary/foist">foist</a>
<div class="definition">to force onto another</div>
<div class="example">Mr. Knoll added that the 3-D “Star Wars” movies are not “going to be
<strong>foisted</strong> on anybody against their will.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=2aabd723d8499c526256f2984e67607e" rel="nofollow">New York Times (Sep 29, 2010)</a></div>


</li>






<li class="entry learnable" id="entry939"
 lang="en" word="dotage" freq="8191.79" prog="0">

<a class="word dynamictext" href="/dictionary/dotage">dotage</a>
<div class="definition">mental infirmity as a consequence of old age</div>
<div class="example">He is, as you say, a senile old man in his
<strong>dotage</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/12020" rel="nofollow">Wilcox, Ella Wheeler</a></div>


</li>






<li class="entry learnable" id="entry940"
 lang="en" word="nexus" freq="8225.99" prog="0">

<a class="word dynamictext" href="/dictionary/nexus">nexus</a>
<div class="definition">a connected series or group</div>
<div class="example">Numerous innovators are also worrying away at this
<strong>nexus</strong> of problems.
<br> —
<a href="http://www.economist.com/businessfinance/displaystory.cfm?story_id=18618271&amp;fsrc=rss" rel="nofollow">Economist (Apr 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry941"
 lang="en" word="choleric" freq="8324.46" prog="0">

<a class="word dynamictext" href="/dictionary/choleric">choleric</a>
<div class="definition">characterized by anger</div>
<div class="example">Jonathan,
<strong>choleric</strong> with indignation, stood by his desk, clenching his hands.
<br> —
<a href="http://www.gutenberg.org/ebooks/36991" rel="nofollow">Mills, Weymer Jay</a></div>


</li>






<li class="entry learnable" id="entry942"
 lang="en" word="garble" freq="8330.32" prog="0">

<a class="word dynamictext" href="/dictionary/garble">garble</a>
<div class="definition">make false by mutilation or addition</div>
<div class="example">But the fact remains that the contradictory and inconsistent things said do reach the public, and usually in
<strong>garbled</strong> and distorted form.
<br> —
<a href="http://www.gutenberg.org/ebooks/38929" rel="nofollow">Unknown</a></div>


</li>






<li class="entry learnable" id="entry943"
 lang="en" word="bucolic" freq="8353.87" prog="0">

<a class="word dynamictext" href="/dictionary/bucolic">bucolic</a>
<div class="definition">idyllically rustic</div>
<div class="example">Forty-four years ago, Bill Sievers moved into his neo-Colonial house in Douglaston, Queens, on
<strong>bucolic</strong> Poplar Street, lined with stately trees and equally stately homes.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=284634174fca59d9f8a76489c5e99ce2" rel="nofollow">New York Times (Mar 26, 2012)</a></div>


</li>






<li class="entry learnable" id="entry944"
 lang="en" word="denouement" freq="8395.4" prog="0">

<a class="word dynamictext" href="/dictionary/denouement">denouement</a>
<div class="definition">the outcome of a complex sequence of events</div>
<div class="example">Suppose the truly apocalyptic
<strong>denouement</strong> happens -- no deal is reached, and taxes rise for everyone.
<br> —
<a href="http://www.salon.com/tech/htww/2010/11/30/obama_tax_cut_summits/index.html" rel="nofollow">Salon (Nov 30, 2010)</a></div>


</li>






<li class="entry learnable" id="entry945"
 lang="en" word="animus" freq="8407.34" prog="0">

<a class="word dynamictext" href="/dictionary/animus">animus</a>
<div class="definition">a feeling of ill will arousing active hostility</div>
<div class="example">The youthful savages had each an armful of snowballs, and they were pelting the child with more
<strong>animus</strong> than seemed befitting.
<br> —
<a href="http://www.gutenberg.org/ebooks/22274" rel="nofollow">Murray, David Christie</a></div>


</li>






<li class="entry learnable" id="entry946"
 lang="en" word="overweening" freq="8449.4" prog="0">

<a class="word dynamictext" href="/dictionary/overweening">overweening</a>
<div class="definition">unrestrained, especially with regard to feelings</div>
<div class="example">He had
<strong>overweening</strong> ambitions even then, along with a highly developed sense of his own importance.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=4fa24d046e9cfdce278598c717d9b3c2" rel="nofollow">New York Times (Apr 19, 2010)</a></div>


</li>






<li class="entry learnable" id="entry947"
 lang="en" word="tyro" freq="8461.49" prog="0">

<a class="word dynamictext" href="/dictionary/tyro">tyro</a>
<div class="definition">someone new to a field or activity</div>
<div class="example">As yet he was merely a
<strong>tyro</strong>, gaining practical experience under a veteran Zeppelin commander.
<br> —
<a href="http://www.gutenberg.org/ebooks/35362" rel="nofollow">Westerman, Percy F. (Percy Francis)</a></div>


</li>






<li class="entry learnable" id="entry948"
 lang="en" word="preen" freq="8461.49" prog="0">

<a class="word dynamictext" href="/dictionary/preen">preen</a>
<div class="definition">dress or groom with elaborate care</div>
<div class="example">He
<strong>preened</strong> on fight nights in a tuxedo, a bow tie and no shirt, and he favored showy rings and bracelets.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/S1x8KwOPWMI/butch-lewis-flashy-promoter-for-boxings-spinks-brothers-dies-at-65.html" rel="nofollow">New York Times (Jul 24, 2011)</a></div>


</li>






<li class="entry learnable" id="entry949"
 lang="en" word="largesse" freq="8461.49" prog="0">

<a class="word dynamictext" href="/dictionary/largesse">largesse</a>
<div class="definition">liberality in bestowing gifts</div>
<div class="example">After being saved by government
<strong>largesse</strong>, they say, big banks then moved to thwart reforms aimed at preventing future meltdowns caused by excessive risk-taking.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=40345a49704445382f41ad21b9f54b5c" rel="nofollow">New York Times (Jul 14, 2011)</a></div>


</li>






<li class="entry learnable" id="entry950"
 lang="en" word="retentive" freq="8504.1" prog="0">

<a class="word dynamictext" href="/dictionary/retentive">retentive</a>
<div class="definition">good at remembering</div>
<div class="example">The child was very sharp, and her memory was extremely
<strong>retentive</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/34166" rel="nofollow">Rowlands, Effie Adelaide</a></div>


</li>






<li class="entry learnable" id="entry951"
 lang="en" word="unconscionable" freq="8559.52" prog="0">

<a class="word dynamictext" href="/dictionary/unconscionable">unconscionable</a>
<div class="definition">greatly exceeding bounds of reason or moderation</div>
<div class="example">For generations in the New York City public schools, this has become the norm with devastating consequences rooted in
<strong>unconscionable</strong> levels of student failure.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=eb30b670e1adb6bb3d492f953af70d88" rel="nofollow">New York Times (Nov 4, 2011)</a></div>


</li>






<li class="entry learnable" id="entry952"
 lang="en" word="badinage" freq="8571.93" prog="0">

<a class="word dynamictext" href="/dictionary/badinage">badinage</a>
<div class="definition">frivolous banter</div>
<div class="example">It was preposterous to talk to her of serious things, and nothing but an airy
<strong>badinage</strong> seemed possible in her company.
<br> —
<a href="http://www.gutenberg.org/ebooks/27198" rel="nofollow">Maugham, W. Somerset (William Somerset)</a></div>


</li>






<li class="entry learnable" id="entry953"
 lang="en" word="insensate" freq="8609.38" prog="0">

<a class="word dynamictext" href="/dictionary/insensate">insensate</a>
<div class="definition">devoid of feeling and consciousness and animation</div>
<div class="example">Men also are those brutal soldiers, alike stupidly ready, at the word of command, to drive the nail through quivering flesh or
<strong>insensate</strong> wood.
<br> —
<a href="http://www.gutenberg.org/ebooks/31390" rel="nofollow">Stowe, Harriet Beecher</a></div>


</li>






<li class="entry learnable" id="entry954"
 lang="en" word="sherbet" freq="8685.28" prog="0">

<a class="word dynamictext" href="/dictionary/sherbet">sherbet</a>
<div class="definition">a frozen dessert made primarily of fruit juice and sugar</div>
<div class="example">"One person said it looks like a big lime
<strong>sherbet</strong> ice cream cone!"
<br> —
<a href="http://feeds.southernliving.com/~r/southernliving/homeandgarden/~3/cC53bROo51I/" rel="nofollow">Southern Living (Apr 28, 2010)</a></div>


</li>






<li class="entry learnable" id="entry955"
 lang="en" word="beatific" freq="8691.67" prog="0">

<a class="word dynamictext" href="/dictionary/beatific">beatific</a>
<div class="definition">resembling or befitting an angel or saint</div>
<div class="example">She dozed at last, her face serene and
<strong>beatific</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/32101" rel="nofollow">Beach, Rex Ellingwood</a></div>


</li>






<li class="entry learnable" id="entry956"
 lang="en" word="bemuse" freq="8717.31" prog="0">

<a class="word dynamictext" href="/dictionary/bemuse">bemuse</a>
<div class="definition">cause to be confused emotionally</div>
<div class="example">They were marching in the middle of the street, chanting and singing and disrupting traffic while countless New Yorkers looked on, some
<strong>bemused</strong>, others applauding.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/5Mw0Ptjd9JA/" rel="nofollow">Time (Oct 28, 2011)</a></div>


</li>






<li class="entry learnable" id="entry957"
 lang="en" word="microcosm" freq="8775.54" prog="0">

<a class="word dynamictext" href="/dictionary/microcosm">microcosm</a>
<div class="definition">a miniature model of something</div>
<div class="example">The building, he said, is "a
<strong>microcosm</strong> of what Shanghai was all about."
<br> —
<a href="http://online.wsj.com/article/SB10001424052748704093204575215811925489410.html?mod=fox_australian" rel="nofollow">Wall Street Journal (Apr 30, 2010)</a></div>


</li>






<li class="entry learnable" id="entry958"
 lang="en" word="factitious" freq="8795.13" prog="0">

<a class="word dynamictext" href="/dictionary/factitious">factitious</a>
<div class="definition">not produced by natural forces</div>
<div class="example">Indeed, the Chinese make a
<strong>factitious</strong> cheese out of peas, which it is difficult to discriminate from the article of animal origin.
<br> —
<a href="http://www.gutenberg.org/ebooks/25520" rel="nofollow">Cameron, Charles Alexander, Sir</a></div>


</li>






<li class="entry learnable" id="entry959"
 lang="en" word="gestate" freq="8867.7" prog="0">

<a class="word dynamictext" href="/dictionary/gestate">gestate</a>
<div class="definition">have the idea for</div>
<div class="example">Mr. Lucas’s most recent project, still
<strong>gestating</strong>, is a collaboration with Cuban musicians.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=901f425f5f56a883a02363f3306edcfd" rel="nofollow">New York Times (May 9, 2011)</a></div>


</li>






<li class="entry learnable" id="entry960"
 lang="en" word="traduce" freq="8887.7" prog="0">

<a class="word dynamictext" href="/dictionary/traduce">traduce</a>
<div class="definition">speak unfavorably about</div>
<div class="example">For Grover Cleveland there were no longer enemies to
<strong>traduce</strong> and vilify.
<br> —
<a href="http://www.gutenberg.org/ebooks/39144" rel="nofollow">Straus, Oscar S.</a></div>


</li>






<li class="entry learnable" id="entry961"
 lang="en" word="sextant" freq="8975.42" prog="0">

<a class="word dynamictext" href="/dictionary/sextant">sextant</a>
<div class="definition">an instrument for measuring angular distance</div>
<div class="example">For example, a
<strong>sextant</strong> could be used to sight the sun at high noon in order to determine one’s latitude.
<br> —
<a href="http://rss.sciam.com/click.phdo?i=8c5e8487965e774dca59d534a91fdf5f" rel="nofollow">Scientific American (Mar 8, 2012)</a></div>


</li>






<li class="entry learnable" id="entry962"
 lang="en" word="coiffure" freq="9064.89" prog="0">

<a class="word dynamictext" href="/dictionary/coiffure">coiffure</a>
<div class="definition">the arrangement of the hair</div>
<div class="example">They sat down, and Saint-Clair noticed his friend's
<strong>coiffure</strong>; a single rose was in her hair.
<br> —
<a href="http://www.gutenberg.org/ebooks/35004" rel="nofollow">M?rim?e, Prosper</a></div>


</li>






<li class="entry learnable" id="entry963"
 lang="en" word="malleable" freq="9078.81" prog="0">

<a class="word dynamictext" href="/dictionary/malleable">malleable</a>
<div class="definition">easily influenced</div>
<div class="example">“The Americans are seen as naïve
<strong>malleable</strong> tools in the hands of the Brits.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=c9c49567e48d7e806c31c5808db0dafb" rel="nofollow">New York Times (Nov 30, 2011)</a></div>


</li>






<li class="entry learnable" id="entry964"
 lang="en" word="rococo" freq="9092.78" prog="0">

<a class="word dynamictext" href="/dictionary/rococo">rococo</a>
<div class="definition">having excessive asymmetrical ornamentation</div>
<div class="example">The upper part of the case is decorated with elaborately carved and gilt
<strong>rococo</strong> motifs.
<br> —
<a href="http://www.gutenberg.org/ebooks/33198" rel="nofollow">Bedini, Silvio A.</a></div>


</li>






<li class="entry learnable" id="entry965"
 lang="en" word="fructify" freq="9142" prog="0">

<a class="word dynamictext" href="/dictionary/fructify">fructify</a>
<div class="definition">become productive or fruitful</div>
<div class="example">Thence they grow, expand,
<strong>fructify</strong>, and the result is Progress.
<br> —
<a href="http://www.gutenberg.org/ebooks/28020" rel="nofollow">Stanton, Elizabeth Cady</a></div>


</li>






<li class="entry learnable" id="entry966"
 lang="en" word="nihilist" freq="9142" prog="0">

<a class="word dynamictext" href="/dictionary/nihilist">nihilist</a>
<div class="definition">someone who rejects all theories of morality</div>
<div class="example">“He’s a loner
<strong>nihilist</strong> who believes in nothing,” Mr. Lu said.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=350caf446fa0fc3b5f6d2a5f9d2ab096" rel="nofollow">New York Times (Nov 6, 2011)</a></div>


</li>






<li class="entry learnable" id="entry967"
 lang="en" word="ellipsis" freq="9177.48" prog="0">

<a class="word dynamictext" href="/dictionary/ellipsis">ellipsis</a>
<div class="definition">omission or suppression of parts of words or sentences</div>
<div class="example">He speaks in
<strong>ellipses</strong>, often leaving sentences hanging, and fiddles apologetically with his BlackBerry.
<br> —
<a href="http://www.guardian.co.uk/artanddesign/2010/jun/28/steve-mccurry-photography" rel="nofollow">The Guardian (Jun 28, 2010)</a></div>


</li>






<li class="entry learnable" id="entry968"
 lang="en" word="accolade" freq="9184.61" prog="0">

<a class="word dynamictext" href="/dictionary/accolade">accolade</a>
<div class="definition">a tangible symbol signifying approval or distinction</div>
<div class="example">The Nobel Prize, considered one of the highest
<strong>accolades</strong> in literature, is given only to living writers.
<br> —
<a href="http://seattletimes.nwsource.com/html/entertainment/2016419891_apeunobelliterature.html?syndication=rss" rel="nofollow">Seattle Times (Oct 6, 2011)</a></div>


</li>






<li class="entry learnable" id="entry969"
 lang="en" word="codicil" freq="9198.91" prog="0">

<a class="word dynamictext" href="/dictionary/codicil">codicil</a>
<div class="definition">a supplement to a will</div>
<div class="example">The
<strong>codicil</strong> to her will, which she had spoken of with so much composure, left three hundred pounds to Stella and me.
<br> —
<a href="http://www.gutenberg.org/ebooks/29219" rel="nofollow">Fothergill, Jessie</a></div>


</li>






<li class="entry learnable" id="entry970"
 lang="en" word="roil" freq="9213.25" prog="0">

<a class="word dynamictext" href="/dictionary/roil">roil</a>
<div class="definition">be agitated</div>
<div class="example">Like thousands of fellow students, he was
<strong>roiled</strong> with emotions, struggling to come to grips with an inescapable reality.
<br> —
<a href="http://feeds1.nytimes.com/~r/nyt/rss/Sports/~3/hFUg7Rc2kBE/they-are-still-penn-state-but-it-will-never-be-the-same.html" rel="nofollow">New York Times (Nov 26, 2011)</a></div>


</li>






<li class="entry learnable" id="entry971"
 lang="en" word="grandiloquent" freq="9213.25" prog="0">

<a class="word dynamictext" href="/dictionary/grandiloquent">grandiloquent</a>
<div class="definition">lofty in style</div>
<div class="example">A large part of his duties will be to strut about on the stage, and mouth more or less unintelligible sentences in a
<strong>grandiloquent</strong> tone.
<br> —
<a href="http://www.gutenberg.org/ebooks/33485" rel="nofollow">Smith, Arthur H.</a></div>


</li>






<li class="entry learnable" id="entry972"
 lang="en" word="inconsequential" freq="9227.63" prog="0">

<a class="word dynamictext" href="/dictionary/inconsequential">inconsequential</a>
<div class="definition">lacking worth or importance</div>
<div class="example">But as the months went by, Mr. Kimura had an unexpected epiphany: His business, which he thought was
<strong>inconsequential</strong>, mattered to a lot of people.
<br> —
<a href="http://online.wsj.com/article/SB10001424052970203707504577007550569072874.html?mod=fox_australian" rel="nofollow">Wall Street Journal (Nov 11, 2011)</a></div>


</li>






<li class="entry learnable" id="entry973"
 lang="en" word="effervescence" freq="9263.78" prog="0">

<a class="word dynamictext" href="/dictionary/effervescence">effervescence</a>
<div class="definition">the property of giving off bubbles</div>
<div class="example">Both were in the very sparkle and
<strong>effervescence</strong> of that fanciful glee which bubbles up from the golden, untried fountains of early childhood.
<br> —
<a href="http://www.gutenberg.org/ebooks/31522" rel="nofollow">Stowe, Harriet Beecher</a></div>


</li>






<li class="entry learnable" id="entry974"
 lang="en" word="stultify" freq="9359.12" prog="0">

<a class="word dynamictext" href="/dictionary/stultify">stultify</a>
<div class="definition">deprive of strength or efficiency; make useless or worthless</div>
<div class="example">Far from being engines of economic growth, Egypt's leading cities are
<strong>stultified</strong>.
<br> —
<a href="http://feedproxy.google.com/~r/inc/headlines/~3/G4aWrkLNX7A/egypt-entrepreneurial-revolution.html" rel="nofollow">Inc (Feb 12, 2011)</a></div>


</li>






<li class="entry learnable" id="entry975"
 lang="en" word="tureen" freq="9366.54" prog="0">

<a class="word dynamictext" href="/dictionary/tureen">tureen</a>
<div class="definition">large deep serving dish with a cover</div>
<div class="example">Soups are presented in big
<strong>tureens</strong> and can be quite good.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=bb0c1043e1e6ab4f60d829a4b8db31bb" rel="nofollow">New York Times (Apr 13, 2012)</a></div>


</li>






<li class="entry learnable" id="entry976"
 lang="en" word="pellucid" freq="9366.54" prog="0">

<a class="word dynamictext" href="/dictionary/pellucid">pellucid</a>
<div class="definition">transparently clear; easily understandable</div>
<div class="example">Caribou Island is a scant 300 pages, and written in prose as
<strong>pellucid</strong> as the rivers he used to fish as a boy.
<br> —
<a href="http://www.guardian.co.uk/books/2011/jan/02/david-vann-caribou-island-interview" rel="nofollow">The Guardian (Jan 1, 2011)</a></div>


</li>






<li class="entry learnable" id="entry977"
 lang="en" word="euphony" freq="9366.54" prog="0">

<a class="word dynamictext" href="/dictionary/euphony">euphony</a>
<div class="definition">any pleasing and harmonious sounds</div>
<div class="example">It depends somewhat on usage and on
<strong>euphony</strong> or agreeableness of sound.
<br> —
<a href="http://www.gutenberg.org/ebooks/30036" rel="nofollow">Hamilton, Frederick W. (Frederick William)</a></div>


</li>






<li class="entry learnable" id="entry978"
 lang="en" word="apocryphal" freq="9396.32" prog="0">

<a class="word dynamictext" href="/dictionary/apocryphal">apocryphal</a>
<div class="definition">being of questionable authenticity</div>
<div class="example">We're reminded of the story, possibly
<strong>apocryphal</strong>, that they used to play the Beach Boys' Smiley Smile in psychiatric wards to calm patients.
<br> —
<a href="http://www.guardian.co.uk/music/2011/jan/20/new-band-therapies-son" rel="nofollow">The Guardian (Jan 20, 2011)</a></div>


</li>






<li class="entry learnable" id="entry979"
 lang="en" word="veracious" freq="9479.2" prog="0">

<a class="word dynamictext" href="/dictionary/veracious">veracious</a>
<div class="definition">precisely accurate</div>
<div class="example">For proof, we cite the following
<strong>veracious</strong> narrative, which bears within it every internal mark of truth, and matter for grave and serious reflection.
<br> —
<a href="http://www.gutenberg.org/ebooks/25256" rel="nofollow">Roby, John</a></div>


</li>






<li class="entry learnable" id="entry980"
 lang="en" word="pendulous" freq="9479.2" prog="0">

<a class="word dynamictext" href="/dictionary/pendulous">pendulous</a>
<div class="definition">hanging loosely or bending downward</div>
<div class="example">And all around, far out of reach, the trees of the forest were swaying restlessly, their long,
<strong>pendulous</strong> branches, like tentacles, lashing out hungrily.
<br> —
<a href="http://www.gutenberg.org/ebooks/29255" rel="nofollow">Bates, Harry</a></div>


</li>






<li class="entry learnable" id="entry981"
 lang="en" word="exegesis" freq="9494.42" prog="0">

<a class="word dynamictext" href="/dictionary/exegesis">exegesis</a>
<div class="definition">an explanation or critical interpretation</div>
<div class="example">Its musical significance has been presented with illuminating
<strong>exegesis</strong> by more than one commentator.
<br> —
<a href="http://www.gutenberg.org/ebooks/35041" rel="nofollow">Forkel, Johann Nikolaus</a></div>


</li>






<li class="entry learnable" id="entry982"
 lang="en" word="effluvium" freq="9509.7" prog="0">

<a class="word dynamictext" href="/dictionary/effluvium">effluvium</a>
<div class="definition">a foul-smelling outflow or vapor</div>
<div class="example">However, acting on my best judgment, I struck a downward course, and then suddenly a horrible
<strong>effluvium</strong> was wafted to my nostrils.
<br> —
<a href="http://www.gutenberg.org/ebooks/32895" rel="nofollow">Mitford, Bertram</a></div>


</li>






<li class="entry learnable" id="entry983"
 lang="en" word="apposite" freq="9610.2" prog="0">

<a class="word dynamictext" href="/dictionary/apposite">apposite</a>
<div class="definition">being of striking appropriateness and pertinence</div>
<div class="example">He was quite capable of meaningful,
<strong>apposite</strong> phrases about the game, even though distant sports editors did not encourage them enough.
<br> —
<a href="http://www.guardian.co.uk/sport/2010/aug/18/eric-hill-obituary" rel="nofollow">The Guardian (Aug 18, 2010)</a></div>


</li>






<li class="entry learnable" id="entry984"
 lang="en" word="viscous" freq="9665.2" prog="0">

<a class="word dynamictext" href="/dictionary/viscous">viscous</a>
<div class="definition">having the sticky properties of an adhesive</div>
<div class="example">Sluggish, blind crawling things like three-foot slugs flowed across their path and among the tree trunks, leaving
<strong>viscous</strong> trails of slime behind them.
<br> —
<a href="http://www.gutenberg.org/ebooks/30452" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry985"
 lang="en" word="misanthrope" freq="9673.1" prog="0">

<a class="word dynamictext" href="/dictionary/misanthrope">misanthrope</a>
<div class="definition">someone who dislikes people in general</div>
<div class="example">And shaking his head like a
<strong>misanthrope</strong>, disgusted, if not with life, at least with men, Patout led the horse to the stable.
<br> —
<a href="http://www.gutenberg.org/ebooks/7079" rel="nofollow">Dumas père, Alexandre</a></div>


</li>






<li class="entry learnable" id="entry986"
 lang="en" word="vintner" freq="9696.91" prog="0">

<a class="word dynamictext" href="/dictionary/vintner">vintner</a>
<div class="definition">someone who makes wine</div>
<div class="example">The question remains, he said, whether established
<strong>vintners</strong> will change their winemaking practices or “continue to sell their schlock.”
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=cba9f47441d739c7997d43cd2c673ce7" rel="nofollow">New York Times (Oct 27, 2010)</a></div>


</li>






<li class="entry learnable" id="entry987"
 lang="en" word="halcyon" freq="9720.83" prog="0">

<a class="word dynamictext" href="/dictionary/halcyon">halcyon</a>
<div class="definition">idyllically calm and peaceful; suggesting happy tranquility</div>
<div class="example">He now seemed to have entered on a
<strong>halcyon</strong> period of life—congenial society, romantic and interesting surroundings.
<br> —
<a href="http://www.gutenberg.org/ebooks/33345" rel="nofollow">Kennard, Nina H.</a></div>


</li>






<li class="entry learnable" id="entry988"
 lang="en" word="anthropomorphic" freq="9801.42" prog="0">

<a class="word dynamictext" href="/dictionary/anthropomorphic">anthropomorphic</a>
<div class="definition">suggesting human features for animals or inanimate things</div>
<div class="example">The same
<strong>anthropomorphic</strong> fallacy that accords human attributes to giant corporations like BP distorts clear thinking about how to limit their political influence.
<br> —
<a href="http://www.salon.com/news/feature/2010/07/28/corporations_money_politics/index.html" rel="nofollow">Salon (Jul 28, 2010)</a></div>


</li>






<li class="entry learnable" id="entry989"
 lang="en" word="turgid" freq="9866.87" prog="0">

<a class="word dynamictext" href="/dictionary/turgid">turgid</a>
<div class="definition">ostentatiously lofty in style</div>
<div class="example">His waspish wit can make him entertaining company at a party, but there is little evidence of that in his largely
<strong>turgid</strong> prose.
<br> —
<a href="http://www.guardian.co.uk/books/2010/jul/18/peter-mandelson-third-man-memoirs" rel="nofollow">The Guardian (Jul 17, 2010)</a></div>


</li>






<li class="entry learnable" id="entry990"
 lang="en" word="malaise" freq="9883.37" prog="0">

<a class="word dynamictext" href="/dictionary/malaise">malaise</a>
<div class="definition">a general feeling of discomfort, uneasiness, or depression</div>
<div class="example">Initially, many doctors discounted sufferers’ feelings of generalized
<strong>malaise</strong> as nothing more than stress or normal fatigue.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/JFsojC7OdGA/" rel="nofollow">Time (Dec 22, 2011)</a></div>


</li>






<li class="entry learnable" id="entry991"
 lang="en" word="polemical" freq="9916.53" prog="0">

<a class="word dynamictext" href="/dictionary/polemical">polemical</a>
<div class="definition">of or involving dispute or controversy</div>
<div class="example">His works include several dogmatic and
<strong>polemical</strong> treatises, but the most important are the historical.
<br> —
<a href="http://www.gutenberg.org/ebooks/27480" rel="nofollow">Various</a></div>


</li>






<li class="entry learnable" id="entry992"
 lang="en" word="gadfly" freq="9991.96" prog="0">

<a class="word dynamictext" href="/dictionary/gadfly">gadfly</a>
<div class="definition">a persistently annoying person</div>
<div class="example">Mr. Phelps is regarded here as the ultimate example of an irritating local
<strong>gadfly</strong>.
<br> —
<a href="http://feeds.nytimes.com/click.phdo?i=8831fc6606f660cff23b00b295f3ee8f" rel="nofollow">New York Times (Oct 9, 2010)</a></div>


</li>






<li class="entry learnable" id="entry993"
 lang="en" word="atavism" freq="10120.27" prog="0">

<a class="word dynamictext" href="/dictionary/atavism">atavism</a>
<div class="definition">a reappearance of an earlier characteristic</div>
<div class="example">Criminal
<strong>atavism</strong> might be defined as the sporadic reversion to savagery in certain individuals.
<br> —
<a href="http://www.gutenberg.org/ebooks/32588" rel="nofollow">Symonds, John Addington</a></div>


</li>






<li class="entry learnable" id="entry994"
 lang="en" word="contusion" freq="10314.53" prog="0">

<a class="word dynamictext" href="/dictionary/contusion">contusion</a>
<div class="definition">an injury in which the skin is not broken</div>
<div class="example">My falling companion, being a much stouter man than myself did not fare so well, as his right shoulder received a severe
<strong>contusion</strong>.
<br> —
<a href="http://www.gutenberg.org/ebooks/27520" rel="nofollow">Bevan, A. Beckford</a></div>


</li>






<li class="entry learnable" id="entry995"
 lang="en" word="parsimonious" freq="10387.04" prog="0">

<a class="word dynamictext" href="/dictionary/parsimonious">parsimonious</a>
<div class="definition">excessively unwilling to spend</div>
<div class="example">Pill-splitting is catching on among
<strong>parsimonious</strong> prescription-takers who want to lower costs.
<br> —
<a href="http://www.forbes.com/2010/03/04/prescription-lipitor-nexium-lifestyle-health-drug-costs.html?feed=rss_forbeslife_health" rel="nofollow">Forbes (Mar 4, 2010)</a></div>


</li>






<li class="entry learnable" id="entry996"
 lang="en" word="dulcet" freq="10497.72" prog="0">

<a class="word dynamictext" href="/dictionary/dulcet">dulcet</a>
<div class="definition">pleasing to the ear</div>
<div class="example">Ever and anon the
<strong>dulcet</strong> murmur of gurgling streams broke gently on the ear.
<br> —
<a href="http://www.gutenberg.org/ebooks/32993" rel="nofollow">Madison, Lucy Foster</a></div>


</li>






<li class="entry learnable" id="entry997"
 lang="en" word="reprise" freq="10516.4" prog="0">

<a class="word dynamictext" href="/dictionary/reprise">reprise</a>
<div class="definition">repeat an earlier theme of a composition</div>
<div class="example">The live set
<strong>reprises</strong> material from this remarkable group's earlier Aurora CD.
<br> —
<a href="http://www.guardian.co.uk/music/2011/jan/06/fernandez-guy-lopez-morning-glory-review" rel="nofollow">The Guardian (Jan 6, 2011)</a></div>


</li>






<li class="entry learnable" id="entry998"
 lang="en" word="anodyne" freq="10535.15" prog="0">

<a class="word dynamictext" href="/dictionary/anodyne">anodyne</a>
<div class="definition">capable of relieving pain</div>
<div class="example">But philosophy failed, as it will probably fail till some far-off age, to find an
<strong>anodyne</strong> for the spiritual distresses of the mass of men.
<br> —
<a href="http://www.gutenberg.org/ebooks/34122" rel="nofollow">Dill, Samuel</a></div>


</li>






<li class="entry learnable" id="entry999"
 lang="en" word="bemused" freq="10553.96" prog="0">

<a class="word dynamictext" href="/dictionary/bemused">bemused</a>
<div class="definition">perplexed by many conflicting situations or statements</div>
<div class="example">They were marching in the middle of the street, chanting and singing and disrupting traffic while countless New Yorkers looked on, some
<strong>bemused</strong>, others applauding.
<br> —
<a href="http://feedproxy.google.com/~r/time/topstories/~3/5Mw0Ptjd9JA/" rel="nofollow">Time (Oct 28, 2011)</a></div>


</li>


	</ol>
	</div>
</div>
</div>
</div>
</div>


<section class="signup-tout center clearfloat sectionbg">
<div class="limited-width ">
	<h2>Sign up, it's free!</h2>
	<div class="margin2 margin2r col8" >
		<p>
		Whether you're a student, an educator, or a life-long learner, Vocabulary.com can put you
		on the path to systematic vocabulary improvement. <br>
		</p>

		<a role="button" class="signup button green" href="/signup/">Get Started</a>

	</div>
</div>
</section>


<footer class="page-footer">
<nav class="sitelinks limited-width hide-mobile clearfloat screen-only">
	<div class="col2 ">
			<h3>For Everyone</h3>
			<ul>
			<li><a href="/play/">Play the Challenge</a></li>
			<li><a href="/lists/">Vocabulary Lists</a></li>
			<li><a href="/dictionary/">Dictionary</a></li>
			<li><a href="/articles/chooseyourwords/">Choose Your Words</a></li>
			</ul>
		</div>

		<div class="col2 ">
			<h3><a href="/educator-edition/">For Educators</a></h3>
			<ul>
			<li><a href="/educator-edition/">Educator Edition</a></li>
			<li><a href="/educator-edition/pricing/">Plans &amp; Pricing</a></li>
			<li><a href="/educator-edition/sales/">Contact Sales</a></li>
			<li><a href="/articles/success-stories/">Success Stories</a></li>
			</ul>
		</div>

		<div class="col2 ">
			<h3><a href="/help/">Help</a></h3>
			<ul>
			<li><a href="/help/">Help Articles / FAQ</a></li>
			<!--  <li><a href="/help/videos/">How-to Videos</a></li>-->
			<li><a href="/help/webinars">Training &amp; Webinars</a></li>
			<li><a href="/help/contactus">Contact Support</a></li>
			<li><a>&nbsp;</a></li>
			</ul>
		</div>

		<div class="col2 ">
			<h3><a href="/leaderboards/">Leaderboards</a></h3>
			<ul>
			<li><a href="/bowl/">Vocabulary Bowl</a></li>
			<li><a href="/leaderboards/bowl/">Bowl Leaders</a></li>
			<li><a href="/leaderboards/today/">Today's Leaders</a></li>
			<li><a href="/leaderboards/thisweek/">Weekly Leaders</a></li>
			<li><a href="/leaderboards/thismonth/">Monthly Leaders</a></li>
			</ul>
		</div>

		<div class="col2 ">
			<h3><a href="/blog/">Connect</a></h3>
			<ul>
			<li><a href="/blog/">Vocabulary.com Blog</a></li>
			<li><a href="https://twitter.com/VocabularyCom">Twitter</a></li>
			<li><a href="https://www.facebook.com/vocabularycom">Facebook</a></li>

			</ul>
		</div>

		<div class="col2 ">
			<h3><a href="/about/">Our Story</a></h3>
			<ul>
			<li><a href="/about/">Our Mission</a></li>
			<li><a href="/about/team/">Team / Jobs</a></li>
			<li><a href="/about/news/">News &amp; Events</a></li>
			<li><a href="/about/partnerships/">Partnerships</a></li>
			</ul>
		</div>

</nav>
<nav class="legal limited-width clearfloat">
		<a href="/terms/">&copy; Vocabulary.com</a>
		<a href="/terms/" class="screen-only">Terms of Use</a>
		<a href="/privacy/" class="screen-only">Privacy Policy</a>
</nav></footer>

<nav class="sitemap screen-only">
<div class="scrollable">
<div>
	<div class="limited-width mobile-5050 pad2y">

	<div class="col9">
		<div class="col4 pad1x">
			<h3>For Everyone</h3>
			<ul>
			<li><a href="/play/">Play the Challenge</a></li>
			<li><a href="/lists/">Vocabulary Lists</a></li>
			<li><a href="/dictionary/">Dictionary</a></li>
			<li><a href="/articles/chooseyourwords/">Choose Your Words</a></li>
			</ul>
		</div>

		<div class="col4 pad1x">
			<h3><a href="/educator-edition/">For Educators</a></h3>
			<ul>
			<li><a href="/educator-edition/">Educator Edition</a></li>
			<li><a href="/educator-edition/pricing/">Plans &amp; Pricing</a></li>
			<li><a href="/educator-edition/sales/">Contact Sales</a></li>
			<li><a href="/articles/success-stories/">Success Stories</a></li>
			</ul>
		</div>

		<div class="col4 pad1x">
			<h3><a href="/help/">Help</a></h3>
			<ul>
			<li><a href="/help/">Help Articles / FAQ</a></li>
			<!--<li><a href="/help/videos/">How-to Videos</a></li>-->
			<li><a href="/help/webinars">Training &amp; Webinars</a></li>
			<li><a href="/help/contactus">Contact Support</a></li>
			<li><a>&nbsp;</a></li>
			</ul>
		</div>

		<div class="col4 pad1x">
			<h3><a href="/leaderboards/">Leaderboards</a></h3>
			<ul>
			<li><a href="/bowl/">Vocabulary Bowl</a></li>
			<li><a href="/leaderboards/bowl/">Bowl Leaders</a></li>
			<li><a href="/leaderboards/today/">Today's Leaders</a></li>
			<li><a href="/leaderboards/thisweek/">Weekly Leaders</a></li>
			<li><a href="/leaderboards/thismonth/">Monthly Leaders</a></li>
			</ul>
		</div>



		<div class="col4 pad1x">
			<h3><a href="/blog/">Connect</a></h3>
			<ul>
			<li><a href="/blog/">Vocabulary.com Blog</a></li>
			<li><a href="https://twitter.com/VocabularyCom">Twitter</a></li>
			<li><a href="https://www.facebook.com/vocabularycom">Facebook</a></li>

			</ul>
		</div>

		<div class="col4 pad1x">
			<h3><a href="/about/">Our Story</a></h3>
			<ul>
			<li><a href="/about/">Our Mission</a></li>
			<li><a href="/about/team/">Team / Jobs</a></li>
			<li><a href="/about/news/">News &amp; Events</a></li>
			<li><a href="/about/partnerships/">Partnerships</a></li>
			</ul>
		</div>
	</div>
	<div class="col3 pad1x">
		<h3><a href="/account/">My Account</a></h3>
		<div class="loggedout-only clearfloat signinoptions">
			<a role="button" class="google button" href="/login/google">Sign in with Google</a>
			<a role="button" class="facebook button" href="/login/facebook">Sign in with Facebook</a>
			<p>or, <a href="/login/">sign in with email.</a></p>
			<p>Don't have an account yet?<br>
			   <a href="/signup">Sign up. It's free and takes five seconds.</a>
			</p>
		</div>
		<ul class="loggedin-only">
			<li><a href="/auth/logout"><i class="ss-logout"></i>Log Out</a></li>
			<li class="nav-assignments with-assignments-only"><a href="/account/assignments"><i class="ss-attach"></i>My Assignments</a></li>
			<li><a href="/progress/"><i class="ss-barchart"></i>My Progress</a>
				<ul>
					<li><a href="/account/progress/words/learning"><i class="ss-hiker ss-symbolicons-block"></i>Words I'm Learning</a></li>
					<li><a href="/account/progress/words/trouble"><i class="ss-bullseye ss-symbolicons-block"></i>My Trouble Words</a></li>
					<li><a href="/account/progress/words/mastered"><i class="ss-check ss-symbolicons-block"></i>Words I've Mastered</a></li>
					<li><a href="/account/progress/achievements"><i class="ss-award ss-symbolicons-block"></i>My Achievements</a></li>
				</ul>
			</li>
			<li ><a href="/account/lists/"><i class="ss-list"></i>My Lists</a>
			<ul>
				<li><a href="/lists/"><i class="ss-search"></i>Find a List to Learn...</a></li>
				<li><a href="/lists/new"><i class="ss-hospital ss-symbolicons-block"></i>Create a New List...</a></li>
			</ul>
			</li>

			<li class="nav-classes perms-create-class-only"><a href="/account/classes"><i class="ss-users"></i>My Classes</a></li>


			<li class="perms-school-reports-only"><a href="/account/schools"><i class="ss-school ss-symbolicons-block"></i>Schools &amp; Teachers</a></li>

			<li class="perms-user-admin-only"><a href="/account/users"><i class="ss-usergroup ss-symbolicons-block "></i>User Administration</a></li>
			<li class="perms-auth-admin-only"><a href="/account/authentication"><i class="ss-key"></i>User Authentication</a></li>
			<li>
				<a href="/account/"><i class="ss-settings"></i>My Account</a>

			</li>
		</ul>
	</div>
	</div>
	<div class="copyright pad2y">
		<div class="limited-width">
		<span>&copy; Vocabulary.com</span>
		<div class="terms">
		<a href="/terms/">Terms of Use</a>
		<a href="/privacy/">Privacy Policy</a>
		</div>
		</div>
	</div>
</div></div>
<div class="nub"></div>
</nav>
</div>

</body>

</html>
'''
# print  textInfo

print "----------------------------------------------------------------------------"

vocabularyList = getVocabularyList(textInfo);
# print vocabularyList
# print len(vocabularyList)

print "----------------------------------------------------------------------------"

nativeList = getVocabularyChineseDefineList(vocabularyList)
# for nativeWord in nativeList:
#     print unicode(nativeWord).encode('utf-8')

print "----------------------------------------------------------------------------"

vocabularyDefine = getVocabularyDefine(textInfo);
# print vocabularyDefine
# print len(vocabularyDefine)

print "----------------------------------------------------------------------------"

vocabularyExample = getVocabularyExample(textInfo);
# print vocabularyExample
# print len(vocabularyExample)

print "----------------------------------------------------------------------------"

printToFile()
print "Complete!!!"
