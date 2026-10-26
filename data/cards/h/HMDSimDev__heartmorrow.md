# HMDSimDev/heartmorrow

⭐ 182 · TypeScript · Unlicense · 推送 2026-08-18 · [GitHub](https://github.com/HMDSimDev/heartmorrow) · [官网](https://heartmorrow.com/) · 组织维护

**本地优先的 AI 约会模拟游戏：用自有语言模型扮演角色谈恋爱**

在浏览器中运行的恋爱+世界模拟游戏：玩家构建角色阵容与世界，与角色进行流式对话约会、用游戏内手机发短信（支持视觉模型读图）、玩小游戏、送礼物，关系沿七维度演化，含分手、复合、纪念日等机制。全部在本地运行：浏览器连接小型本地服务器，服务器再接入任意 OpenAI 兼容端点（LM Studio、Ollama、llama.cpp、vLLM 等）或带 API key 的 Anthropic。未连接模型也可创建角色、上传立绘并浏览 UI，但对话与世界模拟需要模型运行。面向玩家，提供 Discord 社区。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Unlicense |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式角色扮演对话，模型保持角色一致性
- 支持任意 OpenAI 兼容端点及 LM Studio/Ollama/KoboldCpp 原生连接
- 七维度关系系统与社交图谱：八卦传播、嫉妒、纪念日记忆
- 游戏内手机含 Messages/Faces 社交动态/Almanac 等 10+ 应用与 9 个小游戏

## 适用场景

- 用本地模型玩角色扮演恋爱模拟，数据不出本机
- 创作角色与世界并让模型即兴演绎关系走向
- 通过游戏内手机与角色短信互动、送礼物、经营社交圈

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: # Heartmorrow — Local-First AI-Powered Dating Simulator 💞
> L5: Heartmorrow is a fully local dating + world simulator powered by **your own** language
> L11: Everything runs on your machine. The browser **never** talks to the model — it talks to a

## 星数曲线

```mermaid
xychart-beta
    title "HMDSimDev/heartmorrow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 181 --> 183
    line [182, 182]
```

2026-10-18 182 → 2026-10-26 182（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8ffed4313178` · [字段定义](../../DATASET.md)*
