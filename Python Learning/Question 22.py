#count vowels latters how many times becomes
word="I am become data analytics in any situation "
count=0
for ch in word:
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        count +=1
print(f"Vowels in word variable have {count} times")        