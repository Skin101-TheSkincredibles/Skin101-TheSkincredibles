import json
import jsonschema
from functools import wraps
from jsonschema import (
  Draft7Validator,
  draft7_format_checker,
)
from django.http import JsonResponse

# YES THIS THING SHOULD BE IN UTILITIES
def request_schema(schema, method='GET'):
  """
  Validate request based on given schema
  Based on given method will extract data from body or query string
  """
  validator = Draft7Validator(schema, format_checker=draft7_format_checker)

  def _func(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
      if request.method != method:
        return JsonResponse(status=400, data={'message': 'wrong method'})
      
      try:
        if request.method == 'GET':
          data = request.GET.copy()
        
        if request.method == 'POST':
          if request.content_type == 'application/json':
            # Handle json request
            if request.body == '':
              data = {}
            else:
              data = json.loads(request.body)
          elif request.content_type.startswith('application/x-www-form-urlencoded'):
            data = request.POST.copy()
          else:
            data = {}

        data.update(kwargs)
        kwargs.clear()
        
        validator.validate(data)
      except jsonschema.exceptions.ValidationError as ex:
        return JsonResponse(status=400, data={"error": ex.message})

      return func(request, data, *args, **kwargs)

    return wrapper

  return _func