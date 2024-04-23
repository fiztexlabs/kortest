import matplotlib.pyplot as plt

class KorsarMT:
	def __init__(self):
		self.temp = plt.figure()
		plt.xlabel("t, sec")
		plt.ylabel("T, C")
		
		# self.dP = plt.figure()
		# plt.xlabel("t, sec")
		# plt.ylabel("dP, kPa")
		
	def getResult(self, input):
			plt.figure(self.temp.number)
			plt.scatter(input[0], input[1], color = 'red')
			plt.scatter(input[0], input[2], color = 'blue')
			plt.scatter(input[0], input[3], color = 'green')
			plt.legend(["Вход 1к. в ТХ","Выход 1к. из ТХ","Выход 3к."])
			
			
			# plt.figure(self.dP.number)
			# plt.scatter(input[0], input[4], color = 'red')
			# plt.scatter(input[0], input[5], color = 'orange')
			# plt.scatter(input[0], input[6], color = 'y')
			# 
			# plt.scatter(input[0], input[7], color = 'green')
			# plt.scatter(input[0], input[8], color = 'lime')
			# plt.scatter(input[0], input[9], color = 'cyan')
			# plt.legend(["мтр до пучка","мтр пучок","мтр после пучка","внтр до пучка","внтр пучок","внтр после пучка"])
			
			plt.pause(0.001)
			
			return [0]