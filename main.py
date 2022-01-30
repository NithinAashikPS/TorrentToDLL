from flask import Flask
import libtorrent as lt
import time
import datetime
import threading

app = Flask(__name__)


def download():

    link = "magnet:?xt=urn:btih:299fd18d29d67330c9f1b3fa86bc660a24632e92&xt=urn:btmh:1220dc82c32e2036472cdfa3244f023372b1cd6242915129b48f5d798af4743f55bf&dn=www.TamilBlasters.sbs%20-%20Randu%20(2022)%20%5bMalayalam%20-%201080p%20HD%20AVC%20UNTOUCHED%20-%20x264%20-%20%5bDDP5.1(640Kbps)%20%2b%20AAC%5d%20-%207.7GB%20-%20ESub%5d.mkv&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.internetwarriors.net%3a1337%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2fretracker.lanta-net.ru%3a2710%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2fwww.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2ftracker0.ufibox.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.zerobytes.xyz%3a1337%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce"
    ses = lt.session()
    ses.listen_on(6881, 6891)
    params = {
        'save_path': './doodstream/',
        'storage_mode': lt.storage_mode_t(2)
    }

    print(link)

    handle = lt.add_magnet_uri(ses, link, params)
    ses.start_dht()

    begin = time.time()
    print(datetime.datetime.now())

    print('Downloading Metadata...')
    while (not handle.has_metadata()):
        time.sleep(1)
    print('Got Metadata, Starting Torrent Download...')

    print("Starting", handle.name())

    while (handle.status().state != lt.torrent_status.seeding):
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata',
                     'downloading', 'finished', 'seeding', 'allocating']
        print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' %
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
               s.num_peers, state_str[s.state]))
        time.sleep(5)

    end = time.time()
    print(handle.name(), "COMPLETE")

    print("Elapsed Time: ", int((end-begin)//60),
          "min :", int((end-begin) % 60), "sec")

    print(datetime.datetime.now())


@app.route("/")
def asd():

    threading.Thread(target=download, args=()).start()

    return "magnet"


if __name__ == "__main__":

    app.run(host="127.0.0.1", port=5000)
