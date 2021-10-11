import numpy as np


class LogarithmTransform:
    def __init__(self, _dataset):
        self.dataset = _dataset

    def execute(self):
        return np.log10(self.dataset)


if __name__ == "__main__":
    help_text = """Data Transformation using Logarithm-Transform Algorithm
    
    """
    print(help_text)
    dataset = np.asarray(input("!Enter comma-seperated-values. Example [1.0,2.0,4.1,5,5] ").split(","), dtype=np.float32)
    lt_obj = LogarithmTransform(_dataset=dataset)
    np_log_list = lt_obj.execute()
    print(f"""> Logarithm-Transform:
{np_log_list}""")

