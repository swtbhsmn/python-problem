# Q11. Write a program anti_html.py that takes a URL as argument, downloads the html from web
#      and print it after stripping html tags.

from urllib.request import urlopen
import re
import argparse

def remove_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)
   


def download_html_from_web(url):
    get_data_with_tag = urlopen(url).read()
    return remove_html_tags(get_data_with_tag.decode('utf-8'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Takes a URL as argument, downloads the html from web and print it after stripping html tags')
    parser.add_argument('-u', '--url',  
                    required = True,
                    action ='store', 
                    help ='Provide URL for download html from web.')
    args = parser.parse_args()
    text = download_html_from_web(args.url)
    print(str(text).strip())

# Paste in cli for run this code.
# python q11.py -u https://swtbhsmn.github.io/index.html