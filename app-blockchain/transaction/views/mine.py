from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from chain_peers import get_blockchain, consensus, get_peers
from utils.exceptions import CustomError
import requests
import json


class Mine(GenericAPIView):
    def get(self, request):
        blockchain = get_blockchain()
        peers = get_peers()

        check_having_unconfirmed_tx = blockchain.mine()
        if not check_having_unconfirmed_tx:
            raise CustomError()

        chain_length = len(blockchain.chain)
        consensus()
        if chain_length == len(blockchain.chain):
            last_block = blockchain.last_block
            for peer in peers:
                url = '{}/add-block'.format(peer)
                requests.post(
                    url,
                    data=json.dumps(last_block.__dict__, sort_keys=True),
                    headers={
                        'Content-Type': "application/json"
                    },
                )

        res = {
            'success': True,
            'last_block_index': blockchain.last_block.index,
        }

        return Response(res, status=status.HTTP_200_OK)
