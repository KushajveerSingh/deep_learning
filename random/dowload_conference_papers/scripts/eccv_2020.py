import utils

NAME = "eccv_2020"
SAVE_DIR = f"../{NAME}"
NUM_WORKERS = 8

start_html = r"""
<dt class="ptitle"><br>
<a href=papers/eccv_2020/papers_ECCV/html/267_ECCV_2020_paper.php>
"""
end_html = "</dl> </div>\n	</div>\n\n\n	<!-- ECCV 2018 -->"

soup = utils.get_soup(NAME, start_html, end_html)
query1 = soup.findAll('dt', attrs={'class': 'ptitle'})
query2 = soup.findAll('dd')

index, titles, urls = 1000, [], []
for q in query1:
    title = utils.get_title(q.a.text[1:-1], index)
    index += 1
    titles.append(title)

for i, q in enumerate(query2):
    if i % 2 == 0:
        continue
    url = 'https://www.ecva.net/' + q.a['href']
    urls.append(url)

utils.save_csv_file(titles, urls, NAME)

if __name__ == '__main__':
    utils.download_papers(titles, urls, SAVE_DIR, NUM_WORKERS)
