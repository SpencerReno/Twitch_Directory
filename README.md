# Twitch Directory
This data was acquired by the twitch API. The API allows you to get the current top directories based on view count. However, it doesn't specify the actual view count. To obtain the view count I used another api call that obtains all currently active streams. With this API call, you can only access 100 streams at a time so, to get the total correct view count I used a for loop that iterates for every 100 streams until the API returns no more streams for that directory. Going about it this way won't give 100% accuracy since streamers will go live and go offline while iterating through all streams. Although, after running multiple tests with this strategy it appeared that it was only off by a few 10-100 viewers. Once I gather enough data from the API over the next few weeks, I plan on making a machine learning model to predict the viewership of each category.

Twitch API: https://dev.twitch.tv/docs/api/


Top Games API: https://dev.twitch.tv/docs/api/reference#get-top-games


Get Streams API: https://dev.twitch.tv/docs/api/reference#get-streams


## Directory Graph 
This is currently for the first day 01-31-22 of the twitch directory at (11:45AM EST, 10:45AM CST, 08:45AM PST)
![day_one ViewCount](https://user-images.githubusercontent.com/88803320/151845360-33f9e870-cccf-436d-b743-75467aeb831a.png)


Twitch directory comparison from 01-31-22 and 02-01-22 at (11:45AM EST, 10:45AM CST, 08:45AM PST)
![day_two](https://user-images.githubusercontent.com/88803320/152016936-afa46a0d-ceb4-4c31-acc7-81ef7ac1c3f7.png)

Just chatting will most likely be the top directory every day as it is a universal category that streamers can go into regardless of what they are streaming. Over the three days, GTA V has declined each day. Most of the top streamers that do stream in this category don't stream until later in the afternoon. So, most of the time the viewership will be very low at 10:45 am. Leauge had a good spike for February 2nd, 2022 compared to past days. Most other categories stayed mostly consistent from all 3 days. Some categories that don't show a view count are due to that category going in and out of the top 10.
![day_three](https://user-images.githubusercontent.com/88803320/152199209-46831579-c057-4671-b250-17710af0dbbb.png)
