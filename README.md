# WhoAmI - Identity Creator

A Python-based identity creator using the RCS (Reactive Component System) framework.

## Overview

The IdentityCreator is a component that implements the identity function - it passes input directly to output while managing signal types and visualization properties through a JSON schema.

## Features

- Signal-based input/output processing
- JSON serialization/deserialization
- Port color customization
- Metadata tracking with JSON configuration

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

```bash
git clone https://github.com/yourusername/WhoAmI.git
cd WhoAmI
pip install -r requirements.txt
```

## Usage

```bash
python IdentityCreator.py
```

This will:
1. Create an identity creator process
2. Process sample input ("Hello, World!")
3. Display the output
4. Save process configuration to `identity_process.json`
5. Load and re-process from the saved JSON

### Expected Output

```
Hello, World!
(255, 25, 25)
{...json representation...}
Hello, World!
```

## Configuration

Edit `IdentityCreator.JSON` to customize:
- Component name and description
- Version information
- Author details
- License type

### Schema Definition

```json
{
  "IdentityCreatorSchema": {
    "userId": "string",
    "identityType": "string"
  }
}
```

## GitHub Actions

This project includes automated CI/CD workflows:

- **Python Tests** (`python-test.yml`): Runs on every push/PR
  - Tests against Python 3.9, 3.10, 3.11, 3.12
  - Linting with pylint
  - Test execution

- **Deploy** (`deploy.yml`): Runs on push to main and tags
  - Creates release artifacts
  - Publishes releases on version tags

### Triggering Releases

To create a release and automatically deploy:

```bash
git tag v1.0.0
git push origin v1.0.0
```

## License

MIT License - See IdentityCreator.JSON for details

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For issues and questions, please open an issue on GitHub.
