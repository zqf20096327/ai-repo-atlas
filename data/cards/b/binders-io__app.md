# binders-io/app

⭐ 24 · Swift · GPL-3.0 · 推送 2026-10-25 · [GitHub](https://github.com/binders-io/app) · [官网](https://binders.io) · 组织维护

**macOS 本地优先的听写、会议纪要与个人记忆应用，附 MCP 服务器**

面向 Mac 用户的本地优先笔记与记忆应用：按 fn 任意应用听写、录音生成含负责人与行动项的会议纪要、全天语音与写作捕获、消息中的承诺转为待办；笔记/会议/消息索引为知识图谱，可自然语言提问并给出出处。语音经 Neural Engine 上的 Parakeet/Whisper 本地转录，语言功能默认用 Ollama（或 MLX 内置、任一 OpenAI 兼容服务器）。数据存于本地文件，支持通过同步盘共享文件夹协作，内置 MCP 服务器供 Claude Code 等 AI 工具访问知识库与看板。需 macOS 14.2+，AI 功能依赖本地模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意应用内 fn 键听写，Neural Engine 上 Parakeet/Whisper 本地转录
- 会议纪要自动产出摘要、决策与带负责人的行动项
- 笔记/会议/消息构建知识图谱，可按语义检索并带出处问答
- 内置 MCP 服务器，Claude Code/Desktop 等 AI 工具可检索知识库并协作看板

## 适用场景

- 在任意 Mac 应用里用语音输入并自动清理口语
- 开会录音后自动得到会议纪要与分派给各负责人的待办
- 把工作中散落的会议、笔记、消息汇成可问答的个人记忆
- 让 Claude 等 AI 工具经 MCP 读取自己的知识库并代办看板任务

## 场景标签

`知识库管理` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L5: Binders is a free Mac app that turns what you say, what you hear in meetings and what you write into notes, to-dos a
> L74: - Speech is transcribed on the Neural Engine with Parakeet or Whisper. Audio is never uploaded.
> L66:  lets Claude Code, Claude Desktop and other AI tools search and ask your knowledge base and work from your boards, 

## 星数曲线

```mermaid
xychart-beta
    title "binders-io/app 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `61ae441b349e` · [字段定义](../../DATASET.md)*
