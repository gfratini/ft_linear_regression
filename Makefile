PY3 = ${shell which python3}
MAIN = main.py
TRAINER = trainer.py
ERROR = error.py
REQ = "requirements.txt"


init: install run

if:
	@[ -f "thetas.csv" ] || ${PY3} ${TRAINER} fi

trainer:
	@${PY3} ${TRAINER}

run: if
	@${PY3} ${MAIN}

error: if
	@${PY3} ${ERROR}

install:
	@${PY3} -m pip install --target="lib" -r ${REQ}
