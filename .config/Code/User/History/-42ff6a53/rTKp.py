#!/usr/bin/python3 

import time
import Adafruit_DHT      # 라이브러리 불러오기

sensor = Adafruit_DHT.DHT11     #  sensor 객체 생성

pin = 4                        # Data핀의 GPIO핀 넘버

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, pin) # 센서 객체에서 센서 값(ㅇ노도, 습도) 읽기

    if h is not None and t is not None:   #습도 및 온도 값이 모두 제대로 읽혔다면 
        print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h))  # 온도, 습도 순으로 표시
    else:                                                  # 에러가 생겼다면 
        print('Failed to get reading. Try again!')        #  에러 표시
        time.sleep(100)