//
//  Configuration.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import ObjectMapper

struct Configuration: Mappable {
    var name: String = "unknown"
    var server: Server?
    var letters: [Letter] = []

    var render: [Pixel] {
        return letters.flatMap { $0.channels }.flatMap { $0.pixels }
    }

    init?(map: Map) { }

    mutating func mapping(map: Map) {
        name <- map["name"]
        server <- map["server"]
        letters <- map["letters"]
    }
}
