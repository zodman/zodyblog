function addMessage(text, extra_tags) {
    var icon ="";
    if(extra_tags =="error"){
        icon = "alert"
    } else {
        icon = "info"
    }
    var message = $('<li class="'+extra_tags+'"> <span class=" ui-icon ui-icon-'+icon+' float-left"></span>'+text+'</li>');
    $("#messages").append(message);
    $("#messages:hidden").show("blind",{},500,function (){
        setTimeout(function (){
                 $("#messages:visible").hide("blind");
        }, 3000);         
    });
}

function catchMessages() {

        $('#messages').ajaxComplete(function(e, xhr, settings) {
            var contentType = xhr.getResponseHeader("Content-Type");
            if (contentType == "application/javascript" || contentType == "application/json") {
                var json = $.evalJSON(xhr.responseText);
                    $("#messages:hidden").find("li").remove();
                $.each(
                json.django_messages, function (i, item) {
                    addMessage(item.message, item.extra_tags);
                });
            }
         }).ajaxError(function(e, xhr, settings, exception) {
                    $("#messages:hidden").find("li").remove();
            addMessage("There was an error processing your request, please try again.", "error");
        }).hide();

}

function processForm() {

$("#formcontacto").ajaxForm(
            {
                dataType:"json", 
                success:function(json){
                    $(".error").remove();
                    if(!json.success){
                        $.each(json.error, function( key,data){
                                $(data).each(function( pos ) {   
                                    $("#id_" + key).after("<span class='error'> * " +data[pos] +"</span>");
                                });                                
                            });
                    }
                }
            }
        );

}
