# -*- coding: utf-8 -*-
#!/python2.7
#Created by aj nicolas
import requests
from bs4 import BeautifulSoup
import crayons

# While true to get a actual link
def linkfriendly():
    global url
    global r
    global soup
    while True:
        # Gets user shopify link
        try:
            url = raw_input('PASTE LINK HERE: ')
            r = requests.get(url + '.xml')
            soup = BeautifulSoup(r.content, 'html.parser')
            if r == False:
                print 'Link not supported!'
            elif r == True:
                print '\n' + 'Link found!'
            break
            # Handles exceptions
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL, requests.exceptions.ConnectionError,
            requests.exceptions.InvalidSchema,NameError) as e:
            print '{}'.format(crayons.red('link no bueno!'))


# Grabs handle text
def grabhandle():
    try:
        for handL in soup.findAll("handle"):
            return 'Handle: ' + handL.text
    except NameError:
        print '{}'.format(crayons.cyan('Could not find text!'))



# Sets up the link formating and grabs date link was created
def grabdate():
    for created in soup.findAll("created-at"):
        return 'created: ' + created.text


# Function names pretty self explanitory!
def grabsku():
    for sku in soup.findAll("sku"):
        return 'sku: ' + sku.text


def grabprice():
    for price in soup.findAll("price"):
        return 'Price: ' + price.text


# Parses stock,sz name, and variants from shopify site
def grabszstk():
    sz = []
    for size in soup.findAll("title")[1:]:
        # append to list
        sz.append(size)

    stk = []
    for stock in soup.findAll("inventory-quantity"):
        stk.append(stock)

    variants = []
    for variant in soup.findAll("id")[1:]:
        variants.append(variant)

    # formats the data
    fmt = '{:<5}{:<13}{:<10}{}'
    fmat = '{:<5}{:<13}{}'

    # zips the for lists together
    if len(stk) > 0:
        print(fmt.format('', 'size', 'stock', 'variant'))
        for i, (sz, stk, variants) in enumerate(zip(sz, stk, variants)):
            print(fmt.format(i, sz.text, stk.text, variants.text))
        #if stock wasn't found
    else:
        print '{}'.format(crayons.red('STOCK WAS NOT FOUND'))
        print(fmat.format('', 'size','variant'))
        for i, (sz,variants) in enumerate(zip(sz,variants)):
            print(fmat.format(i, sz.text, variants.text))

# Also bad formatting
def formattext():
    print '--' * 38
    print url
    print '  ' * 38
    try:
        print grabhandle() + ' ' + grabdate() + ' \n' + grabprice() + ' \n' + grabsku()
        print grabszstk()
    except TypeError:
        print '{}'.format(crayons.red("Try copying everything before before the '?variant' \n or before the '?' in the link!".upper()))


# While true statment for multiple link checks!
while True:
    if linkfriendly() == True:
        print linkfriendly()
    elif formattext() == True:
        print formattext()
