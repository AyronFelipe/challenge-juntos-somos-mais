# Challenge API Fintech

 - How to run the project locally?
	 - 
	 - Rename `.env.dev.example` to `.env.dev`
	 - Run: `docker-compose up --build`;
	 - If something wrong happens in connection between the application and database, run: `docker-compose restart web`;
	 - Run the migrations of the project: `docker-compose exec web python manage.py migrate`;
 - How to test the application?
	 - 
	 - Run: `docker-compose exec web pytest`;
- Documentation
	- 
	- The documentation can be found in: [http://localhost:8000/docs/](http://localhost:8000/docs/)