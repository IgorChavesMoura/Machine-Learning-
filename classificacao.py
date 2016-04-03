#gordo perna curta  late

porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]

cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]

marcacoes = [1,1,1,-1,-1,-1]



from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados,marcacoes)
misterioso1 = [1,1,0]
misterioso2 = [1,1,1]
misterioso3 = [1,0,1]

marcacoes_teste = [1,-1,1]
teste = [misterioso1,misterioso2,misterioso3]

resultado = modelo.predict(teste)
diferenca = resultado - marcacoes_teste

acertos = [d for d in diferenca if d==0]

nacertos = len(acertos)
nelementos = len(teste)

taxa_acertos = 100.0*nacertos/nelementos

print(taxa_acertos)



