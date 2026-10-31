# badchars/darknet-mcp-server

⭐ 521 · TypeScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/badchars/darknet-mcp-server) · [官网](https://www.npmjs.com/package/darknet-mcp-server) · 个人维护 · 中文 README

**给 AI agent 的暗网与威胁情报 MCP 服务器（66 工具/16 源）**

面向安全调查场景的 Model Context Protocol 服务器：把 HIBP 泄露库、ThreatFox/abuse.ch IOC、勒索软件追踪（ransomware.live/RansomLook）、Tor .onion 访问（需本地 Tor SOCKS5 代理）、MalwareBazaar 恶意样本、GreyNoise、OTX、AbuseIPDB、Vulners 漏洞利用、Hudson Rock 窃密日志与比特币链上情报等 16 个数据源统一为 66 个 MCP 工具，供 Claude Code/Desktop、Cursor 等 MCP 客户端调用。多数工具免 API key 可用，部分源需配置可选环境变量；通过 npx 一条命令运行，无需本地编译。

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

- 66 个工具覆盖 16 个威胁情报数据源
- 多数工具免 API key：勒索追踪、区块链、OTX、GreyNoise 等
- 7 个 Tor 工具经 SOCKS5 代理抓取/搜索 .onion 站点
- npx 一条命令启动，API key 全部可选

## 适用场景

- 让 AI agent 在一次对话中并行查询多源泄露与威胁情报
- 调查目标域名/邮箱的泄露暴露与窃密日志
- 按行业/国家追踪勒索软件受害者与团伙动态
- 分析文件哈希关联的 IOC 与恶意样本信息

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L29:  HIBP, ThreatFox, ransomware tracking, Tor .onion access, blockchain intel, exploit search, stealer logs, malware a
> L62: **darknet-mcp-server** gives your AI agent 66 tools across 16 data sources via the Model Context Protocol. The agen
> L164: Same JSON config format. Point the command to `npx darknet-mcp-server` or your local installation path.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4c8abb929439` · [字段定义](../../DATASET.md)*
