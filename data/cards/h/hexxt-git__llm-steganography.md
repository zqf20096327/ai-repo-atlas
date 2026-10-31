# hexxt-git/llm-steganography

⭐ 14 · TypeScript · 推送 2026-03-20 · [GitHub](https://github.com/hexxt-git/llm-steganography) · 个人维护

**利用 LLM 生成时的 token 选择把秘密信息隐藏进普通文本**

基于 Bun 与 node-llama-cpp 运行本地 GGUF 模型的隐写术工具：不加密文本，而是把 UTF-8 载荷（32 位长度头 + 每字节 8 位）编码进模型生成时非主导步的 token 选择中——每 token 通过在两个最可能的非 EOG 候选间选择编码 1 bit。持有相同模型、tokenizer 与 prompt 的一方重放生成即可恢复比特并读出消息。README 声明为实验性：容量低，解密必须接收 encrypt 返回的原始 completionText 以保持 tokenization 对齐。提供 CLI（commander）与 PATH 上的二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 载荷编码在生成时的 token 选择中，输出读起来仍是正常回答
- 每 token 编码 1 bit：在两个最可能非 EOG 候选间选择
- 解密方需相同模型、tokenizer 与 prompt 重放生成
- 提供 encrypt/decrypt CLI 与 PATH 二进制

## 适用场景

- 在 LLM 生成的普通文本中隐藏短消息做隐蔽通信
- 研究 token 级隐写机制的实验原型
- 验证相同模型下隐藏数据的可恢复性

## 场景标签

 · 领域:密码学/隐写术

## 证据(README 行号)

> L3: **Goal:** hide a short secret message inside normal-looking plaintext using LLM output. The text itself is not encry
> L7: **Why it matters:** the output still reads like a normal response, while the hidden data is carried by small token-l

## 星数曲线

```mermaid
xychart-beta
    title "hexxt-git/llm-steganography 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2a2740aea9bb` · [字段定义](../../DATASET.md)*
