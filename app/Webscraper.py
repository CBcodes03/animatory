import requests
from bs4 import BeautifulSoup

# Initial URL
base_url = 'https://myanimelist.net/clubs.php?action=view&t=members&id=20081&show='

# Accumulate profile names for multiple URLs
all_profile_names = []

for offset in range(0, 3600, 36):  # Adjust the range as needed
    url = f'{base_url}{offset}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    profile_names = []

    for row in soup.find_all('tr'):
        columns = row.find_all('td', class_='borderClass')
        for col in columns:
            profile_name = col.find('a').text.strip()
            profile_names.append(profile_name)

    all_profile_names.extend(profile_names)

# Print the final list of profile names
print('All Profile Names:', all_profile_names)

# Construct list of URLs with usernames replaced
profile_urls = ['https://myanimelist.net/animelist/{}'.format(username) for username in all_profile_names]

# Print the list of profile URLs
print('Profile URLs:', profile_urls)
