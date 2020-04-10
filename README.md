# Docker Flask REST API

REST API using Flask in Docker with a Restaurant model

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on Heroku.

### Prerequisites

You need to have Docker Engine installed and running on your computer. If this is not the case, go [here](https://docs.docker.com/get-docker/)

### Installing

In a terminal, clone this repository, `cd` into it and build the Docker image:
```
docker build -t flask-rest-api .
```

Then run a container from this image:
```
docker run -d -p 5000:5000 flask-rest-api
```

Your app is now up and running locally. You can visit `localhost:5000/restaurants` to get all your restaurants.

For more information about basic Docker Engine commands, go [here](https://docs.docker.com/engine/reference/commandline/docker/)

## Deployment

These instructions will show you how to deploy the project on Heroku, knowing that you already have a built image on your local machine.

### Prerequisites

You need to have Heroku CLI installed on your computer and you should be logged in your account. If this is not the case, go [here](https://devcenter.heroku.com/articles/heroku-cli)

### Deploying

Open a terminal in your project folder and create your app on Heroku:
```
heroku create my-app-name --region eu
```

Provision a Postgres database on Heroku: go to your app dashboard, resources, add-ons and add a `Heroku Postgres` add-on.

Back in your terminal, push your already built Docker image to Heroku:
```
heroku container:push web
```

Then release it:
```
heroku container:release web
```

Your app is now up and running in production. You can visit `https://www.my-app-name.herokuapp.com/restaurants` to get all your restaurants.

For more information about basic Heroku CLI commands, go [here](https://devcenter.heroku.com/articles/using-the-cli)

## Authors

- **[lucien-george](https://github.com/lucien-george)** - [Initial Flask REST API](https://github.com/lucien-george/FlaskRESTApi)
- **[PurpleBooth](https://github.com/PurpleBooth)** - [README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
