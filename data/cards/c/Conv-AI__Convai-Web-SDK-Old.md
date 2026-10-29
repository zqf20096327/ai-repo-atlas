# Conv-AI/Convai-Web-SDK-Old

⭐ 20 · JavaScript · 推送 2026-09-16 · [GitHub](https://github.com/Conv-AI/Convai-Web-SDK-Old) · [官网](https://www.convai.com/) · 组织维护

**在网页中接入 Convai 数字角色对话的 TypeScript SDK**

Convai 官方提供的 Web SDK，用于在浏览器应用中集成数字角色：通过 ConvaiClient 初始化（apiKey、characterId），实现实时对话、动作与面部表情数据传输，面部表情需设置 enableFacialData 为 true。示例采用 TypeScript 绑定，README 附带 NPC 世界（React Three Fiber）与 Reallusion 角色实时口型同步的参考项目链接。以 npm 包 convai-web-sdk 分发，需要 Convai 账号的 API key 与角色 ID 才能使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ConvaiClient 初始化后与角色进行实时对话
- enableFacialData 标志启用面部表情数据
- 提供 NPC 世界（React Three Fiber）与 Reallusion 口型同步参考项目
- 以 npm 包 convai-web-sdk 分发，附 TypeScript 绑定示例

## 适用场景

- 在 Web 应用中嵌入可实时对话的 NPC 或虚拟助手
- 为 Reallusion 等虚拟形象添加实时口型同步
- 在 React Three Fiber 场景中搭建 Convai NPC 交互世界

## 场景标签

`聊天机器人` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L8: import { ConvaiClient } from 'convai-web-sdk';
> L19: convaiClient.current = new ConvaiClient({

## 星数曲线

```mermaid
xychart-beta
    title "Conv-AI/Convai-Web-SDK-Old 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fa8026da0e39` · [字段定义](../../DATASET.md)*
