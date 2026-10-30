# l497996153/AI-RPG-Engine

⭐ 19 · Python · MIT · 推送 2026-03-27 · [GitHub](https://github.com/l497996153/AI-RPG-Engine) · 个人维护 · 中文 README

**LLM 驱动的模块化 RPG 引擎：跑团与视觉小说主持**

基于 FastAPI 后端与 Web 前端的 AI 角色扮演引擎，用 LLM 主持任意桌面 RPG（TTRPG）。规则、属性、骰子与提示词均由模块（module.json/content.md/prompts.md）定义，前端按后端 schema 动态渲染；因完全 schema 驱动，改模块即可变为视觉小说/Galgame 引擎。内置 RAG 一致性记忆，提供房间制 API（创建/验证/聊天/掷骰/重启），内置 CoC 7e 与 D&D 5e 两个模块，另有可在线游玩的 Demo。需配置 Gemini 或 Groq API key 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- schema 驱动模块系统：module.json 定义规则/属性/骰子，前端动态渲染
- RAG 一致性记忆保持剧情连贯
- 改模块即可切换为视觉小说/Galgame 引擎
- 房间制 REST API：创建/重连/聊天/掷骰/重启，内置 CoC 7e 与 D&D 5e 模块

## 适用场景

- 单人游玩 AI 主持的克苏鲁或 D&D 冒险
- 通过自定义模块跑任意规则的桌面 RPG
- 把引擎改造成视觉小说/Galgame 引擎

## 场景标签

 · 领域:游戏/AI 叙事

## 证据(README 行号)

> L5: A modular AI-driven RPG engine powered by LLMs, featuring RAG-based consistent memory
> L7: Designed to support **any Tabletop RPG** — stats, attributes, prompts, and game mechanics are defined per-module, an
> L11: Because the engine is entirely **schema-driven**, it is not limited to traditional tabletop RPGs. By simply modifyi

## 星数曲线

```mermaid
xychart-beta
    title "l497996153/AI-RPG-Engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `1fdde2d301e2` · [字段定义](../../DATASET.md)*
