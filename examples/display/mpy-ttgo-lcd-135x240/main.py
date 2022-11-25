import machine
import st7789
import utime


def setup_display() -> st7789.ST7789:
    """
    Set the display up.
    The driver library can be found here: https://github.com/russhughes/st7789_mpy
    The board specs can be found here: http://www.lilygo.cn/prod_view.aspx?TypeId=50062&Id=1400&FId=t3:50062:3

    :return: Display instance.
    """
    spi = machine.SPI(1, baudrate=30000000, polarity=1,
                      sck=machine.Pin(18), mosi=machine.Pin(19))
    device = st7789.ST7789(spi, 135, 240,
                           reset=machine.Pin(23, machine.Pin.OUT), cs=machine.Pin(5, machine.Pin.OUT),
                           dc=machine.Pin(16, machine.Pin.OUT), backlight=machine.Pin(4, machine.Pin.OUT),
                           rotations=[(0x00, 135, 240, 52, 40), (0x60, 240, 135, 40, 53), (0xc0, 135, 240, 53, 40), (0xa0, 240, 135, 40, 52)],
                           rotation=0, options=0)
    device.init()
    device.inversion_mode(True)
    device.sleep_mode(False)

    return device


class Button:
    def __init__(self, pin_number: int, inverted: bool) -> None:
        """
        This class creates an instance of a button.

        :param pin_number: Hardware pin number.
        :param inverted: Changes the logic from active low to active high.
        """
        self._pin = machine.Pin(pin_number, machine.Pin.IN, machine.Pin.PULL_UP)
        self._inverted = inverted

    @property
    def state(self) -> bool:
        return not bool(self._pin.value()) if self._inverted else bool(self._pin.value())


timer_0_flag = False
def timer_0_callback(timer: machine.Timer) -> None:
    global timer_0_flag
    timer_0_flag = True


timer_1_flag = False
def timer_1_callback(timer: machine.Timer) -> None:
    global timer_1_flag
    timer_1_flag = True


def main() -> None:
    global timer_0_flag
    global timer_1_flag

    display = setup_display()
    button_left = Button(0, True)
    button_right = Button(35, True)

    timer_0 = machine.Timer(0)
    timer_0.init(period=10, mode=machine.Timer.PERIODIC, callback=timer_0_callback)
    timer_1 = machine.Timer(1)
    timer_1.init(period=1000, mode=machine.Timer.PERIODIC, callback=timer_1_callback)

    display.on()

    display.rect(0, 0, 135, 240, st7789.GREEN)

    print(f"Display: h={display.height()}px, w={display.width()}px")

    y_index = 11
    while True:
        if timer_0_flag:
            timer_0_flag = False

            display.fill_circle(int(display.width() / 2), y_index, 20, st7789.BLACK)
            y_index += 1
            if y_index >= (display.height() - 11):
                y_index = 11
            display.fill_circle(int(display.width() / 2), y_index, 20, st7789.RED)

        if timer_1_flag:
            timer_1_flag = False
            print(f"Left: {button_left.state} - Right: {button_right.state}")


if __name__ == '__main__':
    main()
