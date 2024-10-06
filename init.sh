#!/bin/bash
chmod +x ./init.sh
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
