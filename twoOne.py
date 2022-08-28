import time 

print("let's play a game, it\'s called 21")
print()

time.sleep(1)
print("first, rules of the game:")
time.sleep(2)
print("I'll pick a number between 1 and 3 (1,2 or 3. three choices)")
time.sleep(3)
print("then you'll add a number to it. either 1,2 or 3")
time.sleep(3)
print("then I'll add another number to the total")
time.sleep(2)
print("then you'll and this will continue")
time.sleep(2)
print("the person who first reach the number 21 will win the game :)")
print()
time.sleep(2)

switch = 1
while (switch == 1):
	print("#COM └[ꔸ◡ꔸ]┘ : let me go first. I pick :", 1)
	lis = [5,9,13,17,21]
	time.sleep(2)

	num = int(input('*USR ヽ(•◡•)ﾉ : Now your turn, pick a number. you have three choices: either 1,2 or 3 :'))

	while(num > 3 or num < 1):
		time.sleep(1)
		num = int(input(">> remember! only three choices (1,2,3). Pick one again :"))

	total=1+num

	time.sleep(2)
	print("> sum %g + %g = %g" %(1,num,total))
	print()
	i=0
	
	while total != 21: 
		comGuess = lis[i] - total
		time.sleep(2)
		print("#COM └[ꔸ◡ꔸ]┘ : I choose :", comGuess)
		total += comGuess
		time.sleep(2)
		print("> total %g + %g = %g" %(lis[i]-comGuess,comGuess,total))
		i=i+1
		if(total >= 21):
			break
		num=int(input('*USR ヽ(•◡•)ﾉ : Enter the next number you want to add :'))

		while(num>3 or num<1):
			time.sleep(1)
			num = int(input(">> remember! only three choices (1,2,3). Pick one again :"))

		print('> %g + %g = %g' %(total,num,total+num))
		total+=num
		print()

	print()
	time.sleep(1)
	print("  Fatality! COMPUTER WINS └[ꔸ◡ꔸ]┘...[I first reach to the number 21]  ヽ(._.)ﾉ...  ") 
	print()

	time.sleep(2)
	switch = int(input("~(1o1) : Do you want to tray again? [1 for yes 0 for no] :"))
	if switch == 1:
			time.sleep(1)
			print(">> try to pick a number in a way that will take you to the number 21")
			time.sleep(2)
			print(">> good luck for now ;)")
			print()



