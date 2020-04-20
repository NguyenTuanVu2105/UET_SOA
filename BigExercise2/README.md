# TOOL CRAWL AND DOWNLOAD MUSIC FROM ZINGMP3, SOUNDCLOUD

## Run without docker 

Download rabbitmq:

```sh
$ sudo apt install rabbitmq-server
```

Start zingmp3Crawler
```sh
$ python zingmp3Crawler/consumer.py
```

In other teminal, start soundcloudCrawler
```sh
$ python soundcloudCrawler/consumer.py
```

In other terminal, start produer to push list music playlist to queue
```sh
$ python producer/producer.py
```