REM Windows only!

REM populate database
python ..\manage.py loaddata fixtures\category_db.json
python ..\manage.py loaddata fixtures\company_db.json
python ..\manage.py loaddata fixtures\subscriptions_db.json
