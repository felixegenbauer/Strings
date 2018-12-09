from task import show_url  # TODO: complete task.py first
import urllib.request

number = "703410"
urllib.request.urlretrieve(show_url(number), number + ".html")