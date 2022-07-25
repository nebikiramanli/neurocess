from pyparsing import col
import read_file
import json
import os 
import visualization
import pandas as pd


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def manipulate_data(pickle_data, names_json):
    """
    Manipulates the dataframe and returns a new dataframe
    """

    pickle_data = pickle_data.astype({'task': 'str'})
        
    for key, name in names_json.items():
        after_task = "1.0"

        for index in range(pickle_data.shape[0] - 1):
            
            if pickle_data["task"][index] == "1.0" and after_task == "1.0":
                pickle_data.at[index, "task"] = name

                if (pickle_data.shape[0] - 1) > index:
                    after_task = pickle_data["task"][index + 1] 
                
                if after_task == "0.0":
                    break
    
    return pickle_data



def main():
    pickle_data = read_file.read_pickle_file(os.path.join(PROJECT_DIR, 'data/data.pkl'))
    names_json = read_file.read_json_file(os.path.join(PROJECT_DIR, 'data/names.json'))
    manipule_data = manipulate_data(pickle_data, names_json)
    grouped_data = manipule_data["task"].value_counts()
    del grouped_data["0.0"]
    
    data = pd.DataFrame({'Name': grouped_data.index, 'Count': grouped_data.values})
    figure = visualization.get_bar_plot(data, "Name", "Count", "Task Count", fig_size=(10,6), x_rotation=90)
    visualization.save_figure(figure, os.path.join(PROJECT_DIR, 'figure'), "task_count.png")

if __name__ == "__main__":
    main()


        
            

        



            


            

