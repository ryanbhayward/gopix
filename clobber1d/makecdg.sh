for f in *.cdg; do
  python pic.py < "$f" > "${f%.cdg}.eps"
done
