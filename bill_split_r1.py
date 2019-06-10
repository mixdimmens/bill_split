import time
from decimal import Decimal as ds

class Transaction:
    init_swtch = False
    pay_switch = False
    ledger = []
    paid_off = []
    def __init__(self, transaction_name, ammount, debtors):
        self.transaction_name = transaction_name
        self.ammount = ammount
        self.debtors = debtors
        self.traaction_date = time.strftime("%m/%d/%y, %H:%M")

    def date_marker(self):
        return time.strftime("%m/%d/%y, %H:%M")
    
    def split_qty(self):
        try:
            return len(self.debtors)
        except TypeError:
            print('debtors not a list')
    
    def split_val(self):
        return self.ammount / self.split_qty()

    def splt (self):
        # self.ledger = []
        for debtor in self.debtors:
            self.ledger.append([debtor, self.split_val()])
        return self.ledger
    
    def find_debtor_index(self, debtor):
        debtor_index = 0
        for i in range(len(self.ledger)):
            if self.ledger[i][0] == debtor:
                debtor_index = i
                print('check it: {}'.format(self.ledger[i][0]))
        return debtor_index

    def paid(self, debtor):
        try:
            if len(self.ledger) == 0:
                pass
            elif len(self.ledger) > 0:
                self.ledger.pop(self.find_debtor_index(debtor))
            else:
                print('something else is')
            # self.debtors.remove(debtor)
        except ValueError:
            print('some shit is off!')

    def paid_in(self, debtor, ammount):
        # try:
        print(debtor)
        debtor_index = 0
        if len(self.ledger) == 0:
            pass
        else:
            self.ledger[debtor_index][1] = self.ledger[self.find_debtor_index(debtor)][1] - ammount
            self.pay_switch = True
        # except:
        #     print('"paid_in" not working out')
    
    def __repr__(self):
        # self.splt()
        if self.init_swtch == False:
            out_str = str([self.transaction_name, self.traaction_date, self.splt()])
            self.init_swtch = True
        elif len(self.ledger) == 0:
            out_str = "everyone's paid off!"  
        elif self.pay_switch == True:
            out_str = str([self.transaction_name, self.traaction_date, self.ledger])
        # elif self.init_swtch == False:
            # out_str = str([self.transaction_name, self.traaction_date, self.splt()])
            # out_str = str([self.transaction_name, self.traaction_date, self.ledger])
            # out_str = str(self.splt())
            # self.init_swtch = True
        return out_str



testy = Transaction('test', 27, ['a', 'b', 'c'])
print(testy)

testy.paid_in('b', 2)
print(testy)

testy.paid('a')
print(testy)
testy.paid('b')
print(testy)
testy.paid('c')
print(testy)

# testy.date_marker()