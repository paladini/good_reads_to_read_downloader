# Good Reads "To Read" Downloader
Download all books from "to-read" shelf from [GoodReads](http://www.goodreads.com) to your computer using [Libgen.io](http://libgen.io).

## How to use

* Download all the required Python3 modules (`pip3 install -r requirements.txt`).
* [Get a free *developer key* from GoodReads API](https://www.goodreads.com/api/keys).
* Get your number ID from GoodReads. In order to do that, go to your profile and get the numeric value from the address bar. For example, the [URL for my profile](https://www.goodreads.com/user/show/51988336-fernando-paladini) gives me the ID `51988336`.
* In `main.py`, change `<DEVELOPER_KEY>` to the `developer key` you got from Goodreads API and change `<YOUR_DESIRED_ID>` to the number ID you got from your public profile at Goodreads.
* Run `python3 main.py` and wait a considerable amount of time. All books will be saved to 'downloads/' folder.

## About
Developed by Fernando Paladini on May 29, 2016.

## License
WTFPL. For more info, check out the license file.