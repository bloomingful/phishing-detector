import content_features as ctnfe
import url_features as urlfe
import external_features as trdfe
import urllib.parse
import tldextract
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

key = "c0cw4s4s4wsc8w0g0scc4s844wkowk4sw8owks8o" # OPR API key

def is_URL_accessible(url):
    page = None
    try:
        page = requests.get(url, timeout=5)   
    except:
        parsed = urlparse(url)
        url = parsed.scheme+'://'+parsed.netloc
        if not parsed.netloc.startswith('www'):
            url = parsed.scheme+'://www.'+parsed.netloc
            try:
                page = requests.get(url, timeout=5)
            except:
                page = None
                pass
    if page and page.status_code == 200 and page.content not in ["b''", "b' '"]:
        return True, url, page
    else:
        return False, None, None

def get_domain(url):
    o = urllib.parse.urlsplit(url)
    return o.hostname, tldextract.extract(url).domain, o.path

def getPageContent(url):
    parsed = urlparse(url)
    url = parsed.scheme+'://'+parsed.netloc
    try:
        page = requests.get(url)
    except:
        if not parsed.netloc.startswith('www'):
            url = parsed.scheme+'://www.'+parsed.netloc
            page = requests.get(url)
    if page.status_code != 200:
        return None, None
    else:    
        return url, page.content


