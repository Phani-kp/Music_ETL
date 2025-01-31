# Install the Spotipy library
!pip install spotipy

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'your_redirect_uri'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='user-follow-read'))

# Function to get followed artists
def get_followed_artists(sp):
    followed_artists = []
    results = sp.current_user_followed_artists(limit=20)
    
    while results:
        followed_artists.extend(results['artists']['items'])
        if results['artists']['next']:
            results = sp.next(results['artists'])
        else:
            break
    
    return followed_artists

# Retrieve and print the followed artists
followed_artists = get_followed_artists(sp)
for artist in followed_artists:
    print(artist['name'])
