# Django blockchain app

This project is a demo blockchain network include two node: node-1 & node-2, written by Django Rest Framework.

# I/ Api includes:

All api are declared in app "transaction": app-blockchain/transaction/views
Includes theses:

1. transaction/new-transaction: Add transaction to blockchain, but it's added to unconfirmed transactions.
2. transaction/get-blocks-peers: Get list blocks of chain and add peers (node-1 & node-2 in this situation, you can add more).
3. transaction/mine: This api to mine the blockchain network, first it creates a new block includes all unconfirmed transactions we have added in api(1), then checks the proof of work of this block, if it's valid, a new block will be added to the chain.
4. transaction/register-with & transaction/register-node: Register a new node to the peers of this blockchain network, so it can fetch all transaction and list blocks like previous nodes.
5. transaction/add-block: Add a new block to the chain, of course this api is called after api mining and verify proof of work successfully.

# II/ Running and test

In order to run this project, you only need docker installed in your devices, all others like python 3.9, pip and python packages, docker will do this for you.

Running by these steps:

1. Run terminal: docker-compose build
2. Run terminal: docker-compose up
3. Open file front-end/transaction.html and live it on your localhost
4. You can test by enter input to input field and click "Add transaction" to call api new-transaction, then press button "Mine" to mine the blockchain, finally, click "Fetch" button and you will the list blocks is updated via api get-blocks-peers
