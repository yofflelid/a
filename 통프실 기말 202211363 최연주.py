# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:01:05 2023

@author: JUYEON
"""
1. 
height=[58,59,60,61,62,63,64,65,66,67,68,69,70,71,72]
weight=[115,117,120,123,126,129,132,135,139,142,146,150,154,159,164]

1) 두 변수의 상관계수를 계산하는 corr() 함수 작성 
 
def corr(x, y):
    # 각 변수의 평균 계산
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # 각 변수의 편차와 제곱 편차 계산
    deviation_x = [i - mean_x for i in x]
    deviation_y = [i - mean_y for i in y]
    
    # 편차의 곱 계산
    deviation_product = sum([deviation_x[i] * deviation_y[i] for i in range(len(deviation_x))])
    
    # 각 변수의 제곱 편차 계산
    deviation_x_sq = sum([(i - mean_x) ** 2 for i in x])
    deviation_y_sq = sum([(i - mean_y) ** 2 for i in y])
    
    # 상관계수 계산
    correlation = deviation_product / ((deviation_x_sq * deviation_y_sq) ** 0.5)
    
    return correlation

# 예시 데이터
height = [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
weight = [115, 117, 120, 123, 126, 129, 132, 135, 139, 142, 146, 150, 154, 159, 164]

# 상관계수 계산
result_corr = corr(height, weight)
print("두 변수의 상관계수:", result_corr)

#실행 결과 
두 변수의 상관계수: 0.9954947677842162



2) simpleRegression 클래스를 상속받아 앞에서 작성한 corr()과
 결정계수를 계산하는 R()이라는 함수를 추가한 클래스를 구현하고 
 위 자료를 이용한 계산 결과를 제시하시오. 
class simpleRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fit(self):
        # 기울기와 절편 계산
        mean_x = sum(self.x) / len(self.x)
        mean_y = sum(self.y) / len(self.y)
        numerator = sum([(self.x[i] - mean_x) * (self.y[i] - mean_y) for i in range(len(self.x))])
        denominator = sum([(xi - mean_x) ** 2 for xi in self.x])
        self.slope = numerator / denominator
        self.intercept = mean_y - self.slope * mean_x

    def predict(self, new_x):
        # 새로운 x값을 이용한 예측
        return self.slope * new_x + self.intercept
class CustomRegression(simpleRegression):
    def corr(self, x, y):
        mean_x = sum(x) / len(x)
        mean_y = sum(y) / len(y)
        deviation_x = [i - mean_x for i in x]
        deviation_y = [i - mean_y for i in y]
        deviation_product = sum([deviation_x[i] * deviation_y[i] for i in range(len(deviation_x))])
        deviation_x_sq = sum([(i - mean_x) ** 2 for i in x])
        deviation_y_sq = sum([(i - mean_y) ** 2 for i in y])
        correlation = deviation_product / ((deviation_x_sq * deviation_y_sq) ** 0.5)
        return correlation

    def R(self, x, y):
        corr = self.corr(x, y)
        R_squared = corr ** 2
        return R_squared

# 데이터
height = [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
weight = [115, 117, 120, 123, 126, 129, 132, 135, 139, 142, 146, 150, 154, 159, 164]

# CustomRegression 클래스를 이용해 계산
regression = CustomRegression(height, weight)
correlation = regression.corr(height, weight)
R_squared = regression.R(height, weight)

print("두 변수의 상관계수:", correlation)
print("결정계수:", R_squared)

#실행 결과 
두 변수의 상관계수: 0.9954947677842162
결정계수: 0.9910098326857505




2. 합동 분산을 이용 

x=[1.16, 1.18, 1.15, 1.17, 1.14]
y=[1.24, 1.22, 1.18, 1.23, 1.19 ]



1) 두 모집단의 평균을 비교하기 위한 평균차이의 신뢰구간을 추정하는 함수를 작성하시오.
    
import scipy.stats as stats
import numpy as np

def confidence_interval(x, y, alpha=0.05):
    # 데이터셋 크기
    n_x = len(x)
    n_y = len(y)

    # 각 데이터셋의 평균 및 합동 분산 계산
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    var_x = np.var(x, ddof=1)
    var_y = np.var(y, ddof=1)

    # 합동 분산 계산
    pooled_var = ((n_x - 1) * var_x + (n_y - 1) * var_y) / (n_x + n_y - 2)

    # 표준 오차 계산
    std_error = np.sqrt(pooled_var * (1 / n_x + 1 / n_y))

    # t 분포를 이용한 신뢰구간 계산
    df = n_x + n_y - 2
    t_value = stats.t.ppf(1 - alpha / 2, df)
    margin_of_error = t_value * std_error

    # 신뢰구간 계산
    lower_bound = (mean_x - mean_y) - margin_of_error
    upper_bound = (mean_x - mean_y) + margin_of_error

    return lower_bound, upper_bound

# 데이터
x = [1.16, 1.18, 1.15, 1.17, 1.14]
y = [1.24, 1.22, 1.18, 1.23, 1.19]

# 평균차이의 신뢰구간 계산
lower, upper = confidence_interval(x, y)
print(f"평균차이의 신뢰구간: ({lower}, {upper})")

#실행 결과 
평균차이의 신뢰구간: (-0.08328016197249521, -0.02071983802750444)



2) 1)에서 작성한 함수를 멤버로 갖는 클래스를 작성하고 결과를 제시하시오. 
class ConfidenceInterval:
    def __init__(self, x, y, alpha=0.05):
        self.x = x
        self.y = y
        self.alpha = alpha

    def confidence_interval(self):
        # 데이터셋 크기
        n_x = len(self.x)
        n_y = len(self.y)

        # 각 데이터셋의 평균 및 합동 분산 계산
        mean_x = np.mean(self.x)
        mean_y = np.mean(self.y)
        var_x = np.var(self.x, ddof=1)
        var_y = np.var(self.y, ddof=1)

        # 합동 분산 계산
        pooled_var = ((n_x - 1) * var_x + (n_y - 1) * var_y) / (n_x + n_y - 2)

        # 표준 오차 계산
        std_error = np.sqrt(pooled_var * (1 / n_x + 1 / n_y))

        # t 분포를 이용한 신뢰구간 계산
        df = n_x + n_y - 2
        t_value = stats.t.ppf(1 - self.alpha / 2, df)
        margin_of_error = t_value * std_error

        # 신뢰구간 계산
        lower_bound = (mean_x - mean_y) - margin_of_error
        upper_bound = (mean_x - mean_y) + margin_of_error

        return lower_bound, upper_bound


x = [1.16, 1.18, 1.15, 1.17, 1.14]
y = [1.24, 1.22, 1.18, 1.23, 1.19]

ci = ConfidenceInterval(x, y)
lower, upper = ci.confidence_interval()
print(f"평균차이의 신뢰구간: ({lower}, {upper})")


#실행 결과 
평균차이의 신뢰구간: (-0.08328016197249521, -0.02071983802750444)















