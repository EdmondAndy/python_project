# OpenAI Chat Message Roles

In OpenAI’s chat system, every message has a **role**. Roles help the model understand *who is speaking* and *what context to follow*.  

---

## 1. System Role
- **Purpose:** Sets the stage, rules, and personality for the assistant.  
- **Who writes it:** Usually the app developer (hidden from the user).  
- **Example:**
  ```json
  {
    "role": "system",
    "content": "You are a helpful tutor who explains math step by step in simple language."
  }
  ```
- **Effect:** Shapes how the assistant responds throughout the whole conversation.  

---

## 2. User Role
- **Purpose:** The actual input/question/instruction from the end user.  
- **Who writes it:** You (the person chatting).  
- **Example:**
  ```json
  {
    "role": "user",
    "content": "Can you explain Pythagoras’ theorem with a real-life example?"
  }
  ```

---

## 3. Assistant Role
- **Purpose:** The AI’s response to the user.  
- **Who writes it:** The model (ChatGPT).  
- **Example:**
  ```json
  {
    "role": "assistant",
    "content": "Sure! Pythagoras’ theorem says... Imagine a ladder leaning against a wall..."
  }
  ```

---

## 4. Optional Roles
- **tool/function** → When the assistant calls a function.  
- **developer** → For hidden instructions that the user shouldn’t see.  
- **Example:**
  ```json
  {
    "role": "tool",
    "content": {
      "name": "search",
      "arguments": {"query": "latest weather in Melbourne"}
    }
  }
  ```

---

## Real-Life Analogy
- **System role** = Job contract (defines the boundaries of the assistant’s behavior).  
- **User role** = Customer request (what you ask).  
- **Assistant role** = Employee response (what the AI answers).  
- **Tool role** = Employee using a calculator or external tool to get an answer.  
