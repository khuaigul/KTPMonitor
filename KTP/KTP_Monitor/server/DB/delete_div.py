from KTP_Monitor.models import Div_Info

def delete_div(div):
	div.delete()
    
	# print("div deleted")
	return True
