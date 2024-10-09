import json
from triplea.schemas.article import Article
from triplea.service.repository.export.engine import export_engine
from triplea.service.repository.export.unified_export_json import json_converter_02
from config import DATA_DIR,DATA_FILE_NAME


def fx_filter(article:Article):
    """
    The function `fx_filter` takes an `Article` object as input and always returns
    `True`.
    
    :param article: The `fx_filter` function takes an `Article` object as a
    parameter
    :type article: Article
    :return: The function `fx_filter` is returning `True`.
    """
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
    # The code  is extracting the volume information from the
    # `article` object. Here's a breakdown of what the code is doing:
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
    """
    The `export_repo` function selects and transforms articles using specified
    functions and exports the result to a JSON file.
    
    :param output_filename: The `output_filename` parameter is a string that
    represents the name of the file where the data will be exported. This parameter
    should be provided as an argument when calling the `export_repo` function to
    specify the name of the output file
    """

    # The `export_engine` function is being called with the following parameters:
    # - `fx_filter`: This is a function that filters articles based on certain
    # criteria. In this case, it seems to be a function that always returns `True`,
    # meaning all articles will pass the filter.
    # - `fx_transform`: This is a function that transforms the selected articles into
    # a specific format. It takes an `Article` object as input and converts it into a
    # dictionary format.
    # - `fx_output`: This function is responsible for handling the output after
    # transformation. If the output is not an empty string, it will return the
    # output; otherwise, it will return an empty string.
    # - `limit_sample=0`: This parameter specifies the limit on the number of
    # articles to process. Here, it is set to `0`, indicating that there is no limit
    # on the number of articles to process.
    # - `proccess_bar=False`: This parameter controls whether a progress bar is
    # displayed during the export process. Here, it is set to `False`, meaning no
    # progress bar will be shown.
    ol = export_engine(fx_filter,fx_transform,fx_output,
                       limit_sample=0,
                       proccess_bar=False)
    print()
    print(f"{len(ol)} Articles selected and transform.")
    

    with open(DATA_DIR / output_filename, 'w') as fp:
        json.dump(ol, fp)


if __name__ == "__main__":
    export_repo(DATA_FILE_NAME)


