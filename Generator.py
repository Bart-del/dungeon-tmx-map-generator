class GeneratorClass:

    @staticmethod
    def generateNewMap():
        result = ''

        result = """
        <?xml version="1.0" encoding="UTF-8"?>
            <map version="1.2" tiledversion="1.2.3" orientation="orthogonal" renderorder="left-down" width="200" height="200" tilewidth="16" tileheight="16" infinite="0" nextlayerid="4" nextobjectid="1">
            <tileset firstgid="1" name="0x72_16x16DungeonTileset.v4" tilewidth="16" tileheight="16" tilecount="256" columns="16">
            <image source="0x72_16x16DungeonTileset.v4.png" width="256" height="256"/>
            </tileset>
            <layer id="1" name="Warstwa Kafelków 1" width="200" height="200">
                <data encoding="csv">
                    @
                    @ LAYER 1 DATA
                    @
                </data>
            </layer>
            <layer id="2" name="Warstwa Kafelków 2" width="200" height="200">
                <data encoding="csv">
                    @
                    @ LAYER 2 DATA
                    @
                </data>
            </layer>
                <layer id="3" name="Warstwa Kafelków 3" width="200" height="200">
                <data encoding="csv">
                    @
                    @ LAYER 3 DATA
                    @    
                </data>
            </layer>
        </map>
            
        """
        return result
