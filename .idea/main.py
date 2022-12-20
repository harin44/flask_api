import json
from itertools import permutations
#import pandas as pd
import numpy as np
import numpy as np
from flask import Flask, jsonify,request

app = Flask(__name__)
@app.route('/',methods =['POST'])

def index():

    record = json.loads(request.data)

    def cal():
        x_ = 'A'  # on the backend
        y_ = 'B'
        z_ = 'C'

        x11 = record['mac1']  # from the front end
        y12 = record['mac2']
        z13 = record['mac3']

        array_B = [];
        array_B.extend([x11,y12,z13])


        array_A = np.array([x_, y_, z_])  # stroed
        xi = array_A[0]
        yi = array_A[1]
        zi = array_A[2]

        # default

        x1 = 0.0
        y1 = 0.0
        x2 = 7.5
        y2 = 2.0
        x3 = 13.0
        y3 = 0.0

        array_x = np.array([x1, x2, x3])
        array_y = np.array([y1, y2, y3])

        array_B = ([x11, y12, z13])  # saved
        xe = array_B[0]
        ye = array_B[1]
        ze = array_B[2]

        Data = []
        for i in range(3):
            for j in range(3):
                if array_A[i] == array_B[j]:
                    xc = array_x[j]
                    yc = array_y[j]
                    Data.extend((xc, yc))
                    break;

        print(Data)
        return Data;
        # return cal()

    # xc yc

    macValue = cal();
    print(macValue)

    x1 = macValue[0]
    y1 = macValue[1]
    x2 = macValue[2]
    y2 = macValue[3]
    x3 = macValue[4]
    y3 = macValue[5]

    # SLIIT_ENG lattitude - 6.915882699472551 longitude -  79.97326433658601

    # RSSI --> Distance
    def distance_cal_1():
        RSSI =record['router1']
        N = (3.5 + 5) / 2
        calculated_N = 10 * N
        calculated_rssi = (-18.5 - RSSI)
        d = (calculated_rssi / calculated_N)
        calculated_d1 = 10 ** (d)
        return calculated_d1

    r1 = distance_cal_1()

    def distance_cal_2():
        RSSI =record['router2']
        N = (3.5 + 5) / 2
        calculated_N = 10 * N
        calculated_rssi = (-18.5 - RSSI)
        d = (calculated_rssi / calculated_N)
        calculated_d2 = 10 ** (d)
        return calculated_d2

    r2 = distance_cal_2()

    def distance_cal_3():
        RSSI = record['router3']
        N = (3.5 + 5) / 2
        calculated_N = 10 * N
        calculated_rssi = (-18.5 - RSSI)
        d = (calculated_rssi / calculated_N)
        calculated_d3 = 10 ** (d)
        return calculated_d3

    r3 = distance_cal_3()


    def trilit(x1, y1, r1, x2, y2, r2, x3, y3, r3):
        A = 2 * x2 - 2 * x1
        B = 2 * y2 - 2 * y1
        C = r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2
        D = 2 * x3 - 2 * x2
        E = 2 * y3 - 2 * y2
        F = r2 ** 2 - r3 ** 2 - x2 ** 2 + x3 ** 2 - y2 ** 2 + y3 ** 2
        x = (C * E - F * B) / (E * A - B * D)
        y = (C * D - A * F) / (B * D - A * E)
        print(x, y)
        a = json.dumps(x)
        b = json.dumps(y)
        response = {
            "x":a,
            "y":b
        }

        return response

    res =trilit(x1, y1, r1, x2, y2, r2, x3, y3, r3)
    #print(res)

    return res



app.run()