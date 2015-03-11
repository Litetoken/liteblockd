liteblockd
==================================================

``liteblockd`` features a full-fledged JSON RPC-based API, which services Craftwallet, as well as any
3rd party services which wish to use it.

``liteblockd`` provides additional services to Craftwallet beyond those offered in the API provided by ``litetokensd``.

Such services include:

- Realtime data streaming via socket.io
- An extended API for Craftwallet-specific actions like wallet preferences storage and retrieval
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

