import { useState } from 'react'
import './App.css'

const backend_url = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    setIsLoading(true); 
    setResponse("");


    try {
      const res = await fetch(`${backend_url}/send-message?message=${encodeURIComponent(message)}`);
    
      const data = await res.json();

      if (res.ok && data.status === "success") {
        setResponse(data.message);
        setMessage("");
      } else {
        setResponse(data.message || "Error occurred while sending the message.");
      }
    } catch (error) {
      console.error("Error:", error);
      setResponse("Failed to connect to the server.");
    } finally{
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <div className='logo-container'>
        <img src="./logo.jpg" alt="company logo" className='logo' />
        <h2>DexyAI</h2>
      </div>
      
      <h1>Send Message to Wellfound</h1>
      <form onSubmit={handleSubmit}>
        <h3 className=''>Enter Your Message</h3>
        <textarea
          id="message"
          className='input-field'
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message here..."
          required
        />
        <button type="submit" disabled={!message || isLoading}>{isLoading ? "Sending..." : "Send Message"}</button>
      </form>
      {response && <p className="response-success">{response}</p>}
  

    </div>
  );
}

export default App
