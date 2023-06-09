![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen)

<!-- LOGO -->
<br />
<h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/ApexAgante/ApexAgenteSimple/main/img/new_logo.png" alt="Logo" width="140" height="140">
  <br>ApexAgente
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

<details open>
<summary>Go to the project directory</summary>
Go to the cloned project directory by using this command

```bash
cd ApexAgenteSimple
```

</details>

<details>
<summary class="optional">Creating a Python virtual environment (optional)</summary>
To create a Python virtual environment, run the following command

```bash
python3 -m venv venv
. venv/bin/activate
```

</details>

<details open>
<summary>Start the application</summary>
To start the application you can run this command

```bash
./runner <--type> [--n]
```

</details>

> **Note**
>
> - The `--type` option specifies whether to run the application in GUI mode or CLI mode. You can use `--gui` to run the GUI version or `--cli` to run the CLI version
> - The `--n` options deterime whether to use Poetry to run the application. Use `--n` to run without Poetry. If you choose to run with Poetry, ensure that you have Poetry installed on your system before running the application.

<style>
  .optional > summary {
    color: gray;
  }
</style>
