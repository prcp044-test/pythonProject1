import requests

def api_request(url, method='GET', headers=None, params=None, data=None, json=None,auth=None):

    try:
        # Make the request based on the specified method
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers, params=params, auth=auth)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, params=params, data=data, json=json,auth=auth)
        else:
            raise ValueError("Unsupported HTTP method: {}".format(method))

        return response
    except requests.exceptions.HTTPError as err:
        print ( f"HTTP error occurred: {err}" )
    except Exception as e:
        print ( f"An error occurred: {e}" )
    return None

def validate_status_code(response, expected_status_code):
    if response.status_code == expected_status_code:
        print(response.status_code)
        return True
    else:
        print(f"Unexpected status code: {response.status_code}. Expected: {expected_status_code}.")
        return False

def validate_json_value(res_json, key, expected_value):

    # Value=res_json['json'][key]
    # print(expected_value)
    # print ( type(res_json['json'][key]) )
    # print ( type(expected_value) )

    if res_json['json'][key] == expected_value:
        print ( f"The value matching '{key}': {res_json['json'][key]}, expected: {expected_value}" )
        return True
    else:
        print(f"Unexpected value for '{key}': {res_json['json'][key]}, expected: {expected_value}")
        return False

def validate_json_delay_value(res_json, key, expected_value):

    Value=res_json[key]
    # print(expected_value)
    print (Value)
    # print ( type(expected_value) )

    if res_json[key] == expected_value:
        print ( f"The value matching '{key}': {res_json[key]}, expected: {expected_value}" )
        return True
    else:
        print ( f"Unexpected value for '{key}': {res_json[key]}, expected: {expected_value}" )
        return False

