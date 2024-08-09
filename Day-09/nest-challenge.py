# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
#     "Puerto Rico": {
#         "cities_visited": [
#             "Bayamon",
#             "Mayaguez",
#             "San Juan",
#             "Maricao",
#             "Las Marias",
#             "Ponce",
#             "Fajardo",
#         ]
#     },
# }

# Nesting a Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
]

print(travel_log)
