from brownie import AdvancedCollectible
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    advancedcollectible=AdvancedCollectible[len(AdvancedCollectible)-1]
    fund_advanced_collectible(advancedcollectible)
