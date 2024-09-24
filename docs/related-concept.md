

# Opensource Project

## vila 
 Incorporating VIsual LAyout Structures for Scientific Text Classification

https://github.com/allenai/vila/blob/main/README.md

##  CERMINE
Content ExtRactor and MINEr 

CERMINE is a Java library and a web service (cermine.ceon.pl) for extracting metadata and content from PDF files containing academic publications. CERMINE is written in Java at Centre for Open Science at Interdisciplinary Centre for Mathematical and Computational Modelling, University of Warsaw.

https://github.com/CeON/CERMINE

http://cermine.ceon.pl/index.html

# Article

[Structured Affiliations Extraction from Scientific Literature](https://www.dlib.org/dlib/november15/tkaczyk/11tkaczyk.html)

![](https://www.dlib.org/dlib/november15/tkaczyk/tkaczyk-fig7.png)

# Website

[Global Research Identifier Database](https://grid.ac/)

# QA

# How can extract country from affiliations text of scientific article
To extract country information from affiliations text in scientific articles, you can follow these steps:

## Text Processing and Pattern Matching

1. Clean and preprocess the affiliation text by removing punctuation and converting to lowercase.

2. Use a database or list of country names to match against the processed text. This can be done using simple string matching or more advanced natural language processing techniques[1].

3. Look for common patterns that indicate a country, such as:
   - Country names at the end of the affiliation string
   - Country codes (e.g., "UK", "USA")
   - State/province names followed by a country

## Leveraging Existing Tools and Libraries

Several tools and libraries can assist in this process:

- **Natural Language Processing (NLP) libraries**: Use libraries like spaCy or NLTK to perform named entity recognition, which can identify country names in text[3].

- **Geocoding services**: Utilize geocoding APIs or services to convert affiliation text into structured location data, including country information[3].

- **Specialized libraries**: Some libraries are designed specifically for parsing academic affiliations, such as the "affiliations" library in Python[3].

## Machine Learning Approaches

For more complex cases or large datasets, consider using machine learning:

1. Train a model on a dataset of labeled affiliations to recognize country information.
2. Use features such as word embeddings, character n-grams, and positional information to improve accuracy.

## Post-processing and Validation

After extraction:

1. Normalize country names to a standard format (e.g., "United States" vs "USA").
2. Validate extracted countries against a known list to catch errors.
3. Handle edge cases like multiple countries in a single affiliation.

## Considerations

- Be aware that affiliation formats can vary widely between publications and disciplines[1].
- Some articles may not explicitly mention the country, requiring inference from city or institution names[3].
- Consider using a combination of methods for best results, as no single approach is likely to catch all cases accurately.

By implementing these techniques, you can effectively extract country information from affiliation text in scientific articles, enabling various analyses such as collaboration patterns and geographic distribution of research.

Citations:
[1] https://stackoverflow.com/questions/5318076/extracting-country-name-from-author-affiliations
[2] https://api-lab.dimensions.ai/cookbooks/7-researchers/Researchers-Search-tips-V2.html
[3] https://www.linkedin.com/advice/3/how-can-you-extract-author-affiliation-data-from-academic-ksquf
[4] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0244918
[5] https://www.researchgate.net/post/Do_you_know_how_can_i_extract_scientific_productions_of_a_country_on_the_issue_of_library_science_from_the_Scopus
[6] https://www.dlib.org/dlib/november15/tkaczyk/11tkaczyk.html
[7] https://www.researchgate.net/publication/262327268_Extracting_and_matching_authors_and_affiliations_in_scholarly_documents
[8] https://www.comp.nus.edu.sg/~kanmy/papers/jcdl2013.pdf

# can you write python code for this or introduce an opensource project that can do it for me
To extract country information from author affiliations in scientific articles, you can use a combination of natural language processing techniques and existing libraries. Here's a Python-based approach using an open-source project called "pycountry" that can help you achieve this:

## Using pycountry and custom logic

First, install the required libraries:

```bash
pip install pycountry pandas
```

Then, you can use the following Python code:

```python
import pycountry
import pandas as pd
import re

def extract_country(affiliation):
    # Convert to lowercase for easier matching
    affiliation = affiliation.lower()
    
    # Remove common words that might interfere with country detection
    words_to_remove = ['university', 'institute', 'department', 'of', 'the']
    for word in words_to_remove:
        affiliation = affiliation.replace(word, '')
    
    # Check for country names
    for country in pycountry.countries:
        if country.name.lower() in affiliation:
            return country.name
        if country.alpha_2.lower() in affiliation:
            return country.name
        if hasattr(country, 'alpha_3') and country.alpha_3.lower() in affiliation:
            return country.name
    
    # Check for common country abbreviations
    common_abbrevs = {'usa': 'United States', 'uk': 'United Kingdom'}
    for abbrev, full_name in common_abbrevs.items():
        if abbrev in affiliation:
            return full_name
    
    return 'Unknown'

# Example usage
df = pd.read_csv('your_data.csv')  # Load your data
df['Country'] = df['Affiliation'].apply(extract_country)

print(df[['Affiliation', 'Country']])
```

This code does the following:

1. It defines a function `extract_country` that takes an affiliation string as input.
2. The function preprocesses the affiliation text by converting it to lowercase and removing common words that might interfere with country detection.
3. It then checks for country names, 2-letter codes, and 3-letter codes using the pycountry library.
4. It also checks for common abbreviations like "USA" and "UK".
5. If no country is found, it returns "Unknown".

## Open-source projects

For more comprehensive solutions, you might want to consider these open-source projects:

1. **ScientoPy**: This is a Python-based scientometric analysis tool that includes functionality for extracting country information from author affiliations[3]. It's available on GitHub and can be a good starting point for more advanced analysis.

2. **AffiliationParser**: While not specifically for country extraction, this project on GitHub (https://github.com/titipata/affiliation_parser) uses machine learning to parse affiliations into structured data, including country information.

3. **geoparse**: This is a Python library for extracting country and city information from text. It's not specifically designed for scientific affiliations but could be adapted for this purpose.

Remember that extracting country information from affiliations can be challenging due to the variety of formats and potential ambiguities. You may need to refine and customize any solution to fit your specific dataset and requirements.

Citations:
[1] https://stackoverflow.com/questions/61781079/extracting-country-name-from-dataframe-column-python
[2] https://www.geeksforgeeks.org/python-program-to-get-country-information/
[3] https://github.com/jpruiz84/ScientoPy
[4] https://stackoverflow.com/questions/5318076/extracting-country-name-from-author-affiliations
[5] https://api-lab.dimensions.ai/cookbooks/7-researchers/Researchers-Search-tips-V2.html
[6] https://groups.google.com/g/zotero-dev/c/oGwTXNOZh28
[7] https://www.linkedin.com/advice/3/how-can-you-extract-author-affiliation-data-from-academic-ksquf
[8] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0244918

## What is GROTOAP2 dataset?
GROTOAP2 (GROund TruthOAP 2) is a dataset used for training and evaluating models in document layout analysis and information extraction from scientific papers. Here are the key details about GROTOAP2:

1. Purpose: It's designed for tasks related to extracting structured information from scientific articles, particularly focusing on layout analysis and metadata extraction[1][2].

2. Content: The dataset consists of scientific papers, primarily from the life sciences domain[1].

3. Size: GROTOAP2 contains approximately 119,000 documents, split into training (83,000), development (18,000), and test (18,000) sets[1].

4. Annotation: The documents in GROTOAP2 are automatically annotated, providing labels for various elements of the paper's structure and content[1].

5. Format: Originally, the dataset was in TrueViz XML format. However, it has been modified to include visual layout information and converted to a format compatible with HuggingFace Datasets[1].

6. Categories: GROTOAP2 includes 22 different categories for labeling document elements[1].

7. Preprocessing: Various preprocessing scripts and tools are available to convert the GROTOAP2 XML documents into formats suitable for machine learning tasks, such as TFRecords[2].

8. Availability: The dataset can be downloaded, and there are instructions provided for accessing the source PDFs[1].

GROTOAP2 is widely used in research related to document understanding, particularly for tasks involving the extraction of metadata and structural information from scientific papers. It serves as a valuable resource for developing and evaluating models in this domain.

Citations:
[1] https://github.com/allenai/vila/blob/main/datasets/README.md
[2] https://github.com/mmcmahon13/deep-metadata-extraction
[3] https://api-lab.dimensions.ai/cookbooks/7-researchers/Researchers-Search-tips-V2.html
[4] https://github.com/jpruiz84/ScientoPy
[5] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0244918
[6] https://www.comp.nus.edu.sg/~kanmy/papers/jcdl2013.pdf
[7] https://groups.google.com/g/zotero-dev/c/oGwTXNOZh28
[8] https://www.linkedin.com/advice/3/how-can-you-extract-author-affiliation-data-from-academic-ksquf