# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(760, 640)
        Register.setMinimumSize(QSize(720, 620))
        Register.setStyleSheet(u"QWidget#RegisterWidget { background-color: #0E1216; font-family: \"Segoe UI\"; color: #E8EFF5; }\n"
"QFrame#shellFrame { background-color: #11161A; border-radius: 30px; }\n"
"QFrame#brandPanel { background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0B161F, stop:0.62 #173548, stop:1 #1F5570); border-top-left-radius: 30px; border-bottom-left-radius: 30px; }\n"
"QLabel#badgeLabel { background-color: rgba(255, 167, 79, 0.16); color: #FFC184; border: 1px solid rgba(255, 177, 104, 0.34); border-radius: 16px; padding: 8px 14px; font-size: 11px; font-weight: 700; }\n"
"QLabel#heroTitle { color: #FFFFFF; font-size: 30px; font-weight: 700; }\n"
"QLabel#heroSubtitle, QLabel#infoText, QLabel[class=\"featureLabel\"] { color: rgba(255, 255, 255, 0.82); font-size: 14px; }\n"
"QFrame#infoCard { background-color: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 20px; }\n"
"QLabel#infoTitle { color: #FFFFFF; font-size: 16px; font-weight: 700; }\n"
"QFrame#formPanel { background-color: #131A20; border-top-right-radius: 30px; border-bottom-right-radius: 30px; }\n"
"QLabel#sectionTag { color: #FFAA5A; font-size: 12px; font-weight: 700; }\n"
"QLabel#formTitle { color: #E8EFF5; font-size: 30px; font-weight: 700; }\n"
"QLabel#formSubtitle, QLabel#requiredLabel { color: #9EA8B4; font-size: 14px; }\n"
"QLabel[class=\"fieldLabel\"] { color: #DCE6F1; font-size: 13px; font-weight: 700; }\n"
"QFrame[class=\"fieldGroup\"] { background-color: #131A20; border: 1px solid #223147; border-radius: 18px; }\n"
"QLineEdit, QComboBox { background-color: #10161D; border: 1px solid #223147; border-radius: 14px; padding: 10px 12px; min-height: 24px; color: #F4F9FF; selection-background-color: #2CCED2; selection-color: #08171D; }\n"
"QLineEdit:focus, QComboBox:focus { border: 2px solid #2CCED2; padding: 9px 11px; }\n"
"QComboBox::drop-down { border: none; width: 26px; }\n"
"QPushButton#registerButton { background-color: #2D6AB7; color: #FFFFFF; border: none; border-radius: 15px; padding: 14px 18px; font-size: 15px; font-weight: 700; }\n"
"QPushButton#registerButton:hover { background-color: #3F7FD2; }\n"
"QPushButton#registerButton:pressed { background-color: #245B95; }")
        self.mainLayout = QVBoxLayout(Register)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(28, 28, 28, 28)
        self.shellFrame = QFrame(Register)
        self.shellFrame.setObjectName(u"shellFrame")
        self.shellLayout = QHBoxLayout(self.shellFrame)
        self.shellLayout.setSpacing(0)
        self.shellLayout.setObjectName(u"shellLayout")
        self.shellLayout.setContentsMargins(0, 0, 0, 0)
        self.brandPanel = QFrame(self.shellFrame)
        self.brandPanel.setObjectName(u"brandPanel")
        self.brandPanel.setMinimumSize(QSize(320, 0))
        self.brandPanel.setMaximumSize(QSize(340, 16777215))
        self.brandLayout = QVBoxLayout(self.brandPanel)
        self.brandLayout.setSpacing(18)
        self.brandLayout.setObjectName(u"brandLayout")
        self.brandLayout.setContentsMargins(28, 28, 28, 28)
        self.badgeLabel = QLabel(self.brandPanel)
        self.badgeLabel.setObjectName(u"badgeLabel")

        self.brandLayout.addWidget(self.badgeLabel)

        self.heroTitle = QLabel(self.brandPanel)
        self.heroTitle.setObjectName(u"heroTitle")
        self.heroTitle.setWordWrap(True)

        self.brandLayout.addWidget(self.heroTitle)

        self.brandSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.brandLayout.addItem(self.brandSpacer)

        self.featureOneLabel = QLabel(self.brandPanel)
        self.featureOneLabel.setObjectName(u"featureOneLabel")
        self.featureOneLabel.setWordWrap(True)

        self.brandLayout.addWidget(self.featureOneLabel)

        self.featureTwoLabel = QLabel(self.brandPanel)
        self.featureTwoLabel.setObjectName(u"featureTwoLabel")
        self.featureTwoLabel.setWordWrap(True)

        self.brandLayout.addWidget(self.featureTwoLabel)


        self.shellLayout.addWidget(self.brandPanel)

        self.formPanel = QFrame(self.shellFrame)
        self.formPanel.setObjectName(u"formPanel")
        self.formLayout = QVBoxLayout(self.formPanel)
        self.formLayout.setSpacing(18)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(34, 34, 34, 34)
        self.sectionTag = QLabel(self.formPanel)
        self.sectionTag.setObjectName(u"sectionTag")

        self.formLayout.addWidget(self.sectionTag)

        self.formTitle = QLabel(self.formPanel)
        self.formTitle.setObjectName(u"formTitle")

        self.formLayout.addWidget(self.formTitle)

        self.formSubtitle = QLabel(self.formPanel)
        self.formSubtitle.setObjectName(u"formSubtitle")
        self.formSubtitle.setWordWrap(True)

        self.formLayout.addWidget(self.formSubtitle)

        self.fieldsGrid = QGridLayout()
        self.fieldsGrid.setSpacing(18)
        self.fieldsGrid.setObjectName(u"fieldsGrid")
        self.firstnameFieldGroup = QFrame(self.formPanel)
        self.firstnameFieldGroup.setObjectName(u"firstnameFieldGroup")
        self.firstnameGroupLayout = QVBoxLayout(self.firstnameFieldGroup)
        self.firstnameGroupLayout.setSpacing(8)
        self.firstnameGroupLayout.setObjectName(u"firstnameGroupLayout")
        self.firstnameGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.firstnameLabel = QLabel(self.firstnameFieldGroup)
        self.firstnameLabel.setObjectName(u"firstnameLabel")

        self.firstnameGroupLayout.addWidget(self.firstnameLabel)

        self.firstnameLineEdit = QLineEdit(self.firstnameFieldGroup)
        self.firstnameLineEdit.setObjectName(u"firstnameLineEdit")
        self.firstnameLineEdit.setMaxLength(40)
        self.firstnameLineEdit.setClearButtonEnabled(True)

        self.firstnameGroupLayout.addWidget(self.firstnameLineEdit)


        self.fieldsGrid.addWidget(self.firstnameFieldGroup, 0, 0, 1, 1)

        self.lastnameFieldGroup = QFrame(self.formPanel)
        self.lastnameFieldGroup.setObjectName(u"lastnameFieldGroup")
        self.lastnameGroupLayout = QVBoxLayout(self.lastnameFieldGroup)
        self.lastnameGroupLayout.setSpacing(8)
        self.lastnameGroupLayout.setObjectName(u"lastnameGroupLayout")
        self.lastnameGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.lastnameLabel = QLabel(self.lastnameFieldGroup)
        self.lastnameLabel.setObjectName(u"lastnameLabel")

        self.lastnameGroupLayout.addWidget(self.lastnameLabel)

        self.lastnameLineEdit = QLineEdit(self.lastnameFieldGroup)
        self.lastnameLineEdit.setObjectName(u"lastnameLineEdit")
        self.lastnameLineEdit.setMaxLength(40)
        self.lastnameLineEdit.setClearButtonEnabled(True)

        self.lastnameGroupLayout.addWidget(self.lastnameLineEdit)


        self.fieldsGrid.addWidget(self.lastnameFieldGroup, 0, 1, 1, 1)

        self.emailFieldGroup = QFrame(self.formPanel)
        self.emailFieldGroup.setObjectName(u"emailFieldGroup")
        self.emailGroupLayout = QVBoxLayout(self.emailFieldGroup)
        self.emailGroupLayout.setSpacing(8)
        self.emailGroupLayout.setObjectName(u"emailGroupLayout")
        self.emailGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.registerEmailLabel = QLabel(self.emailFieldGroup)
        self.registerEmailLabel.setObjectName(u"registerEmailLabel")

        self.emailGroupLayout.addWidget(self.registerEmailLabel)

        self.registerEmailLineEdit = QLineEdit(self.emailFieldGroup)
        self.registerEmailLineEdit.setObjectName(u"registerEmailLineEdit")
        self.registerEmailLineEdit.setMaxLength(100)
        self.registerEmailLineEdit.setClearButtonEnabled(True)

        self.emailGroupLayout.addWidget(self.registerEmailLineEdit)


        self.fieldsGrid.addWidget(self.emailFieldGroup, 1, 0, 1, 1)

        self.phoneFieldGroup = QFrame(self.formPanel)
        self.phoneFieldGroup.setObjectName(u"phoneFieldGroup")
        self.phoneGroupLayout = QVBoxLayout(self.phoneFieldGroup)
        self.phoneGroupLayout.setSpacing(8)
        self.phoneGroupLayout.setObjectName(u"phoneGroupLayout")
        self.phoneGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.phoneLabel = QLabel(self.phoneFieldGroup)
        self.phoneLabel.setObjectName(u"phoneLabel")

        self.phoneGroupLayout.addWidget(self.phoneLabel)

        self.phoneLineEdit = QLineEdit(self.phoneFieldGroup)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        self.phoneLineEdit.setMaxLength(10)
        self.phoneLineEdit.setClearButtonEnabled(True)

        self.phoneGroupLayout.addWidget(self.phoneLineEdit)


        self.fieldsGrid.addWidget(self.phoneFieldGroup, 1, 1, 1, 1)

        self.genderFieldGroup = QFrame(self.formPanel)
        self.genderFieldGroup.setObjectName(u"genderFieldGroup")
        self.genderGroupLayout = QVBoxLayout(self.genderFieldGroup)
        self.genderGroupLayout.setSpacing(8)
        self.genderGroupLayout.setObjectName(u"genderGroupLayout")
        self.genderGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.genderLabel = QLabel(self.genderFieldGroup)
        self.genderLabel.setObjectName(u"genderLabel")

        self.genderGroupLayout.addWidget(self.genderLabel)

        self.genderComboBox = QComboBox(self.genderFieldGroup)
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.setObjectName(u"genderComboBox")

        self.genderGroupLayout.addWidget(self.genderComboBox)


        self.fieldsGrid.addWidget(self.genderFieldGroup, 2, 0, 1, 1)

        self.roleFieldGroup = QFrame(self.formPanel)
        self.roleFieldGroup.setObjectName(u"roleFieldGroup")
        self.roleGroupLayout = QVBoxLayout(self.roleFieldGroup)
        self.roleGroupLayout.setSpacing(8)
        self.roleGroupLayout.setObjectName(u"roleGroupLayout")
        self.roleGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.roleLabel = QLabel(self.roleFieldGroup)
        self.roleLabel.setObjectName(u"roleLabel")

        self.roleGroupLayout.addWidget(self.roleLabel)

        self.roleComboBox = QComboBox(self.roleFieldGroup)
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.setObjectName(u"roleComboBox")

        self.roleGroupLayout.addWidget(self.roleComboBox)


        self.fieldsGrid.addWidget(self.roleFieldGroup, 2, 1, 1, 1)

        self.passwordFieldGroup = QFrame(self.formPanel)
        self.passwordFieldGroup.setObjectName(u"passwordFieldGroup")
        self.passwordGroupLayout = QVBoxLayout(self.passwordFieldGroup)
        self.passwordGroupLayout.setSpacing(8)
        self.passwordGroupLayout.setObjectName(u"passwordGroupLayout")
        self.passwordGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.registerPasswordLabel = QLabel(self.passwordFieldGroup)
        self.registerPasswordLabel.setObjectName(u"registerPasswordLabel")

        self.passwordGroupLayout.addWidget(self.registerPasswordLabel)

        self.registerPasswordLineEdit = QLineEdit(self.passwordFieldGroup)
        self.registerPasswordLineEdit.setObjectName(u"registerPasswordLineEdit")
        self.registerPasswordLineEdit.setMaxLength(255)
        self.registerPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.passwordGroupLayout.addWidget(self.registerPasswordLineEdit)


        self.fieldsGrid.addWidget(self.passwordFieldGroup, 3, 0, 1, 1)

        self.confirmFieldGroup = QFrame(self.formPanel)
        self.confirmFieldGroup.setObjectName(u"confirmFieldGroup")
        self.confirmGroupLayout = QVBoxLayout(self.confirmFieldGroup)
        self.confirmGroupLayout.setSpacing(8)
        self.confirmGroupLayout.setObjectName(u"confirmGroupLayout")
        self.confirmGroupLayout.setContentsMargins(16, 16, 16, 16)
        self.confirmPasswordLabel = QLabel(self.confirmFieldGroup)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")

        self.confirmGroupLayout.addWidget(self.confirmPasswordLabel)

        self.confirmPasswordLineEdit = QLineEdit(self.confirmFieldGroup)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setMaxLength(255)
        self.confirmPasswordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.confirmGroupLayout.addWidget(self.confirmPasswordLineEdit)


        self.fieldsGrid.addWidget(self.confirmFieldGroup, 3, 1, 1, 1)


        self.formLayout.addLayout(self.fieldsGrid)

        self.formSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.addItem(self.formSpacer)

        self.requiredLabel = QLabel(self.formPanel)
        self.requiredLabel.setObjectName(u"requiredLabel")
        self.requiredLabel.setWordWrap(True)

        self.formLayout.addWidget(self.requiredLabel)

        self.error_label = QLabel(self.formPanel)
        self.error_label.setObjectName(u"error_label")

        self.formLayout.addWidget(self.error_label)

        self.registerButton = QPushButton(self.formPanel)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(0, 52))

        self.formLayout.addWidget(self.registerButton)


        self.shellLayout.addWidget(self.formPanel)


        self.mainLayout.addWidget(self.shellFrame)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Inscription", None))
        self.badgeLabel.setText(QCoreApplication.translate("Register", u"NOUVEL UTILISATEUR", None))
        self.heroTitle.setText(QCoreApplication.translate("Register", u"Une inscription plus propre et plus simple.", None))
        self.featureOneLabel.setText(QCoreApplication.translate("Register", u"- Email et telephone controles plus facilement", None))
        self.featureOneLabel.setProperty(u"class", QCoreApplication.translate("Register", u"featureLabel", None))
        self.featureTwoLabel.setText(QCoreApplication.translate("Register", u"- Mise en page en deux colonnes plus professionnelle", None))
        self.featureTwoLabel.setProperty(u"class", QCoreApplication.translate("Register", u"featureLabel", None))
        self.sectionTag.setText(QCoreApplication.translate("Register", u"CREATION DE COMPTE", None))
        self.formTitle.setText(QCoreApplication.translate("Register", u"Inscription", None))
        self.formSubtitle.setText(QCoreApplication.translate("Register", u"Les champs affiches correspondent a la structure actuelle de la table users dans ta base.", None))
        self.firstnameFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.firstnameLabel.setText(QCoreApplication.translate("Register", u"* Prenom", None))
        self.firstnameLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.firstnameLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Prenom", None))
        self.lastnameFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.lastnameLabel.setText(QCoreApplication.translate("Register", u"* Nom", None))
        self.lastnameLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.lastnameLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Nom de famille", None))
        self.emailFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.registerEmailLabel.setText(QCoreApplication.translate("Register", u"* Email", None))
        self.registerEmailLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.registerEmailLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"adresse@exemple.com", None))
        self.phoneFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.phoneLabel.setText(QCoreApplication.translate("Register", u"Telephone", None))
        self.phoneLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.phoneLineEdit.setInputMask(QCoreApplication.translate("Register", u"0000000000;_", None))
        self.phoneLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"0612345678", None))
        self.genderFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.genderLabel.setText(QCoreApplication.translate("Register", u"* Genre", None))
        self.genderLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.genderComboBox.setItemText(0, QCoreApplication.translate("Register", u"Selectionner un genre", None))
        self.genderComboBox.setItemText(1, QCoreApplication.translate("Register", u"homme", None))
        self.genderComboBox.setItemText(2, QCoreApplication.translate("Register", u"femme", None))
        self.genderComboBox.setItemText(3, QCoreApplication.translate("Register", u"non-renseigner", None))

        self.roleFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.roleLabel.setText(QCoreApplication.translate("Register", u"* Role", None))
        self.roleLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.roleComboBox.setItemText(0, QCoreApplication.translate("Register", u"Selectionner un role", None))
        self.roleComboBox.setItemText(1, QCoreApplication.translate("Register", u"admin", None))
        self.roleComboBox.setItemText(2, QCoreApplication.translate("Register", u"gestionnaire", None))
        self.roleComboBox.setItemText(3, QCoreApplication.translate("Register", u"enseignant", None))
        self.roleComboBox.setItemText(4, QCoreApplication.translate("Register", u"etudiant", None))
        self.roleComboBox.setItemText(5, QCoreApplication.translate("Register", u"technicien", None))

        self.passwordFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.registerPasswordLabel.setText(QCoreApplication.translate("Register", u"* Mot de passe", None))
        self.registerPasswordLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.registerPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Definir un mot de passe", None))
        self.confirmFieldGroup.setProperty(u"class", QCoreApplication.translate("Register", u"fieldGroup", None))
        self.confirmPasswordLabel.setText(QCoreApplication.translate("Register", u"* Confirmation", None))
        self.confirmPasswordLabel.setProperty(u"class", QCoreApplication.translate("Register", u"fieldLabel", None))
        self.confirmPasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Confirmer le mot de passe", None))
        self.requiredLabel.setText(QCoreApplication.translate("Register", u"* Le telephone est optionnel, mais reste unique en base s'il est renseigne.", None))
        self.error_label.setText(QCoreApplication.translate("Register", u"erro", None))
        self.registerButton.setText(QCoreApplication.translate("Register", u"S'inscrire", None))
    # retranslateUi

