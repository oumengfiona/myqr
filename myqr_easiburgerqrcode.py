from MyQR import myqr
version, level, qr_name = myqr.run(
    words='https://melbsc.com.au/en/',
    version=2,
    level='H',
    picture='burger.gif',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='easiqrcode01.gif',
    save_dir="/Users/apple/PycharmProjects/helloworld3"
)