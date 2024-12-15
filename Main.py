import argparse
from Translator import Translator

def parse_args():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Parse text and translate it.")
    parser.add_argument('text', type=str, help="Text to translate")

    # Parse the arguments
    args = parser.parse_args()
    return args
def main(args):
    translator = Translator()
    config = translator.parse(args.text)
    return config


if __name__ == "__main__":
    print(main(parse_args()))