import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y, label='y = 2x', color='blue', marker='o')

# 제목과 라벨
plt.title('기본 선 그래프')
plt.xlabel('x 값')
plt.ylabel('y 값')
plt.legend()  # 범례 표시

# 그래프 출력
plt.grid(True)
plt.show()
