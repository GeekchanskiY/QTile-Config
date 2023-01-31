from subprocess import check_output

def get_memory_usage() -> dict:
    """ Gets current memory usage with free command """
    usage = str(check_output("free", shell=True)).split("\\n")[1].split("     ")
    total = usage[1].strip()
    used = usage[2].strip()
    free = usage[3].strip()
    return {
        "used": used,
        "free": free,
        "total": total,
    }


if __name__ == "__main__":
    print(get_memory_usage())
