# zjunlp/OneDayAgent

⭐ 37 · HTML · MIT · 推送 2026-08-15 · [GitHub](https://github.com/zjunlp/OneDayAgent) · 组织维护 · 中文 README

**长时程自主 agent harness：分解多小时任务并验证修复产出**

面向开放式日常请求（如调研主题、制作幻灯片、交付报告）的长时程 agent 执行框架。核心机制为三项：将过载请求拆分为有界子任务、LLM 验证器对交付物做全局校验与定向修复、把工具观察压缩为可复用的执行记忆并做子任务检查点。可运行于任意 OpenAI 兼容 LLM 后端，在 AgentIF-OneDay 基准（104 任务）上跨 3 个模型家族的 5 个后端进行了评测。官方推荐以预构建 Docker 镜像运行，手动搭建需大量系统依赖（Playwright、LibreOffice、ffmpeg 等），并需在 .env 配置各模型与工具 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任务分解：将多小时的过载请求拆为有界子任务，保留全局意图
- 全局验证与修复：LLM 验证器核对交付物并触发定向修复循环
- 执行记忆：即时摘要压缩工具观察并检查点化子任务状态
- 同一 harness 跨 5 个模型（GLM/Gemini/DeepSeek）运行，无需改架构

## 适用场景

- 让 agent 执行跨环境、多模态的数小时长时程任务
- 在 AgentIF-OneDay 基准上评测长时程 agent 表现
- 研究上下文压力下子任务分解与验证修复机制

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L10: **OneDayAgent** is a long-horizon agent harness that turns open-ended everyday requests into a managed execution pr
> L38:  OneDayAgent uses a long-horizon harness that decomposes an everyday task, executes subtasks through environment-gr
> L42: ## Main Results

## 星数曲线

```mermaid
xychart-beta
    title "zjunlp/OneDayAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1cce5efcc82e` · [字段定义](../../DATASET.md)*
