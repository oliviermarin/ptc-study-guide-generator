# -*- coding: utf-8 -*-

from fpdf import FPDF
from pymongo import MongoClient
from point import Point
from category import Category

# Connection au client mongodb
client=MongoClient('localhost', 27017)
passeTonCode=client.passeTonCode
signs=passeTonCode.signs

result=signs.find();
sign_list_result=[sign for sign in result]
chunks=[sign_list_result[i:i+12] for i  in range(0, len(sign_list_result), 12)]

# Définition des points initiaux
category_pt=Point(8, 0)
image_pt=Point(31, 10)
meaning_pt=Point(8, 39)

# liste de réperage des panels de la fiche
landmark_list=[]
for ordo in range(3):
	for absc in range(4):
		landmark_list.append(Point(absc, ordo))

# Définition des décalage
horizontal_gap=70
vertical_gap=64

#Création du pdf
pdf = FPDF('L')

for chunk_index, sign_list in enumerate(chunks):

	# Création du pdf courant
	pdf.add_page()

	# Lignes verticales
	pdf.dashed_line(8, 0, 8, 192, dash_length = 1, space_length = 1)
	pdf.dashed_line(78, 0, 78, 192, dash_length = 1, space_length = 1)
	pdf.dashed_line(148, 0, 148, 192, dash_length = 1, space_length = 1)
	pdf.dashed_line(218, 0, 218, 192, dash_length = 1, space_length = 1)
	pdf.dashed_line(288, 0, 288, 192, dash_length = 1, space_length = 1)

	# Lignes horizontales
	pdf.dashed_line(8, 0, 288, 0, dash_length = 1, space_length = 1)
	pdf.dashed_line(8, 64, 288, 64, dash_length = 1, space_length = 1)
	pdf.dashed_line(8, 128, 288, 128, dash_length = 1, space_length = 1)
	pdf.dashed_line(8, 192, 288, 192, dash_length = 1, space_length = 1)
	
	for index, sign in enumerate(sign_list):		
		category_ptn_pt=Point(category_pt.x+landmark_list[index].x*horizontal_gap, category_pt.y+landmark_list[index].y*vertical_gap)
		pdf.set_xy(category_ptn_pt.x, category_ptn_pt.y)
		
		for category in Category:
			if category.name.lower() == sign_list[index]['category']:
				pdf.set_fill_color(category.value['color'].r, category.value['color'].g, category.value['color'].b)
				pdf.set_font('Arial', 'B', 12)
				pdf.cell(70, 10, txt=category.value['title'], border=0, ln=0, align='C', fill=True)

		image_ptn_pt=Point(image_pt.x+landmark_list[index].x*horizontal_gap, image_pt.y+landmark_list[index].y*vertical_gap)
		pdf.image(sign_list[index]['miniature_uri'], x=image_ptn_pt.x, y=image_ptn_pt.y, w=24, h=24, type='jpg')
	
		meaning_ptn_pt=Point(meaning_pt.x+landmark_list[index].x*horizontal_gap, meaning_pt.y+landmark_list[index].y*vertical_gap)
		pdf.set_xy(meaning_ptn_pt.x, meaning_ptn_pt.y)
		pdf.set_font('Arial', '', 8)
		alignment='C' if (pdf.get_string_width(sign_list[index]['meaning'].encode('cp1252')) < 70) else 'J'
		pdf.multi_cell(70, 3, txt=sign_list[index]['meaning'].encode('cp1252'), border=0, align=alignment, fill=False)

pdf.output('./permis-study-guide/study-guide.pdf', 'F')
