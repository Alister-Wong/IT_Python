def percentTaxToDec(percentTax):
    return float(percentTax) / 100
def calcTax(salary, tax):
    return salary * tax

while True: 
    salary = raw_input("How much salary do you earn per year?: ")
    if not salary.isalpha():
        salary = float(salary)
        break
    else:
        print "Please insert numbers only"

while True:
    rawtax = raw_input("What percent is the tax?: ")
    if not rawtax.isalpha():
        rawtax = percentTaxToDec(rawtax)
        break
    else:
        print "Please insert numbers only"
    
print '$' + str(calcTax(salary, rawtax))
