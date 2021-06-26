## Testing the Markdown parser # {: #anid .aclass somekey='some value' }

[This should be a link](https://cxllm.xyz)

- This
- Is
- A
- List

| Table | Table | Table | Table | Table |
| ----- | ----- | ----- | ----- | ----- |
| Table | Table | Table | Table | Table |
| Table | Table | Table | Table | Table |

```js
//This is a code block with some boilerplate bot code
const { Client, Collection } = require("discord.js");
const { readdirSync } = require("fs");
const { join } = require("path");
const client = new Client();
const prefix = "!";
client.commands = new Collection();
client.aliases = new Collection();
readdirSync(join(__dirname, "commands"))
  .filter((file) => file.endsWith(".js"))
  .map((file) => {
    const command = require(`./commands/${file}`);
    client.commands.set(command.name, command);
    command.aliases.map((alias) => client.aliases.set(alias, command.name));
  });
client.on("ready", () => {
  console.log(
    `The client has connected to Discord's gateway as ${client.user.tag}`
  );
});
client.on("message", async (message) => {
  if (message.channel.type == "dm" || !message.author.bot) return;
  if (!message.content.startsWith(prefix)) return;
  const args = message.content.slice(prefix.length).split(" ");
  const command = args.shift().toLowerCase();
  const cmd =
    client.commands.get(command) ||
    client.commands.get(client.aliases.get(command));
  if (!cmd) return;
  cmd.run(client, message, args);
});
client.login("Your epic bot token here");
```
