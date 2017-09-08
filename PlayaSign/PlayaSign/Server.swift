//
//  Server.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import ObjectMapper

fileprivate let sizeChannel = 64
fileprivate let nbrChannels = 8

class Server: Mappable {
    private var hostname: String = "localhost"
    private var port: Int32 = 7890
    private var opc: OPC?
    private var numberControllers: Int = 0

    required init?(map: Map) { }

    deinit {
        opc?.disconnect()
    }

    func mapping(map: Map) {
        hostname <- map["hostname"]
        port <- map["port"]
        numberControllers <- map["controllers"]
    }

    func connect() {
        opc = OPC(hostName: hostname, port: port)
        opc?.connect()
    }

    func push(_ render: [Pixel]) {
        log.debug()
        let sizeScreen = numberControllers * nbrChannels * sizeChannel
        var pixels: [OPC.PixelColor] = Array(repeatElement((0,0,0), count: sizeScreen))

        render.forEach {
            let i = $0.index + ($0.channel?.index ?? 0) * sizeChannel
            let channelColorSpace = $0.channel?.colorspace ?? .rgb
            let colorspace = Defaults[.colorspaceCorrection] ? channelColorSpace : .rgb
            pixels[i] = $0.color.convert(to: colorspace)
        }

        opc?.setPixels(pixels: pixels)
    }

    func clean() {
        let sizeScreen = numberControllers * 8 * 64
        let pixels: [OPC.PixelColor] = Array(repeatElement((0,0,0), count: sizeScreen))
        opc?.setPixels(pixels: pixels)
    }
}
