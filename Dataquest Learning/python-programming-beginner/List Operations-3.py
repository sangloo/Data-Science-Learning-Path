## 2. Parsing the File ##

weather_data = []

data = open('la_weather.csv', 'r').read()
rows = data.split('\n')

for row in rows:
    split_row = row.split(',')
    weather_data.append(split_row)

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []

for item in weather_data:
    val = item[1]
    weather.append(val)

## 4. Counting the Items in a List ##

count = 0
for item in weather:
    count = count + 1

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

if 'cat' in animals:
    cat_found = True
    
if 'space_monster' not in animals:
    space_monster_found = False

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []

for item in weather_types:
    if item in new_weather:
        weather_type_found.append(True)
    else:
        weather_type_found.append(False)