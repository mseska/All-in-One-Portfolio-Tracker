import { Component } from "react";
import { PieChart, Pie, Cell, Tooltip } from "recharts";
import "./piechart.css";

class Piechart extends Component {
  state = {
    isHighlighted: false,
    name: "Deneme",
    data: [
      { name: "North", value: 100 },
      { name: "South", value: 200 },
      { name: "East", value: 300 },
      { name: "West", value: 400 },
      { name: "T", value: 500 },
      { name: "T2", value: 500 },
      { name: "T3", value: 500 },
      { name: "T4", value: 500 },
    ],
  };

  handleClick = () => {
    this.setState((prevState) => ({
      isHighlighted: !prevState.isHighlighted,
    }));
  };

  generateColors = (length) => {
    const COLORS = [
      "#0088FE",
      "#00C49F",
      "#FFBB28",
      "#FF8042",
      "#3D9970",
      "#85144b",
      "#7FDBFF",
      "#FFDC00",
      "#F012BE",
      "#FF851B",
      "#B10DC9",
      "#2ECC40",
      "#FF4136",
      "#39CCCC",
      "#2E2E2E",
      "#01FF70",
      "#7FDBFF",
      "#001f3f",
      "#F012BE",
      "#FFDC00",
      "#3D9970",
      "#85144b",
      "#7FDBFF",
      "#FFDC00",
      "#F012BE",
      "#FF851B",
      "#B10DC9",
      "#2ECC40",
      "#FF4136",
      "#39CCCC",
      "#2E2E2E",
      "#01FF70",
      "#7FDBFF",
      "#001f3f",
      "#F012BE",
      "#FFDC00",
      "#3D9970",
      "#85144b",
      "#7FDBFF",
      "#FFDC00",
      "#F012BE",
      "#FF851B",
      "#B10DC9",
      "#2ECC40",
      "#FF4136",
      "#39CCCC",
      "#2E2E2E",
      "#01FF70",
      "#7FDBFF",
      "#001f3f",
    ];
    const colors = [];
    for (let i = 0; i < length; i++) {
      colors.push(COLORS[i % COLORS.length]);
    }
    return colors;
  };

  render() {
    const colors = this.generateColors(this.state.data.length);
    const containerClass = this.state.isHighlighted ? "HighlightedContainer" : "PiechartContainer";

    return (
      <div
        className={`PiechartContainer ${containerClass}`}
        style={{ width: "400px" }}
      >
        <h3 className="PiechartName" onClick={this.handleClick}>
          {this.state.name}
        </h3>
        <PieChart width={250} height={250}>
          <Pie
            data={this.state.data}
            dataKey="value"
            nameKey="name"
            cx="50%"
            cy="50%"
            outerRadius={100}
            fill="#8884d8"
            labelLine={false}
          >
            {this.state.data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={colors[index]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </div>
    );
  }
}

export default Piechart;
