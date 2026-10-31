# Unmortan-Ellary/Vascura-FRONT

⭐ 23 · HTML · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Unmortan-Ellary/Vascura-FRONT) · 个人维护

**单 HTML 文件的无依赖 LLM 聊天前端**

以单个约 500KB 的 HTML 文件在浏览器中运行的 LLM 前端，无需 Python 或 Node.js。通过 OpenAI 兼容 API 连接任意后端（LM Studio、Kobold.Cpp、Llama.Cpp Server、Text Generation WebUI 等），Strict API 模式下支持 Mistral、OpenRouter 等 v1 端点。功能包括即时文本编辑、React 多回复生成、9 个网页搜索 agent（压缩进 4K token 上下文）、Lorebook 动态注入（文本/宏/图片）、宏引擎（变量、条件、LLM 子请求链）、VAR 快照存档系统与 LLM 主动对话。附 Character Card 转换工具，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 HTML 文件运行，无 Python/Node.js 依赖
- 9 个网页搜索 agent，搜索结果压缩进 4K token 上下文
- Lorebook 动态注入文本、宏脚本与图片作为内部记忆
- 宏引擎支持变量、条件逻辑与可嵌套的 LLM 子请求链

## 适用场景

- 在浏览器中连接 LM Studio/Llama.cpp 等本地后端进行 LLM 对话
- 用 Lorebook 与宏引擎构建带变量和状态快照的角色扮演/RPG 场景
- 对比与重新生成同一条 LLM 回复，编辑任意位置的对话文本

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L6: - **Dependency-Free:** No downloads, no Python, no Node.js - just a single compact (500~ kb) HTML file that runs in 
> L11: - **OpenAI-compatible API:** The most widely supported standard, chat-completion format.

## 星数曲线

```mermaid
xychart-beta
    title "Unmortan-Ellary/Vascura-FRONT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c4068cea757f` · [字段定义](../../DATASET.md)*
