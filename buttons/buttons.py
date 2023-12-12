"""
This simple app demonstrates how cards can automatically advance to another
card after a certain amount of time. The auto_advance can either be a string
containing the name of the next card, or a function to call that returns the
name of the next card.
"""
from pypercard import App, Card


def auto_func(app, card):
    """
    Called while transitioning from card 2, to card 3.
    """
    count = app.datastore.setdefault("counter", 0)
    count += 1
    app.datastore["counter"] = count
    return "card3"


# The templates for these cards can be found in pypercard.html.
# cards = [
#     Card("card1"),
#     Card("card2", ),
#     Card("card3", 
#     Card("card4", transition="card5"),
#     Card("card5", transition="card6"),
#     Card("card6", transition="card7"),
#     Card("card7", transition="card8"),
#     Card("card8", transition="card9"),
#     Card("card9", transition="card10"),
#     Card("card10", transition="card11")
# ]


# Create the app while ensuring the counter is reset.
carousel_app = App(
    name="PyperCard carousel", datastore={"counter": 0}
)


@carousel_app.transition("morning", "click", "food")
def reset(app, card):
    return "boring_meal"

@carousel_app.transition("morning", "click", "full-course")
def reset(app, card):
    return "big_meal"

@carousel_app.transition("big_meal", "click", "sleep")
def next_card(app, card):
    return "stay_home"

@carousel_app.transition("boring_meal", "click", "stay")
def next_card(app, card):
    return "stay_home"

@carousel_app.transition("stay_home", "click", "reset")
def next_card(app, card):
    return "morning"

carousel_app.start("morning")

