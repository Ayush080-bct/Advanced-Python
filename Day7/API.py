import requests,json
response=requests.get("https://catfact.ninja/facts?limit=3")
data=response.json()
with open ("facts.json","w") as f:
    json.dump(data,f,indent=2)#2 spaces per level