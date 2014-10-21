"""Build a file with sample data that can be loaded into database.

After having run this script, a database can be built using the sample data
with the command

`./manage.py loaddata sample.json

"""

import json
import requests

# Fetch sample data from url.
sample_url = "http://www.unisport.dk/api/sample/"
response = requests.get(sample_url)
initial_products = json.loads(response.text)['latest']

# Format the data in the way loaddata expects.
result = []
for product in initial_products:
    new = {}
    new['model'] = 'products.Product'
    new['pk'] = product['id']
    new['fields'] = product
    del new['fields']['id']

    # Convert the fields to the correct types.
    fields = new['fields']
    fields['free_porto'] = fields['free_porto'] == "True"

    # Decimal expects dot-decimal notation, not comma as used in Denmark.
    fields['price'] = fields['price'].replace(",", ".")
    fields['price_old'] = fields['price_old'].replace(",", ".")

    result.append(new)

# Store the results in a file so we can import the data.
with open('sample.json', 'wb') as outfile:
    outfile.write(json.dumps(result))
