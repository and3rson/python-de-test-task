# Python Data Engineering Test Task

1. Configure Docker & docker-compose (if you don't have it yet) & understand what this project consists of.
2. Bring up everything with `docker-compose up`. This will start `maindb` (source database), `stabledb` (target database) and `inserter` (script that simulates frequent insertion of dummy events into `maindb`).
3. Create a new application (it can be added as an extra service in `docker-compose.yaml` or executed seperately outside of Docker, as you wish) which will periodically migrate data from `maindb` to `stabledb` (let's say, every minute). The script should be easily configurable (DB credentials, migration interval etc) via command-line arguments or environment variables.
4. Add reporting to the script (stdout, text file, web interface - as you wish). Report must contain information about the amount of data that was migrated and time taken to process everything.
5. Bonus points: implement a simple web-server that will start data migration when a POST request is received.
6. Bonus points: edit `inserter/main.py`, decrease the insertion interval to 0 (line 28) and see if your script still works.
7. Bonus points: make the ETL process configurable so that if `events` table changes, code change will not be required (e. g. define ETL mapping via some seperate YAML config file.)
8. Bonus points: fork this repo, implement your changes in your fork and create a pull request to this repo.

Note: application must be written in Python.

Hint: you can add comments to describe your code. You can also provide multiple solutions if there is more than one good way to solve something.
