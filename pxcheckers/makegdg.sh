for f in *.gdg; do
  python checkerpic.py < "$f" > "${f%.gdg}.eps"
done
