import utils

NAME = "cvpr_2021"
SAVE_DIR = f"../{NAME}"
NUM_WORKERS = 8

soup = utils.get_soup(NAME)
soup = soup.findAll('div', attrs={'id': 'content'})[0]

query = soup.findAll('dt', attrs={'class': 'ptitle'})

index, titles, urls = 1000, [], []
for q in query:
    title = utils.get_title(q.text, index)
    index += 1
    titles.append(title)

    url = "https://openaccess.thecvf.com/content/CVPR2021/papers/"
    url = url + q.a['href'].split('html/')[-1]
    url = url[:-4]
    url = url + "pdf"
    urls.append(url)

utils.save_csv_file(titles, urls, NAME)

if __name__ == "__main__":
    utils.download_papers(titles, urls, SAVE_DIR, NUM_WORKERS)
