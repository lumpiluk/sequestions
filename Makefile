se_questions.md: src/make_readme.py src/templates/Readme.md.jinja se_questions.yaml
	src/make_readme.py --in se_questions.yaml --out se_questions.md --template Readme.md.jinja

cleanall:
	rm -f Readme.md
