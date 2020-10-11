SILENT = @

clean:
	$(SILENT) find . -type f -name *.pyc -delete
	$(SILENT) find . -type d -name __pycache__ -delete

run:
	python3 -m comparesort
