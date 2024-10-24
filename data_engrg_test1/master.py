import os
import time
import threading

def read_sql_files(directory):
    sql_files = {}
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".sql"):
                filepath = os.path.join(foldername, filename)
                with open(filepath, 'r') as file:
                    sql_files[filename] = {
                        'content': file.read(),
                        'folder': foldername
                    }
    return sql_files

def find_dependencies(sql_files):
    dependencies = {}
    for filename, info in sql_files.items():
        content = info['content']
        dependencies[filename] = []
        for other_file in sql_files.keys():
            if other_file != filename and other_file.split('.')[0] in content:
                dependencies[filename].append(other_file)
    return dependencies

def topological_sort(dependencies):
    visited = set()
    order = []
    
    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in dependencies[node]:
                visit(neighbor)
            order.append(node)
    
    for node in dependencies:
        visit(node)
    
    return order[::-1] 

def run_sql_file(sql_file, sql_files):
    folder = sql_files[sql_file]['folder'] 
    print(f"Running {sql_file} from folder '{folder}'...")
    time.sleep(2)
    print(f"Finished {sql_file} from folder '{folder}'.")

def run_sql_files_in_order(sql_order, sql_files):
    for sql_file in sql_order:
        run_sql_file(sql_file, sql_files)

def run_sql_file_in_parallel(sql_file, sql_files, dependencies, lock, completed):
    with lock:
        while not all(dep in completed for dep in dependencies[sql_file]):
            lock.release()
            time.sleep(1)
            lock.acquire()

        folder = sql_files[sql_file]['folder']
        print(f"Running {sql_file} from folder '{folder}'...")
        time.sleep(2)
        print(f"Finished {sql_file} from folder '{folder}'.")

        completed.append(sql_file)

def run_sql_files_in_parallel(sql_order, sql_files, dependencies):
    lock = threading.Lock()
    completed = []
    threads = []

    for sql_file in sql_order:
        thread = threading.Thread(target=run_sql_file_in_parallel, args=(sql_file, sql_files, dependencies, lock, completed))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":

    sql_folder = "data_engrg_test1/sql"  
    
    sql_files = read_sql_files(sql_folder)
    
    dependencies = find_dependencies(sql_files)
    
    print("Dependencies between SQL files:")
    for file, deps in dependencies.items():
        print(f"{file} depends on: {', '.join(deps) if deps else 'None'}")
    
    sql_order = topological_sort(dependencies)
    
    print("\nExecuting SQL files in the following order (Sequential Execution):")
    run_sql_files_in_order(sql_order, sql_files)
    
    print("\nExecuting SQL files in parallel (Parallel Execution):")
    run_sql_files_in_parallel(sql_order, sql_files, dependencies)
