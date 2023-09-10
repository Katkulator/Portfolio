playlist = {
    "title" : "Liked Songs",
    "author" : "Matko Katić",
    "songs" : [
        {"song name" : "Jersey", "artist" : ["Mayday Parade"], "duration" : 3.5},
        {"song name" : "When the sun sleeps", "artist(s)" : ["Underoath"], "duration" : 3.8},
        {"song name" : "Note to self", "artist(s)" : ["From First To Last"], "duration" : 4}
        ]
}
total_length = 0

for song in playlist["songs"]:
    total_length += song["duration"]

print(total_length)