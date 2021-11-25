# Messi Ankles Website

## User Stories

### Owner Goals:

1. Have a Website that tells people about the club.
2. Be able to save data about games and players.
3. Have an easily accessible and easy to use ticket system.

### Customer Goals:

1. Be able to book tickets.
2. Be able to see when games are and the scores of previouse games.
3. See player stats.
4. Not have to put in my details every time I pay for tickets.
5. Not have to create an account to use the service.
6. See my previously booked tickets.

### My Goals:

1. Have a responsive website.
2. Player carosel on home page.
3. Base functionality eg. creating edditing and deleting data works without any problems.
4. Automatic email on booking. 



## UX

### Design:
* The colour scheme is going to be yellow and black as those are the club colours.
* I want the website to be modern, have a robust feel about it, so using sharp lines and blocked structure.

## Features
### General UI

* A Dynamicaly changing nav bar that looks good across all devices, on mobile has an offcanvas side menu that displays all the sam tabs that would be shown on desktop.

* Nave bar is styled in a trapezoid shape so it lines up nicely with the right and side of the page and keeps that sharp lined design I'm going for.

* Footer has email for contact info and links to social accounts so that the user can easily find out more about us or contact us.

* Toasts popup in the bottom right displaying any message the server has for the user, the toasts are color coded depending on the type of message.

    | Message | Color  |
    | ------- | ------ |
    | Success | Green  |
    | Warning | Yellow |
    | Info    | Blue   |
    | Error   | Red    |

### Home Page

* The hero image is displayed on the home page sso users can instantly see the whole team and instantly recognise that this is a website about a sports team.

* The Fixtures tab on the Home page is visible as soon as you load the page as it has the most important information on it of the teams next fixture and also a link to buy tickets for that fixture.

* A player carousel at the bottom of the page that links to player stats and shows off the team. It is functional on both desktop and mobile. 

### Players Page

* Each individual player has there own player card with there name and shirt number. The players are sorted in to position for user ease of looking through the players and also forms a nice layout for the page.

* Each card links to the individual players profile with stats about the player that the user can find out and also keep a record for the club.

### Players Profile Page

* The profile page has a picture of the playre and the stats of the player. The stats are generated through functions making sure that each goal or assist is linked to an instance of the Goal model saved in the database. This is the same for clean sheets and appearences, with the Fixtures model. Because the stats are set up this way it means that when you create a goal you don't have to manually update player stats aswell.

* The page is also viewable across all screen sizes and will automatically change layoout if needed.

* Admin can edit the players name number and position but are unable to change goals assists, appearences or cleansheets without creating the Fixture or Goal instance to go along with it.

* Theres also a back button to take you back to the players page.

### Fixtures Page

* The fixtures table shows all fixtures that are in the database, this includes the date and time of the fixture, the home and away team and also the score if the game has been played. The fixtures are displayed in date order.

* For admin users there is an edit fixture button next to each fixture to make it obviouse which fixture your edditing and an add fixture button at the bottom of the page.

* The add fixtures form lets the admin input the home team, away team, the date and time of the fixture. It does not include goals of the fixture or wether the fixture has been played yet because the fixtures should be put up in advance of the match and then you can edit them after to add goals and change the game played status.

* There is also a cancel button to go back incase the admin didn't want to add a fixture.

* The edit fixture page is similar to the add fixture page except it has the option to add goals and change the game played status. The form is already filled out with the info about the fixture that is saved on the data base.

* The add goals form on the edit fixtures form creates instances of goals linked to the currently edditing fixture. If the team that is selected to have scored is Messi Ankles then you also get the option to add a goal scorer and assist maker which will also be saved to the goal object. This then gets displayed in a table underneath the team name whch displays all the goals. and a button to delete the goal if it was a mistake.

* If you change teams there would still be goals of the previouse teams linked to the fixture so when you change team a popup will apear letting you no whats going to happen and wether you wwan't to continue or not. if you do want to continue it will delete all goals in the fixture related to that team.

### Table 

