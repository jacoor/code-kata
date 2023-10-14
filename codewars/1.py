# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
# Solution:
def title_case(title, minor_words=''):
    if not title:
        return title
    title = title.title()
    for minor_word in minor_words.split(" "):
        title = title.replace(minor_word.title(), minor_word.lower())
    title = title[0].upper() + title[1:]
    return title
    
    
