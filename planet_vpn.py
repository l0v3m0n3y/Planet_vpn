import requests
class Client():
	def __init__(self):
		self.api="https://skdjf7az.online"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def register(self,email):
		data={"email":email,"visitor_id":"none","affiliate_stamp":"{\"a_aid\":\"500\",\"btag\":\"a500-b1-p0-cRU\"}"}
		return requests.post(f"{self.api}/register",json=data,headers=self.headers).json()
	def my_ip(self):
		return requests.get(f"{self.api}/ip",headers=self.headers).json()
	def offers(self):
		return requests.get(f"{self.api}/offers",headers=self.headers).json()
	def forgot_password(self,email):
		data={"email":email}
		return requests.post(f"{self.api}/forgot",json=data,headers=self.headers).json()