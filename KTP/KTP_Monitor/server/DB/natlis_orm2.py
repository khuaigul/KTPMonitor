from KTP_Monitor.models import Div_Info

def pr():
    divs = Div_Info.objects.all()
    print(divs.query)
    print(divs)
    print(123)