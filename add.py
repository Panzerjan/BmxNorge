from bmx.comi import CommissionerManager

def main():
    # Create a CommissionerManager instance
    manager = CommissionerManager("commissær.json")

    # Details of the new commissioner
    new_commissioner = {
        "name": "New Commissioner",
        "type": "Local",
        "club": "Some BMX Club",
        "status": True
    }

    # Add the new commissioner
    manager.add_commissioner(new_commissioner)

if __name__ == "__main__":
    main()
