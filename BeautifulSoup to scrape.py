#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])

print('List all the header tags :', *titles, sep='\n\n')


# In[186]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[100]:


url= 'https://bookpage.com/reviews?book_genre=children_s&page=1'
page = requests.get(url)
page


# In[103]:


soup = BeautifulSoup(page.content, "html.parser") 
print(soup.prettify())


# In[104]:


scraped_bookname = soup.find_all ('h4', class_= "italic")
scraped_bookname                                  


# In[117]:


booknames =[]
for bookname in scraped_bookname: 
    booknames.append(bookname.get_text().strip())
    


# In[118]:


booknames


# In[76]:


page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
soup


# In[247]:


period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)


# In[248]:


period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods


# In[251]:


short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)


# In[252]:


import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs})
weather


# In[268]:


import pandas as pd
 
from bs4 import BeautifulSoup
import requests


# In[269]:


page = requests.get("https://internshala.com/fresher-jobs")
page


# In[270]:


page.content


# In[271]:


soup=BeautifulSoup(page.content)
soup


# In[272]:


print(soup.prettify())


# In[273]:


first_title=soup.find('div', class_="heading_4_5 profile")
first_title


# In[274]:


first_title.text


# In[275]:


first_title.text.replace('\n','')


# In[276]:


first_company=soup.find('a', class_="link_display_like_text")
first_company


# In[277]:


first_company.text


# In[278]:


first_company.text.replace('\n', '')


# In[285]:


first_ctc=soup.find('div', class_="internship_other_details_container")
first_ctc


# In[145]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[146]:


url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
page = requests.get(url)
page


# In[147]:


soup=BeautifulSoup(page.content)
soup


# In[149]:


no_of_match = []
points = []
rating =[]
new_list = []


# In[150]:


no_of_match = []


# In[151]:


match1 = soup.find_all("td", class_="rankings-block__banner--matches")
for i in match1:
    no_of_match.append(i.text)


# In[152]:


no_of_match


# In[153]:


complite_info = []
match_1 = soup.find_all("td", class_="table-body__cell u-text-right rating")
for i in match_1:
    complete_info.append(i.text)
    


# In[154]:


complete_info


# In[164]:


for i in range (0,len(complete_info),2):
    no_of_match.append(complete_info[i])


# In[165]:


no_of_match


# In[171]:


player_name = []
Team = []
rating =[]


# In[172]:


player_name = []


# In[190]:


player_name1 = soup.find_all("div", class_="rankings-block__banner--name")
    for i in player_name1:
    player_name.append(i.text)


# In[191]:


player_name.append(i.text)


# In[1]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[2]:


url = "https://www.imdb.com/chart/top/"
page = requests.get(url)
page


# In[22]:


Soup = BeautifulSoup (page.content)
print(Soup.prettify())


# In[29]:


scraped_movies = Soup.find_all('td', class_='titleColumn')
scraped_movies


# In[42]:


movies =[]
for movie in scraped_movies: 
    movies.append(movie.get_text().strip().replace('\n',''))
movies


# In[47]:


scraped_ratings = Soup.find_all('td', class_='ratingColumn imdbRating')
scraped_ratings 


# In[91]:


rating = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n','')
    ratings.append(rating)


# In[92]:


ratings


# In[77]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[78]:


url = "https://www.imdb.com/india/top-rated-indian-movies/"
page = requests.get(url)
page


# In[79]:


Soup = BeautifulSoup (page.content)
print(Soup.prettify())


# In[80]:


scraped_movies = Soup.find_all('td', class_='titleColumn')
scraped_movies


# In[81]:


movies =[]
for movie in scraped_movies: 
    movies.append(movie.get_text().strip().replace('\n',''))
movies


# In[82]:


rating = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n','')
    ratings.append(rating)


# In[83]:


ratings


# In[86]:


import pandas as pd 


# In[88]:


data = pd.DataFrame()
data['Movie Names'] = movies
data['Ratings'] = rating
data.head()


# In[122]:


import pandas as pd
import requests 
from bs4 import BeautifulSoup


# In[123]:


url = "https://www.amazon.in/s?k=mobile+phones+under+Rs.+20%2C000&rh=n%3A976419031%2Cp_36%3A1318506031&dc&qid=1627581467&rnid=1318502031&ref=sr_nr_p_36_4"
page = requests.get(url)
page


# In[124]:


Soup = BeautifulSoup (page.content)
print(Soup.prettify())


# In[132]:


product = soup.find_all(‘span',class_=‘a-size-medium a-color-base a-text-normal’)
product


# In[130]:


product 


# In[ ]:




