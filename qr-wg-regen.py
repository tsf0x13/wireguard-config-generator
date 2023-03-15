import os, fnmatch, qrcode

def qr_regen(directory, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                config = f.read()
                img = qrcode.make(config)
                print(os.path.splitext(filepath)[0])
                img.save(f"{os.path.splitext(filepath)[0]}.png")
                
qr_regen("/Users/tsf/Nextcloud/ISLG_IT/VPN", "client*.conf")