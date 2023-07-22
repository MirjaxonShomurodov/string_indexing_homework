def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a1=s%10
    s//=10

    a2=s%10
    s//=10

    a3=s%10
    s//=10

    a4=s%10
    s//10

    a5=s%10
    s//=10

    a6=s
    m=a1+a2+a3+a4+a5+a6
    s=int("10920")
    return m
print(main(int("10920")))

   
   