from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from chain_peers import get_blockchain
from utils import services
from utils.exceptions import CustomError


class NewTransaction(GenericAPIView):
    def post(self, request):
        request_data = request.data

        content = services.get_object(request_data, 'content')
        creator = services.get_object(request_data, 'creator')
        if not content or not creator:
            raise CustomError()

        transaction_data = {
            'content': request_data['content'],
            'creator': request_data['creator'],
            'created': str(datetime.now())
        }

        blockchain = get_blockchain()
        blockchain.add_new_transaction(transaction_data)

        return Response(None, status=status.HTTP_200_OK)
