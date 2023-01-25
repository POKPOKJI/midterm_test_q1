class AIChatBot:
	def showSubjectName(self):
		print("AI for robot system")
		return()
	def showStudentYear(self):
		x = input()
		if x[1] == "0" :
			print("6")
		elif x[1] == "1" :
			print("5")
		elif x[1] == "2" :
			print("4")
		elif x[1] == "3" :
			print("3")
		elif x[1] == "4" :
			print("2")
		elif x[1] == "5" :
			print("1")
		return()
	def calculator(self):
    		x = input()
    		if x == "+":
        		a = 0
        		b = int(input())
        		while a == 0 :
            			x = int(input())
            			n = b + x
            			print(n)
            			a = 1
    		elif x == "-":
        		a = 0
        		b = int(input())
        		while a == 0 :
            			x = int(input())
            			n = b - x
            			print(n)
            			a = 1
    		return()
	def main(self):
		x = input()
		x = str(x)
		if x == "subject" :
			self.showSubjectName()
		elif x == "year" :
			self.showStudentYear()
		elif x == "calc" :
			self.calculator()
				
				
while(1):
	bot = AIChatBot()
	bot.main()
				
