import json, urllib3, re, difflib, time
start_time = time.perf_counter()
# earl = 'https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_kjv.json'
def get_jaccard_sim(str1, str2):
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

file = open("en_kjv.json", 'r',errors='ignore', encoding='UTF-8-sig')
def load_data(file):
    js = json.load(file)
    stringify(js)
def stringify(js):
    jaccard = []
    jac = []
    with open("jaccard.json", 'w', encoding='UTF-8', errors='ignore') as of:
        for a, b in enumerate(js):
            for c, d in enumerate(js):
                if a > c:
                    book1 = js[a].get("chapters")
                    book2 = js[c].get("chapters")
                    text1 = ""
                    text2 = ""
                    for chapter in book1:
                        for verse in chapter:
                            text1 += str(verse).lower()
                    for chapter in book2:
                        for verse in chapter:
                            text2 += str(verse).lower()
                    #g = difflib.SequenceMatcher(None, data, data1).ratio()
                    #jaccard.append('"book1":"' + js[i].get("name") + '","book2":"' + js[x].get("name") + '", "type":"sequencematcher", "similarity":"' + str(g) + '"\n')
                    jaccard.append('{"book1":"' + js[a].get("name") + '","book2":"' + js[c].get("name") + '", "type":"jaccard", "similarity":"' + str(get_jaccard_sim(text1,text2)) + '"}\n')
        for j in jaccard:
            jac.append(json.loads(j).get("similarity"))
        for m in sorted(jac, reverse=True):
            for j in jaccard:
                if m == json.loads(j).get("similarity"):
                    of.write(j)

load_data(file)
print(time.perf_counter() - start_time, "seconds")