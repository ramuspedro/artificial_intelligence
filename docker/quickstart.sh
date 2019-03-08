#!/bin/bash

docker build . -t jupyter-scipy-notebook-ee

docker run -it --rm -p 8888:8888 --hostname localhost -e JUPYTER_LAB_ENABLE=yes -v "$PWD/../projects:/home/jovyan/mount" jupyter-scipy-notebook-ee start.sh jupyter lab

docker logs -f jupyter-scipy-notebook-ee
