# real-Elysia886/inkflow

⭐ 37 · Python · MIT · 推送 2026-05-21 · [GitHub](https://github.com/real-Elysia886/inkflow) · 个人维护 · 中文 README

**多智能体协同的长篇小说创作引擎，面向小说作者**

基于 LLM 的长篇小说创作引擎，通过 7 个专职 Agent（战略师、大纲师、编排师、写手、编辑、观察者、图书管理员等）组成管线协作创作。以“真相文件”系统持久化角色档案、关系图谱、伏笔池、资源账本与信息边界，作为长程一致性的事实来源。提供代码层+LLM 层双层审计、去 AI 味检测、文风蒸馏与融合，以及全自动多章生成模式。技术栈为 Python/FastAPI/WebSocket，提供 Glassmorphism Web UI 与 Docker 部署。需用户自行配置 LLM Provider 与 API Key（如 OpenAI、DeepSeek），支持为不同 Agent 角色路由不同模型与温度参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个专职 Agent 组成的标准化创作管线
- 真相文件系统持久化角色档案、伏笔池、关系图谱与信息边界
- 代码层（零 Token）+ LLM 层双层质量审计与自动重写
- 文风蒸馏：上传样章生成 5 种定制 Agent Skill，支持多书风格融合

## 适用场景

- 长篇连载小说保持角色、伏笔与世界观的前后一致
- 上传样章克隆特定文风后自动生成章节
- 通过 Web UI 实时监控多 Agent 创作进度并一键重写

## 场景标签

`多智能体` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L6:  多智能体协同的小说创作引擎：让长篇创作重获连贯与灵魂
> L29: ### 1. 7-Agent 协同管线 (The Pipeline)

## 星数曲线

```mermaid
xychart-beta
    title "real-Elysia886/inkflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `81e002acf502` · [字段定义](../../DATASET.md)*
