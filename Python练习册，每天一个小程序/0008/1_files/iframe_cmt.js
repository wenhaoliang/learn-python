/**
 * 评论系统前端JS
 * @auth pingrj & luanhm
 * @date 2014-11-12 
 */
var Share=function(){
		this.init.apply(this,arguments)
	};
	Share.prototype={
		init:function(options){
			this.btn=options.btn;
			this.parent=options.parent;
			this.btn.on("mouseenter",function(event){
				event.preventDefault();
				$(this).parent().find(".shareBox").css({display:"block"});
			})
			this.parent.on("mouseleave",function(event){
				event.preventDefault();
				$(this).find(".shareBox").css({display:"none"});
			})
		}
};
$(document).ready(function(){
	var d = document,params = {};
	$("script").each(function(){
		var sSrc=$(this).attr("src");
		if(typeof(sSrc)!="undefined" && sSrc.indexOf('iframe_cmt.js') != -1){
		 	ss=$(this).attr('src');
		}		
	});
	ss.replace(/(uid|artinfo_id|style|lang|sub_artinfo_id|css_url)=([^&]+)/g, function(a, p, v) {
		params[p] = v;
	});
	//评论大对象
	window.CMSCMT = {
		lang : {},
		apiHost: '', //  如'http://comment.51cto.com/'，在init方法里赋值		
		api_js_dir: '', //如'http://comment.51cto.com/static/js/api_js/‘，在init方法里赋值
		imgHost: 'http://v2.CMSCMT.cc/code/images/',		
		
		
		/**
		 *  通过ajax提交jsonp函数的一个简洁封装
		 * @example CMSCMT.sendJsonp('test',{"aa":"1234","name":"luanhm"},'CMSCMT.testme');
		 * @param: m 请求到cc框架url中的m参数
		 * @param :data 数据
		 * @param: jsonpCallback 回掉函数的函数名 
		 * @return null 
		 * 
		 */
		sendJsonp: function(m,data,jsonpCallback){
			data.artinfo_id = CMSCMT.conf.artinfo_id; //全局artinfo_id
			data.sub_artinfo_id = params['sub_artinfo_id'];//全局的子评论id
			$.ajax({
		        type: "get",
		        //async: false, //设置为发送同步请求
		        data : data,
		        url:  CMSCMT.apiHost+"index.php?m="+m,
		        dataType: "jsonp",
		        timeout : 10000, //10s超时 
		        //jsonp: "callback",//传递给请求处理程序或页面的，用以获得jsonp回调函数名的参数名(一般默认为:callback)
		        jsonpCallback: jsonpCallback,//自定义的jsonp回调函数名称，默认为jQuery自动生成的随机函数名，也可以写"?"，jQuery会自动为你处理数据
		        success: function(data){            
		            alert("已提交");
		       }
		    });
		},

		getHost:function(){
			$("script").each(function(){
				var sSrc=$(this).attr("src");
				if(typeof(sSrc)!="undefined" && sSrc.indexOf('iframe_cmt.js') != -1){
					ss=$(this).attr('src');
				}
			});
			ss = parseURL(ss);
			ss = ss.host;
			var cms_host = 'http://' + ss;
			//console.log(ss);
			/*var cur_host = window.location.host;
			if(/\.hc3i\.cn/.test(cur_host) == true){
				cms_host = 'http://comment.hc3i.cn';
			}else if(/\.51cto\.com/.test(cur_host) == true){
				cms_host = 'http://comment.51cto.com';
			}else if(/\.watchstor\.com/.test(cur_host) == true){
				cms_host = 'http://comment.watchstor.com';
			}*/
			return cms_host;
		},
		/*随机函数*/
		randNum: function() {
		    var r = '',
		        n = 10;
		    for (var i = 0; i < n; i++) r += Math.floor(Math.random() * 10);
		    return r
		},
		
		/*初始化执行的函数*/
		init:function(Func){
			//加载样式js ,以及配置js  
			var url=window.location.href;
			var title=$("title").text();
			title=title.replace(' - 51CTO.COM', "");
			
			CMSCMT.apiHost = CMSCMT.getHost()+'/';
			CMSCMT.api_js_dir = CMSCMT.getHost()+'/static/js/api_js/';
			
			var src_conf = CMSCMT.apiHost+"index.php?do=index&m=get_js_conf2&artinfo_id="+ params['artinfo_id']+ "&sub_artinfo_id="+ params['sub_artinfo_id']+"&url="+ encodeURIComponent(url)+"&title="+ encodeURIComponent(title);
			//var src_style = CMSCMT.api_js_dir+'style1.js?' + "&"/* + CMSCMT.randNum()*/; //todo style后的编号可以在conf中动态配置
			//var src_conf = CMSCMT.apiHost+"index.php?do=index&m=get_style1";

			/*$.ajax({
				url: src_conf,
				async: false,
				dataType: "script"
			});
			$.ajax({
				url: src_style,
				async: false,
				dataType: "script"				
			});	*/
			CMSCMT
			$.getJSON(src_conf+"&jsoncallback=?",function(PARAM){
				CMSCMT.conf = PARAM.conf;
				CMSCMT.lang = PARAM.lang;
					try{
						window.CMSCMT.sjs = "";
						window.CMSCMT.sjs += "<div class='title'>";
						window.CMSCMT.sjs += "<span class='word'>"+CMSCMT.lang.boxTitle+"</span>";
						window.CMSCMT.sjs += "<p class='con'>";
						window.CMSCMT.sjs += CMSCMT.lang.boxNumStr1+"<span class='total' id='cmt_num'>0</span>"+CMSCMT.lang.boxNumStr2+",<span class='total' id='zan_num'>0</span>"+CMSCMT.lang.boxZan;
						window.CMSCMT.sjs += "</p><p style='float:right; margin-top: 17px;'>"+CMSCMT.lang.boxTishi1+"<span id=\"uyan_tts\" >500</span>"+CMSCMT.lang.boxTishi2+"</p>";
						window.CMSCMT.sjs += "</div>";
						window.CMSCMT.sjs += "<div class='frame center'>";
						window.CMSCMT.sjs += "<textarea value='' id=\"comment\" onblur=\"window.CMSCMT.shoIntro(this);\" onfocus=\"window.CMSCMT.hidIntro(this);\" onkeydown=\"window.CMSCMT.checkTxt(this, 140);\" onkeyup=\"window.CMSCMT.checkTxt(this, 140);\" style=\"color:#7c7c7c; font-family:Microsoft Yahei;\">"+CMSCMT.lang.iptCmt+"</textarea>";
						window.CMSCMT.sjs += "</div>";
						window.CMSCMT.sjs += "<div class='user'>";
						window.CMSCMT.sjs += "<a  id=\"uyan_cmt_btn\" onclick=\"window.CMSCMT.addCmt(this);\"  class='submit'>";
						window.CMSCMT.sjs += CMSCMT.lang.boxSubmit;
						window.CMSCMT.sjs += "</a>";
						window.CMSCMT.sjs += "<dl>";

						if(CMSCMT.conf.islogin == 1){
							window.CMSCMT.sjs += "<dt class='icon'><img src=\""+CMSCMT.conf.uface+"\" alt=\"\" /></dt>";
							window.CMSCMT.sjs += "<dd class='msg'><span class='name'>"+CMSCMT.conf.uname+"</span>"+CMSCMT.lang.userStr1+"</dd>";
						}else if(CMSCMT.conf.islogin == 0){
							window.CMSCMT.sjs += "<dt class='icon'><img src='http://comment.51cto.com/static/images/duface.png' alt=\"\" /></dt>";
							window.CMSCMT.sjs += "<dd class='btn'>";
							window.CMSCMT.sjs += "<span >"+CMSCMT.lang.userStr2+"</span>";
							window.CMSCMT.sjs += "<span class='note'>"+CMSCMT.lang.userStr3+"</span>";
							window.CMSCMT.sjs += "&nbsp;<a href=\""+CMSCMT.conf.login_url+"\" style='color:red;' >"+CMSCMT.lang.userStr4+"</a>&nbsp;";
							window.CMSCMT.sjs += "<span class='note'>"+CMSCMT.lang.userStr5+"</span>";
							window.CMSCMT.sjs += "&nbsp;<a href=\""+CMSCMT.conf.reg_url+"\" style='color:red;'>"+CMSCMT.lang.userStr6+"</a>&nbsp;";
							window.CMSCMT.sjs += "</dd>";
						}
						window.CMSCMT.sjs += "</dl>";
						window.CMSCMT.sjs += "</div>";
						window.CMSCMT.sjs += "<ul class='list center first' id='uyan_cmt_list'>";
						window.CMSCMT.sjs += "<li style='text-align: center;'> "+CMSCMT.lang.userStr7+" </li></ul>";
						window.CMSCMT.sjs += "<div class='more line' id='uyan_more_cmt'><a >"+CMSCMT.lang.userStr8+">></a></div>";
					} catch (e) {console.log(e)}

				CMSCMT.conf.url=url;
				CMSCMT.conf.title=title;
				//alert(window.CMSCMT.sjs);
				//根据配置加载样式
				if( params['css_url'] == undefined){
					var layout_css = CMSCMT.getHost()+"/static/css/layout"+CMSCMT.conf.layout+".css";
				} else {
					var layout_css = params['css_url'];
				}
				$("<link>").attr({ rel: "stylesheet",type: "text/css", href: layout_css}).appendTo("head");
				$("#cmscmt_iframe").html(window.CMSCMT.sjs);

				Func();
			})
			

		/*	setTimeout(function() {
				CMSCMT.conf.url=url;
				CMSCMT.conf.title=title;
				//alert(window.CMSCMT.sjs);
				//根据配置加载样式

				if( params['css_url'] == undefined){
					var layout_css = CMSCMT.getHost()+"/static/css/layout"+CMSCMT.conf.layout+".css";
				} else {
					var layout_css = params['css_url'];
				}
				$("<link>").attr({ rel: "stylesheet",type: "text/css", href: layout_css}).appendTo("head");
				$("#cmscmt_iframe").html(window.CMSCMT.sjs);
			}, 1100)*/
			
        },
		islogin: function () { 
        	if(CMSCMT.conf.islogin!=1){
				alert(CMSCMT.lang.userStr2);
				return false;
			}else{return true;}
        },
	isforbid: function () {
		if(CMSCMT.conf.isforbid != 1){
			alert(CMSCMT.lang.forbidden_comment);
			return false;
		}else{return true;}
	}, 		       
        /*休眠函数*/
      sleep: function (numberMillis) { 
        	var now = new Date(); 
        	var exitTime = now.getTime() + numberMillis; 
        	while (true) { 
        	 	now = new Date(); 
        	 	if (now.getTime() > exitTime) 
        	 	return; 
        	 	} 
        },
        cmtShare : function(t,cont){
			cont=cont.substr(0,130);
			var url='';	
			if(t=='tqq'){
				url='http://share.v.t.qq.com/index.php?c=share&a=index&url='+ CMSCMT.conf.url +'&title='+ cont ;	
			}else if(t=='sina'){
				var sinaTitle='';
				if(CMSCMT.conf.domain=='51cto.com'){
					cont=cont.substr(0,80);
					sinaTitle=  CMSCMT.lang.shareSina1 + cont + CMSCMT.lang.shareSina2 + CMSCMT.conf.title + CMSCMT.lang.shareSina3;
					sinaTitle = encodeURIComponent(sinaTitle);	
				}else{
					sinaTitle=cont;	
				}
				url='http://service.weibo.com/share/share.php?title='+ sinaTitle +'&url='+ CMSCMT.conf.url +'#jtss-tsina&source=bookmark&appkey=2378297317&pic=&ralateUid=';	
			}else if(t=='qzone'){
				url='http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url='+ CMSCMT.conf.url +'%23jtss-qzone&title='+ cont +'&summary=-+51CTO.COM';	
			}
			
			//url=encodeURIComponent(url);
			window.open(url);
		},
        /*显示评论列表——被php数出的js调用*/
       showCmtlist: function(rs){
        	rs = eval(rs);
        	var list = rs.data
        	if(!list){
        		return false;
        	}
        	var strVar = "";

        	$(list).each(function (key, val){
//        		alert(val.uname);        		
        		    strVar += "";
					
					strVar += "<li class='element' id='cmt_"+ val.id +"'>";
					strVar += "<dl class=''>";
					strVar += "<dt class='head'>";
					strVar += "<a target=\"_blank\" href=\""+ val.home  +"\">";
					strVar += "<img onerror=\"CMSCMT.noUface(this, '/static/images/duface.png');\"";
        		    strVar += "src=\""+ val.uface +"\"";
        		    strVar += "onload=\"CMSCMT.loadUface(this, '"+ val.uface +"');\"";
        		    strVar += "style=\"border: 0 none; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.22); border-radius: 4px; width: 50px; height: 50px;\">";
        		    strVar += "</a>";
					strVar += "</dt>";
					strVar += "<dd>";
					strVar += "<div class='name'>";
					strVar += "<a target=\"_blank\" href=\""+ val.home +"\" id=\"cmt_uname_"+ val.id +"\">"+val.uname +"<\/a>";
					strVar += "</div>";
					strVar += "<p class='con'>"+ val.content +"</p>";
					strVar += "<div class='tool line one'>";
					strVar += "<div class='date'>"+CMSCMT.lang.userStr9+ val.cTime +"</div>";
					strVar += "<div class='btn'>";
					strVar += "<div class='shareBox'>";
					//strVar += "<div><img width=\"20\" height=\"20\" onclick=\"CMSCMT.share('sina','测试8')\" src=\"static/images/sina.jpg\">";
					strVar += "<div class=\"jiathis_style_24x24\">";					
					strVar += "<a class=\"jiathis_button_tsina\" onclick=\"CMSCMT.cmtShare('sina','"+ val.content +"');\"><img src='http://s2.51cto.com/wyfs02/M00/58/35/wKioL1SsonugeKo0AAAGlF6KMqM876.png' alt=''></a>";
					strVar += "<a class=\"jiathis_button_qzone\" onclick=\"CMSCMT.cmtShare('qzone','"+ val.content +"');\"><img src='http://s3.51cto.com/wyfs02/M02/58/39/wKiom1SsobuxdEMvAAAF92NU77A112.png' alt=''></a>";
					strVar += "<a class=\"jiathis_button_tqq\" onclick=\"CMSCMT.cmtShare('tqq','"+ val.content +"');\"><img src='http://s8.51cto.com/wyfs02/M00/58/39/wKiom1SsobuDEp5ZAAAGB9ePTKU216.png' alt=''></a>";
					strVar += "</div></div>";
					strVar += "<a class=\"reply self\" style=\"cursor: pointer;\"  onclick=\"CMSCMT.addRpyBox("+ val.id +","+ val.id +",'one');\" id=\"cmt_rpy_"+ val.id +"\" >"+ CMSCMT.lang.addRpy +" <\/a>";
					strVar += "<a class=\"support self\" style=\"cursor: pointer; \"  onclick=\"CMSCMT.cmtUD("+ val.id +");\">"+ CMSCMT.lang.dS +"(<span id=\"zan_"+ val.id +"\">"+ val.zan_count +"</span>)<\/a><a  class=\"share self\">"+ CMSCMT.lang.cmtShare +" </a>";
					strVar += "</div>";
					strVar += "</div>";
					strVar += "<ul class='list center second' id='cmt_reply_list_" + val.id + "'>";
					if(val.reply_list){
         		    	strVar += CMSCMT.showReplylist(val.reply_list, true,val.id);
         		    }
					strVar += "</ul>";
					strVar += "</dd>";
				    strVar += "</dl>";
			        strVar += "</li>";


        		   //查看更多回复按钮
        		  strVar += '<li><div id="uyan_more_rpy_' + val.id +'">';
        		  if(val.reply_list && val.reply_list.data.length >= CMSCMT.conf.fr_pagesize){
           		   strVar += '<div id="uyan_more_rpy_' + val.id + '" onclick="CMSCMT.getReply(2, '+ val.id +');" style="cursor: pointer; background: none repeat scroll 0 0 #fcfcfc; height: 28px; line-height: 28px; display: block; border: 1px solid #dcdcdc; margin-top: 15px; margin-bottom: 10px; text-align: center; border-radius: 3px; font-size: 13px; color: #424242; text-decoration: none; margin-left: 60px;">'+ CMSCMT.lang.mRpyS +'<img src="'+ CMSCMT.apiHost +'static/images/arrow.png" style="padding-left: 4px; border: none; display: inline;">';
           		   strVar += '</div></li>';  
        		   }
        	})
        	
        	//评论列表显示
        	if(rs.page == 1){
        		$("#uyan_cmt_list").html(strVar);  
        	}else {
        		$("#uyan_cmt_list").append(strVar);
        	}
        	
        	//查看更多评论按钮
        	if(!CMSCMT.conf.comment_count ||list.length < CMSCMT.conf.fc_pagesize){//没有评论了
        		$("#uyan_more_cmt").html("");
        	} else { //分页按钮（点击更多）page+1
        		var more_btn = '<div onclick="CMSCMT.getCmt('+(rs.page+1)+');"  style="cursor: pointer; background: none repeat scroll 0 0 #fcfcfc; height: 28px; line-height: 28px; display: block; border: 1px solid #dcdcdc; margin-top: 15px; margin-bottom: 10px; text-align: center; border-radius: 3px; font-size: 13px; color: #424242; text-decoration: none;">'+ CMSCMT.lang.mCmtS +'<img src="'+ CMSCMT.apiHost +'static/images/arrow.png" style="padding-left: 4px; border: none; display: inline;"></div>';
    			$("#uyan_more_cmt").html(more_btn);	
        	}
       },
       
       	/*显示回复列表*/
       showReplylist: function (rs, is_return,rpyid){
    		rs = eval(rs);
        	var list = rs.data; 
        	if(!list){
        		//隐藏更多回复按钮
        		$("#uyan_more_rpy_"+rs.reply_id).html("");
        		return false;
        	}
        	
        	var restrVal = ''; //函数间变量名也不要用相同的
      	$(list).each(function (key, val){ 
      		restrVal += "";
			restrVal += "<li class='element line'  id=\"cmt_"+ val.id +"\">";
			restrVal += "		<dl>";
			restrVal += "			<dt class='head'>";
			restrVal += "        <a target=\"_blank\" style=\"cursor: pointer; text-decoration: none; white-space: inherit;\"";
      		restrVal += "        href=\""+ val.home +"\">";
      		restrVal += "            <img onerror=\"CMSCMT.noUface(this, '/static/images/duface.png');\"";
      		restrVal += "            src=\""+ val.uface +"\"";
      		restrVal += "            onload=\"CMSCMT.loadUface(this, '"+ val.uface +"', '/static/images/duface.png');\"";
      		restrVal += "            style=\"border: 0 none; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.22); border-radius: 4px; width: 50px; height: 50px;\">";
      		restrVal += "        <\/a>";
			
			restrVal += "</dt>";
			restrVal += "			<dd>";
			restrVal += "				<div class='name'>";
			restrVal += "            <a target=\"_blank\" href=\""+ val.home +"\" id=\"cmt_uname_"+ val.id +"\">"+val.uname+"<\/a>";
			restrVal += "</div>";
			restrVal += "				<p class='con'>"+ val.content +"</p>";
			restrVal += "				<div class='tool line'>";
			restrVal += "					<div class='date'>"+CMSCMT.lang.userStr9 + val.cTime +"</div>";
			restrVal += "					<div class='btn'>";
			restrVal += "						<div class='shareBox'>";
			restrVal += "							<div class=\"jiathis_style_24x24\">";
			restrVal += "								<a class=\"jiathis_button_tsina\"  onclick=\"CMSCMT.cmtShare('sina','"+ val.content +"');\"><img src='http://s2.51cto.com/wyfs02/M00/58/35/wKioL1SsonugeKo0AAAGlF6KMqM876.png' alt=''></a>";
			restrVal += "								<a class=\"jiathis_button_qzone\"  onclick=\"CMSCMT.cmtShare('qzone','"+ val.content +"');\"><img src='http://s3.51cto.com/wyfs02/M02/58/39/wKiom1SsobuxdEMvAAAF92NU77A112.png' alt=''></a>";
			restrVal += "								<a class=\"jiathis_button_tqq\" onclick=\"CMSCMT.cmtShare('tqq','"+ val.content +"');\"><img src='http://s8.51cto.com/wyfs02/M00/58/39/wKiom1SsobuDEp5ZAAAGB9ePTKU216.png' alt=''></a>";
			restrVal += "							</div>";
			restrVal += "						</div>";
			restrVal += "<a class=\"reply self\" style=\"cursor: pointer;\"  onclick=\"CMSCMT.addRpyBox("+ val.id +","+ rpyid +");\" id=\"cmt_rpy_"+ val.id +"\" >"+ CMSCMT.lang.addRpy +" <\/a>";
			restrVal += "<a class=\"support self\" style=\"cursor: pointer; \"  onclick=\"CMSCMT.cmtUD("+ val.id +");\">"+ CMSCMT.lang.dS +"(<span id=\"zan_"+ val.id +"\">"+ val.zan_count +"</span>)<\/a><a  class=\"share self\">"+ CMSCMT.lang.cmtShare +"</a>";
			restrVal += "					</div>";
			restrVal += "				</div>";
			restrVal += "			</dd>";
			restrVal += "		</dl>";
			restrVal += "	</li>";
							
      		
      		})
		  
    	   if(is_return){     		   
    		   return restrVal;
    	   } else {
    		   $("#cmt_reply_list_"+rs.reply_id).append(restrVal);
    		   
    		   //更新"更多回复"按钮
	       	if(list.length < CMSCMT.conf.fr_pagesize){//没有更多回复了
	       		$("#uyan_more_rpy_"+rs.reply_id).html("");
	       	} else { //分页按钮（点击更多）page+1
	       		var more_btn = '<li><div id="uyan_more_rpy_' + rs.reply_id + '" onclick="CMSCMT.getReply('+(rs.page+1) +', '+ rs.reply_id +');" style="cursor: pointer; background: none repeat scroll 0 0 #fcfcfc; height: 28px; line-height: 28px; display: block; border: 1px solid #dcdcdc; margin-top: 15px; margin-bottom: 10px; text-align: center; border-radius: 3px; font-size: 13px; color: #424242; text-decoration: none; margin-left: 60px;">'+ CMSCMT.lang.mRpyS +'<img src="'+ CMSCMT.apiHost +'static/images/arrow.png" style="padding-left: 4px; border: none; display: inline;"></div></li>';
	       		$("#uyan_more_rpy_"+rs.reply_id).html(more_btn);
	       		}
    	   }
         },
		htmlEncode :function(str) 
		{
			return str.replace(/&/g, '&amp').replace(/</g, '&lt;').replace(/>/gi, '&gt;').replace(/"/gi, '&quot;').replace(/'/g, '&#039');
		},
       	onShare: function(th){
			$this=$(th);
			$this.parent().find(".shareBox").css({display:"block"});
			
		}, 
		outShare: function(th){
			$this=$(th);
			$this.parent().find(".shareBox").css({display:"none"});
			
		},
         /*没有头像的用户 todo*/ 
		noUface: function(e, u) {
			e.onerror = function() {};
			if (u != null && u != '') {
				e.src = u
			}
        },
         /*读配置中的默认头像*/
		loadUface: function(e, u) {
			if (u != null && u != '') {
				setTimeout(function() {
					e.src = u
				}, 1000)
			}
			e.onload = function() {};
		},
		changeS: function (){
         
        },
         
         mouseOO: function (){
        	 
         },
        
         /*顶评论*/
         cmtUD: function (cid){
			 if(!CMSCMT.islogin()) return false;
			if(!CMSCMT.isforbid()) return false;
			CMSCMT.sendJsonp('cmtZan',{"cid":cid,"url":CMSCMT.conf.url,"title":CMSCMT.conf.title,artinfo_id:CMSCMT.conf.artinfo_id},'CMSCMT.hidZan');
         },
		 hidZan: function(rs){
			if(rs['rs']){
				var $zanobj = $("#zan_"+ rs['cmtid']); 
				var zan=$zanobj.html();
				var zan_all=$('#zan_num').text();
				
				zan = parseInt(zan) + 1;
				zan_all = parseInt(zan_all) + 1;
				$zanobj.html(zan);	 
				$zanobj.parent().removeAttr('onclick');
				$zanobj.parent().css("color","red");
				$('#zan_num').text(zan_all);
				
			}
		},
         
         /* 隐藏输入框提示*/
         hidIntro: function (th){
			if($(th).val() == CMSCMT.lang.iptCmt){
				$(th).val('');
			}
			//alert($("#"+ id).val());
         },
         /*显示输入框提示*/	
         shoIntro: function (th){
			 if($(th).val() == ''){
				$(th).val(CMSCMT.lang.iptCmt);
			}
         },
         
         /*实时统计评论字数*/
         checkTxt: function (th,total,rid){
        	 $this=$(th);
			 n=$this.val().length;
			 yn=total-n;
			 if(rid!='') $('#cmt_tts_' + rid).text(yn);
			 $('#uyan_tts').text(yn);
         },
         
         /*改变按钮状态*/
         cagBtn: function (){
        	 
         },
         
         /*添加评论*/
         addCmt: function (th){
			if(!CMSCMT.islogin()) return false; 
			if(!CMSCMT.isforbid()) return false;
			var content=$("#comment").val();
			if(content==''){
				return false;
			}
			if(content==CMSCMT.lang.iptCmt){				
				return false;
			}
			CMSCMT.conf.content=content;
			CMSCMT.sendJsonp('addCmt',{"content":content,"url":CMSCMT.conf.url,"title":CMSCMT.conf.title,"artinfo_id":CMSCMT.conf.artinfo_id},'CMSCMT.addCmtDo');
			 
         },
         /*添加评论回调函数*/
         addCmtDo: function (rs){
			 CMSCMT.conf.content=CMSCMT.htmlEncode(CMSCMT.conf.content);
			 if(rs){		
				var cmt_cont='<li id="cmt_'+ rs +'" class="element"><dl><dt class="head"><a href="#" style="cursor: pointer; text-decoration: none; white-space: inherit;" target="_blank"><img style="border: 0 none; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.22); border-radius: 4px; width: 50px; height: 50px;" onload="CMSCMT.loadUface(this, \''+ CMSCMT.conf.uface +'\', \'http://v2.CMSCMT.cc/code/images/duface.png\');" src="'+ CMSCMT.conf.uface +'" ></a></dt><dd><div class="name"><a id="cmt_uname_'+ rs +'"  href="'+  CMSCMT.conf.home +'" target="_blank" >'+ CMSCMT.conf.uname +'</a></div><p class="con">'+ CMSCMT.conf.content +'</p><div class="tool line one"><div class="date">'+ CMSCMT.lang.userStr9 +''+ CMSCMT.get_date() +'</div><div class="btn"><div class="shareBox"><div class=\"jiathis_style_24x24\"><a class=\"jiathis_button_tsina\" onclick="CMSCMT.cmtShare(\'sina\',\''+ CMSCMT.conf.content +'\');"><img src=\"http://s2.51cto.com/wyfs02/M00/58/35/wKioL1SsonugeKo0AAAGlF6KMqM876.png\" ></a><a class=\"jiathis_button_qzone\" onclick="CMSCMT.cmtShare(\'qzone\',\''+ CMSCMT.conf.content +'\');"><img src=\"http://s3.51cto.com/wyfs02/M02/58/39/wKiom1SsobuxdEMvAAAF92NU77A112.png\"></a><a class=\"jiathis_button_tqq\" onclick="CMSCMT.cmtShare(\'tqq\',\''+ CMSCMT.conf.content +'\');"><img src=\"http://s8.51cto.com/wyfs02/M00/58/39/wKiom1SsobuDEp5ZAAAGB9ePTKU216.png\"></a></div></div><a id="cmt_rpy_'+ rs +'" onclick="CMSCMT.addRpyBox('+ rs +','+ rs +',\'one\');" class="reply self"  style="cursor: pointer;">'+ CMSCMT.lang.addRpy +'</a><a onclick="CMSCMT.cmtUD('+ rs +');" class=\"support self\">'+ CMSCMT.lang.dS +'<span id="zan_'+ rs +'">0</span></a><a class=\"share self\">'+ CMSCMT.lang.cmtShare +'</a></div></div><ul id="cmt_reply_list_'+ rs +'" class="list center second"></ul></dd></dl></li>';
			 	$("#uyan_cmt_list").prepend(cmt_cont);
			 	$("#comment").val(CMSCMT.lang.iptCmt);
				$("#uyan_cmt_list_warn").remove();
				var cmt_num=$('#cmt_num').text();
				cmt_num = parseInt(cmt_num) + 1;
				$('#cmt_num').text(cmt_num);
			 }
         },
         /*添加回复框*/
		addRpyBox: function (cmtid,rpyid,cla){
			if(!CMSCMT.islogin()){
				return false;
			}
			if(!CMSCMT.isforbid()) return false;
			var cmtbox=$("#cmt_rpybox_"+ cmtid);
			if(cmtbox.length>0){
				if(cmtbox.is(':visible')){
					cmtbox.css("display","none");
				}else{
					cmtbox.css("display","block");	
				}
			}else{
				var rpyuname="@"+ $("#cmt_uname_" + cmtid).text() +":";
				rpyuname=$.trim(rpyuname);
				var rpybox="<div class='sub_frame' id='cmt_rpybox_"+ cmtid +"'>";
				if(cla=='one'){
					rpybox += "<div class='core'>";
				}else{
					rpybox += "<div class='core2'>";	
				}
				rpybox += "<textarea onkeydown='CMSCMT.checkTxt(this, 500,"+cmtid+");' onkeyup='CMSCMT.checkTxt(this, 500, "+cmtid+");' id='comment_"+ cmtid +"'>"+ rpyuname +"</textarea></div><div class='btn' id='cmt_rpy_btn_"+ cmtid +"' onclick='CMSCMT.addRpy(this, "+ cmtid +","+ rpyid +");'><a>"+ CMSCMT.lang.addRpy +"</a></div></div>";
				//console.log("#cmt_" + cmtid);
				
				if(cla=='one'){
					$("#cmt_" + cmtid).find('.one').after(rpybox);	
				}else{
					$("#cmt_" + cmtid).append(rpybox);
				}
				
				
				//
				
				
			}
			
         },
		/*添加回复*/
		addRpy: function (th,cid,rpyid){
			if(!CMSCMT.islogin()) return false;
			if(!CMSCMT.isforbid()) return false;
			var rpy_cont=$("#comment_" + cid).val();
			CMSCMT.conf.rpyContent=rpy_cont;
			CMSCMT.conf.rid=rpyid;
			CMSCMT.conf.rpyboxid=cid;
			CMSCMT.sendJsonp('addRpy',{"rpyid":rpyid,"artinfo_id":CMSCMT.conf.artinfo_if,"content":rpy_cont,"col_id":CMSCMT.conf.col_id},'CMSCMT.addRpyDo');	 
		},
		addRpyDo: function (rs){
			CMSCMT.conf.rpyContent=CMSCMT.htmlEncode(CMSCMT.conf.rpyContent);
			var rpy_content='<li id="cmt_'+ rs +'" class="element line"><dl><dt class="head"><a href="'+  CMSCMT.conf.home +'" style="cursor: pointer; text-decoration: none; white-space: inherit;" target="_blank"><img style="border: 0 none; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.22); border-radius: 4px; width: 50px; height: 50px;" onload="CMSCMT.loadUface(this, \''+  CMSCMT.conf.uface +'\', \'http://v2.CMSCMT.cc/code/images/duface.png\');" src="'+  CMSCMT.conf.uface +'" onerror="CMSCMT.noUface(this, \''+  CMSCMT.conf.uface +'\');"></a></dt><dd><div class="name"><a id="cmt_uname_'+ rs +'" href="'+  CMSCMT.conf.home +'" target="_blank">'+  CMSCMT.conf.uname +'</a></div><p class="con">'+ CMSCMT.conf.rpyContent +'</p><div class="tool line"><div class="date">'+CMSCMT.lang.userStr9+ CMSCMT.get_date() +'</div><div class="btn"><div class="shareBox" style="display: none;"><div class="jiathis_style_24x24"><a class="jiathis_button_tsina"  onclick="CMSCMT.cmtShare(\'sina\',\''+ CMSCMT.conf.rpyContent +'\');"><img src="http://s2.51cto.com/wyfs02/M00/58/35/wKioL1SsonugeKo0AAAGlF6KMqM876.png" alt=""></a><a class="jiathis_button_qzone"  onclick="CMSCMT.cmtShare(\'qzone\',\''+ CMSCMT.conf.rpyContent +'\');"><img src="http://s3.51cto.com/wyfs02/M02/58/39/wKiom1SsobuxdEMvAAAF92NU77A112.png" alt=""></a><a class="jiathis_button_tqq"  onclick="CMSCMT.cmtShare(\'tqq\',\''+ CMSCMT.conf.content +'\');"><img src="http://s8.51cto.com/wyfs02/M00/58/39/wKiom1SsobuDEp5ZAAAGB9ePTKU216.png" alt=""></a></div>						</div><a id="cmt_rpy_'+ rs +'" onclick="CMSCMT.addRpyBox('+ rs +','+ CMSCMT.conf.rid +');" style="cursor: pointer;" class="reply self" id="cmt_rpy_'+ rs +'" onclick="CMSCMT.addRpyBox('+ rs +','+ CMSCMT.conf.rid +');">'+ CMSCMT.lang.addRpy +'</a><a style="cursor: pointer;" class="support self" onclick="CMSCMT.cmtUD('+ rs +');" >'+ CMSCMT.lang.dS +'(<span id="zan_'+ rs +'">0</span>)</a><a class="share self">'+ CMSCMT.lang.cmtShare +'</a></div></div></dd></dl></li>';
			//console.log("#cmt_reply_list_"+CMSCMT.conf.rid);
			$("#cmt_reply_list_"+CMSCMT.conf.rid).append(rpy_content);
			$("#cmt_rpybox_"+CMSCMT.conf.rpyboxid).remove();
			var cmt_num=$('#cmt_num').text();
			cmt_num = parseInt(cmt_num) + 1;
			$('#cmt_num').text(cmt_num);
		},
		/*？？？*/
		hideBox: function (){
		   
		},
		/*？？？*/
		cmty: function (){
		   
		},
		
		/*显示更多评论*/
		showMoreCmtlist:function (){
		   
		},
		
		/*显示更多回复*/
		showMoreReplylist:function (){
		   
		},
		 
		/*分页获取评论*/
		getCmt:function (page){
			CMSCMT.sendJsonp('get_cmtlist',{"page":page},'CMSCMT.showCmtlist');
		}, 
		
		/*分页获取回复*/
		getReply: function (page, reply_id){
			CMSCMT.sendJsonp('get_replylist',{"page":page, "reply_id":reply_id},'CMSCMT.showReplylist');
		},
		get_date:function (){
			var d=new Date();
			var date=d.getFullYear()+"-"+(d.getMonth()+1)+"-"+d.getDate()+" "+d.getHours()+":"+d.getMinutes()+":"+d.getSeconds();	
			return date;
		},
		creSye: function(s) {
			var b = d.createElement('style');
			b.type = 'text/css';
			if (b.styleSheet) {
				b.styleSheet.cssText = s
			} else {
				b.appendChild(d.createTextNode(s))
			}
			d.getElementsByTagName('head')[0].appendChild(b)
		}
         
	} 
	
	try{		
		CMSCMT.init(function(){
			if(CMSCMT.conf.comment_count > 0){
				CMSCMT.getCmt(1); //初始化显示第一页评论，如果有的话。
				new Share({
					btn:$("#uyan_cmt_list").find(".share"),
					parent:$("#uyan_cmt_list").find(".btn")
				});
				$("#cmt_num").html(CMSCMT.conf.comment_count);
				$("#zan_num").html(CMSCMT.conf.zan_count);
			}else{
				$("#uyan_cmt_list").html('<div style="margin-top: 10px; padding-top: 10px; font-size: 12px; color: #303030; text-align: center;" id="uyan_cmt_list_warn">'+ CMSCMT.lang.noCmt +'</div>');
				$("#uyan_more_cmt").remove();
			}
		});
		/*setTimeout(function() {
			
			if(CMSCMT.conf.comment_count > 0){
				CMSCMT.getCmt(1); //初始化显示第一页评论，如果有的话。
				new Share({
					btn:$("#uyan_cmt_list").find(".share"),
					parent:$("#uyan_cmt_list").find(".btn")
				});
				$("#cmt_num").html(CMSCMT.conf.comment_count);
				$("#zan_num").html(CMSCMT.conf.zan_count);
			}else{
				$("#uyan_cmt_list").html('<div style="margin-top: 10px; padding-top: 10px; font-size: 12px; color: #303030; text-align: center;" id="uyan_cmt_list_warn">'+ CMSCMT.lang.noCmt +'</div>');
				$("#uyan_more_cmt").remove();
			}
		},1100)*/
	} catch (e) {}
});

function parseURL(url) {
	var a =  document.createElement('a');
	a.href = url;
	return {
		source: url,
		protocol: a.protocol.replace(':',''),
		host: a.hostname,
		port: a.port,
		query: a.search,
		params: (function(){
			var ret = {},
					seg = a.search.replace(/^\?/,'').split('&'),
					len = seg.length, i = 0, s;
			for (;i<len;i++) {
				if (!seg[i]) { continue; }
				s = seg[i].split('=');
				ret[s[0]] = s[1];
			}
			return ret;
		})(),
		file: (a.pathname.match(/\/([^\/?#]+)$/i) || [,''])[1],
		hash: a.hash.replace('#',''),
		path: a.pathname.replace(/^([^\/])/,'/$1'),
		relative: (a.href.match(/tps?:\/\/[^\/]+(.+)/) || [,''])[1],
		segments: a.pathname.replace(/^\//,'').split('/')
	};
}
