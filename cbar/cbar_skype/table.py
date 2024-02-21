""" Simple and small functions to be used in the project."""
import re
import pickle
from pathlib import Path
from datetime import datetime


def data_dir_path() -> str:
    """Path for the `data` directory which are going hosts all pickle files."""
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "data"
    return DATA_DIR


def check_data_dir() -> str:
    """Check data directory, if the directory doesn't exists create that."""
    data_dir = data_dir_path()
    if not data_dir.exists():
        print("Creating `data` directory.")
        data_dir.mkdir()

    return data_dir


def post_save(filename: str) -> bool:
    """Check pickle file if it saved or not, also check if `data` directory exsits."""
    data_dir = data_dir_path()


# using pickle to speed up :: expermental
def save_pickle(file_path, data):
    with open(file_path, "wb") as pickle_file:
        pickle.dump(data, pickle_file)


def read_pickle(file_path):
    with open(file_path, "rb") as pickle_file:
        data = pickle.load(pickle_file)
    return data


def readfile(filename: str) -> str:
    content = ""
    try:
        with open(filename, "r", encoding="utf-8") as text_file:
            content = text_file.read()
    except FileNotFoundError as err:
        print(f"{filename} doesn't exsist.", err)
    return content


def get_matches(text: str):
    """Return everything between ELEMENT-ID and Date like AGUEST 18, 2023."""
    pattern = r"(ELEMENT-ID\s+=\s+\d+)\s+[\w\s]*(\([\w\s]*\))\s+(.*?)\d+\s+(\w+\s+\d{1,2},\s\d{1,4})"
    return re.findall(pattern, text, re.DOTALL)


def extract_element_id(element_text):
    """Extract element id form text ELEMENT-ID = 3540001"""
    return element_text.split("=")[-1].strip()


def get_body_rows(body_data):
    return [row.strip() for row in body_data.split("\n") if row]


def create_header(header_text):
    return [item.strip() for item in header_text.split()]


def create_sub_header(sub_header_text):
    matches = re.findall(r"\w+\s\d?", sub_header_text, re.IGNORECASE)
    return [sub_header.strip() for sub_header in matches]


def create_body(body_rows):
    return [[float(item) for item in row.split()] for row in body_rows]


def create_cbar_table(data):
    element_text, title, body_data, date_text = data
    date = datetime.strptime(date_text, "%B %d, %Y")
    element_id = extract_element_id(element_text)
    header_text, sub_header_text, *body_rows = get_body_rows(body_data)
    header = create_header(header_text)
    sub_header = create_sub_header(sub_header_text)
    body = create_body(body_rows)
    el_type = "CBAR"
    # keys and values for the table dict
    keys = ("element_id", "header", "sub_header", "body", "date", "el_type")
    values = (element_id, header, sub_header, body, date,el_type)
    return dict(zip(keys, values))


def create_cbush_table(data):
    element_text, title, body_data, date_text = data
    date = datetime.strptime(date_text, "%B %d, %Y")
    element_id = extract_element_id(element_text)
    header_text, *body_rows = get_body_rows(body_data)
    el_type = "CBUSH"
    header = create_header(header_text)
    body = create_body(body_rows)
    # keys and values for the table dict
    keys = ("element_id", "header", "body", "date", "el_type")
    values = (element_id, header, body, date, el_type)
    return dict(zip(keys, values))    


        



# def get_cbush_tables(filename: str):
#     """Make a cbar table from a nastarn file that contains ELEMENT-IDs."""
#     text = readfile(filename)
#     tables = [create_cbush_table(element_match) for element_match in get_matches(text)]
#     # pickle stuff
#     data_path = data_dir_path()
#     file_path = data_path / filename
#     save_pickle(f"{file_path}.pickle", tables)
def create_table(data):
    element_text, title, body_data, date_text = data
    date = datetime.strptime(date_text, "%B %d, %Y")
    element_id = extract_element_id(element_text)
    if "( C B U S H )" in title:
        return create_cbush_table(data)
    elif "( C B A R )" in title:
        return create_cbar_table(data)
        
        
def get_tables(filename: str):
    """Make a cbar table from a nastarn file that contains ELEMENT-IDs."""
    text = readfile(filename)
     
    tables = [create_table(element_match) for element_match in get_matches(text)]

    # pickle stuff
    data_path = data_dir_path()
    file_path = data_path / filename
    save_pickle(f"{file_path}.pickle", tables)
    return tables




if __name__ == "__main__":

    f_path = "/nobackup/vol01/a420192/GSO/CNA_7139_MV2_Hood/cvm_bolt/it2/PPVT736_CNA_7139_it2_U_sol112t_012.f06"
    f_path2 = "/nobackup/vol01/a420192/GSO/CNA_7139_MV2_Hood/cvm_bolt/it2/test/xaa"
    f = open("/nobackup/vol01/a420192/GSO/CNA_7139_MV2_Hood/cvm_bolt/it12/test_it/exectime.txt", "a")
    # create all tables for the give Nastran file.
    # start_time = time.time()
    # #get_cbar_tables("/nobackup/vol01/a420192/GSO/CNA_7139_MV2_Hood/cvm_bolt/it12/test_it/PPVT736_CNA_7139_it12_U_sol112t_008.f06")
    # # run_with_threads("file.f06")
    # get_cbush_tables(f_path)
    # end_time = time.time()
    # exec_time = end_time - start_time
    # # exec_time = timeit.timeit(lambda: get_cbar_tables("fileaa"), number=1)
    # # save excuation time
    # print(exec_time, "seconds")
    # f.write(
    #     f"File size: 21M | Multi Thread(PC) | Execuation Time: {exec_time:.2f} Seconds\n"
    # )
    get_tables(f_path)
    
