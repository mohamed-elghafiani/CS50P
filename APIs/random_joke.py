import requests

# data = {
#     "user_input": "fdghjkw",
#     "request": "dghjwkl"
# }

res = requests.post("https://official-joke-api.appspot.com/random_joke").json()

print("setup: ", res["setup"])
print("punchline: ", res["punchline"])
