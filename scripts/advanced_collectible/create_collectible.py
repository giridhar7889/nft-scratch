from brownie import AdvancedCollectible,accounts,config
from scripts.helpful_scripts import get_breed
import time

STATIC_SEED=122
def main():
    dev=accounts.add(config['wallets']['from_key'])
    advanced_collectible=AdvancedCollectible[len(AdvancedCollectible)-1]
    transaction=advanced_collectible.createCollectible("None",{"from":dev})
    transaction.wait(1)
    time.sleep(35)
    requestId=transaction.events["requestedCollectible"]["requestId"]
    tokenId=advanced_collectible.requestIdToTokenId(requestId)
    breed=get_breed(advanced_collectible.tokenIdToBreed(tokenId))
    print('Dog breed of tokenId {} is {}'.format(tokenId,breed))

#0x4c71b02e6B962c49e9B5DC60B936dD8D1FaADA0C
