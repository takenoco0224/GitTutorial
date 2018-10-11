#!/usr/bin/env python
#coding: utf-8
#===========================================================
# COMLOG.py
#===========================================================
# 実行方法
# A. ソースファイルのアクセス権を実行可能にして
#    「./COMLOG.py」
# B. 「python COMLOG.py」
# 注意：改行コードが\n\r(CR+LF)になっているとA.の方法では実行できません。
#       \n(LF)で保存してください。
#

import sys
from serial.tools import list_ports
import serial
import time
from datetime import datetime, timezone, timedelta
import logging
from logging import basicConfig, getLogger, DEBUG

# このスクリプト本体のロガーを取得してログレベルを設定する
logger = getLogger(__name__)
logger.setLevel(DEBUG)

def select_port():
    ports = list_ports.comports()

    if len(ports) == 0:
    	print("Error: serial device not found")
    	sys.exit(0)
    elif len(ports) == 1:
    	n = 0
    else:
	    # ポート選択
	    for i,port in enumerate(ports):
	        print("%5d : %s" % (i,port.device))

	    print("intput number of device:")
	    n = int(input())

    ser = serial.Serial(ports[n].device, 9600)

    return ser

def comport():
    ser = select_port()

    logging.basicConfig(filename="mylog.log", level=logging.INFO)
    logging.info('Started' + timestamp())

    while True:
        try:
            line = ser.readline()
            line = line.decode().strip()
            logging.info(line)
        except KeyboardInterrupt:
            ser.close()
            break
        except:
            pass

    logging.info('Finished')
    print("end")
def timestamp():
    now = time.time()
    JST = timezone(timedelta(hours=+9), 'JST')
    loc = datetime.fromtimestamp(now, JST)
    return str(loc)
# エントリポイント
if __name__ == "__main__":
        comport()

        raise SystemExit
