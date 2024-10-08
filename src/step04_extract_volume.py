
import triplea.service.repository.persist as PERSIST
import click
from triplea.schemas.article import Article
from triplea.utils.general import print_error
from triplea.service.click_logger import logger
from triplea.config.settings import SETTINGS

def remove(limit_sample=0,
           proccess_bar=True):
    """
    The function `remove` iterates through a list of article IDs, checks for a
    specific volume in each article's metadata, and deletes articles that do not
    match the specified volume criteria.
    
    :param limit_sample: The `limit_sample` parameter in the `remove` function is
    used to specify the maximum number of articles to process before stopping. If
    `limit_sample` is set to a non-zero value, the function will stop processing
    articles once it has checked and potentially deleted the specified number of
    articles. If `, defaults to 0 (optional)
    :param proccess_bar: The `proccess_bar` parameter in the `remove` function is a
    boolean flag that determines whether a progress bar should be displayed during
    the removal process. If `proccess_bar` is set to `True`, a progress bar will be
    shown to indicate the progress of the removal operation. If it, defaults to
    True (optional)
    :return: The `remove` function returns nothing. If the number of documents is
    0, the function will return early without performing any further actions.
    """
    l_id = PERSIST.get_all_article_id_list()
    SETTINGS.AAA_CLI_ALERT_POINT
    n = 0
    doc_number = len(l_id)
    if doc_number == 0:
        return
    if proccess_bar:
        bar = click.progressbar(length=doc_number,
                                show_pos=True,
                                show_percent=True)
    else:
        logger.INFO("Start remove...")

    # MIE Volume
    vl = [316,
            302,
            294,
            281,
            270,
            247,
            235,
            228,
            210,
            205,
            180,
            169,
            150,
            136,
            124,
            116,
            95,
            90,
            77,
            68,
            43,
            34
    ]
    delete_number = 0
    for id in l_id:
        n = n + 1
        try:
            a = PERSIST.get_article_by_id(id)
            article = Article(**a.copy())

            ### Check Volume 
            # PubmedArticleSet PubmedArticle MedlineCitation Article Journal JournalIssue Volume
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

            if volume == "":
                print (f"""Tag Volume is not exist in metadata.
                        PMID {article.PMID}""")
            else:
                try:
                    v = int(volume)
                except:
                    if volume == "43 Pt A":
                        v = 43
                    elif volume == "43 Pt B":
                        v = 43
                    elif volume == "52 Pt 1":
                        v = 52
                    elif volume == "52 Pt 2":
                        v = 52
                    else:
                        print(f"We can not convert {volume} to int.")

                if v in vl:
                    pass
                    # It should not be erased and should be kept

                else:
                    pass # must be deleted
                    try:
                        PERSIST.delete_article_by_id(id)
                        delete_number = delete_number + 1
                    except Exception:
                        print_error()
            ### Check Volume

            # For View Proccess
            if proccess_bar:
                bar.label = f"""{n} Article(s) checked. {delete_number} deleted."""
                bar.update(1)
            else:
                if n % SETTINGS.AAA_CLI_ALERT_POINT == 0:
                    logger.INFO(f"{n} Article(s) checked.")


            if limit_sample != 0:  # Unlimited
                if n > limit_sample:
                    break
        except Exception:
            print()
            print(logger.ERROR(f"article. ID = {id}"))
            print_error()
            
    if proccess_bar is False:
        logger.INFO(f"Delete {delete_number} Document.")
    

if __name__ == "__main__":
    remove(0, proccess_bar=True)
    PERSIST.refresh()
