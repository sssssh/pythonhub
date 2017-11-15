import time
import array
from PIL import Image


x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def show_greyscale(output_raw, width, height, max_iterations):
    max_iterations = float(max(output_raw))
    print(max_iterations)
    scale_factor = float(max_iterations)
    scaled = [int(o / scale_factor * 255) for o in output_raw]
    output = array.array('B', scaled)
    im = Image.new("L", (width, width))
    im.frombytes(output.tostring(), "raw", "L", 0, -1)
    im.show()


def show_false_greyscale(output_raw, width, height, max_iterations):
    assert width * height == len(output_raw)
    max_value = float(max(output_raw))
    output_raw_limited = [int(float(o) / max_value * 255) for o in output_raw]
    output_rgb = (
        (o + (256 * o) + (256 ** 2) * o) * 16 for o in output_raw_limited)
    output_rgb = array.array('I', output_rgb)
    im = Image.new("RGB", (width, height))
    im.frombytes(output_rgb.tostring(), "raw", "RGBX", 0, -1)
    im.show()


def calculate_z_serial_purepython(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_pure_python(draw_output, desired_width, max_iterations):
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y1 - y2) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    width = len(x)
    height = len(y)
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("length of x:", len(x))
    print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")
    assert sum(output) == 33219980

    if draw_output:
        show_greyscale(output, width, height, max_iterations)


if __name__ == "__main__":
    calc_pure_python(draw_output=True, desired_width=1000, max_iterations=300)
