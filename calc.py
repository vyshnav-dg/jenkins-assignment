def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

def handler(event, context):
    print(add(5,10))
    print(subtract(5,10))
    print(multiply(5,10))
    print(divide(5,10))
    return {"statusCode": 200}