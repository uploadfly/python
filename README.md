# python

UploadFly Python SDK

The Python SDK provides a convenient interface for interacting with the UploadFly API to upload and delete files.

## Installation

from github

```bash
pip install -e git+https://github.com/uploadfly/python
```

from PyPi repository(coming soon)

```bash
pip install uploadfly
```

## Usage

### Class: `UploadflyClient`

#### constructor: `UploadflyClient(api_key)`

- Creates new instance of the `UploadflyClient` class
- **Parameters:**
  - `api_key` (string): The API key required for authentication with the UploadFly service.
- **Throws:**
  - `Exception`: If the `api_key` parameter is not provided.

### Methods

#### `upload(file: File, filename='filename')`

- Uploads a file to the Uploadfly cloud.
- **Parameters:**
  - `file` (BufferedReader or string): The file to be uploaded. BufferedReader can be created by using the `open('filename', 'rb')` function.
  - `filename` (string): The desired filename for the uploaded file. If not provided, the original filename will be used.
- **Returns:**
  - response from the Uploadfly API.
- **Throws:**
  - `Exception`: If the `file` parameter is not provided or if the file upload fails.
  - `Exception`: If an error occurs during the file upload process.

#### `delete(file_url: string)`

- Deletes a file from the Uploadfly cloud.
- **Parameters:**
  - `file_url` (string): The URL of the file to be deleted.
- **Returns:**
  - response from the Uploadfly API.
- **Throws:**
  - `Exception`: If the `file_url` parameter is not provided or if the file deletion fails.
  - `Exception`: If an error occurs during the file deletion process.

## Example Usage

### Upload files

```python
from uploadfly import UploadflyClient

uploadfly = UploadClient('your-api-key')


# upload with BufferedReader
file = open('file.txt', 'rb')
try:
    response = uploadfly.upload(file, filename='custom-filename')
    print('file uploaded', response)
except Exception as e:
    print('error uploading file', e.message)

# upload with file path
file = 'path/to/file'
try:
    response = uploadfly.upload(file, filename='custom-filename')
    print('file uploaded', response)
except Exception as e:
    print('error uploading file', e.message)
```

### Delete files

```python
file_url = # file url

try:
    response = uploadfly.delete(file_url)
    print('file deleted', response)
except Exception as e:
    print('error deleting file', e.message)
```
