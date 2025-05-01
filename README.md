# 2025cloud

## Introduction
The purpose of this project is to show how to use GitHub Action to create and automatically deploy Docker images.

## 🔧 Build and Execute

### Build Container Image

```bash
docker build -t 2025cloud .
```
### Run Container Image

```bash
docker run -p 5000:5000 2025cloud
```