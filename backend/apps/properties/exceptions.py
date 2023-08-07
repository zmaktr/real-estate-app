from rest_framework.exceptions import APIException

class ProperyNotFound(APIException):
    status_code = 404
    default_detail = 'The requested property does not exist'