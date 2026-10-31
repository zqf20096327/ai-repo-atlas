# TheSolaAI/sola-application

⭐ 53 · TypeScript · GPL-3.0 · 推送 2025-12-11 · [GitHub](https://github.com/TheSolaAI/sola-application) · [官网](https://beta.solaai.xyz/) · 组织维护

**面向 Solana 区块链的语音 AI 助手应用**

基于 WebRTC 的语音/文字 AI 助手，接入 OpenAI 做自然语言处理，并对接 Solana 链上数据与交互。采用微服务架构：Next.js 前端、Rust 编写的数据服务（按用户查询过滤链上与网络数据）、钱包服务（构建预定义交易）、用户服务（聊天室与设置管理）。工作流为语音/文字输入→数据获取→交易构建→嵌入式或自定义钱包执行→语音/文字回复。安装方式为克隆仓库、yarn install 配置 .env 后 yarn dev 运行，GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebRTC 实时语音与文字通信
- Rust 微服务过滤与结构化 Solana 链上数据
- 支持链上交互（转账、兑换）与嵌入式/自定义钱包执行
- 集成 OpenAI 做自然语言处理

## 适用场景

- 用语音查询 Solana 区块链数据
- 通过对话完成链上转账与兑换操作
- 以免手方式管理区块链交互

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: Sola AI is a personalized AI voice assistant that bridges Solana blockchain technology and AI through a hands-free u
> L22:  * Interfaces with OpenAI for natural language processing.

## 星数曲线

```mermaid
xychart-beta
    title "TheSolaAI/sola-application 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-31 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `187d5ef1826d` · [字段定义](../../DATASET.md)*
