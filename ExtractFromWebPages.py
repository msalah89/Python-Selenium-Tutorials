import re
import linkGrabber

#                                                        Explaination
# in this example we are going to grab all urls and links inside the page . this is used in web surfing and crawling scenarios here we are not using selenium
#here we use linkGrabber library which is not in python packages  by default so we install it using pip open your cmd and type the below command
#----------------------------------------------------------------------------------------------------------------------------------------------
#
#                                                    pip install linkGrabber
#
#----------------------------------------------------------------------------------------------------------------------------------------------
#Parameters:
#* filters (dict): Beautiful Soup's filters as a dictionary
#* limit (int): Limit the number of links in sequential order
#* reverse (bool): Reverses how the list of <a> tags are sorted
#* sort (function): Accepts a function that accepts which key to sort upon
#within the List class


links  = linkGrabber.Links('https://google.com')
gb= links.find(limit=8, duplicates=False,pretty=True)

print(gb)