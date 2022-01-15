PY3 = ${shell which python3}
MAIN = main.py
REQ = "requirements.txt"

 
all: install
	@${PY3} ${MAIN}

run: 
	@${PY3} ${MAIN}

install:
	@${PY3} -m pip install --target="lib" -r ${REQ}
