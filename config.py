NEWS_API_KEY = "d8dfdf72-735b-4f98-916c-1816d0a85899"

ETHICS_KEYWORDS = {
    "labor": [
        "child labor", "workers", "union", "wages",
        "exploitation", "strike", "labor abuse", "scandal", "controversy", "forced labor"
    ],
    "environment": [
        "pollution", "emissions", "deforestation",
        "water usage", "climate", "environmental violation"
    ], 
    "animal": [
        "animal cruelty", "factory farming",
        "animal welfare", "slaughter"
    ]
}

SEVERITY_WEIGHTS = {
    "child labor": -5,
    "forced labor": -5,
    "exploitation": -5,
    "pollution": -3,
    "deforestation": -4,
    "lawsuit": -2,
    "fine": -2,
    "sustainability": +2,
    "renewable": +2,
    "scandal": -2,
    "controversy": -2

}
