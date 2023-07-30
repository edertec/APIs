import requests

# Get the API key from Steam
API_KEY = "C0D3F4398699BD76BC085E41E04B77D6"

# Make a request to the Steam API
response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=" + API_KEY)

# Decode the response body
response_body = response.json()

# Get the list of games
games = response_body["applist"]["apps"]

# Create a HTML table
table = """
<table>
<tr>
<th>App ID</th>
<th>Name</th>
</tr>
"""

# Iterate over the games
for game in games:
    # Add a row to the table
    table += """
    <tr>
    <td>{appid}</td>
    <td>{name}</td>
    </tr>
    """.format(appid=game["appid"], name=game["name"])
    continue

# Close the table
table += "</table>"

# Print the table to the console
print(table)

# Save the table to a file
with open("games.html", "w") as f:
    f.write(table)