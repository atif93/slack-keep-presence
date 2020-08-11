# Keep your slack status active always.

Slack desktop app makes the status away after 30 minutes of system inactivity while the web version does it after 30 minutes of browser inactivity (source: [Mashable](https://mashable.com/article/how-to-keep-slack-status-active-while-away/), [Twitter](https://twitter.com/slackhq/status/448966862521786368)). It's not configurable and thus it gets difficult to keep the status active when multitasking especially nowadays during WFH. This script helps to achieve this goal.

## Prerequisites:

1) Make your mac/desktop settings to make it never goto sleep. In macbook it's in the Energy Saver settings.
2) Download chromedriver for your Chrome version from [here](https://chromedriver.chromium.org/downloads).
3) Get your slack team URL (e.g. https://team-name.slack.com).
4) Make sure some version of python is installed with [selenium](https://pypi.org/project/selenium/) package.

## Steps to follow next:

1) Run the script:  
  `python main.py <team_slack_url> <absolute_path_to_chromedriver>`
2) A Chrome window will open with your `<team_slack_url>`. Login to your slack team.
3) Leave this Chrome window open and let the script run in the background. The script will keep refreshing this window every 10 minutes and thus will keep the slack status active. Do not put the system to sleep or close the lid.
4) Stop the script whenever the status is no longer required to be kept active.