### Data Extraction Process
def extract_data_from_URL(hostname, content, domain, Href, Link, Anchor, Media, Form, CSS, Favicon, IFrame, Title, Text):
    Null_format = ["", "#", "#nothing", "#doesnotexist", "#null", "#void", "#whatever",
               "#content", "javascript::void(0)", "javascript::void(0);", "javascript::;", "javascript"]

    soup = BeautifulSoup(content, 'html.parser', from_encoding='iso-8859-1')

    # collect all external and internal hrefs from url
    for href in soup.find_all('a', href=True):
        dots = [x.start(0) for x in re.finditer('\.', href['href'])]
        if hostname in href['href'] or domain in href['href'] or len(dots) == 1 or not href['href'].startswith('http'):
            if "#" in href['href'] or "javascript" in href['href'].lower() or "mailto" in href['href'].lower():
                 Anchor['unsafe'].append(href['href']) 
            if not href['href'].startswith('http'):
                if not href['href'].startswith('/'):
                    Href['internals'].append(hostname+'/'+href['href']) 
                elif href['href'] in Null_format:
                    Href['null'].append(href['href'])  
                else:
                    Href['internals'].append(hostname+href['href'])   
        else:
            Href['externals'].append(href['href'])
            Anchor['safe'].append(href['href'])

    # collect all media src tags
    for img in soup.find_all('img', src=True):
        dots = [x.start(0) for x in re.finditer('\.', img['src'])]
        if hostname in img['src'] or domain in img['src'] or len(dots) == 1 or not img['src'].startswith('http'):
            if not img['src'].startswith('http'):
                if not img['src'].startswith('/'):
                    Media['internals'].append(hostname+'/'+img['src']) 
                elif img['src'] in Null_format:
                    Media['null'].append(img['src'])  
                else:
                    Media['internals'].append(hostname+img['src'])   
        else:
            Media['externals'].append(img['src'])
           
    for audio in soup.find_all('audio', src=True):
        dots = [x.start(0) for x in re.finditer('\.', audio['src'])]
        if hostname in audio['src'] or domain in audio['src'] or len(dots) == 1 or not audio['src'].startswith('http'):
             if not audio['src'].startswith('http'):
                if not audio['src'].startswith('/'):
                    Media['internals'].append(hostname+'/'+audio['src']) 
                elif audio['src'] in Null_format:
                    Media['null'].append(audio['src'])  
                else:
                    Media['internals'].append(hostname+audio['src'])   
        else:
            Media['externals'].append(audio['src'])
            
    for embed in soup.find_all('embed', src=True):
        dots = [x.start(0) for x in re.finditer('\.', embed['src'])]
        if hostname in embed['src'] or domain in embed['src'] or len(dots) == 1 or not embed['src'].startswith('http'):
             if not embed['src'].startswith('http'):
                if not embed['src'].startswith('/'):
                    Media['internals'].append(hostname+'/'+embed['src']) 
                elif embed['src'] in Null_format:
                    Media['null'].append(embed['src'])  
                else:
                    Media['internals'].append(hostname+embed['src'])   
        else:
            Media['externals'].append(embed['src'])
           
    for i_frame in soup.find_all('iframe', src=True):
        dots = [x.start(0) for x in re.finditer('\.', i_frame['src'])]
        if hostname in i_frame['src'] or domain in i_frame['src'] or len(dots) == 1 or not i_frame['src'].startswith('http'):
            if not i_frame['src'].startswith('http'):
                if not i_frame['src'].startswith('/'):
                    Media['internals'].append(hostname+'/'+i_frame['src']) 
                elif i_frame['src'] in Null_format:
                    Media['null'].append(i_frame['src'])  
                else:
                    Media['internals'].append(hostname+i_frame['src'])   
        else: 
            Media['externals'].append(i_frame['src'])

    # collect all link tags
    for link in soup.findAll('link', href=True):
        dots = [x.start(0) for x in re.finditer('\.', link['href'])]
        if hostname in link['href'] or domain in link['href'] or len(dots) == 1 or not link['href'].startswith('http'):
            if not link['href'].startswith('http'):
                if not link['href'].startswith('/'):
                    Link['internals'].append(hostname+'/'+link['href']) 
                elif link['href'] in Null_format:
                    Link['null'].append(link['href'])  
                else:
                    Link['internals'].append(hostname+link['href'])   
        else:
            Link['externals'].append(link['href'])

    for script in soup.find_all('script', src=True):
        dots = [x.start(0) for x in re.finditer('\.', script['src'])]
        if hostname in script['src'] or domain in script['src'] or len(dots) == 1 or not script['src'].startswith('http'):
            if not script['src'].startswith('http'):
                if not script['src'].startswith('/'):
                    Link['internals'].append(hostname+'/'+script['src']) 
                elif script['src'] in Null_format:
                    Link['null'].append(script['src'])  
                else:
                    Link['internals'].append(hostname+script['src'])   
        else:
            Link['externals'].append(link['href'])

    # collect all css
    for link in soup.find_all('link', rel='stylesheet'):
        dots = [x.start(0) for x in re.finditer('\.', link['href'])]
        if hostname in link['href'] or domain in link['href'] or len(dots) == 1 or not link['href'].startswith('http'):
            if not link['href'].startswith('http'):
                if not link['href'].startswith('/'):
                    CSS['internals'].append(hostname+'/'+link['href']) 
                elif link['href'] in Null_format:
                    CSS['null'].append(link['href'])  
                else:
                    CSS['internals'].append(hostname+link['href'])   
        else:
            CSS['externals'].append(link['href'])
    
    for style in soup.find_all('style', type='text/css'):
        try: 
            start = str(style[0]).index('@import url(')
            end = str(style[0]).index(')')
            css = str(style[0])[start+12:end]
            dots = [x.start(0) for x in re.finditer('\.', css)]
            if hostname in css or domain in css or len(dots) == 1 or not css.startswith('http'):
                if not css.startswith('http'):
                    if not css.startswith('/'):
                        CSS['internals'].append(hostname+'/'+css) 
                    elif css in Null_format:
                        CSS['null'].append(css)  
                    else:
                        CSS['internals'].append(hostname+css)   
            else: 
                CSS['externals'].append(css)
        except:
            continue
            
    # collect all form actions
    for form in soup.findAll('form', action=True):
        dots = [x.start(0) for x in re.finditer('\.', form['action'])]
        if hostname in form['action'] or domain in form['action'] or len(dots) == 1 or not form['action'].startswith('http'):
            if not form['action'].startswith('http'):
                if not form['action'].startswith('/'):
                    Form['internals'].append(hostname+'/'+form['action']) 
                elif form['action'] in Null_format or form['action'] == 'about:blank':
                    Form['null'].append(form['action'])  
                else:
                    Form['internals'].append(hostname+form['action'])   
        else:
            Form['externals'].append(form['action'])
            
    # collect all link tags
    for head in soup.find_all('head'):
        for head.link in soup.find_all('link', href=True):
            dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
            if hostname in head.link['href'] or len(dots) == 1 or domain in head.link['href'] or not head.link['href'].startswith('http'):
                if not head.link['href'].startswith('http'):
                    if not head.link['href'].startswith('/'):
                        Favicon['internals'].append(hostname+'/'+head.link['href']) 
                    elif head.link['href'] in Null_format:
                        Favicon['null'].append(head.link['href'])  
                    else:
                        Favicon['internals'].append(hostname+head.link['href'])   
            else:
                Favicon['externals'].append(head.link['href'])
                
        for head.link in soup.findAll('link', {'href': True, 'rel':True}):
            isicon = False
            if isinstance(head.link['rel'], list):
                for e_rel in head.link['rel']:
                    if (e_rel.endswith('icon')):
                        isicon = True
            else:
                if (head.link['rel'].endswith('icon')):
                    isicon = True
       
            if isicon:
                 dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
                 if hostname in head.link['href'] or len(dots) == 1 or domain in head.link['href'] or not head.link['href'].startswith('http'):
                     if not head.link['href'].startswith('http'):
                        if not head.link['href'].startswith('/'):
                            Favicon['internals'].append(hostname+'/'+head.link['href']) 
                        elif head.link['href'] in Null_format:
                            Favicon['null'].append(head.link['href'])  
                        else:
                            Favicon['internals'].append(hostname+head.link['href'])   
                 else:
                     Favicon['externals'].append(head.link['href'])
                                 
    # collect i_frame
    for i_frame in soup.find_all('iframe', width=True, height=True, frameborder=True):
        if i_frame['width'] == "0" and i_frame['height'] == "0" and i_frame['frameborder'] == "0":
            IFrame['invisible'].append(i_frame)
        else:
            IFrame['visible'].append(i_frame)
    for i_frame in soup.find_all('iframe', width=True, height=True, border=True):
        if i_frame['width'] == "0" and i_frame['height'] == "0" and i_frame['border'] == "0":
            IFrame['invisible'].append(i_frame)
        else:
            IFrame['visible'].append(i_frame)
    for i_frame in soup.find_all('iframe', width=True, height=True, style=True):
        if i_frame['width'] == "0" and i_frame['height'] == "0" and i_frame['style'] == "border:none;":
            IFrame['invisible'].append(i_frame)
        else:
            IFrame['visible'].append(i_frame)
          
    # get page title
    try:
        Title = soup.title.string
    except:
        pass
    
    # get content text
    Text = soup.get_text()
    
    return Href, Link, Anchor, Media, Form, CSS, Favicon, IFrame, Title, Text

