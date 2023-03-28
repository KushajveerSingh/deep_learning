# dowload_conference_papers
Python scripts to download conference papers as PDFs
- [CVPR 2021](scripts/cvpr_2021.py)
- [ICLR 2021](scripts/iclr_2021.py)
- [ECCV 2020](scripts/eccv_2020.py)
- [CVPR 2020](scripts/cvpr_2020.py)

### Directory structure
```
├── download_urls
│   ├── cvpr_2021.csv
├── html
│   ├── cvpr_2021.html
└── scripts
    ├── cvpr_2021.py
    └── utils.py
```
- [download_urls](download_urls)\
    Contains `csv` files for each conference with name of the paper and the corresponding url for the PDF of the paper.

    ```
    title                                                url
    1000_Invertible_Denoising_Network__A_Light_Sol...  https://openaccess.thecvf.com/content/CVPR2021...
    1001_Greedy_Hierarchical_Variational_Autoencod...  https://openaccess.thecvf.com/content/CVPR2021...
    ```

    The titles of the paper have been preprocessing using the following code
    ```python
    def get_title(title, index):
    title = title.strip()
    return str(index) + '_' + title.replace(' ', '_').\
        replace('/', '_').replace('?', '_').replace(':', '_')+'.pdf'
    ```

    This ensures that the name of the paper can be used to directly save the PDF to disk. Each papers is also appended with a four digit number starting from 1000. This is only used to sort the papers, so they are in the same order in the download directory as they are in the HTML file.

- [html](html)\
    Contains the HTML file(s) of the conference to scrape the data from

- [scripts](scripts)\
    Python scripts to downlaod the conference papers. For each script you can modify the following parameters at the start of the script.
    ```python
    SAVE_DIR = f"../cvpr_2021"
    NUM_WORKERS = 8
    ```

    Then you can run the python script to download the papers to the specified `SAVE_DIR`. `NUM_WORKERS` specifies the number of threads to use to download the papers. Set this value to the number of threads on your CPU for maximum performance.
    ```
    python cvpr_2020.py
    ```

- [scripts/utils.py](scripts/utils.py)\
    Utility functions used by the scripts. The provided functions are listed below and the documentation of each function can be checked on how to use the function.

    - `get_soup`- Read HTML file and return `bs4.BeautifulSoup` object. Optionally you can also provide `start_html` and `end_html` to filter the HTML file before passing to `bs4`
    - `get_soups`- Returns a list of `bs4.BeautifulSoup` objects in case there are multiple HTML files for a conference. Internally, it calls `get_soup` and you can pass `start_html` and `end_html` also.
    - `get_title`- Code to replace special characters in the title of a paper with underscore and append the title with a four digit index
    - `save_csv_file`- Saves titles and urls to csv file
    - `download_papers`- Reads in titles and urls and downloads the papers in parallel
    - `download_papers_from_csv`- Titles and urls and read from a csv file and then `download_papers` is called to download the papers

### Requirements
- Python
- Beautiful Soup
- Pandas

### License
[Apache License v2](LICENSE)