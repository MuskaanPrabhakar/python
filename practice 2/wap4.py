#4. Build a duplicate finder. Take a list of numbers from the user. Use sets to find which numbers appear more than once, which appear exactly once, and which appear more than twice. Print three separate results.
l = list((input("Enter numbers with spaces: ")).split())
print(l)
once = set()
moreonce = set()
moretwice= set()
for num in l:
    num=int(num)
    if num not in once:
        once.add(num)
    elif num in once and num not in moreonce:
        moreonce.add(num)
    elif num in moreonce:
        moretwice.add(num)
once -= moreonce
moreonce-=moretwice
print(f"Number that appeared more than once are {moreonce}\n Number that appeared only once {once}\n Number that appeared more than twice {moretwice}")