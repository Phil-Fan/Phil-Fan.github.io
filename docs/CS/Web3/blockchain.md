# 以太坊区块链基础
[一文读懂区块链技术](https://blog.chain.link/what-is-blockchain-zh/)

[以太坊基础 - 鹤翔万里的笔记本](https://note.tonycrane.cc/ctf/blockchain/eth/basic/)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240713192452.png)

两种账户：EOA

有一对公私钥，用于签署交易
- 私钥是随机生成的 256 位数（32 字节）
- 公钥由私钥经过 ECDSA 算法计算而来，是一个 64 字节的数
- 地址由公钥经过 Keccak-256 哈希后取前 20 字节得到

```
> personal.unlockAccount(eth.accounts[0],"GEIC&UJMeOy12m#Q")
true
> personal.sendTransaction({from:eth.accounts[0],to:"0xb3bc02f0b64ab21e34ad594ebc3f1418d6225b85",value:web3.toWei(0.5,"ether"),gas:21000,gasPrice: web3.toWei(1, "gwei")},"GEIC&UJMeOy12m#Q")
```