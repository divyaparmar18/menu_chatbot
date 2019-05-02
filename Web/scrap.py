import requests
from bs4 import BeautifulSoup
import json

url = " https://www.imdb.com/india/top-rated-indian-movies/"


def scrape_top():
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    movie_details = []

    tbody = soup.find('tbody', class_="lister-list")
    tr = tbody.findAll("tr")
    j = 0
    for i in tr:
        new = {}
        position = j = j+1
        name = i.find("td", class_="titleColumn").a.getText()
        year = i.find("td", class_="titleColumn").span.getText()
        rank = i.find("td", class_="ratingColumn").getText()
        link = i.find("a", href=True)

        links = "https://www.imdb.com" + link["href"]

        new["position"] = position
        new["movie_name"] = name
        new["year"] = int(year[1:5])
        new["rank"] = float(rank)
        new["link"] = links

        movie_details.append(new)
        with open("dta.json", "w") as outlet:
            json.dump(movie_details, outlet, indent=2)
    return (movie_details)


scrapped = scrape_top()
#print (scrapped)


def group_by_year(movie):
    years = []
    for i in movie:
        year = i["year"]
        if year not in years:
            years.append(year)
    years.sort()
    movie_dict = {i: []for i in years}
    for i in movie_dict:
        for x in movie:
            if (str(i) in str(x)):
                movie_dict[i].append(x)

    with open("year.json", "w") as fs:
        json.dump(movie_dict, fs, indent=2)
    return movie_dict


movie_years = group_by_year(scrapped)
#print (n)


def group_by_decade(movie, movies):
    years = []
    for i in movie:
        mod = i % 10
        year = i - mod
        if year not in years:
            years.append(year)
    years.sort()

    decade_dict = {i: []for i in years}
    for i in decade_dict:
        for x in movies:
            if x["year"] >= i and x["year"] < (i+10):
                decade_dict[i].sort(key=lambda i: i["year"])
                decade_dict[i].append(x)

    with open("decade.json", "w") as fs:
        json.dump(decade_dict, fs, indent=2)

    return decade_dict

#print (group_by_decade(n,scrapped))


def movie_details(movie_url):

    res = requests.get(movie_url)
    soup = BeautifulSoup(res.text, "html.parser")
    movie = {}
    Genre = []

    movie_ = soup.find('h1', class_="").get_text().split("(")
    movie_name = movie_[0].strip()

    dir_nam = soup.find("div", class_="credit_summary_item")
    direct = dir_nam.findAll("a")
    direct_name = []
    for i in direct:
        direct_name.append(i.get_text())

    bio = soup.find("div", class_="summary_text").get_text().strip()

    poster_url = soup.find("div", class_="poster").a["href"]
    main_link = "https://www.imdb.com"+poster_url

    run = soup.find("div",class_ = "subtext").time.get_text().strip()
    hours = int(run[0]) * 60
    if "min" in run:
        run_min = int(run[3:].strip("min"))
        Runtime = hours + run_min
    else:
        Runtime = hours 

    gene = None
    genre_name = soup.findAll("div", class_="see-more inline canwrap")
    for j in genre_name:
        gene = j.get_text()
        if "Genres:" in gene:
            gene_list= gene.split()
            for i in gene_list:
                if i != "Genres:" and i != "|":
                     Genre.append((i))

    block = None
    txt_block = soup.findAll("div",class_="txt-block")
    for i in txt_block:
        block  = i.get_text()
        
        if "Country:" in block:
            Count = block.split()
            Country = Count[1]
            
        elif "Language:" in block:
            Lang = block.split()
            Language = []
            for i in Lang:
                if i != "Language:" and i != "|":
                    Language.append(i)


    movie["movie_name"] = movie_name
    movie["director"] = direct_name
    movie["Country"] = Country
    movie["language"] = Language
    movie["poster_url"] = main_link
    movie["Runtime"] = (Runtime)
    movie["bio"] = bio
    movie["Genre"] = Genre

    with open("detail.json", "w") as fs:
        json.dump(movie, fs, indent=2)

    return movie

data = movie_details("https://www.imdb.com/title/tt0093603/")
(data)

top_movies = scrape_top()
def  movie_details_list(movies):
    movie_detail = []
    for i in movies:
          url =  (i.get("link"))
          detail_of_movie = movie_details(url)
          (detail_of_movie)
          movie_detail.append(detail_of_movie)

    # with open("task5.json", "w") as fs:
    #     json.dump(movie_detail, fs, indent=2)

    return movie_detail
    
        
print (movie_details_list(top_movies[:10]))



