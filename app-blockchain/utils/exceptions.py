from rest_framework.exceptions import APIException
from rest_framework import status


class CustomError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Having errors'
    default_code = 0

    def __init__(self, detail=None, code=None):
        super().__init__(detail=detail, code=code)
