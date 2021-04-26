## UK Bus Companies and Developers

### The Dilemma

Here in the UK, our buses are ran by private companies, such as TfL (Transport for London), Traveline (who own Stagecoach) and Arriva. In my local area, Stagecoach is the company that provides our bus services. What I wanted to do was make a small customised website for myself that showed me the bus times for the bus stops I might need. My first instinct was to look for an API. There were two options I found: NextBuses API, which you have to apply for (and I am yet to receive a response from) and Transport API which only allows 1000 "hits" per day, of which the requests I was looking to make took up around 10 hits each, so not ideal, as I would be requesting once or twice a minute. The first option seems to only allow companies to use their API, which isn't great for an individual such as myself.

### The Solution - Scraping

To access live information that I would quite like to access in the mornings, I either need to accept a limit, be a company or find another way. Inevitably, as the article description suggests, I found another way. I found that if I could scrape the bus stop pages on my local bus company's website, then I would be able to get the bus times live, as they were being provided by an accurate source that both their site and app used. Now that wasn't easy. Their website seems to have some form of scraping protection, as they have a loading symbol when you first load up the site, and then they have times which are a few minutes off at first (that can't be seen as they go away after about 0.1s) and then they finally load the correct times. To get around this, I had to make it seem that I was requesting as a browser, so I used the puppeteer tool for node.js to do that. This not only allowed me to look as though I was an actual user requesting this data, I was also able to wait for the page to load before fetching the data and feeding it into cheerio, allowing me to get accurate times for the buses, which is, obviously, ideal when checking live times in the morning

I can't make the code that I use for this public, as I have to provide bus stop URLs to the code, which can reveal where I live & where I travel to, sensitive info I'd rather not made public.

### Why is this a problem in the first place?

The UK government is usually quite helpful when providing APIs you can use for all kinds of country-wide services, they even have a [catalogue](https://www.api.gov.uk/#uk-government-apis) of all the APIs for UK services that you can use and most of the time, these are useful. However, the bus companies in the UK have been privatised for a while now, meaning they handle the way APIs are run on their end, which causes issues such as these. While there are solutions such as Transport API, this isn't official, and I can't seem to find a way to upgrade your plan like they say is possible. So, for now, I suppose web scraping seems like the only option.
