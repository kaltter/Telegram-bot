import feedparser
import telebot
from time import sleep
from models import ParsedNews
from app import db, db1, config
from bitlyshortener import Shortener




# parse from 'the local'
def parse():
    return feedparser.parse('https://feeds.thelocal.com/rss/index.php')

parsed = parse()

# add parsed to db
def add_to_db():
    for i in parsed.entries:
        for n in i.links:
                if (n.rel == 'alternate'):
                    pass
                else:
                    news = ParsedNews(title=i.title, description=i.description, link=i.link, img=n.href)
                    db.session.add(news)
                    db.session.commit()
    
add_to_db()

# connect to telegram bot
bot = telebot.TeleBot(config.TOKEN)

# post message
def post_to_tg():
    news = db1.execute("SELECT * FROM parsed_news LIMIT 1")
    for i in news:
        news_title = "{}".format(i['title'])
        news_descr = "{}".format(i['description'])
        news_link = "{}".format(i['link'])
        news_img = "{}".format(i['img'])
        # send_message with photo below
        # print(bot.send_message(config.CHANNEL_NAME, text="[.](news_img)" + '\n\n' + '*' + news_title + '*' + '\n\n' + news_descr + '\n\n' + '*link:* ' + news_link, disable_web_page_preview=False, parse_mode="Markdown"))
        print(bot.send_photo(config.CHANNEL_NAME, photo=news_img, caption='*' + news_title + '*' + '\n\n' + news_descr + '\n\n' + '*link:* ' + news_link, parse_mode="Markdown"))
        # sleep(0.5)
    else:
        "error"


post_to_tg()