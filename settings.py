class Settings():
    """ Save all configurations of alien invasion """

    def __init__(self):
        self.screen_width = 990;
        self.screen_height = 690;
        self.bgColor = (230,230,230);

        #ship settings
        self.ships_amount = 3;

        #bullet settings
        self.bullet_width = 3;
        self.bullet_height = 15;
        self.bullet_color = 60,60,60;
        self.bullet_allowed = 3;
        #ufo settings
        self.fleet_drop_speed = 10;
        # 
        self.scale_acceleration =  1.1;
        #
        self.scale_score = 1.5;
        self.dynamic_settings_init();
        
    def dynamic_settings_init(self):
        #ship settings
        self.factor_ship_speed = 1.5;
        #bullet settings
        self.factor_bullet_speed = 1;
        #ufo settings
        self.factor_alien_speed = 1;
        #fleet direction, case: 1 --> | case: -1 <--
        self.fleet_direction = 1;
        #Score
        self.points_alien = 50
    
    def increase_speed(self):
        self.factor_ship_speed *= self.scale_acceleration;
        self.factor_bullet_speed *= self.scale_acceleration;
        self.factor_alien_speed *= self.scale_acceleration;
        
        self.points_alien = int(self.points_alien * self.scale_score);
        print(self.points_alien);