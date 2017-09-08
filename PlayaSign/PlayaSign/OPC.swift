//
//  OPC.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//  Copyright © 2017 GlamCocks. All rights reserved.
//

import Foundation
import Socket

public class OPC {
    public typealias PixelColor = (UInt8, UInt8, UInt8)

    private struct Utility {
        static func clampColor(color: PixelColor) -> PixelColor {
            let (r, g, b) = color
            return (min(255, max(0, r)), min(255, max(0, g)), min(255, max(0, b)))
        }
    }

    let hostName: String
    let port: Int32
    var configByte: UInt8 = 0
    var socket: Socket?

    public var dithering: Bool = true {
        didSet {
            if dithering {
                configByte &= ~0x01
            } else {
                configByte |= 0x01
            }
            sendConfigPackage()
        }
    }

    public var interpolation: Bool = true {
        didSet {
            if interpolation {
                configByte &= ~0x02
            } else {
                configByte |= 0x02
            }
            sendConfigPackage()
        }
    }

    public init(hostName: String, port: Int32) {
        self.hostName = hostName
        self.port = port
    }

    public func connect() {
        disconnect()

        do {
            socket = try Socket.create()
            try socket?.connect(to: hostName, port: port)
            logOPC.info("Connected to OPC server \(hostName):\(port)")
            sendConfigPackage()
        } catch {
            logOPC.error("Cannot create the socket")
        }
    }

    private func checkIfConnected() -> Bool {
        guard let socket = socket, socket.isConnected else {
            connect()
            return false
        }

        return true
    }

    public func disconnect() {
        socket?.close()
    }

    private func sendConfigPackage() {
        let configBytesArray: [UInt8] = [0, 0xFF, 0, 5, 0x00, 0x01, 0x00, 0x02, configByte]
        sendByteArray(bytes: configBytesArray)
    }

    public func setPixels(pixels: [PixelColor], channel: UInt8 = 0) {
        guard checkIfConnected() == true else {
            print("Not connected, skipping this command")
            return
        }

        let numPixels = pixels.count * 3
        let hiByte: UInt8 = UInt8(numPixels / 256)
        let loByte: UInt8 = UInt8(numPixels % 256)
        let command: UInt8 = 0
        let pixelBytes = pixels.flatMap { color -> [UInt8] in
            let (r, g, b) = Utility.clampColor(color: color)
            return [r,g,b]
        }

        let resultBytes: [UInt8] = [channel, command, hiByte, loByte] + pixelBytes
        sendByteArray(bytes: resultBytes)
    }

    private func sendByteArray(bytes: [UInt8]) {
        let bytesData = Data(bytes: bytes, count: bytes.count * MemoryLayout<UInt8>.size)
        do {
            try socket?.write(from: bytesData)
        } catch {
            print("cannot send data")
        }
    }
}
