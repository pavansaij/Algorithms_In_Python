class Interval(object):
	def __init__(self,s=0,e=0):
		self.start = s
		self.end = e

class stack(object):
	def __init__(self):
		self.stack = []
	def push(self, item):
		return self.stack.append(item)
	def pop(self):
		return self.stack.pop()
	def peek(self):
		return self.stack[len(self.stack)-1]
	def disp(self):
		print(self.stack)

	
class Merge(object):
	def insert(self, si):
		stk = stack()
		stk.push(si[0])
		for i in range(1,len(si)):
			if si[i][0] in range(1-stk.peek()[0],1+stk.peek()[1]):
				sr = min(si[i][0],stk.peek()[0])
				en = max(si[i][1],stk.peek()[1])
				stk.pop()
				stk.push((sr,en))
			else:
				stk.push(si[i])
		return stk

inst = Merge()
inter = [[1,10],[2,2],[3,6],[4,14]]
print(inst.insert(inter).disp())