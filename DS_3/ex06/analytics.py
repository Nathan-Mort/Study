import os
from random import randint
import config
import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    filename="analytics.log",
    format="%(asctime)s %(message)s",
    filemode="w",
)


class Research:

    def __init__(self, file_path):
        self.file_path = file_path
        logging.info("Инициализация Research")

    def file_reader(self, has_header=True):

        if not os.path.exists(self.file_path):
            logging.error(f"Файл '{self.file_path}' не найден.")
            raise FileNotFoundError(f"Файл '{self.file_path}' не найден.")

        with open(self.file_path, "r") as data_file:
            lines = [line.strip() for line in data_file.readlines()]
            if len(lines) < 2:
                logging.error("Неверное количество строк")
                raise ValueError("Неверное количество строк")

            if has_header:
                header = lines[0].split(",")
                if len(header) != 2:
                    logging.error("Неверное количество заголовков")
                    raise ValueError("Неверное количество заголовков")
                data_lines = lines[1:]
            else:
                data_lines = lines

            data_list = []
            for line in data_lines[1:]:
                values = line.split(",")
                if len(values) != 2 or not all(value in ["0", "1"] for value in values):
                    logging.error("Неверное содержание строк")
                    raise ValueError("Неверное содержание строк")
                data_list.append([int(value) for value in values])

        logging.info(f"Файл '{self.file_path}' успешно прочитан")
        return data_list

    class Calculations:

        def __init__(self, data_list):
            self.data_list = data_list
            self.heads, self.tails = self.counts()
            self.total = self.total_tossing()
            self.head_fraction, self.tail_fraction = self.fractions()
            logging.info("Инициализация Calculations")

        def counts(self):
            heads = sum(row[0] for row in self.data_list)
            tails = sum(row[1] for row in self.data_list)
            logging.info("Подсчет количества heads и tails")
            return heads, tails

        def total_tossing(self):
            total = self.heads + self.tails
            logging.info("Подсчет общего количества подбрасываний")
            return total

        def fractions(self):
            if self.total != 0:
                head_fraction = (self.heads / self.total) * 100
                tail_fraction = (self.tails / self.total) * 100
            logging.info("Подсчет процентного содержания")
            return head_fraction, tail_fraction

    class Analytics(Calculations):

        def __init__(self, data_list):
            super().__init__(data_list)
            self.predictions = self.predict_random()
            self.predict_heads, self.predict_tails = self.count_tails_and_heads()
            logging.info("Инициализация Analytics")

        def predict_random(self):
            predicts = []
            for _ in range(config.NUM_OF_STEPS):
                rand_num = randint(0, 1)
                predict = [rand_num, 1 - rand_num]
                predicts.append(predict)
            logging.info("Формирование списка предполагаемых исходов")
            return predicts

        def count_tails_and_heads(self):
            predict_heads = sum(row[0] for row in self.predictions)
            predict_tails = sum(row[1] for row in self.predictions)
            logging.info("Подсчет количества heads и tails предполагаемых исходов")
            return predict_heads, predict_tails

        def save_file(self, name_of_file, file_format):
            logging.info("Формирование Отчета")
            try:
                with open(name_of_file + file_format, "w") as report_file:
                    report_file.write(
                        f"We have made {self.total} observations from tossing a coin: "
                        f"{self.tails} of them were tails and {self.heads} of them were heads.\n"
                        f"The probabilities are {self.tail_fraction:.2f}% and {self.head_fraction:.2f}%, respectively. Our forecast "
                        f"is that in the next\n{config.NUM_OF_STEPS} observations we will have: "
                        f"{self.predict_tails} tail and {self.predict_heads} heads."
                    )
                logging.info("Отчет успешно создан")
                self.message = "Отчет успешно создан"
            except Exception as e:
                logging.error(f"Ошибка при создании отчета: {e}")
                self.message = "Отчет не создан из-за ошибки"

            self.send_telegram_message()

        def send_telegram_message(self):
            url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": config.TELEGRAM_CHAT_ID, "text": self.message}
            try:
                requests.post(url, json=payload)
                logging.info(f"Сообщение отправлено в Telegram: {self.message}")
            except Exception as e:
                logging.error(f"Ошибка при отправке сообщения в Telegram: {e}")
