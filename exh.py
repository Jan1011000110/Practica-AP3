from yogi import read
import time
import sys


def llegir_entrada():
	C = read(int)  # n cotxes
	M = read(int)  # n millores
	K = read(int)  # n classes

	Ce: list[int] = []  # maxim per finestra tipus i
	for i in range(M):
		x = read(int)
		Ce.append(x)

	Ne: list[int] = []  # tamany finestra tipus i
	for i in range(M):
		x = read(int)
		Ne.append(x)

	Mill_Cotx: list[list[bool]] = []  # cal millorar cotxe tipus i amb millora j?
	Q: list[int] = []  # Quantitat tipus i
	
	for i in range(K):
		t, q = read(int), read(int)
		Q.append(q)
		Mill_Cotx.append([])  
		for j in range(M):
			x = read(int)
			Mill_Cotx[i].append(x == 1)
	return C,M,K,Ce,Ne,Q,Mill_Cotx






def main():
	C,M,K,Ce,Ne,Q,Mill_Cotx = llegir_entrada()
	

	def cerca_exhaustiva(i:int, resposta:list[int], cost:int, Q:list[int], millor_resposta:list[int], millor_cost:int):
		if i == C:
			# tots cotxes colocats
			if millor_cost == -1 or cost < millor_cost: # Encara no hem trobat cap resposta o la que hem trobat es millor
				millor_cost =  cost
				for j in range(len(resposta)):
					millor_resposta[j] = resposta[j]
			return millor_resposta, millor_cost
		if cost < millor_cost or millor_cost == -1:
			for j in range(K):
				if Q[j] > 0:
					Q[j] -= 1
					resposta[i] = j
					cnt = 0
					for c in range(M):
						cnt1 = 0
						for k in range(min(i+1,Ne[c])):
							cnt1 += (Mill_Cotx[resposta[i-k]][c])
						cnt += max(0, cnt1-Ce[c])
					if cost+cnt < millor_cost or millor_cost == -1:
						millor_resposta, millor_cost = cerca_exhaustiva(i+1, resposta, cost+cnt, Q, millor_resposta, millor_cost)
					Q[j] += 1
					resposta[i] = -1

		return millor_resposta, millor_cost


	millor_resposta = [0] * C
	millor_cost = -1
	resposta = [-1] * C
	millor_resposta, millor_cost = cerca_exhaustiva(0, resposta, 0,Q, millor_resposta, millor_cost)
	return millor_resposta, millor_cost

	    

if __name__ == "__main__":
	STime = time.time()
	millor_resposta, millor_cost = main()
	total_time = time.time() - STime
	# print(millor_cost, f"{total_time:.1f}")
	# for i in millor_resposta:
	# 		print(i, end = " ")
	if len(sys.argv) < 2:
		print("Error: falta el nom del fitxer de sortida.", file=sys.stderr)
		sys.exit(1)
	output_filename = sys.argv[1]
	with open(output_filename, "w") as f:
		print(millor_cost, f"{total_time:.1f}", file=f)
		for i in millor_resposta:
	 		print(i, end = " ", file=f)
		