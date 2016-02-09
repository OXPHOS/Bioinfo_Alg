'''
 Input: An integer money and an array Coins = (coin1, ..., coind).
 Output: The minimum number of coins with denominations Coins that changes money.
'''


def DPChange(money, coins):
    MinNumCoins = [0]
    for m in range(1, money + 1):
        MinNumCoins.append(money)
        for coin in coins:
            if (m >= coin) and (MinNumCoins[m - coin] + 1 <= MinNumCoins[m]):
                MinNumCoins[m] = MinNumCoins[m - coin] + 1
    return MinNumCoins[money]
    

coins = [50,25,20,10,5,1]
print DPChange(40, coins)