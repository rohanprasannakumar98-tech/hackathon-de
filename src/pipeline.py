from utils.logging import get_logger

logger = get_logger()

def main():
    logger.info("Pipeline starting...")
    # TODO: extract -> transform -> load -> dq
    logger.info("Pipeline finished (skeleton).")

if __name__ == "__main__":
    main()
