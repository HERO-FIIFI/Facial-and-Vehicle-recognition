import numpy as np
import cv2
from PIL import Image
import pytesseract as tess

def recognize_license_plate(license_plate_image):

	def preprocess(img):
		imgBlurred = cv2.GaussianBlur(img, (5,5), 0)
		gray = cv2.cvtColor(imgBlurred, cv2.COLOR_BGR2GRAY)
		sobelx = cv2.Sobel(gray,cv2.CV_8U,1,0,ksize=3)
		ret2,threshold_img = cv2.threshold(sobelx,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		return threshold_img

	def cleanPlate(plate):
		gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
		_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
		im1,contours,_ = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		
		if contours:
			areas = [cv2.contourArea(c) for c in contours]
			max_index = np.argmax(areas)
			max_cnt = contours[max_index]
			x,y,w,h = cv2.boundingRect(max_cnt)
			
			if not ratioCheck(max_cntArea,w,h):
				return plate,None
			
			cleaned_final = thresh[y:y+h, x:x+w]
			return cleaned_final,[x,y,w,h]
		else:
			return plate,None

	def extract_contours(threshold_img):
		element = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(17, 3))
		morph_img_threshold = threshold_img.copy()
		cv2.morphologyEx(src=threshold_img, op=cv2.MORPH_CLOSE, kernel=element, dst=morph_img_threshold)
		_,contours, _ = cv2.findContours(morph_img_threshold,mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
		return contours

	def ratioCheck(area, width, height):
		ratio = float(width) / float(height)
		if ratio < 1:
			ratio = 1 / ratio
		aspect = 4.7272
		min = 15*aspect*15  # minimum area
		max = 125*aspect*125  # maximum area
		rmin = 3
		rmax = 6
		if (area < min or area > max) or (ratio < rmin or ratio > rmax):
			return False
		return True

	def isMaxWhite(plate):
		avg = np.mean(plate)
		if(avg>=115):
			return True
		else:
			return False

	def validateRotationAndRatio(rect):
		(x, y), (width, height), rect_angle = rect
		if(width>height):
			angle = -rect_angle
		else:
			angle = 90 + rect_angle
		if angle>15:
			return False
		if height == 0 or width == 0:
			return False
		area = height*width
		if not ratioCheck(area,width,height):
			return False
		return True

	def cleanAndRead(img,contours):
		for i,cnt in enumerate(contours):
			min_rect = cv2.minAreaRect(cnt)
			if validateRotationAndRatio(min_rect):
				x,y,w,h = cv2.boundingRect(cnt)
				plate_img = img[y:y+h,x:x+w]
				if(isMaxWhite(plate_img)):
					clean_plate, rect = cleanPlate(plate_img)
					if rect:
						x1,y1,w1,h1 = rect
						x,y,w,h = x+x1,y+y1,w1,h1
						plate_im = Image.fromarray(clean_plate)
						text = tess.image_to_string(plate_im, lang='eng')
						return text  # return the recognized text

	def recognize_license_plate(license_plate_image_path):
		#img = cv2.imread(license_plate_image_path)
		license_plate_image
		threshold_img = preprocess(img)
		contours = extract_contours(threshold_img)
		plate_text = cleanAndRead(img, contours)
		return plate_text

	# Test (optional)
	if __name__ == '__main__':
		plate = recognize_license_plate("testData/test.jpeg")
		print("Recognized License Plate:", plate)
# return license_plate_text
