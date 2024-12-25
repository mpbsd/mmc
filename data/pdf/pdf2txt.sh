#!/usr/bin/env bash

gs -sDEVICE=txtwrite -o2022_2.txt 2022_2.pdf
gs -sDEVICE=txtwrite -o2023_1.txt 2023_1.pdf
gs -sDEVICE=txtwrite -o2023_2.txt 2023_2.pdf
gs -sDEVICE=txtwrite -o2024_1.txt 2024_1.pdf
gs -sDEVICE=txtwrite -o2024_2.txt 2024_2.pdf
gs -sDEVICE=txtwrite -o2025_1.txt 2025_1.pdf

exit 0
