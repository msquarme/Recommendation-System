from math import sqrt
import yaml
UserRating={
    'Musie Meressa': {'Toy Story': 3.0, 'Jumanji' : 3.5, 'Grumpier Old Men' : 4.0 , 'Waiting to Exhale' : 3.0, 'Father of the Bride Part II': 4.5,  'Heat': 2.5, 'Sabrina': 4.0, 
						'Tom and Huck': 3.5, 'Sudden Death': 2.5, 'GoldenEye': 3.5, 'American President, The' :1.5, 'Dracula: Dead and Loving It' : 2.0, 'Balto' :4.0 ,'Nixon' : 5.0, 
						'Cutthroat Island' : 2.0, 'Casino' : 4.5, 'Sense and Sensibility' : 3.0, 'Four Rooms' : 1.5,'Ace Ventura: When Nature Calls':  4.0, 'Money Train' :  1.5, 
						'Get Shorty': 2.5
						},
    'Almaz Abrha': { 'Toy Story': 1.0,'Grumpier Old Men' : 2.0 , 'Waiting to Exhale' : 3.0, 'Father of the Bride Part II': 4.5,  'Heat': 2.5, 'Sabrina': 1.0, 'Tom and Huck': 3.5,
					'GoldenEye': 2.5, 'American President, The': 4.5, 
					'Dracula: Dead and Loving It' : 2.0, 'Balto' :3.0 ,'Nixon' : 2.0, 'Cutthroat Island' : 2.0, 'Casino' : 4.5, 'Sense and Sensibility' : 2.0, 'Get Shorty': 4.5
					},
    'Luel Michael': {'Toy Story': 4.0, 'Jumanji' : 1.5, 'Grumpier Old Men' : 2.0 , 'Waiting to Exhale' : 5.0, 'Father of the Bride Part II': 4.5,  'Heat': 2.5, 'Sabrina': 2.0, 
						'Tom and Huck': 4.5, 'Sudden Death': 2.5, 'GoldenEye': 1.5, 'American President, The' :4.5, 'Dracula: Dead and Loving It' : 4.0
					},
    'Abraha Tesfay': {'Heat': 2.5, 'Sabrina': 4.0,'Tom and Huck': 3.5, 'Sudden Death': 2.5, 'GoldenEye': 3.5, 'American President, The': 3.5, 'Dracula: Dead and Loving It' : 2.0, 'Balto' :1.0 ,'Nixon' : 1.0, 
						'Cutthroat Island' : 3.0, 'Casino' : 2.5, 'Sense and Sensibility' : 3.0, 'Four Rooms' : 4.5,'Ace Ventura: When Nature Calls':  2.0, 'Money Train' :  4.5, 
						'Get Shorty': 4.5
					},
    'Nigus Zinabu': { 'Toy Story': 1.0, 'Jumanji' : 3.5, 'Grumpier Old Men' : 2.0 , 'Waiting to Exhale' : 3.0, 'Father of the Bride Part II': 4.5,  'Heat': 2.5, 'Sabrina': 4.0, 
						'Tom and Huck': 2.5, 'Sudden Death': 2.5, 'GoldenEye': 4.5, 'American President, The' :1.5, 'Dracula: Dead and Loving It' : 2.0, 'Balto' :2.0 ,'Nixon' : 2.0, 
						'Cutthroat Island' : 2.0, 'Casino' : 4.5, 'Sense and Sensibility' : 4.0, 'Four Rooms' : 3.5,'Ace Ventura: When Nature Calls':  2.5, 'Money Train' :  4.0, 
						'Get Shorty': 1.5
					},
    'Tesfay Abaraha': { 'Heat': 2.5, 'Sabrina': 2.0,'Tom and Huck': 4.5, 'Sudden Death': 2.5, 'GoldenEye': 1.0, 'American President, The': 2.0, 'Dracula: Dead and Loving It' : 2.0, 'Balto' :4.0 ,'Nixon' : 5.0, 
						'Cutthroat Island' : 3.0, 'Casino' : 2.5, 'Sense and Sensibility' : 3.0, 'Four Rooms' : 4.5,'Ace Ventura: When Nature Calls':  4.0, 'Money Train' :  1.5, 
						'Get Shorty': 4.5
    
					},
    'Haddis Alemu': {'Heat': 2.5, 'Sabrina': 1.0,'Tom and Huck': 2.5, 'Sudden Death': 3.5, 'GoldenEye': 4.0},
    'Tsige Haile': {'Father of the Bride Part II': 1.5,  'Heat': 1.0, 'Sabrina': 5.0, 'Tom and Huck': 2.5, 'Sudden Death': 2.5, 'GoldenEye': 1.5, 
					'American President, The': 5.0, 'Dracula: Dead and Loving It' : 1.5, 'Balto' :1.0 
					},
    'Selam Abay': {'Four Rooms' : 3.5,'Ace Ventura: When Nature Calls':  1.0, 'Money Train' :  4.5, 'Get Shorty': 1.5},
    'Shewit Tesfu': {'Tom and Huck': 1.5, 'Sudden Death': 4.5, 'GoldenEye': 4.0, 'American President, The': 2.5, 'Dracula: Dead and Loving It' : 5.0, 'Balto' :1.0 ,'Nixon' : 2.5}
    }
    
    
    

MovieRating = {}

def organize(): 
    for person in UserRating:
        for film in UserRating[person]:
            if film not in MovieRating:
                MovieRating[film]={}
            MovieRating[film][person]=UserRating[person][film]

def cos_similarity(people,movie1,movie2):
    si={}
    for item in people[movie1]:
        if item in people[movie2]:
            si[item]=1
    if len(si)==0:
        return 0
    sum1=0
    sum21=0
    sum22=0
    for item in si:
        sum1+=(people[movie1][item]*people[movie2][item])
        sum21+=pow(people[movie1][item],2)
        sum22+=pow(people[movie2][item],2)
    if sum21==0 or sum22==0:
        return 0

    return round(sum1/(sqrt(sum21)*sqrt(sum22)),2)



if __name__ == "__main__":
    organize()
    threshold=0.98
    movies_watched=["Sudden Death","Sense and Sensibility","Get Shorty", "Casino" , "Cutthroat Island", "Waiting to Exhale", "Money Train"]
    print("----------------------------------------------------")
    for movie1 in movies_watched:
        print("|", "List of Recommended Movies for | ",movie1,"|")
        print("----------------------------------------------------")
        for movie2 in sorted(MovieRating.keys()):
            if movie1==movie2:
                continue
            if movie1 in movies_watched:
                result=cos_similarity(MovieRating, movie1, movie2)
                if result>=threshold:
                    print(movie2 +"\t",cos_similarity(MovieRating, movie1, movie2))
        print("----------------------------------------------------")

