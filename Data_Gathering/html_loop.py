import requests
import urllib.request

def main():
    try:
        page = "2"
        clause = "&orderby=new"
        url = "https://www.lotto-8.com/philippines/listltoPH42.asp?indexpage={}{}".format(page,clause)
        response = requests.get(url)
        print(response)
    except:
        print("Error")

if __name__ == "__main__":
	main()