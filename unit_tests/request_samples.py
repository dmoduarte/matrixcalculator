
requestSampleA = [
        {
            "1": {"1": 1, "2": 3},
            "2": {"1": 3, "2": 4}
        },

        {"op": "ADD"},

        {
            "1": {"1": 2, "2": 3},
            "2": {"1": 4, "2": 4}
        },

        {"op": "ADD"},

        {
            "1": {"1": 1, "2": 0, "3": -3},
            "2": {"1": -2, "2": 4, "3": 1}
        },

        {"op": "MULT"},

        {
            "1": {"1": 1, "2": 0, "3": 4, "4": 1},
            "2": {"1": -2, "2": 3, "3": -1, "4": 5},
            "3": {"1": 0, "2": -1, "3": 2, "4": 1}
        }
    ]

requestSampleB = [
    {
        "1": {"1": 1, "2": 2},
        "2": {"1": 2, "2": 1} 
    },

    {"op": "ADD"},

    {
        "1": {"1": 2, "2": 2},
        "2": {"1": 3, "2": 2} 
    },

    {"op": "MULT"},

    {
        "1": {"1": 4, "2": 5},
        "2": {"1": 6, "2": 1} 
    },

    {"op": "MULT"},

    {
        "1": {"1": 3, "2": 1},
        "2": {"1": 4, "2": 1} 
    }
 ]

requestSampleC = [
    {
        "1": {"1": 1}
    },

    {"op": "ADD"},

    {
        "1": {"1": 2}
    },

    {"op": "ADD"},

    {
        "1": {"1": 3}
    },

    {"op": "ADD"},

    {
        "1": {"1": 4}
    }
 ]