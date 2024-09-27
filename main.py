import io
import sys
from tools import setup

if __name__ == "__main__":
    # 创建io缓冲区
    output_err = io.StringIO()
    sys.stderr = output_err
    output_stdout = io.StringIO()
    sys.stdout = output_stdout
    # 主函数
    run = setup.Run()
    run.run()