import { GoogleGenerativeAI } from "@google/generative-ai";
import * as dotenv from "dotenv";

dotenv.config();

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  throw new Error("GEMINI_API_KEY not found in environment");
}

const genAI = new GoogleGenerativeAI(apiKey);

async function main() {
  const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });
  const result = await model.generateContent(
    "What is a neural network in one sentence?"
  );
  console.log(result.response.text());
}

main();