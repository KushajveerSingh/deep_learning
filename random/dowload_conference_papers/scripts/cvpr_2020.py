import utils

NAME = "cvpr_2020"
SAVE_DIR = f"../{NAME}"
NUM_WORKERS = 8

soups = utils.get_soups(NAME, 3)

index, titles, urls = 1000, [], []
for soup in soups:
    query = soup.findAll('dt', attrs={'class': 'ptitle'})
    for q in query:
        title = utils.get_title(q.a.text, index)
        index += 1
        titles.append(title)

        url = 'https://openaccess.thecvf.com/content_CVPR_2020/papers/'
        url = url + q.a['href'][23:-4] + 'pdf'
        urls.append(url)

utils.save_csv_file(titles, urls, NAME)

if __name__ == "__main__":
    utils.download_papers(titles, urls, SAVE_DIR, NUM_WORKERS)
