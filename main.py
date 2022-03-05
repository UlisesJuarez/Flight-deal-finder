from data_manager import DataManager

data_manager=DataManager()
sheety_data=data_manager.get_destination_data()


if sheety_data[0]["iataCode"]=="":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheety_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheety_data)

    data_manager.destination_data=sheety_data
    data_manager.update_destination_codes()
