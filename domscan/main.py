'''
    ALERT: All comments are in Brazilian Portuguese (PT_BR)
'''

import whois # Biblioteca base do projeto

extensoes_aceitas = [ # Os domínios que serão aceitos.
    'com', 'com.br', 'net', 'org', 'org.br', 'info', 'biz', 'edu', 'gov', 'co', 'io', 'tv', 'me',
    'us', 'eu', 'uk', 'ca', 'au', 'jp', 'de', 'fr', 'it', 'es', 'nl', 'ru', 'ch', 'se', 'no', 'dk',
    'at', 'be', 'cz', 'fi', 'gr', 'hu', 'ie', 'kr', 'mx', 'pl', 'pt', 'sg', 'tr', 'za', 'ae', 'br',
    'cn', 'in', 'ro', 'sa', 'tw', 'vn', 'ar', 'cl', 'id', 'my', 'ph', 'th', 'hk', 'il', 'nz', 'ua'
]

class Domscan: # from domscan import Domscan
    # Verificar se um domínio está registrado ou não.
    def domain(self, dominio):
        extensao = self._extension(dominio)
        if extensao['status']:
            try:
                whois.whois(dominio)
                return {
                    "status": True,
                    "resumo": f'{dominio} já está registrado.'
                }
            except Exception as error:
                return {
                "status": False,
                "resumo": f'{dominio} está livre no mercado.'
            }
        return f"Invalid domain extension. (.{extensao['extensao']})"

    # Verificar se a extensão é válida.
    def _extension(self, dominio):
        dominio_usado = dominio.split('.', 1)[-1]
        if dominio_usado in extensoes_aceitas:
            return {
                "status": True,
                "extensao": dominio_usado
            }
        return {
                "status": False,
                "extensao": dominio_usado
            }