# domscan | v1

Desenvolvi uma solução em Python para verificar o status de registro de domínios. Esta ferramenta permite determinar se um determinado domínio está registrado ou não. Embora não seja possível incluir todos os domínios existentes, compilei uma lista abrangente para cobrir uma ampla gama de possibilidades.

> **ALERTA:** *Não registrei o meu projeto no pypi. Então não é possível instalar atráves do PIP.*

# Guia de uso (Exemplos)

```python
from domscan import Domscan

dom = Domscan()
print(dom.domain('youtube.com'))
# {'status': True, 'resumo': 'youtube.com já está registrado.'}

print(dom.domain('youtub3333e.com'))
# {'status': False, 'resumo': 'youtub3333e.com está livre no mercado.'}

print(dom.domain('youtube.come')) # Extensão inválida.
# Invalid domain extension. (.come)
```
