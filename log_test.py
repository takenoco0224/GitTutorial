from logging import basicConfig, getLogger, DEBUG

# このスクリプト本体のロガーを取得してログレベルを設定する
logger = getLogger(__name__)
logger.setLevel(DEBUG)

def main():
    # ここからメイン処理を書く
    logger.debug('This is debug message.')
    logger.info('This is info message.')
    logger.warn('This is warning message.')
    logger.error('This is error message.')
    logger.critical('This is critical message.')
if __name__ == '__main__':
    # このスクリプトから呼び出されるモジュール全体のログ設定を行う
    basicConfig(
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt='%y-%m-%d %H:%M:%S'
    )

    # メイン処理実行
    main()
