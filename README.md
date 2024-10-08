# Discord Voice Channel Notification Bot AKA Watcher

<p align="center">
  <img src="watcher.gif" alt="Watcher">
</p>

This Discord bot sends notifications when users join or leave voice channels in your server.

## Features

- Notifies when a user joins a voice channel
- Notifies when a user leaves a voice channel
- Includes timestamps in local time for each notification

## Prerequisites

- Python 3.9 or higher
- Discord.py library
- A Discord bot token
- Docker (optional, for containerized deployment)

## Setup

1. Clone this repository or download the source code.

2. Create a `config.json` file in the project root with the following content:

   ```json
   {
       "token": "YOUR_BOT_TOKEN",
       "notification_channel_id": YOUR_CHANNEL_ID
   }
   ```

   Replace `YOUR_BOT_TOKEN` with your Discord bot token and `YOUR_CHANNEL_ID` with the ID of the channel where you want notifications to be sent.

3. Install the required Python package:

   ```
   pip install discord.py
   ```

## Running the Bot

### Directly with Python

Run the bot using Python:

```
python bot.py
```

### Using Docker

1. Build the Docker image:

   ```
   docker build -t discord-watcher-bot .
   ```

2. Run the Docker container:

   ```
   docker run discord-watcher-bot
   ```

## File Structure

- `bot.py`: The main bot script
- `config.json`: Configuration file for bot token and notification channel
- `Dockerfile`: Instructions for building the Docker image
- `README.md`: This file, containing project information and instructions

## Bot Permissions

The bot requires the following permissions:

- Read Messages/View Channels
- Send Messages
- Read Message History
- View Voice Channel

Ensure the bot has these permissions in your Discord server.

## Security Note

Keep your `config.json` file secure and never share your bot token publicly.

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.