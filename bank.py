class BankAccount:
  def __init__(self):
    self.balance = 0
    self.interest = .02
  
  def deposit(self, amount):
    if (amount < 0):
      return False
    self.balance += amount
    print(f"deposited {amount} into the account \n new balance is: {self.balance}")

  def withdraw(self, amount):
    if (amount < 0):
      return False
    self.balance -= amount
    print(f"withdrew {amount} from the account \n new balance is: {self.balance}")

  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.interest)
    print(f"accumulated interest on the account \n new balance is: {self.balance}")
    return self.balance


class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.interest = 0
  
  def accumulate_interest(self):
    self.balance = self.balance + 10
    print(f"accumulated interest on the account \n new balance is: {self.balance}")
    return self.balance


class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__()
    self.overdraft_penalty = 40
  
  def withdraw(self, amount):
    if (amount < 0):
      return False
    elif ((self.balance - amount) < 0):
      self.balance -= self.overdraft_penalty
      print(f"cannot withdraw that amount \n charged a fee of {self.overdraft_penalty} \n new balance is: {self.balance}")
      return False
    self.balance -= amount
  
  def accumulate_interest(self):
    if (self.balance < 0):
      self.interest = 0
    self.balance = self.balance + (self.balance * self.interest)
    print(f"no interest accumulated because the balance is: {self.balance}")


basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))

