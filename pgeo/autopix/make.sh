for f in *.geo; do
  ./geopic.py < "$f" > "${f%.geo}.eps"
done
