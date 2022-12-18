

# Die URL der Webseite, von der die Bilder heruntergeladen werden sollen
url = ''
sub_url = ""

# Die Webseite herunterladen und den HTML-Code speichern
response = requests.get(url)
html = response.text

# Den HTML-Code parsen und das DOM erstellen
soup = BeautifulSoup(html, 'html.parser')

# Alle img-Tags im DOM finden
images = soup.find_all('img')

# Für jedes Bild die URL extrahieren und das Bild herunterladen
#try:
for image in images:
    # Die URL des Bildes extrahieren
    img_url = image['src']
    print(sub_url+img_url)
        
        
  # Das Bild herunterladen
    img_data = requests.get(sub_url+img_url).content
    #Den Dateinamen des Bildes aus der URL extrahieren
    filename = img_url.split('/')[-1]
    #Das Bild auf der Festplatte speichern
    with open(filename, 'wb') as f:
        f.write(img_data)
#except:
    #print("Es ist ein Fehler aufgetreten")
