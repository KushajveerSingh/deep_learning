import utils

NAME = "iclr_2021"
SAVE_DIR = f"../{NAME}"
NUM_WORKERS = 8

if __name__ == "__main__":
    utils.download_papers_from_csv(NAME, SAVE_DIR, NUM_WORKERS)
