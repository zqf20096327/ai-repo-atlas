# badchars/osint-mcp-server

⭐ 62 · TypeScript · MIT · 推送 2026-03-17 · [GitHub](https://github.com/badchars/osint-mcp-server) · [官网](https://github.com/badchars/osint-mcp) · 个人维护

**为 AI agent 提供 37 个 OSINT 工具的统一 MCP 服务器**

通过 Model Context Protocol 向 AI agent 暴露 37 个 OSINT 与侦察工具，覆盖 12 个数据源：DNS、RDAP/WHOIS、crt.sh、Shodan、VirusTotal、SecurityTrails、Censys、GeoIP、BGP、Wayback Machine、HackerTarget 与 Microsoft 365。其中 21 个工具无需 API key 即可使用，16 个付费源工具通过可选环境变量启用。实现上采用每源独立限流器、TTL 缓存与 Promise.allSettled 并行查询，仅依赖 @modelcontextprotocol/sdk 与 zod。支持 npx 一条命令运行，亦可接入 Claude Code、Claude Desktop、Cursor 等 MCP 客户端，并提供 GitHub Actions 与 CLI 用法。免费层存在速率限制（如 HackerTarget 50 次/天）。

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

- 37 个工具覆盖 12 个 OSINT 数据源，21 个免费无需 API key
- osint_domain_recon 并行调用 8 个源，单源超时不影响其余返回
- 每源独立限流器与 TTL 缓存，缺失 key 时优雅降级
- SPF 递归链解析含环检测与 RFC 7208 查询上限检查

## 适用场景

- 渗透测试或漏洞赏金前让 AI agent 做目标侦察
- 对域名/资产做攻击面映射与子域名枚举
- 审计目标域名的邮件安全配置（SPF/DMARC/DKIM）
- 在 CI/CD 流水线中以 GitHub Actions 调用 OSINT 工具

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L27:  OSINT & reconnaissance intelligence for AI agents.
> L63: **osint-mcp-server** gives your AI agent 37 tools across 12 data sources via the Model Context Protocol. The agent 
> L376: - **2 dependencies** &mdash; `@modelcontextprotocol/sdk` and `zod`. All HTTP via native `fetch`. All DNS via `node


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `09b05e01a4b6` · [字段定义](../../DATASET.md)*
