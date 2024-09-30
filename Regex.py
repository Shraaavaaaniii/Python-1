#python program using regular expression

# re.findall()
# import re
# text = '''Hello my number is 123456789 and my friend number is 987654321'''
# pattern = r'\d+'
# match = re.findall(pattern,text)
# print(match)

# re.search()
# import re
# text = "The rain in spain"
# pattern = '\s'   #It will match the whitespaces from text
# match = re.search(pattern,text)
# print("The whitespaces start from",match.start())
# match2 = re.search('India',text) # if match not found then it will return null
# print(match2)

#re.sub()
# import re
# text = 'I love talkative people'
# newstr = re.sub('\s','-',text)   #it will replace whitespaces with hypen
# print(newstr)

#re.split()
# import re
# text = "There is raining"
# li = re.split('\s',text)
# print(li)
# text2 = "Hello  and Hi my name is shravani and I'm from top"
# match = re.findall('^H\w+',text2)
# print(match)
# match = re.findall('\w+p$',text2)
# print(match)

# re.compile()
# import re 
# p = re.compile('[a-e]')
# print(p.findall('Aye,said Mr.Gibenson stark'))