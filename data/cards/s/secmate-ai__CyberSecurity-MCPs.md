# secmate-ai/CyberSecurity-MCPs

⭐ 17 · JavaScript · 推送 2026-02-04 · [GitHub](https://github.com/secmate-ai/CyberSecurity-MCPs) · 组织维护 · 中文 README

**面向网络安全领域的 9 个 MCP 服务器集合，供 AI 助手调用**

收集与开发网络安全相关 MCP Server 的合集项目，每个实现独立封装在各自目录。包含 9 个实现：sqlmap-mcp（SQL注入扫描）、quake-server（360 Quake 网络空间搜索）、doc-processor（Markdown 转 Word）、threat-intel-mcp（集成 VirusTotal/AbuseIPDB/Shodan）、hash-analyzer-mcp、ssl-analyzer-mcp、cve-lookup-mcp（NVD 漏洞查询）、encryption-mcp（17 种加密编码）、cipher-identifier-mcp（密码识别与自动解密）。基于 TypeScript 开发，通过 npm 安装构建，可在 Claude Desktop 中配置使用，部分实现需外部 API 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个独立封装的网络安全 MCP Server（TypeScript）
- threat-intel-mcp 整合 VirusTotal/AbuseIPDB/Shodan 三大平台 8 个工具
- encryption-mcp 支持 17 种加密与编码方式
- 支持 MCP Inspector Web 界面调试

## 适用场景

- 在 Claude Desktop 等 MCP 客户端中接入安全测试与情报查询工具
- 自动化 SQL 注入扫描与 SSL/TLS 配置检测
- 查询 CVE 漏洞信息与 IP/Domain/URL 信誉

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: 这是一个专注于网络安全领域的 Model Context Protocol Server (MCPs) 集合项目，包含两个主要目标：
> L16: SQL注入测试工具的MCP服务器实现。基于TypeScript开发，提供了以下功能：

## 星数曲线

```mermaid
xychart-beta
    title "secmate-ai/CyberSecurity-MCPs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a14e9eca4dd8` · [字段定义](../../DATASET.md)*
