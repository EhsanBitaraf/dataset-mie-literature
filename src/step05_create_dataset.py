import json
import click
from triplea.schemas.article import Article
from triplea.service.repository.export.engine import export_engine
from triplea.service.repository.export.unified_export_json import json_converter_01,json_converter_02
from triplea.service.repository.export.unified_export_json.convert import Converter
# from triplea.utils.general import safe_csv

from config import DATA_FILE, DATA_DIR


def fx_filter(article:Article):
    return True
    for i in article.ReviewLLM:
        if i['TemplateID'] == "datamodel":
            if isinstance(i['Response'],dict):
                if 'IsDataModelDesign' in i['Response']:
                    if i['Response']['IsDataModelDesign'] is True:
                        return True
                else:
                    return False
            else:
                pass
                
    # Finally
    return False

def harmonization_string_field(f):
    if isinstance(f,str):
        output = []
        if f.__contains__(','):
            list_f = f.split(',')
            for i in list_f:
                output.append(safe_csv(i.strip()))
        elif f.__contains__(' or '):
            list_f = f.split(' or ')
            for i in list_f:
                output.append(safe_csv(i.strip()))
        elif f.__contains__(' and '):
            list_f = f.split(' and ')
            for i in list_f:
                output.append(safe_csv(i.strip()))
        else:        
            output = [safe_csv(f)]
    elif isinstance(f,list):
        output = f
    elif f is None:
        output = None
    else:
        # print()
        # print(f"in harmonization_string_field - {f} with type {type(f)} is unhandel.")
        output = ['Can not parse.']

    return output

def fx_transform(article:Article):
    # convert article info into unified format
    ainfo = json_converter_02(article)

    output = {}

    # General one to one info of article
    output['title'] = ainfo["title"]
    output['year'] = ainfo["year"]
    # output['publisher'] = ainfo["publisher"]
    output['journal_issn'] = ainfo["journal_issn"]
    # output['journal_iso_abbreviation'] = ainfo["journal_iso_abbreviation"]
    output['language'] = ainfo["language"]
    # output['url'] = ainfo["url"]
    # output['abstract'] = ainfo["abstract"]
    output['doi'] = ainfo["doi"]
    output['pmid'] = ainfo["pmid"]
    # output['state'] = ainfo["state"]
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
    export_repo("dataset-ios.json")


