import requests
import json


lib_has = {
'inspiration':"#Inspiration4",
'Inspiration':"#Inspiration4",
'Dragon':"#Dragon",
'dragon':"#Dragon",
'Resilience':"#Resilience",
"CesiumAstro":"#cesiumastro",
"Cesiumastro":"#cesiumastro",
"cesiumAstro":"#cesiumastro",
"Turksat":"#turksat",
"turksat":"#Turksat",
"spacex":"#SpaceX",
"SpaceX":"#SpaceX",
"falcon":"#Falcon",
"Falcon":"#Falcon",
"crew":"#Crew",
"Crew":"#Crew",
"space":"#Space",
"Space":"#Space",
"Starship":"#Starship",
"Texas":"#Texas",
"Starbase":"#Starbase",
"BocaChica":"#BocaChica",



}

paritcular ={
	'Falcon 9':'#Falcon9',
	'Crew Dragon':'#CrewDragon',
	'Inspiration 4':'#Inspiration4',
	'Space X':'#SpaceX',
	'Space Force':'#SpaceFroce'
}



def hashtag(text):
	result = requests.get("http://127.0.0.1:5000/hashtag/"+text)
	return json.loads(result.text)['hashtaged']
	"""
	for i, v in paritcular.items():
		
		if i in text:
			inn = text.index(i)
			text = text[:inn] + paritcular[i] + text[inn + len(i):]
	
	


	splt_text = text.split(" ")
	htg_ed = []

	for i in splt_text:
		if i in lib_has:
			htg_ed.append(lib_has[i])
		else:
			htg_ed.append(i)
	regrouped = " ".join(htg_ed)
	return regrouped
	"""




