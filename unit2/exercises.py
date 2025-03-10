# Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

# def lineup(artists, set_times):
#     # artist_lineup = dict(zip(artists, set_times))
#     # return artist_lineup
#     return {artist: set_time for artist, set_time in zip(artists, set_times)}

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# '''
# You are designing an app for your festival to help attendees have the best experience possible! As part of the application, 
# users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
# Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to 
# dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about 
# the given artist.

# If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.
# '''
# def get_artist_info(artist, festival_schedule):
#     # Return dictionary giving info about artist
#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
#         return {"message": "Artist not found"}


# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

# A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

# def total_sales(ticket_sales):
#     total = 0
#     for sales in ticket_sales.values():
#         total += sales

#     return total

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))