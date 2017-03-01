# Spotify Album Playlist Maker

This is a script to take a file containing a list of album names, and creates a Spotify playlist of them.

I often find "best of" lists that I want to create a playlist of, or I want to make a playlist of an artist's studio discography. It's tedious searching and adding album after album, so this automates it for you. I couldn't find something like this out there already.

## Authentication

You will need to create an application in the [Spotify Developer portal](https://developer.spotify.com/my-applications) in order to generate your own Client ID, Client Secret, and Redirect URI to use with this script. See [here](https://developer.spotify.com/web-api/tutorial/) for more information.

The script uses the [Spotipy python client library](http://spotipy.readthedocs.io/en/latest/) for most of the real work. The first time you run the script it should launch a browser window and prompt you to give your application (this script using your keys) permission to be able to create public playlists. See the [Spotipy docs on Authorization](http://spotipy.readthedocs.io/en/latest/#authorized-requests) for more details.

## Requirements

You will need to install the libraries in the `requirements.txt` file:
```
pip install -r requirements.txt
```

## Running the script

Create a text file with a list of album names (1 per line) called `input.txt`. Ran the script with all the parameters for your application substituted:
```
./create_playlist.py --username my_username --client_id 12345 --client_secret ABCDE --redirect_uri https://example.com/callback/ --playlist_name '39 essential albums for audiophiles' input.txt
```

## Example

Using the list from http://www.stuff.tv/features/39-essential-albums-audiophiles create a file called `input.txt` containing the following:
```
Radiohead A Moon Shaped Pool
Nirvana In Utero 20th Anniversary Deluxe Edition
Interpol Turn On The Bright Lights The Tenth Anniversary Edition
My Bloody Valentine Loveless
Dr Dre 2001
Marvin Gaye What’s Going On
Nirvana MTV Unplugged in New York
The Beatles Abbey Road
Bon Iver Bon Iver
R.E.M. Automatic for the People
Dusty Springfield Dusty in Memphis
Burial Untrue
The Flaming Lips The Soft Bulletin
The xx xx
Rage Against The Machine Rage Against The Machine
Jay-Z The Blueprint
Animal Collective Merriweather Post Pavilion
Fleetwood Mac Rumours
OutKast Speakerboxxx/The Love Below
Steely Dan Aja
Joni Mitchell Blue
Daft Punk Random Access Memories
Miles Davis Kind of Blue
Sigur Ros Agaetis Byrjun
Neil Young After The Gold Rush
Radiohead OK Computer
Prince Sign o’ the Times
The Congos Heart Of The Congos
Pink Floyd Wish You Were Here
Jeff Buckley Grace
Michael Jackson Thriller
Massive Attack Mezzanine
Underworld Second Toughest in the Infants
Slint Spiderland
Phil Collins Hello, I Must Be Going
Love Forever Changes
My Morning Jacket It Still Moves
Isis Panopticon
Manic Street Preachers The Holy Bible
```

The script will only look for albums, so putting the artist on the line will help make sure the correct album is found when searching.

Run the script:
```
./create_playlist.py --username my_username --client_id 12345 --client_secret ABCDE --redirect_uri https://example.com/callback/ --playlist_name '39 essential albums for audiophiles' input.txt
```

The script should run with the following output:
```
Found album: "Radiohead - A Moon Shaped Pool"
Found album: "Nirvana - In Utero - 20th Anniversary - Deluxe Edition"
Found album: "Interpol - Turn On The Bright Lights: The Tenth Anniversary Edition (Remastered)"
Found album: "My Bloody Valentine - Loveless"
Found album: "Dr. Dre - 2001"
Found album: "Marvin Gaye - What's Going On - 40th Anniversary (Super Deluxe)"
Found album: "Nirvana - MTV Unplugged In New York"
Found album: "The Beatles - Abbey Road (Remastered)"
Found album: "Bon Iver - Bon Iver"
Found album: "R.E.M. - Automatic For The People"
Found album: "Dusty Springfield - Dusty In Memphis [Deluxe Edition]"
Found album: "Burial - Untrue"
Found album: "The Flaming Lips - The Soft Bulletin"
Found album: "The xx - xx"
Found album: "Rage Against The Machine - Rage Against The Machine - XX (20th Anniversary Special Edition)"
No result found: for "Jay-Z The Blueprint"
Found album: "Animal Collective - Merriweather Post Pavilion"
Found album: "Fleetwood Mac - Rumours (Super Deluxe)"
Found album: "OutKast - Speakerboxxx/The Love Below"
Found album: "Steely Dan - Aja"
Found album: "Joni Mitchell - Blue"
Found album: "Daft Punk - Random Access Memories"
Found album: "Miles Davis - Kind Of Blue (Legacy Edition)"
Found album: "Sigur Rós - Ágætis Byrjun"
Found album: "Neil Young - After The Gold Rush (Remastered Version)"
Found album: "Radiohead - OK Computer"
Found album: "Prince - Sign 'O' The Times"
Found album: "The Congos - Heart Of The Congos"
Found album: "Pink Floyd - Wish You Were Here"
Found album: "Jeff Buckley - Grace (Legacy Edition)"
Found album: "Michael Jackson - Thriller 25 Super Deluxe Edition"
Found album: "Massive Attack - Mezzanine"
Found album: "Underworld - Second Toughest In The Infants (Deluxe / Remastered)"
Found album: "Slint - Spiderland (remastered)"
Found album: "Phil Collins - Hello, I Must Be Going! (Deluxe Edition)"
Found album: "Love - Forever Changes (2015 Remastered Version)"
Found album: "My Morning Jacket - It Still Moves"
Found album: "ISIS - Panopticon (Remastered)"
Found album: "Manic Street Preachers - The Holy Bible 20 (Remastered)"
Found 11 tracks for "A Moon Shaped Pool"
Found 43 tracks for "In Utero - 20th Anniversary - Deluxe Edition"
Found 28 tracks for "Turn On The Bright Lights: The Tenth Anniversary Edition (Remastered)"
Found 11 tracks for "Loveless"
Found 23 tracks for "2001"
Found 46 tracks for "What's Going On - 40th Anniversary (Super Deluxe)"
Found 14 tracks for "MTV Unplugged In New York"
Found 17 tracks for "Abbey Road (Remastered)"
Found 10 tracks for "Bon Iver"
Found 12 tracks for "Automatic For The People"
Found 25 tracks for "Dusty In Memphis [Deluxe Edition]"
Found 13 tracks for "Untrue"
Found 14 tracks for "The Soft Bulletin"
Found 11 tracks for "xx"
Found 25 tracks for "Rage Against The Machine - XX (20th Anniversary Special Edition)"
Found 11 tracks for "Merriweather Post Pavilion"
Found 50 tracks for "Rumours (Super Deluxe)"
Found 40 tracks for "Speakerboxxx/The Love Below"
Found 7 tracks for "Aja"
Found 10 tracks for "Blue"
Found 13 tracks for "Random Access Memories"
Found 21 tracks for "Kind Of Blue (Legacy Edition)"
Found 10 tracks for "Ágætis Byrjun"
Found 11 tracks for "After The Gold Rush (Remastered Version)"
Found 12 tracks for "OK Computer"
Found 16 tracks for "Sign 'O' The Times"
Found 10 tracks for "Heart Of The Congos"
Found 5 tracks for "Wish You Were Here"
Found 22 tracks for "Grace (Legacy Edition)"
Found 30 tracks for "Thriller 25 Super Deluxe Edition"
Found 11 tracks for "Mezzanine"
Found 18 tracks for "Second Toughest In The Infants (Deluxe / Remastered)"
Found 20 tracks for "Spiderland (remastered)"
Found 21 tracks for "Hello, I Must Be Going! (Deluxe Edition)"
Found 11 tracks for "Forever Changes (2015 Remastered Version)"
Found 12 tracks for "It Still Moves"
Found 7 tracks for "Panopticon (Remastered)"
Found 13 tracks for "The Holy Bible 20 (Remastered)"

Found 38 albums for 39 search terms
No results found for:
"Jay-Z The Blueprint"

Create playlist of 684 tracks? [Y/N]: Y
Creating playlist: "39 essential albums for audiophiles"
Created playlist at spotify:user:my_username:playlist:12345ABCDE (external url: http://open.spotify.com/user/my_username/playlist/12345ABCDE )
Adding 100 tracks to playlist...
Adding 100 tracks to playlist...
Adding 100 tracks to playlist...
Adding 100 tracks to playlist...
Adding 100 tracks to playlist...
Adding 100 tracks to playlist...
Adding 84 tracks to playlist...
All tracks added successfully!
```

## Notes

The script does as much batching as possible for looking up album tracks and adding tracks to playlists, however there is no API for batch searching. It's possible to get rate limited if you hit the API too frequently. As shown above, I've been able to run the script with 38 albums and 684 tracks without issue, so I have not added any logic for honoring Spotify's [rate limiting](https://developer.spotify.com/web-api/user-guide/#rate-limiting) or `Retry-After` headers.
