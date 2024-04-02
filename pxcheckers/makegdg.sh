for f in *.gdg; do
  python3 checkerpic.py < "$f" > "${f%.gdg}.eps"
done
