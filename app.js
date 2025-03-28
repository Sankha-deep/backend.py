import React, { useState } from "react";
import { View, Text, TextInput, Button, ScrollView, StyleSheet } from "react-native";
import axios from "axios";

export default function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const fetchRiskAnalysis = async () => {
    try {
      const result = await axios.get("http://127.0.0.1:8000/analyze_risk/");
      setResponse(result.data.risk_analysis);
    } catch (error) {
      setResponse("Error fetching data");
    }
  };

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>AI Risk Management Chatbot</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter risk query..."
        value={query}
        onChangeText={setQuery}
      />
      <Button title="Analyze Risk" onPress={fetchRiskAnalysis} />
      <Text style={styles.result}>{response}</Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: "#fff" },
  title: { fontSize: 20, fontWeight: "bold", marginBottom: 10 },
  input: { borderWidth: 1, padding: 10, marginBottom: 10 },
  result: { marginTop: 10, fontSize: 16 }
});
