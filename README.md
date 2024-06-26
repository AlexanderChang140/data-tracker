# data-tracker
Pulling data from transit APIs.

## Build Instructions

### Grafana

'''bash
sudo apt-get update
sudo apt-get upgrade
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo apt-get install -y software-properties-common
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
'''

### SQLite3
'''bash
sudo apt-get install sqlite3
'''

### Python Environment Variables
'''bash
pip install python-dotenv
'''