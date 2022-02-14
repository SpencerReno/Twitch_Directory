# Twitch Directory
This data was acquired by the twitch API. The API allows you to get the current top directories based on view count. However, it doesn't specify the actual view count. To obtain the view count I used another api call that obtains all currently active streams. With this API call, you can only access 100 streams at a time so, to get the total correct view count I used a for loop that iterates for every 100 streams until the API returns no more streams for that directory. Going about it this way won't give 100% accuracy since streamers will go live and go offline while iterating through all streams. Although, after running multiple tests with this strategy it appeared that it was only off by a few 10-100 viewers. Once I gather enough data from the API over the next few weeks, I plan on making a machine learning model to predict the viewership of each category.

Twitch API: https://dev.twitch.tv/docs/api/


Top Games API: https://dev.twitch.tv/docs/api/reference#get-top-games


Get Streams API: https://dev.twitch.tv/docs/api/reference#get-streams

## Summary For all Dates
![Total all weeks](https://user-images.githubusercontent.com/88803320/153803518-1add65dc-dc13-4aa5-95c8-346018e427f3.png)


## Week One by Directory 
Just chatting will most likely be the top directory every day as it is a universal category that streamers can go into regardless of what they are streaming. February 3, 2022, is an interesting one as two directories come into play, and others lacking compared to previous days. There are many reasons why directory viewership changes like this on random days. For example, starting with Dying Light 2. This game just released on Febuary 3rd, and it has drops currently active where viewers can get in-game rewards just by watching a streamer on twitch. This means that the viewership will be inflated for a few days while the drops are active. The other category that was added was Cities Skylines this one is a major outlier as its viewership is only inflated due to one streamer. xQcOW or Felix is one of the top streamers on the platform and his viewership alone can affect a directory to get into the top 10. At the current timestamp of 10:45 AM, he has 72,600 viewers alone. The directory for the game has 73,700. This equates to 98% of the viewers in the directory coming from his stream. 
![DAY_SIX](https://user-images.githubusercontent.com/88803320/152650861-b6a4dd07-c6c3-455a-a794-4b7a9161f2ad.png)


## Week One Summary
This Graph shows the max and average viewer counts based on each directory for week one of pulling data from the twitch api. Its clear of which directories are outliers as their max will be the same as their average view count. This means they were only in the top 10 directories for one day at 10:45am. Just Chatting was the leading directory mostly due to this being a universal directory that has a lot of different content within. Dying light 2 will mostlikly wont stay within the top 3 after a few weeks since it just released its viewership is slightly infated for the time being. 
![weekOneSummary](https://user-images.githubusercontent.com/88803320/152651182-60dbac99-7d3e-411b-835b-1c3903379411.png)


## Week Two by Directory
Week two finally shows some competition to just chatting. The release of Lost Ark in America, having drops and a very successful launch skyrocketed the viewership for this week. Most of the other directories lay within their respected location. For this week there weren't too many outliers only dying light 2, rust, slots, and sifu. Sifu had just been released at the beginning of the week this explains its spike and drop of viewers. Rust had drops early on in the week and slots just depend on who is live when the data is pulled. 
![weektwodayseven](https://user-images.githubusercontent.com/88803320/153741041-dbec1b73-83b0-4887-a144-b7136d40c326.png)

## Week Two Summary
Although lost ark made this week competitive in terms of trading top viewership with just chatting. Just chatting still came out on top with the highest viewer count of 652,093 viewers. Most directories stayed within the 100,000-200,000 for max viewers and slightly less for the averages.  
![weektwosumma](https://user-images.githubusercontent.com/88803320/153741033-e6623afd-a70b-4965-a169-45f964810c70.png)


## Week Three by Directory 
![weekThreeDay](https://user-images.githubusercontent.com/88803320/153803498-8003da2b-a32a-4d30-ba3c-6c917e6b44df.png)




## Week Three Summary
![weekThreeSumma](https://user-images.githubusercontent.com/88803320/153803439-2fc4ecd1-df33-4e23-ac93-facb2cbea7ab.png)
