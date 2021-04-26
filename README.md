# Challenge JS+

 - How to run the project locally?
	 - 
	 - Rename `.env.dev.example` to `.env.dev`
	 - Run: `docker-compose up --build -d`;
	 - If you get the following error: `django.db.utils.OperationalError: FATAL:  database "hello_django_dev" does not exist`;
	 - Run `docker-compose down -v` to remove the volumes with the containers. Then run `docker-compose up -d --build` again; 
	 - Run the migrations of the project: `docker-compose exec web python manage.py migrate`;
 - How to test the application?
	 - 
	 - Run: `docker-compose exec web pytest`;
- Documentation
	- 
	- The documentation can be found in: [http://localhost:8000/docs/](http://localhost:8000/docs/)