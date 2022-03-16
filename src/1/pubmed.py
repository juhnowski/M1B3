from pymed import PubMed
pubmed = PubMed(tool="MyTool", email="my@email.address")
results = pubmed.query("\"hdrs\"[All Fields] AND (\"scale s\"[All Fields] OR \"scaled\"[All Fields] OR \"scaling\"[All Fields] OR \"scalings\"[All Fields] OR \"weights and measures\"[MeSH Terms] OR (\"weights\"[All Fields] AND \"measures\"[All Fields]) OR \"weights and measures\"[All Fields] OR \"scale\"[All Fields] OR \"scales\"[All Fields])", max_results=500)

articleList = []
articleInfo = []

for article in results:
# Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle).
# We need to convert it to dictionary with available function
    articleDict = article.toDict()
    articleList.append(articleDict)

# Generate list of dict records which will hold all article details that could be fetch from PUBMED API
for article in articleList:
#Sometimes article['pubmed_id'] contains list separated with comma - take first pubmedId in that list - thats article pubmedId
    pubmedId = article['pubmed_id'].partition('\n')[0]
    # Append article info to dictionary 
    articleInfo.append({u'pubmed_id':pubmedId,
                       u'title':article['title'],
                      # u'keywords':article['keywords'],
                      # u'journal':article['journal'],
                       u'abstract':article['abstract'],
                       #u'conclusions':article['conclusions'],
                       #u'methods':article['methods'],
                       #u'results': article['results'],
                       #u'copyrights':article['copyrights'],
                       u'doi':article['doi'],
                       u'publication_date':article['publication_date'], 
                       u'authors':article['authors']})


print(articleInfo[0])