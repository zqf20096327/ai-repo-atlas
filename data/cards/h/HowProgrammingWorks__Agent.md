# HowProgrammingWorks/Agent

⭐ 45 · JavaScript · MIT · 推送 2026-09-04 · [GitHub](https://github.com/HowProgrammingWorks/Agent) · 组织维护

**面向开发者的 Node.js 模块化编码 agent 参考实现**

展示编码 agent 核心循环的最小 harness：用户任务→模型响应→工具调用的循环不经框架封装直接可见。提供 read/write/edit/bash/grep/glob 等 11 种工具，LLM 客户端基于 OpenAI SDK，通过 BASE_URL 接入任意 OpenAI 兼容端点。包含终端 IDE（树、编辑器、shell、聊天）与安全机制：工作区文件访问限制（含 symlink 检查）、写出 git 仓库前交互确认、步数与输出截断限制。需 Node.js 20+ 与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 种工具（read/write/edit/bash/grep/glob/delete/patch/check/fetch/todo），各带 JSON 规格
- 任意 OpenAI 兼容端点接入，支持 MODEL 与 FALLBACK_MODELS 配置
- 工作区文件访问限制（symlink 感知）与写出仓库前的交互审批
- 自带终端 IDE（tree/editor/shell/chat）

## 适用场景

- 学习编码 agent 的核心循环与工具调用机制
- 在其上定制自己的工具或接入自选模型端点
- 作为最小可运行的 agentic coding 原型进行实验

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: > small, modular coding-agent harness for Node.js. It demonstrates the core loop behind agentic coding tools without
> L25: Tools are `read`, `write`, `edit`, `bash`, `grep`, `glob`, `delete`, `patch`, `check`, `fetch`, and `todo`. Specs l
> L37: - Any OpenAI-compatible provider via `BASE_URL` in `config.js`

## 星数曲线

```mermaid
xychart-beta
    title "HowProgrammingWorks/Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f1eb3f8484c1` · [字段定义](../../DATASET.md)*
