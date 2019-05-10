# Elle web scrapper

##
This repository contains application which scraps horoscope articles from [Elle.com](https://www.elle.com/it/oroscopo/).

### Running
```bash
for line in $(cat ./links); do name=$(basename $line); python3 app.py $line > out/$name  ; done
```
