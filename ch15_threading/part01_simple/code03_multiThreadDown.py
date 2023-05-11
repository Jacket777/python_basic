"""
code03 多线程下载
"""
import requests, os, bs4, threading


def downlaodXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        #  Downlaod the page
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to  ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(1000000):
                imageFile.write(chunk)


if __name__ == '__main__':
    os.makedirs('xkcd', exist_ok=True)
    # Create and start the Thread objects
    downloadThreads = []
    for i in range(0, 1400, 100):
        downloadThread = threading.Thread(target=downlaodXkcd, args=(i, i + 99))
        downloadThreads.append(downloadThread)
        downloadThread.start()

    # Wait for all threads to end
    for downloadThread in downloadThreads:
        downloadThread.join()

    print('Done.')
