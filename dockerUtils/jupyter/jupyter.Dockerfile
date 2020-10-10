FROM python
RUN mkdir -p /opt/work
WORKDIR /opt/work
COPY ./requirements.txt /opt/work/
RUN pip install -r requirements.txt
EXPOSE 8888
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--NotebookApp.token=''", "--no-browser", "--allow-root"]