* The table shows the current league table of all the fixtures in the database, it shows the wins draws and losses, total points and number of goals scored by each team.

### Tickets Page

* The Tickets page has a select input of all the fixtures that haven't been played yet to buy tickets for as you don't want people buying tickets for games that have already been played.

* it also has a number input that lets the user put in how many tickets they want which then changes a total box on screen displaying the final price.

* The ticket form will make sure that nothing is empty before you continue onto the checkout page and validate the data being put in.

### Checkout Page

* The checkout page will display the details of the order for the user to make sure they are correct.

* The checkout form will be prefilled with info if the user is logged in and has the details saved to there profile. If the user is not logged in they will have to fill out their first and last name and email aswell as their card info.

* The card info is automatically validated by stripe. before being sent off to be processed.

* If the checkout is complete then the user will be taken to a success page with their order information and an email sent to there email account.

* The checkout page also has a loading sign whilst waiting for stripe to respond.

### Profile Page

* The profile page has a list of the users orders

* There is also a small form to save info to prefill the checkout form.

### Login/ Logout/ Create an Account Page

* Login/ Create an account page have links to each other to easily swith if user does or doesn't have an account.

* Logout doubble checks to make sure if you do want to logout to avoid mistakes.

## Technologies Used

## Testing

### Testing User Goals

* Have a Website that tells people about the club.


