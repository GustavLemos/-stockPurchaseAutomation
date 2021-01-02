class Produto():

    def __init__(self, idNumber, name, bruteValue, finalValue, productSolds):
        self.idNumber = idNumber
        self.name = name
        self.bruteValue = bruteValue
        self.finalValue = finalValue
        self.profit = finalValue - bruteValue
        self.productSolds = productSolds