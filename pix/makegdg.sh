for f in *.gdg; do
  python gopic.py < "$f" > "${f%.gdg}.eps"
done
