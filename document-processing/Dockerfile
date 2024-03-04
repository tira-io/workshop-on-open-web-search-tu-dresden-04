#see https://github.com/OpenWebSearch/wows-code/tree/main/ecir24/baselines/dev-container
FROM webis/wows-2024-baseline:0.0.5

ADD baseline_document_processing.py /code/baseline_document_processing.py

RUN pip3 install matplotlib pprint textstat \
	&& rm -rf /root/.cache

ENTRYPOINT [ "python3", "/code/baseline_document_processing.py" ]
