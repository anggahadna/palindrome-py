test = ['aba','abcd','abcde','aebcbea','aaaaabcbaaaaa','ppppssss','psasp','abcda']

for words in (test):
  a = len(words)
  b = a // 2
  i=1
  checkList = []
  for x in range(b):
    temp1 = words[x]
    temp2 = words[a-i]
    check = temp1==temp2
    checkList.append(check)
    print(temp1 + " " + temp2)
    i+=1
  finalCheck = False not in checkList
  print(words + " = " + str(finalCheck) + "\n")
  
