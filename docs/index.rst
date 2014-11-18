blueblockd
==================================================

``blueblockd`` features a full-fledged JSON RPC-based API, which services Bluejudywallet, as well as any
3rd party services which wish to use it.

``blueblockd`` provides additional services to Bluejudywallet beyond those offered in the API provided by ``bluejudyd``.

Such services include:

- Realtime data streaming via socket.io
- An extended API for Bluejudywallet-specific actions like wallet preferences storage and retrieval
- API includes functionality for retieving processed time-series data suitable for display and manipulation
  (useful for distributed exchange price data, and more)

Contents:

.. toctree::
   :maxdepth: 3

   API


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

