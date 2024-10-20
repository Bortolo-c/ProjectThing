import streamlit

path = "./mianpage.html"
with open(path,"r") as f:
    html_data = f.read()
streamlit.html(html_data)

recipe = streamlit.text_input("ENTER A RECIPE", value="", max_chars=None, type="default", label_visibility="visible")

button = streamlit.button("SUBMIT")

if button:
    def pleaseWorkIBegYou():
        safeToEat = True
        nonolist = ["zucchini", "spaghetti", "butter", "cheese", "pasta", "beef", "pork", "lamb", "soy", "wheat", "garlic", "bacon", "sausage", "pepperoni", "salami", "buns", "steak", "bread", "onion", "cauliflower", "broccoli", "curry", "flour", "milk", "cream", "yogurt", "custard", "cheddar", "mozzerella", "brie", "gouda"]
        for i in nonolist:
            if safeToEat == True:
                if i in recipe:
                    safeToEat = False
                    path = "./badrecipe.html"
                    with open(path,"r") as f:
                        html_data = f.read()
                    streamlit.html(html_data)
        if safeToEat == True:
            path = "./khronicKings.html"
            with open(path, "r") as f:
                html_data = f.read()
            streamlit.html(html_data)
    pleaseWorkIBegYou()