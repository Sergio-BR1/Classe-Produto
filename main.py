class Produto(): 
	def __init__(self, nome, preco, quantidade):
		self._nome = nome
		self._preco = preco
		self._quantidade = quantidade

	
	def get_nome(self):
		return self._nome 

	def get_preco(self):
		if self._quantidade <=10:
			return (f"R${(self._preco * self._quantidade):.2f}")
		elif 11 <= self._quantidade <= 20:
			return (f"R${((self._preco * self._quantidade) - self._preco * 0.1 * self._quantidade):.2f}") 

		elif 21 <= self._quantidade <= 50:
			return (f"R${((self._preco * self._quantidade) - self._preco * 0.2 * self._quantidade):.2f}") 
		else:
			return (f"R${((self._preco * self._quantidade) - self._preco * 0.25 * self._quantidade):.2f}") 	

	def get_quant(self):
		return self._quantidade

	def compra(self):
		print(f"Produto: {self.get_nome()}")
		print(f"Quantidade comprada: {self.get_quant()}")
		print(f"Preço: {self.get_preco()}")
		print()

if __name__ == "__main__":

	produto1 = Produto("Leite", 4.00, 51)
	produto1.compra()
	
	produto2 = Produto("Feijão", 7.40, 12)
	produto2.compra()
	
	produto3 = Produto("Carne Moída", 20.00, 2)
	produto3.compra

	produto4 = Produto("Ovos", 0.35, 50)
	produto4.compra()