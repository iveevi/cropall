
# Installation

Clone the repository, `cd` into it, and run the following installation command:

`pip install .`

# Usage

Try `cropall --help` which will give the following output:

```
usage: cropall [-h] [--directory DIRECTORY] [--region REGION [REGION ...]] [--action {crop,markup}] images [images ...]

positional arguments:
  images

options:
  -h, --help            show this help message and exit
  --directory DIRECTORY
  --region REGION [REGION ...]
  --action {crop,markup}
```

Example usage:

```
cropall source/* --region 700 500 900 700 700 100 900 300 --action markup --directory marked
```
