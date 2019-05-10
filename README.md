# RUN

for line in $(cat ./links); do name=$(basename $line); python3 app.py $line > out/$name  ; done
