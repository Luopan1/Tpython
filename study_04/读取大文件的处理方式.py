# coding=utf-8



f = open( "/Volumes/Think/android-studio-ide-162.4069837-mac.dmg", "rb" )

while True:
    content = f.read( 1024 )
    print( content )
    if len( content ) == 0:
        break
