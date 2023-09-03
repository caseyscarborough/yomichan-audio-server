# <img src="https://i.imgur.com/1QgctyK.png" height="24" alt="Yomichan Logo"> Yomichan Audio Server

[![](https://github.com/caseyscarborough/yomichan-audio-server/actions/workflows/release.yaml/badge.svg)](https://github.com/caseyscarborough/yomichan-audio-server/actions/workflows/release.yaml)
[![](https://img.shields.io/badge/License-MIT-orange)](https://github.com/caseyscarborough/yomichan-audio-server/blob/master/LICENSE)
[![](https://img.shields.io/badge/Dockerhub-1.0.0-blue)](https://hub.docker.com/r/caseyscarborough/yomichan-audio-server)

This is a self-hosted audio server for Yomichan to fetch audio files from,
using a database containing over 250,000 unique expressions.
With this setup, you are able to create Anki cards nearly instantaneously,
get word audio without a working internet connection (if hosted internally
in your own network), and increase the quality and coverage of word audio.

This project was forked from [themoeway/local-audio-yomichan](https://github.com/themoeway/local-audio-yomichan) and has been modified by me to remove the Anki plugin-related files and slightly refactored to run standalone in Docker. All the credits go to the original creator [**@Aquafina-water-bottle**](https://www.github.com/Aquafina-water-bottle) and the others who worked on [local-audio-yomichan](https://github.com/themoeway/local-audio-yomichan).

The purpose of this project is to host the audio server externally
(outside of localhost). If you don't to host this on your own server,
NAS, Kubernetes cluster, etc. then you should stick with the original project.

## Reasons for and against this setup

<details>
    <summary><b>Advantages:</b> <i>(click here)</i></summary>

1. Most audio is gotten in **almost instantly**. Without the audio server,
    fetching the audio can take anywhere from one second to a full minute
    (on particularly bad days).

    Most of the delay from Yomichan when creating cards is from fetching the audio.
    In other words, audio fetching is the main bottleneck when creating Anki cards.
    This add-on removes the aforementioned bottleneck, meaning **you can make cards with virtually 0 delay**.
2. If you do not have internet access, you can still add audio to your cards (if hosted inside your home network).
3. Compared to standard Yomichan, this **improves audio coverage** because it adds various sources not covered by Yomichan: Forvo (select users), NHK 2016, and Shinmeikai 8.
4. Much [pre-processing](https://github.com/Aquafina-water-bottle/local-audio-yomichan-build-scripts) has been done to this audio to make it as high quality as possible:
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

1. <details>
     <summary><b>Download all the required audio files</b> <em>(click here)</em></summary>

   You have two main options:

    1. <details>
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
       >     

       </details>
     
    2. <details>
         <summary>MP3 audio (4.9 GiB)</summary>

       > Older and less efficient codec, but needed for compatibility with pretty much all evices.
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

  </details>

2. <b>Extract the `.tar.xz` file.</b>
    * **Windows** users can use [7zip](https://7-zip.org/download.html). Note that 7zip users must extract the resulting `tar` file as well.
    * **Linux and MacOS** users can use either the default GUI archive manager or the `tar -xf` command.

3. <b>Move the extracted `user_files` folder to the location you want to keep it.</b>
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

4. <b>[Configure and run the Docker container](#running-the-container).</b>
5. <details>
     <summary><b>Add the URL in Yomichan</b> <em>(click here)</em></summary>

   * In Yomichan Settings ![image](./img/yomichan_cog.svg), go to:
     > `Audio` →  `Configure audio playback sources`.
   * Set the first source to be `Custom URL (JSON)`.
   * Under the first source, set the `URL` field to be:
     ```
     http://localhost:5050/?term={term}&reading={reading}
     ```
     Or if you're hosting this externally on a server use
     ```
     ${EXTERNAL_URL}/?term={term}&reading={reading}
     ```
      e sure to replace `${EXTERNAL_URL}` with the same value you used when configuring the `EXTERNAL_URL` Docker environment variable.
   * If you have other sources, feel free to re-add them under the first source.
   ![image](./img/custom_url_json.gif)
  </details>

6. <b>Ensure that everything works.</b>

    To do this, play some audio from Yomichan. You should notice two things:

    - The audio should be played almost immediately after clicking the play button.
    - After playing the audio, you should be able to see the available sources by right-clicking on the play button.

    Here is an example for 読む:

    ![image](./img/yomu.gif)

    Play all the sources from the above (読む) to ensure the sound is properly fetched.

## Running the Server

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
# Basic usage for running with defaults
# (bind to 0.0.0.0:5050 with /data directory for audio and database):
docker run \
  -p 5050:5050 \
  -v /path/to/user_files:/data \
  caseyscarborough/yomichan-audio-server:latest

# To run externally, you may need to configure
# the environment. These environment variables are the
# defaults and can be modified if necessary:
docker run \
  -p 5050:5050 \
  -e BIND_ADDRESS=0.0.0.0 \
  -e BIND_PORT=5050 \
  -e EXTERNAL_URL="http://localhost:5050" \
  -e DATA_DIRECTORY=/data \
  -e CONFIG_DIRECTORY=/data \
  -v /path/to/user_files:/data \
  caseyscarborough/yomichan-audio-server:latest
```

You can use any of the following image tags:

- `latest` - The latest stable release
- `master` - The master branch
- `1.0.0` - Specific version (replace with the version you want to use)

<details>
  <summary><b>Advanced</b></summary>

You may want to separate the database directory from the audio files.
In my case, I wanted to host the audio files over NFS, but keep the
database on block storage to prevent issues with file locking with
SQLite. To do this, you can mount the audio files wherever you like
inside the container, as long as you update your `config.json` file
to point to the correct path inside the container:

```bash
docker run \
  -p 5050:5050 \
  # The database will still get initialized here
  -e DATA_DIRECTORY=/data \
  -v /path/to/database_folder:/data \
  # Mount the audio files at /user_files in
  # the container
  -v /path/to/user_files:/user_files \
  # Custom config at path /config/config.json
  -e CONFIG_DIRECTORY=/config \
  -v /path/to/config.json:/config/config.json
```

Then ensure that your `config.json` uses the proper paths (replacing
`/data` with `/user_files`):

```json
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
      "id": "shinmekai8",
      "path": "/user_files/shinmeikai8_files",
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

I will try to setup an `install.yaml` file or a Helm chart eventually to simplify this.

### Build and Run from Source

This has only been tested on Linux and macOS but it should likely work on Windows too:

```bash
git clone https://github.com/caseyscarborough/yomichan-audio-server.git
cd yomichan-audio-server
docker build . -t yomichan-audio-server
docker run ... yomichan-audio-server
```

### Run the Container in Kubernetes

You can run this in Kubernetes using a setup similar to the following. In this setup I am hosting the audio files on an NFS share and mounting it into the `/user_files` directory in the container. The database files are in a persistent volume mounted at `/data`.

* <details>
  
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
              - name: audio
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
          - name: audio
            nfs:
              path: /path/to/user_files
              server: 192.168.1.100
  ```
  
  </details>
  
* <details>
      <summary>configmap.yaml</summary>
  
  The following is my ConfigMap for the `config.json` file. I've added the NHK '98 files from AJATT Tools audio source (see [Adding Additional Sources](#adding-additional-sources)).
  
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
  
* <details>
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
  
* <details>
      <summary>pvc.yaml</summary>
  
  I am using [Longhorn](https://longhorn.io/) for persistent storage but you can use whatever you like.
  If this is for your `/data` directory (where the database goes), you should
  likely avoid NFS, since SQLite sometimes has issues with NFS due to file locking.
  
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
  
* <details>
      <summary>ingress.yaml</summary>
  
  This is an example for [Nginx Ingress](https://github.com/kubernetes/ingress-nginx), but you can use other Ingresses like [Traefik](https://github.com/traefik/traefik).
  
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

## Adding Additional Sources

You can add additional sources by using your own `config.json` file. For example, you can add the NHK '98 source audio from [Ajatt-Tools](https://github.com/Ajatt-Tools) by doing the following:

* Clone the repo you wish to add into your `user_files` directory:
  
  ```bash
  cd /path/to/user_files
  # For opus
  git clone https://github.com/Ajatt-Tools/nhk_1998_pronunciations_index
  
  # For mp3
  git clone https://github.com/Ajatt-Tools/nhk_1998_pronunciations_index_mp3
  ```
* Add the new source to your `config.json` (other sources are omitted for the purposes of the example):

  ```json
  {
    "sources": [
      {
        "type": "ajt_jp",
        "id": "nhk98",
        "path": "/data/nhk_1998_pronunciations_index_mp3",
        "display": "NHK98 %s"
      }
    ]
  }
  ```

> Note: Adding the NHK '16 files from AJATT tools won't work out of the box and requires additional setup due to the pronunciations in the index file being Katakana and using the handakuten on "g" sounds to denote nasality. Just stick to the original `nhk16_files` from the torrent for the NHK '16 source which work out of the box.

## Configuring Sources

* If you wish to reorder the priority of sources or remove sources,
    you can specify the sources using the custom URL. Here are a few examples:
    * <details>
        <summary>JPod, NHK16, Shinmeikai8, Forvo (the original default order)</summary>

      ```
      http://localhost:5050/?term={term}&reading={reading}&sources=jpod,nhk16,shinmeikai8,forvo
      ```

      </details>
    * <details>
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

## Troubleshooting

These are additional instructions and tips if something doesn't work as expected.

* Ensure the local audio server is actually running.
  You can do this by visiting [http://localhost:5050](http://localhost:5050).
  If it says "Local Audio Server (version)", then the server is up and running!
* Ensure you haven't copied any files from the torrent outside of `user_files`.
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
