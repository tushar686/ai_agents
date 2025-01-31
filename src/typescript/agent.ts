import ollama from 'ollama'
import readLine  from "readline"


const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
})

const messages = [] as any;

async function send_to_llm(content: string) {
    messages.push({
        role: "user",
        content: content
    });

    const response = await ollama.chat({ model: 'llama3.2', messages: messages, stream: false })

    // messages.push(response.message.content);

    return response;
}

async function main() {
    while(true) {
        const input: string = await new Promise((resolve)=>{
            rl.question("Say something: ", resolve);
        });

        const response = await send_to_llm(input);
        console.log(response);
        console.log();
        console.log(response.message.content);
    }
    
    
    
}

main()
