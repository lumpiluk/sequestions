all: Readme.md se_questions.md flashcards_5x2-on-a4paper.pdf

Readme.md: src/fill_template.py src/templates/Readme.md.jinja se_questions.yaml
	src/fill_template.py --in se_questions.yaml --out Readme.md --template Readme.md.jinja

se_questions.md: src/fill_template.py src/templates/plain_list.md.jinja se_questions.yaml
	src/fill_template.py --in se_questions.yaml --out se_questions.md --template plain_list.md.jinja

flashcards_5x2-on-a4paper.tex: src/fill_template.py src/templates/flashcards.tex.jinja se_questions.yaml
	src/fill_template.py --in se_questions.yaml --out flashcards_5x2-on-a4paper.tex --template flashcards.tex.jinja

flashcards_5x2-on-a4paper.pdf: flashcards_5x2-on-a4paper.tex
	latexmk -pdf -f flashcards_5x2-on-a4paper.tex

cleanall: clean
	rm -f Readme.md se_questions.md
	latexmk -C flashcards_5x2-on-a4paper.tex
	rm -f flashcards_5x2-on-a4paper.tex flashcards_5x2-on-a4paper.pdf

clean: 
	latexmk -c flashcards_5x2-on-a4paper.tex
