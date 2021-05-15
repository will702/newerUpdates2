import os
import certifi
from gingerit.gingerit import GingerIt

os.environ['SSL_CERT_FILE'] = certifi.where()
def grammar(isi):
    res = GingerIt().parse(isi)

    print(res)
    return str(res['result'])