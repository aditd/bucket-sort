from queue import Queue
import sys


# this is the input queue
inpt = Queue()
# this is useful to determine the number of digits
largest = 0


#we take in the input and split the input according to the spaces
x = input().split()
x = list(map(int,x))
# the list x is then converted from a list of strings 
# to a list of integers
# we need to use the max function to find the largest number in the list

# we then add the numbers in x to the inpt which is a Queue() object
for i in x:
	inpt.put(i)

# this finds out the largest number in the list
largest = max(x)


# the number of digits help us decide how many iterations to go through
digits = len(str(largest))

n = len(x)

# creating a row of buckets
kyu = [Queue(maxsize = n) for i in range(0,10)]

# this whole collection of buckets is kyu
# | | | | | | | | | | | | | | | | | | | |
# |_| |_| |_| |_| |_| |_| |_| |_| |_| |_| 



# d is the digit place we are at dth from the left
def bucketing(d):
	# this function takes in d which is the dth digit from the right
	# and will go through all the input elements
	# according to the value at the dth place, it will put the number into one of the "buckets"

	for k in range(0, n):
		number = inpt.get()

		# if the digit that needs to be compared is the digit at the hundreds place
		# then we will divide the number eg 4230 // 10**(d=2) = 4230//100 = 42
		# according to this we will put 2 in the 2s bucket
		num_mod = number//(10**d)
		# we need to find the remainder of the modified number 
		remainder = num_mod%10

		# according to the remainder, we put the number in its bucket
		kyu[remainder].put(number)

		# | | | | | 4230 | | | | | | | | | | | | | | |
		# |_| |_| |______| |_| |_| |_| |_| |_| |_| |_| 
		#  0.  1.    2.     3.  4.  5.  6.  7.  8.  9 

def dq():
	# it goes through all the buckets
	for i in range(0,10):
		#this empties out the bucket and stops when the bucket is empty
		while not kyu[i].empty():
			inpt.put(kyu[i].get())
			# this queues the input queue and dequeus the ith bucket 


for j in range(0, digits):
	bucketing(j)
	dq()

# it is easier to print a list. so we convert the queue into a list and then print it according 
# to the autograder's format :)
x=[]
#for printing
for a in list(inpt.queue):
	x.append(a)



for a in x:
	if a ==x[-1]:
		print(a)
		break
	print(a,end=', ')
