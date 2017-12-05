import click
import requests

from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('src', nargs=-1)   
@click.argument('dst', nargs=1)
def main(src, dst):
    	"""Get Chord Guitar"""
	src_search=""	
	for fn in src:
        	src_search+='%s' % (fn)+" "
	src_search+='%s'%(dst)
	url_search="https://www.google.co.in/search?ei=8TkhWvTLKsH-vAS--4SYDg&q="+src_search+" guitarthai.com".replace(" ","+")
	html=requests.get(url_search)
	b=BeautifulSoup(html.content,'html.parser')
	hint=b.find_all('div',{'class':'s'})[0].div.cite.text
	src=requests.get(hint)
	b=BeautifulSoup(src.content,'html.parser')
	photo_chord=b.find_all('div',{'id':'contentboxarticle1'})[0].img['src']
	req=requests.get("https://www.guitarthai.com"+photo_chord)
	img=Image.open(StringIO(req.content))  
	img.show()
	
