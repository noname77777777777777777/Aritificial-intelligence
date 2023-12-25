def get_data(file_path):
    graph = []
    with open(file_path,"r",encoding="UTF8") as f:
         for line in f:
            row = line.rstrip().split("\t")
            graph.append(row)
    return graph




