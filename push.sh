git config user.email "thomasn-dev@protonmail.ch"
git config user.name "thomasn-dev"
git add .
# commit message comes from bash argument
git commit -m "$1"
git branch -M main
git remote add origin git@github.com:thomasn-dev/python-lisp-interpreter.git
git push -u origin main



