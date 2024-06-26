def authenticate(username, password):
    def calculateSI (prainciple, period, rate):
        result = (prainciple * period * rate) / 100
        return result
    
    if (username == "admin" and password == "pwd123"):
        print("SimpleInterrest",calculateSI(1000,1,6))
        return calculateSI

authenticate ("admin", "pwd123")

