for f in *.g; do
  python3 pic.py < "$f" > "${f%.g}.eps"
done
