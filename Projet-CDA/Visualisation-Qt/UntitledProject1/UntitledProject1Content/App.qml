import QtQuick
import QtQuick.Window
import UntitledProject1

Window {
    width: mainScreen.width
    height: mainScreen.height

    visible: true
    title: "UntitledProject1"

    Screen01 {
        id: mainScreen

        anchors.centerIn: parent
    }

}

