import re

def nb_hyperlinks(Href, Link, Media, Form, CSS, Favicon): # column: nb_hyperlinks
    return len(Href['internals']) + len(Href['externals']) +\
           len(Link['internals']) + len(Link['externals']) +\
           len(Media['internals']) + len(Media['externals']) +\
           len(Form['internals']) + len(Form['externals']) +\
           len(CSS['internals']) + len(CSS['externals']) +\
           len(Favicon['internals']) + len(Favicon['externals'])

# def nb_hyperlinks(dom): # column: nb_hyperlinks
#     return len(dom.find("href")) + len(dom.find("src"))

def h_total(Href, Link, Media, Form, CSS, Favicon):
    return nb_hyperlinks(Href, Link, Media, Form, CSS, Favicon)

def h_internal(Href, Link, Media, Form, CSS, Favicon):
    return len(Href['internals']) + len(Link['internals']) + len(Media['internals']) +\
           len(Form['internals']) + len(CSS['internals']) + len(Favicon['internals'])

def internal_hyperlinks(Href, Link, Media, Form, CSS, Favicon): # column: ratio_intHyperlinks
    total = h_total(Href, Link, Media, Form, CSS, Favicon)
    if total == 0:
        return 0
    else :
        return h_internal(Href, Link, Media, Form, CSS, Favicon)/total

def h_external(Href, Link, Media, Form, CSS, Favicon):
    return len(Href['externals']) + len(Link['externals']) + len(Media['externals']) +\
           len(Form['externals']) + len(CSS['externals']) + len(Favicon['externals'])
                   
def external_hyperlinks(Href, Link, Media, Form, CSS, Favicon): # column: ratio_extHyperlinks
    total = h_total(Href, Link, Media, Form, CSS, Favicon)
    if total == 0:
        return 0
    else :
        return h_external(Href, Link, Media, Form, CSS, Favicon)/total

def external_css(CSS): # column: nb_extCSS
    return len(CSS['externals'])

def login_form(Form): # column: login_form
    p = re.compile('([a-zA-Z0-9\_])+.php')
    if len(Form['externals'])>0 or len(Form['null'])>0:
        return 1
    for form in Form['internals']+Form['externals']:
        if p.match(form) != None :
            return 1
    return 0

def external_favicon(Favicon): # column: external_favicon
    if len(Favicon['externals'])>0:
        return 1
    return 0

def links_in_tags(Link): # column: links_in_tags
    total = len(Link['internals']) +  len(Link['externals'])
    internals = len(Link['internals'])
    try:
        percentile = internals / float(total) * 100
    except:
        return 0
    return percentile

def internal_media(Media): # column: ratio_intMedia
    total = len(Media['internals']) + len(Media['externals'])
    internals = len(Media['internals'])
    try:
        percentile = internals / float(total) * 100
    except:
        return 0
    
    return percentile

def external_media(Media): # column: ratio_extMedia
    total = len(Media['internals']) + len(Media['externals'])
    externals = len(Media['externals'])
    try:
        percentile = externals / float(total) * 100
    except:
        return 0
    
    return percentile

def iframe(IFrame): # column: iframe
    if len(IFrame['invisible'])> 0: 
        return 1
    return 0

def popup_window(content): # column: popup_window
    if "prompt(" in str(content).lower():
        return 1
    else:
        return 0

def safe_anchor(Anchor): # column: safe_anchor
    total = len(Anchor['safe']) +  len(Anchor['unsafe'])
    unsafe = len(Anchor['unsafe'])
    try:
        percentile = unsafe / float(total) * 100
    except:
        return 0
    return percentile 

def onmouseover(content): # column: onmouseover
    if 'onmouseover="window.status=' in str(content).lower().replace(" ",""):
        return 1
    else:
        return 0

def right_clic(content): # column: right_clic
    if re.findall(r"event.button ?== ?2", content):
        return 1
    else:
        return 0

def empty_title(Title): # column: empty_title
    if Title:
        return 0
    return 1

def domain_in_title(domain, title): # column: domain_in_title
    if domain.lower() in title.lower(): 
        return 0
    return 1

def domain_with_copyright(domain, content): # column: domain_with_copyright
    try:
        m = re.search(u'(\N{COPYRIGHT SIGN}|\N{TRADE MARK SIGN}|\N{REGISTERED SIGN})', content)
        _copyright = content[m.span()[0]-50:m.span()[0]+50]
        if domain.lower() in _copyright.lower():
            return 0
        else:
            return 1 
    except:
        return 0
