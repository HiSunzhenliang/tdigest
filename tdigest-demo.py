#!/usr/bin/env python3
import math


def q_to_k(q, d):
    if q >= 0.5:
        return d - d * math.sqrt(0.5 - 0.5 * q)
    return d * math.sqrt(0.5 * q)


def k_to_q(k, d):
    k_div_d = k / d
    if k_div_d >= 0.5:
        base = 1 - k_div_d
        return 1 - 2 * base * base
    return 2 * k_div_d * k_div_d


def main():
    d = 10
    print("d: {}".format(d))
    X = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1],
         [6, 1], [7, 1], [8, 1], [9, 1], [10, 1],
         [11, 1], [12, 1], [13, 1], [14, 1], [15, 1],
         [59,1],[44,1],[33,1],[28,1],[19,1],[99,1],
         ]
    print("UNSORTED X:", X)

    X = sorted(X, key=lambda x: x[0])
    print("SORTED   X:", X)

    S = sum(x[1] for x in X)
    print("S:", S)

    C1 = []
    q0 = 0

    k = q_to_k(q0, d)
    qlimit = k_to_q(k+1, d)
    z = X[0]

    print("Begin:")
    for i in range(1, len(X)):
        print(
            "LOOP {} ===========================================================".format(i))
        print("ADD z: \033[0;31;40m{}\033[0m".format(z))
        q = q0 + (z[1] + X[i][1]) / S
        print("q:{:.4f}    qlimit:{:.4f}".format(q, qlimit))
        if q <= qlimit:
            t_sum = z[0] * z[1] + X[i][0] * X[i][1]
            z[1] += X[i][1]
            z[0] = t_sum / z[1]
            print("\033[0;33;40mUPDATE i:{:2}    q:{:.4f}     qlimit:{:.4f}     z:{}    C1:{}\033[0m".format(
                i, q, qlimit, z, C1))
        else:
            C1.append(z)
            q0 = q0 + z[1] / S
            k = q_to_k(q0, d)
            qlimit = k_to_q(k+1, d)
            z = X[i]
            print("\033[0;32;40mCREATE i:{:2}    q:{:.4f}     qlimit:{:.4f}     z:{}    C1:{}\033[0m".format(
                i, q, qlimit, z, C1))
    C1.append(z)
    print("END ===========================================================")
    print("X: ", X)
    print("\033[0;34;40mC1: {}\033[0m".format(C1))


if __name__ == '__main__':
    main()
    print('Done.')
  
