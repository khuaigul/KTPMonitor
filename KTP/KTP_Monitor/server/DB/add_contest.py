from KTP_Monitor.models import Contest_Info

def add_contest(name, link, divs):
    c = Contest_Info.objects.get_or_create(name = name, link = link)
    print(c)
    for d in divs:
        c[0].divs.add(d)
    
    print("contest added with choosen divs")
    # return c[0]

	
	

