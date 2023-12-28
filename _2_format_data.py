import csv
import os

category_mapping = {
    '1': 'Film & Animation',
    '2': 'Autos & Vehicles',
    '10': 'Music',
    '15': 'Pets & Animals',
    '17': 'Sports',
    '18': 'Short Movies',
    '19': 'Travel & Events',
    '20': 'Gaming',
    '21': 'Videoblogging',
    '22': 'People & Blogs',
    '23': 'Comedy',
    '24': 'Entertainment',
    '25': 'News & Politics',
    '26': 'Howto & Style',
    '27': 'Education',
    '28': 'Science & Technology',
    '29': 'Nonprofits & Activism',
    '30': 'Movies',
    '31': 'Anime/Animation',
    '32': 'Action/Adventure',
    '33': 'Classics',
    '34': 'Comedy',
    '35': 'Documentary',
    '36': 'Drama',
    '37': 'Family',
    '38': 'Foreign',
    '39': 'Horror',
    '40': 'Sci-Fi/Fantasy',
    '41': 'Thriller',
    '42': 'Shorts',
    '43': 'Shows',
    '44': 'Trailers',
    '45': 'Gaming',
    '46': 'Vlog',
    '47': 'Style',
    '48': 'Cooking',
    '49': 'How-to & DIY',
    '50': 'Fitness',
    '51': 'Sports',
    '52': 'Gaming',
    '53': 'Music',
    '54': 'Movies',
    '55': 'News & Politics',
    '56': 'Science & Technology',
    '57': 'Fashion & Beauty',
    '58': 'Nonprofit & Activism',
    '59': 'Travel & Events',
    '60': 'Gaming',
    '61': 'Videoblogging',
    '62': 'People & Blogs',
    '63': 'Comedy',
    '64': 'Entertainment',
    '65': 'News & Politics',
    '66': 'Howto & Style',
    '67': 'Education',
    '68': 'Science & Technology',
    '69': 'Nonprofits & Activism',
    '70': 'Movies',
    '71': 'Anime/Animation',
    '72': 'Action/Adventure',
    '73': 'Classics',
    '74': 'Comedy',
    '75': 'Documentary',
    '76': 'Drama',
    '77': 'Family',
    '78': 'Foreign',
    '79': 'Horror',
    '80': 'Sci-Fi/Fantasy',
    '81': 'Thriller',
    '82': 'Shorts',
    '83': 'Shows',
    '84': 'Trailers'
}

file_path = r'C:\Users\joaov\Documents\Code\GithubProjects\DataScience\YoutubeDataAnalysis\data\database_BR.csv'

with open(file_path, 'r+', encoding='utf-8', newline='') as original_csv_file:
    csv_reader = csv.reader(original_csv_file)
    
    header = next(csv_reader)

    index_category_id = header.index('CategoryId')

    converted_data = []
    for row in csv_reader:
        row[index_category_id] = category_mapping.get(row[index_category_id], 'Unknown')
        converted_data.append(row)

    # Move the file cursor to the beginning
    original_csv_file.seek(0)

    csv_writer = csv.writer(original_csv_file)
    
    csv_writer.writerow(header)
    
    csv_writer.writerows(converted_data)

print('Dados alterados com sucesso')
