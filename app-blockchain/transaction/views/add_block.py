from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from chain_peers import Block, get_blockchain
from utils.exceptions import CustomError


class AddBlock(GenericAPIView):
    def post(self, request):
        block_data = request.data
        block = Block(block_data["index"],
                      block_data["transactions"],
                      block_data["timestamp"],
                      block_data["previous_hash"],
                      block_data["nonce"])
        proof = block_data['hash']
        blockchain = get_blockchain()
        check_added = blockchain.add_block(block, proof)

        if not check_added:
            raise CustomError()

        return Response(None, status=status.HTTP_200_OK)
