# iyashjayesh/tokenchit

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/iyashjayesh/tokenchit) · [官网](https://tokenchit.app) · 个人维护

**读取本地 AI 编程代理日志并生成可提交到 README 的用量统计卡**

面向使用 AI 编程代理的开发者的 CLI 工具：检测本机的 Claude Code、Codex、OpenCode、Gemini CLI 日志，统计 token 用量与折算 API 费用，生成 SVG 统计卡提交到仓库 README，并提供年度回顾卡与跨机器历史合并（按 session 去重）。默认路径无网络上传，publish 为唯一上传命令，仅发送每日 token 汇总与句柄；另有 MCP server 供模型查询用量。限制：Copilot CLI 检测到但标记为不支持，Gemini 旧版本记录无法计数，回滚旧版本不安全。

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

- 检测 Claude Code/Codex/OpenCode/Gemini CLI 四种代理日志并统计 token 与折算费用
- 生成提交到仓库的 SVG 统计卡，非托管图片
- 本地路径无网络代码，由测试强制（net.isolated）
- 提供 MCP server（get_usage 等四个工具，禁止网络请求）

## 适用场景

- 在个人 README 中展示自己的 AI 编程代理用量统计
- 合并多台机器的代理使用历史
- 让模型通过 MCP 查询我的 token 用量

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L10: **Turn your local AI coding agent logs into a stat card you commit to your README.**
> L78: |agent|source|
> L169: There is an MCP server in `packages/mcp`, so a model can answer questions about your usage

## 星数曲线

```mermaid
xychart-beta
    title "iyashjayesh/tokenchit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6bbdf9010025` · [字段定义](../../DATASET.md)*
