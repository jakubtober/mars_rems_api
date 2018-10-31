# MARS REMS Data - REST API

REST API created using Django Rest Framework - CRUD for Mars REMS data (will be used by MartianUpdates twitter bot).

API uses TokenAuthentication, CREATE, UPDATE and DELETE views require user authentication

## API endpoints

* /api/sols/
* /api/sols/sol_number/
* /api/token-auth/
* /api/sols/create/ - authentication is required
* /api/sols/sol_number/update/ - authentication is required
* /api/sols/sol_number/delete/ - authentication is required
