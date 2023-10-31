
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def ext(file):
	index = file.find(".jpg")
	current_file = ""
	current_file = file[index:]
	return current_file 

def ext2(file):
	index = file.find(".jpeg")
	current_file = ""
	current_file = file[index:]
	return current_file 

def ext3(file):
	index = file.find(".png")
	current_file = ""
	current_file = file[index:]
	return current_file 

def convert(words):
	s = ""
	for word in words:
		s += word.upper() 
	return s

caption_first = convert(captionarr[0])
caption_second = convert(captionarr[1])
caption_third = convert(captionarr[2])
	
print(caption_first)
print(caption_second)
print(caption_third)


count = 0

for f in os.listdir('.'):
	try:
		if (ext(f) == '.jpg' or ext2(f) == '.jpeg' or ext3(f) == '.png'):
			img = Image.open(f) 
			width, height = img.size
			basewidth = 1200
			wpercent = (basewidth / float(img.size[0]))
			hsize = int((float(img.size[1])*float(wpercent)))
			img = img.resize((basewidth, hsize), Image.ANTIALIAS)
			new_width, new_height = img.size


			if not img.mode == 'RGB':
				img = img.convert('RGB')
		
			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype("Arial Bold.ttf", 35) 
			if count == 0:
				draw.text((new_width / 15 + 25, new_height - 100),
						caption_first, (255, 0, 0), font = font,
						align ="center")
			elif count == 1: 
				draw.text((new_width / 15 + 25, new_height - 100),
						caption_second, (255, 0, 0), font = font,
						align ="center")    
			else: 
				draw.text(( new_width / 15 + 25, new_height - 100),
							caption_third, (255, 0, 0), font = font,
							align ="center")			 

			img.save("CaptionedImges/{}".format(f))	 
			print('done')
			count = count + 1
			
	except OSError:
		pass
