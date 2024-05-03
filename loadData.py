import loadStates
import loadObesity
import loadPop
import loadSeriesId

# method to call all function needed to load data into data base
def loadAllData():
    loadStates.get_state_data()
    loadObesity.get_obesity_data()
    loadPop.get_pop_data()
    loadSeriesId.get_series_data()



