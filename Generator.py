import random
"""
    Generator of TMX map - documentation
    difficulty level - min 50 - max 100
        
"""


def __randomize_level(difficulty_lvl):
    if difficulty_lvl > 100 or difficulty_lvl < 50:
        raise Exception("Wrong value of difficulty level")
    squares_amount = int(difficulty_lvl / random.randint(5, 8))

    print("Difficulty level: ", difficulty_lvl)
    print("Squares amount: ", squares_amount)

    for x in range(squares_amount):


    result = {'squares_amount': squares_amount}
    return result


def __initialize_layer(width, height):
    output = ''
    for n in range(width * height):
        if n == width * height - 1:
            output = output + '0'
        else:
            output = output + '0,'
    return output


def __generate_background_layer(width, height):
    output = ''
    for n in range(width * height):
        if n == width * height - 1:
            output = output + '101'
        else:
            output = output + '101,'
    return output


def __generate_ground_layer(width, height):
    output = __initialize_layer(width, height)
    square_x = 16
    square_y = 0
    x_loop_controller = 0

    for y in range(10):
        for x in range(x_loop_controller, square_x):
            if x_loop_controller % 2 == 0:
                output = output[:x_loop_controller] + 'g' + output[x_loop_controller + 1:]
            x_loop_controller += 1
        square_x = square_x + 400
        x_loop_controller = x_loop_controller + 384

    output = output.replace('g', '51')
    return output


def __generate_object_passive_layer(width, height):
    output = __initialize_layer(width, height)
    return output


def __generate_object_active_layer(width, height):
    output = __initialize_layer(width, height)
    return output


def __generate_enemies_layer(width, height):
    output = __initialize_layer(width, height)
    return output


def generate_new_Map(widthMap, heightMap, difficulty_lvl):
    lvl_random_data = __randomize_level(difficulty_lvl)
    new_file_map = open("target\\newTileGeneratedMap.tmx", "w+")
    result = """<?xml version="1.0" encoding="UTF-8"?>
<map version="1.2" tiledversion="1.2.3" orientation="orthogonal" renderorder="left-down" width="{}" height="{}" tilewidth="16" tileheight="16" infinite="0" nextlayerid="4" nextobjectid="1">
 <tileset firstgid="1" name="0x72_16x16DungeonTileset.v4" tilewidth="16" tileheight="16" tilecount="256" columns="16">
  <image source="0x72_16x16DungeonTileset.v4.png" width="256" height="256"/>
 </tileset>
 <layer id="1" name="LAYER_BACKGROUND" width="200" height="200">
  <data encoding="csv">
{}
</data>
 </layer>
 <layer id="2" name="LAYER_GROUND" width="200" height="200">
  <data encoding="csv">
{}
</data>
 </layer>
 <layer id="3" name="LAYER_OBJECT_PASSIVE" width="200" height="200">
  <data encoding="csv">
{}   
</data>
 </layer>
 <layer id="3" name="LAYER_OBJECT_ACTIVE" width="200" height="200">
  <data encoding="csv">
{}   
</data>
 </layer>
 <layer id="3" name="LAYER_ENEMIES" width="200" height="200">
  <data encoding="csv">
{}  
</data>
 </layer>
</map>
 """.format(widthMap, heightMap,
            __generate_background_layer(widthMap, heightMap),
            __generate_ground_layer(widthMap, heightMap),
            __generate_object_passive_layer(widthMap, heightMap),
            __generate_object_active_layer(widthMap, heightMap),
            __generate_enemies_layer(widthMap, heightMap))
    new_file_map.write(result)
    new_file_map.close()
