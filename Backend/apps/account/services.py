class UserServices():

    def standardize_phone_number(self, phone_number):
        """
        Before Saving into database or Querying from database, Phone Number have to be standardized
        """
        standardized_phone_number = phone_number.strip().replace(' ', '') # Removing space
        if standardized_phone_number[0] == "0": # Remove first character "0"
            standardized_phone_number = standardized_phone_number[1:]
        return standardized_phone_number
