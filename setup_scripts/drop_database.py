from src.src.controllers.DatabaseController import DatabaseController


def main():
    DatabaseController.drop_tables()


if __name__ == "__main__":
    main()

# count = 0
# for i in TwitterProfile.select():
#     if count < 1:
#         count_real = 0
#         for var in dir(i):
#             if var in ["tracked", "owner", "lang", "profile_location", "profile_image_url_https",
#                        "profile_use_background_image", "contributors_enabled",
#                        "default_profile_image", "profile_text_color", "profile_banner_url", "has_extended_profile",
#                        "profile_background_color",
#                        "time_zone", "translator_type", "description", "url", "default_profile", "follow_request_sent",
#                        "status", "profile_background_image_url_https",
#                        "verified", "profile_image_url", "created_at", "profile_background_tile", "favourites_count",
#                        "profile_sidebar_fill_color"
#                        "statuses_count", "followers_count", "notifications", "location", "is_translator", "protected",
#                        "listed_count", "geo_enabled",
#                        "following", "friends_count", "is_translation_enabled", "profile_background_image_url",
#                        "utc_offset", "profile_sidebar_border_color"]:
#                 if count_real == 0:
#                     print("TwitterProfile(" + var + "=" + str(getattr(i, var)) + ", ")
#                 elif count_real == 38:
#                     print(var + "=" + str(getattr(i, var)) + ") \n")
#                 else:
#                     print(var + "=" + str(getattr(i, var)) + ", ")
#                 count_real += 1
#         count += 1
