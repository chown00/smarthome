#!/bin/bash

 export FLASK_APP=frontend       # Set directory of application
 export FLASK_ENV=development    # Set dev mode
 flask run --host=0.0.0.0        # Run application and make it externally visible