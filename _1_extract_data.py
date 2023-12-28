import csv
import os
from googleapiclient.discovery import build

def get_most_viewed_videos(country, max_results=50, next_page_token=None):
    results = youtube.videos().list(
        part='snippet,contentDetails,statistics',
        chart='mostPopular',
        regionCode=country,
        videoCategoryId='0',
        maxResults=max_results,
        pageToken=next_page_token
    ).execute()

    return results['items'], results.get('nextPageToken')

api_key = 'AIzaSyBmcBQxRVAFP1P2cAbIetoJycXz8VvmVG8'
youtube = build('youtube', 'v3', developerKey=api_key)

brazil_videos = []
next_page_token = None

while len(brazil_videos) < 10000:
    videos, next_page_token = get_most_viewed_videos('JP', max_results=50, next_page_token=next_page_token)
    brazil_videos.extend(videos)

    if not next_page_token:
        break

directory = r'C:\Users\joaov\Documents\Code\GithubProjects\DataScience\YoutubeDataAnalysis\data'
csv_filename = 'database.csv'

csv_header = ['VideoId', 'Title', 'PublishedAt', 'ChannelId', 'ChannelTitle', 'CategoryId', 'ViewCount', 'LikeCount', 'DislikeCount', 'CommentCount']

with open(os.path.join(directory, csv_filename), 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(csv_header)

    for video in brazil_videos:
        csv_writer.writerow([
            video['id'],
            video['snippet']['title'],
            video['snippet']['publishedAt'],
            video['snippet']['channelId'],
            video['snippet']['channelTitle'],
            video['snippet']['categoryId'],
            video['statistics']['viewCount'],
            video['statistics'].get('likeCount', 0),
            video['statistics'].get('dislikeCount', 0),
            video['statistics'].get('commentCount', 0)
        ])

print(f'Dados salvos com sucesso!')
