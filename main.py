# -*- coding: utf-8 -*-

from case import case1


if __name__ == "__main__":
    case1.jaccard("FRANCE", "french")    # 16384
    case1.jaccard("handshake", "shake hands")    # 65536
    case1.jaccard("aa1 + aa2", "AAAA12")    # 43690
    case1.jaccard("E = M * C ^ 2", "e = m * c ^ 2")    #65536

    # case1.kaka_bus(1,1,5,["08:00", "08:01", "08:02", "08:03"])  # 	"09:00"
    # case1.kaka_bus(2,10,2,["09:10", "09:09", "08:00"])  # 	"09:09"
    # case1.kaka_bus(2,1,2,["09:00", "09:00", "09:00", "09:00"])  # 	"08:59"
    # case1.kaka_bus(1,1,5,["00:01", "00:01", "00:01", "00:01", "00:01"])  # 	"00:00"
    # case1.kaka_bus(1,1,1,["23:59"])  # 	"09:00"
    # case1.kaka_bus(10,60,45,["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]) # "18:00"

    # case1.kaka_cache(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) # 50
    # case1.kaka_cache(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) #	21
    # case1.kaka_cache(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) #	60
    # case1.kaka_cache(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) #	52
    # case1.kaka_cache(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) #	16
    # case1.kaka_cache(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])    #25
    #
    # case1.kaka_dart("1S2D*3T")   # 37
    # case1.kaka_dart("1D2S#10S")  # 9
    # case1.kaka_dart("1D2S0T")    # 3
    # case1.kaka_dart("1S*2T*3S")  # 23
    # case1.kaka_dart("1D#2S*3S")  # 5
    # case1.kaka_dart("1T2D3D#")   # -4
    # case1.kaka_dart("1D2S3T*")   # 5
    #
    # case1.kaka_map()
