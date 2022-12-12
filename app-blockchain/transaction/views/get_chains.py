from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from chain_peers import get_blockchain, get_peers


class GetChains(GenericAPIView):
    def get(self, request):
        chain = []
        blockchain = get_blockchain()
        peers = get_peers()

        for block in blockchain.chain:
            chain.append(block.__dict__)

        res = {
            'length': len(chain),
            'chain': chain,
            'peers': list(peers)
        }

        return Response(res, status=status.HTTP_200_OK)
