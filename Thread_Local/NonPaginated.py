from web_context import WebContext
import threading

class NonPaginated(object):
    def per(self, obj):
        WebContext.set_web_request(str(threading.currentThread().getName()))
        obj.perform()
        print(WebContext.get_web_response())
        WebContext.clear_context()