import plotly.figure_factory as ff;
import plotly.graph_objects as go;
import pandas as pd;
import csv;
import random;
import statistics;


data_file = pd.read_csv('data_2.csv');
data = data_file['temp'].tolist();


def random_set_of_mean(counter):
    data_set = [];
    for i in range(0, counter):
        index = random.randint(0, len(data ) - 1);
        value = data[index];
        data_set.append(value);

    sampling_mean = statistics.mean(data_set);
    return sampling_mean;

def show_graph(mean_list):
    df = mean_list;
    mean= statistics.mean(df);
    graph = ff.create_distplot([df],['average'],show_hist= False);
    graph.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode = 'lines', name= 'mean'))
    graph.show();

def setup():
    mean_list = [];
    for i in range(0, 1000):
        set_means = random_set_of_mean(100);
        mean_list.append(set_means);
    show_graph(mean_list); 

def st_Dev():
    mean_list = [];
    for i in range(0, 1000):
        set_means = random_set_of_mean(100);
        mean_list.append(set_means);
    print(statistics.stdev(mean_list)); 




setup();    
st_Dev();


# data_set = [];

# # for i in range(0, 10):
# #     index = random.randint(0, len(data));
# #     value = data[index];
# #     data_set.append(value);


# population_mean = statistics.mean(data_set);
# population_stdev = statistics.stdev(data_set);



# print(population_mean, population_stdev);
# # graph = ff.create_distplot([data],['average'],show_hist= False);
# # graph.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0,1], mode = 'lines', name= 'mean'))
# # graph.show();

