from taipy.gui import Gui
import pathlib
import tempfile

import pandas as pd

PATH_TO_TABLE = str(pathlib.Path(tempfile.gettempdir()) / "table.csv")


data = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})
data.to_csv(PATH_TO_TABLE,',', index=False)

Gui('<|{data}|table|>\n<|{PATH_TO_TABLE}|file_download|name=table.csv|label=Download table|>').run()




