#!/bin/bash
(time yhrun -n 1 -c 24 ./runWorkflow.py --memGb=60 --mode=local) 2>manta.logfile
