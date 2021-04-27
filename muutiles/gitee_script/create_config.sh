l='
kf5-kcrash
kf5-kjobwidgets
kf5-kpackage
kf5-kpty
kf5-kdesu
kf5-kglobalaccel
kf5-kiconthemes
kf5-knotifications
kf5-kservice
kf5-ktextwidgets
kf5-kwallet
kf5-frameworkintegration
kf5-kdelibs4support
kf5-kemoticons
kf5-kio
kf5-plasma
kf5-syntax-highlighting
kf5-kxmlgui
kf5-kdewebkit
'
for i in $l;do
  cat >>config.txt << EOF
    {
        'access_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXX',
        'title': 'init package',
        'body': 'init package',
        'srcbranch': 'userid:master',
        'dst': 'src-openeuler',
        'dstbranch': 'master',
        'dstrepo': '$i',
        'Content-Type': 'application/json;charset=UTF-8'
    },
EOF
done
