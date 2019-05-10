# RUN

for line in $(cat ./links); do name=$(basename $line); touch $name; python3 app.py $line > out/$name  ; done
