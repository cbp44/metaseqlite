init:
	conda env create -f conda_env.yaml

activate:
	conda activate metaseq-lite

remove:
	conda env remove -n metaseq-lite

test:
	nosetests tests
