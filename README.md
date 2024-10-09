# Decoding MIE: A Novel Dataset Approach Using Topic Extraction and Affiliation Parsing
![Repo Size](https://img.shields.io/github/repo-size/EhsanBitaraf/dataset-mie-literature)

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/EhsanBitaraf/dataset-mie-literature)


This dataset represents a valuable resource for the medical informatics community and related fields. Its comprehensive nature, combining bibliometric data with advanced topic extraction and affiliation mining, provides a unique opportunity for multifaceted analyses. As the field of medical informatics continues to evolve rapidly, this dataset offers a solid foundation for understanding its historical development and current state, while also providing insights that can shape its future direction.


*Dataset:*  
[![DOI:10.6084/m9.figshare.27174759](https://zenodo.org/badge/doi/10.6084/m9.figshare.27174759.svg)](https://doi.org/10.6084/m9.figshare.27174759)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This dataset contains 4606 articles from 1996 to 2024 that were presented in MIE (Medical Informatics Europe Conference) conferences. This data was extracted from PubMed and topic extraction and affiliation parsing were done on it.


# How to Use

You can access and use the generated dataset through the following [link](https://doi.org/10.6084/m9.figshare.27174759). This dataset contains valuable information for further analysis. Additionally, you can load the dataset directly in your Python environment using the following code snippet:

```python
from src.dataset import load_dataset_mie
data = load_dataset_mie()
```

This will load the dataset into the `data` variable for easy access and manipulation in your Python projects.

If you want to update the dataset or generate it from scratch, follow the instructions provided in the ["How to Create"](#how-to-create) section below.

---

## How to Create

To generate the dataset from scratch or update an existing dataset, follow these steps:

### 1. Set Up the Repository

```sh
git clone https://github.com/EhsanBitaraf/dataset-mie-literature.git
```

First, create and activate a Python virtual environment to isolate your project's dependencies:

```sh
python -m venv venv
```

#### For Windows:

```sh
$ .\venv\Scripts\activate
```

#### For Linux/MacOS:

```sh
$ source venv/bin/activate
```

### 2. Install Dependencies

Once your virtual environment is activated, install the required dependencies for the project:

```sh
pip install -r requirements.txt
```

*Note:* 
You can install the latest version of **TripleA** (the tool used for processing and analyzing the data) directly from the GitHub repository using the following command:

```sh
pip install git+https://github.com/EhsanBitaraf/triple-a.git
```

### 3. Configure Environment Variables

To configure the project, you need to set up your environment variables. Copy the `.env.sample` file and rename it to `.env` in the root directory of the project:

```sh
cp .env.sample .env
```

After this, open the `.env` file and configure the necessary variables for your project, such as database connection details, or other settings as needed.


### 4. Setup Database

You can choose between two types of databases for this project:

1. **TinyDB**:  
   TinyDB is a lightweight, document-oriented database suitable for smaller-scale applications. It is simple to set up, as it only requires specifying the file name in the `.env` configuration file. No external server or complex setup is necessary, making it ideal for projects that don’t require heavy database operations.

   To set up **TinyDB**:
   - Define the file name in your `.env` file. (`AAA_TINYDB_FILENAME`)

2. **MongoDB**:  
   For handling larger datasets or more complex data requirements, **MongoDB** is recommended. MongoDB is a widely-used, NoSQL database that scales well for larger applications and provides flexibility in how you store and query data. You can install MongoDB through the official installation [guide](https://www.mongodb.com/docs/manual/installation/).

   To configure **MongoDB** in your project, you'll need to modify two environment variables in the `.env` file:
   - Set `AAA_MONGODB_CONNECTION_URL` to the MongoDB connection string.
   - Set `AAA_MONGODB_DB_NAME` to the name of your MongoDB database.

Both options offer different benefits depending on your project needs. Choose **TinyDB** for simplicity or **MongoDB** for scalability.

### 5. Run Steps

| #  | Step                      | File Name               | Description |
|----|---------------------------|-------------------------|-------------|
| 1  | **Check Configuration**    | `step01_check_config.py` | This step checks the configuration settings of the TripleA system, ensuring all required parameters and configurations are correctly set before running the pipeline. |
| 2  | **Retrieve Papers from PubMed** | `step02_get_pubmed.py`   | In this step, relevant academic papers are retrieved from PubMed using a predefined search strategy. The search utilizes the keywords: `"Stud Health Technol Inform"[jour]` to ensure the content meets minimum quality standards for further processing. |
| 3  | **Run Pipeline**           | `step03_run_pipeline.py` | This step applies the "Triple A" operators to process the metadata and content of the papers. It includes tasks like extracting keywords and MeSH terms from the metadata, performing topic extraction from titles and abstracts using the TextRank algorithm, and conducting affiliation mining. |
| 4  | **Extract Volume Data**    | `step04_extract_volume.py` | This step isolates conference proceedings from the MIE (Medical Informatics Europe) series by filtering the data based on volume numbers specifically associated with MIE conferences. This ensures the data is focused on the target publications. You can find the MIE conference volume information in the following [document](/docs/IOSPressArticles.v.0.2.xlsx). |
| 5  | **Create Dataset**         | `step05_create_dataset.py` | In the final step, the filtered and processed data is exported as a dataset, ready for analysis or other downstream applications. |



# Results

We conducted an initial review of the dataset using [Jupyter Notebook](/dataset-review.ipynb), which provided a general overview of its structure and content. This review helped us understand the key attributes and dimensions of the dataset, allowing us to better analyze and interpret the information it contains.

## Field Descriptions

Each entry in the dataset represents an individual article and contains various fields that provide important metadata and bibliographic details. Below is a description of each field:

| **Field**              | **Description**                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------------|
| `title`                | The full title of the article.                                                                        |
| `year`                 | The publication year of the article.                                                                  |
| `abstract`             | A brief summary of the article’s content.                                                             |
| `journal_issn`         | The International Standard Serial Number (ISSN) of the journal in which the article was published.     |
| `language`             | The language in which the article was written (e.g., `"eng"` for English).                            |
| `doi`                  | The Digital Object Identifier (DOI) of the article, if available.                                     |
| `pmid`                 | The PubMed Identifier (PMID) of the article.                                                          |
| `citation_count`       | The number of times the article has been cited by other works.                                         |
| `IOSPressVolume`       | The volume number of the article in the IOS Press publication series, if applicable.                  |
| `publication_type`     | The type of publication (e.g., `"Journal Article"`, `"Research Support, Non-U.S. Gov't"`). This field based-on [PubMed Publication Type](https://www.nlm.nih.gov/mesh/2019_pubtypes.html)                            |
| `authors`              | A list of authors’ names who contributed to the article.                                              |
| `keywords`             | A list of keywords associated with the article, typically retrieved from PubMed metadata.             |
| `topics`               | The top 10 topics extracted from the article’s title and abstract using an unsupervised topic extraction method. |
| `affiliation_countries`| A list of countries associated with the affiliations of the authors, derived using the [specific algorithm](https://github.com/titipata/affiliation_parser).|
| `affiliations`         | The PubMed affiliations of the article’s authors.                                              |

The dataset is stored in a JSON format, where each article is represented as a JSON object containing these fields. This structure allows for efficient storage, retrieval, and processing of the data. Below is an example of the structure for a single article entry:


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

The dataset comprises a total of **4,606 articles** from the MIE Conference proceedings. A preliminary analysis has been conducted on this dataset, which you can read about in the article available [here](https://arxiv.org/abs/2410.04602). Additionally, you can explore and perform your own analyses using the Jupyter Notebook provided [here](/dataset-review.ipynb). 

The following figures provide insights into various trends within the dataset, including the presence of Digital Object Identifiers (DOIs), authorship information, and language distribution across the articles.

### Figure 1: Articles with and without DOI by Year

![Figure 1: "Articles with and without DOI by Year"](/output/Articles%20with%20and%20without%20DOI%20by%20Year.png)

This figure illustrates the distribution of articles that include a DOI compared to those that do not, broken down by publication year. DOIs are essential for accurately identifying and linking to scholarly works, facilitating access to research for readers and ensuring proper citation. This analysis provides valuable insights into how DOI usage has evolved over time within the dataset.

### Figure 2: Articles with No Authors vs. At Least One Author by Year

![Figure 2: "Articles with No Authors vs At Least One Author by Year"](/output/Articles%20with%20No%20Authors%20vs%20At%20Least%20One%20Author%20by%20Year.png)

This figure compares the number of articles that list no authors with those that have at least one author, segmented by publication year. The presence of authorship is crucial for evaluating the credibility and traceability of academic works. This analysis highlights trends or irregularities in authorship attribution over time. 

**Observation:** Upon initial review, it was noted that articles without listed authors are often book titles from collections indexed in PubMed. Below is an example of such an article.

![Example of Article without Author](/docs/sample-article-without-author.png)

### Figure 3: English vs. Non-English Articles by Year

![Figure 3: "English vs Non-English Articles by Year"](/output/English%20vs%20Non-English%20Articles%20by%20Year.png)

This figure presents a breakdown of articles written in English versus those in other languages, categorized by year. Given that English is the predominant language in academic publishing, this analysis assesses the proportion of articles catering to non-English-speaking audiences and tracks any changes in this trend over the years. 

**Note:** All articles categorized as non-English were published in German. A complete list of these articles can be found [here](/docs/non-english-article.xlsx).

### Figure 4: Affiliation Anomalies

During the analysis of author affiliations, we identified several incomplete affiliations that could not be parsed correctly. Out of the total **4,606 articles**, **1,564** articles exhibited incomplete affiliations, indicating that **33.96%** of the dataset is affected by this issue.

![Figure 4: "Affiliation Anomalies"](/output/Articles%20with%20at%20least%20one%20incomplete%20affiliation%20parsing.png)

These anomalies may impact the overall analysis of the dataset and underscore the importance of comprehensive data collection and validation processes.


# Data Availability
[![DOI:10.6084/m9.figshare.27174759](https://zenodo.org/badge/doi/10.6084/m9.figshare.27174759.svg)](https://doi.org/10.6084/m9.figshare.27174759)


The MIE Dataset is available [here](https://doi.org/10.6084/m9.figshare.27174759) under a CC BY 4.0 license.
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)


## Citing
If you use the MIE dataset in a scientific publication, we would appreciate references to the following [paper](https://arxiv.org/abs/2410.04602):

Biblatex entry:
```latex
@misc{bitaraf2024decodingmienoveldataset,
      title={Decoding MIE: A Novel Dataset Approach Using Topic Extraction and Affiliation Parsing}, 
      author={Ehsan Bitaraf and Maryam Jafarpour},
      year={2024},
      eprint={2410.04602},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2410.04602}, 
}
```

# Contributors

[![01 project contributors](https://contrib.rocks/image?repo=EhsanBitaraf/dataset-mie-literature)](https://github.com/EhsanBitaraf/dataset-mie-literature/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

Please see our [contributing guidelines](CONTRIBUTING.md) for more details on how to get involved.

---

# License

This Repository is available under the [CC0 1.0 Universal](LICENSE).