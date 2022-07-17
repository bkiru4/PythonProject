class ParkingLot:
    def __init__(self, largeSpots, regularSpots, compactSpots, motorcycleSpots):
        self.largeSpots = self.largeSpotsLeft = largeSpots
        self.regularSpots = self.regularSpotsLeft = regularSpots
        self.compactSpots = self.compactSpotsLeft = compactSpots
        self.motorcycleSpots = self.motorcycleSpotsLeft = motorcycleSpots
        self.spotList = []
        self.vehicle_count = self.motorcycle_count = self.car_count = self.van_count = 0

    def spacesLeft(self):
        #print parking spaces left
        print("Total number of parking spaces left: "+str(self.largeSpotsLeft + self.regularSpotsLeft+self.compactSpotsLeft+self.motorcycleSpotsLeft))
        print("  Remaining Motorcycle Spaces: "+str(self.motorcycleSpotsLeft))
        print("  Remaining Compact Spaces: "+str(self.compactSpotsLeft))
        print("  Remaining Regular Spaces: "+str(self.regularSpotsLeft))
        print("  Remaining Large Spaces: "+str(self.largeSpotsLeft))
    def spacesTotal(self):
        '''print total # of parking spaces in parking garage'''
        print("This parking garage has a total of {} parking spots\nMotorcycle: {}\nCompact: {}\nRegular: {}\nLarge: {}".format(self.motorcycleSpots+self.compactSpots+self.regularSpots+self.largeSpots,self.motorcycleSpots,self.compactSpots,self.regularSpots,self.largeSpots))
        pass
    def lotEmpty(self):
        #print if parking lot is empty
        pass
    def lotFull(self):
        #print if parking lot is full
        pass
    def addVehicle(self, vehicle, spotType):
        '''Vehicle : ('motorcycle' / 'car' / 'van')
        Spot Type : ('motorcycle' / 'compact' / 'regular' / 'large')
        '''
        if(self.checkVehicleInput(vehicle)==True and self.checkSpotTypeInput(spotType)==True):
            self.spotList.append([vehicle,spotType])
            self.vehicle_count+=1
            exec("self."+vehicle.lower()+"_count+=1")
            exec("self."+spotType.lower()+"SpotsLeft-=1")
            print("Added {} into {} parking spot".format(vehicle,spotType))
    def seeSpotList(self):
        print(self.spotList)
    def checkVehicleInput(self, vehicle):
        if(vehicle.lower() not in ['motorcycle','car','van']):
            print("Not a valid vehicle")
            return False
        else:
            return True
    def checkSpotTypeInput(self, spotType):
        if(spotType.lower() not in ['motorcycle','compact','regular','large']):
            print("Not a valid parking spot")            
            return False
        else:
            return True
    def checkParkingSpace(self,vehicle,spaceType):
        #if (vehicle)
        pass
#---------------------------------------------------------------------------
vehicles = ['motorcycle','car','van']
parkingSpots = ['motorcycle', 'compact','regular','large']
parkinglotA = ParkingLot(100,100,100,1)
parkinglotA.spacesTotal()
print()
parkinglotA.addVehicle(vehicles[1],parkingSpots[1])
parkinglotA.addVehicle("motorcycle","motorcycle")
#print(parkinglotA.vehicle_count)
#print(parkinglotA.motorcycle_count)
print()
parkinglotA.spacesLeft()
print()
print(parkinglotA.spotList)

# parking lot is full -> specific type (motorcycle)
# total number -> specific types(vans)

# types -> motorcycle / car / vans
# park types -> motorcycle / compact / regular / large
