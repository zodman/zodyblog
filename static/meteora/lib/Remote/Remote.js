
Json.Remote=XHR.extend({initialize:function(url,options){this.url=url;this.addEvent('onSuccess',this.onComplete);this.parent(options);this.setHeader('X-Request','JSON');},send:function(obj){return this.parent(this.url,'json='+Json.toString(obj));},onComplete:function(){this.fireEvent('onComplete',[Json.evaluate(this.response.text,this.options.secure)]);}});