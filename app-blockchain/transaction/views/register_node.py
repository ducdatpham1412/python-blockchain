from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from chain_peers import get_blockchain, get_peers
from utils import services
from utils.exceptions import CustomError


class RegisterNode(GenericAPIView):
    def post(self, request):
        node_address = services.get_object(request.data, 'node_address')
        if not node_address:
            raise CustomError()

        blockchain = get_blockchain()
        peers = get_peers()

        peers.add(node_address)

        chain = []
        for block in blockchain.chain:
            chain.append(block.__dict__)

        res = {
            'length': len(chain),
            'chain': chain,
            'peers': list(peers)
        }

        return Response(res, status=status.HTTP_200_OK)
