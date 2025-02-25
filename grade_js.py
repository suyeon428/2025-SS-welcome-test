# 해달 부트캠프 과제 채점 프로그램
# JavaScript 코드를 실행하여 테스트 케이스를 통과하는지 확인합니다.

import os
import sys
import time
import threading
import itertools
import subprocess

def spinner(stop):
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    while not stop():
        sys.stdout.write(next(spinner) + ' 채점 중입니다.')
        sys.stdout.flush()
        sys.stdout.write('\r')
        time.sleep(0.1)

def print_welcome():
    print("🌟 해달 부트캠프 과제 채점기 🌟")

def print_result(problem: str, result: dict[int, tuple[bool, str]]):
    sys.stdout.write('\r                              \n')
    sys.stdout.flush()

    print(f"📝 {problem} 문제 채점 결과")

    for number, (success, message) in result.items():
        if  success:
            print(f"✅ 테스트 {number}: 통과")
        else:
            print(f"❌ 테스트 {number}: {message}")

def run(script: str, input_data) -> list[tuple[str, float]]:
    start_time = time.time()

    process = subprocess.Popen(
        ["node", script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    process.stdin.write(input_data)
    process.stdin.close()

    output = []
    while True:
        line = process.stdout.readline()
        if not line and process.poll() is not None:
            break
        if line:
            elapsed = time.time() - start_time
            output.append((line.strip(), elapsed))
    
    if process.poll() is None:
        process.terminate()

    return output


# a, b, c, e, d, f 문제를 채점하는 함수
def compare(answer: list[str], output: list[tuple[str, float]]) -> tuple[bool, str]:
    timeout = 1

    if len(answer) != len(output):
        return (False, "정답이 아닙니다.")

    for _, (expected, (actual, elapsed)) in enumerate(zip(answer, output)):
        if expected != actual:
            return (False, "정답이 아닙니다.")
        if elapsed > timeout:
            return (False, "시간 초과")

    return (True, "테스트 통과")


def check(problem: str) -> dict[int, tuple[bool, str]]:
    stop_spinner = False
    spinner_thread = threading.Thread(target=spinner, args=(lambda: stop_spinner,))
    spinner_thread.start()

    check_table = {
        1: (False, ""),
        2: (False, ""),
        3: (False, ""),
        4: (False, ""),
        5: (False, ""),
    }

    for number in range(1, 6):
        input_txt = os.path.join(os.path.dirname(__file__), f"answer/{problem}/input{number}.txt")
        output_txt = os.path.join(os.path.dirname(__file__), f"answer/{problem}/output{number}.txt")
        script = os.path.join(os.path.dirname(__file__), f"javaScript_test/{problem}.js")
        
        # 파일 끝까지 읽어서 한 문장으로 만들기
        try:
            f = open(input_txt)
            input_data = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"입력 파일이 존재하지 않습니다.: {problem}/input{number}.txt")

        expected_output = []
        try:
            f = open(output_txt)
            for line in f:
                expected_output.append(line.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f"출력 파일이 존재하지 않습니다.: {problem}/output{number}.txt")
        
        try:
            f = open(script)
        except FileNotFoundError:
            raise FileNotFoundError(f"스크립트 파일이 존재하지 않습니다.: {problem}.js")

        # 실행
        output = run(script, input_data)

        check_table[number] = compare(expected_output, output)

    stop_spinner = True
    spinner_thread.join()
    sys.stdout.write('\r')
    sys.stdout.flush()
    
    return check_table


def compare_h1(answer: list[str], output: list[tuple[str, float]], timeouts: list[int]) -> tuple[bool, str]:
    if len(answer) != len(output):
        return (False, "정답이 아닙니다.")

    max_elapsed = 0
    for i, (expected, (actual, elapsed)) in enumerate(zip(answer, output)):
        if expected != actual:
            return (False, "정답이 아닙니다.")
        max_elapsed = max(max_elapsed, int(elapsed))
    
    if max(timeouts) != max_elapsed:
        return (False, "시간이 올바르지 않습니다.")

    return (True, "테스트 통과")


def compare_h2(answer: list[str], output: list[tuple[str, float]], timeouts: list[int]) -> tuple[bool, str]:
    if len(answer) != len(output):
        return (False, "정답이 아닙니다.")

    max_elapsed = 0
    if len(answer) == 1:
        if answer[0] == output[0][0]:
            return (True, "테스트 통과")
        
        return (False, "정답이 아닙니다.")

    for i, (expected, (actual, elapsed)) in enumerate(zip(answer, output)):
        if expected != actual:
            if "배포" in actual:
                if str(int(elapsed)) in actual:
                    continue
            return (False, "정답이 아닙니다.")
        if actual.count(str(int(elapsed))) <= 0:
            return (False, "시간이 올바르지 않습니다.")

        max_elapsed = max(max_elapsed, int(elapsed))
    
    if max(timeouts) != max_elapsed:
        return (False, "시간이 올바르지 않습니다.")

    return (True, "테스트 통과")

def check_with_time(problem: str) -> dict[int, tuple[bool, str]]:
    stop_spinner = False
    spinner_thread = threading.Thread(target=spinner, args=(lambda: stop_spinner,))
    spinner_thread.start()

    check_table = {
        1: (False, ""),
        2: (False, ""),
        3: (False, ""),
        4: (False, ""),
        5: (False, ""),
    }

    for number in range(1, 6):
        input_txt = os.path.join(os.path.dirname(__file__), f"answer/{problem}/input{number}.txt")
        output_txt = os.path.join(os.path.dirname(__file__), f"answer/{problem}/output{number}.txt")
        script = os.path.join(os.path.dirname(__file__), f"javaScript_test/{problem}.js")
        
        # 파일 끝까지 읽어서 한 문장으로 만들기
        try:
            f = open(input_txt)
            input_data = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"입력 파일이 존재하지 않습니다.: {problem}/input{number}.txt")
        timeouts = list(map(int, input_data.split(' ')))

        expected_output = []
        try:
            f = open(output_txt)
            for line in f:
                expected_output.append(line.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f"출력 파일이 존재하지 않습니다.: {problem}/output{number}.txt")
        
        try:
            f = open(script)
        except FileNotFoundError:
            raise FileNotFoundError(f"스크립트 파일이 존재하지 않습니다.: {problem}.js")

        # 실행
        output = run(script, input_data)

        if problem == "h1":
            check_table[number] = compare_h1(expected_output, output, timeouts)
        elif problem == "h2":
            check_table[number] = compare_h2(expected_output, output, timeouts)

    stop_spinner = True
    spinner_thread.join()
    sys.stdout.write('\r')
    sys.stdout.flush()
    
    return check_table


def main():
    print_welcome()

    perfect = True
    for problem in ('a', 'b', 'c', 'd', 'e', 'f'):
        check_table = check(problem)
        for success, _ in check_table.values():
            perfect = success and perfect
        print_result(problem, check_table)

    for problem in ('h1', 'h2'):
        check_table = check_with_time(problem)
        for success, _ in check_table.values():
            perfect = success
        print_result(problem, check_table)
    

    print()
    if perfect:
        print("🎉 모든 문제를 성공적으로 통과하였습니다.")
    else:
        print("😢 아쉽게도 모든 문제를 통과하지 못하였습니다.")
        exit(1)


if __name__ == '__main__':
    main()
