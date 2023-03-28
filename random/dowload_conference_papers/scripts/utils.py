import multiprocessing
import os
import tqdm
from urllib.request import urlretrieve

import bs4
import pandas as pd

__all__ = ["get_soup", "get_soups", "get_title", "save_csv_file",
           "download_papers", "download_papers_from_csv"]


def get_soup(name, start_html=None, end_html=None):
    if start_html is None and end_html is None:
        return bs4.BeautifulSoup(open(f"../html/{name}.html"), 'html.parser')
    else:
        with open(f"../html/{name}.html", "r") as f:
            html = f.read()

        start_index = html.index(start_html)
        end_index = html.index(end_html)
        html = html[start_index:end_index]
        return bs4.BeautifulSoup(html, 'html.parser')


def get_soups(name, num_html_files, start_html=None, end_html=None):
    path = f"../html/{name}"
    soups = []

    for i in range(1, num_html_files+1):
        if num_html_files <= 9:
            name = f"{path}_0{i}"
        elif num_html_files <= 99:
            name = f"{path}_{i}"
        else:
            raise ValueError("Number of HTML files should be < 100")
        soups.append(get_soup(f"{path}_{i}", start_html, end_html))
    return soups


def get_title(title, index):
    title = title.strip()
    return str(index) + '_' + title.replace(' ', '_').\
        replace('/', '_').replace('?', '_').replace(':', '_')+'.pdf'


def save_csv_file(titles, urls, name):
    info = list(zip(titles, urls))
    df = pd.DataFrame(info, columns=['title', 'url'])
    df.to_csv(f"../download_urls/{name}.csv", index=False)


def _download_papers(info):
    title, url, save_dir = info[0], info[1], info[2]
    save_path = f"{save_dir}/{title}"
    urlretrieve(url, save_path)


def download_papers(titles, urls, save_dir, num_workers=8):
    os.makedirs(save_dir, exist_ok=True)
    info = list(zip(titles, urls, [save_dir]*len(titles)))

    pool = multiprocessing.Pool(processes=num_workers)
    for _ in tqdm.tqdm(pool.imap_unordered(_download_papers, info),
                       total=len(info)):
        pass


def download_papers_from_csv(name, save_dir, num_workers=8):
    df = pd.read_csv(f"../download_urls/{name}.csv")
    titles = df['title'].tolist()
    urls = df['url'].tolist()

    download_papers(titles, urls, save_dir, num_workers)
