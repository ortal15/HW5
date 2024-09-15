# START
movie: int = int(input('Movie time in minutes:'))
hours: int = movie // 60
minute: int = movie % 60

print(f"The film is {hours} hour and {minute} minutes long")
# END
