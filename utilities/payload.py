def get_payload(custemail, custname, phone):
    body = {
        "comments": "",
        "custemail": custemail,
        "custname": custname,
        "custtel": phone,
        "delivery": "",
        "size": "small",
        "topping": "bacon"

    }
    return body
