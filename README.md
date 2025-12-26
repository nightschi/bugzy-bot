# bugzy-bot
🤖 Discord bot for ease of use in streaming community discord servers.

# Summary
Bugzy Bot is a Discord bot designed for streaming communities, functioning as an alert system. Its primary purpose is to ping a certain role when a message is sent in a particular channel.

## Deployment

To deploy on Render:

1. Sign up at [render.com](https://render.com/).
2. Create a new Web Service and select your repo.
3. Set up:
   - Start Command: `gunicorn webserver:app & python main.py`
4. Add these environment variables:
   - `DISCORD_BOT_TOKEN`: Your bot token, obtained from the discord developer site.
   - `CHANNEL_ID`: Your channel ID.
   - `ROLE_NAME`: Your role name.
5. Deploy web service.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.