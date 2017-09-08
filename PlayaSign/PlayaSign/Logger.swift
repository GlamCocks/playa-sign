//
//  Logger.swift
//  Socket
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import XCGLogger

public let log = XCGLogger(identifier: "Default", showLogIdentifier: false)
public let logOPC = XCGLogger(identifier: "OPC", showLogIdentifier: true)

public extension XCGLogger {
    public convenience init(identifier: String,
                            showLogIdentifier: Bool,
                            showFunctionName: Bool = true,
                            showThreadName: Bool = true,
                            showLogLevel: Bool = true,
                            showFileName: Bool = true,
                            showLineNumber: Bool = true,
                            showDate: Bool = true) {
        self.init(identifier: identifier, includeDefaultDestinations: false)

        // TODO: Set to .info when not in debug build
        outputLevel = .debug

        let aslDestination = AppleSystemLogDestination(owner: self, identifier: "\(identifier).destination.asl")
        aslDestination.showLogIdentifier = showLogIdentifier
        aslDestination.showFunctionName = showFunctionName
        aslDestination.showThreadName = showThreadName
        aslDestination.showLevel = showLogLevel
        aslDestination.showFileName = showFileName
        aslDestination.showLineNumber = showLineNumber
        aslDestination.showDate = showDate
        aslDestination.outputLevel = outputLevel
        add(destination: aslDestination)
    }
}
