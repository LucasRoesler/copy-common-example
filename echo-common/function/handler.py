import json
import logging

lookup = {}
with open("./common/lookup_dict.json") as f:
    lookup = json.load(f)

def handle(event, context):
    payload = str(event.body, 'utf-8')

    logging.debug("looking for: "+payload)
    logging.debug("in"+ json.dumps(lookup))
    return {
        "statusCode": 200,
        "body": lookup.get(payload, "no found")
    }
