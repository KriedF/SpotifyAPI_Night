import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timezone
import time
import yaml

# Load configuration files
with open('system_config.yml') as f:
    system_config = yaml.load(f, Loader=yaml.FullLoader)

with open('user_config.yml') as f:
    user_config = yaml.load(f, Loader=yaml.FullLoader)

with open('analysis_config.yml') as f:
    analysis_config = yaml.load(f, Loader=yaml.FullLoader)

# Set up Spotify API credentials
CLIENT_ID = system_config['spotify_api']['client_id']
CLIENT_SECRET = system_config['spotify_api']['client_secret']
REDIRECT_URI = system_config['spotify_api']['redirect_uri']
SCOPE = user_config['user']['scope']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

try:
    # Measure the time taken to fetch recent tracks
    start_time = time.time()
    recent_tracks = sp.current_user_recently_played(limit=analysis_config['analysis']['track_limit'])
    print(f"Analyzing your recent tracks... Time taken: {time.time() - start_time:.2f} seconds")

    # Filter tracks listened to at night
    night_tracks = [track for track in recent_tracks['items'] if 0 <= datetime.fromisoformat(track['played_at'][:-1]).replace(tzinfo=timezone.utc).hour <= 6]

    # Measure the time taken to filter tracks
    start_time = time.time()
    night_tracks = [track for track in recent_tracks['items'] if 0 <= datetime.fromisoformat(track['played_at'][:-1]).replace(tzinfo=timezone.utc).hour <= 6]
    print(f"Filtering tracks listened to at night... Time taken: {time.time() - start_time:.2f} seconds")

    # Count artist occurrences
    artist_count = {}
    for track in night_tracks:
        artist = track['track']['artists'][0]['name']
        artist_count[artist] = artist_count.get(artist, 0) + 1

    # Find most listened-to artist
    most_listened_artist = max(artist_count, key=artist_count.get)

    print(f"The most listened-to artist at night is: {most_listened_artist}")

    # Measure the time taken for the rest of the processing
    start_time = time.time()
    print(f"Completing analysis... Time taken: {time.time() - start_time:.2f} seconds")

except Exception as e:
    print(f"Error: {e}")
