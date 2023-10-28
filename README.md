<!-- Improved compatibility of back to top link: See: https://github.com/glweber/python_dash/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the python_dash. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">SuperSales Insights - Dashboard Python</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project is a Python-based dashboard designed for the visualization of supermarket sales data. It provides an interactive interface that allows users to explore and analyze sales data easily and efficiently.

## Key Features

- **Data Visualization:** The dashboard offers interactive charts and tables that display essential information about supermarket sales, including sales trends, top-selling categories, performance over time, and more.

- **Analysis Tools:** Users can select the desired month for analysis.

- **User-Friendly Interface:** The dashboard's interface is intuitive and user-friendly, designed to cater to both technical and non-technical users for optimal data visualization.

- **Flexibility:** This project is highly flexible and customizable, allowing for expansion and the addition of additional features to meet user needs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

![Python][Python.lg]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

. Clone this repository to your local machine.

2. Install the dependencies listed in the `requirements.txt` file using `pip`.

3. Run the Streamlit application with the command `streamlit run dash.py` from the `/py` folder.

4. Open your web browser and access `http://localhost:8501` to interact with the dashboard.

5. Explore the data, apply filters, and analyze the supermarket sales information.

### Docker

1. Clone this repository to your local machine.

2. Ensure that Docker is installed on your machine.

3. Navigate to the project's root folder.

4. Execute the following command to build and run the Docker image:

   ```sh
     docker build -t my-dashboard-app .
     docker run -p 8501:8501 my-dashboard-app
   ```
   
5. Open your web browser and access `http://localhost:8501` to interact with the dashboard.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Guilherme Weber - weba.guilherme@outlook.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Dashboard built based on a tutorial from Azimov Academy.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/glweber/python_dash.svg?style=for-the-badge
[contributors-url]: https://github.com/glweber/python_dash/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/glweber/python_dash.svg?style=for-the-badge
[stars-url]: https://github.com/glweber/python_dash/stargazers
[issues-shield]: https://img.shields.io/github/issues/glweber/python_dash.svg?style=for-the-badge
[issues-url]: https://github.com/glweber/python_dash/issues
[license-shield]: https://img.shields.io/github/license/glweber/python_dash.svg?style=for-the-badge
[license-url]: https://github.com/glweber/python_dash/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/glweber
[product-screenshot]: src/img/screenshot.png
[Python.lg]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python_url]: www.python.org
