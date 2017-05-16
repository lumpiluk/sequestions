#!/usr/bin/env python3

import yaml  # requires PyYAML (on Ubuntu, this comes with the python3-yaml package)
from jinja2 import Environment, PackageLoader, Template  # Jinja templating engine
import sys
from getopt import getopt, GetoptError


DEFAULT_TEMPLATE = """
{% for question in questions %}
{% if question.prompt %}
- (Source: [{{ question.source.link }}]({{ question.source.link }}))
  - *IL:* {{ question.prompt }}
  - *Q:* {{ question.question }}
{% else %}
- {{ question.question }} (Source: [{{ question.source.link }}]({{ question.source.link }}))
{% endif %}
{% endfor %}
"""


def show_help():
    print("Usage: ./make_readme.py -i <input yaml filename> -o <output filename>")
    print("\nReads a list of questions from a specifically formatted YAML file and "
          "inserts them into an optional template.")
    print("\nOptions:")
    print("-h\t--help\tShow this help.")
    print("-i\t--in <file>\tSet the input YAML file.")
    print("-o\t--out <file>\tSet the output YAML file.")
    print("-t\t--template <file>\t The name of the template. "
          "The template must be located in this package's 'templates' folder!")


def main():
    try:
        opts, args = getopt(sys.argv[1:], "hi:o:t:", ["help", "in=", "out=", "template="])
    except GetoptError as err:
        print(err)
        show_help()
        sys.exit(2)
    
    input_filename = None
    output_filename = None
    template_name = None

    for opt, arg in opts:
        if opt in ["-h", "--help"]:
            show_help()
            sys.exit()
        elif opt in ["-i", "--in"]:
            input_filename = arg
        elif opt in ["-o", "--out"]:
            output_filename = arg
        elif opt in ["-t", "--template"]:
            template_name = arg
    
    if input_filename is None or output_filename is None:
        print("Please provide both an input and an output file!\n")
        show_help()
        sys.exit()

    yaml_to_markdown_list(input_filename, output_filename, template_name)


def yaml_to_markdown_list(input_filename, output_filename, template_name=None):
    """
    Convert a list of questions specified in a YAML file to a Markdown-formatted list.
    :param output_filename: Name of the output file.
    :param template_name: Name of the Jinja2 template file located in the sub-folder 'templates', may be None.
    :param input_filename: Path to the input YAML file.
    :return: The Markdown-formatted list as a string.
    """
    with open(input_filename, 'r') as stream:
        try:
            questions = yaml.load(stream)
            template = Template(DEFAULT_TEMPLATE)
            if template_name is not None:
                jinja_env = Environment(loader=PackageLoader(__name__, 'templates'),
                                        trim_blocks=True,
                                        lstrip_blocks=True)
                template = jinja_env.get_template(template_name)
            with open(output_filename, 'w') as output_file:
                output_file.write(template.render(questions=questions))
        except yaml.YAMLError as e:
            print("Error while parsing the input file {}:".format(input_filename))
            print(e)


if __name__ == "__main__":
    main()
