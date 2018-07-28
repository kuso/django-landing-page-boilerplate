# django-landing-page-boilerplate

This is django landing page boilerplate project that uses the [freelancer bootstrap theme](https://startbootstrap.com/template-overviews/freelancer/) from [startbootstrap](https://startbootstrap.com)

To start, clone the project into a local directory

To serve the static files, add to nginx server configuration block with the following
```
server {

    location /vendor/ {
		 alias /path/to/django-landing-page-boilerplate/static/vendor/;
	}

	location /mail/ {
	     alias /path/to/django-landing-page-boilerplate/static/mail/;

	}

	location /js/ {
	     alias /path/to/django-landing-page-boilerplate/static/js/;

	}

	location /img/ {
		 alias /path/to/django-landing-page-boilerplate/static/img/;
	}

	location /css/ {
		 alias /path/to/django-landing-page-boilerplate/static/css/;
	}
}

```
python manage.py runserver
```