for f in *.gdg; do
  python3 gopic.py < "$f" > "${f%.gdg}.eps"
done
