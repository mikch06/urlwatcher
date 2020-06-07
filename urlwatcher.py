import os

urls = [
('Google', 'https://google.ch'),
('kissel.ch', 'https://kissel.ch/site'),
('SBB', 'https://sbb.ch')
]

def printConfiguredUrl():
    for domain,url in urls:
        print(domain, url)

def manageDirs():
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

def createImages():



manageDirs()
printConfiguredUrl()
