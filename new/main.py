from sys import excepthook
import  requests
import bs4

url= input("enter url")
response=requests.get(url)
filename="page.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted_text= bs.prettify()
print(formatted_text)

with open(filename,"w+") as f:
        f.writelines(formatted_text)

   list_imgs=bs.find('img')
       no_of_imgs = len(list_imgs)
       list_as = bs.find_all('a')
       no_of_as =len(list_as)
       print("number of img tags",no_of_imgs)
       print("number of anchor tags",no_of_as)
  for imglink in list_imgs:
      print(imgtag)          