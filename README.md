# spectral-to-splunk

Pull Spectral issues via the API and upload to Splunk Collector Event API.

## Installation

`pip install git+https://github.com/Cloud-Security-Architects/spectral-to-splunk`

## Usage

1. Configure the following environment variables:
- SPECTRAL_URL=https://get.spectralops.io
- SPECTRAL_SPU=spu-XXXXXXXXXX
- SPLUNK_URL=https://localhost:8080
- SPLUNK_AUTH=XXXXXXXXXXXXXXXXXXXXX

2. Run the script
`spectral_to_splunk`

## Known limitations

- Will only upload the first page of issues (100)
- Deduplication of issues is expected to happen in Splunk
