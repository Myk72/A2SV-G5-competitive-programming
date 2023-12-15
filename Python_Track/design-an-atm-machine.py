class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.money_in_bank=[0]*5
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.money_in_bank[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawal=[0]*5
        right =4 # used for index iteration
        self.tmp_money=self.money_in_bank[:] # we need the copy due to modifying money_in_bank in case of request rejection [-1] is not applicable
        while right >= 0:
            if self.denominations[right] <= amount:
                withdrawal[right] = min(amount // self.denominations[right], self.tmp_money[right])
                self.tmp_money[right] -= withdrawal[right]
                amount -= withdrawal[right] * self.denominations[right]
            if amount==0:
                self.money_in_bank=self.tmp_money
                return withdrawal
            right -= 1
        return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)