from conn import *

# ========================= GET Data ================================
	# ============================= Tabel ===========================

def data_abstract(t):
	sql = 'SELECT teks FROM `'+t+'`;'
	q.execute(sql)
	d = q.fetchall()
	data = []
	for i  in d:
		for j in i:
			data.append(j)
	return data

da1 = data_abstract("multimedia")
da2 = data_abstract("hs")
da3 = data_abstract("ai")
da4 = data_abstract("network")

	#========================== TF IDF ============================

def get_tfidf(v):
	result = []
	sql = 'SELECT teks,values_'+v+' FROM `tfidf`'
	q.execute(sql)
	d = q.fetchall()
	result.append([])
	result.append([])
	for i in d:
		result[0].append(i[0])
		result[1].append(i[1])
	return result

get_tfidf1 = get_tfidf('multimedia')
get_tfidf2 = get_tfidf('hs')
get_tfidf3 = get_tfidf('ai')
get_tfidf4 = get_tfidf('network')
	# ======================================= P(Data)
def p_data(id_table,table):
	q.execute('SELECT `'+id_table+'` FROM `'+table+'`') 
	count = len(q.fetchall())
	return count

d1 = p_data('id_multimedia','multimedia') #bug if c == 0 : c = 1 ==============
d2 = p_data('id_hs','hs')
d3 = p_data('id_ai','ai')
d4 = p_data('id_network','network')


	# ====================================== P(Class)
def p_class(count_k):
	jml_klass = d1+d2+d3+d4
	prob = count_k/jml_klass
	return prob

c1 = p_class(d1)
c2 = p_class(d2)
c3 = p_class(d3)
c4 = p_class(d4)
#===============================================================
# ============================== Join Data =========================

def join_data(da):
	data = []
	for i in range(len(da)):
		data.append(da[i].split())

	return data

join_data1 = join_data(da1)
join_data2 = join_data(da2)
join_data3 = join_data(da3)
join_data4 = join_data(da4)

# ============================= Value TFIDF ========================
def val_tfidf(jd,tfi):
	tfidf = []
	val_tfidf = tfi[1]
	for i in range(len(jd)):
		tfidf.append([])
		for j in jd[i]:
			if j in tfi[0]:
				idx = tfi[0].index(j)
				tfidf[i].append(val_tfidf[idx])

	return tfidf

val_mulmed_tfidf1 = val_tfidf(join_data1,get_tfidf1)
val_mulmed_tfidf2 = val_tfidf(join_data1,get_tfidf2)
val_mulmed_tfidf3 = val_tfidf(join_data1,get_tfidf3)
val_mulmed_tfidf4 = val_tfidf(join_data1,get_tfidf4)

val_hs_tfidf1 = val_tfidf(join_data2,get_tfidf1)
val_hs_tfidf2 = val_tfidf(join_data2,get_tfidf2)
val_hs_tfidf3 = val_tfidf(join_data2,get_tfidf3)
val_hs_tfidf4 = val_tfidf(join_data2,get_tfidf4)

val_ai_tfidf1 = val_tfidf(join_data3,get_tfidf1)
val_ai_tfidf2 = val_tfidf(join_data3,get_tfidf2)
val_ai_tfidf3 = val_tfidf(join_data3,get_tfidf3)
val_ai_tfidf4 = val_tfidf(join_data3,get_tfidf4)

val_network_tfidf1 = val_tfidf(join_data4, get_tfidf1)
val_network_tfidf2 = val_tfidf(join_data4, get_tfidf2)
val_network_tfidf3 = val_tfidf(join_data4, get_tfidf3)
val_network_tfidf4 = val_tfidf(join_data4, get_tfidf4)

# ========================= Result =================================

def result(v,c):
	pk = c
	val = []
	for i in range(len(v)) :
		for j in v[i]:
			k = j+1
			pk *= k
		val.append(pk)
	return val

res_mulmed1 = result(val_mulmed_tfidf1,c1)
res_mulmed2 = result(val_mulmed_tfidf2,c2)
res_mulmed3 = result(val_mulmed_tfidf3,c3)
res_mulmed4 = result(val_mulmed_tfidf4,c4)

res_hs1 = result(val_hs_tfidf1,c1)
res_hs2 = result(val_hs_tfidf2,c2)
res_hs3 = result(val_hs_tfidf3,c3)
res_hs4 = result(val_hs_tfidf4,c4)

res_ai1 = result(val_ai_tfidf1,c1)
res_ai2 = result(val_ai_tfidf2,c2)
res_ai3 = result(val_ai_tfidf3,c3)
res_ai4 = result(val_ai_tfidf4,c4)

res_network1 = result(val_network_tfidf1,c1)
res_network2 = result(val_network_tfidf2,c2)
res_network3 = result(val_network_tfidf3,c3)
res_network4 = result(val_network_tfidf4,c4)


def result_bdg(res1, res2, res3, res4, res5):
	for i in range(len(res1)) :
		if  res1[i] > res2[i] and res1[i] > res3[i] and res1[i] > res4[i] :
			sql = "INSERT INTO `CV` VALUES ( '"+res5+"', '"+str(res1[i])+"', '"+str(res2[i])+"', '"+str(res3[i])+"', '"+str(res4[i])+"', 'Multimedia');"
			q.execute(sql)
			conn.commit()

		elif res2[i] > res1[i] and res2[i] > res3[i] and res2[i] > res4[i] :
			sql = "INSERT INTO `CV` VALUES ( '"+res5+"', '"+str(res1[i])+"', '"+str(res2[i])+"', '"+str(res3[i])+"', '"+str(res4[i])+"', 'Hardware & software');"
			q.execute(sql)
			conn.commit()

		elif res3[i] > res1[i] and res3[i] > res2[i] and res3[i] > res4[i] :
			sql = "INSERT INTO `CV` VALUES ( '"+res5+"', '"+str(res1[i])+"', '"+str(res2[i])+"', '"+str(res3[i])+"', '"+str(res4[i])+"', 'AI');"
			q.execute(sql)
			conn.commit()

		elif res4[i] > res1[i] and res4[i] > res2[i] and res4[i] > res3[i] :
			sql = "INSERT INTO `CV` VALUES ( '"+res5+"', '"+str(res1[i])+"', '"+str(res2[i])+"', '"+str(res3[i])+"', '"+str(res4[i])+"', 'network');"
			q.execute(sql)
			conn.commit()

		else:
			print ('unknow')

result_bdg(res_mulmed1,res_mulmed2,res_mulmed3,res_mulmed4,'Multimedia')	#mulmed
result_bdg(res_hs1,res_hs2,res_hs3,res_hs4, 'hardware')						#Hardware
result_bdg(res_ai1,res_ai2,res_ai3,res_ai4, 'AI')							#AI
result_bdg(res_network1,res_network2,res_network3,res_network4, 'Network')	#Network