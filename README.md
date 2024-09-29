# ACP2-Twitter-Profile-Scoring
Twitter Profile Credibility Evaluator Outcome of ACP2 course of University of Oulu. Original project link: https://github.com/kannadan/ACP2-Twitter-Profile-Scoring

## Project Demo

![Screenshot 2023-02-09 at 15-04-35 twitter-rater-ui](https://github.com/user-attachments/assets/aaec3be8-fe4a-4dec-beea-c3a9c277879f)
![Screenshot 2023-02-09 at 15-11-21 twitter-rater-ui](https://github.com/user-attachments/assets/7693fe25-677f-437e-a149-cf397f672c9c)

## Development
### Install dependencies
Install Poetry (package manager): https://pypi.org/project/poetry/

Install packages:
```shell
$ poetry install
```

### Start the application
```shell
$ ./start.sh
```
or
```shell
$ ./build.sh
$ docker-compose up
```
## Deployment
Add your publish SSH key as authorized key to the target host.

Copy .env.dist as .env and fill the values. DEPLOY_SSH_PORT is optional, 22 is used as default.

Run
```
./deploy.sh
```
