# ninedter/llm-usage-tracker

⭐ 19 · TypeScript · 推送 2026-10-20 · [GitHub](https://github.com/ninedter/llm-usage-tracker) · 个人维护

**监测 Claude/OpenAI 订阅配额并追踪 agent 会话的自托管仪表盘**

以单个 Docker 容器运行的常驻服务：读取 Claude（claude.ai 会话或 Claude Code OAuth）与 Codex CLI 登录的官方用量端点显示订阅配额窗口；通过 hook 脚本捕获 Claude Code 全部 7 类事件、内置 watcher 追踪 Codex CLI rollout 日志与 Claude 转录（~/.claude/projects）派生 token 用量，数据落入 SQLite 并经 SSE 实时推送到浏览器 UI。多机器以边缘节点上报同一 hub。本地存储、凭据 AES-256-GCM 加密、无遥测；订阅制下成本记为 $0，按 token 量排名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取官方端点的 Claude 5 小时/7 天与 Codex 配额监测（不消耗 API key）
- Claude Code 7 类 hook 事件 + Codex 日志 + 转录 token 双源核算，SSE 实时推送
- 活动/工具/文件/模型多维分析，含 90 天历史回填与 idempotent 摄取
- 单容器多浏览器架构，边缘机器批量上报 hub，数据全本地（SQLite 卷）

## 适用场景

- 实时查看 Claude 与 OpenAI 订阅配额的消耗与重置
- 追踪 Claude Code / Codex agent 会话的工具调用、文件改动与 token 用量
- 多台开发机汇总到一个 hub 统一分析 AI 使用情况

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: An always-on Docker application, opened in any browser, that monitors your AI subscription quotas (Claude, OpenAI/Co
> L20: **Agent activity tracking.** A tiny hook script forwards every Claude Code lifecycle event (all 7 hook types) to th

## 星数曲线

```mermaid
xychart-beta
    title "ninedter/llm-usage-tracker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f861f4b5d823` · [字段定义](../../DATASET.md)*
