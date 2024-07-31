from Scripts.common_methods import *
import requests
import json
from utilities.config import *
from utilities.payload import *
from requests.auth import *

class Api():

# Send /get request and validate response code

    header={
        'accept': 'application / json'
    }
    # url = get_config ()['API']['endpoint']
    #
    # response=api_request(url,"GET")
    # print(response.json())
    # validate_status_code(response,200)

# Send /post request with json body and validate response contains relevant data
#     print(get_payload("prash@co.com","Prashanth",9620121212),"--------------")

    # url = get_config ()['API']['endpoint-post']
    #
    # response = api_request ( url, "POST",headers=header,json=get_payload("prash@co.com","Prashanth",9620414242))
    # res_json=response.json ()
    # # print(res_json)
    # validate_status_code ( response, 200 )
    # validate_json_value(res_json,'custemail','prash@co.com')
    # validate_json_value ( res_json, "custname", "Prashanth" )
    # validate_json_value ( res_json, "custtel", 9620414242)

#Validate request with delayed response /delay/{delay_time}


    # url = get_config ()['API']['endpoint-delay']
    #
    # response = api_request ( url, "GET")
    # res_json=response.json ()
    # # print(res_json)
    # validate_status_code ( response, 200 )
    # validate_json_delay_value(res_json,"url","https://httpbin.org/delay/5")

#Simulate Unauthorized Access

    # url = get_config ()['API']['endpoint-auth']
    # username = get_config ()['credentials']['UserName']
    # password = get_config ()['credentials']['Password']
    # response = api_request (url, "GET",auth=(username,password))
    # validate_status_code ( response, 401 )

#Write any negative scenario (invalid URL)

    url = get_config ()['API']['endpoint-auth-neg']
    response = api_request ( url, "GET")
    validate_status_code ( response, 401 )



















