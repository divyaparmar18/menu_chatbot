decade = {"1950": [{"position": 9,"movie_name": "Pather Panchali",},{"position": 3,"movie_name": "Aparajito",}],"1960": [{"position": 19,"movie_name": "Guide"},{"position": 33,"movie_name": "Mughal-E-Azam",}]}
for i in decade.keys():
	print i
	decade[i].sort(key=lambda i: i["position"])
print decade
		
