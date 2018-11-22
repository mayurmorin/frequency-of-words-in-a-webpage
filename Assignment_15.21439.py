
# coding: utf-8

# ### In this assignment I have to find the frequency of words in a webpage. I will use urllib and BeautifulSoup to extract text from webpage.

# ### Importing Modules

# In[1]:


from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords, webtext
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# ### Loading Data

# In[2]:


response = urllib.request.urlopen('http://php.net/') #Requesting to http://php.net/
html = response.read() #Reads the response from http://php.net/
soup = BeautifulSoup(html,"html5lib") #Parses pages the same way a web browser does and Creates valid HTML5


# ### Data Exploration

# In[3]:


#Prints the type of response variable
print(type(response))


# In[4]:


#Prints the type of html variable
print(type(html))


# In[5]:


#Prints the type of soup variable
print(type(soup))


# In[6]:


#Prints html data i.e. response read from http://php.net
print(html)


# In[7]:


#Prints soup data, its BeautifulSoup object which represents the document as a nested data structure
print(soup)


# In[8]:


#The BeautifulSoup object itself represents the document as a whole. 
soup.name


# In[9]:


#Shows the data in head html tag
soup.head


# In[10]:


#Shows the title tag data
soup.title


# In[11]:


#Shows the first <b> tag beneath the <body> tag
soup.body.b


# In[12]:


#Shows the first tag by 'a' name 
soup.a


# In[13]:


#Shows all the a tag
soup.find_all('a')


# In[14]:


#Prints all extracted text from the page
print(soup.get_text())


# ### Counting the words

# In[15]:


#Extracting all text from the page.
texts = soup.get_text(strip=True)

#Creating a list of the words extracted from the page
tokens = [txt for txt in texts.split()]

#Count the number of times that each a word occurs and stores in a dictionary where word is the key and count is value.
counts = nltk.FreqDist(tokens)

#Printing all the words and occurance of the word.
for key,value in counts.items(): 
    print(key + ' --> ' + str(value))


# ### Removing the Stopwords

# In[16]:


import nltk
nltk.download('stopwords')
    
#Creating a list of the english stopwords
sw = stopwords.words('english')

#List of new tokens without stopwords
tokens_new = [tkn for tkn in tokens if tkn not in sw]

#Count the number of times that each a word occurs and stores in a dictionary where word is the key and count is value.
counts_new = nltk.FreqDist(tokens_new)

#Printing all the words and occurance of the word.
for key,value in counts_new.items(): 
    print(key + ' --> ' + str(value))


# ### Count Plot

# In[17]:


#Plots the cumulative counts of the 30 most commonly occuring words.
plt.figure(figsize=(16,9))
counts_new.plot(30, cumulative=True)


# ### Dispersion Plot

# In[18]:


import nltk
nltk.download('webtext')
#Dispersion plot of first 30 words with respect to webtext words
plt.figure(figsize=(16,9))
webtext = nltk.text.Text(nltk.corpus.webtext.words())
webtext.dispersion_plot(tokens_new[:30])