def extract_features(url):
    def words_raw_extraction(domain, subdomain, path):
        w_domain = re.split("\-|\.|\/|\?|\=|\@|\&|\%|\:|\_", domain.lower())
        w_subdomain = re.split("\-|\.|\/|\?|\=|\@|\&|\%|\:|\_", subdomain.lower())   
        w_path = re.split("\-|\.|\/|\?|\=|\@|\&|\%|\:|\_", path.lower())
        raw_words = w_domain + w_path + w_subdomain
        w_host = w_domain + w_subdomain
        raw_words = list(filter(None,raw_words))
        return raw_words, list(filter(None,w_host)), list(filter(None,w_path))
    
    Href = {'internals':[], 'externals':[], 'null':[]}
    Link = {'internals':[], 'externals':[], 'null':[]}
    Anchor = {'safe':[], 'unsafe':[], 'null':[]}
    Media = {'internals':[], 'externals':[], 'null':[]}
    Form = {'internals':[], 'externals':[], 'null':[]}
    CSS = {'internals':[], 'externals':[], 'null':[]}
    Favicon = {'internals':[], 'externals':[], 'null':[]}
    IFrame = {'visible':[], 'invisible':[], 'null':[]}
    Title =''
    Text= ''
    state, iurl, page = is_URL_accessible(url)
    if state:
        content = page.content
        hostname, domain, path = get_domain(url)
        extracted_domain = tldextract.extract(url)
        domain = extracted_domain.domain+'.'+extracted_domain.suffix
        subdomain = extracted_domain.subdomain
        tmp = url[url.find(extracted_domain.suffix):len(url)]
        pth = tmp.partition("/")
        path = pth[1] + pth[2]
        words_raw, words_raw_host, words_raw_path= words_raw_extraction(extracted_domain.domain, subdomain, pth[2])
        tld = extracted_domain.suffix
        parsed = urlparse(url)
        scheme = parsed.scheme
        
        Href, Link, Anchor, Media, Form, CSS, Favicon, IFrame, Title, Text = extract_data_from_URL(hostname, content, domain, Href, Link, Anchor, Media, Form, CSS, Favicon, IFrame, Title, Text)

        ### url-based features
        url1 = urlfe.url_length(url)
        print(f"URL length: {url1}")
        url2 = urlfe.url_length(hostname)
        print(f"Hostname length: {url2}")
        url3 = urlfe.having_ip_address(url)
        print(f"Presence of IP: {url3}")
        url4 = urlfe.count_dots(url)
        print(f"Number of dots in URL: {url4}")
        url5 = urlfe.count_hyphens(url)
        print(f"Number of hyphens in URL: {url5}")
        url6 = urlfe.count_at(url)
        print(f"Number of @ in URL: {url6}")
        url7 = urlfe.count_exclamation(url)
        print(f"Number of ! in URL: {url7}")
        url8 = urlfe.count_and(url)
        print(f"Number of & in URL: {url8}")
        # urlfe.count_or(url),
        url9 = urlfe.count_equal(url)
        print(f"Number of = in URL: {url9}")
        url10 = urlfe.count_underscore(url)
        print(f"Number of _ in URL: {url10}")
        url11 = urlfe.count_tilde(url)
        print(f"Number of ~ in URL: {url11}")
        url12 = urlfe.count_percentage(url)
        print(f"Number of % in URL: {url12}")
        url13 = urlfe.count_slash(url)
        print(f"Number of / in URL: {url13}")

        url14 = urlfe.count_star(url)
        print(f"Number of * in URL: {url14}")
        url15 = urlfe.count_colon(url)
        print(f"Number of : in URL: {url15}")
        url16 = urlfe.count_comma(url)
        print(f"Number of , in URL: {url16}")
        url17 = urlfe.count_semicolumn(url)
        print(f"Number of ; in URL: {url17}")
        url18 = urlfe.count_dollar(url)
        print(f"Number of $ in URL: {url18}")
        url19 = urlfe.count_space(url)
        print(f"Number of space in URL: {url19}")
        url20 = urlfe.check_www(words_raw)
        print(f"Number of 'www' in URL: {url20}")
        url21 = urlfe.check_com(words_raw)
        print(f"Number of 'com' in URL: {url21}")
        url22 = urlfe.count_double_slash(url)
        print(f"Number of // in URL: {url22}")
        url23 = urlfe.count_http_token(path)
        print(f"Number of 'http' in URL: {url23}")
        url24 = urlfe.https_token(scheme)
        print(f"Use of HTTPS (yes = 0; no = 1): {url24}") 
        url25 = urlfe.ratio_digits(url)
        print(f"Ratio of digits in URL: {url25}")
        url26 = urlfe.ratio_digits(hostname)
        print(f"Ratio of digits in host: {url26}")
        url27 = urlfe.punycode(url)
        print(f"Presence of punycode: {url27}")
        url28 = urlfe.port(url)
        print(f"Presence of port: {url28}")
        url29 = urlfe.tld_in_path(tld, path)
        print(f"Presence of TLD in path: {url29}")
        url30 = urlfe.tld_in_subdomain(tld, subdomain)
        print(f"Presence of TLD in subdomain: {url30}")
        url31 = urlfe.abnormal_subdomain(url)
        print(f"Abnormal subdomain: {url31}")
        url32 = urlfe.count_subdomain(url)
        print(f"Number of subdomain in URL: {url32}")
        url33 = urlfe.prefix_suffix(url)
        print(f"Prefixes and suffixes separated by - in URL: {url33}")
        # urlfe.random_domain(domain),
        url34 = urlfe.shortening_service(url)
        print(f"Use of shortening service: {url34}")
        url35 = urlfe.path_extension(path)
        print(f"Presence of path extension in URL path: {url35}")
        url36 = urlfe.count_redirection(page)
        print(f"Number of redirections: {url36}")
        url37 = urlfe.count_external_redirection(page, domain)
        print(f"Number of external redirections: {url37}")
        url38 = urlfe.length_word_raw(words_raw)
        print(f"Number of words in URL: {url38}")
        url39 = urlfe.char_repeat(words_raw)
        print(f"Number of consecutive characters in URL: {url39}")
        url40 = urlfe.shortest_word_length(words_raw)
        print(f"Length of shortest word in URL: {url40}")
        url41 = urlfe.shortest_word_length(words_raw_host)
        print(f"Length of shortest word in host: {url41}")
        url42 = urlfe.shortest_word_length(words_raw_path)
        print(f"Length of shortest word in path: {url42}")
        url43 = urlfe.longest_word_length(words_raw)
        print(f"Length of longest word in URL: {url43}")
        url44 = urlfe.longest_word_length(words_raw_host)
        print(f"Length of longest word in host: {url44}")
        url45 = urlfe.longest_word_length(words_raw_path)
        print(f"Length of longest word in path: {url45}")
        url46 = urlfe.average_word_length(words_raw)
        print(f"Average word length in URL: {url46}")
        url47 = urlfe.average_word_length(words_raw_host)
        print(f"Average word length in host: {url47}")
        url48 = urlfe.average_word_length(words_raw_path)
        print(f"Average word length in path: {url48}")
        url49 = urlfe.phish_hints(url)
        print(f"Number of phish hints in URL: {url49}")
        url50 = urlfe.domain_in_brand(extracted_domain.domain)
        print(f"Presence of brands in domain: {url50}")
        url51 = urlfe.brand_in_path(extracted_domain.domain,subdomain)
        print(f"Presence of brands in subdomain: {url51}")
        url52 = urlfe.brand_in_path(extracted_domain.domain,path)
        print(f"Presence of brands in path: {url52}")
        url53 = urlfe.suspecious_tld(tld)
        print(f"Presence of suspicious TLD: {url53}")
        url54 = urlfe.statistical_report(url, domain)
        print(f"URL in top phishing domains: {url54}")

        ### content-based features
        ctn1 = ctnfe.nb_hyperlinks(Href, Link, Media, Form, CSS, Favicon)
        print(f"Number of hyperlinks: {ctn1}")
        ctn2 = ctnfe.internal_hyperlinks(Href, Link, Media, Form, CSS, Favicon)
        print(f"Ratio of internal hyperlinks: {ctn2}")
        ctn3 = ctnfe.external_hyperlinks(Href, Link, Media, Form, CSS, Favicon)
        print(f"Ratio of external hyperlinks: {ctn3}")
        # ctnfe.null_hyperlinks(hostname, Href, Link, Media, Form, CSS, Favicon),
        ctn4 = ctnfe.external_css(CSS)
        print(f"Number of external CSS: {ctn4}")
        # ctnfe.internal_redirection(Href, Link, Media, Form, CSS, Favicon),
        ctn5 = ctnfe.external_redirection(Href, Link, Media, Form, CSS, Favicon)
        print(f"Ratio of external redirections: {ctn5}")
        # ctnfe.internal_errors(Href, Link, Media, Form, CSS, Favicon),
        ctn6 = ctnfe.external_errors(Href, Link, Media, Form, CSS, Favicon)
        print(f"Ratio of external errors: {ctn6}")
        ctn7 = ctnfe.login_form(Form)
        print(f"Presence of login form: {ctn7}")
        ctn8 = ctnfe.external_favicon(Favicon)
        print(f"Use of external favicon: {ctn8}")
        ctn9 = ctnfe.links_in_tags(Link)
        print(f"Percentile of links in tags: {ctn9}")
        # ctnfe.submitting_to_email(Form),
        ctn10 = ctnfe.internal_media(Media)
        print(f"Ratio of internal media: {ctn10}")
        ctn11 = ctnfe.external_media(Media)
        print(f"Ratio of external media: {ctn11}")

        ### additional content-based features
        # ctnfe.sfh(hostname, Form),
        ctn12 = ctnfe.iframe(IFrame)
        print(f"Use of invisible <iframe> tags: {ctn12}")
        ctn13 = ctnfe.popup_window(Text)
        print(f"Presence of popup window with text field: {ctn13}")
        ctn14 = ctnfe.safe_anchor(Anchor)
        print(f"Percentile of safe anchors: {ctn14}")
        ctn15 = ctnfe.onmouseover(Text)
        print(f"Presence of onmouseover: {ctn15}")
        ctn16 = ctnfe.right_clic(Text)
        print(f"Use of ’event.button==2’ to onmouseover: {ctn16}")
        ctn17 = ctnfe.empty_title(Title)
        print(f"Empty title: {ctn17}")
        ctn18 = ctnfe.domain_in_title(extracted_domain.domain, Title)
        print(f"Domain as web title: {ctn18}")
        ctn19 = ctnfe.domain_with_copyright(extracted_domain.domain, Text)
        print(f"Presence of domain within the copyright: {ctn19}")

        ### third-party-based features
        # trdfe.whois_registered_domain(domain),
        # trdfe.domain_registration_length(domain),
        # trdfe.domain_age(domain),
        # trdfe.web_traffic(url),
        trd1 = trdfe.dns_record(domain)
        print(f"DNS record: {trd1}")
        # trdfe.google_index(url),
        trd2 = trdfe.page_rank(key,domain)
        print(f"Openpagerank: {trd2}")

        row = [
            url1, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12, url13, url14, url15, url16, url17, url18, url19, url20, url21, url22, url23, url24, url25, url26, url27, url28, url29, url30, url31, url32, url33, url34, url35, url36, url37, url38, url39, url40, url41, url42, url43, url44, url45, url46, url47, url48, url49, url50, url51, url52, url53, url54, ctn1, ctn2, ctn3, ctn4, ctn5, ctn6, ctn7, ctn8, ctn9, ctn10, ctn11, ctn12, ctn13, ctn14, ctn15, ctn16, ctn17, ctn18, ctn19, trd1, trd2
        ]
        return row
    return None