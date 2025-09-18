import json

import requests
# import requests
import calculator as c



def lambda_handler(event, context):
    
    a,b,op=int(event["a"]),int(event["b"]),str(event["op"])
    result=None
    ops = {
    "+": c.add,
    "-": c.sub,
    "*": c.mul,
    "/": c.div,
    }
    
    func=ops.get(op)
    if func:
        result=func(a,b)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
            "result": f"{a} {op} {b} = {result}"
            
        }),
    }
