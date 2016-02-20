import os, time, datetime
from PIL import Image

path = '../Downloads'

print 'test';

def get_minimum_creation_time(exif_data):
    mtime = '?'
    if 306 in exif_data and exif_data[306] < mtime: # 306 = DateTime
        mtime = exif_data[306]
    if 36867 in exif_data and exif_data[36867] < mtime: # 36867 = DateTimeOriginal
        mtime = exif_data[36867]
    if 36868 in exif_data and exif_data[36868] < mtime: # 36868 = DateTimeDigitized
        mtime = exif_data[36868]
    if mtime == '?':
	return False
    return time.strptime(mtime[0].encode('ascii'), "%Y:%m:%d %H:%M:%S")

today = datetime.datetime.now()
threshold = datetime.datetime(today.year - 21, today.month, today.day, today.hour, today.minute, today.second);

for root, dirs, files in os.walk(path):
    for name in files:
	if name.endswith((".jpeg", ".jpg")):
		img = Image.open(root+'/'+name)
		exif_data = img._getexif()
		if exif_data is not None:
			created = get_minimum_creation_time(exif_data);
			if created != False:
				created = datetime.datetime(*created[:6])
				print root + '/' + name
				print created
				print threshold
				print (created < threshold)
