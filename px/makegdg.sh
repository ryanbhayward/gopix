for f in *.gdg; do
  ./gopic.py < "$f" > "${f%.gdg}.eps"
done
