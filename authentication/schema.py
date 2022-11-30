login_api_request = {
  'type': 'object',
  'properties': {
    'username': {'type': 'string'},
    'password': {'type': 'string'},
  },
  'required': ['username', 'password'],
}

signup_api_request = {
  'type': 'object',
  'properties': {
    'username': {'type': 'string'},
    'password1': {'type': 'string'},
    'password2': {'type': 'string'},
  },
  'required': ['username', 'password1', 'password2'],
}