import  re
import  requests
from    bs4 import BeautifulSoup
import  parse
from    kavenegar import *


result = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

price = result.json()
check_price = price['bpi']['USD']['rate'] 
check_price = check_price.replace(',','')
if(float(check_price) < 35000):
    try:
        api = KavenegarAPI('4A4642384C5978537053396938315172544A4E69746D63632B397664456B77334563654353614B6B306D303D')
        params = {'sender': '1000596446','receptor': '09037682290','message': 'Tradi Coders Team \nBitCoin price is\n%s USD$ \nand it is time to buy'%(check_price)}
        response = api.sms_send(params)
        print(response)
        print('sent')
    except APIException as e: 
        print(e)
        print('error1')
    except HTTPException as e: 
        print(e)
        print('error2')
if(float(check_price) >= 50000):
    try:
        api = KavenegarAPI('4A4642384C5978537053396938315172544A4E69746D63632B397664456B77334563654353614B6B306D303D')
        params = {'sender': '1000596446','receptor': '09037682290','message': 'Tradi Coders Team \nBitCoin price is\n%s USD$ \nand it is time to sell'%(check_price)}
        response = api.sms_send(params)
        print(response)
        print('sent')
    except APIException as e: 
        print(e)
        print('error1')
    except HTTPException as e: 
        print(e)
        print('error2')
