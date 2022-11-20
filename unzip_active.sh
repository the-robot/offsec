#!/bin/bash
read -p 'Enter password to unzip: ' password
unzip -P $password \*.zip