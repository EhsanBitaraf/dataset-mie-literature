from triplea.service.repository.state.initial import get_article_list_from_pubmed_all_store_to_arepo

if __name__ == "__main__":
    # Get article from Pubmed for the 
    # Studies in health technology and informatics journal
    pubmed_search_string = '"Stud Health Technol Inform"[jour]'
    get_article_list_from_pubmed_all_store_to_arepo(pubmed_search_string)

