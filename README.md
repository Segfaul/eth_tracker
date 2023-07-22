
# `Ethereum Tracker`

Asynchronous bot for analyzing the futures market according to the algorithm of taking into account percentage deviations from the main trading indicators with the possibility of alerting.

The algorithm works on the principle of average deviation from SMA and RSI, PSAR indices. 

___

## *Project Status*

***Completed &#10003;***
___
## Functionality
- CRUD operations with **USER** and **TradingPair** models via [Services](https://github.com/Segfaul/eth_tracker/tree/7d0bcfa4a054a44f1fbb4ae13a999b9daac3ff43/app/services)
- Notifications via [TelegramBot](https://github.com/Segfaul/eth_tracker/blob/7d0bcfa4a054a44f1fbb4ae13a999b9daac3ff43/app/services/bot_service.py#L17-L325) class with built-in admin panel
- Work with database via [Asynchronous ORM](https://github.com/Segfaul/eth_tracker/blob/7d0bcfa4a054a44f1fbb4ae13a999b9daac3ff43/app/services/db_service.py#L7-L32)

## Technologies and Frameworks
- Python 3.11
- Aiohttp 3.8.5
- Aiogram 2.25
- TortoiseORM 0.19.3
- PostgreSQL
- Docker
___

## Installation

1. Clone the repository to the local machine

    ```shell
    git clone https://github.com/Segfaul/eth_tracker.git
    ```

2. Go to the repository directory

    ```shell
    cd eth_tracker
    ```

3. Create and activate a virtual environment

    ```shell
    python -m venv env
    source env/bin/activate
    ```

4. Set project dependencies

    ```shell
    pip install -r requirements.txt
    ```

5. Configure the configuration file .env

    ```shell
    nano .env
    ```

6. Run the main application in the background

    ```python
    python -m app.main
    ```

7. In case of a problem, the program will stop automatically or you can stop execution using

    ```shell
    ps aux | grep ".py"
    kill PID
    ```

8. Also you can build a docker app and run the container

    ```shell
    docker-compose up -d --build
    ```

___

## Algorithm Perfomance (2% / w)

![](https://i.imgur.com/faeBqat.png)

```python
~  ATOM/USDT

~  Unrealized (P&L) : 0%
~  Total Profit: 2.0 %
```
___
