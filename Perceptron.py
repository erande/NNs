import numpy as np

# 形状: {1 : 圆形; -1 : 非圆形}
# 质地: {1 : 光滑; -1 : 粗糙}
# 重量: {1 : >1磅; -1 : <1磅}

def getdata():
	# 训练集
	# 标准香蕉模式
	p1 = np.mat([[-1],[1],[-1]])
	# 标准苹果模式
	p2 = np.mat([[1],[1],[-1]]) 
	train = {1:p1,0:p2}

	# 粗糙香蕉测试集
	a0 = np.mat([[-1],[-1],[-1]])
	a1 = np.mat([[-1],[0.7],[-1]])
	a2 = np.mat([[-1],[1],[-1]])
	a3 = np.mat([[-1],[1],[-1]])
	test = [a0,a1,a2,a3]
	
	return train, test

def hardlim(e):
	if e >= 0:
		return 1
	else:
		return 0
	
def classify(p,w,b):
	return hardlim(w * p + b)

def study(train):
	w = np.mat([[0.5,-1,-0.5]])
	b = 0.5
	count = len(train)
	while count!=0:
		count = len(train)
		for t,p in train.items():
			a = hardlim(w * p + b)
			e = t - a
			if e == 0:
				count -= 1
			w = w + e * p.T
			b = b + e
	return w,b

def test():
	train, test = getdata()
	w, b = study(train)
	print('w=',w)
	print('b=',b)

	L = len(test)
	count = 0
	banana = 1
	for p in test:
		a = classify(p,w,b)
		if a == banana:
			count += 1
			print(p.T,'预测正确')
	print('正确率:',(count / L * 1.0) * 100 ,'%')


if __name__ == '__main__':
    test()


