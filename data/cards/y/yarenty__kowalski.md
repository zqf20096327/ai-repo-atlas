# yarenty/kowalski

⭐ 66 · Rust · MIT · 推送 2026-10-28 · [GitHub](https://github.com/yarenty/kowalski) · 个人维护

**Rust 单二进制多智能体框架：本地 Ollama/OpenAI 端点上跑带 MCP 工具的 agent 流水线**

一个 Rust 编写的单二进制多智能体框架，内置 Web UI 与 HTTP API。'horde' 是以 Markdown 定义的分步流水线，支持 cron 定时、文件落地与 webhook 三种触发器；agent 配备 MCP 工具与记忆，模型走本地 Ollama 或任意 OpenAI 兼容端点。内置五个 horde：电子表格分析（经 tableski 把工作簿转 SQL 表）、晨报、文件夹监视、URL 摘要、知识编译。运行状态持久化到 SQLite，确定性步骤（取数、跑 SQL、生成工作簿）由代码完成，小模型只需写查询或段落。安装提供 macOS dmg 与 curl 安装脚本，亦可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- horde 为 Markdown 文件夹定义的流水线，支持 cron/watch/webhook 触发并以 .kwf.zip 打包迁移
- 经 tableski 将 Excel/CSV/Parquet 转为 SQL 表供模型查询
- 任意 MCP 工具接入，运行状态持久化到 SQLite 且可跨重启存活
- 确定性步骤交由代码执行，本地小模型即可承担

## 适用场景

- 用自然语言向电子表格提问并得到报告工作簿
- 定时抓取常看网页生成每日晨报
- 监视文件夹中的文档并产出要点与待办笔记
- 自建带 MCP 工具与记忆的 agent 流水线并打包分发

## 场景标签

`Agent 框架` `多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L111: A horde is a folder of Markdown: `horde.md` (the pipeline and its triggers), `agents/*.md` (one
> L121: One process holds the operator UI, the HTTP API, the horde runner and the agent core. Runs are

## 星数曲线

```mermaid
xychart-beta
    title "yarenty/kowalski 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-28 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `78d69b34e795` · [字段定义](../../DATASET.md)*
