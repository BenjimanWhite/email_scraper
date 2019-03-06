import sys
import requests
import re

""" This python script takes a space separated sequence of urls and finds
    email addresses present at those urls.

    Example Usage:

    `pipenv run python scraper.py <"first_url" "second_url" ...>`

    It returns a dictionary of the form,

    {first_url: 
       {'email_address_1': <number_of_times_email_address_1_appears>,
        'email_address_2': <number_of_times_email_address_2_appears>
       },
     second_url:
       {'email_address_1': <number_of_times_email_address_1_appears>,
        'email_address_2': <number_of_times_email_address_2_appears>
       }
     ...
    }"""

website_urls = sys.argv[1:]

email_regex = r'[\w\.-]+@[\w\.-]+'

def run_script():
  output = {}
  for url in website_urls:
    email_dictionary = {} 
    emails = get_emails(scrape_html(url))

    for email in emails:
      if email in email_dictionary:
        email_dictionary[email] += 1
      else:
        email_dictionary[email] = 1

    output[url] = email_dictionary
  return output

def scrape_html(url):
  response = requests.get(url)
  return response.text

def get_emails(html):
  emails = re.findall(email_regex, html)
  return emails

print(run_script())
