# This is a kind of interface to the Gentle library to allow
# it to run with Lambda. The idea is for post requests via the
# AWS API to be handled here and subsequently call the required
# functions in the Gentle library.

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    #print("value1 = " + event['key1'])
    #print("value2 = " + event['key2'])
    #print("value3 = " + event['key3'])
    return "Hey hey there! Welcome to Gentle on Lambda"