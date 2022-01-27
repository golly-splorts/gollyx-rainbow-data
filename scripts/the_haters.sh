#!/bin/bash

gsed -i -e  's/Seattle Sneakers/Team 1/g' \
		-e	's/"SS"/"ABBR1"/g' \
		-e	's/e86215/AAAAAAAAAAAA/g' \
			*.json


gsed -i -e  's/San Francisco Boat Shoes/Team 2/g' \
		-e	's/"SFBS"/"ABBR2"/g' \
		-e	's/e7d7c1/BBBBBBBBBBBB/g' \
			*.json


gsed -i -e  's/Team 1/San Francisco Boat Shoes/g' \
		-e	's/"ABBR1"/"SFBS"/g' \
		-e	's/AAAAAAAAAAAA/e7d7c1/g' \
			*.json


gsed -i -e  's/Team 2/Seattle Sneakers/g' \
		-e	's/"ABBR2"/"SS"/g' \
		-e	's/BBBBBBBBBBBB/e86215/g' \
			*.json


##########################################


gsed -i -e  's/Vegas Vampires/Team 3/g' \
		-e	's/"VV"/"ABBR3"/g' \
		-e	's/aa8040/CCCCCCCCCCCC/g' \
			*.json


gsed -i -e  's/Sacramento Boot Lickers/Team 4/g' \
		-e	's/"SAC"/"ABBR4"/g' \
		-e	's/ffb627/DDDDDDDDDDDD/g' \
			*.json


gsed -i -e  's/Team 3/Sacramento Boot Lickers/g' \
		-e	's/"ABBR3"/"SAC"/g' \
		-e	's/CCCCCCCCCCCC/ffb627/g' \
			*.json


gsed -i -e  's/Team 4/Vegas Vampires/g' \
		-e	's/"ABBR4"/"VV"/g' \
		-e	's/DDDDDDDDDDDD/aa8040/g' \
			*.json

