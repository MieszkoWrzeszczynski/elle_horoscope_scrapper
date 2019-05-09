# RUN

for line in $(cat lol); do name=$(basename $line); touch $name; python3 app.py $line > $name  ; done
