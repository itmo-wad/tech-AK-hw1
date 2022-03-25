# Homework 1

## Build
This repo uses [Flask](https://flask.palletsprojects.com/en/2.0.x/) as backend server and HTML-templates. 
Install dependencies at first via ``pip install Flask`` and then run web server via ``python ProfilePage.py``

## Description
This file shows a small profile page at ``/profile`` by using ``render_template(args)``. The profile information (like name, e-mail, university name and so on) is passed as **parameter** to the HTML-template, so that it is possible to adapt the profile page to other personalities without changing the HTML template itself. The HTML template uses the [Bootstrap Framework](https://getbootstrap.com/docs/5.0/getting-started/introduction/) and can be found in the ``templates`` folder.

In addition, there are two different views of the profile page: The **default view** and the **extended view** also holding detailed contact information. The extended view is available via ``/profile/full`` while the default view is served for every other route.

The web server also redirects default route ``/`` to the subpage ``/profile``.