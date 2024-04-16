"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["vehicle", "vheclie"],
            "answer": 1.2,
        },
        {
            "input": ["checkpoint", "cehkipont"],
            "answer": -1,
        },
        {
            "input": ["doctor", "doctor"],
            "answer": 0,
        },
        {
            "input": ["research", "rsceearh"],
            "answer": 1.67,
        },
    ],
    "Extra": [
        {
            "input": ["headquarters", "haduqertares"],
            "answer": 1.4,
        },
        {
            "input": ["manslaughter", "magltheuansr"],
            "answer": 3.6,
        },
        {
            "input": ["hospital", "hatospil"],
            "answer": 2.67,
        },
        {
            "input": ["squeezed", "seezuedq"],
            "answer": -1,
        },
        {
            "input": ["admitted", "aimttded"],
            "answer": 1.33,
        },
        {
            "input": ["pensioners", "pneosenirs"],
            "answer": 1.25,
        },
        {
            "input": ["blunder", "blendur"],
            "answer": 1.2,
        },
        {
            "input": ["teenager", "tageener"],
            "answer": 2,
        },
    ]
}
