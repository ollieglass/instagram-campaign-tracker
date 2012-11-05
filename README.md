Quick and dirty Instagram campaign tracker
==========================================

See my [Instagram campaing reporting blog post](http://ollieglass.com/2012/11/05/instagram-campaign-reporting) for details

To use:

1. Login to the Instagram API console, copy the access token.
2. In download_data.py:
  * Paste your access token into the access_token variable
  * Change the hashtag variable to whatever you're intested in.

3. Run download_data.py for a while. It paginates through Instagram's results. Quit when you have a few pages.
4. Run parse_data.py and see some stats on the campaign.