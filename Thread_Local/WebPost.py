from web_context import WebContext

class Sample(object):
    def perform(self):
        print("Request from " + WebContext.get_web_request())
        WebContext.set_web_response("Response for")