* "Be able to save data about games and players."

    The database I have created has models for Teams, Players, Fixtures, Goals, Tickets, and Users. All of these have a table where they get saved to after being created.
    The Teams and Players have been loaded in through fixtures that I created using [Mockaroo](https://www.mockaroo.com/) which generates random json files with custom fields you put in.
    everything else is created within the app using Djangos models and `.save()` method.



    fixtures/models.py
    ```
    class Fixture(models.Model):

    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', null=False, blank=False)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team', null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    game_played = models.BooleanField(default=False, null=False, blank=False)


    def __str__(self):
        return f'{self.date}: {self.home_team} v {self.away_team}'

    def home_team_goals(self):
        goals = Goal.objects.filter(fixture=self, team=self.home_team)
        return goals

    def away_team_goals(self):
        goals = Goal.objects.filter(fixture=self, team=self.away_team)
        return goals
    ```

    This is my fixtures model, the data saved to it are the home team, away team, date of the fixture, time of the fixture and weather or not the game has been played. The goals in the fixture are class methods because it means that when you want to look up the number of goals in the fixture each goal is linked with a goal object which will decrease the amount of error across all tables with linked data such as goals or assists or clean sheets as there is no physical data linked to the objects.



    fixtures/models.py
    ```
    class Goal(models.Model):

    goal_id = models.CharField(max_length=100, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False, related_name='team_goals')
    goal_scorer = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goals' , null=True, blank=True)
    assist_maker = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='assists', null=True, blank=True)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'Goal: {self.team}, {self.fixture}'

    ``` 

    This is my Goal class it contains the id of the goal, the team which scored, the goal scorer, assist maker and which fixture the goal was scored in. with all this information linked to the goal it makes it easy to make queries about the goals in certain fixtures or by ceertain teams or even by players throughout the app.



    players/models.py

    ```
    class Player(models.Model):

        name = models.CharField(max_length=254)
        number = models.IntegerField(null=False)
        position = models.CharField(max_length=15)
        team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False, related_name='team_players')
        image_url = models.CharField(
            max_length=100,
            null=True,
            blank=True
            )

        def __str__(self):
            return str(self.name)

        def appearances(self):
            appearances = 0
            fixtures = self.team.home_team.all() | self.team.away_team.all()
            for fixture in fixtures:
                if fixture.game_played == True:
                    appearances += 1

            return appearances

        def clean_sheets(self):
            clean_sheets = 0
            home_fixtures = self.team.home_team.all()
            for fixture in home_fixtures:
                if fixture.game_played == True:
                    if len(fixture.away_team_goals()) == 0:
                        clean_sheets += 1

            away_fixtures = self.team.away_team.all()
            for fixture in away_fixtures:
                if fixture.game_played == True:
                    if len(fixture.home_team_goals()) == 0:
                        clean_sheets += 1

            return clean_sheets

    ```

    This is my Player class it saves the name of the player, their shirt number, their position the team they play for and the url for their image that I use on the app.
    Data about the players performance is gotten through class methods for the same reason as the Fixture class because it means mistakes are less likley and keeps things consistent across the database. You can edit the features of the Messi Ankles ankles players, such as shirt number or position or name through the app, admins have access via an edit player button to change the values of these fields.  The players that belong to other teams I don't think need the ability to be changed in the app as it is a Messi Ankles website. But if you do wish you can edit them through the Django admin or if you wish to change which team the websites for just change which team is being filtered in the queries and you will be able to acces these other players but as it is filler data that is not directly related to the users of the website theres no need to access them through the app.


    Here is the method of how to save fixtures and goals:

    1. Go to the fixtures tab and at the bottom click add fixture and fill out the form and click add fixture.

        ![Add Fixtures form](media/README/testing/fixure-player-edditing/save-fixture-1.jpg)

    2. Then to add a goal click edit fixture next to the fixture youve just added on the table. 

        ![Fixtures table with new fixture added](media/README/testing/fixure-player-edditing/save-fixture-2.jpg)

    3. Click add goal and then fill out the team, goal_scorer and assist maker of the goal and click add goal.

        ![Add goal form](media/README/testing/fixure-player-edditing/save-fixture-3.jpg)

    4. This has saved the goal and you will be able to see it in the edit fixtures view.

        ![Edit Fixture view with new goal added](media/README/testing/fixure-player-edditing/save-fixture-4.jpg)

    5. You can then see that it has been changed in the admin view too.

        ![Admin view of both goal and fixture object.](media/README/testing/fixure-player-edditing/save-fixture-5.jpg)



    Here is how you edit a player:

    1. Go to the players tab and then click on the player you want to edit.

        ![Player profile view](media/README/testing/fixure-player-edditing/edit-player-1.jpg)

    2. Then you can edit what you want and click update player.

        ![Player edit view](media/README/testing/fixure-player-edditing/edit-player-2.jpg)

    3. You can then see the changes in the player view.

        ![Player Profile showing changes made](media/README/testing/fixure-player-edditing/edit-player-3.jpg)

    4. Here are the changes in the admin view.

        ![admin view of changes to player object](media/README/testing/fixure-player-edditing/edit-player-4.jpg)


*   "Have an easily accessible and easy to use ticket system."

    "Be able to book tickets."

    "Not have to put in my details every time I pay for tickets."

    "Not have to create an account to use the service."



    When creating the ticket system I implemented 'easy to use' by making it a minimum two step process. First choose the ticket and then then checkout. For extra ease you can create an account that saves your info to make checking out quicker but it is not neccasery to purchasing a ticket for users who "don't want to create an account". and to make the tickets 'easily accessible' across all devices the tickets button is directly vissible in the nav bar and also visible through a banner on the home page when you first load the webpage.

    Here is what the navbar and home page look like across different pages:

    Desktop

    ![Destop view showing the navbar and home page linking to the tickets page.](media/README/testing/tickets-system/ticket-nav-desktop.jpg)

    Tablet

    ![Tablet view showing the navbar and home page linking to the tickets page.](media/README/testing/tickets-system/ticket-nav-tablet.jpg)

    Mobile

    ![Mobile view showing the navbar and home page linking to the tickets page.](media/README/testing/tickets-system/ticket-nav-mobile.jpg)


    Heres how to book tickets:
    
    1. Click on the tickets page and fill out what tickets and how many you want.

        ![Ticket booking page choosing the tickets](media/README/testing/tickets-system/ticket-purchasing-1.jpg)

    2. Fill out your details, if you have your profile details saved it will be prefilled for you and you just have to enter your card details otherwise just enter your name a, email and card info.

        ![Ticket checkout page](media/README/testing/tickets-system/ticket-purchasing-2.jpg)

    3. Click checkout and if your card is good you will be taken to the success page. and sent a booking confirmation email.

        ![Booking success page](media/README/testing/tickets-system/ticket-purchasing-3.jpg)
        ![Booking confirmation email](media/README/testing/tickets-system/ticket-purchasing-4.jpg)

    4. Here is the admin view of the ticket object. If the user had no account the ticket holder field would be empty.

        ![Admin view of saved ticket object](media/README/testing/tickets-system/ticket-purchasing-5.jpg)


* "See my previously booked tickets."

    In the profiles app there is a list of your previousley bought tickets with the ticket id, price, fixture and number of tickets purchased viewable to the user.
    Currently it's limited to 5 tickets so the page isn't over filled, but in the future i'm going to add a show more button/ the ability to search and scroll through all the previouse bookings.

    ![Profile page](media/README/testing/profile/profile-page.jpg)


### My Goals


* "Have a responsive website."

* "Player carosel on home page."

* "Base functionality eg. creating edditing and deleting data works without any problems."

* "Sending an automatic email on ticket bookings."


## Future Ideas

* The ability to search tthrough previouse tickets.

* Be able to filter fixtures shown on the fixtures table by Team and date.

* For the league table, currently the fixtures need to be part of my database, in the future it would be good to use an api to get the data off of a central league database that all the teams update so that each website doesn't have to keep a database of all the fixtures and just keep there own, or even just get what ones they need from this central db.

## Deployment
This is how I deployed my project to Github and Heroku and set up amazon web services.

### Github & Heroku

1. First of all I create a github repository using Code institutes github-full-template on git pod.

2. Then created your base files and install Django using `pip3 install django`. 

3. Then create an env.py file which holds sensitive data that you don't want uploaded to git such as the Database url and secret key. Then create a .gitignore file and put the env.py file and pycache in so they don't get uploaded to github.

4. Then write in the terminal `git add -a`, `git commit` and then `git push` to push it to your github repository

5. Go to Heroku and login. Then click on create new app, enter a name and chose a region.

6. Then on the resources tab in the add ons section  look up postgres and chose heroku postgres and the free hobby dev plan to go along with it.

7. Then back on gitpod  install  `dj_database_url` and  `psycopg2-binary` using `pip3 install ...` as these are required by postgres to work.

8. Then use `pip3 freeze > requirements.txt` so that heroku will install all the apps requirements.

9. Then in settings.py add ```import dj_database_url``` at the top and change

    settings.py
    ```
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
    ```

    into 

    settings.py
    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
     ```

     which looks if theres a database url in the enviroment and then if not will use the django sqlite database.

10. Then on heroku go to your app settings and select reveal config variables. Then copy the 'DATABASE_URL' variable and set it up in your env.py file.

    env.py
    ```
    import os

    DATABAS_URL = 'your database url goes here'
    ```

11. If you have already made models/ made migrations now would be the time to migrate using `python3 manage.py migrate`. also if you have fixtures that are located in `appname/fixtures/fixturename.json` then you will want to load data using `python3 manage.py loaddata fixturename`

12. Then you will want to create a super user user using `python3 manage.py create superuser` in the terminal.

13. Then back on Heroku go to the deploy tab click on connect with github and add your repository. Then enable automatic deployment so each time you push in git pod it will push to heroku. 

14. Then click settings then config veariables and add SECRET_KEY and make it your django secret key. and then in the settings.py file change your secret key so it looks like this.

    settings.py
    ```
    SECRET_KEY = os.environ.get('SECRET_KEY', '')
    ```

    and add a new secret key to your env.py file.

    env.py
    ```
    import os

    DATABAS_URL = 'your database url goes here'
    SECRET_KEY = 'your new secret key'
    ```

14. Then run `git add .`, `git commit -m` and `git push` in the terminal to push your repository to heroku. 



15. Then in the terminal install gunicorn using `pip3 install gunicorn` and `pip3 freeze > requirements.txt`.
 
16. then create a Procfile and put in it 

    Procfile
    ```
    web: gunicorn yourappname.wsgi:application
    ```

    This creates a web dyno and serves the django app.

17. Then disable collect static by going into your config variables creating a variable calles DISABLE_COLLECTSTAIC and set it to 1.

18. Then in settings.py add the url of your heroku app to ALLOWED_HOSTS and also local host so you can still run the test server.

    settings.py
    ```
    ALLOWED_HOSTS = ['your-app.herokuapp.com', 'localhost']
    ```


### AWS

1. Go to https://aws.amazon.com/ and create an account.

2. Then you will need to enter a credit card number which will get charged if you go over the service limit for this project you will not go over the limit.

3. Go back to https://aws.amazon.com/ and login and go to aws management console under my account.

4. then search s3 in the services search bar.

5. Then you want to click on create bucket and give your bucket the name your heroku app and select your closest region. Also untick block all public access and check the box that aknowledges you know that your bucket will be public and then click create.

6. Then go to the properties tab and turn on static website hosting and fill in the index doceument and error document with index.html and error.html as we will not use them and click save.

7. Then on the permissions tab go to CORS configuration and paste in 
    ```
    [
      {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposeHeaders": []
      }
    ]
    ```
    and save it.

8. Then go to the bucket policy tab and select policy generator to create a security policy.

9. The policy type will be an S3 bucket policy, in principals put '*',  and in actions select GET object.

10. Then go back to the permissions tab and copy the ARN code to paste into the ARN box.

11. Then click add statement and then generate policy and copy the poicy into the bucke policy editor.

12. Before saving add /* on to the end of the resource key to allow access to all resources in the bucket. Then click save and done.

13. Next go to the access controll list tab and set the list objects to everyone.

14. Go to the services menu and look up IAM.

15. First click on groups and create group and call it name it so you know what app it's for eg. yourappname-manager.

16. Then click next step twice as we dont have a policy to attach to it yet. And then click create group.

17. Then on the left side menu click policies and create policies. then click on the json tab and click import policiy.

18. Search for s3 then click on AmazonS3FullAccess and import it.

19. Next you will want to get your bucket ARN from the bucket policies tab again and paste it twice into the resource section as a list and after the second one add a '/*' to the end so it selects all.

20. Then click on review policy and give it a name and short description to do with your app. and then click create policy.

22. Then go back to the group you created. select attach policy, search and select the policy you just created and attach it.

23. Next youll want to add a user so click add user at the top and give the user a name like 'myapp-static-files-user' give them programatic access and then click next.

24. then add the user to the group and click next through to the end and then create user.

25. You then need to download the csv file which contains the access key you need to give to your django app.

26. Go over to your django app and use `pip3 install ...` to install `boto3` and `django-storages`. And freeze them into requirements.txt.

27. in setiings add storages into the installed apps.

28. Then at the bottom of your settings file add

    settings.py
    ```
    if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your bucket name'
    AWS_S3_REGION_NAME = 'your region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

    #Telling Django where the static files are coming from
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # This connects to the custom_storages file you will create next to store static and media files.
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

    and add your AWS variables to the env.py file.

29. Add your AWS keys to your config variables on your heroku app. and remove the DISABLE_COLLECTSTATIC variable as the static files should hopefully go to S3.

30. Next you will want to create a file called custom_storages.py and set it up like this.

    custom_storages.py
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    
    ```

31. Then run `git add .`, `git commit -m` and `git push` in the terminal to push the changes to heroku and static files to s3. You will know it has worked if when you look at the build log on heroku it will say static files coppied. Also if you go onto s3 you will see the static files in your bucket.

## Acknowledgements/ Links

CSS Shapes - https://css-tricks.com/the-shapes-of-css/

Fixed footer - https://stackoverflow.com/questions/40853952/bootstrap-footer-at-the-bottom-of-the-page/40854221

CSRF cookie code - https://stackoverflow.com/questions/43606056/proper-django-csrf-validation-using-fetch-post-request


admin login page does not exist fix https://stackoverflow.com/questions/9736975/django-admin-doesnotexist-at-admin