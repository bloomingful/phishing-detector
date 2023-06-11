from datetime import datetime
from bs4 import BeautifulSoup
import requests
import whois
import time
import re
import dns.resolver
import json
from urllib.parse import urlencode

#################################################################################################################################
#               DNSRecord  expiration length
#################################################################################################################################

def dns_record(domain):
    try:
        nameservers = dns.resolver.resolve(domain,'NS')
        if len(nameservers)>0:
            return 0
        else:
            return 1
    except:
        return 1

#################################################################################################################################
#               Page Rank from OPR
#################################################################################################################################

def page_rank(key, domain): # column: page_rank
    url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
    try:
        request = requests.get(url, headers={'API-OPR':key})
        result = request.json()
        result = result['response'][0]['page_rank_integer']
        if result:
            return result
        else:
            return 0
    except:
        return -1