for f in *.g; do
  python pic.py < "$f" > "${f%.g}.eps"
done
