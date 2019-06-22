## France Clickstream

The current data includes the following 4 fields:

### n:
- the number of occurrences of the (referer, resource) pair

### prev:
- the result of mapping the referer URL to the fixed set of values described above
```
an article in the main namespace -> the article title
a page from any other Wikimedia project -> other-internal
an external search engine -> other-search
any other external site -> other-external
an empty referer -> other-empty
anything else -> other-other
```

```
It will/may be empty when the enduser

entered the site URL in browser address bar itself.
visited the site by a browser-maintained bookmark.
visited the site as first page in the window/tab.
clicked a link in an external application.
switched from a https URL to a http URL.
switched from a https URL to a different https URL.
has security software installed (antivirus/firewall/etc) which strips the referrer from all requests.
is behind a proxy which strips the referrer from all requests.
visited the site programmatically (like, curl) without setting the referrer header (searchbots!).
```

### curr:
- the title of the article the client requested

### type:
- describes (prev, curr)
- link: 
    - if the referer and request are both articles and the referer links to the request
- external: 
    - if the referer host is not en(.m)?.wikipedia.org
- other
    - if the referer and request are both articles but the referer does not link to the request. This can happen when clients search or spoof their refer.


- https://stackoverflow.com/questions/6880659/in-what-cases-will-http-referer-be-empty
- https://data36.com/pandas-tutorial-2-aggregation-and-grouping/
- https://meta.wikimedia.org/wiki/Research:Wikipedia_clickstream#Format

# German Wikipedia clickstream
- The data shows how people get to a Wikipedia article and what articles they click on next.
- most people found the X page through Google Search and that only a small fraction of readers went on to another article

## Ideas
- determine the most frequent links people click on for a given article
- determine the most common links people followed to an article
- determine how much of the total traffic to an article clicked on a link in that article

- Top article of the 3 month 2019 (and december 2018) 
- Top referrer
- What's the most trending on twitter per month
- Most requested missing pages
- Is there more traffic going into an article or going out of an article 

## Referrer -> Resource pair
- an article in the main namespace -> the article title
- a page from any other Wikimedia project -> other-internal
- an external search engine -> other-search
- any other external site -> other-external
- an empty referer -> other-empty
- anything else -> other-other
```

an article in the main namespace of German Wikipedia -> 
the article title
    any Wikipedia page that is not in the main namespace of German Wikipedia -> other-wikipedia
    an empty referer -> other-empty
    a page from any other Wikimedia project -> other-internal
    Google -> other-google
    Yahoo -> other-yahoo
    Bing -> other-bing
    Facebook -> other-facebook
    Twitter -> other-twitter
    anything else -> other-other

```

## Format

The data includes the following 6 fields:

### prev_id: 
- if the referer does not correspond to an article in the main namespace of English Wikipedia, this value will be empty. Otherwise, it contains the unique MediaWiki page ID of the article corresponding to the referer i.e. the previous article the client was on

### curr_id: 
- the MediaWiki unique page ID of the article the client requested
### n: 
- the number of occurrences of the (referer, resource) pair
### prev_title: 
- the result of mapping the referer URL to the fixed set of values described above
### curr_title: 
- the title of the article the client requested
### type
- `"link"` if the referer and request are both articles and the referer links to the request
- `"redlink"` if the referer is an article and links to the request, but the request is not in the produiction enwiki.page table
- `"other"` if the referer and request are both articles but the referer does not link to the request. This can happen when clients search or spoof their refer

## References
- https://meta.wikimedia.org/wiki/Research:Wikipedia_clickstream#Format
- https://github.com/valgog/wmf/blob/master/clickstream/ipython/Wikipedia%20Clickstream%20-%20Getting%20Started-Extended.ipynb
- https://dumps.wikimedia.org/other/clickstream/readme.html