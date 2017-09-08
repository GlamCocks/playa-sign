//
//  main.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//  Copyright © 2017 GlamCocks. All rights reserved.
//

import Foundation

Defaults.registerDefaults()

guard CommandLine.arguments.count == 2, let configurationPath = CommandLine.arguments.last else {
    log.error("Configuration filepath missing")
    exit(1)
}

guard let data = try? Data(contentsOf: URL(fileURLWithPath: configurationPath)) else {
    log.error("Cannot read configuration file")
    exit(1)
}

do {
    if let configuration = Configuration(JSONString: try String(contentsOf: URL(fileURLWithPath: configurationPath))) {
        log.info("Loading '\(configuration.name)' configuration...")

        if let server = configuration.server {
            server.connect()

            let scene = RainbowScene()
            scene.setup(configuration.letters)

            while true {
                scene.render()
                server.push(configuration.render)
                usleep(useconds_t(1.0 / Defaults[.fps] * 1_000_000))
            }
        } else {
            log.error("Configuration does not contain OPC server information")
            exit(1)
        }
    } else {
        log.error("Configuration is not valid")
        exit(1)
    }
} catch {
    log.error(error.localizedDescription)
    exit(1)
}
