import json
from triplea.schemas.article import Article
from triplea.service.repository.export.engine import export_engine
from triplea.service.repository.export.unified_export_json import json_converter_02



from config import DATA_FILE, DATA_DIR


def fx_filter(article:Article):
    return True


def fx_transform(article:Article):
    # convert article info into unified format
    ainfo = json_converter_02(article)

    output = {}

    # General one to one info of article
    output['title'] = ainfo["title"]
    output['year'] = ainfo["year"]
    output['journal_issn'] = ainfo["journal_issn"]
    output['language'] = ainfo["language"]
    output['abstract'] = ainfo["abstract"]
    output['doi'] = ainfo["doi"]
    output['pmid'] = ainfo["pmid"]
    output['citation_count'] = ainfo["citation_count"]


    # For IOS Volume
    volume = ""
    if 'PubmedArticleSet' in article.OreginalArticle:
        d = article.OreginalArticle['PubmedArticleSet']
        if 'PubmedArticle' in d:
            d = d['PubmedArticle']
            if 'MedlineCitation' in d:
                d = d['MedlineCitation']
                if 'Article' in d:
                    d = d['Article']
                    if 'Journal' in d:
                        d = d['Journal']
                        if 'JournalIssue' in d:
                            d = d['JournalIssue']
                            if 'Volume' in d:
                                volume = d['Volume']
    

    if volume == "43 Pt A":
        volume = "43"
    elif volume == "43 Pt B":
        volume = "43"

    output['IOSPressVolume'] = volume

    # Recreate publicationType
    # ------------------------Publication Type--------------------
    pt = []
    p = article.OreginalArticle["PubmedArticleSet"]["PubmedArticle"]["MedlineCitation"][
        "Article"
    ]["PublicationTypeList"]["PublicationType"]
    if isinstance(p, list):
        for i in p:
            chunk = i["#text"]
            pt.append(chunk)
    else:
        publication_type = article.OreginalArticle["PubmedArticleSet"]["PubmedArticle"][
            "MedlineCitation"
        ]["Article"]["PublicationTypeList"]["PublicationType"]["#text"]
        pt.append(publication_type)
    # ------------------------Publication Type--------------------
    output['publication_type'] = pt

    # General one to many info of article
    output['authors'] = ainfo["authors"]
    
    list_keywords = []
    if ainfo["keywords"] is not None:
        for k in ainfo["keywords"]:
            list_keywords.append(k.Text)
    output['keywords'] = list_keywords
    list_topic = []
    if ainfo["topics"] is not None:
        for t in ainfo["topics"]:
            list_topic.append(t['text'])
    output['topics'] = list_topic

    output['affiliation_countries'] = ainfo['affiliation_countries']
    output['affiliations'] = ainfo['affiliations'] 


    return output


def fx_output(output):
    if output !="":
        return output
    else:
        return ""
    

def export_repo(output_filename):
    ol = export_engine(fx_filter,fx_transform,fx_output,
                       limit_sample=0,
                       proccess_bar=False)
    print()
    print(f"{len(ol)} Articles selected and transform.")
    

    with open(DATA_DIR / output_filename, 'w') as fp:
        json.dump(ol, fp)

    # # General Model
    # c = Converter()
    # c.convert_unified2csv_dynamically(ol)

if __name__ == "__main__":
    export_repo("dataset-mie.json")


