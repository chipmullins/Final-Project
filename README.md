# HPC Cache Optimization Demo

This project demonstrates cache optimization through memory locality in high-performance computing (HPC).

## Overview
The experiment compares:
- Row-major traversal (cache-friendly)
- Column-major traversal (cache-unfriendly)

## Why It Matters
Modern CPUs rely on cache memory. Efficient memory access patterns can significantly improve performance.

## How to Run

```bash
pip install -r requirements.txt
python cache_demo.py
