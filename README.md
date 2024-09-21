# Dataset MIE Literature

Export from \notingithub\bibliometric-ios-press-ebook


under construction


<br>

---

⚠️ **WARNING:** This experimental project is under rapid development and lacks basic safeguards. Until a stable `1.0` release, **ONLY** run this repository on devices without sensitive information or access to paid services. ⚠️

---

<br>

![Repo Size](https://img.shields.io/github/repo-size/mjafarpour87/medical-insights)

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mjafarpour87/medical-insights)

<!-- ![Downloads](https://img.shields.io/github/downloads/mjafarpour87/medical-insights/total) -->


This dataset represents a valuable resource for the medical informatics community and related fields. Its comprehensive nature, combining bibliometric data with advanced topic extraction and affiliation mining, provides a unique opportunity for multifaceted analyses. As the field of medical informatics continues to evolve rapidly, this dataset offers a solid foundation for understanding its historical development and current state, while also providing insights that can shape its future direction.


# How to use

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
|Step 4|step04_extract_volume.py||
|Step 5|step07_create_dataset.py|Export Dataset|


## How to use


under construction

# Article
The [Paper](https://pubmed.ncbi.nlm.nih.gov/39176947/) is accepted and published at MIE 2024. To cite this work:

Bitaraf E, Jafarpour M, Shool S, Saboori Amleshi R. Unveiling Medical Insights: Advanced Topic Extraction from Scientific Articles. Stud Health Technol Inform. 2024 Aug 22;316:944-948. doi: 10.3233/SHTI240566. PMID: 39176947.

# Contributors

[![01 project contributors](https://contrib.rocks/image?repo=mjafarpour87/medical-insights)](https://github.com/mjafarpour87/medical-insights/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

Please see our [contributing guidelines](CONTRIBUTING.md) for more details on how to get involved.

---

# License

THis Repository is available under the [CC0 1.0 Universal](LICENSE).