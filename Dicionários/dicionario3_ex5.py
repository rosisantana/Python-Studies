# Cidades: Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário. Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser algo como country, population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.

cities = { 
    'paris': {
        'país': 'frança',
        'população': '66.99 milões',
        'curiosidade': 'Você sabia que a cidade de Paris já teve um outro nome? Ele foi dado à cidade pelos romanos quando chegaram, que não passava de uma vila de pescadores. Como o rio Sena cobria a vila ao encher e deixava tudo coberto de lama, deram o nome Lutetia, significa “lama” em latim.',
    },

    'nova_york': {
        'país': 'estados unidos',
        'população': '8.62 milhões',
        'curiosidade': ' Foi em Nova York que foi fundada a primeira pizzaria dos Estados Unidos, em 1905, pelo imigrante italiano Gennaro Lomardi. A pizzaria está aberta até hoje.',
    },
    'kuala_lumpur': {
        'país': 'malásia', 
        'população': '1.8 milhões',
        'curiosidade': 'Devido a sua diversidade cultural, os cidadãos e turistas tem a possibilidade de comemorar 3 vezes o ano novo sendo elas tradicionalmente no dia 1° de janeiro e o ano novo islâmico e o ano novo chinês, que não possuem dia fixo.',
    },
}

for cidade, cidades_infos in cities.items():
    print('\nCidade: ' + cidade.title() + 
    '\n\tPaís: ' + cidades_infos['país'].title() + 
    '\n\tPopulação: ' + cidades_infos['população'] + 
    '\n\tCuriosidade: ' + cidades_infos['curiosidade'])
    
