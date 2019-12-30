# importing google_images_download module 
from google_images_download import google_images_download 

def downloadimages(vegetable, limit, response): 
	# keywords is the search query 
	# format is the image file format 
	# limit is the number of images to be downloaded 
	# print urs is to print the image file url 
	# size is the image size which can 
	# be specified manually ("large, medium, icon") 
	# aspect ratio denotes the height width ratio 
	# of images to download. ("tall, square, wide, panoramic") 
	arguments = {"keywords": vegetable, 
				"format": "jpg", 
				"limit":limit, 
				"print_urls":False, 
				"size": "medium", 
				"aspect_ratio": "square",
				"output_ directory":"dataset",
				"image_directory": vegetable,
				"prefix" : vegetable}
	try: 
		response.download(arguments) 
	
	# Handling File NotFound Error	 
	except FileNotFoundError: 
		arguments = {"keywords": vegetable, 
					"format": "jpg", 
					"limit":4, 
					"print_urls":False, 
					"size": "medium",
					"output_ directory":"dataset",
					"image_directory": vegetable}
					
		# Providing arguments for the searched query 
		try: 
			# Downloading the photos based 
			# on the given arguments 
			response.download(arguments) 
		except: 
			pass

# Driver Code
def download_images(vegetables, num=50):
	# creating object 
	response = google_images_download.googleimagesdownload() 

	for vegetable in vegetables: 
		downloadimages(vegetable, num, response) 
		print() 
