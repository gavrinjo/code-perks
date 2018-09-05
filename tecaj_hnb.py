import urllib.request, json
with urllib.request.urlopen("http://api.hnb.hr/tecajn/v1") as url:
    data = json.loads(url.read())
"""
-(data keys)-
Broj tečajnice
Datum primjene
Država
Šifra valute
Valuta
Jedinica
Kupovni za devize
Srednji za devize
Prodajni za devize
"""
print("|{:{align}{width}}|{:{align}{width3}}|{:{align}{width1}}|{:{align}{width2}}|{:{align}{width2}}|{:{align}{width2}}|".format("Datum","Država","","Kupovni","Srednji","Prodajni", align="^", width="12",width1="5",width2="10",width3="22"))
#print("|---------------------------------------------------|")
for i in data:
  dp = i["Datum primjene"]
  dr = i["Država"]
  vl = i["Valuta"]
  tmin = i["Kupovni za devize"]
  tmid = i["Srednji za devize"]
  tmax = i["Prodajni za devize"]
  print("| {} | {:{align}{width}} | {} | {} | {} | {} |".format(dp, dr, vl, tmin, tmid, tmax, align="^", width="20"))
#print("|---------------------------------------------------|")
