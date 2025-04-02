from character import Character
import random

class Hero(Character):
    def __init__(self,combat_strength,health_points):
        super().__init__(combat_strength, health_points)
    
    def hero_attacks(combat_strength, m_health_points):
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                @@@@@@          @@  @    
                @@       @@        @ @@     
            @%         @     @@@ @       
                @        @@     @@@@@     
                @@@@@        @@       
                @    @@@@                
            @@@ @@                        
        @@     @                         
    @@*       @                          
    @        @@                          
            @@                                                    
            @   @@@@@@@                    
            @            @                  
        @              @                  

    """
        print(ascii_image)
        print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("    |    You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= combat_strength

            print("    |    You have reduced the monster's health to: " + str(m_health_points))
        return m_health_points
    
    def __del__():
        super().__del__()
        

