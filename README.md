# Twitch Directory
This data was acquired by the twitch API. The API allows you to get the current top directories based on view count. However, it doesn't specify the actual view count. To obtain the view count I used another api call that obtains all currently active streams. With this API call, you can only access 100 streams at a time so, to get the total correct view count I used a for loop that iterates for every 100 streams until the API returns no more streams for that directory. Going about it this way won't give 100% accuracy since streamers will go live and go offline while iterating through all streams. Although, after running multiple tests with this strategy it appeared that it was only off by a few 10-100 viewers. Once I gather enough data from the API over the next few weeks, I plan on making a machine learning model to predict the viewership of each category.

Twitch API: https://dev.twitch.tv/docs/api/


Top Games API: https://dev.twitch.tv/docs/api/reference#get-top-games


Get Streams API: https://dev.twitch.tv/docs/api/reference#get-streams

# Predictions
After a full 5 weeks of pulling data, and gathering 300+ rows of data. Running some machine learning models still shows that more data needs to be gathered for the models to be more precise. I ran three different regression models to compare from decision Tree, Kneighbors, and random forest. Decision Tree had the best scores but still not where I'd like them to be. The training score was 71. While the testing score was 56. These both could further improve over time once more data is gathered.

Decision Tree Model\
Train: 0.7111598069381483\
Test: 0.5662584827145769



## Summary For all Dates
![Total all weeks](https://user-images.githubusercontent.com/88803320/158040480-f53ccbe8-dfb1-4276-a37d-e743017a3223.png)




# Week One
## Individual Directories
Just chatting will most likely be the top directory every day as it is a universal category that streamers can go into regardless of what they are streaming. February 3, 2022, is an interesting one as two directories come into play, and others lacking compared to previous days. There are many reasons why directory viewership changes like this on random days. For example, starting with Dying Light 2. This game just released on Febuary 3rd, and it has drops currently active where viewers can get in-game rewards just by watching a streamer on twitch. This means that the viewership will be inflated for a few days while the drops are active. The other category that was added was Cities Skylines this one is a major outlier as its viewership is only inflated due to one streamer. xQcOW or Felix is one of the top streamers on the platform and his viewership alone can affect a directory to get into the top 10. At the current timestamp of 10:45 AM, he has 72,600 viewers alone. The directory for the game has 73,700. This equates to 98% of the viewers in the directory coming from his stream. 
![DAY_SIX](https://user-images.githubusercontent.com/88803320/152650861-b6a4dd07-c6c3-455a-a794-4b7a9161f2ad.png)


## Week One Summary
This Graph shows the max and average viewer counts based on each directory for week one of pulling data from the twitch api. Its clear of which directories are outliers as their max will be the same as their average view count. This means they were only in the top 10 directories for one day at 10:45am. Just Chatting was the leading directory mostly due to this being a universal directory that has a lot of different content within. Dying light 2 will mostlikly wont stay within the top 3 after a few weeks since it just released its viewership is slightly infated for the time being. 
![weekOneSummary](https://user-images.githubusercontent.com/88803320/152651182-60dbac99-7d3e-411b-835b-1c3903379411.png)

# Week Two
## Individual Directories
Week two finally shows some competition to just chatting. The release of Lost Ark in America, having drops and a very successful launch skyrocketed the viewership for this week. Most of the other directories lay within their respected location. For this week there weren't too many outliers only dying light 2, rust, slots, and sifu. Sifu had just been released at the beginning of the week this explains its spike and drop of viewers. Rust had drops early on in the week and slots just depend on who is live when the data is pulled. 
![weektwodayseven](https://user-images.githubusercontent.com/88803320/153741041-dbec1b73-83b0-4887-a144-b7136d40c326.png)

## Week Two Summary
Although lost ark made this week competitive in terms of trading top viewership with just chatting. Just chatting still came out on top with the highest viewer count of 652,093 viewers. Most directories stayed within the 100,000-200,000 for max viewers and slightly less for the averages.  
![weektwosumma](https://user-images.githubusercontent.com/88803320/153741033-e6623afd-a70b-4965-a169-45f964810c70.png)


# Week Three
## Individual Directories 
This week seen a lot of back and forth with Lost ark and Just chatting. At the begining of the week lost ark started very strong and slowly declined as the week progressed. Just chatting stayed very consistant within the 500-600 thousand range. This week had a total of eight outliers with games that showed up for two or less of the seven days. These directories being Dota 2, Minecraft, Slots, Warzone, Dead by Daylight, Horizon Forbiden West, Mario Kart, and Elden Ring. 
![weekThreeDay](https://user-images.githubusercontent.com/88803320/154818265-86664a8c-c938-4599-9448-7ace676d0ad6.png)



## Week Three Summary
Just chatting managed to stay just ahead of lost ark this week. However, the max viewers almost broke into the 700,000 range for lost ark. This week also seen a lot of outliers compared to other weeks. 
![weekThreeSumma](https://user-images.githubusercontent.com/88803320/154818337-86e4147e-ddde-43c6-bc81-12d246a92c8a.png)



# Week Four
## Individual Directories
![weekFourDay](https://user-images.githubusercontent.com/88803320/155892959-730f3506-86c5-41ad-a406-9b7f65524ec2.png)


## Week Four Summary 
![WeekFourSumma](https://user-images.githubusercontent.com/88803320/155892960-6db443e5-2f41-4802-9b0a-1809122398a5.png)


# Week Five
## Individual Directories 
![weekfiveday](https://user-images.githubusercontent.com/88803320/156907615-bddc7b17-61fd-4736-9820-e17344eb334c.png)


## Week Five Summary
![weeekfivesumma](https://user-images.githubusercontent.com/88803320/156907614-306bc632-7201-4725-a4a8-019ef4979d1d.png)


# Week Six
## Individual Directories
![weeksixday](https://user-images.githubusercontent.com/88803320/158040478-5d809cdc-a519-4e4a-ba60-36e3487e333d.png)


## Week Six Summary
![weeksixsumma](https://user-images.githubusercontent.com/88803320/158040479-1b883831-847f-4961-b1e3-2d769628eff0.png)

