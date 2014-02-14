"""
runscope_adapter.py
~~~~~~~~~~

Contains an implementation of an HTTP adapter for Requests that automatically
creates Runscope URLs for requests.
"""
import urlparse
from requests.adapters import HTTPAdapter

class RunscopeAdapter(HTTPAdapter):
    """
    A Runscope-aware Transport Adapter for Python Requests. The central
    portion of the API.

    :param bucket_key: The Runscope bucket key to use for this request.
    """

    bucket_key = ""
    auth_token = None

    def __init__(self, bucket_key, auth_token=None, **kwargs):
        self.bucket_key = bucket_key
        self.auth_token = auth_token
        super(RunscopeAdapter, self).__init__(**kwargs)


    def send(self, request, **kwargs):
        """
        Sends a PreparedRequest object.

        :param request: The Requests :class:`PreparedRequest <PreparedRequest>` object to send.
        """

        request.url, port = self.proxify(request.url, self.bucket_key)
        if port:
            request.headers["Runscope-Request-Port"] = port

        if self.auth_token:
            request.headers["Runscope-Bucket-Auth"] = self.auth_token

        return super(RunscopeAdapter, self).send(request, **kwargs)


    def build_response(self, request, response):
        """
        Builds a Response object from a urllib3 response. 

        :param request: The Requests :class:`PreparedRequest <PreparedRequest>` object sent.
        :param response: The urllib3 response.
        """
        resp = super(RunscopeAdapter, self).build_response(request, response)
        return resp


    def proxify(self, original_url, bucket_key, gateway_host="runscope.net"):
        """
        Take a raw url string and turn it into a valid Runscope URL.
        
        Before:
            http://foo.example.com/path
        After:
            http://foo-example-com-bucket_key.<gateway_host>/path
        """

        parts = urlparse.urlsplit(original_url)

        # prevent double proxifying (e.g. when handling rewritten redirect locations)
        if gateway_host in original_url:
            return original_url, port if parts.port else None

        clean_host = parts.hostname.replace("-", "~").replace(".", "-")
        new_host = "{0}-{1}.{2}".format(clean_host, bucket_key, gateway_host).replace("~", "--")

        if parts.username or parts.password:
            new_host = "{0}:{1}@{2}".format(parts.username, parts.password, new_host)

        port = None
        if parts.port:
            port = parts.port

        return urlparse.urlunsplit((parts.scheme, new_host, parts.path, parts.query, parts.fragment)), port
