from typing import List

def calculate_richest(accounts: List[List[int]]) -> int:
    '''
    Time: O(n), Space: O(1)
    '''
    n_customers = len(accounts)
    # edge case
    if n_customers == 0:
        return 0
    
    ans = 0
    for customer in range(n_customers):
        customer_wealth = sum(accounts[customer])
        if customer_wealth > ans:
            ans = customer_wealth
    return ans


accounts = [[1, 2, 3], [3, 2, 1]]
print(calculate_richest(accounts))
accounts = [[1, 5], [7, 3], [3, 5]]
print(calculate_richest(accounts))
accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
print(calculate_richest(accounts))