import os
import urls


def printConfiguredUrl():
    with open('urls.py', 'r') as urls:
        for domain,url in urls:
            print(domain, url)

def manageDirs():
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

def createImages():



#manageDirs()
#printConfiguredUrl()
