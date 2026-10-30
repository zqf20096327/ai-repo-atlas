# helioschat/app

⭐ 15 · TypeScript · MIT · 推送 2026-03-03 · [GitHub](https://github.com/helioschat/app) · [官网](https://heliosch.at) · 组织维护

**浏览器端运行的隐私优先 LLM 聊天客户端**

基于 SvelteKit 构建的 LLM 聊天客户端，为 T3 Chat Cloneathon 竞赛开发。所有聊天逻辑与数据存储均在浏览器本地完成，支持端到端加密的跨设备同步（凭口令、无需注册邮箱）、临时会话、消息编辑、会话置顶与分支、网页搜索集成。采用 BYOK 模式，兼容所有 OpenAI API 格式的模型提供方，用户填入自己的 API key 使用。安装方式为 git clone 源码后以 bun 安装依赖并运行开发服务器。项目自述为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 聊天逻辑与数据存储 100% 在浏览器客户端完成
- 端到端加密同步，凭口令使用、无需注册邮箱
- BYOK 模式，兼容所有 OpenAI API 兼容提供方
- 消息编辑、会话置顶、分支对话与临时会话

## 适用场景

- 在浏览器本地与各家 LLM 对话且数据不出本机
- 用自有 API key 跨设备加密同步聊天记录
- 快速发起不留痕的临时对话

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Helios is a blazing fast, privacy-first LLM chat client built for the T3 Chat Cloneathon. It is fully open source an
> L9: - **Bring Your Own Key (BYOK)**: Compatible with every OpenAI API-compatible provider. Use your own API keys for max

## 星数曲线

```mermaid
xychart-beta
    title "helioschat/app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ca5a311e5379` · [字段定义](../../DATASET.md)*
