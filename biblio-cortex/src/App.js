import React, { Component, useState } from 'react';
import logo from './logo1.png';
import './App.css';





const Contact = (props) => {
	if(props.contact == false){
	return(<div></div>)
	}else{
	return(<div><p>
	<ul>
	{props.info.map(infos => <li key={infos.id}>{infos.id}: {infos.content}</li>)}
	
	
	</ul>
	</p></div>)
	}

}

const PastProjects = (props) => {
	if(props.pastProjects == false){
	return(<div></div>)
	}else{
	return(<div><p>PAST PROJECTS</p></div>)
	}

}

const Portfolio = (props) => {
	if(props.portfolio == false){
	return(<div></div>)
	}else{
	return(<div>
	<p><a href="https://www.linkedin.com/in/wolf-norgren-887403178">LinkedIn</a></p>
	<p><a href="https://github.com/WLNORGREN/TALOS/tree/master">Github</a></p>
	</div>)
	}

}

const About = (props) => {
	if(props.about == false){
	return(<div></div>)
	}else{
	return(<div><p>BiblioCortex provides consulting services in a wide variety of areas of software development
	from data science to web design.</p></div>)
	}

}



const App = () => {

const [contact, setContact] = useState(false)
const [pastProjects, setPastProjects] = useState(false)
const [portfolio, setPortfolio] = useState(false)
const [about, setAbout] = useState(false)

const info = [

	
	{id: "Name",
	content: "Wolf Norgren"},
	{id: "Title",
	content: "Chief Information Officer"},
	{id: "Phone",
	content: "402-237-6900"},
	{id: "E-mail",
	content: "wnorgren2@gmail.com"},


]

const handleContact = () => {
	setContact(!contact)
	setPastProjects(false)
	setPortfolio(false)
	setAbout(false)
}
const handlePastProjects = () => {
	setPastProjects(!pastProjects)
	setContact(false)
	setPortfolio(false)
	setAbout(false)
}
const handlePortfolio = () => {
	setPortfolio(!portfolio)
	setAbout(false)
	setPastProjects(false)
	setContact(false)
}
const handleAbout = () => {
	setAbout(!about)
	setContact(false)
	setPortfolio(false)
	setPastProjects(false)
}


const menuStyle =  {
  align:'top',

}

const buttonStyle = {
  backgroundColor: 'blue', 
  border: '2px solid white',
  borderRight: 'none',
  color: 'white',
  width: '25%',
  padding: '15px 32px',
  textAlign: 'center',
  textDecoration: 'none',
  display: 'inline-block',
  fontSize: '30px',
  fontWeight: 'bold',
  cursor: 'pointer',
  float: 'left',
}

const headerStyle = {
	textAlign: 'center',
}

const imageStyle = {
	display: 'block',
	marginLeft:'auto',
	marginRight:'auto',
	}




return(
<div>
	<h1 style={headerStyle}>BIBLIOCORTEX, LLC</h1>
	<img style={imageStyle} src={logo}></img>
	<div style={menuStyle}>
		<button onClick={handleContact} style={buttonStyle}>CONTACT</button>
		<button onClick={handlePastProjects} style={buttonStyle}>PAST PROJECTS</button>
		<button onClick={handlePortfolio} style={buttonStyle}>PORTFOLIO</button>
		<button onClick={handleAbout} style={buttonStyle}>ABOUT</button>
	</div>
	<div style={menuStyle}>
	<Contact contact={contact} info={info}/>
	<PastProjects pastProjects={pastProjects}/>
	<Portfolio portfolio={portfolio}/>
	<About about={about}/>
	</div>


</div>


)


}


export default App;
