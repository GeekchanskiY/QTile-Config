from subprocess import check_output

def screens_info() -> list[str]:
        var = str(check_output("xrandr --listmonitors", shell=True)).split("\\n")
        del var[0]
        del var[-1]
        return var
        

def auto_init_screen():
    pass

if __name__ == "__main__":
    screens = screens_info()
    print(screens)
    for screen in screens:
        print(screen.split(" ")[3])
