from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import _get_queryset 

class Meteora:
    """ 
        Meteora lib for django
    """
    def __init__(self, success = None, message = None ):
        self.message = {}
        self.execute_js= []
        if success is None and message is None:
            return 

        if success is False:
            self.message["errorMessage"]= message
            if self.message.has_key("successMessage"):
                del self.message["successMessage"]
        else:
            self.message["successMessage"]= message
            if self.message.has_key("errorMessage"):
                del self.message["errorMessage"]
 

    def bubble(self, id, message ):
        self.execute(" var b = new Bubble('%s','%s'); b.show(); " % ( id, message) )

    def json_response(self):
        return HttpResponse(simplejson.dumps(self.message), mimetype="text/plain")
        
    def more_execute(self, execute):
        self.execute_js.append(execute)

    def execute(self, execute = False ):
        if execute:
            self.execute_js.append(execute)
        if "execute" in self.message:
            self.message["execute"] += "".join(self.execute_js).replace("\n",'')
        else:
            self.message["execute"] = "".join(self.execute_js).replace("\n",'')
        self.execute_js = []

    def form_invalid(self, table_id, form ):
        """ 
            For show datas on form ...... FF only.
            <table id="table_id">
                 {{ form }}
            </table>

        """
        self.execute("$('%s').innerHTML='%s'" % ( table_id, form.as_table() ) )
    #Notebooks def
    # ttp://meteora.astrata.com.mx/pages/documentation/control-notebook
    def notebook_close_page(self, notebook, id ):
        """close a page from a notebook """
        self.execute_js.append(" var nb = document.%s; nb.closePage('%s');" % ( notebook, id ) )
        self.execute()
    def notebook_select_page(self, notebook, id ):
        """ select a page from a notebook """
        self.execute_js.append(" var nb = document.%s; nb.selectPage('%s');" % (notebook,id) )
        self.execute()
    
    # jsonRpc Core  defs
    # http://meteora.astrata.com.mx/pages/documentation/core-jsonrpc
    def redirectTo(self, url ):
        self.message["redirectTo"] = url

    def update_object(self, object_id, view):
        self.message['updateObject'] = {'objectId': object_id, 'data' : view}
        
    def update_object_url(self, object_id, url ):
        self.message['updateObject'] = {'objectId': object_id, 'dataSource' : url}   
        
    def delete_object(self, object_id):
        self.message['deleteObject'] = object_id
       
    def error_message(self, string):
        self.message['errorMessage'] = string
       
    def hide_object(self, object_id):
        self.message['hideObject'] = object_id
        
    def show_object(self, object_id):
        self.message['showObject'] = object_id

class MeteoraError(Exception):
    pass


def json( convert ):
    return HttpResponse(simplejson.dumps(convert), mimetype="text/plain")

def get_object_or_404(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs), True
    except queryset.model.DoesNotExist:
        m = Meteora(False,"No %s not matches the given query." % queryset.model._meta.object_name)
        return m.json_response(), False
