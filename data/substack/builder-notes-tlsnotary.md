# Builder notes : TLSNotary

**Nov 21, 2024**

---

Hey there ! This article will be a brain dump of what I learned by building with TLSNotary during this past ETH Global hackathon ✨

Took me one day and a half to finally notarize my first proof (probably skill issue) but still want to help new builders who want to try it out.

Spoilers : TLSNotary is not yet production ready (of course) - and if something doesn't work, it's probably not your fault. But ask questions on Discord, team is great & reactive. Also keep in mind, this article date from the 16th of July - so some advices might not be up-to-date when you read it.

## What's TLSNotary ?

It's an open-source protocol that can verify the authenticity of web data while protecting privacy. It's being built by Privacy & Scaling Explorations (PSE), which is an open-source research focused team funded by the Ethereum Foundation.

The protocol has first been proposed in 2013 on Bitcoin forums - and have been rebuilt with the latest cryptographic innovations we've seen in the last decade.

Basically the most obvious use-cases are proving you own an account, retrieving your bank account information (how many dollars you have) or showing you are KYC-ed on a platform.

I've been diving into Gen AI ecosystem for the past week - ComfyUI LoRA Stable Diffusion and all this stuff - so I know I wanted to hack around this during ETH Global. In my past life, I've been an artist - before the AI renaissance - and wanted to create a way to prove your art is not AI generated. I posted all my art on Instagram - so I felt like it's the best platform to build something on.

---

## Okay, so where do we start from ?

The documentation & the GitHub of TLSN.

It's really great to understand the protocol technically and how it discloses data. Be careful, docs and GitHub aren't really in sync - so try to double-check each time to find what's really up-to-date.

You can run the protocol in three different ways :

- Natively with Rust
- In the browser (React / Typescript)
- With a Chrome extension

If you happen to have some WASM knowledge, I think it's the best way to start building. I actually don't (might be time to learn), so I started with the React app.

The implementation is fairly simple :

```javascript
const p = await prove('https://swapi.dev/api/people/1', {
      method: 'GET',
      maxTranscriptSize: 16384,
      notaryUrl: 'http://localhost:7047',
      websocketProxyUrl: 'ws://localhost:55688',
    });
setProof(p);
```

Nevertheless, I would not recommend using this for the moment - as it does not support secret headers and secret body, meaning this is fairly useless. I also struggled to implement proofs that were working, oddly I had a regular size with the Chrome extension - and an abysmal difference with the React app.

After that, I tried using the TLSN Extension from the Chrome store. The extension is really well-designed and easy to use. Here is a walkthrough :

- **Requests** is where you see all network requests, you can click on them and see the headers, payload, response & notarize them.
- **Custom** is to make custom requests, a built-in Postman.
- **Verify** is to drop your proof, it's basically the explorer - but on the extension
- **History** show every attempt to notarize you made - and you can get some error info or download proofs.
- **Option** is to set up your Notary & Proxy API (Will talk about it later).

They have a good tutorial on the docs to notarize Twitter account access. Basically, you try to find a xmlhttprequest with a json - and look at the response. You can also inspect the website responses by using the network tab from Chrome DevTools.

I found out that most website don't have this at all - and it is sometimes tricky to get a valid response that provides useful information on the user. Some tips : check every xmlhttprequest and try some more static pages (parameters, for example). The response shouldn't be too big (max 200–300 lines) - so it's almost impossible to notarize main_frames (the plain HTML response). Trick is probably to retrieve only part of the website before trying to notarize - and then notarizing only a small part, but not sure if it's possible / if it's still secure.

---

## Setting up a Proxy

So at this step, you might try to notarize stuff with the extension. But if you are not notarizing something out of those websites, you probably also need a proxy :

```
api.twitter.com:443
twitter.com:443
gateway.reddit.com:443
reddit.com:443
swapi.dev:443
api.x.com:443
x.com:443
discord.com:443
connect.garmin.com:443
uber.com:443
riders.uber.com:443
m.uber.com:443
```

Hopefully, it is really easy to run, just change swapi.dev with the website you want to notarize, example : instagram.com. Then, use ws://localhost:55688 as the Proxy URL API.

```bash
git clone https://github.com/novnc/websockify && cd websockify
./docker/build.sh
docker run -it --rm -p 55688:80 novnc/websockify 80 swapi.dev:443
```

Just be careful, URL sometimes are tricky - and you should try a lot of different configurations : adding www before the domain, sometimes it's just api.x.com, ... - If something is not working, check 3 times all your URL configurations.

You might also want to run your own Notary Server, but it's not always required. It was useful for me, because the PSE hosted server was being bombed by requests during the hackathon. Each request took between 20 minutes and 1 hour to respond. It also allows you to customize the max size to more than 20.48kb, which can be useful for testing & production - and also add some server side logging.

Got a lot of issues trying to run it - we found out it's not working on WSL for Windows 11 (maybe other versions idk) - so run it on a Linux VM on AWS or your own device VM (open your ports if you use AWS ofc). If you already run your own proxy, no need to change anything - except turning off the TLS in the config. Keep in mind that there are multiple versions of the server - and some of them aren't working the same way. I used alpha.5 and it worked well.

---

## Building Plugins

Now that you have tested your set-up and saw that notarization works, you should migrate to the latest Chrome extension that add plugins.

You should be able to install it from there. It adds some cool debugging options, but more importantly, a way to import plugins.

You can also see my Instagram plugin here: https://github.com/aaronjmars/tlsn-plugin-instagram

You just gotta build them with Extism and import twitter_profile. It then gives you a way to customize the user experience, making sure he follows all the right step and enabling you to verify their set-up.

The two main files you are going to edit are index.js (or .ts) and config.json. The latter is used for the onboarding flow, and it should map exactly your index.js for the requests, functions, cookies & headers.

On the example, there are three main functions :

1. Validating & redirection of the host, making sure the user is on the right page and is signed-up
2. Retrieving the user headers & cookies to set up the right request
3. Crafting the request with all required headers, cookies, and secretHeaders

---

## Some stuff worth exploring :

- Forking the explorer to make the proofs more interactive and adding onchain validation (or attestations).
- Modifying the Chrome extension plugin to make it customizable around only one plugin - making it easy to build user facing applications for specific use-cases.
- Easy WASM-based website for crafting proofs.

Thanks for reading, please reach out on X / Twitter if anything is not correct or if you have any questions - have a great day <3
