# Data version control with lakeFS and lakeFS-spec
This repository contains a jupyter notebook example that showcases the abilities lakeFS and lakeFS-spec for data version control with Python.

The notebook was the basis for a talk on data version control given by Max Mynter (MLOps engineer at appliedAI Institute for Europe) at PyData Heilbronn in February 2024.

The talk is available on YouTube. Click the video below, to watch it. The talk is about ~25 min (the video is longer as it is a livestream recording that went into the break).
In it's first half we cover data version control in general, the second half is a hands-on walkthrough on versioning datasets from Python with lakeFS and lakeFS-spec.

[![YouTube thumbnail of the PyData Heilbronn talk on data version control with lakeFS and lakeFS-spec](resources/YT_thumbnail.png)](https://www.youtube.com/watch?v=1LcCAjJ589Y)

## Running the Notebook on your machine
To run the notebook you need to setup your local development environment and a lakeFS server.
Let's start with the latter.

We provide a `docker-compose.yaml` so you can launch the instance with `docker compose up` in your terminal.
You also need to provide a `~/.lakectl.yaml` file that stores your credentials; in this case the default ones.
Create one by executing the following command (ATTENTION: the command will overwrite an existing file)
```bash
cat <<EOF > ~/.lakectl.yaml
credentials:
  access_key_id: AKIAIOSFOLQUICKSTART
  secret_access_key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
metastore:
  glue:
    catalog_id: ""
  hive:
    db_location_uri: file:/user/hive/warehouse/
    uri: ""
server:
  endpoint_url: http://127.0.0.1:8000
EOF
```

With lakeFS running, we can now set up our development environment. 
Set up a new virtual environment by executing the following commands in your terminal within the root of this repository.
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Now you can launch the notebook by typing `jupyter notebook` in your terminal and opening the `pydata-demo.ipynb` in the browser that opened up.
We have added some explanations in the notebook. However, we recommend going through it next to the talk to get further context on the versioning operations that are done (the notebook walkthrough starts at 9:45 in the video). 
