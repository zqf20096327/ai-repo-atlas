# aicayzer/companies-house-mcp

⭐ 13 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/aicayzer/companies-house-mcp) · [官网](https://companies-house.uk) · 个人维护

**英国 Companies House 公共登记册的 CLI 与 MCP 服务器**

非官方的 TypeScript 工具，包含 npm CLI（ch 命令）与 MCP 服务器两种形态，读取英国 Companies House 公共登记册：公司搜索与档案、高管任职与禁止任职记录、实益所有人（PSC）、申报历史与 PDF 文件下载，并提供一次性汇总报告与尽调筛查命令。全部请求经用户自己的免费 API key 直连官方 API，无托管后端、无遥测，客户端在 600 请求/5 分钟限额内排队。README 明确声明筛查结果不构成核实或信用/制裁审查结论。

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

- CLI 与 MCP 双形态，支持 Claude Code、Cursor、Codex、Zed 等客户端
- 公司搜索/档案/高管/实益所有权/申报文件全链路读取
- due_diligence_check 一次性筛查汇总，并声明其检查边界
- API key 仅本地存储（owner-only 权限），无遥测，限速内自动排队

## 适用场景

- 在 AI 助手中查询英国公司的登记信息与申报文件
- 用终端命令批量拉取公司档案与尽调初筛
- 自部署 Cloudflare Worker 供远程客户端访问

## 场景标签

 · 领域:公共数据访问/MCP 工具

## 证据(README 行号)

> L7: Read the UK Companies House public register from your terminal, your scripts, or an AI assistant. Search companies, 
> L15: **In an AI assistant** — Claude Code, Claude Desktop, Codex, Cursor, Zed:

## 星数曲线

```mermaid
xychart-beta
    title "aicayzer/companies-house-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b9ea8ea2d6a4` · [字段定义](../../DATASET.md)*
