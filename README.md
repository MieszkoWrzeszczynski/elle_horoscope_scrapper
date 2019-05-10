# Elle web scrapper

## Desc
This repository contains application which scraps horoscope articles from [Elle.com](https://www.elle.com/it/oroscopo/).

### Running
```bash
LINKS="./links.txt"
OUTPUT_DIR="./out"

for line in $(cat $LINKS); do name=$(basename $line); python3 app.py $line > $OUTPUT_DIR/$name  ; done
```

#### Output format
Each of scrapped document it's formatted in this way:
```
Title

Author

Date

Content
```
