#!/bin/bash
# Displays all methods a server will accept
curl -X options -i $1
