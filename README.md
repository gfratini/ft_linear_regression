<h1 style="text-align: center"> FT_LINEAR_REGRESSION </h1>
<h2 style="text-align: center"> how to </h2>
<br/>

Makefile will take care of everything, just:  
```bash
$ make
```
to:  
* install dependecies __in the current directory__
* run the trainer
* run the calculator program

in this order
<br/>

if you want to do by yourself you can

* `make install ` to install dependencies
* `make trainer ` to train the model
* `make run ` to run the calculator
<br/>
<br/>

### Don't have Makefile?
<br/>

install the requirements
```bash
$ python -m pip install --target="lib" -r "requirements.txt"
```

and then
```bash
$ python {trainer.py/main.py/error.py}
```
### each one to do the respective work (which is to train/estimate/calculate the error)

<br/>

<h2 style="text-align: center"> other things, might be useful, i don't know </h2>

* the dataset used is data.csv by default, change it in `trainer.py` to use a different one, or change the data in the file, i don't know, do whatever you want
* the result is stored in thetas.csv