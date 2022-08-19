a = input("Yes or no?")
if(a=='y'):
    import requests as re
    from eitaa import Eitaa
    obj = Eitaa("bot56953:e73da9dd-de29-4135-a1e7-41bb8c22f4f9")
    url =  "http://api.navasan.tech/latest/?api_key=freebmyds9rdtma0gguvaNtEMQjDHgIS"
    r = re.get(url)
    dp = r.json()["usd_buy"]["value"]
    up = r.json()["eur_pp"]["value"]
    print(obj.send_message("8178087",'''The dollar price is %s
The euro price is %s'''%(dp,up),pin = 0))
