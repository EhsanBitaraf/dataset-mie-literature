 Decoding MIE: A Novel Dataset Approach Using Topic Extraction and Affiliation Mining

# Introduction
In the rapidly evolving landscape of artificial intelligence (AI), the role of high-quality, diverse datasets cannot be overstated. These datasets serve as the foundation upon which AI models are built, trained, and refined, ultimately shaping the capabilities and performance of AI systems across various domains [1](https://dl.acm.org/doi/10.1145/3461702.3462590)[2](https://www.mdpi.com/2076-3417/13/12/7082). The medical field, in particular, stands to benefit immensely from the application of AI, with potential improvements in diagnosis, treatment planning, and healthcare management [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8285156/).

The Medical Informatics Europe (MIE) Conference, a cornerstone event in the field of medical informatics, generates a wealth of valuable scientific content annually. However, the sheer volume of articles presented at such conferences poses a significant challenge for researchers and practitioners attempting to extract meaningful insights and identify emerging trends [1](https://pubmed.ncbi.nlm.nih.gov/34584329/). This challenge underscores the need for sophisticated tools and methodologies to analyze and synthesize large volumes of scientific literature effectively [1](https://www.nature.com/articles/nj7612-457a).

In response to this need, we present a novel dataset derived from the MIE Conference proceedings, processed using advanced techniques such as topic extraction and affiliation mining. This dataset not only exemplifies the power of open-source data in driving scientific progress but also demonstrates the potential of intelligent tools in managing and analyzing vast amounts of scientific information.

By making datasets freely available to the research community, we foster collaboration, encourage reproducibility, and accelerate the pace of innovation [1](https://pubmed.ncbi.nlm.nih.gov/21738610/). Open-source datasets democratize access to valuable information, enabling researchers from diverse backgrounds to contribute to the advancement of AI and its applications in fields like medical informatics [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9715297/).

Furthermore, the application of smart tools for analyzing scientific articles across various disciplines has become increasingly crucial. As the volume of published research continues to grow exponentially, traditional manual methods of literature review and synthesis become increasingly untenable [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10335470/). Advanced techniques such as natural language processing, machine learning, and data mining offer powerful means to extract key insights, identify patterns, and uncover hidden relationships within large corpora of scientific literature [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10335470/).

This paper presents a comprehensive overview of our dataset preparation process. It details the methodologies employed in topic extraction and affiliation mining. By providing this dataset and elaborating our approach, we aim to contribute to the broader scientific community's efforts in leveraging AI for knowledge discovery and synthesis in the field of medical informatics.

# Related Work
In the realm of data-driven research, several notable datasets have significantly contributed to advancing various scientific fields. This section highlights key datasets that have set benchmarks in their respective domains, providing a context for the novel dataset approach used in our study.

## CORD-19

The COVID-19 Open Research Dataset (CORD-19) is a comprehensive collection of over 200,000 research papers on COVID-19 curated by the Allen Institute for AI. This dataset has been instrumental in facilitating rapid scientific discovery and understanding of the COVID-19 pandemic by providing researchers with a rich repository of scholarly articles for text mining and data analysis. The extensive use of CORD-19 underscores the importance of well-curated datasets in addressing global health crises [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7251955/).

## S2ORC (Semantic Scholar Open Research Corpus)

S2ORC is another significant dataset, consisting of a vast collection of research papers across various scientific disciplines. This open research corpus is designed to support large-scale text mining and natural language processing (NLP) tasks, enabling researchers to explore and analyze scientific literature comprehensively. S2ORC's broad scope and accessibility make it a valuable resource for advancing scientific research and innovation [1](https://aclanthology.org/2020.acl-main.447/).

## ScisummNet

ScisummNet is a specialized dataset focused on summarizing scientific papers. It provides annotated summaries of research articles, which are crucial for developing and evaluating automatic summarization algorithms. By offering a structured approach to summarizing scientific literature, ScisummNet aids in enhancing the efficiency and accuracy of information retrieval in academic research [1](https://arxiv.org/pdf/1909.01716).

## TaeC

The TaeC dataset is a manually annotated text dataset designed for trait and phenotype extraction and entity linking in wheat breeding literature. This dataset supports the agricultural research community by providing detailed annotations that facilitate the extraction of valuable information related to wheat traits and phenotypes, thereby advancing the field of plant breeding and genetics [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11175518/).

## MPI-LIT

MPI-LIT is a literature-curated dataset of microbial binary protein-protein interactions. This dataset is beneficial for researchers studying microbial interactions, as it provides curated information on protein interactions, which is critical for understanding microbial functions and developing new biotechnological applications [1](https://pubmed.ncbi.nlm.nih.gov/18786976/).




# Methodology

In this study, we employed a structured and multi-stage approach to collect, process, and prepare a comprehensive dataset of articles from the Medical Informatics Europe (MIE) Conference. The primary tool used for this process was the Triple-A software [1](https://ieeexplore.ieee.org/document/10139229), which facilitated data retrieval and preprocessing. This section outlines the various steps involved in constructing the dataset, including metadata acquisition, affiliation mining, and topic extraction.

## Data Acquisition

We began by sourcing the metadata for the articles from the PubMed database, utilizing the Triple-A tool to streamline the extraction process. Our initial query targeted all publications within the journal series "Studies in Health Technology and Informatics" (Stud Health Technol Inform), which regularly publishes MIE conference proceedings. This ensured we captured a wide range of articles, from which we could later refine the dataset. 

To focus specifically on MIE conference papers, we filtered out irrelevant volumes that did not correspond to MIE-related events. This step ensured that the dataset was centered around contributions presented at the MIE Conference, maintaining a consistent scope for further analysis.


| Tag | Volume | Published Year | Place |
| --- | --- | --- | --- |
| MIE2023 | 302 | 2023 | Gothenburg, Sweden |
| MIE2022 | 294 | 2022 | Nice, France |
| MIE2021 | 281 | 2021 | Athens, Greece (e-Conference) |
| MIE2020 | 270 | 2020 | Geneva, Switzerland |
| MIE2018 | 247 | 2018 | Gothenburg, Sweden |
| MIE2017 | 235 | 2017 | Manchester, UK |
| MIE2016 | 228 | 2016 | (@HEC2016) – Munich, Germany |
| MIE2015 | 210 | 2015 | Madrid, Spain |
| MIE2014 | 205 | 2014 | Istanbul, Turkey |
| MIE2012 | 180 | 2012 | Pisa, Italy |
| MIE2011 | 169 | 2011 | Oslo, Norway |
| MIE2009 | 150 | 2009 | Sarajevo, Bosnia-Herzegovina |
| MIE2008 | 136 | 2008 | Gothenburg, Sweden |
| MIE2006 | 124 | 2006 | Maastricht, Netherlands |
| MIE2005 | 116 | 2005 | Geneva, Switzerland |
| MIE2003 | 95  | 2003 | Sant Malo, France |
| MIE2002 | 90  | 2002 | Budapest, Hungary |
| MIE2000 | 77  | 2000 | Hanover, Germany |
| MIE1999 | 68  | 1999 | Ljubljana, Slovenia |
| MIE1997 | 43  | 1997 | Thessaloniki, Greece |
| MIE1996 | 34  | 1996 | Copenhagen, Denmark |


## Affiliation Mining

<br>

---

⚠️ **WARNING:** It should be explained more about what it is and then reference should be made and then reference should be made to the hobby kit that we used. ⚠️

---

<br>

Once the relevant articles were identified, we conducted a detailed analysis of the affiliation metadata. For this task, we implemented a fast and efficient parser designed for MEDLINE and PubMed Open Access data, which enabled us to extract key elements from the affiliation strings. This process allowed us to systematically retrieve multiple fields, including:

- Department
- Affiliation (institution)
- Location
- Country
- Email address
- Zip code

Additionally, we utilized an affiliation-matching function that cross-referenced the extracted affiliation data with the Global Research Identifier Database (GRID) [1](https://www.grid.ac/). This step improved the consistency and accuracy of the institutional affiliations, ensuring that the dataset was robust for further institutional and geographic analysis.

## Topic Extraction

For topic extraction, we applied the TextRank algorithm [1](https://aclanthology.org/W04-3252/), a graph-based natural language processing (NLP) technique well-suited for unsupervised keyword and sentence extraction. TextRank operates by constructing a graph where the nodes represent words or sentences, and edges represent relationships between them based on co-occurrence. By identifying the most important nodes in this graph, TextRank effectively extracts key topics without the need for labeled training data. This algorithm was particularly beneficial for our dataset as it allowed us to extract relevant topics from articles spanning various languages and medical informatics domains, making the method adaptable and scalable across different contexts.

## Data Output and Formatting

The final dataset was prepared in multiple formats to maximize usability and accessibility for a broad range of users. The primary output was structured in JSON format, allowing for flexibility in data handling and compatibility with various applications. In addition, a CSV version of the dataset was generated to ensure ease of use for researchers and practitioners who may prefer more traditional tabular formats. This dual-format approach ensures that the dataset can be easily integrated into a variety of workflows, enhancing its utility for downstream analysis.


# Value of the Data

The Medical Informatics Europe (MIE) Conference dataset presented in this article offers significant value to researchers, practitioners, and policymakers in the field of medical informatics. The following points highlight the key benefits and potential applications of this dataset:

1. **Longitudinal Analysis of Medical Informatics Trends**:
   - The dataset, covering MIE conferences from 1997 onwards, enables researchers to track the evolution of medical informatics over three decades.
   - Temporal analysis can reveal shifting focus areas, emerging topics, and the lifecycle of various subfields within medical informatics.

2. **Topic Modeling and Content Analysis**:
   - The inclusion of extracted topics for each article facilitates in-depth content analysis without the need for full-text processing.
   - Researchers can identify popular themes, track the emergence of new concepts, and analyze the interconnections between different areas of medical informatics.

3. **Bibliometric Studies**:
   - Citation counts and publication details allow for comprehensive bibliometric analyses.
   - Researchers can identify influential papers, authors, and institutions in the field of medical informatics.
   - The data supports studies on citation patterns, impact assessment, and the diffusion of ideas within the community.

4. **Collaboration Network Analysis**:
   - Author information and affiliation data enable the construction and analysis of collaboration networks.
   - Researchers can study patterns of international collaboration, institutional partnerships, and the role of key individuals in shaping the field.

5. **Geographical Distribution of Research**:
   - The affiliation mining results, particularly the country and institution information, allow for geographical analysis of medical informatics research.
   - This data can inform policy decisions related to research funding, educational programs, and international collaborations.

6. **Curriculum Development and Education**:
   - The dataset provides a comprehensive overview of topics in medical informatics, which can be valuable for developing or updating educational curricula.
   - Educators can use the data to ensure that their teaching reflects current trends and important historical developments in the field.

7. **Industry and Technology Tracking**:
   - By analyzing the topics and keywords over time, the dataset can provide insights into the adoption and impact of various technologies in healthcare informatics.
   - This information is valuable for industry stakeholders, technology developers, and healthcare organizations planning IT investments.

8. **Research Gap Identification**:
   - By mapping the landscape of published work, researchers can identify underexplored areas or topics that warrant further investigation.
   - This can guide future research directions and funding allocations in the field of medical informatics.

9. **Conference Impact Assessment**:
   - The dataset allows for analysis of the MIE conference's impact on the field of medical informatics over time.
   - Organizers and sponsors can use this information to assess the conference's role in shaping the discipline and to plan future events.

10. **Natural Language Processing (NLP) and Machine Learning Applications**:
    - The structured nature of the dataset, with extracted topics and keywords, makes it an excellent resource for training and testing NLP and machine learning models focused on medical informatics literature.

11. **Interdisciplinary Research Opportunities**:
    - The dataset can facilitate studies at the intersection of medical informatics with other fields such as computer science, healthcare management, and public health.
    - Researchers from various disciplines can use this data to understand how their field intersects with medical informatics.

12. **Policy and Funding Impact Analysis**:
    - By correlating the dataset with information on research funding and policy initiatives, analysts can study the impact of various interventions on the field of medical informatics.

This dataset represents a valuable resource for the medical informatics community and related fields. Its comprehensive nature, combining bibliometric data with advanced topic extraction and affiliation mining, provides a unique opportunity for multifaceted analyses. As the field of medical informatics continues to evolve rapidly, this dataset offers a solid foundation for understanding its historical development and current state, while also providing insights that can shape its future direction.


# Dataset Description
The dataset described in this article comprises a single JSON file containing detailed information about articles presented at the Medical Informatics Europe (MIE) Conference. This dataset was collected using the Triple-A tool and further enhanced through advanced techniques such as topic extraction and affiliation mining.



## File Structure

The JSON file contains a list of objects, where each object represents a single article and includes various fields of information. Below is an example of the structure for a single article entry:

```json
{
    "title": "Using an open source observational tool ....",
    "year": "2009",
    "publisher": "Studies in health technology and informatics",
    "journal_issn": "0926-9630",
    "journal_iso_abbreviation": "Stud Health Technol Inform",
    "language": "eng",
    "url": "https://pubmed.ncbi.nlm.nih.gov/19745467/",
    "doi": "",
    "pmid": "19745467",
    "citation_count": 4,
    "IOSPressVolume": "150",
    "publication_type": [
        "Journal Article"
    ],
    "authors": [
        "De Lusignan, S",
        "Kumarapeli, P",
        "Debar, S",
        "Kushniruk, A",
        "Pearce, C"
    ],
    "keywords": [
        "Attitude to Computers",
        "Computer Systems",
        "Decision Making",
        "Education",
        "Family Practice",
        "Humans",
        "\"Medical Records Systems, Computerize\"",
        "Observation",
        "\"Outcome and Process Assessment, Health Car\"",
        "Physician-Patient Relations",
        "Referral and Consultation",
        "Video Recording"
    ],
    "topics": [
        "EPR systems",
        "consultation",
        "primary care computer systems",
        "EPR",
        "computer use",
        "considerable variation",
        "the computer mediated consultation",
        "functionality",
        "psychiatry",
        "a simulated clinical consultation"
    ],
    "affiliation_integration_country": [
        "united kingdom"
    ],
    "affiliation_integration_department": [
        ""
    ],
    "affiliation_integration_institution": [
        "St George's University of London"
    ]
}
```

## Field Descriptions

Each article entry in the dataset contains the following fields:

| Field | Description |
|-------|-------------|
| title | The full title of the article |
| year | The publication year of the article |
| publisher | The name of the publisher or journal |
| journal_issn | The International Standard Serial Number (ISSN) of the journal |
| journal_iso_abbreviation | The standardized abbreviation of the journal name |
| language | The language of the article (e.g., "eng" for English) |
| url | The URL link to the article, typically on PubMed |
| doi | The Digital Object Identifier of the article, if available |
| pmid | The PubMed ID of the article |
| citation_count | The number of times the article has been cited |
| IOSPressVolume | The volume number in the IOS Press publication series |
| publication_type | The type of publication (e.g., "Journal Article") |
| authors | A list of the authors' names |
| keywords | A list of keywords associated with the article in PubMed |
| topics | The first 10 topics extracted through an unsupervised topic extraction mechanism |
| affiliation_integration_country | The countries associated with the authors' affiliations, extracted using the described algorithm |
| affiliation_integration_department | The departments associated with the authors' affiliations, if available |
| affiliation_integration_institution | The institutions associated with the authors' affiliations |

## Data Processing and Enhancement

This dataset has been enriched through several advanced techniques:

1. **Topic Extraction**: An unsupervised topic extraction mechanism was applied to identify the most relevant topics for each article. The 'topics' field lists the top 10 extracted topics, providing a quick overview of the article's content without relying solely on author-provided keywords.

2. **Affiliation Mining**: An algorithm was developed to extract and standardize information about authors' affiliations. This process resulted in the 'affiliation_integration_country', 'affiliation_integration_department', and 'affiliation_integration_institution' fields, which provide valuable insights into the geographical and institutional distribution of research in medical informatics.

3. **Bibliometric Data**: The inclusion of citation counts and publication details allows for bibliometric analyses, enabling researchers to identify influential papers and trends in the field.

This comprehensive dataset offers a rich resource for researchers interested in the evolution of medical informatics, collaboration patterns, and trending topics in the field. The combination of bibliometric data, extracted topics, and standardized affiliation information provides multiple avenues for analysis and insights into the MIE conference contributions over time.


# Results

The analysis of the Medical Informatics Europe (MIE) Conference dataset, prepared using the Triple-A tool and enhanced with topic extraction and affiliation mining techniques, revealed several interesting patterns and characteristics.

## Dataset Composition

The dataset comprises a total of 3,459 articles from the MIE Conference proceedings. This substantial corpus provides a comprehensive view of the research trends and developments in medical informatics over the years covered by the dataset.

## Digital Object Identifier (DOI) Assignment

A notable trend in the dataset is the inconsistent assignment of Digital Object Identifiers (DOIs) across the years. As illustrated in Figure 1, only articles from the most recent three years consistently included DOIs in their metadata. This observation highlights the evolving practices in digital article identification and the gradual adoption of DOIs in the field of medical informatics.

![Figure 1: "Articles with and without DOI by Year"](/output/Articles%20with%20and%20without%20DOI%20by%20Year.png)

[Figure 1: "Articles with and without DOI by Year"]

<br>

---

⚠️ **WARNING:** Using this approach we extracted ... papers leading to ... metadata, ... affiliations, and ... topics. As we delved deeper into the dataset analysis, we observed that while certain articles lacked a DOI on PubMed, they were associated with a DOI on the IOS Press website. However, a significant challenge lies in the absence of a systematic approach to access this metadata from IOS Press. For instance, consider PMID: 25160183. ⚠️

---

<br>

## Citation Patterns

The analysis of citation data, extracted from PubMed metadata, reveals varying levels of scholarly impact across the years. Figure 2 presents a year-wise breakdown of articles that have received at least one citation versus those that remain uncited.

![Figure 2: "Articles with No Citations vs At Least One Citation by Year"](/output/Articles%20with%20No%20Citations%20vs%20At%20Least%20One%20Citation%20by%20Year.png)

[Figure 2: "Articles with No Citations vs At Least One Citation by Year"]

This visualization provides insights into the influence and reach of MIE Conference publications over time, potentially reflecting changes in research focus, quality, or dissemination strategies.

## Authorship Anomalies

An unexpected finding in the dataset pertains to authorship information. As shown in Figure 3, a number of articles across various years were found to have no authors attributed to them.

![Figure 3: "Articles with No Authors vs At Least One Author by Year"](/output/Articles%20with%20No%20Authors%20vs%20At%20Least%20One%20Author%20by%20Year.png)

[Figure 3: "Articles with No Authors vs At Least One Author by Year"]

This anomaly appears to be related to the indexing practices of PubMed, particularly for conference proceedings. For instance, in 1996, the entire conference book was saved as a single information field in PubMed, leading to inconsistencies in individual article metadata. This observation underscores the challenges in standardizing bibliographic data for conference proceedings and highlights the need for careful data cleaning and validation in bibliometric studies.


<br>

---

⚠️ **WARNING:** Bring some pictures and examples for it ⚠️

---

<br>

## Language of Publications

While English has been the primary language of the MIE Conference, our analysis revealed an interesting deviation in the year 2000. As depicted in Figure 4, a small number of articles were accepted in German during this year.

![Figure 4: "English vs Non-English Articles by Year"](/output/English%20vs%20Non-English%20Articles%20by%20Year.png)

[Figure 4: "English vs Non-English Articles by Year"]

This finding provides an intriguing glimpse into the conference's language policies and potential efforts to accommodate non-English speaking researchers. It also raises questions about the impact of language diversity on the dissemination and accessibility of research in the field of medical informatics.

In conclusion, these results offer valuable insights into the characteristics and evolution of the MIE Conference dataset. The observed patterns in DOI assignment, citation trends, authorship anomalies, and language diversity not only inform our understanding of the dataset itself but also reflect broader trends in medical informatics research and academic publishing practices over the years.





# Limitations

While the dataset presented in this article offers valuable insights into the Medical Informatics Europe (MIE) Conference proceedings, it is important to acknowledge several limitations that may impact its comprehensiveness and applicability:

1. **Incomplete Conference Coverage**: 
   - Not all EFMI MIE conferences are published in IOS Press or indexed in PubMed.
   - This limitation results in a partial representation of the complete MIE conference history.
   - Researchers should be aware that some conferences and their associated papers may be missing from this dataset.

2. **Temporal Constraints**:
   - The dataset covers MIE conferences from 1994 onwards.
   - This limitation is due to the availability of data through the PubMed API and the capabilities of the TripleA program used for data collection.
   - Earlier conferences (pre-1994) are not represented in this dataset, potentially omitting historical trends and developments in the field of medical informatics.

3. **Data Source Dependence**:
   - The dataset relies primarily on PubMed indexing and the PubMed API for data retrieval.
   - Papers or conferences not indexed in PubMed are consequently excluded from the dataset.
   - This dependence may introduce a bias towards certain types of publications or research areas that are more likely to be indexed in PubMed.

4. **Affiliation Data Limitations**:
   - The affiliation mining algorithm, while advanced, may not capture all nuances of institutional affiliations.
   - There might be inconsistencies or missing data in the affiliation fields, especially for older publications or those with complex multi-institutional collaborations.

5. **Topic Extraction Constraints**:
   - The unsupervised topic extraction mechanism, while powerful, may not always accurately represent the full scope of an article's content.
   - The limitation to the top 10 topics per article might oversimplify the research focus, especially for interdisciplinary or complex studies.

6. **Citation Count Timeliness**:
   - Citation counts are subject to the update frequency of the PubMed database and may not reflect the most current impact of the articles.
   - Newer articles may have lower citation counts due to the time lag in accumulating citations, potentially underrepresenting their importance or impact.

7. **Language Bias**:
   - While the dataset includes a 'language' field, it predominantly contains English-language publications due to PubMed's indexing practices.
   - This may underrepresent research published in other languages, potentially missing important contributions from non-English speaking regions.

8. **Metadata Completeness**:
   - Some fields, such as 'doi' or 'affiliation_integration_department', may be incomplete for certain entries, limiting the ability to perform comprehensive analyses across all dimensions of the dataset.

These limitations should be carefully considered when using this dataset for research or analysis purposes. While the dataset provides a valuable resource for studying trends and developments in medical informatics through the lens of MIE conferences, users should be aware of its scope and potential biases. Future work could focus on addressing these limitations by incorporating additional data sources, extending the temporal coverage, and refining the data processing techniques.


# Conclusion

The Medical Informatics Europe (MIE) Conference dataset presented in this article represents a significant contribution to the field of medical informatics. By compiling and enhancing data from MIE conferences since 1994, this dataset offers a unique and comprehensive resource for researchers, educators, policymakers, and industry professionals.

Key aspects of this dataset include:

1. **Comprehensive Coverage**: Despite some limitations, the dataset provides a broad overview of MIE conferences from 1994 onwards, offering insights into the evolution of medical informatics over nearly three decades.

2. **Advanced Data Processing**: The application of topic extraction and affiliation mining techniques has enriched the raw bibliometric data, providing additional layers of information for analysis.

3. **Multifaceted Information**: Each entry in the dataset contains a wealth of information, including bibliometric details, extracted topics, author information, and standardized affiliation data.

The value of this dataset lies in its potential to facilitate a wide range of analyses and applications:

- Longitudinal studies of trends in medical informatics
- Bibliometric analyses to identify influential works and authors
- Collaboration network mapping and geographical distribution of research
- Topic modeling to track the emergence and evolution of key themes in the field
- Curriculum development and educational planning
- Industry and technology trend analysis
- Identification of research gaps and future directions

While acknowledging limitations such as incomplete conference coverage and temporal constraints, this dataset nonetheless represents a valuable resource for the medical informatics community. Its comprehensive nature allows for multifaceted analyses that can provide insights into the historical development, current state, and future directions of the field.

The potential applications of this dataset extend beyond academic research. It can inform policy decisions, guide funding allocations, assist in conference planning, and help bridge the gap between academia and industry in the rapidly evolving field of medical informatics.

As the healthcare sector continues to digitize and the role of informatics in medicine grows, datasets like this one become increasingly valuable. They provide a foundation for understanding the field's trajectory and can help shape its future direction. By making this dataset available, we aim to foster collaboration, innovation, and progress in medical informatics.

Future work could focus on expanding the dataset to include more recent conferences, incorporating additional data sources to address current limitations, and developing tools to facilitate easier analysis and visualization of the data. We encourage the research community to utilize this resource and build upon it, potentially leading to new insights and advancements in the field of medical informatics.

In conclusion, this MIE conference dataset represents a significant contribution to the medical informatics community. It not only provides a window into the history and evolution of the field but also serves as a springboard for future research, collaboration, and innovation. As we continue to navigate the complex intersection of healthcare and technology, resources like this dataset will play a crucial role in shaping our understanding and guiding our progress.

# Ethics Statement
The current work does not involve human subjects, animal experiments, or any data collected from social media platforms.


# Data Availability

The data is available in json format on the figshare platform with DOI 172609283 in this [link](https://figshare.com/).