from googlesearch import search

def searching(query):
    results = {}
    key = 1
    for i in search(query, tld="co.in", num=10, stop=10, pause=2):
        results[key] = i
        key += 1
    else:
        return results

#query = input("Enter Search: ")
#searching(query)