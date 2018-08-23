import urllib2
import json
import base64
from Crypto.PublicKey import RSA
import farmware_tools as fwt

server = fwt.get_config_value("account_switcher", "server", str)
email = fwt.get_config_value("account_switcher", "email", str)

credentials_json = json.dumps({
    'password': fwt.get_config_value("account_switcher", "password", str),
    'email': email,
    'version': 1,
    'id': '_whatever'
})
key_url = server + "/api/public_key"
key_string = urllib2.urlopen(key_url).read()
public_key = RSA.importKey(key_string)
encrypted = public_key.encrypt(credentials_json, 32)[0]
secret = base64.b64encode(encrypted)

rpc = fwt.device.rpc_wrapper({
    'kind': 'change_ownership',
    'args': {},
    'body': [
        fwt.device.assemble_pair("secret", secret),
        fwt.device.assemble_pair("email", email),
        fwt.device.assemble_pair("server", server),
    ]
})

fwt.device.send_celery_script(json.dumps(rpc))
