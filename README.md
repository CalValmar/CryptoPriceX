
# CryptoPriceX

[![GitHub license](https://img.shields.io/badge/License-MIT-orange)](https://raw.githubusercontent.com/CalValmar/CryptoPriceX/main/LICENSE)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Version](https://img.shields.io/badge/Version-2.2-brightgreen)

CryptoPriceX is a script that allows you to retrieve the price of a crypto currency on the Binance exchange.
It is written in Python and uses the Binance API.

## Authors

- @Jpiix - Version 1.X
- [@Valmar](https://www.github.com/CalValmar) - Version 2.X

## Run Locally

**Install dependencies**

```bash
  $ sudo pip install requests
```

**Start the script**

```bash
  python3 main.py
```

## API Reference

```
  GET /api/v3/ticker/price
```

| Parameter | Symbols Provided     | Weight                |
| :-------- | :------- | :-------------------------------- |
| `symbols` | `1`      | `1`                               |
|           | symbol parameter is omitted| `2`             |
| `symbols` | Any      | `2`                               |

**Exemple :**

```
  GET /api/v3/ticker/price?symbol=FLUXBUSD
```
**Response :**
```
{"symbol":"FLUXBUSD","price":"0.51300000"}
```

## Resources

- [Binance API](https://www.binance.com/en/binance-api)
- [API Documentation](https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics)
- [List of Supported Assets](https://support.binance.us/hc/en-us/articles/360049417674-List-of-Supported-Assets)
- [Exemple](https://api.binance.com/api/v3/ticker/price?symbol=FLUXBUSD)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details