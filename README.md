# Serbia's used cars market analysis, visualized
Being interested in which used cars and brands are sold the most in Serbia, I've decided to write an web scraper that'll extract the amount of ads for each brand, and in it, each model and while at it, I found that visualizing it would be good way to have something that can be updated every few months while being easy to look at. And in future, changes to the market could be tracked and visualized.

## The process:
In order to do analysis and visualization, first there needed to be some data. <br>
I decided to obtain it from a popular site for used vehicles [polovniautomobili.com](https://www.polovniautomobili.com).
On the site there are 81 brands from which 1129 models, the scraper needed to visit each one and extract total amount of ads.
Data is saved to an .csv file, which is later read and manipulated through **Pandas**. After that, it is be visualized with **Matplotlib**

## Some of the visualized examples from data, by amount of current vehicles selling...
<div>
<ul>
  <li>Top 10 brands as lines with nubmers:</li><br>
  <img src="plot_images/top10-brands-line.png", width="500", height="400"/>
  <li>Same, but now as circle graph with procentages:</li><br>
  <img src="plot_images/top10-brands-circle.png", width="500", height="400"/><br>
  <li>Top 10 models in of Top 10 brands:</li><br>
  <img src="plot_images/top10-brands-models.png", width="auto", height="500"/><br>
  </ul>
</div>

