# Gerador de Senhas

Programa em Python para gerar senhas seguras com requisitos personalizáveis.

## Descrição
Gera senhas de pelo 8 caracteres que obrigatoriamente contêm:
- 2 letras minúsculas
- 2 letras maiúsculas
- 2 números
- 2 caracteres especiais

O usuário pode especificar um tamanho maior que o mínimo para gerar senhas mais longas. Nunca menor.

## Requisitos
- Python 3.8+ (recomendado)
- Módulos padrão da biblioteca (nenhuma dependência externa)

## Uso
1. Clone ou copie este repositório.
2. Execute o script principal (certifique-se de estar no caminho correto quando executar o script):
   - No Windows (terminal): python gerador_senha.py
3. Siga as instruções exibidas para gerar a senha.

## Exemplo
Ao executar, o programa deve retornar uma senha que satisfaça todos os requisitos listados acima. Exemplo de saída:
- `aB3!f9K#t2`

## Boas práticas
- Armazene senhas geradas em gerenciadores de senhas confiáveis.
- Não compartilhe senhas em texto plano ou canais inseguros.

## Melhorias planejadas
- Refatorar o código em funções reutilizáveis. ✅
- Permitir opção de configuração de comprimento e composição (ex.: exigir 2 maiúsculas, 2 minúsculas, 2 números, 2 símbolos). ✅
- Adicionar testes automatizados e validação mais robusta. ❌
- Fornecer interface gráfica para o usuário. ❌
- Permitir que o usuário passe os paramêtros desejados para criar uma senha personalizada. No entanto, exibir uma mensagem que essa personalização pode não ser a melhor esclha em termos de segurança. Por exemplo:
   - Apenas números.
   - Apenas letras.
   - Apenas números e símbolos.

## Contribuição
Pull requests são bem-vindos. Abra uma issue antes de mudanças maiores.
