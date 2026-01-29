# Interoperability is magic: Wormhole vs Layer Zero vs Hyperlane

**Nov 21, 2024**

---

Web3 is the next evolution of the internet - emphasizing decentralization, trustlessness & user empowerment through the blockchain technology. We are in the midst of the third revolution of blockchains, with dozens of new L2 and L3 every week.

This revolution extends the need for interoperability, making the user experience more ubiquitous. Indeed, if I mint an NFT on a chain, I want to be able to use it on another chain - otherwise the blockchain experience becomes similar to Web2, with silos on every ecosystem.

Interoperability in Web3 refers to the ability of different blockchain networks and decentralized applications to seamlessly interact, share messages and execute transactions across one another. This capability is crucial for realizing the full potential of Web3 and fostering an interconnected, user-centric digital environment.

> "Interoperability is the future" — Vitalik Buterin.

---

This is where Arbitrary Messaging Bridges (AMB) come to play, enabling truly cross-chain experiences and interoperability of assets. It unlocks a lot of use-cases :

**Improved user-experience:** users don't need to bridge and acquire the right gas token, they can do anything from their favorite blockchain and get access to a fully abstracted environment.

**Better liquidity for assets:** token standard created by AMBs (OFTs e.g) make assets easier to transfer, enabling a better chain accounting & removing the need to lock assets as an LP.

**Enabling the money legos:** having the possibility to prove you own an asset on any chain enables to build smarter dApps, integrating NFTs into DeFi, unlocking new experiences based on your holdings or gating an access ONLY if you have the NFT.

Yet, we're still in the experimentation phase of AMBs - and we need to be cautious about their implementations. As a matter of fact, one of the leader of this category - Wormhole - has been exploited 2 years ago for $320M worth of assets.

Each protocol has different security standards, and which one is best always depends on the usage. Most of the risks can be summarized by this assessment made by the Uniswap research committee & cross chain risk framework :

- **Protocol Architecture Risk:** Encompasses the risks stemming from the design of a protocol, including its primary validation mechanism and other architecturally significant components.
- **Protocol Implementation Risk:** Includes the risks associated with the implementation of a protocol's specification.
- **Protocol Operational Risk:** Refers to the various risks that arise from the operational security and management of different components.
- **Network Risks:** Cross-chain protocols rely on certain assumptions about the safety and liveness guarantees of underlying networks.

To sum up, risks are mostly modeled around the trust model, upgradability of the protocol - and the environment it gets deployed around.

But security is a nuanced concept that depends on specific needs and circumstances. There isn't a one-size-fits-all solution; rather, security operates on a spectrum, with different measures appropriate for different situations. A one-size-fits-all approach to security often leads to applications either under or overpaying for security.

---

## Wormhole (Mutable - Shared security)

VAAs (Verifiable Action Approvals) are the core messaging primitive in Wormhole. You can think of them as packets of cross chain data that are emitted any time a cross chain application contract interacts with the Core Contract.

Each VAAs are observed and validated by Guardian Network - a 19/26 multisig - including many reputable entities. Both the number of validators and security thresholds are set at satisfactory levels, but doesn't involve slashing.

They have a Spy function, enabling easy recording of VAAs to enable off-chain accounting (SQL or other).

Relayers in the Wormhole context are processes that deliver VAAs to their destination, playing a crucial role in Wormhole's security model. They can't compromise security, only liveness, and act as delivery mechanisms for VAAs without the capacity to tamper with the outcome.

Their NTT token standard focuses on preserving ownership, upgradability and customizability through chains. Projects are also able to retain fine-grained control over their security, such as rate limits, pauses, access controls, and balance accounting.

Supports 25 blockchains across 6 different runtimes.

---

## Layer Zero (Immutable - Isolated security)

Layer Zero had some backlash due to their V1 architecture. With their V2 model, applications have complete control over security by adopting Modular Security principles.

They are effectively focusing on the transport layer, while creating a marketplace for the verification layer. Compatibility with non-EVM's is greatly increased.

Architecture is fairly simple, with Endpoint Contracts acting as entry point for cross chain messages and DVN being the verifier network for messages, with guaranteed instant finality for cross-chain transactions.

The protocol is also extendable, with adapters allowing applications to permissionlessly verify messages through third-party networks, native bridges, and middle chains.

DVN creation is permisionless, enabling modularity based on usage.

For use cases like low-cost NFT transfers, an application might set a 1/1/1 Security Stack - or even use a ZK light-client (Lagrange State Committee e.g).

CCIP & Axelar are also available as DVN Adapters.

Their Pre-Crime module functions as an advanced security layer, proactively scrutinizing transactions for potential threats or irregularities before they are executed.

Their token standard is the Omnichain Fungible Token (OFT) - it allows developers to extend the normal ERC20 token to record balances on any supported blockchain ledger. It's the most adopted token standard through AMBs, with over 100 projects.

This works by deploying an OFT contract on every blockchain you want to interact with, enabling you to debit a token from an address on one chain and credit it on the other. It's also compatible with different blockchains that utilize different underlying execution environments (e.g., EVM vs non-EVM).

With the OFT adapter, it allows for a quick multichain presence without overhauling the token's code - and is also available for NFTs (ERC721 or 1155).

Support 73 EVM blockchains and Solana.

---

## Hyperlane (Immutable - Isolated security)

Hyperlane uses "Inbox" and "Outbox" smart contracts to send and receive interchain messages. Every chain Hyperlane supports has one Outbox and n-1 Inboxes (one for every other chain).

Security's assumptions are similar to Layer Zero, with immutable contracts and a Modular Security architecture called ISM. It enables possibilities to create your own security stack, from a low-security 1-1 multisig to Wormhole or CCIP validation.

Anyone can permissionlessly deploy Hyperlane to any blockchain environment, whether it is a layer 1, roll-up, or app-chain, allowing that chain to communicate seamlessly with any other chain on which Hyperlane has been deployed. Block finality can also be customized to support every configuration.

They also have their own token standard, HypERC20 / HypERC721, similar to OFTs.

Interchain accounts allows interacting directly with another chain using an ownable CREATE2 contract, serving as a proxy for cross-chain calls.

Currently serving 16 chains - and can be permisionlessly deployed on new ones.

---

## Summary

To sum up, each protocol have their own strength and weaknesses.

- **Wormhole** is usually the most secure and customizable for token standards.
- **Layer Zero** is great for composability and speed - and boast a great ecosystem.
- **Hyperlane** is the most open and customizable, allowing for permisionless deployment to any chain.

I haven't covered CCIP, Axelar, Omni, ICP nor XCM on this article because I think it's out of scope, but they are interesting protocol and design choices as well.

Two interesting use-cases I've witnessed recently around AMBs have been Inco and Catalyst:

**Inco** leveraged Hyperlane to enable any dApp on any chain to use their smart-contract to provide confidentiality as a service. It's an interesting design pattern, because it makes Inco directly available to any available chain and any chain that will be deployed.

**Catalyst** is creating a General Automatic Relayer Payment, which is effectively a smart contract serving as an intermediary between applications and AMBs - the source-of-truth to define how relayers are paid based on the observed (and verified) messages delivered.
