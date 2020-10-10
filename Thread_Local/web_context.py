import threading

class WebContext(object):
    thread_space = threading.local()

    @staticmethod
    def get_web_request():
        try:
            return WebContext.thread_space.__getattribute__('web_request')
        except:
            return None

    @staticmethod
    def set_web_request(web_service_request):
        WebContext.thread_space.__setattr__("web_request", web_service_request)
    
    @staticmethod
    def get_web_response():
        try:
            return WebContext.thread_space.__getattribute__('web_response')
        except:
            return None

    @staticmethod
    def set_web_response(web_service_response):
        WebContext.thread_space.__setattr__("web_response", web_service_response + str(threading.currentThread().getName()))

    @staticmethod
    def clear_context():
        try:
            WebContext.thread_space.__delattr__("web_response")
            WebContext.thread_space.__delattr__("web_request")
        except:
            pass

    