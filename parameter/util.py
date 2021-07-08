from pymongo import MongoClient
from gauss_class import Gauss
import pandas as pd


def _connect_mongo():
    #NOT USEABLE YET AS THE USERNAME AND PASSWORD AREN'T INSERTED
    mongo_uri = "mongodb+srv://USERNAME:PASSWORD@cluster1.vxinb.mongodb.net/refl_database"
    conn = MongoClient(mongo_uri)
    return conn


def findGauss(name, parameter):
    client = MongoClient()
    db = client.refl_database
    cursor = db.Gaussian.find({'name':name, 'parameter': parameter},{"_id":0, "loc":1,"scale":1,"xrange":1})
    data = pd.DataFrame(list(cursor))

    #use this to get a 2d numpy array
    data_arr = data.to_numpy(dtype=float)

    #use this to get the values for lb and ub
    bounds = findUniform(name,'v_h')
    lb = bounds[0]
    ub = bounds[1]

    #INSERT THE ARRAY OF LOCS AND SCALES AND THE LB AND UB INTO GAUSS CLASS
    prior_object = Gauss(data_arr,lb,ub)

    return prior_object


def findUniform(name, parameter):

    client = MongoClient()
    db = client.refl_database
    cursor = db.uniform.find({'name':name,'parameter':parameter},{"_id":0, "name":0,"parameter":0})
    data = pd.DataFrame(list(cursor))
    lb = data.iat[0,0]
    lb = float(lb)
    ub = data.iat[0,1]
    ub = float(ub)

    return [lb,ub]


