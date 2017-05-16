all: Readme.md se_questions.md

Readme.md: src/fill_template.py src/templates/Readme.md.jinja se_questions.yaml
	src/fill_template.py --in se_questions.yaml --out Readme.md --template Readme.md.jinja

se_questions.md: src/fill_template.py src/templates/plain_list.md.jinja se_questions.yaml
	src/fill_template.py --in se_questions.yaml --out se_questions.md --template plain_list.md.jinja

cleanall:
	rm -f Readme.md
