import requests


session = requests.session()

form_url = 'https://urs.earthdata.nasa.gov/home'
form_response = session.get(form_url)
form_html = form_response.text

for line in form_html.split('\n'):
    if 'form id="login"' in line:
        pos = line.find('authenticity_token" value=')
        token = line[pos:].split('"')[2]
        break

# input your own info
payload = {
        'username': 'YOUR USERNAME',
        'password': 'YOUR PASSWORD,',
        'utf8': '✓',
        'authenticity_token': token,
}

print(session.cookies)
url = 'https://urs.earthdata.nasa.gov/login'
response = session.post(url, data=payload, headers=dict(Referer=url))

# sample file to be downloaded: url = "https://data.gesdisc.earthdata.nasa.gov/data/NLDAS/NLDAS_FORB0125_M.2.0/1997/NLDAS_FORB0125_M.A199701.020.nc"

in_python = # your .txt file containing all the links to be downloaded created using EarthData download site 

with open(in_python, 'r') as file:
    urls = file.readlines()
for url in urls:
    url = url.strip()
    current_file = ""
    try:
        files = [
                url
                ]
        for ff in files:
            current_file = ff
            out_f = ff.split("/")[-1]
            result = session.get(ff)
            result.raise_for_status()
            f = open(out_f, "wb")
            f.write(result.content)
            f.close()
            print("contents of URL written to " + out_f)
    except Exception as e:
        print(current_file, e)

