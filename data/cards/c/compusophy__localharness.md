# compusophy/localharness

⭐ 12 · Rust · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/compusophy/localharness) · [官网](https://localharness.xyz) · 个人维护

**让开发者构建自带钱包与链上身份的自主 agent 的 Rust SDK**

一个 Rust crate，兼具 agent SDK 与自主托管 agent 运行时：提供流式工具调用循环、hooks、策略、triggers、MCP 与上下文压缩，模型后端经统一 Connection 接缝可切换。可选 wallet 特性为每个 agent 生成设备本地 secp256k1/BIP-39 钱包与链上 NFT 身份，agent 之间以 $LH 信用按调用互相结算，且可编译到浏览器（wasm32）运行。目标用户是希望在浏览器或自有二进制中运行无中间服务器 agent 的开发者。限制：Pre-1.0 存在破坏性变更，iOS 首次身份创建受限，浏览器 Gemma 后端为重型可选功能且尚未完全验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 crate 提供 agent 循环：流式输出、工具调用、hooks、策略、triggers、MCP、上下文压缩
- Gemini/Anthropic/OpenAI/Mock 后端经单一 Connection 接缝切换，模型无关
- wallet 特性提供链上身份、$LH 信用结算与 x402 付费调用
- 同一源码编译为原生二进制与浏览器 wasm 版本

## 适用场景

- 为应用嵌入支持多模型切换的 agent SDK
- 创建可在链上被其他 agent 发现并付费调用的自主 agent
- 在浏览器中运行由 ACP 编辑器（Zed/JetBrains）驱动的 agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agents that own themselves. **One Rust crate** that is both an agent SDK and a
> L22: It is also, plainly, a good agent SDK. `cargo add localharness` gives you a
> L108: - **One crate, not a workspace.** `cargo add localharness` is the whole SDK. Optional

## 星数曲线

```mermaid
xychart-beta
    title "compusophy/localharness 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-14", "2026-11-26"]
    y-axis "stars" 10 --> 13
    line [11, 12, 12]
```

2026-11-02 11 → 2026-11-26 12（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `cb50af97f624` · [字段定义](../../DATASET.md)*
