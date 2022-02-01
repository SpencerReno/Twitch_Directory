# Twitch Directory
This data was acquired by the twitch API. The API allows you to get the current top directories based on view count. However, it doesn't specify the actual view count. To obtain the view count I used another api call that obtains all currently active streams. With this API call, you can only access 100 streams at a time so, to get the total correct view count I used a for loop that iterates for every 100 streams until the API returns no more streams for that directory. Going about it this way won't give 100% accuracy since streamers will go live and go offline while iterating through all streams. Although, after running multiple tests with this strategy it appeared that it was only off by a few 10-100 viewers.   

## Directory Graph 
This is currently for the first day 01-31-22 of the twitch directory at (11:45AM EST, 10:45AM CST, 08:45AM PST)
![day_one ViewCount](https://user-images.githubusercontent.com/88803320/151845360-33f9e870-cccf-436d-b743-75467aeb831a.png)


Twitch directory comparison from 01-31-22 and 02-01-22 at (11:45AM EST, 10:45AM CST, 08:45AM PST)
![day_two](https://user-images.githubusercontent.com/88803320/152014496-3b6694bf-8e4d-41db-a1d0-a714402c99ff.png)