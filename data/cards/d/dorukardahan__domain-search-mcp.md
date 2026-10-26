# dorukardahan/domain-search-mcp

⭐ 28 · TypeScript · MIT · 推送 2026-10-05 · [GitHub](https://github.com/dorukardahan/domain-search-mcp) · [官网](https://www.npmjs.com/package/domain-search-mcp) · 个人维护

**零配置域名可用性查询与命名评分 MCP 服务器**

基于 Model Context Protocol 的域名查询服务器，供 Claude Desktop、ChatGPT、Cursor、VS Code 等 MCP 客户端调用。核心功能：跨 500+ TLD 的域名可用性检查（RDAP→GoDaddy→WHOIS 三级回退链）、批量查询、溢价/拍卖域名检测、社交用户名与 npm 包名可用性检查、基于微调 Qwen 7B-DPO 的命名生成与 anti-slop 评分排名（name_project 两阶段命名引擎）。定价功能需自建后端或配置 Porkbun/Namecheap 密钥。支持 stdio 与 HTTP/SSE 双传输，提供 npx 直接运行与源码构建两种安装方式。

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

- RDAP→GoDaddy→WHOIS 零配置可用性回退链
- 两阶段命名引擎：生成指令 + anti-slop 评分排名与可用性核验
- 微调 Qwen 7B-DPO 命名生成，可指向自建 llama.cpp/Qwen 推理端点
- stdio 与 HTTP/SSE 双传输，含 OpenAPI 规范与 Prometheus /metrics 端点

## 适用场景

- 为项目命名时批量核验域名、社交用户名与 npm 包名是否可用
- 让 Claude/ChatGPT 等 MCP 客户端直接调用域名查询工具
- 扫描 Sedo 拍卖与到期域名寻找投资标的

## 场景标签

 · 领域:开发工具/域名服务

## 证据(README 行号)

> L11: **Naming engine with availability intelligence** — an MCP server that scores the names your model generates and run
> L19: Built on the Model Context Protocol for Claude, Codex, VS Code, Cursor, Cline, and other MCP-compatible clients.
> L162: All 12 tools listed below are exposed to MCP clients by default. The 6-tool

## 星数曲线

```mermaid
xychart-beta
    title "dorukardahan/domain-search-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9df4ca3cc22f` · [字段定义](../../DATASET.md)*
