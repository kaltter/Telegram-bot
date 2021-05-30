from bitlyshortener import Shortener


# Use your own.
tokens_pool = ['24764ac7e594119dfb7ab0819a4ad207d1ca5511']
shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)

# Shorten to list
urls = ['https://www.thelocal.se/20200526/what-happens-if-you-break-swedens-coronavirus-restrictions']
short_link = shortener.shorten_urls(urls)

print(short_link)
