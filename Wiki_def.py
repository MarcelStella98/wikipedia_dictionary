
import wikipediaapi



def get_wiki_definition(word):
    wiki = wikipediaapi.Wikipedia('pl')
    page = wiki.page(word)
    if page.exists():
        return page.summary
    else:
        return "Sorry, I couldn't find a definition for that word."

word = ("kamień") # słowo, dla którego chcesz uzyskać definicję
definition = get_wiki_definition(word)
print(definition)
