import requests
import json

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow") 

for question in (response.json()['items']):
	if question['answer_count'] == 0:
		print (question['title'])
	else:
		print('Skipped')
	print ()