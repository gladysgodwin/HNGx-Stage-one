# HNGx-Stage-one

# Task:
Create and host an endpoint using any programming language of your choice.
The endpoint should take two GET request query parameters and return specific information in JSON format.
## Requirements <br>
The information required includes: <br>
-  Slack name
-  Current day of the week
-  Current UTC time (with validation of +/-2)
-  Track
-  The GitHub URL of the file being run
-  The GitHub URL of the full source code.
-  A Status Code of Success
JSON <br>
{ <br>
  "slack_name": "example_name",<br>
  "current_day": "Monday",<br>
  "utc_time": "2023-08-21T15:04:05Z",<br>
  "track": "backend",<br>
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",<br>
  "github_repo_url": "https://github.com/username/repo",<br>
  "status_code": 200<br>
}<br>
Acceptance Criteria<br>
Endpoint Creation: Provide a publicly accessible endpoint.<br>
GET Parameters: The endpoint should accept two GET request query parameters: slack_name and track.<br>
       E.g.: http://example.com/api?slack_name=example_name&track=backend.<br>
Slack Name: The response should include the slack_name passed as a GET request query parameter.<br>
Current Day of the Week: Display the current day of the week in full (e.g., Monday, Tuesday, etc.). <br>
Current UTC Time: Return the current UTC time, accurate within a +/-2 minute window.<br>
Track: The response should display the track of the you signed up for (Backend). This will be based on the track GET parameter passed to the endpoint.<br>
GitHub File URL: Include a direct link to the specific file in the GitHub repository that's being executed.<br>
GitHub Repo URL: Include a link to the main page of the GitHub repository containing the project's entire source code.<br>
Status Code: Return 200 as Integer. <br>
JSON Format: The endpoint's response should adhere to the specified JSON format.<br>
Testing: Before submission:<br>
Ensure the endpoint is accessible.<br>
Check the returned JSON against the defined format.<br>
Validate the correctness of each data point in the JSON response<br>




# Result of Task:
![image](https://github.com/gladysgodwin/HNGx-Stage-one/assets/99274632/16170c0a-5684-4b2d-808a-c27ff33cd2d8)
![image](https://github.com/gladysgodwin/HNGx-Stage-one/assets/99274632/f884d118-845d-4ae1-be70-9fb7e269e3d2)

## Endpoint url: https://5000-gladysgodwi-hngxstageon-hyz1ytbs1hd.ws-eu104.gitpod.io/api?slack_name=GladysGodwin&track=backend
# Language used: Python
