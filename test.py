import requests, json, sys, re


url = "https://restapi.nftscan.com/api/v2/account/own/all/0x8de1c9025F0584054153338d2A0916477E4BAE62?erc_type=&show_attribute=false"
header={"X-API-KEY" : 'VnPYpXflXOIsqAqsPhtBEDub'}
response = requests.get(url,  headers=header)
res = response.json()['data']
for i in range(len(res)):
    assets = res[i]['assets']
    for asset in assets:
            print(f"you have the NFT {asset['name']} of the collection {asset['contract_name']} , the mint price was {asset['mint_price']}ETH")





