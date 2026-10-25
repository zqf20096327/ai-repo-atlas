# s-nagaev/chibi

⭐ 55 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/s-nagaev/chibi) · [官网](https://chibi.bot) · 个人维护 · 中文 README

**自托管的 Telegram AI 伴侣机器人，编排多家模型提供商与工具**

自托管、异步运行的 Telegram 机器人，以对话为入口编排多个 AI 提供商、工具与子代理，产出代码修改、研究综合、媒体生成等结果。支持十余家第一方 LLM 提供商、多家推理聚合商及 Ollama/vLLM 等本地端点，具备递归子代理委派、后台异步任务、文件系统与终端访问、MCP 工具集成、持久化记忆与内置技能机制，并可生成图像、视频、音乐与语音。通过 pip 安装为 CLI 后台服务，或用 Docker Compose 部署；各提供商需自备 API key，提供用户/群组白名单与终端执行审核等安全配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一会话内多提供商编排，可按任务路由并中途切换模型
- 递归子代理委派与后台异步任务执行
- MCP 工具集成（GitHub、浏览器自动化、Docker、数据库、Blender/Figma 等）
- 支持图像/视频/音乐/语音生成，及 Ollama/vLLM 等本地 OpenAI 兼容端点

## 适用场景

- 在 Telegram 里让子代理并行跑测试并修复代码
- 让多个研究代理汇总资料并按期交付综合报告
- 自托管一个统一入口调用各家模型与创意生成工具
- 团队用它审查 PR 并通过 MCP 更新文档

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L27: **Chibi** is an asynchronous, self-hosted **Telegram-based digital companion** that orchestrates multiple AI provid
> L33: - **Autonomous execution.** Sub-agents work in parallel; long tasks run asynchronously.
> L45: - **Alibaba Cloud** (Qwen)

## 星数曲线

```mermaid
xychart-beta
    title "s-nagaev/chibi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-25 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bb44b3a4bd70` · [字段定义](../../DATASET.md)*
