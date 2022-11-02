
import os


# Cloud related variables
API_KEY = "LJWRUXHIT3A7W7WK" #os.getenv('API_KEY',None)
API_SECRET_KEY = "/eiKZ9dg/Hmi8miCthBm9JmjPoE2aTlkR9RpbadQUvy1M5VJgaWOFBOuiUkvwbNq" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

# Authentication related variables
#SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
#SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

# Schema related variables
ENDPOINT_SCHEMA_URL  = "https://psrc-7q7vj.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)
SCHEMA_REGISTRY_API_KEY = "WLBOXE4ULPKBL474" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "1AzZCC9txJmQ6qaGtrAQph2NGcb88TQ0NKjilNIxBOqJVA95I8WWM9/JuulrOsYT" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    #print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

