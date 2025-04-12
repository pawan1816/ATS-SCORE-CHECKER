const API_URL = 'http://localhost:5000';

export const checkATSScore = async (resumeText, jobDescription) => {
  try {
    const response = await fetch(`${API_URL}/check-score`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        resume: resumeText,
        job_description: jobDescription,
        credentials: "include",
      }),
      credentials: 'include'
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    return { error: error.message || 'Failed to check score' };
  }
};