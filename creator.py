class Creator:
    """
    Basically Creators has two default features health, alived.
    As input these features can be vary.
    """
    def __init__ (self, name):
        self.name = name
        self.features = []
        health = 100.
        alived = True
        self.features.append(["alived", alived])
        self.features.append(["health", health])
        
    def get_name (self):
        return self.name  
    
    def add_features (self, features): # Adding new features at once to an object
        for feature in features: # Also features list should be a nested list that include ["feature_name", value]
            self.features.append(feature)
    
    def print_features (self): # To DeBUG ; Write down each feature and its value
        print("-----------------------------------------------------")
        print(f"\"{self.name}\" has the following featurs:")
        for feature_name, value in self.features:
            print(f"\"{feature_name}\" feature has value of {value}")
        print("-----------------------------------------------------")
        
    def find_feature_index (self, feature_name): # Gets feature_name and return by its index
        for i in range(len(self.features)):
            if(self.features[i][0] == feature_name):
                return i
        # If it isnt founded returns as -1
        return -1
    
    def change_feature (self, feature_name, value): # Change spesific feature 
        index = self.find_feature_index(feature_name)
        if index != -1:
            self.features[index][1] = value