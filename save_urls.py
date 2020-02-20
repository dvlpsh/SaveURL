import sys
import datetime
import pathlib #pip install pathlib
import lz4.block #pip install lz4
import json
import webbrowser #comes bundled with python 3.6

class OpenLinks:
	def open_urls_in_browser(self, fname):
		with open(fname, 'r') as file:
			#urls = savelink.get_urls()
			line = file.readline().strip()
			while(line != ''):
			#for url in urls:
				webbrowser.open_new_tab(line)



class SaveLinks:

	def append_urls_to_file(self):
		now = datetime.datetime.now()
		fname=str('links')+'-'+str(now.day)+'-'+str(now.month)+'-'+str(now.year)+'.txt'
		print(fname)
	
		with open(fname, "a") as file:
			urls = self.get_urls()
			for url in urls:
				print("URL: ", url, "\n")
				file.write(url+'\n\n') 
		#file.close() 
	

	def get_urls(self):
		path = pathlib.Path.home().joinpath('.mozilla/firefox')
		files = path.glob('*default*/sessionstore-backups/recovery.js*')

		try:
			template = sys.argv[1]
		except IndexError:
			template = '%s %s'

		urls=[] #empty list where urls will be stored
		for f in files:
			b = f.read_bytes()
			if b[:8] == b'mozLz40\0':
				b = lz4.block.decompress(b[8:])
			j = json.loads(b)
			for w in j['windows']:
				for t in w['tabs']:
					i = t['index'] - 1 
					#print(template % ('Url:' , t['entries'][i]['url']))
					urls.append(str(t['entries'][i]['url']))
				
		return urls
						
				
				
def main(): #driver code

	savelink=SaveLinks()
	openlink=OpenLinks()
	
	flag=0
	
	while flag!=-1:
		choice=int(input('1.Save Links to file?\n2.Open Saved links in a browser window\nPress -1 to Exit\n\nEnter your choice:'))
		flag1=True
		
		if choice==1:
			savelink.append_urls_to_file()
			
		elif choice==2:
			fname = input('Enter the filename')
			
			try:
				 f = open(fname)
				 f.close()
			except FileNotFoundError:
				 print('File does not exist')
				 flag1=False

			if flag1==True :
				openlink.open_urls_in_browser(fname)#provide path to the file
				
		elif choice==-1:
			flag=choice;
			
		else :
			print('Invalid choice. Try again.\n\n')
	
	
	
	#get_urls() #should return a list of urls, write a separate function accepting this list and printing it to a file
	#append_urls_to_file()
	#open_urls_in_browser('links-18-2-2020.txt')
	
	
if __name__ == "__main__":
	main()

	
			
			
#DONE
# create a new file named links-todays-date.txt
# If such a file already exists, create new file named links-todays-date-1.txt
# provision for opening all specified links in a saved file in a web browser window.


#Todo

# modularity, put everything into functions and arrange this as a class
# put this up on github and create a perfect documwntation, and update resume
# Research about the various functions and libraries used here.
# put this in place of video downloader and update video downloaer to audio downloader on the resume.
#
#
# Save this file to the desktop as defailt location, or to the location provided, if location is invalid, prompt for correct location, create provision for being able to change the default location

