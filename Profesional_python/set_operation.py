
#establecemos nuestros diferentes sets por tipo de pokemon XD

pokemon_tipo_fuego = { 'Charizard', 'Moltres' }
pokemon_tipo_volador = { 'Charizard', 'Butterfree', 'Pidgeot', 'Fearow', 'Dodrio', 'Gyarados', 'Aerodactyl',
  'Articuno', 'Zapdos', 'Moltres', 'Dragonite' }
pokemon_tipo_veneno = { 'Butterfree' }
pokemon_tipo_normal = { 'Pidgeot', 'Fearow', 'Dodrio' }
pokemon_tipo_agua = { 'Gyarados' }
pokemon_tipo_roca = { 'Aerodactyl' }
pokemon_tipo_hielo = { 'Articuno' }
pokemon_tipo_electrico = { 'Zapdos','Riachu' }
pokemon_tipo_dragon = { 'Dragonite','Riachu' }

#unión
my_set1 = pokemon_tipo_fuego | pokemon_tipo_agua
print(f'Pokemon tipo fuego | agua: {my_set1}') # >> Pokemon tipo fuego | agua: {'Moltres', 'Charizard', 'Gyarados'}

#intersección
my_set2 = pokemon_tipo_normal & pokemon_tipo_volador
print(f'Pokemon tipo normal & volador: {my_set2}') # >> Pokemon tipo normal & volador: {'Fearow', 'Dodrio', 'Pidgeot'}

#diferencia
my_set3 = pokemon_tipo_volador - pokemon_tipo_fuego
print(f'Pokemon tipo volador - fuego: {my_set3}') 
# >> Pokemon tipo volador - fuego: {'Zapdos', 'Dodrio', 'Aerodactyl', 'Fearow', 'Dragonite', 'Pidgeot', 'Articuno', 'Gyarados', 'Butterfree'}

#diferencia asimetrica
my_set4 = pokemon_tipo_dragon ^ pokemon_tipo_electrico
print(f'Pokemon tipo dragon ^ electrico: {my_set4}')
# >> Pokemon tipo dragon ^ electrico: {'Dragonite', 'Zapdos'}




