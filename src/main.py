import math
import time
import random
start_time = time.time()
# fungsi untuk menghitung jarak antara dua titik dalam ruang 3D
def cari_jarak(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

# fungsi untuk mencari jarak terdekat dari pasangan titik dalam daftar P
def closest_pair_3d(P):
    n = len(P)
    if n <= 3:
        min_pair = min([(P[i], P[j]) for i in range(n) for j in range(i+1, n)], key=lambda pair: cari_jarak(pair[0], pair[1]))
        return (cari_jarak(min_pair[0], min_pair[1]), min_pair)
    
    # membagi daftar P menjadi dua bagian
    mid = n // 2
    Pl = P[:mid]
    Pr = P[mid:]
    
    # mencari jarak terdekat dari pasangan titik di setiap bagian
    dl, min_pair_l = closest_pair_3d(Pl)
    dr, min_pair_r = closest_pair_3d(Pr)
    d, min_pair = (dl, min_pair_l) if dl < dr else (dr, min_pair_r)
    
    # mencari jarak terdekat dari pasangan titik yang satu berada di Pl dan yang satu lagi berada di Pr
    mid_point = P[mid][0]
    S = [p for p in P if mid_point - d <= p[0] <= mid_point + d]
    S.sort(key=lambda x: x[1])
    k = len(S)
    for i in range(k):
        for j in range(i+1, min(i+8, k)):
            d_ij = cari_jarak(S[i], S[j])
            if d_ij < d:
                d = d_ij
                min_pair = (S[i], S[j])
    
    return (d, min_pair)

# fungsi untuk menghasilkan titik-titik secara acak dalam ruang 3D
def acak(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        z = random.uniform(0, 100)
        points.append((x, y, z))
    return points

# fungsi utama
def main():
    end_time = time.time()
    elapsed_time = end_time - start_time
    # input jumlah titik dari pengguna
    n = int(input("Masukkan jumlah titik: "))

    # menghasilkan titik-titik secara acak
    P = acak(n)

    # # mencetak daftar titik-titik
    # print("Daftar titik-titik: ", P)

    # mencetak jarak terdekat antara pasangan titik
    closest_pair_distance, closest_pair = closest_pair_3d(P)
    print("Jarak terdekat antara pasangan titik: ", closest_pair_distance)

    # Print Pasangan terdekat
    print("Pasangan titik terdekat: ", closest_pair)


    # mencetak waktu yang keluar
    print("Waktu : {:.6f} detik".format(elapsed_time)) 

if __name__ == '__main__':
    main()
