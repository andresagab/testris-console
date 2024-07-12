class Figure:

    FIGURES = {
        'O': [
            # A position
            [
                ["🟩", "🟩"],
                ["🟩", "🟩"],
            ]
        ],
        'J': [
            # A position
            [
                ["🟩", "🔲", "🔲"],
                ["🟩", "🟩", "🟩"],
            ],
            # B position
            [
                ["🟩", "🟩",],
                ["🟩", "🔲",],
                ["🟩", "🔲",],
            ],
            # C position
            [
                ["🟩", "🟩", "🟩"],
                ["🔲", "🔲", "🟩"],
            ],
            # D position
            [
                ["🔲", "🟩",],
                ["🔲", "🟩",],
                ["🟩", "🟩",],
            ],
        ],
        'L': [
            # A position
            [
                ["🔲", "🔲", "🟩"],
                ["🟩", "🟩", "🟩"],
            ],
            # B position
            [
                ["🟩", "🔲",],
                ["🟩", "🔲",],
                ["🟩", "🟩",],
            ],
            # C position
            [
                ["🟩", "🟩", "🟩"],
                ["🟩", "🔲", "🔲"],
            ],
            # D position
            [
                ["🟩", "🟩",],
                ["🔲", "🟩",],
                ["🔲", "🟩",],
            ],
        ],
        'S': [
            # A position
            [
                ["🔲", "🟩", "🟩"]
                ["🟩", "🟩", "🔲"]
            ]
            # B position
            [
                ["🟩", "🔲"]
                ["🟩", "🟩"]
                ["🔲", "🟩"]
            ]
        ],
        'Z': [
            # A position
            [
                ["🟩", "🟩", "🔲"]
                ["🔲", "🟩", "🟩"]
            ]
            # B position
            [
                ["🔲", "🟩"]
                ["🟩", "🟩"]
                ["🟩", "🔲"]
            ]
        ],
        'T': [
            # A position
            [
                ["🔲", "🟩", "🔲"]
                ["🟩", "🟩", "🟩"]
            ]
            # B position
            [
                ["🟩", "🔲"]
                ["🟩", "🟩"]
                ["🟩", "🔲"]
            ]
            # C position
            [
                ["🟩", "🟩", "🟩"]
                ["🔲", "🟩", "🔲"]
            ]
            # D position
            [
                ["🔲", "🟩"]
                ["🟩", "🟩"]
                ["🔲", "🟩"]
            ]
        ],
        'I': [
            # A position
            [
                ["🟩"],
                ["🟩"],
                ["🟩"],
                ["🟩"],
            ]
            # B position
            [
                ["🟩", "🟩", "🟩", "🟩"],
            ]
        ],
    }

    # The figure
    figure:str = "O"

    # The figure position
    position:str = "A"

    def __init__(self, figure:str, position:str) -> None:
        self.figure = figure
        self.position = position

    def get_figure(self) -> dict:
        return self.FIGURES[self.figure]

    def rotate(self, rotation:int) -> None:
        positions = self.get_figure()

        if len(positions) > 1:
            
