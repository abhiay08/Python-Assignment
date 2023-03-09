# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:41:03 2023

@author: HP
"""
# Assignment 5 que 2
class BikeOnRent:
    def __init__(self):
        self.inventory={}

    def add_bike(self,bike_id):
        self.inventory[bike_id]="available"

    def remove_bike(self,bike_id):
        if bike_id in self.inventory:
            del self.inventory[bike_id]

    def display_inventory(self):
        return self.inventory

    def rent_bike(self,bike_id,rental_period):
        if bike_id in self.inventory:
            if self.inventory[bike_id]=="available":
                if rental_period=="hourly":
                    self.inventory[bike_id]="rented_hourly"
                    return 5
                elif rental_period=="daily":
                    self.inventory[bike_id]="rented_daily"
                    return 20
                elif rental_period=="weekly":
                    self.inventory[bike_id]="rented_weekly"
                    return 60
                else:
                    return "invalid rental period"
            else:
                return "bike not available"
        else:
            return "bike not found"

    def return_bike(self,bike_id):
        if bike_id in self.inventory:
            rental_period=self.inventory[bike_id]
            if rental_period=="rented_hourly":
                self.inventory[bike_id]="available"
                return "Amount to be paid:$5 for hourly rental"
            elif rental_period=="rented_daily":
                self.inventory[bike_id]="available"
                return "Amount to be paid:$20 for daily rental"
            elif rental_period=="rented_weekly":
                self.inventory[bike_id]="available"
                return "amount to be paid:$60 for weekl rental"
            else:
                return "invalid bike id"
        else:
            return "bike not found"


shop=BikeOnRent()
shop.add_bike(1)
shop.add_bike(2)
shop.add_bike(3)
shop.rent_bike(1,"hourly")
shop.rent_bike(2,"daily")
shop.rent_bike(3,"weekly")
a=shop.return_bike(2)
print(a)