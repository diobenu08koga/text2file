# Document Generation Service

A web application that converts Markdown text into various document formats including PDF, DOCX, and plain text.

## Overview

This service provides a RESTful API for dynamic document generation, enabling seamless integration with other applications. It supports multiple output formats and includes caching mechanisms for improved performance.

## Features

- **Multiple Output Formats**: Generate documents in PDF, DOCX, and plain text
- **RESTful API**: HTTP endpoints for easy integration
- **Caching System**: Redis-based caching for improved performance
- **Modular Architecture**: Extensible design for additional formats
- **Docker Support**: Containerized deployment with docker-compose

## Installation

```bash
docker-compose up -d
```

## Usage

Send POST requests to the API with Markdown content to generate documents in your preferred format.

## Project Structure

- `src/` - Source code
- `docker-compose.yml` - Docker configuration
- `README.MD` - Documentation

## License

MIT License
