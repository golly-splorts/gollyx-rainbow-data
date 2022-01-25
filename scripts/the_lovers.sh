#!/bin/bash

gsed -i -e  's/San Diego Balloon Animals/Team 1/g' \
		-e	's/"SDBA"/"ABBR1"/g' \
		-e	's/f08700/AAAAAAAAAAAA/g' \
			*.json


gsed -i -e  's/Tucson Butchers/Team 2/g' \
		-e	's/"TB"/"ABBR2"/g' \
		-e	's/bb0000/BBBBBBBBBBBB/g' \
			*.json


gsed -i -e  's/Team 1/Tucson Butchers/g' \
		-e	's/"ABBR1"/"TB"/g' \
		-e	's/AAAAAAAAAAAA/bb0000/g' \
			*.json


gsed -i -e  's/Team 2/San Diego Balloon Animals/g' \
		-e	's/"ABBR2"/"SDBA"/g' \
		-e	's/BBBBBBBBBBBB/f08700/g' \
			*.json


##########################################


gsed -i -e  's/Fargo Flea Flickers/Team 3/g' \
		-e	's/"FFF"/"ABBR3"/g' \
		-e	's/daed20/CCCCCCCCCCCC/g' \
			*.json


gsed -i -e  's/Milwaukee Flamingos/Team 4/g' \
		-e	's/"MILF"/"ABBR4"/g' \
		-e	's/ff66cc/DDDDDDDDDDDD/g' \
			*.json


gsed -i -e  's/Team 3/Milwaukee Flamingos/g' \
		-e	's/"ABBR3"/"MILF"/g' \
		-e	's/CCCCCCCCCCCC/ff66cc/g' \
			*.json


gsed -i -e  's/Team 4/Fargo Flea Flickers/g' \
		-e	's/"ABBR4"/"FFF"/g' \
		-e	's/DDDDDDDDDDDD/daed20/g' \
			*.json

