def main():
     number = get_number()
     name(number)


def name(num):
     for i in range(num):
        print("Hey! Sujan You are handsome")

def get_number():
     while True:
          n = int(input("Give me number : "))
          if n>0:
               return n
          else:
               continue



main()