class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richestCustomerWealth = 0
        for currentCustomer in accounts:
            currentCustomerWealth = 0
            for currentBankBalance in currentCustomer:
                currentCustomerWealth += currentBankBalance
            if currentCustomerWealth > richestCustomerWealth:
                richestCustomerWealth = currentCustomerWealth
        return richestCustomerWealth
