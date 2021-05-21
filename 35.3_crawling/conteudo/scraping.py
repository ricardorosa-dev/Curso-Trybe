import dependencies as deps
from responses import make_requests
from extract import extract_data_from
import csv


pacotes = deps.get_dependencies()
urls = deps.get_dependencies_urls(pacotes)

# o [:3] é pra fazer só 3 requisições. Pra não atrapalhar o site fazendo mil requisições
# o make_requests retorna uma lista de urls
data = []
for response in make_requests(urls[:3]):
    data.append(extract_data_from(response.text))

# salvar em um csv
with open('dependencies.csv', 'w') as output:
    writer = csv.DictWriter(output, data[0].keys())
    writer.writeheader()
    for item in data:
        writer.writerow(item)
