# <img src="https://i.imgur.com/1QgctyK.png" height="24" alt="Yomichan Logo"> Yomichan Audio Server

[![](https://github.com/caseyscarborough/yomichan-audio-server/actions/workflows/release.yaml/badge.svg)](https://github.com/caseyscarborough/yomichan-audio-server/actions/workflows/release.yaml)

This is a self-hosted audio server for Yomichan to fetch audio files from,
using a database containing over 250,000 unique expressions.
With this setup, you are able to create Anki cards nearly instantaneously,
get word audio without a working internet connection (if hosted internally
in your own network), and increase the quality and coverage of word audio.

This project was forked from [themoeway/local-audio-yomichan](https://github.com/themoeway/local-audio-yomichan) and has been modified by me to remove the Anki plugin-related files and slightly refactored to run standalone in Docker. All the credits go to the original creator [**@Aquafina-water-bottle**](https://www.github.com/Aquafina-water-bottle) and the others who worked on [local-audio-yomichan](https://github.com/themoeway/local-audio-yomichan).

The purpose of this project is to host the audio server externally
(outside of localhost). If you don't want to mess with Docker, or
don't want to host this on your own server, NAS, Kubernetes cluster,
etc. then you stick with the original project.

## Reasons for and against this setup

<details>
    <summary><b>Advantages:</b> <i>(click here)</i></summary>

1. Most audio is gotten in **almost instantly**. Without the audio server,
    fetching the audio can take anywhere from one second to a full minute
    (on particularly bad days).

    Most of the delay from Yomichan when creating cards is from fetching the audio.
    In other words, audio fetching is the main bottleneck when creating Anki cards.
    This add-on removes the aforementioned bottleneck, meaning **you can make cards with virtually 0 delay**.

1. If you do not have internet access, you can still add audio to your cards.

1. Compared to standard Yomichan, this **improves audio coverage** because it adds various sources not covered by Yomichan: Forvo (select users), NHK 2016, and Shinmeikai 8.

1. Much [pre-processing](https://github.com/Aquafina-water-bottle/local-audio-yomichan-build-scripts) has been done to this audio to make it as high quality as possible:
    - All audio is normalized, so the volume remains relatively similar for each file.
    - Silence has been trimmed from the beginning and end of each file.
    - Using JMdict's data, variant forms with the same readings are back-filled with existing audio.

</details>

<details>
    <summary><b>Disadvantages:</b> <i>(click here)</i></summary>

1. This setup requires about **3-5 GB of free space**.

</details>

## Instructions

These instructions setup the audio server using Docker.

1. Download all the required audio files. You have two main options:

    1.  <details>
        <summary><b>Ogg/Opus audio (2.5 GiB) (Recommended)</b></summary>

        > The [Opus](https://opus-codec.org/) audio codec provides much better quality at lower bitrates (which saves a lot of space and makes syncing large collections faster).
        >
        > **However, Opus is NOT compatible with AnkiMobile (iOS), Android 4, and AnkiWeb.**
        > If you use any of these, please use the 2nd option (MP3 audio) below.
        >
        > -   **Download the files from [this torrent](https://nyaa.si/view/1681655)**.
        >     Alternatively, use the magnet link below:
        >     <details><summary>Magnet link</summary>
        >
        >     ```
        >     magnet:?xt=urn:btih:ef90ec428e6abcd560ffc85a2a1c083e0399d003&dn=local-yomichan-audio-collection-2023-06-11-opus.tar.xz&tr=http%3a%2f%2fanidex.moe%3a6969%2fannounce&tr=http%3a%2f%2fnyaa.tracker.wf%3a7777%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.moeking.me%3a6969%2fannounce&tr=udp%3a%2f%2fopentracker.i2p.rocks%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.zerobytes.xyz%3a1337%2fannounce
        >     ```
        >
        >     </details>
        </details>

    1.  <details>
        <summary>MP3 audio (4.9 GiB)</summary>

        > Older and less efficient codec, but needed for compatibility with pretty much all devices.
        > -   **Download the files from [this torrent](https://nyaa.si/view/1681654)**.
        >     Alternatively, use the magnet link below:
        >     <details><summary>Magnet link</summary>
        >
        >     ```
        >     magnet:?xt=urn:btih:5bd0aa89667860e68b31a585dc6e7a2bfc811702&dn=local-yomichan-audio-collection-2023-06-11-mp3.tar.xz&tr=http%3a%2f%2fanidex.moe%3a6969%2fannounce&tr=http%3a%2f%2fnyaa.tracker.wf%3a7777%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fopen.stealth.si%3a80%2fannounce&tr=udp%3a%2f%2ftracker.tiny-vps.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.moeking.me%3a6969%2fannounce&tr=udp%3a%2f%2fopentracker.i2p.rocks%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.torrent.eu.org%3a451%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=udp%3a%2f%2ftracker.zerobytes.xyz%3a1337%2fannounce
        >     ```
        >
        >     </details>
        </details>

    If you have never downloaded from a torrent before, I highly recommend using the
    [qBittorrent](https://www.qbittorrent.org/) client.

2. Extract the `.tar.xz` file.
    * **Windows** users can use [7zip](https://7-zip.org/download.html). Note that 7zip users must extract the resulting `tar` file as well.
    * **Linux and MacOS** users can use either the default GUI archive manager or the `tar -xf` command.

3. Move the extracted `user_files` folder to the location you want to keep it.
    It will need to be mounted into your Docker container.
    <details>
        <summary>Expected file structure <i>(click here)</i></summary>

    ```    
    └── user_files
        ├── jmdict_forms.json
        ├── forvo_files
        │   ├── akitomo
        │   │   └── 目的.opus
        │   ├── kaoring
        │   │   └── ...
        │   └── ...
        ├── jpod_files
        │   ├── media
        │   │   ├── 000113d2d8419a26e97eacc0b7cfd675.opus
        │   │   ├── 0001d108dd8f99509769192effc1f9e4.opus
        │   │   └── ...
        │   ├── index.json
        │   └── source_meta.json
        ├── nhk16_files
        │   ├── audio
        │   │   ├── 20170616125910.opus
        │   │   └── ...
        │   └── entries.json
        └── shinmeikai8_files
            ├── media
            │   ├── 00001.opus
            │   ├── 00002.opus
            │   └── ...
            └── index.json
    ```
    </details>

4. [Configure and run the Docker container](#running-the-container).
5. Add the URL in Yomichan.

    * In Yomichan Settings ![image](./img/yomichan_cog.svg), go to:
      > `Audio` →  `Configure audio playback sources`.

    * Set the first source to be `Custom URL (JSON)`.
    * Under the first source, set the `URL` field to `http://localhost:5050/?term={term}&reading={reading}`, or if you're hosting this externally on a server, `${EXTERNAL_URL}/?term={term}&reading={reading}`, replacing `${EXTERNAL_URL}` with the same value you used when configuring the Docker environment variable.
    * If you have other sources, feel free to re-add them under the first source.
    ![image](./img/custom_url_json.gif)


6. Ensure that everything works. To do this, play some audio from Yomichan.
    You should notice two things:

    - The audio should be played almost immediately after clicking the play button.
    - After playing the audio, you should be able to see the available sources
        by right-clicking on the play button.

        Here is an example for 読む:

        ![image](./img/yomu.gif)

    Play all the sources from the above (読む) to ensure the sound is properly fetched.

## Running the Container

### Preparation

Ensure that you've copied the extracted audio folder (`user_files`) to a specific location. This folder will need to be mounted into the container at the path `/data` (which can customized using the `DATA_DIRECTORY` environment variable).

You can optionally provide your own `config.json` file. You can use the [`plugin/config.default.json`](https://github.com/caseyscarborough/yomichan-audio-server/blob/master/plugin/config.default.json) file as a starting point. If you use this file, it can be placed at the root of the `DATA_DIRECTORY`. Alternatively, you can put it elsewhere and configure the `CONFIG_DIRECTORY` environment variable to the path of the folder that contains it. Using a custom `config.json` gives you the following:
- Changing the priority of sources and removing sources
- Specify a path for each source folder. You can use this to store audio files in a different drive.
- Add entirely new audio sources.

If you're hosting the project externally (not on localhost), you will want to configure the `EXTERNAL_URL` environment variable, so that the server knows how to respond with the proper audio links from the API. An example value for this would be something like `https://mydomain.com`.

### Environment Variables

All environment variables should be optional, these are mostly for overriding the default configuration.

- `BIND_ADDRESS` - The hostname/address to bind to, defaults to `0.0.0.0`
- `BIND_PORT` - The port to bind to, defaults to `5050`
- `EXTERNAL_URL` - The external address for the server, defaults to `http://$BIND_ADDRESS:$BIND_PORT`.
- `DATA_DIRECTORY` - The path to the `user_files` folder containing the audio files, defaults to `/data`. This needs to match the path to the files in your custom `config.json` file.
- `CONFIG_DIRECTORY` - The path to the directory holding your `config.json` file, defaults to the `DATA_DIRECTORY`.

### Run the Container using Docker

```bash
# Basic usage for running locally:
docker run \
  -p 5050:5050
  -v /path/to/user_files:/data
  caseyscarborough/yomichan-audio-server:latest

# To run on externally, you will need to configure
# the environment. These environment variables are the
# defaults and can be modified if necessary:
docker run \
  -p 5050:5050
  -e BIND_ADDRESS=0.0.0.0
  -e BIND_PORT=5050
  -e EXTERNAL_URL="http://localhost:5050"
  -e DATA_DIRECTORY=/data
  -e CONFIG_DIRECTORY=/data
  -v /path/to/user_files:/data
  caseyscarborough/yomichan-audio-server:latest
```

You can use any of the following image tags:

- `latest` - The latest stable release
- `master` - The master branch
- `1.0.0` - Specific version (replace with the version you want to use)

### Run the Container in Kubernetes

You can run this in Kubernetes using a setup similar to the following. In this setup I am hosting the audio files on an NFS share and mounting it into the `/user_files` directory in the container. The database files are in a persistent volume mounted at `/data`.

<details>

  <summary>deployment.yaml</summary>

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yomichan-audio-server
  namespace: yomichan-audio-server
  labels:
    app: yomichan-audio-server
spec:
  replicas: 1
  revisionHistoryLimit: 0
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: yomichan-audio-server
  template:
    metadata:
      labels:
        app: yomichan-audio-server
    spec:
      serviceAccountName: default
      containers:
        - name: yomichan-audio-server
          image: "caseyscarborough/yomichan-audio-server:latest"
          imagePullPolicy: Always
          env:
            - name: TZ
              value: America/New_York
            - name: PUID
              value: "1000"
            - name: PGID
              value: "1000"
            - name: BIND_ADDRESS
              value: "0.0.0.0"
            - name: BIND_PORT
              value: "5050"
            - name: EXTERNAL_URL
              value: "https://yourdomain.sh"
            - name: DATA_DIRECTORY
              value: /data
            # Host the config file separately
            # because we're going to mount it
            # with a configmap.
            - name: CONFIG_DIRECTORY
              value: "/config"
          ports:
            - name: http
              containerPort: 5050
              protocol: TCP
          volumeMounts:
            - name: pvc
              mountPath: /data
            - name: downloads
              mountPath: /user_files 
            - name: config
              mountPath: /config
      volumes:
        - name: config
          configMap:
            name: yomichan-audio-server-cm
            items:
              - key: config.json
                path: config.json
        - name: pvc
          persistentVolumeClaim:
            claimName: yomichan-audio-server-pvc
        # You can use this to host the files on an NFS share
        - name: downloads
          nfs:
            path: /path/to/user_files
            server: 192.168.1.100
```

</details>

<details>
    <summary>configmap.yaml</summary>

The following is my custom configuration file. I've removed the `shinmekai8_files` that is included in the torrent and added the Shinmekai 8 and NHK '99 files from AJATT Tools [here](https://github.com/Ajatt-Tools/?q=mp3&type=all&language=&sort=). Don't try adding the NHK '16 files from AJATT tools, because it won't work properly without some additional setup due to the pronunciations in the index file being Katakana and using the handakuten on "g" sounds to denote nasality. Just stick to the original `nhk16_files` for the NHK '16 source.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: yomichan-audio-server-cm
  namespace: yomichan-audio-server
data:
  config.json: |
    {
      "sources": [
        {
          "type": "nhk",
          "id": "nhk16",
          "path": "/user_files/nhk16_files",
          "display": "NHK16 %s"
        },
        {
          "type": "ajt_jp",
          "id": "nhk98",
          "path": "/user_files/nhk_1998_pronunciations_index_mp3",
          "display": "NHK98 %s"
        },
        {
          "type": "ajt_jp",
          "id": "shinmekai8",
          "path": "/user_files/shinmeikai_8_pronunciations_index_mp3",
          "display": "SMK8 %s"
        },
        {
          "type": "forvo",
          "id": "forvo",
          "path": "/user_files/forvo_files",
          "display": "Forvo (%s)"
        },
        {
          "type": "jpod",
          "id": "jpod",
          "path": "/user_files/jpod_files",
          "display": "Jpod101"
        },
        {
          "type": "jpod",
          "id": "jpod_alternate",
          "path": "/user_files/jpod_alternate_files",
          "display": "JPod101 Alt"
        }
      ]
    }
```

</details>

<details>
    <summary>service.yaml</summary>

```yaml
apiVersion: v1
kind: Service
metadata:
  name: yomichan-audio-server
  namespace: yomichan-audio-server
  labels:
    app: yomichan-audio-server
spec:
  type: ClusterIP
  ports:
    - port: 5050
      name: http
      targetPort: http
      protocol: TCP
  selector:
    app: yomichan-audio-server
```
</details>

<details>
    <summary>pvc.yaml</summary>

I am using Longhorn for persistent storage but you can use whatever you like.
If this is for your `/data` directory (where the database goes), you should
likely avoid NFS though since SQLite sometimes has issues with NFS due to file locking.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: yomichan-audio-server-pvc
  namespace: yomichan-audio-server
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: longhorn
  resources:
    requests:
      storage: 1Gi
```
</details>

<details>
    <summary>ingress.yaml</summary>

This is an example for nginx-ingress, but you can use any Ingress.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: yomichan-audio-server-ingress
  namespace: yomichan-audio-server
  annotations:
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
    nginx.ingress.kubernetes.io/proxy-body-size: "0"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
      - '*.mydomain.com'
      secretName: cluster-wildcard-cert
  rules:
  - host: yomichan.mydomain.com
    http:
      paths:
      - pathType: Prefix
        path: /
        backend:
          service:
            name: yomichan-audio-server
            port:
              number: 5050
```

</details>

## Configuring sources

* If you wish to reorder the priority of sources or remove sources,
    you can specify the sources using the custom URL.

    Here are a few examples:

    *   <details>
        <summary>JPod, NHK16, Shinmeikai8, Forvo (the original default order)</summary>

        ```
        http://localhost:5050/?term={term}&reading={reading}&sources=jpod,nhk16,shinmeikai8,forvo
        ```

        </details>

    *   <details>
        <summary>NHK16, Shinmeikai8, Forvo (JPod will never be fetched!)</summary>

        ```
        http://localhost:5050/?term={term}&reading={reading}&sources=nhk16,shinmeikai8,forvo
        ```

        </details>

* For Forvo audio specifically, you can modify the priority of users by using `&user=`.

    For example, the following will get Forvo audio in the priority of strawberrybrown, then akitomo. All other users **will not be included in the search**.
    ```
    http://localhost:5050/?term={term}&reading={reading}&user=strawberrybrown,akitomo
    ```

    <details>
    <summary>List of available Forvo users</summary>

    * `akitomo`
    * `kaoring`
    * `poyotan`
    * `skent`
    * `strawberrybrown`

    </details>


## Build and Run from Source

This has only been tested on Linux and macOS but it should likely work on Windows too:

```bash
git clone https://github.com/caseyscarborough/yomichan-audio-server.git
cd yomichan-audio-server
docker build . -t yomichan-audio-server
docker run ... yomichan-audio-server
```

## Troubleshooting
These are additional instructions and tips if something doesn't work as expected.

*   Ensure the local audio server is actually running.
    You can do this by visiting [http://localhost:5050](http://localhost:5050).
    If it says "Local Audio Server (version)", then the server is up and running!
*   Ensure you haven't copied any files from the torrent outside of `user_files`.
* If all else fails, remove the `entries*` files from your `DATA_DIRECTORY` and restart the server.

## Credits & Acknowledgements

A huge thanks to [@Aquafina-water-bottle](https://github.com/Aquafina-water-bottle) for creating the original project. This couldn't have been done without that project.

The following is the list of credits and acknowledgements from the original project ([themoeway/local-audio-yomichan](https://github.com/themoeway/local-audio-yomichan)):

* **Zetta#3033**: Creator of the original addon + gave advice for improving query speed
* **kezi#0001**: Getting NHK16 audio
* **(anonymous)**: Adding SQL + NHK16 audio support
* **[@Renji-XD](https://github.com/Renji-XD)**: Getting Forvo audio, adding Forvo audio support
* **[@tatsumoto-ren](https://github.com/tatsumoto-ren)**: [Getting Shinmeikai 8 audio](https://github.com/Ajatt-Tools/shinmeikai_8_pronunciations_index)
* **[@MarvNC](https://github.com/MarvNC)**: Creating and maintaining the torrent + testing out the rewritten add-on
* **[@shoui520](https://github.com/shoui520)**: Maintaining and popularizing the original set of instructions that these instructions were initially based off of
* **[@ctpk](https://github.com/ctpk)**: Investigated and patched a bug with `.aac` files not having the correct mime type
* **[@Mansive](https://github.com/Mansive)**: Helped with [pre-processing the audio](https://github.com/Aquafina-water-bottle/local-audio-yomichan-build-scripts)
* **[@tsweet64](https://github.com/tsweet64)**: Added support for more audio types, and helped with [pre-processing the audio](https://github.com/Aquafina-water-bottle/local-audio-yomichan-build-scripts)
* **[@jamesnicolas](https://github.com/jamesnicolas)**: Creator of [Yomichan Forvo Server for Anki](https://github.com/jamesnicolas/yomichan-forvo-server). The original code was heavily based off of this project.
* **[@KamWithK](https://github.com/KamWithK)**: Creator of [Ankiconnect Android](https://github.com/KamWithK/AnkiconnectAndroid). This allows the local audio server to work on Android. Also gave advice for improving the database.
* **[@DillonWall](https://github.com/DillonWall)**: Creator of [Generate Batch Audio](https://github.com/DillonWall/generate-batch-audio-anki-addon). This allows you to backfill existing cards with the local audio server, or anything else.

## License

[MIT](https://github.com/caseyscarborough/yomichan-audio-server/blob/master/LICENSE)
