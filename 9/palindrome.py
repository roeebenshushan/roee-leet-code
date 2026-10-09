
def get_digit_num(x: int) -> int:
    digits_num = 1

    while x / 10 ** digits_num >= 1:
        digits_num = digits_num + 1

    return digits_num

def get_digit(x: int, index: int) -> int:
    return int(
        (
            x % 10 ** (index + 1) 
            - 
            x % 10 ** index
        ) 
        / 
        10 ** index
    )   

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    digits_num = get_digit_num(x)

    for index in range(digits_num):
        inverted_index = digits_num - index - 1

        if get_digit(x, index) != get_digit(x, inverted_index):
            return False

    return True