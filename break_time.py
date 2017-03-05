import webbrowser as browser
import time
# from python standard library

# if you truly want to learn something... please teach it to someone else

# python make my program wait
total_breaks = 3
break_count = 0
print("This Progrram Started On: " + time.ctime())
print(break_count)

while(break_count < total_breaks):
	time.sleep(10)
	browser.open("https://www.youtube.com/watch?v=f6vY6tYvKGA")
	break_count += 1


'''
	get all the file names
	for each of the file name rename those files and remove the number from  the file name
'''