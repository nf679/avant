from pymongo import MongoClient
from gauss_class import Gauss
import pandas as pd


def _connect_mongo():
    """
    ***NOT USABLE YET CAUSE I DON'T WANNA PUT THE USERNAME AND PASSWORD ON GITHUB***
    Connects the user to the database on the Atlas cluster.
    """
    mongo_uri = "mongodb+srv://USERNAME:PASSWORD@cluster1.vxinb.mongodb.net/refl_database"
    conn = MongoClient(mongo_uri)
    return conn


def findGauss(name, parameter):
    """
    Opens the database to extract the data, inserts it into Gauss class and returns a Gauss prior object.
    Input:      name of molecule, parameter to find
    Output:    Gauss prior object containing pdf, logpdf, cdf, ppf and rvs methods
    """
    # connect to the database
    client = MongoClient()
    db = client.refl_database
    # query the database
    cursor = db.Gaussian.find({'name':name, 'parameter': parameter},{"_id":0, "loc":1,"scale":1,"xrange":1})
    # return the query as a pandas DataFrame so the data can be extracted
    data = pd.DataFrame(list(cursor))
    # convert the DataFrame to a numpy array so it's in the right format for Gauss class
    data_arr = data.to_numpy(dtype=float)

    # get the values for the lower and upper bound of the distribution
    bounds = findUniform(name,parameter)
    lb = bounds[0]
    ub = bounds[1]

    # insert the data into Gauss class to get the prior probability object
    prior_object = Gauss(data_arr,lb,ub)

    return prior_object


def findUniform(name, parameter):
    """
    Opens the database to extract the data and returns an array of bounds for the uniform prior probability.
    Input:      name of molecule, parameter of interest
    Output:     array of length [2] with the upper and lower bounds for the uniform prior
    """
    # connect to the database
    client = MongoClient()
    db = client.refl_database
    # extract the data into a pandas DataFrame object
    cursor = db.uniform.find({'name':name,'parameter':parameter},{"_id":0, "name":0,"parameter":0})
    data = pd.DataFrame(list(cursor))
    # extract the lower and upper bounds as floats
    lb = data.iat[0,0]
    lb = float(lb)
    ub = data.iat[0,1]
    ub = float(ub)

    return [lb,ub]


