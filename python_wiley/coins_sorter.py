def select_coins(coins_list, desired_amount):
    coins_list.sort(reverse=True)  # Sort coins in descending order

    def find_combination(remaining_amount, coins_index):
        if remaining_amount == 0:
            return []
        if coins_index >= len(coins_list) or remaining_amount < coins_list[coins_index]:
            return None

        coin = coins_list[coins_index]
        with_coin = find_combination(remaining_amount - coin, coins_index)
        if with_coin is not None:
            return [coin] + with_coin
        return find_combination(remaining_amount, coins_index + 1)

    selected_coins = find_combination(desired_amount, 0)

    return selected_coins if selected_coins is not None else "Cannot achieve the desired amount with the given coins."

# Example usage:
coins = [25, 10, 5, 1]  # List of coins
desired_amount = 37  # Desired amount to achieve
selected_coins = select_coins(coins, desired_amount)
print("Selected Coins:", selected_coins)
