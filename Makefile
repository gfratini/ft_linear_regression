PY3 = ${shell which python3}
MAIN = main.py
TRAINER = trainer.py
CALCULATOR = calculator.py
REQ = "requirements.txt"


init: install
	@${PY3} ${MAIN}

trainer:
	@${PY3} ${TRAINER}

calculator:
	@${PY3} ${CALCULATOR}

run: 
	@${PY3} ${MAIN}

install:
	@${PY3} -m pip install --target="lib" -r ${REQ}