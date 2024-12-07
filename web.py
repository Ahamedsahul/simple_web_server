from http.server import HTTPServer, BaseHTTPRequestHandler
content="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laptop Specs</title>
</head>
<body>
    <center>
        <h1>LAPTOP SPECIFICATION</h1>
        <img src="Laptop.webp" alt="">
        <table border ="12" style="margin-bottom: 30px;">
            <tr>
               <th>PROCESSOR</th>
               <td>AMD Ryzen™ R7-7435HS</td>
            </tr>
            <tr>
                <th>OPERATING SYSTEM</th>
                <td>Windows 11 Pro</td>
            </tr>
            <tr>
                <th>GRAPHICS</th>
                <td>NVIDIA® GeForce RTX™ 4060 Laptop GPU 8GB GDDR6 (115W ) 2370MHz Boost Clock (VR ready, G-SYNC support) <br>
                    40 Series NVIDIA Supported Technologies: <br>
                    NVIDIA DLSS 3 <br>
                        i) NVIDIA Ada Lovelace Architecture <br>
                       ii) NVIDIA Max-Q Technologies <br>
                      iii) Advanced Optimus <br>
                       iv) Optimal Playable Settings <br>
                        v) Rapid Core Scaling <br>
                       vi) CPU Optimizer <br>
                      vii) Dynamicboost <br>
                     viii) DLSS <br>
                       ix) Resizable BAR <br>
                </td>
            </tr>
            <tr>
                <th>MEMORY</th>
                <td>Up to 24GB (2x12GB) 4800MHz DDR5 <br>
                    2 x SO-DIMM</td>
            </tr>
            <tr>
                <th>STORAGE</th>
                <td>Up to 1TB M.2 2242 PCIe SSD (Gen4) (The slots support M.2 2280 and 2242) <br>

                    2 x PCIE-Gen4-SSD-Slot (2280/2242 capable design, 1 occupied by default SSD installed; the other is reserve for customer upgrade.)</td>
            </tr>
            <tr>
                <th>BATTERY</th>
                <TD>4-cell 60Whr <br>

                    Support Super Rapid Charge Pro (10min charge 0-40% capacity, 30min charge 0-80% capacity, 60min charge 0-100% capacity) </TD>
            </tr>
            <tr>
                <th>AUDIO</th>
                <td>2 x 2 watt speakers with Nahimic Audio</td>
            </tr>
            <tr>
                <th>CAMERA</th>
                <td>Built-in Webcam (720p) with E-Shutter</td>
            </tr>
        </table>
    </center>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd= HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()