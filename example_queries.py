import requests
from decouple import config

exposed_url = str(config.EXPOSED_URL)

query_url = exposed_url + ":9200/blog/user/dilbert" + "?pretty=true"

## TODO: automate the annoying query syntax w/ the elasticsearch python package

print(response)

# curl that works. for more complex ones u gotta escape "s on windeez
# curl -XGET "EXPOSED_URL:9200/blog/user/dilbert?pretty=true"
