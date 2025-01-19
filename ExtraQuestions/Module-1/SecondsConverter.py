Seconds = int(input("Enter the Number of Seconds: "))
Hours = Seconds//3600
Minutes = (Seconds%3600)//60
Remaining_Seconds = Seconds//60

print(f"{Seconds}Seconds = {Hours}:{Minutes}:{Remaining_Seconds}")