import PackageDescription

let package = Package(
    name: "PlayaSign", 
    dependencies: [
    	.Package(url: "https://github.com/IBM-Swift/BlueSocket.git", majorVersion: 0, minor: 11),
    	.Package(url: "https://github.com/Hearst-DD/ObjectMapper.git", majorVersion: 2, minor: 2),
    	.Package(url: "https://github.com/DaveWoodCom/XCGLogger.git", majorVersion: 5, minor: 0)
    ]
)
