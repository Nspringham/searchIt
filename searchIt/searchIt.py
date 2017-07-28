#! python3
# searchIt.py - Launches a google search tab for the content of your clipboard


import webbrowser, sys, pyperclip

url = 'https://www.google.co.uk/search?q='

def search_web():
        if len(sys.argv) > 1:
                # Get address from command line
                search = ' '.join(sys.argv[1:])
                print("Searching google for: [" + search + "]")
        else:
                # Get address from clipboard.
                search = pyperclip.paste()
                print("Searching google for: [" + search + "]")

        webbrowser.open(url+search)

if __name__ == '__main__':
        search_web()
