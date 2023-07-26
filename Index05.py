def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=len(s)
    i=0
    c=0
    while i<a:
        if s[i].isdigit()==1:
            c+=1
        i+=1
    return c
print(main("14o5j"))