# -*- coding: utf-8 -*-
#
# Autor:    Lcs_EncodePy
# GitHub:   https://github.com/EncodePy
# Contact:  https://t.me/Error_404p
#
# -First you Learn, then remove the 'L'.

import re, requests, os
from bs4 import BeautifulSoup as bfs

def site():
	tag = input('Digite sua tag >>> ')
	if '#' in tag:
		tag = tag.replace('#', "")
	os.system('clear')
	
	site = f'https://statsroyale.com/br/profile/{tag}?fresh=1'
	return site
	
def siteRequest(site):
	req = requests.get(site)
	stt = req.status_code
	try:
		if stt == 200:
			soup = bfs(req.text, 'html.parser')
			text = (req).text
			div = soup.find_all("div")
			div = str(div)
			div_rrr = div.replace('\n', "")
			return div_rrr
		else:
			return ('Error... status code:', stt)

	except Exception as error:
		print(error)

def reg_responseFromSite(text_parse):
	p_name = re.search(r'<span class="profileHeader__nameCaption">(.*?)</span>', text_parse).group(1)
	m_cup = re.search(r'<div class="statistics__metricCounter ui__headerExtraSmall">(.*?)</div>', text_parse).group(1)
	f_card = re.search(r'<span class="profile__favouriteCardName">(.*?)</span>', text_parse).group(1)
	p_tag = re.search(r'<div class="refresh__buttonContainer"><div class="refresh__button" data-id="(.*?)">', text_parse).group(1)

	data = {
		
		'tag': p_tag,
		'name': p_name,
		'cups': m_cup,
		'fcard': f_card
		
	}
	
	return data

def result():
	print('Tag:', response['tag'])
	print('Player:', response['name'])
	print('Max troféus:', response['cups'])
	print('Carta favorita:', response['fcard'])

site = site()
acess = siteRequest(site)
response = reg_responseFromSite(acess)
start = result()

#teste