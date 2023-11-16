from dm_logger import DMLogger

logger = DMLogger("main")

logger.info("test message", tag="test tag")
logger.debug("new message", id=123312)
logger.info("only mess")
logger.critical(env="production")
logger.warning({"key": "value"})
logger.error(["item1", "item2", 3])
logger.info()
