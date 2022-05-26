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

#### Prediction Test Two 
The first time I pulled predictions was 5 weeks into this project. It's now been tripple that time now being on the 15th week. I've ran the predictions file once again to see if there would be any change with the predictions models. Without changing any of the models parameters most of the results were consistant with the first test. However, they all did increase in their own respective ways. For exaple the final model that I chose to show the scores for in test one was a default Decision Tree model. This model ran now has an increased Training score 0.72 and the Testing score from a 0.56 to a 0.63. An Increase in the Testing scores are what im really looking for. This is a good increase for a defualt model with no parameters. Still no the best but seeing the imporvement shows that the more data gathered the higher the scores get. At this rate its rougly +5 score on the testing data per rougly 7 weeks.


Decision Tree Model\
Train: 0.7247906637597405\
Test: 0.6349583075382321



# View Count Based On Months
Feb has the most viewers by 30,000 this is interesting as this could be related to many reasons. February also has two 
fewer days that are being taken into account. The most likely reason is since Feb is still considered the winter a lot more people stay inside. March is the start of spring the fewer people are staying in and watching twitch. However, the argument for this is that the data was pulled at 10:45 am central. Meaning a lot of people would be in school or work and not viewing twitch. I think seeing what was being viewed in these months might depict this and give us a clearer answer. 

![Viewer_count](https://i.gyazo.com/300bbef82c6c6e754c298ecf3f31c38a.png)

## Directory Viewership For February - April
Now, this graph gives us a clear understanding of why February viewership was so high compared to March and April. 
In February two highly anticipated games were released and had some insane viewership within the first few weeks. These games being Elden Ring and Lost Ark. In the following month of March both of these directories fell off more than half of their peak viewership in February. This is very typical for twitch as games release they gain an initial boost and decline at extreme rates as people get over the release hype.

![Viewership_feb-apr](https://i.gyazo.com/1c44d4d134f4bb01ee379eef9e64b4b6.png)




# Summary For all Dates
![Total_all_weeks](https://i.gyazo.com/3cd7b3b37c296864e1dddf72c848d6d6.png)


## Week Fourteen
![Day](https://i.gyazo.com/d0589f368ea5529b85cdf77a4ba6fede.png)

## Week Fourteen Summary
![summa](https://i.gyazo.com/4747c99ca0600aa12d086bc763dc5e4d.png)


