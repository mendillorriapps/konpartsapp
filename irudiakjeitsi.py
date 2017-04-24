import csv
import requests
izenak=["Pamplona","mendillorri"]
for izena in izenak:
    data={}
    with open('/home/euskera/Mahaigaina/Dokumentuak/JULEN/konpartsapp/parametroak.csv') as fin:
        reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
        for row in reader:
            data[row[0]]=row[1]

    data["t"]=izena
    r = requests.get('https://dabuttonfactory.com/button.png', params=data)
    print(r.url,r.status_code)
    with open(izena+".png", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    print(data)