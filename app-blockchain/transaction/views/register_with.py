from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from utils import services
from utils.exceptions import CustomError
import requests
import json
from chain_peers import get_blockchain, get_peers, Block


class RegisterWith(GenericAPIView):
    def post(self, request):
        node_address = services.get_object(request.data, 'node_address')
        if not node_address:
            raise CustomError()

        try:
            res = requests.post(
                url='{}/register-node'.format(node_address),
                data=json.dumps({
                    'node_address': request.get_host(),
                }),
                headers={
                    'Content-Type': "application/json"
                }
            )
            res = res.json()

            blockchain = get_blockchain()
            peers = get_peers()

            # Update chain
            for idx, block_data in enumerate(res['chain']):
                if idx == 0:
                    continue  # skip genesis block
                block = Block(block_data["index"],
                              block_data["transactions"],
                              block_data["timestamp"],
                              block_data["previous_hash"],
                              block_data["nonce"])
                proof = block_data['hash']
                added = blockchain.add_block(block, proof)
                if not added:
                    raise CustomError("The chain dump is tampered!!")

            # Update peers
            peers.update(res['peers'])

            return Response(None, status=status.HTTP_200_OK)
        except:
            raise CustomError()
