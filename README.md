Stalk-Site

Its a Stalksite just like Stop Stalk made in Django using Beautiful Soup and Mechanical Soup, as well as Selenium.
As it takes time to render all the sites and scrape the details therefore Celery Beat is used to schedule the task and update the details of all users at a particular time and update the changes in the database so that when user hits the url he doesn't have to wait for the scraping to take place.
The frontend and backend will be further improved in the near future.
