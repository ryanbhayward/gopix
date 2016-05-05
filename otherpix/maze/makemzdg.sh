for f in *.mzdg; do
  python mazepic.py < "$f" > "${f%.mzdg}.eps"
done
