text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque nec velit id libero volutpat ultricies.
Sed dictum sem sit amet lectus suscipit, sed laoreet purus eleifend.
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
Quisque efficitur, tellus at tincidunt molestie, ipsum dui maximus libero, vel tempus nisi purus eu mauris.
Phasellus at justo aliquam, vehicula turpis at, faucibus justo.
Aenean lobortis feugiat sem id varius. Curabitur vulputate lacus a augue pretium, at viverra dui mollis.
Fusce euismod ante ac nulla ultricies fringilla."""

sentences = text.split('. ')
topics = {}
keywords = {
'тема 1': ['Lorem', 'ipsum', 'dolor', 'sit', 'amet'],
'тема 2': ['consectetur', 'adipiscing', 'elit'],
'тема 3': ['Pellentesque', 'nec', 'velit'],
'тема 4': ['Sed', 'dictum', 'sem', 'sit', 'amet'],
'тема 5': ['Vestibulum', 'ante', 'ipsum'],
'тема 6': ['Quisque', 'efficitur', 'tellus'],
'тема 7': ['Phasellus', 'at', 'justo'],
'тема 8': ['Aenean', 'lobortis', 'feugiat'],
'тема 9': ['Curabitur', 'vulputate', 'lacus'],
'тема 10': ['Fusce', 'euismod', 'ante']
}

for sentence in sentences:
for topic, keys in keywords.items():
if any(key in sentence for key in keys):
if topic in topics:
topics[topic].append(sentence)
else:
topics[topic] = [sentence]

for topic, sentences in topics.items():
print(f'---{topic}---')
for sentence in sentences:
print(sentence)
print('\n')