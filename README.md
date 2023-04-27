![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen)

<!-- LOGO -->
<br />
<h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/L0garithmic/FastColabCopy/main/img/logo.png" alt="Logo" width="140" height="110">
  <br>FastColabCopy
</h1>
  <p align="center">
    Python3 script to check Apex agent in Trend Micro.
    <br />
    </p>
</p>
<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#importing">Importing</a> •
  <a href="#run-locally">Run Locally</a>
</p>

## About The Project
Apex Agente is a powerful Python application designed to gather data from Trend Micro Apex URL, a cloud-based security platform that provides advanced threat protection for enterprise networks. With Apex Agente, you can easily retrieve all available data from the Apex URL or retrieve specific data by hostname.

The first feature of Apex Agente allows you to retrieve all data from the Apex URL, giving you a comprehensive view of all datas available. This data can include information on host name, entity id, registration ip, and last registration time.

The second feature of Apex Agente allows you to retrieve data specific to a particular host name. This feature is particularly useful if you want to drill down into getting deeper information of a particular host or agent. With this feature, you can retrieve information on a host which included name, entity id, server id, registration ip, connection status, etc.

Apex Agente is easy to use and comes with a simple and intuitive user interface. It is designed to work with Trend Micro Apex URL, so you can be confident that the data you retrieve is accurate and up-to-date. Whether you are a security professional, network administrator, or IT manager, Apex Agente is a must-have tool for monitoring the security status of your network and ensuring that your organization stays safe from potential threats.

## Importing
Import from github
```bash
  git clone https://github.com/ApexAgante/ApexAgenteSimple
```

## Run Locally
Go to the project directory
```bash
  cd ApexAgenteSimple
```

[OPTIONAL]
Make python virtualenv
```bash
python3 -m venv venv
. venv/bin/activate
```

Start the application
```bash
./runner <--type> [--n]
```

<div style="border: 1px solid #ccc; background-color: #f0f0f0; padding: 10px;">
    <p><strong>Note:</strong></p>
    <p>The '--type' option specifies whether to run the application in GUI mode or CLI mode. You can use '--type=gui' to run the GUI version or '--type=cli' to run the CLI version.</p>
    <p>The '--n' options determine whether to use Poetry to run the application. Use '--n' to run without Poetry. If you choose to run with Poetry, ensure that you have Poetry installed on your system before running the application.</p>
</div>