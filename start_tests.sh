python3 -m pip install requirements.txt

python3 service/service.py &

python3 -m pytest -v tests/test_service.py

kill -9 $(ps -efl | grep service.py | grep -v grep | awk '{ print $4 }')