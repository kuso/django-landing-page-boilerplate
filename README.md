# django-landing-page-boilerplate

This is a django landing page boilerplate project that uses the [freelancer bootstrap theme](https://startbootstrap.com/template-overviews/freelancer/) from [startbootstrap](https://startbootstrap.com)

To start, clone the project into a local directory

To serve the static files, add to nginx server configuration block with the following and reload nginx
```
server {
    listen       80;
    server_name  dev_server;

    location /vendor/ {
		 alias /path/to/django-landing-page-boilerplate/myproject/landing_page/static/vendor/;
	}

	location /mail/ {
	     alias /path/to/django-landing-page-boilerplate/myproject/landing_page/static/mail/;
	}

	location /js/ {
	     alias /path/to/django-landing-page-boilerplate/myproject/landing_page/static/js/;
	}

	location /img/ {
		 alias /path/to/django-landing-page-boilerplate/myproject/landing_page/static/img/;
	}

	location /css/ {
		 alias /path/to/django-landing-page-boilerplate/myproject/landing_page/static/css/;
	}

	location / {
		 proxy_pass http://127.0.0.1:8000;
	}
}

```

Go to myproject directory and start the web server
```
python manage.py runserver
```

open [http://dev_server/landing_page](http://dev_server/landing_page) with browser

