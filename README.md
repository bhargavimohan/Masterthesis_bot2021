# Mastersthesis_bot2021
Evaluation and Implementation of a motivational bot to support documentation process in mechatronics system design

The code is based on the boillerplate code available in the official documentation available from Microsoft called [Bot builder samples](https://github.com/microsoft/BotBuilder-Samples)
## D3driver

This is a productivity bot designed to support documentation of prominent design decisions in an inter disciplinary team. It makes use of the rich set of adaptive cards feature of the Microsoft for communication and documenting design decsions. Detailed information available in the final thesis report.

## Requirements
* [ngrok](https://ngrok.com/)
* A valid developer account in [Microsoft Teams](https://www.microsoft.com/en-ww/microsoft-teams/download-app)
* [Python 3.7](https://www.python.org/downloads/)
* [Visual studio code](https://code.visualstudio.com/download)

## Steps to run this bot in the local system

1. Clone the repository `https://github.com/bhargavimohan/Masterthesis_bot2021/tree/D3driver`
2. Open the directory in Visual studio code
3. Install Microsoft Teams Toolkit from the _Extensions_ of Visual studio code
4. Register a bot named _D3driver_ following [Bot Framework registration](https://docs.microsoft.com/en-us/microsoftteams/platform/build-your-first-app/build-bot#register-your-web-service-with-the-bot-framework)
5. 5. Start the ngrok using the terminal inside Visual studio code using `ngrok http -host-header=rewrite 3978`
6. Install all dependencies by running `pip3 install -r requirements.txt` in a new terminal from the right folder
7. Navigate to `config.py` to change the **Microsoft App ID** & **App password** as provided during Bot Framework registration in Step 4
8. The below steps should be done for a unique Microsoft teams instance
* Navigate to **teamsAppManifest** folder to update the `manifest.json`. All occurances of `<<YOUR-MICROSOFT-APP-ID>>` should be replaced with the __Microsoft App      ID__ that was crreated during Bot Framework registration in step 4
* All the files in the **teamsAppManifest** directoory should be zipped to create `manifest.zip`
*  Upload the `manifest.zip`in Microsoft teams using the _upload a custom app_ option
9. Navigate to `Masterthesis_bot2021/src/app.py` and open `app.py`, bring up another new terminal to run `pip3 app.py` or press `ctrl+F5` 

