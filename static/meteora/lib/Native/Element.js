
var Element=new Class({initialize:function(el,props){if($type(el)=='string'){if(window.ie&&props&&(props.name||props.type)){var name=(props.name)?' name="'+props.name+'"':'';var type=(props.type)?' type="'+props.type+'"':'';delete props.name;delete props.type;el='<'+el+name+type+'>';}
el=document.createElement(el);}
el=$(el);return(!props||!el)?el:el.set(props);}});var Elements=new Class({initialize:function(elements){return(elements)?$extend(elements,this):this;}});Elements.extend=function(props){for(var prop in props){this.prototype[prop]=props[prop];this[prop]=$native.generic(prop);}};function $(el){if(!el)return null;if(el.htmlElement)return Garbage.collect(el);if([window,document].contains(el))return el;var type=$type(el);if(type=='string'){el=document.getElementById(el);type=(el)?'element':false;}
if(type!='element')return null;if(el.htmlElement)return Garbage.collect(el);if(['object','embed'].contains(el.tagName.toLowerCase()))return el;$extend(el,Element.prototype);el.htmlElement=function(){};return Garbage.collect(el);};document.getElementsBySelector=document.getElementsByTagName;function $$(){var elements=[];for(var i=0,j=arguments.length;i<j;i++){var selector=arguments[i];switch($type(selector)){case'element':elements.push(selector);case'boolean':break;case false:break;case'string':selector=document.getElementsBySelector(selector,true);default:elements.extend(selector);}}
return $$.unique(elements);};$$.unique=function(array){var elements=[];for(var i=0,l=array.length;i<l;i++){if(array[i].$included)continue;var element=$(array[i]);if(element&&!element.$included){element.$included=true;elements.push(element);}}
for(var n=0,d=elements.length;n<d;n++)elements[n].$included=null;return new Elements(elements);};Elements.Multi=function(property){return function(){var args=arguments;var items=[];var elements=true;for(var i=0,j=this.length,returns;i<j;i++){returns=this[i][property].apply(this[i],args);if($type(returns)!='element')elements=false;items.push(returns);};return(elements)?$$.unique(items):items;};};Element.extend=function(properties){for(var property in properties){HTMLElement.prototype[property]=properties[property];Element.prototype[property]=properties[property];Element[property]=$native.generic(property);var elementsProperty=(Array.prototype[property])?property+'Elements':property;Elements.prototype[elementsProperty]=Elements.Multi(property);}};Element.extend({set:function(props){for(var prop in props){var val=props[prop];switch(prop){case'styles':this.setStyles(val);break;case'events':if(this.addEvents)this.addEvents(val);break;case'properties':this.setProperties(val);break;default:this.setProperty(prop,val);}}
return this;},inject:function(el,where){el=$(el);switch(where){case'before':el.parentNode.insertBefore(this,el);break;case'after':var next=el.getNext();if(!next)el.parentNode.appendChild(this);else el.parentNode.insertBefore(this,next);break;case'top':var first=el.firstChild;if(first){el.insertBefore(this,first);break;}
default:el.appendChild(this);}
return this;},injectBefore:function(el){return this.inject(el,'before');},injectAfter:function(el){return this.inject(el,'after');},injectInside:function(el){return this.inject(el,'bottom');},injectTop:function(el){return this.inject(el,'top');},adopt:function(){var elements=[];$each(arguments,function(argument){elements=elements.concat(argument);});$$(elements).inject(this);return this;},remove:function(){return this.parentNode.removeChild(this);},clone:function(contents){var el=$(this.cloneNode(contents!==false));if(!el.$events)return el;el.$events={};for(var type in this.$events)el.$events[type]={'keys':$A(this.$events[type].keys),'values':$A(this.$events[type].values)};return el.removeEvents();},replaceWith:function(el){el=$(el);this.parentNode.replaceChild(el,this);return el;},appendText:function(text){this.appendChild(document.createTextNode(text));return this;},hasClass:function(className){return this.className.contains(className,' ');},addClass:function(className){if(!this.hasClass(className))this.className=(this.className+' '+className).clean();return this;},removeClass:function(className){this.className=this.className.replace(new RegExp('(^|\\s)'+className+'(?:\\s|$)'),'$1').clean();return this;},toggleClass:function(className){return this.hasClass(className)?this.removeClass(className):this.addClass(className);},setStyle:function(property,value){switch(property){case'opacity':return this.setOpacity(parseFloat(value));case'float':property=(window.ie)?'styleFloat':'cssFloat';}
property=property.camelCase();switch($type(value)){case'number':if(!['zIndex','zoom'].contains(property))value+='px';break;case'array':value='rgb('+value.join(',')+')';}
this.style[property]=value;return this;},setStyles:function(source){switch($type(source)){case'object':Element.setMany(this,'setStyle',source);break;case'string':this.style.cssText=source;}
return this;},setOpacity:function(opacity){if(opacity==0){if(this.style.visibility!="hidden")this.style.visibility="hidden";}else{if(this.style.visibility!="visible")this.style.visibility="visible";}
if(!this.currentStyle||!this.currentStyle.hasLayout)this.style.zoom=1;if(window.ie)this.style.filter=(opacity==1)?'':"alpha(opacity="+opacity*100+")";this.style.opacity=this.$tmp.opacity=opacity;return this;},getStyle:function(property){property=property.camelCase();var result=this.style[property];if(!$chk(result)){if(property=='opacity')return this.$tmp.opacity;result=[];for(var style in Element.Styles){if(property==style){Element.Styles[style].each(function(s){var style=this.getStyle(s);result.push(parseInt(style)?style:'0px');},this);if(property=='border'){var every=result.every(function(bit){return(bit==result[0]);});return(every)?result[0]:false;}
return result.join(' ');}}
if(property.contains('border')){if(Element.Styles.border.contains(property)){return['Width','Style','Color'].map(function(p){return this.getStyle(property+p);},this).join(' ');}else if(Element.borderShort.contains(property)){return['Top','Right','Bottom','Left'].map(function(p){return this.getStyle('border'+p+property.replace('border',''));},this).join(' ');}}
if(document.defaultView)result=document.defaultView.getComputedStyle(this,null).getPropertyValue(property.hyphenate());else if(this.currentStyle)result=this.currentStyle[property];}
if(window.ie)result=Element.fixStyle(property,result,this);if(result&&property.test(/color/i)&&result.contains('rgb')){return result.split('rgb').splice(1,4).map(function(color){return color.rgbToHex();}).join(' ');}
return result;},getStyles:function(){return Element.getMany(this,'getStyle',arguments);},walk:function(brother,start){brother+='Sibling';var el=(start)?this[start]:this[brother];while(el&&$type(el)!='element')el=el[brother];return $(el);},getPrevious:function(){return this.walk('previous');},getNext:function(){return this.walk('next');},getFirst:function(){return this.walk('next','firstChild');},getLast:function(){return this.walk('previous','lastChild');},getParent:function(){return $(this.parentNode);},getChildren:function(){return $$(this.childNodes);},hasChild:function(el){return!!$A(this.getElementsByTagName('*')).contains(el);},getProperty:function(property){var index=Element.Properties[property];if(index)return this[index];var flag=Element.PropertiesIFlag[property]||0;if(!window.ie||flag)return this.getAttribute(property,flag);var node=this.attributes[property];return(node)?node.nodeValue:null;},removeProperty:function(property){var index=Element.Properties[property];if(index)this[index]='';else this.removeAttribute(property);return this;},getProperties:function(){return Element.getMany(this,'getProperty',arguments);},setProperty:function(property,value){var index=Element.Properties[property];if(index){this[index]=value;}else{if(window.ie&&property=='style'){this.style.cssText=value;}else{this.setAttribute(property,value);}}
return this;},setProperties:function(source){return Element.setMany(this,'setProperty',source);},setHTML:function(){this.innerHTML=$A(arguments).join('');return this;},setText:function(text){var tag=this.getTag();if(['style','script'].contains(tag)){if(window.ie){if(tag=='style')this.styleSheet.cssText=text;else if(tag=='script')this.setProperty('text',text);return this;}else{this.removeChild(this.firstChild);return this.appendText(text);}}
this[$defined(this.innerText)?'innerText':'textContent']=text;return this;},getText:function(){var tag=this.getTag();if(['style','script'].contains(tag)){if(window.ie){if(tag=='style')return this.styleSheet.cssText;else if(tag=='script')return this.getProperty('text');}else{return this.innerHTML;}}
return($pick(this.innerText,this.textContent));},getTag:function(){return this.tagName.toLowerCase();},empty:function(){Garbage.trash(this.getElementsByTagName('*'));return this.setHTML('');}});Element.fixStyle=function(property,result,element){if($chk(parseInt(result)))return result;if(['height','width'].contains(property)){var values=(property=='width')?['left','right']:['top','bottom'];var size=0;values.each(function(value){size+=element.getStyle('border-'+value+'-width').toInt()+element.getStyle('padding-'+value).toInt();});return element['offset'+property.capitalize()]-size+'px';}else if(property.test(/border(.+)Width|margin|padding/)){return'0px';}
return result;};Element.Styles={'border':[],'padding':[],'margin':[]};['Top','Right','Bottom','Left'].each(function(direction){for(var style in Element.Styles)Element.Styles[style].push(style+direction);});Element.borderShort=['borderWidth','borderStyle','borderColor'];Element.getMany=function(el,method,keys){var result={};$each(keys,function(key){result[key]=el[method](key);});return result;};Element.setMany=function(el,method,pairs){for(var key in pairs)el[method](key,pairs[key]);return el;};Element.Properties=new Abstract({'class':'className','for':'htmlFor','colspan':'colSpan','rowspan':'rowSpan','accesskey':'accessKey','tabindex':'tabIndex','maxlength':'maxLength','readonly':'readOnly','frameborder':'frameBorder','value':'value','disabled':'disabled','checked':'checked','multiple':'multiple','selected':'selected'});Element.PropertiesIFlag={'href':2,'src':2};Element.Methods={Listeners:{addListener:function(type,fn){if(this.addEventListener)this.addEventListener(type,fn,false);else this.attachEvent('on'+type,fn);return this;},removeListener:function(type,fn){if(this.removeEventListener)this.removeEventListener(type,fn,false);else this.detachEvent('on'+type,fn);return this;}}};window.extend(Element.Methods.Listeners);document.extend(Element.Methods.Listeners);Element.extend(Element.Methods.Listeners);var Garbage={elements:[],collect:function(el){if(!el.$tmp){Garbage.elements.push(el);el.$tmp={'opacity':1};}
return el;},trash:function(elements){var len=elements.length-1;for(var i=len;i>=0;i--){free(elements[i]);elements[i]=null;}},empty:function(){free(document);free(window);if(!window.ie){delete document;delete window;}}};window.addListener('beforeunload',function(){window.addListener('unload',Garbage.empty);if(window.ie)window.addListener('unload',CollectGarbage);});