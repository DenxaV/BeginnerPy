def beaufort_number(wind_desc):
    try:
        wind_desc = wind_desc.lower()
        descriptors = {
            "calm": 0,
            "light air": 1,
            "light breeze": 2,
            "gentle breeze": 3,
            "moderate breeze": 4,
            "fresh breeze": 5,
            "strong breeze": 6,
            "near gale": 7,
            "gale": 8,
            "strong gale": 9,
            "storm": 10,
            "hurricane force": 11
        }
        if wind_desc in descriptors:
            return descriptors[wind_desc]
        else:
            available_descriptors = ", ".join(descriptors.keys())
            return f"Invalid descriptor '{wind_desc}'. Available descriptors are: {available_descriptors}"
    except KeyboardInterrupt:
        return "Program interrupted by user"    
descriptor = input("Enter wind descriptor: ")
print(beaufort_number(descriptor))