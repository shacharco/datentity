from Main import main

def test_main(creation_text):
    config = main(creation_text)
    print(config)