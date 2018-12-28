from id3 import observation

'''
The following is a sample dataset, used for testing the code
'''

sample = [
observation('No', { 'Outlook':'Sunny', 'Temp':'Hot', 'Humidity':'High', 'Windy':'False'}),
observation('No', { 'Outlook':'Sunny', 'Temp':'Hot', 'Humidity':'High', 'Windy':'True'}),
observation('Yes', { 'Outlook':'Overcast', 'Temp':'Hot', 'Humidity':'High', 'Windy':'False'}),
observation('Yes', { 'Outlook':'Rainy', 'Temp':'Mild', 'Humidity':'High', 'Windy':'False'}),
observation('Yes', { 'Outlook':'Rainy', 'Temp':'Cool', 'Humidity':'Normal', 'Windy':'False'}),
observation('No', { 'Outlook':'Rainy', 'Temp':'Cool', 'Humidity':'Normal', 'Windy':'True'}),
observation('Yes', { 'Outlook':'Overcast', 'Temp':'Cool', 'Humidity':'Normal', 'Windy':'True'}),
observation('No', { 'Outlook':'Sunny', 'Temp':'Mild', 'Humidity':'High', 'Windy':'False'}),
observation('Yes', { 'Outlook':'Sunny', 'Temp':'Cool', 'Humidity':'Normal', 'Windy':'False'}),
observation('Yes', { 'Outlook':'Rainy', 'Temp':'Mild', 'Humidity':'Normal', 'Windy':'False'}),
observation('Yes', { 'Outlook':'Sunny', 'Temp':'Mild', 'Humidity':'Normal', 'Windy':'True'}),
observation('Yes', { 'Outlook':'Overcast', 'Temp':'Mild', 'Humidity':'High', 'Windy':'True'}),
observation('Yes', { 'Outlook':'Overcast', 'Temp':'Hot', 'Humidity':'Normal', 'Windy':'False'}),
observation('No', { 'Outlook':'Rainy', 'Temp':'Mild', 'Humidity':'High', 'Windy':'True'})
]

KEYS = sample[0].attribs.keys()
