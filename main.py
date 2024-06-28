def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    number = 0
    while True:
        try: 
            number = int(input('Enter a number  '))
            if number > 0 and number < 100:
                break
            else: 
                print ('Enter a correct number')
        except ValueError:
            print ('Only enter a number')
            

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
