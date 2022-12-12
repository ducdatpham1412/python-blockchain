from django.urls.conf import path
from transaction.views import new_transaction, get_chains, mine, register_with, register_node, add_block


urlpatterns = [
    path('new-transaction', new_transaction.NewTransaction.as_view()),
    path('get-blocks-peers', get_chains.GetChains.as_view()),
    path('mine', mine.Mine.as_view()),
    # for register new host
    path('register-with', register_with.RegisterWith.as_view()),
    path('register-node', register_node.RegisterNode.as_view()),
    path('add-block', add_block.AddBlock.as_view())
]
