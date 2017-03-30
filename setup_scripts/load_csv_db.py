from src.src.models.Entity.Entity import Entity


def main():
    with open("coachella_artist.csv", encoding="latin-1") as coachella_file:
        for line in coachella_file:
            line_information = line.split(",")
            print(line_information)
            Entity(name=line_information[0], type='musician', twitter_uhandle=line_information[5],
                   twitter_uid=line_information[6], soundcloud_uname=line_information[4],
                   soundcloud_uid=line_information[3], spotify_uid=line_information[2], active=True).save()


if __name__ == "__main__":
    main()
