#!/usr/bin/env python

from burp import IBurpExtender
from burp import IHttpRequestResponse
from burp import IHttpService
from burp import ITab
from java.io import PrintWriter
from java.lang import RuntimeException
from javax.swing import JPanel
from javax.swing import JLabel
from javax.swing import JButton
from java.awt import Button
from java.awt import GridLayout

class BurpExtender(IBurpExtender, IHttpRequestResponse, IHttpService, ITab):

  def registerExtenderCallbacks(self, callbacks):
    self.callbacks = callbacks
    self.helpers = callbacks.getHelpers()
    callbacks.setExtensionName("Hello Burp")

    self.panel = JPanel()
    self.label = JLabel("Hello Burp")
    self.buttonOutput = Button("Print to Output", actionPerformed=self.printToOutput)
    self.buttonErrors = Button("Print to Errors", actionPerformed=self.printToErrors)
    self.buttonAlerts = Button("Print to Alerts", actionPerformed=self.printToAlerts)
    self.panel.add(self.label)
    self.panel.add(self.buttonOutput)
    self.panel.add(self.buttonErrors)
    self.panel.add(self.buttonAlerts)

    callbacks.customizeUiComponent(self.panel)
    callbacks.addSuiteTab(self)

    self.stdout = PrintWriter(callbacks.getStdout(), True)
    self.stderr = PrintWriter(callbacks.getStderr(), True)
    burpInfo = callbacks.getBurpVersion()
    self.stdout.println("Hello " + burpInfo[0] + " v" + burpInfo[1] + "." + burpInfo[2] +"!")

  def getTabCaption(self):
    return "Hello Burp"

  def getUiComponent(self):
    return self.panel

  def printToOutput(self, event):
    self.stdout.println("Hello output")

  def printToErrors(self, event):
    self.stderr.println("Hello errors")

  def printToAlerts(self, event):
    self.callbacks.issueAlert("Hello alerts")
