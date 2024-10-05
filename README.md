# Dataset MIE Literature
![Repo Size](https://img.shields.io/github/repo-size/mjafarpour87/medical-insights)

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mjafarpour87/medical-insights)

<!-- ![Downloads](https://img.shields.io/github/downloads/mjafarpour87/medical-insights/total) -->


This dataset represents a valuable resource for the medical informatics community and related fields. Its comprehensive nature, combining bibliometric data with advanced topic extraction and affiliation mining, provides a unique opportunity for multifaceted analyses. As the field of medical informatics continues to evolve rapidly, this dataset offers a solid foundation for understanding its historical development and current state, while also providing insights that can shape its future direction.


Dataset:
[![DOI:10.6084/m9.figshare.27174759](https://zenodo.org/badge/doi/10.6084/m9.figshare.27174759.svg)](https://doi.org/10.6084/m9.figshare.27174759)

This dataset contains 4606 articles from 1996 to 2024 that were presented in MIE (Medical Informatics Europe Conference) conferences. This data was extracted from PubMed and topic extraction and affiliation parsing were done on it.

# How to use
You can use the dataset generated through this [link](https://doi.org/10.6084/m9.figshare.27174759). In addition, you can use it using the following code in the Python environment
```python
def load_dataset_mie():
    ds_path = DATA_DIR / "dataset-ios.json"


    with open(ds_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data
```

If you want to update the dataset or create it from scratch, follow the instructions in the ["How to create"](#how-to-create) section.

## How to create 

### Setup Repository
```sh
python -m venv venv
```

Windows
```sh
$ .\venv\Scripts\activate
```
Linux
```sh
$ source venv/bin/activate
```

```sh
pip install -r requirements.txt
```
You can install last version of triplea with this command
```sh
pip install git+https://github.com/EhsanBitaraf/triple-a.git
```

### Run steps
|#     |File Name            |Description|
|-|-|-|
|Step 1|step01_check_config.py|Check TripleA Configuration|
|step 2|step02_get_pubmed.py|To retrieve relevant papers with minimum quality content, we used the search strategy keywords: `"Stud Health Technol Inform"[jour]`.|
|Step 3|step03_run_pipline.py|In this step, "Triple A" operators were used to process paper metadata and content at different states, including extracting keywords and MeSH terms from the metadata. Extract topic from abstract and title with method textrank and affiliation mining|
|Step 4|step04_extract_volume.py|To isolate MIE conference proceedings from other publications in the journal series, this step filters the collected data based on volume numbers associated with MIE conferences. This selective approach ensures the dataset's focus and relevance. You can find information about the volume of the MIE conference [here](/docs/IOSPressArticles.v.0.2.xlsx).|
|Step 5|step05_create_dataset.py|Export Dataset|


# Result

We have done the initial review of the dataset using [Jupyter Notebook](/dataset-review.ipynb), which shows us the general outline of it.

## Field Descriptions

Each article entry in the dataset contains the following fields:

| Field | Description |
|-------|-------------|
| title | The full title of the article |
| year | The publication year of the article |
| abstract | The abstract of the article |
| journal_issn | The International Standard Serial Number (ISSN) of the journal |
| language | The language of the article (e.g., "eng" for English) |
| doi | The Digital Object Identifier of the article, if available |
| pmid | The PubMed ID of the article |
| citation_count | The number of times the article has been cited |
| IOSPressVolume | The volume number in the IOS Press publication series |
| publication_type | The type of publication (e.g., "Journal Article") |
| authors | A list of the authors' names |
| keywords | A list of keywords associated with the article in PubMed |
| topics | The first 10 topics extracted through an unsupervised topic extraction mechanism |
| affiliation_countries | The countries associated with the authors' affiliations, extracted using the described algorithm |
| affiliations | The list of authors' affiliations |

The JSON file contains a list of objects, where each object represents a single article and includes various fields of information. Below is an example of the structure for a single article entry:


```json
[
    {
        "title": "Validation of Multiple Path Translation for SNOMED CT Localisation.",
        "year": "2022",
        "journal_issn": "1879-8365",
        "language": "eng",
        "abstract": "The MTP (multiple translation paths) approach supports human translators in clinical terminology localization. It exploits the results of web-based machine translation tools and generates, for a chosen target language, a scored output of translation candidates for each input terminology code. We present first results of a validation, using four SNOMED CT benchmarks and three translation engines. For German as target language, there was a significant advantage of MTP as a generator of plausible translation candidate lists, and a moderate advantage of the top-ranked MTP translation candidate over single best performing direct-translation approaches.",
        "doi": "10.3233/SHTI220641",
        "pmid": "35612259",
        "citation_count": 0,
        "IOSPressVolume": "294",
        "publication_type": [
            "Journal Article"
        ],
        "authors": [
            "Schulz, S",
            "Boeker, M",
            "Prunotto, A"
        ],
        "keywords": [
            "Ethnicity",
            "Humans",
            "Language",
            "Systematized Nomenclature of Medicine",
            "Translations",
            "Machine Translation",
            "NLP",
            "SNOMED CT"
        ],
        "topics": [
            "translation candidates",
            "plausible translation candidate lists",
            "clinical terminology localization",
            "multiple translation paths",
            "human translators",
            "SNOMED CT Localisation",
            "target language",
            "approach",
            "web-based machine translation tools",
            "single best performing direct-translation approaches"
        ],
        "affiliation_countries": [
            "austria",
            "germany"
        ],
        "affiliations": [
            "IMI, Medical University of Graz, Austria.",
            "Institute for AI in Healthcare, Technical University of Munich, Germany."
        ]
    }
]
```

## Analysis

![Figure 1: "Articles with and without DOI by Year"](/output/Articles%20with%20and%20without%20DOI%20by%20Year.png)

Figure : "Articles with and without DOI by Year"

![Figure 3: "Articles with No Authors vs At Least One Author by Year"](/output/Articles%20with%20No%20Authors%20vs%20At%20Least%20One%20Author%20by%20Year.png)

Figure : "Articles with No Authors vs At Least One Author by Year"

![Figure 4: "English vs Non-English Articles by Year"](/output/English%20vs%20Non-English%20Articles%20by%20Year.png)

Figure : "English vs Non-English Articles by Year"

# Data Availability
[![DOI:10.6084/m9.figshare.27174759](https://zenodo.org/badge/doi/10.6084/m9.figshare.27174759.svg)](https://doi.org/10.6084/m9.figshare.27174759)


The MIE Dataset is available [here](https://doi.org/10.6084/m9.figshare.27174759) under a CC BY 4.0 license.
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


## Citing
If you use the MIE dataset in a scientific publication, we would appreciate references to the following paper:

Biblatex entry:
```latex

```

# Contributors

[![01 project contributors](https://contrib.rocks/image?repo=mjafarpour87/medical-insights)](https://github.com/mjafarpour87/medical-insights/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

Please see our [contributing guidelines](CONTRIBUTING.md) for more details on how to get involved.

---

# License

This Repository is available under the [CC0 1.0 Universal](LICENSE).