#!/bin/bash
cd ~/KatalogFactory || exit 1
python3 -m compileall src
git status
echo
echo "Danach:"
echo "git add ."
echo "git commit -m \"Sitzungsabschluss\""
echo "git push"
