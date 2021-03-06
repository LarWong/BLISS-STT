import React from 'react'
import PropTypes from 'prop-types'
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

class VoiceHints extends React.Component {
    /* Component for voice assistant hints */

    constructor(props) {
        super(props);
        this.state = {
            hintslist: [],
            numhintstoshow: 4,
        };
    }

    componentDidMount() {
        /* Runs as soon as component is mounted */
        // TODO: get hints list dynamically, figure out where from
        this.setState(
            {
                hintslist = [
                   '"Call John."',
                   '"What\'s on my schedule?"',
                   '"Retrieve radiation data."',
                   '"Start taking notes."',
                   '"Send Kevin a message."',
                   '"What\'s the time?"',
                   '"What can you do?"',
                   '"I want to hear a joke!"',
                ]
            }
        );
    }

    showMoreHints(event) {
        // TODO: implement
    }

    render() {
        /* Renders the component */
        return (
            <Container className="voicehints">
                <h1>Some things you can say:</h1>
                <React.Fragment>
                    <ul className="voicehintslist">
                        {
                            this.state.hintslist.slice(0, 4).map(
                                hintitem => (
                                    <li key={hintitem} className="voicehintsitem">
                                        {hintitem}
                                    </li>
                                )
                            )
                        }
                    </ul>
                </React.Fragment>
                <Button type="button" onClick={this.showMoreHints}>See More</Button>
            </Container>
        );
    }
}

VoiceHints.propTypes = {
    numhintstoshow: PropTypes.number.isRequired,
};

export default VoiceHints;