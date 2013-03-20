#!/bin/bash
echo 'Adding data to database'

python -B manage.py shell <<END
import data.ingredients_json_to_db
END
echo ''
