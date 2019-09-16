{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for, request\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\n\n\napp = Flask(__name__)\n\napp.config[\"MONGO_DBNAME\"] = 'My_Cocktails'\napp.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')\n\n\n@app.route('/')\n    def get_drinks():\n    return ('base.html')","undoManager":{"mark":60,"position":62,"stack":[[{"start":{"row":0,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for, request","from flask_pymongo import PyMongo","from bson.objectid import ObjectId",""],"id":1}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["a"],"id":3},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["p"]},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["p"]}],[{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":[" "],"id":4},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["="]}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":[" "],"id":5}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["F"],"id":6},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["l"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["a"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["s"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["k"]}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":13},"action":"insert","lines":["()"],"id":7}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["_"],"id":8},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["_"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["_"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["n"],"id":9},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["a"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["m"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":21},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":10}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":43},"action":"insert","lines":["app.config[\"MONGO_DBNAME\"] = 'task_manager'"],"id":13}],[{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"remove","lines":["r"],"id":14},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"remove","lines":["e"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"remove","lines":["g"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"remove","lines":["a"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"remove","lines":["n"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"remove","lines":["a"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"remove","lines":["m"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"remove","lines":["_"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"remove","lines":["k"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"remove","lines":["s"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"remove","lines":["a"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"remove","lines":["t"]}],[{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["M"],"id":15},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["y"]},{"start":{"row":9,"column":32},"end":{"row":9,"column":33},"action":"insert","lines":["_"]},{"start":{"row":9,"column":33},"end":{"row":9,"column":34},"action":"insert","lines":["C"]},{"start":{"row":9,"column":34},"end":{"row":9,"column":35},"action":"insert","lines":["o"]},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["c"]},{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["k"]},{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["t"]},{"start":{"row":9,"column":38},"end":{"row":9,"column":39},"action":"insert","lines":["a"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["i"]}],[{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"insert","lines":["l"],"id":16},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"insert","lines":["s"]}],[{"start":{"row":9,"column":43},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":71},"action":"insert","lines":["app.config[\"MONGO_URI\"] = os.getenv('MONGO_URI', 'mongodb://localhost')"],"id":18}],[{"start":{"row":10,"column":71},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["@"]},{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":["a"]},{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"insert","lines":["p"],"id":21},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["."]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["r"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["o"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["u"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["t"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":12},"action":"insert","lines":["()"],"id":22}],[{"start":{"row":13,"column":11},"end":{"row":13,"column":13},"action":"insert","lines":["''"],"id":23}],[{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["/"],"id":24}],[{"start":{"row":13,"column":15},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":26}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":27}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "],"id":28}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["d"],"id":29},{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["e"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":[" "],"id":30},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["g"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["e"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["t"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":[")"]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":[")"],"id":31}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["_"],"id":32},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["r"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["e"],"id":33},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["r"]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["c"],"id":34},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["o"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["c"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["k"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["t"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["a"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["i"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["s"],"id":35}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["l"],"id":36},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["s"]}],[{"start":{"row":14,"column":21},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["r"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["e"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["t"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["u"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["r"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":[":"],"id":38}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":[" "],"id":39},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["r"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["e"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["n"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["d"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["e"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["r"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":17},"action":"remove","lines":["render"],"id":40},{"start":{"row":15,"column":11},"end":{"row":15,"column":26},"action":"insert","lines":["render_template"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":28},"action":"insert","lines":["()"],"id":41}],[{"start":{"row":15,"column":27},"end":{"row":15,"column":28},"action":"remove","lines":[")"],"id":42},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["("]},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["e"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["t"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["a"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["l"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"remove","lines":["p"]},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"remove","lines":["m"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"remove","lines":["e"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"remove","lines":["t"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["_"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"remove","lines":["r"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"remove","lines":["e"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"remove","lines":["d"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["n"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["e"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"remove","lines":["r"],"id":43}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["M"],"id":44},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["y"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":13},"action":"remove","lines":["My"],"id":45},{"start":{"row":15,"column":11},"end":{"row":15,"column":23},"action":"insert","lines":["My_Cocktails"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"remove","lines":[":"],"id":46}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":23},"action":"insert","lines":["()"],"id":47}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":25},"action":"insert","lines":["\"\""],"id":48}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":25},"action":"remove","lines":["\"\""],"id":49}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":[":"],"id":50}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":23},"action":"remove","lines":["My_Cocktails"],"id":51},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["b"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["a"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["s"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["e"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["."]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["h"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["t"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["m"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["l"]}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["\""],"id":52}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["\""],"id":53}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["("],"id":54}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["_"],"id":55}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"remove","lines":["_"],"id":56}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":[")"],"id":57}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"remove","lines":["\""],"id":58}],[{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["'"],"id":59}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["\""],"id":60}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["'"],"id":61}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["s"],"id":62},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["l"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["i"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":["a"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["t"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["k"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["c"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["o"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["c"]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["d"],"id":63},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["r"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["i"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["n"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["k"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["s"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":15},"end":{"row":13,"column":15},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568641312848}