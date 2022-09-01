# This is the link to this Python coding challenge
# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root():
    num = int(input('Enter any number: '))
    sumlength = 0
    while sumlength != 1:
        numstring = str(num)
        sum = 0
        arr = []
        for i in numstring:
            arr.append(int(i))
            sum += int(i)
        print(f'{arr} = {sum}')
        # print(arr)
        # print(sum)
        num = sum
        sumlength = len(str(sum))
        # print(sumlength)
        if sumlength == 1:
            return print(f'The digital root is {sum}')
digital_root()