from PNGProcessor import PNGProcessor

png_path = "test.png"

processor = PNGProcessor()

# 사진 열어서 2차원 리스트로 저장
pixels = processor.open_png(png_path)

if pixels:
    # 색상 반전
    inverted_pixels = processor.invert_image_colors(pixels)

    #사진 출력
    for y in pixels:
        for x in y:
            if x<10:
                print("  ",x,end="")
            elif x<100:
                print(" ",x,end="")
            else:
                print("",x,end="")
        print()

    #반전 사진 출력
    for y in inverted_pixels:
        for x in y:
            if x<10:
                print("  ",x,end="")
            elif x<100:
                print(" ",x,end="")
            else:
                print("",x,end="")
        print()

    #이미지 모양
    print("Image:", len(pixels), "rows /", len(pixels[0]),"columns")

