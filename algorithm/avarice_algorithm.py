#!/usr/bin/env python
# -*- coding:utf-8 -*-


def avarice():
    # The set_list contain the states of needed override
    states_needed = ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
    set_states_need = set(states_needed)

    # The dic represent the broadcasting
    stations = dict()
    stations["kone"] = {"id", "nv", "ut"}
    stations["ktwo"] = {"wa", "id", "mt"}
    stations["kthree"] = {"or", "nv", "ca"}
    stations["kfour"] = {"nv", "ut"}
    stations["kfive"] = {"ca", "az"}

    # Use the set store result(The final select station)
    final_stations = set()

    while set_states_need:
        best_station = None
        # 存储该电台覆盖了哪些未被覆盖的州
        states_covered = set()
        # 执行循环，从中选出覆盖最广的station
        for station, states_for_station in stations.items():  # 对字典进行迭代，取出电台以及该电台覆盖的州
            coverd = set_states_need & states_for_station  # 需要覆盖的与该电台要覆盖的求交集
            if len(coverd) > len(states_covered):  # 覆盖的区域比上次覆盖的大，循环完成后取出最大的
                best_station = station  # 最优的电台设定为该电台
                states_covered = coverd  # 覆盖的州设置为该州
        final_stations.add(best_station)  # 加入到最终结果中，存储在集合中， 也可以是列表
        set_states_need -= states_covered  # 减掉最大的已经覆盖的州（差集）
    return final_stations


if __name__ == '__main__':
    result = avarice()
    print result
