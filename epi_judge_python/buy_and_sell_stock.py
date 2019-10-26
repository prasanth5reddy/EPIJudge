from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # Time complexity : O(n)
    # Space complexity : O(1)
    min_price, max_profit = float('inf'), float('-inf')
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

    # # DP solution using Kadane's algorithm of finding maximum subarray
    # # find maximum subarray of
    # # Time complexity : O(n)
    # # Space complexity : O(1)
    # max_cur, max_so_far = 0, 0
    # for i in range(1, len(prices)):
    #     max_cur = max(0, max_cur + prices[i] - prices[i - 1])
    #     max_so_far = max(max_cur, max_so_far)
    # return max_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
