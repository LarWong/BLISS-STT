import React from 'react'
import PropTypes from 'prop-types'


/*
Profile Button class for user.
When clicked, shows a users profile
and communication options
*/
class ProfileButton extends React.Component {
    
    // Initialize button with userId
    constructor(props) {
        super(props);
        this.state = { profileImg: '', profileLink: '', name:''};
    }

    componentDidMount() {
        const { userId } = this.props;

        fetch('INSERT_API_ROUTE_HERE', {
            method: 'GET',
            credentials: 'same-origin',
          })
            .then((response) => {
              if (!response.ok) throw Error(response.statusText);
              return response.json();
            })
            .then((data) => {
              this.setState({
                profileImg: data.profileImg,
                profileLink: data.profileLink,
                name: data.name,
              });
            })
            .catch((error) => console.log(error));
     }

     render() {
        return <div>
                    <a className='profileButton' 
                    href={this.state.profileImg} 
                    >
                        <img source={this.state.profileImgUrl} alt={this.state.name}/>
                    </a>
     }          </div>
}