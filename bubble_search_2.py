MyList = [25, 34, 98, 7, 41, 19, 5]
print(MyList)
MaxIndex = len(MyList)

# n ← MaxIndex – 1
n = MaxIndex - 1
# FOR i ← 0 TO MaxIndex – 1
for i in range(0, n):
# 	FOR j ← 0 TO n
    for j in range(0, n):
# 		IF MyList[j] > MyList [j + 1] THEN
        if MyList[0] > MyList[j+1]:
            print(MyList)
# 			Temp ← MyList [j]
            Temp = MyList[j]
# 			MyList [j] ← MyList [j + 1]
            MyList[j] = MyList[j+1]
# 			MyList [j + 1] ← Temp
            MyList[j+1] = Temp
# 		ENDIF
# 	NEXT j
# 	n ← n – 1 //not look at already sorted values
    n = n -1
# NEXT i

print(MyList)