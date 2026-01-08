import concurrent.futures
import time
import functions as proxy_utils


def main():
    with open('proxy_list.txt', "r") as file:
        lines = file.readlines()

    flag = input("Check every port? (Y/N):\n").lower() in ['y', 'yes']
    lst = proxy_utils.url_gen_all(lines) if flag else (next(proxy_utils.url_gen(line)) for line in lines)
    sorted_lst = sorted(lst, key=proxy_utils.get_port)

    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(proxy_utils.check_proxy, sorted_lst)
        for result in results:
            print(result)

    finish = time.perf_counter()
    total_time = round(finish - start, 2)
    print(f"Finished in {total_time} second{'s'[:int(total_time) ^ 1]}")


if __name__ == "__main__":
    main()
