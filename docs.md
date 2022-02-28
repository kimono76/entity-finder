The file setup.py allow you to install the current directory as a package. -e stans for editable., so you can keep editing the content and it will still be treated as a package
Then you should run this command 

```sh

	pip install -e .

```


the next command downloads the language model (small size) 

```sh 
	python -m  spacy download en_core_web_sm
```
