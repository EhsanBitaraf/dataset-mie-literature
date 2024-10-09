import json
import triplea.service.repository.persist as PERSIST

data = PERSIST.get_article_by_pmid('10179518')
# data = PERSIST.get_article_by_id("9433")
data= json.dumps(data, indent=4)
with open("one-article-10179518.json", "w") as outfile:
    outfile.write(data)