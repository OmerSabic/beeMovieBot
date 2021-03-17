# beeMovieBot
Simple discord bot to spam you your favorite movie scripts and store the data on a firebase database.

## Run your own
### Initializing the API
#### Create A Firebase Database 🔥

1. Go to firebase.google.com
2. Log in with Google
3. Press "Get started"
4. Press "Add project"
5. Follow the instrucions
6. Create an app and create a firestore database
7. Go to /beeMovieBot/API - Website/.env
8. Edit in .env file: PROJECTID="your-project-id"

#### Making a secret key 🔑

1. Go to /beeMovieBot/Api - Website/.env
2. Edit in .env file: API_SECRET="a-super-secret-password"

This key will be used to add up points to users, don't give it away or users will be able to get infinite points.

#### Discord token 👾

1. Go to [the discord development portal](https://discord.com/developers/)
2. Log in with discord if you're already not
3. Press "New Application" at the top-right of your screen
4. Put in a friendly name for your bot
5. Press "Bot" on the left
6. Create a bot and copy the token
7. Go to /beeMovieBot/API - Website/.env
8. Edit in .env file: DISCORD_TOKEN="token-you-just-copied"

Do not give away this token

### Initializing the bot
#### Copying the secret key 🔑

1. Go to /beeMovieBot/Bot/.env
2. Edit in .env file: API_SECRET="Same-key-you-put-last-time"

#### Copying the discord token 👾

1. Go to /beeMovieBot/Bot/.env
2. Edit in .env file: TOKEN = "Same-token-you-put-last-time"

#### Linking bot to API

1. Host your api from /beeMovieBot/API - Website
2. On line 26 in /beeMovieBot/Bot/main.py there should be a variable named "api_url"
3. Set it to the URL directing to your API
