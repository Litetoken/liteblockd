# -*- coding: utf-8 -*-
VERSION = "1.5.0" #should keep up with the litetokenswallet version it works with (for now at least)

DB_VERSION = 22 #a db version increment will cause liteblockd to rebuild its database off of litetokensd 

CAUGHT_UP = False #atomic state variable, set to True when litetokensd AND liteblockd are caught up

UNIT = 100000000

SUBDIR_ASSET_IMAGES = "asset_img" #goes under the data dir and stores retrieved asset images
SUBDIR_FEED_IMAGES = "feed_img" #goes under the data dir and stores retrieved feed images

MARKET_PRICE_DERIVE_NUM_POINTS = 8 #number of last trades over which to derive the market price (via WVAP)

# FROM litetokensd
# NOTE: These constants must match those in litetokensd/lib/config.py
REGULAR_DUST_SIZE = 5011
MULTISIG_DUST_SIZE = 6011
ORDER_LTC_DUST_LIMIT_CUTOFF = MULTISIG_DUST_SIZE

mongo_db = None #will be set on server init

LTC = 'LTC'
XLT = 'XLT'

MAX_REORG_NUM_BLOCKS = 10 #max reorg we'd likely ever see

ARMORY_UTXSVR_PORT_MAINNET = 6590
ARMORY_UTXSVR_PORT_TESTNET = 6591

QUOTE_ASSETS = ['LTC', 'XLTC', 'XLT'] # define the priority for quote asset
MARKET_LIST_QUOTE_ASSETS = ['XLT', 'XLTC', 'LTC'] # define the order in the market list