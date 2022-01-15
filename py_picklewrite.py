import pickle

team={"groupA":["India", "NewZealand","England"],
    "groupB":["Aus","WI","SA"]}

fh = open("TeamList", "wb") # write + binary

pickle.dump(team,fh)

fh.close()