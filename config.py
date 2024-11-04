# -*- coding: utf-8 -*-
# @Time:    2024-11-04 22:41
# @Author:  Herbert·Simon
# @Email:   yonglonggeng@163.com
# @WeChat:  ddgetget
# @File:    config.py
# @Project: GUI-Tools
# @Package: 
# @Ref:     just do it for yourself!


# 自定义HTML头信息
custom_css = """
<link rel="icon" href="/favicon.ico" type="image/x-icon">
"""

html_content = """
    <!DOCTYPE html>
    <html>
    <title>GUI-Tools</title>
    <link rel="icon" type="image/x-icon" href="/static/10pbr-f4sot-001.ico">
    <head>
        <title>FastAPI Table Example</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                padding: 0 20%;
            }
            .container {
                text-align: center;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
                text-align: left;
            }
            tr:nth-child(even) {background-color: #f9f9f9;}
            tr:hover {background-color: #ddd;}
            a {
                color: blue;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Table Data</h1>
            <table id="data-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </div>

        <script>
            async function fetchData() {
                const response = await fetch('/data');
                const data = await response.json();
                const tableBody = document.querySelector('#data-table tbody');
                tableBody.innerHTML = '';
                data.forEach(item => {
                    const baseUrl = new URL(window.location.href).origin;
                    const fullLink = `${baseUrl}${item.link}`;
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.id}</td>
                        <td>${item.app}</td>
                        <td>${item.des}</td>
                        <td><a href="${fullLink}" target="_blank">Go to ${item.app}</a></td>
                    `;
                    tableBody.appendChild(row);
                });
            }

            fetchData();
        </script>
    </body>
    </html>
    """
