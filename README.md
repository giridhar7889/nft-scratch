# TokenURI

The tokenURI on an NFT is a unique identifier of what the token "looks" like. A URI could be an API call over HTTPS, an IPFS hash, or anything else unique.
These show what an NFT looks like, and its attributes. The image section points to another URI of what the NFT looks like. This makes it easy for NFT platforms like Opensea, Rarible, and Mintable to render NFTs on their platforms, since they are all looking for this metadata.

# IPFS

IPFS is a peer to peer network in a decentralised manner where we can store data

# \_safeMint(owner,Id)

owner->the one who initially hit that create collectible function
Id->the item id

# \_setTokenURI(item,tokenURI)

# smartcontract interaction
when ever you interact with a smartcontract on chain you need two things:-
->abi : abi defines the way to interact with a smartcontract
->interface:you need the network link_token address

# CURL
Curl is a command-line utility that allows users to create network requests. 
To make a basic POST request using curl, type the following command on your command-line:
curl -X POST https://example.com/
curl -X  POST -F file=@img/pug.png http://127.0.0.1:5000/api/v0/add returns {"Name":"pug.png","Hash":"QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8","Size":"5699"}

It means it got succesfully uploaded and gives us the hash

# /api/v0/add 
add the file or directory to ipfs