
#ABAIXO POSSUI UMA LINHA DE CODIGO ESTRANHA NA QUAL É A SOLUÇÃO DE UM ERRO QUE NAO RECONHECIA O MODULO (a pasta src) CORRETAMENTE

import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))) # Adiciona manualmente o caminho da pasta src


from exemplo import ListaCompras

class TestListaCompras(unittest.TestCase):
    def setUp(self):
        # Configuração inicial antes de cada teste. Cria uma nova instância da classe ListaCompras.
        self.lista = ListaCompras()

    def test_adicionar_produto(self):
        # Testa se um produto é adicionado corretamente à lista.
        resultado = self.lista.adicionar_produto("maçã")
        # Verifica se "maçã" está na lista de produtos.
        self.assertIn("maçã", self.lista.produtos)
        # Verifica se a mensagem retornada é a correta.
        self.assertEqual(resultado, "O produto maçã foi adicionado à lista.")

    def test_remover_produto(self):
        # Testa se um produto é removido corretamente da lista.
        self.lista.adicionar_produto("maçã")  # Adiciona um produto para teste.
        resultado = self.lista.remover_produto("maçã")
        # Verifica se "maçã" não está mais na lista de produtos.
        self.assertNotIn("maçã", self.lista.produtos)
        # Verifica se a mensagem retornada é a correta.
        self.assertEqual(resultado, "O produto maçã foi removido da lista.")

    def test_remover_produto_nao_existente(self):
        # Testa a remoção de um produto que não existe na lista.
        resultado = self.lista.remover_produto("banana")
        # Verifica se a mensagem de produto não encontrado é retornada.
        self.assertEqual(resultado, "Este produto não está na lista de compras!")

    def test_ver_lista_vazia(self):
        # Testa se a lista vazia retorna a mensagem apropriada.
        resultado = self.lista.ver_lista()
        # Verifica se a mensagem indica que a lista está vazia.
        self.assertEqual(resultado, "A lista de compras está vazia.")

    def test_ver_lista(self):
        # Testa se a lista de produtos é exibida corretamente quando há itens.
        self.lista.adicionar_produto("maçã")
        self.lista.adicionar_produto("banana")
        # Verifica se a lista contém os produtos corretos.
        self.assertEqual(self.lista.ver_lista(), ["maçã", "banana"])

if __name__ == "__main__":
    # Executa os testes quando o arquivo é executado diretamente.
    unittest.main()
