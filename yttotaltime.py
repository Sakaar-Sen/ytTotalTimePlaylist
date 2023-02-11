from requests_html import HTMLSession
import datetime
import argparse

def convert_time_to_seconds(time_string):
    time_parts = [int(part) for part in time_string.split(":")]
    if len(time_parts) == 2:
        return time_parts[0] * 60 + time_parts[1]   
    else:
        return time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]

def divide_time_by_value(time_string, value):
    total_seconds = convert_time_to_seconds(time_string)
    divided_seconds = total_seconds / value
    hours = int(divided_seconds // 3600)
    minutes = int((divided_seconds % 3600) // 60)
    seconds = int(divided_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The complete youtube url of the playlist you want to scrap.")
    args = parser.parse_args()

    try:
        session = HTMLSession()
        url = args.url

        r = session.get(url)

        r.html.render(sleep=1, keep_page=True, scrolldown=1)

        videos = r.html.find("#text.ytd-thumbnail-overlay-time-status-renderer")

        totalvideos = []

        for item in videos:
            totalvideos.append(convert_time_to_seconds(item.text))

        totaltimess = 0

        for i in totalvideos:
            totaltimess += i

        totaltime1x = str(datetime.timedelta(seconds = totaltimess))
        print(f"Original Time: {totaltime1x}")

        totaltime_1_5x = divide_time_by_value(totaltime1x , 1.5)
        print(f"Time to complete in 1.5x: {totaltime_1_5x}")

        totaltime_1_75x = divide_time_by_value(totaltime1x , 1.75)
        print(f"Time to complete in 1.75x: {totaltime_1_75x}")

        totaltime_2x = divide_time_by_value(totaltime1x , 2)
        print(f"Time to complete in 2x: {totaltime_2x}")

        totaltime_3x = divide_time_by_value(totaltime1x , 3)
        print(f"Time to complete in 3x: {totaltime_3x}")

    except:
        print("Oopsie dasie an error occured. Check your internet connection and make sure you're using the correct format when writing the url.")








