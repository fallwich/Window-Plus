# Code Review

## Major Issues
1. **Duplicate handler registration loop** – `handler_thread` continually adds a new `MessageHandler` every two seconds (`full_code.py`, lines 435-439). The dispatcher keeps every handler that gets added, so this loop will register an unbounded number of identical handlers. Over time each incoming message is processed repeatedly, causing duplicate replies and eventually exhausting memory/CPU. Create the handler once and register it a single time before entering the loop.
2. **Sending text strings through Bluetooth sockets** – Both `dht_11_send` (`full_code.py`, lines 173-186) and `dust_gas_thread` (`full_code.py`, lines 448-456) call `client_socket.send` with plain Python strings (e.g. `"999"`). Under Python 3 the PyBluez `BluetoothSocket.send` API expects a bytes-like object; passing `str` raises `TypeError` and the telemetry never reaches the client. Encode all payload fragments (e.g. `b"999"` or `"999".encode("utf-8")`) before sending.
3. **Hard-coded Telegram secrets** – The bot token and chat IDs are committed in plaintext (`full_code.py`, lines 73-75). Publishing secrets in source control allows anyone with repo access to control the bot and read private data. Move these credentials to an environment variable or external configuration that is not checked into source control, and rotate the exposed token immediately.

## Additional Observations
- Consider adding exception handling around the hardware initialisation (I²C open, Bluetooth accept, API calls) so that the service can fail gracefully when the hardware or network is unavailable.
- The infinite control loop at the bottom of `full_code.py` runs without any sleep interval. Introducing a short delay (even a few milliseconds) can reduce CPU usage without impacting responsiveness.

