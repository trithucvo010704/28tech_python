from math import *
def sieve_of_eratosthenes_optimized(n):
    if n < 2:
        return []
    
    # Khởi tạo danh sách đánh dấu các số lẻ từ 3 trở đi (số 2 được xử lý riêng biệt)
    sieve = [True] * ((n // 2) + 1)
    sieve[0] = False  # Số 1 không phải là số nguyên tố
    
    # Xử lý số 2
    primes = [2] if n >= 2 else []
    
    # Duyệt qua các số lẻ từ 3 đến sqrt(n)
    for i in range(1, int(n**0.5) // 2 + 1):
        if sieve[i]:
            prime = 2 * i + 1
            # Đánh dấu các bội số của số lẻ
            for j in range(2 * i * (i + 1), n // 2 + 1, 2 * i + 1):
                sieve[j] = False
    
    # Tập hợp các số lẻ nguyên tố
    primes += [2 * i + 1 for i in range(1, n // 2 + 1) if sieve[i]]
    return primes

# Nhập vào N từ người dùng
N = int(input("Nhập vào N: "))
primes = sieve_of_eratosthenes_optimized(N)
print(f"Các số nguyên tố nhỏ hơn hoặc bằng {N}: {primes}")
