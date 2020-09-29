import logging
import threading

def func_a():

	logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', level=logging.INFO, filename="today_log", filemode="w")

	logging.debug("A Debug Logging Message")

	logging.info("A Info Logging Message")

	logging.warning("A warning Logging Message")

	logging.error("A error Logging Message")

	logging.critical("A Critical Logging Message")


for i in range(1000):
	a = threading.Thread(target=func_a)
	a.start()
	print("writing")
