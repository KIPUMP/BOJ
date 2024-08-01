def count369(number) :
    count = 0
    while number > 0 :
        digit = number % 10 
        if digit == 3 or digit == 6 or digit == 9 :
            count += 1
        number //= 10
        
    return count

def main() :
    n = int(input())
    count = 0
    
    for i in range(1,n+1) :
        count += count369(i)
        
    print(count)
    
    
if __name__ == "__main__" :
    main()