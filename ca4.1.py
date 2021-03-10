import sys
sys.setrecursionlimit (10**5)
class Price:
    def __init__(self,amount):
        self.amount = amount
                
class City:
    def __init__(self,pis):
        self.pis = pis
        self.prices = []
        self.set_prices()
        
    def set_prices(self):
        for price in self.pis:
            new_price = Price(price)
            self.prices.append(new_price)

class Travel:
    def __init__(self,n,m):
        self.spent_money = 0
        self.cities = []
        self.num_of_cities = n
        self.budget = m
        self.done = False
        self.answer = 0
        
    def add_city(self,prices):
        prices.sort()
        prices.reverse()
        new_city = City(prices)
        self.cities.append(new_city)

    def calc_max_spent(self,city_id):
        if self.done == True:
            return
        if city_id == self.num_of_cities-1:
            for price in self.cities[city_id].prices:
                if self.spent_money + price.amount == self.budget:
                    self.answer = self.budget
                    self.done = True
                    return
                elif self.spent_money + price.amount < self.budget:
                    if self.spent_money + price.amount > self.answer:
                        self.answer = self.spent_money + price.amount
                        
            return  

        for price in self.cities[city_id].prices:
            if self.done == True:
                return
            self.spent_money += price.amount
            self.calc_max_spent(city_id + 1)
            self.spent_money -= price.amount
        return

t = int(input())
for i in range(t):
    m_n = [int(x) for x in input().strip().split()]
    m = m_n[0]
    n = m_n[1]
    
    Pis = [int(x) for x in input().strip().split()]
    travel = Travel(n,m)
    for i in range(n):
        prices = [int(x) for x in input().strip().split()]
        travel.add_city(prices)
    travel.calc_max_spent(0)
    print(travel.answer)
