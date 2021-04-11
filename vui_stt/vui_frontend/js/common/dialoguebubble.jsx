import React from 'react'
import PropTypes from 'prop-types'
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

class DialogueBubble extends React.Component {
    /* Component for voice assistant hints */

    constructor(props) {
        super(props);
        this.state = {
            message: "",
            bubblecolor: "",
        };
    }

    componentDidMount() {
        /* Runs as soon as component is mounted */
    }

    render() {
        /* Renders the component */
        return (
            <Container className="dialoguebubble" style={{backgroundColor: bubblecolor}}>
                <p>{this.state.message}</p>
            </Container>
        );
    }
}

DialogueBubble.propTypes = {
    message: PropTypes.string.isRequired,
    bubblecolor: PropTypes.string.isRequired,
};

export default DialogueBubble;