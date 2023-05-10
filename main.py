from files.comi import CommissionerManager


def main():
    path = "./files/comi.json"

    try:
        manager = CommissionerManager(path)

        new_commissioner = {
            "name": "Endre Boe",
            "type": "Local",
            "club": "Sola Bmx",
            "status": True
        }

        manager.add_commissioner(new_commissioner)
    except Exception as e:
        print(e)
        raise e


if __name__ == "__main__":
    main()
