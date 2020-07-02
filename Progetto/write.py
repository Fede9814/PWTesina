import arcade
import Fov

class Card(arcade.Sprite):

    def __init__(self):

        self.Birth,            =   Fov.Birth
        self.IDVehicle,        =   Fov.IDVehicle    
        self.pilot_sex,        =   Fov.pilot_sex    
        self.true_age,         =   Fov.true_age    
        self.pilot_name,       =   Fov.pilot_name    
        self.pilot_surname,    =   Fov.pilot_surname        
        self.plate,            =   Fov.plate
        self.region,           =   Fov.region
        self.car_model,        =   Fov.car_model    
        self.Displacement,     =   Fov.Displacement        
        self.Tax_status,       =   Fov.Tax_status    
        self.Insurance_status  =   Fov.Insurance_status            

    def on_draw(self):

        self.Json_car =  {
            "CarBirthTime":     self.Birth,
            "IDVehicle" :       self.IDVehicle,
            "Gender":           self.pilot_sex,
            "Age":              self.true_age,
            "Name":             self.pilot_name,
            "Surname":          self.pilot_surname,
            "Plate":            self.plate,
            "Region":           self.region,
            "Model" :           self.car_model,
            "Displacement" :    self.Displacement,
            "CarTax" :          self.Tax_status,
            "Insurance" :       self.Insurance_status
            }
      
        self.str_card_birth             = str(self.IDVehicle)
        self.str_card_IDVehicle         = str(self.IDVehicle)
        self.str_card_pilot_sex         = str(self.pilot_sex)
        self.str_card_true_age          = str(self.true_age)
        self.str_card_pilot_name        = str(self.pilot_name)
        self.str_card_pilot_surname     = str(self.pilot_surname)
        self.str_card_plate             = str(self.plate)
        self.str_card_region            = str(self.region)
        self.str_card_car_model         = str(self.car_model)
        self.str_card_Displacement      = str(self.Displacement)
        self.str_card_Tax_status        = str(self.Tax_status)
        self.str_card_Insurance_status  = str(self.Insurance_status)
        self.card_birth                 = arcade.draw_text(self.str_card_birth           , 100, 700, arcade.color.BLACK, 10)
        self.card_IDVehicle             = arcade.draw_text(self.str_card_IDVehicle       , 1000, 1045, arcade.color.BLACK, 10)
        self.card_pilot_sex             = arcade.draw_text(self.str_card_pilot_sex       , 1000, 1020, arcade.color.BLACK, 10)
        self.card_true_age              = arcade.draw_text(self.str_card_true_age        , 1000, 1005, arcade.color.BLACK, 10)
        self.card_pilot_name            = arcade.draw_text(self.str_card_pilot_name      , 1000, 990 , arcade.color.BLACK, 10)
        self.card_pilot_surname         = arcade.draw_text(self.str_card_pilot_surname   , 1000, 975 , arcade.color.BLACK, 10)
        self.card_plate                 = arcade.draw_text(self.str_card_plate           , 1000, 960 , arcade.color.BLACK, 10)
        self.card_region                = arcade.draw_text(self.str_card_region          , 1000, 945 , arcade.color.BLACK, 10)
        self.card_car_model             = arcade.draw_text(self.str_card_car_model       , 1000, 930 , arcade.color.BLACK, 10)
        self.card_Displacement          = arcade.draw_text(self.str_card_Displacement    , 1000, 915 , arcade.color.BLACK, 10)
        self.card_Tax_status            = arcade.draw_text(self.str_card_Tax_status      , 1000, 900 , arcade.color.BLACK, 10)
        self.card_Insurance_status      = arcade.draw_text(self.str_card_Insurance_status, 1000, 885 , arcade.color.BLACK, 10)