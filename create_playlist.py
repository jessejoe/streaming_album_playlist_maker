#!/usr/bin/env python

import click
import spotipy
import spotipy.util as util


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option(
    '--username',
    help='Spotify username to create the playlist with',
    required=True)
@click.option(
    '--client_id',
    help='Client ID from your appplication, can be set with env var SPOTIPY_CLIENT_ID',
    envvar='SPOTIPY_CLIENT_ID',
    required=True)
@click.option(
    '--client_secret',
    help='Client Secret from your application, can be set with env var SPOTIPY_CLIENT_SECRET',
    envvar='SPOTIPY_CLIENT_SECRET',
    required=True)
@click.option(
    '--redirect_uri',
    help='A whitelisted Redirect URI for your application, can be set with env var SPOTIPY_REDIRECT_URI',
    envvar='SPOTIPY_REDIRECT_URI',
    required=True)
@click.option(
    '--playlist_name', help='Name of playlist to create', required=True)
@click.argument('input_file', type=click.Path(exists=True))
def main(username, client_id, client_secret, redirect_uri, playlist_name,
         input_file):
    """
    This script will take a list of album names from INPUT_FILE and create a
    playlist of all their tracks

    See https://developer.spotify.com/web-api/tutorial/ for how to register
    an application to get a client_id, client_secret, and redirect_uri
    """
    token = util.prompt_for_user_token(
        username=username,
        scope='playlist-modify-public',
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth=token)
    user_id = sp.current_user()['id']

    with open(input_file) as f:
        albums = f.read().splitlines()

    track_ids = []
    found_albums = []
    not_found_albums = []
    for album in albums:
        search_resp = sp.search(album, type="album", limit=1)
        if not search_resp['albums']['total']:
            not_found_albums.append(album)
            print('No result found: for "{}"'.format(album))
            continue

        first_result = search_resp['albums']['items'][0]
        # 'artists' is a list of dicts, so assume there can be more than one
        # and join them
        album_artists = ', '.join(
            [artist['name'] for artist in first_result['artists']])
        album_name = first_result['name']
        album_id = first_result['id']
        print('Found album: "{} - {}"'.format(album_artists, album_name))
        found_albums.append(album_id)

    # Instead of querying 1 album at a time, batch lookup 20 at a time
    for chunk in chunks(found_albums, 20):
        batch_album_res = sp.albums(chunk)
        for album in batch_album_res['albums']:
            tracks = album['tracks']['items']
            print('Found {} tracks for "{}"'.format(len(tracks), album['name']))
            track_ids += [track['id'] for track in tracks]

    print('\nFound {} albums for {} search terms'.format(
        len(found_albums), len(albums)))
    if not_found_albums:
        quoted_not_found_albums = [
            '"' + album + '"' for album in not_found_albums
        ]
        print('No results found for:\n{}\n'.format('\n'.join(
            quoted_not_found_albums)))

    while True:
        user_input = input(
            'Create playlist of {} tracks? [Y/N]: '.format(len(track_ids)))
        if user_input in ['Y', 'N']:
            break
        else:
            print('Invalid option')

    if user_input != 'Y':
        raise SystemExit

    print('Creating playlist: "{}"'.format(playlist_name))
    create_resp = sp.user_playlist_create(user_id, playlist_name)
    playlist_uri = create_resp['uri']
    playlist_public_url = create_resp['external_urls']['spotify']
    print('Created playlist at {} (external url: {} )'.format(
        playlist_uri, playlist_public_url))
    # Spotify limits adding 100 tracks at a time to a playlist
    chunk_size = 100
    for chunk in chunks(track_ids, chunk_size):
        print('Adding {} tracks to playlist...'.format(len(chunk)))
        add_track_res = sp.user_playlist_add_tracks(user_id, create_resp['id'],
                                                    chunk)
        # Don't get much back from this method, but the response should at
        # least contain 'snapshot_id'
        assert 'snapshot_id' in add_track_res, "Did not receive a 'snapshot_id' after adding tracks"
    print('All tracks added successfully!')


def chunks(l, n):
    """
    Yield successive n-sized chunks from l
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    main()
