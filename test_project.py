from project import guesses_reduce, bigger_or_smaller, win_check, play_again

def test_guesses_reduce():
    assert guesses_reduce(10) == "You have 9 chances to guess the correct number or you lose."
    assert guesses_reduce(7) == "You have 6 chances to guess the correct number or you lose."
    assert guesses_reduce(5) == "You have 4 chances to guess the correct number or you lose."


def test_bigger_or_smaller():
    assert bigger_or_smaller(44, 50) == "The secret number is bigger than 44."
    assert bigger_or_smaller(44, 25) == "The secret number is smaller than 44."
    assert bigger_or_smaller(20, 99) == "The secret number is bigger than 20."

def test_win_check():
    assert win_check(30, 45) == False
    assert win_check(50, 50) == None # print statement returns as none







