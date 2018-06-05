# -*- coding: utf-8 -*-

from test_case import test_case_1


if __name__ == "__main__":
    test_case_1.kaka_test4(1,1,5,["08:00", "08:01", "08:02", "08:03"])  # 	"09:00"
    test_case_1.kaka_test4(2,10,2,["09:10", "09:09", "08:00"])  # 	"09:09"
    test_case_1.kaka_test4(2,1,2,["09:00", "09:00", "09:00", "09:00"])  # 	"08:59"
    test_case_1.kaka_test4(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])  # 	"00:00"
    test_case_1.kaka_test4(1,1,1,["23:59"])  # 	"09:00"
    test_case_1.kaka_test4(10,60,45,["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]) # "18:00"

    test_case_1.kaka_test3(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) # 50
    test_case_1.kaka_test3(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) #	21
    test_case_1.kaka_test3(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) #	60
    test_case_1.kaka_test3(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) #	52
    test_case_1.kaka_test3(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) #	16
    test_case_1.kaka_test3(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])    #25

    test_case_1.kaka_test2("1S2D*3T")   # 37
    test_case_1.kaka_test2("1D2S#10S")  # 9
    test_case_1.kaka_test2("1D2S0T")    # 3
    test_case_1.kaka_test2("1S*2T*3S")  # 23
    test_case_1.kaka_test2("1D#2S*3S")  # 5
    test_case_1.kaka_test2("1T2D3D#")   # -4
    test_case_1.kaka_test2("1D2S3T*")   # 59