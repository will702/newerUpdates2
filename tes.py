
import json
import requests

import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()

def check_resi(expedition, resi):
    url = "https://pluginongkoskirim.com/cek-tarif-ongkir/front/resi-amp"
    data = {"kurir": expedition, "resi": resi}
    try:
        response = requests.post(url, data=data)
        result = json.loads(response.text)

        return result
    except Exception as e:
        return {
            "error": True,
            "message": "{}".format(e)
        }
# a = (check_resi("jnt","JP8247782781"))
# print(a['data'])
# print(a['data']['detail']['status'])
# print(a['data']['detail']['date_shipment'])
# print(a['data']['detail']['date_received'])
# print(a['data']['detail']['receiver'])
# for i in a['data']['detail']['history']:
#     print(i)