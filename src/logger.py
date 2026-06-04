import logging
import os

os.makedirs(
    "logs",
    exist_ok=True
)

logging.basicConfig(
    filename="logs/execucao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def registrar_log(mensagem):
    logging.info(mensagem)