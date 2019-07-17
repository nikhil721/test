import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mac_address", help="Query a Mac Address ",
                    type=str)
args = parser.parse_args()


mac_address = args.mac_address
params = {
    'apiKey': 'at_kM8JCU2bTmFymZ9X2jdxgGqfRygWH',
    'output':  'json',
    'search': mac_address
}

mac_address_response = requests.get('https://api.macaddress.io/v1',params=params)
if mac_address_response.status_code == 200:
    lead_string = 'MAC Address'
    company_name = mac_address_response.json().get('vendorDetails').get('companyName')
    if mac_address == mac_address_response.json().get('vendorDetails').get('oui'):
        lead_string = 'OUI'
    print('The  {0}  {1} is associated with Company {2}'.format(lead_string,mac_address,company_name))

elif mac_address_response.status_code == 422:
    print('Invalid MAC or OUI address was received')
else:
    print(mac_address_response.text)



