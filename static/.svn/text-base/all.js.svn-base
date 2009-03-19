Meteora.uses("Control.Dialog");Meteora.uses("Control.Picbox");Meteora.uses('Control.Form');Meteora.uses('Control.Toolbox');Meteora.uses('Fx.Visual');function addComment(entrada_id){Meteora.overlay();addCommentDialog=new Dialog({url:'/zodycomments/add/'+entrada_id+'/'},{height:460,width:480,title:"add Comment",onClose:function(){Meteora.removeOverlay();}});addCommentDialog.center();}
function showComments(entrada_id){$('show_comments').toggle();$('showComments').setContent({url:"/zodycomments/show/"+entrada_id+'/'});$('showComments').toggle();$('commentForm').toggle();}
function hideComments(){$('show_comments').toggle();$('showComments').toggle();$('commentForm').toggle();}
var tbox=false
function showLinks(el){if(tbox==false){options={autoClose:true,autoMove:false,enableDrag:false}
tbox=new Toolbox(Widget.div({'class':'showlinks','id':'showlinks'},''),options);var pos=el.getPosition();tbox.moveTo(pos.y,pos.x+25);$('showlinks').setContent({url:'/links'});}
tbox.show();}
function closeLinks(){tbox.hide();}