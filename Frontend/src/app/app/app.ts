import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Colors } from 'chart.js';
import { ChartModule } from 'primeng/chart';


const COLORS = [
  '#4dc9f650',
  '#f6701950',
  '#f5379450',
  '#537bc450',
  '#acc23650',
  '#166a8f50',
  '#00a95050',
  '#58595b50',
  '#8549ba50'
];
@Component({
  selector: 'app-root',
  imports: [RouterOutlet,ChartModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App implements OnInit {
  data: any;
  options: any;
  ngOnInit(): void {
    this.data = {
      labels: ["A","B","C"],
      datasets: [
        {
          label: 'Ribbon superior',
          data: [23,45,32],
          borderColor: "#000000",
          backgroundColor: COLORS[0],
        },
        {
          label: 'Média',
          data: [25,47,39],
          borderColor: "#000000",
          backgroundColor: COLORS[2],
        },
        {
          label: 'Ribbon inferior',
          data: [28,49,43],
          borderColor: "#000000",
          backgroundColor: COLORS[1],
          fill: '-2'
        },
      ]
    }

    this.options = {
      type: 'line',
      data: this.data,
      options: {
        scales: {
          y: {
            stacked: true
          }
        },
        plugins: {
          filler: {
            propagate: false
          },
          'samples-filler-analyser': {
            target: 'chart-analyser'
          }
        },
        interaction: {
          intersect: false,
        },
      },
    };
  }


}

