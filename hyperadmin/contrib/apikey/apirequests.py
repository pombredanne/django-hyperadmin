from hyperadmin.apirequests import HTTPAPIRequest

from hyperadmin.contrib.apikey.common import authenticate

HTTP_HEADER = 'API_KEY'
GET_VARIABLE = '_API_KEY'

class APIKeyMixin(object):
    def populate_session_data_from_request(self, request):
        data = super(APIKeyMixin, self).populate_session_data_from_request(request)
        if HTTP_HEADER in request.META:
            key = request.META[HTTP_HEADER]
            user = authenticate(key)
            if user:
                data['user'] = user
        if GET_VARIABLE in request.GET:
            key = request.GET[HTTP_HEADER]
            user = authenticate(key)
            if user:
                data['user'] = user
        return data

class HTTPAPIKeyRequest(APIKeyMixin, HTTPAPIRequest):
    pass

