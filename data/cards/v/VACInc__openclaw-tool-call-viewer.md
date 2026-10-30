# VACInc/openclaw-tool-call-viewer

⭐ 27 · HTML · MIT · 推送 2026-03-25 · [GitHub](https://github.com/VACInc/openclaw-tool-call-viewer) · 组织维护

**浏览 OpenClaw 会话工具调用历史的本地 Web UI**

零依赖的 Node.js Web 界面，动态解析 OpenClaw 的 JSONL 会话文件，列出工具调用记录。支持按工具类型、模型、会话、日期与文本过滤，列头排序，交叉过滤计数，10 秒轮询自动刷新，结果导出为 JSON；提供 REST API 端点（/api/tools、/api/stats）。默认读取 ~/.openclaw/agents/main/sessions，可自定义端口与会话目录。README 明确警告仅限本地网络使用，不得暴露公网。面向 OpenClaw 用户与开发者，git clone 后直接 node server.js 运行，无需 npm install。

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

- 动态解析 JSONL 会话文件，零依赖仅需 Node.js v18+
- 多维度过滤、排序与交叉过滤计数，10 秒轮询自动刷新
- 过滤结果导出 JSON，并提供 /api/tools、/api/stats REST 端点
- 支持 macOS launchd / Linux systemd 常驻运行

## 适用场景

- 回看 OpenClaw agent 会话中每个工具调用的参数与结果
- 按模型、工具类型或日期筛选排查 agent 行为
- 在局域网内用手机/平板查看工具调用统计

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A lightweight web UI for browsing OpenClaw session tool call history. Zero dependencies — just Node.js.
> L13: - **Dynamic parsing** of JSONL session files

## 星数曲线

```mermaid
xychart-beta
    title "VACInc/openclaw-tool-call-viewer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d9c4457dee58` · [字段定义](../../DATASET.md)*
