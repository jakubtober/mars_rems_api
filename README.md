# MARS REMS Data - REST API

REST API created using Django Rest Frameworok - CRUD for Mars REMS data (will be used by MartianUpdates twitter bot).

API uses TokenAuthentication, CREATE, UPDATE and DELETE views require user authentication

## API endpoints

* /api/sols/
* /api/sols/<id>/
* /api/token-auth/
* /api/sols/create/ - authentication is required
* /api/sols/<id>/update/ - authentication is required
* /api/sols/<id>/delete/ - authentication is required
