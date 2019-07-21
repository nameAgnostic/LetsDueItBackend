Shift and right click in the main folder where "launchserver.py" exists.

Select "open powershell window here"

enter this:
	python launchserver.py

open a browser and navigate to the ip that the window gave you
	http://127.0.0.1:5000/

---

Troubleshooting:

Issue: No module named 'flask'
Fix: in powershell, type this:
	pip install flask
