import http.client

"""
class rajaongkirApi
"""
import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()
class rajaongkirApi:

    def __init__(self, key=False, accountType=False):
        self.key = key
        self.accountType = accountType
        self.conn = http.client.HTTPSConnection("api.rajaongkir.com")
        self.headers = {
            'key': self.key,
            'content-type': "application/x-www-form-urlencoded"
        }

    """
    rajaongkirApi.requestApi
    Get detail of requestApi.
    @param   null|String    province    provinceID
    @param   null|String    city        cityID
    @param   null|String    origin      cityID
    @param   null|String    destination cityID
    @param   null|int       weight      gram
    @param   null|String    courier     jne/pos/tiki
    #Mendapatkan list seluruh propinsi
    rajaongkirApi.requestApi(province="")

    #Mendapatkan list seluruh kota
    rajaongkirApi.requestApi(city="")
    #Mendapatkan list seluruh kota pada satu provinsi
    rajaongkirApi.requestApi(city="", province="5")
    #Mendapatkan list satu kota pada satu provinsi
    rajaongkirApi.requestApi(city="419", province="5")
    #Mendapatkan list cost
    rajaongkirApi.requestApi(origin="501", destination="114", weight="1700", courier="jne")
    """

    def requestApi(self, province=False, city=False, origin=False, destination=False, weight=False, courier=False):
        try:
            url = ""
            payload = ""
            if origin is not False and destination is not False and weight is not False and courier is not False:
                url = "cost"
                payload = "origin={}&destination={}&weight={}&courier={}".format(origin, destination, weight, courier)
            elif city is False and province is not None:
                url = "province?id={}".format(province)
            elif province is False and city is not None:
                url = "city?id={}".format(city)
            elif province != "" and city is not None:
                url = "city?id={}&province={}".format(city, province)

            print("/{}/{}".format(self.accountType, url))
            if payload != "":
                self.conn.request("POST", "/starter/cost", payload, self.headers)
            else:
                self.conn.request("GET", "/{}/{}".format(self.accountType, url), headers=self.headers)

            res = self.conn.getresponse()
            data = res.read()
            return data
        except Exception as e:
            print(str(e))
            return {"status": {"code": 500, "description": "Internal Server Error"}}
