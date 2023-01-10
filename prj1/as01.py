# Задача №1. Секция статьи "Задача №1."
# Написать метод domain_name, который вернет домен из url адреса:

# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = "cnet"


def domain_name(url):
    # Get start of domain
    if "www." in url:
        start_index = url.find("www.") + 4
    elif "://" in url:
        start_index = url.find("://") + 3
    else:
        pass
    domain_start = url[start_index:]
    end_index = domain_start.find(".")
    domain = domain_start[:end_index]
    print(f"domain: {domain}")
    return domain


domain_name("https://www.cnet.com")
domain_name("http://github.com/carbonfive/raygun")

print("Tests:")
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
