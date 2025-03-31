from analytics import Research
import config


def print_all():

    research_file = Research(config.NAME_DATA_FILE)
    file_contents = research_file.file_reader()

    report = Research.Analytics(file_contents)
    report.save_file(config.NAME_REPORT_FILE, config.FILE_EXTENSION)


if __name__ == "__main__":
    print_all()
