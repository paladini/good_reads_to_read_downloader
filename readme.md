# GoodReads "To Read" Downloader
Download all books from "to-read" shelf from [GoodReads](http://www.goodreads.com) to your computer using [Libgen.io](http://libgen.io).

## How to use

1. Clone this project to your computer or [download a zip from the latest version](https://github.com/paladini/good_reads_to_read_downloader/archive/master.zip).
2. Install required modules using `pip3 install -r requirements.txt`.
3. [Get a free *developer key* from GoodReads API](https://www.goodreads.com/api/keys).
4. Get your number ID from GoodReads. In order to do that, go to your profile and get the numeric value from the address bar. For example, the [URL for my profile](https://www.goodreads.com/user/show/51988336-fernando-paladini) gives me the ID `51988336`.
5. In `main.py`, change `<DEVELOPER_KEY>` to the `developer key` you got from Goodreads API and change `<YOUR_DESIRED_ID>` to the number ID you got from your public profile at Goodreads.
6. Run `python3 main.py` and wait a considerable amount of time. All books will be saved to 'downloads/' folder.

## About
Developed by Fernando Paladini on May 29, 2016.

## License
WTFPL. For more info, check out the license file.

Book:
{
	"title": O Mundo assombrado pelos demônios,
	"identifier": [
		{ type: "isbn", value: },
		{ type: "isbn13", value: },
		{ type: "issn", value: }
	],
	


}