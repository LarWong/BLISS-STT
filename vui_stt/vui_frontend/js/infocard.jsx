import React from 'react'
import PropTypes from 'prop-types'

class InfoCard extends React.Component {
    // What each info card needs:
    // Card title
    // Level
    // Value/Quantifier
    // Graphic that displays the the value in an intuitive way - figure this out later

    // Initialize the state of the infocard with blank values
    // Props should be empty
    constructor(props)
    {
        super(props)
        this.state = { title: '', level: '', value: 0 };
    }

    // Get the appropriate information necessary from the API/database
    // and assign it to the state members
    componentDidMount()
    {
        fetch('Add API Source here', { method: 'GET', credentials: 'same-origin' })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          this.setState({
            title: data.title,
            level: data.level,
            value: data.value,
          });
        })
        .catch((error) => console.log(error));
    }

    //
    render()
    {
        return (
            <div>
              <div className="post" onDoubleClick = {this.Like.handleDoubleClick}>
                
              </div>
            </div>
          );
    }
}