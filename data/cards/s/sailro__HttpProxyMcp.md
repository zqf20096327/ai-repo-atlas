# sailro/HttpProxyMcp

⭐ 14 · C# · 推送 2026-04-09 · [GitHub](https://github.com/sailro/HttpProxyMcp) · 个人维护

**MITM 抓包代理，以 MCP 服务器形式让 LLM 查询分析流量**

基于 .NET 10、C# 与 SQLite 构建的 HTTP/HTTPS MITM 代理，捕获请求、响应、头、body 与计时数据存入 SQLite，通过 MCP 协议经 stdio 暴露 14 个工具，供 Copilot CLI、VS Code 等 MCP 客户端的 LLM 以自然语言控制代理、过滤检索流量、搜索 body、查看统计并导出 HAR 1.2 文件。支持动态证书生成与自动配置 Windows 系统代理，需在首次运行时安装根 CA 证书；根 CA 可解密全部 HTTPS 流量，README 提示仅应在开发机安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MITM 拦截 HTTP/HTTPS，动态证书生成，全量存入 SQLite
- MCP 服务器暴露 14 个工具：代理控制、会话管理、流量分析与 HAR 1.2 导出
- 自动配置并恢复 Windows 系统代理，含多级崩溃清理处理器
- HAR 导出含服务器 IP 与 send/wait/receive 细粒度计时

## 适用场景

- 在 IDE 或 CLI 中用自然语言让 LLM 分析应用的网络流量
- 按域名、状态码、body 内容检索调试 API 请求
- 将捕获的会话导出为 HAR 供浏览器 DevTools 等工具分析

## 场景标签

 · 领域:开发者工具/网络调试

## 证据(README 行号)

> L4: An HTTP/HTTPS MITM proxy with full traffic capture, exposed as an **MCP server** so LLMs can inspect, filter, and an
> L20: - **MCP server** exposes 14 tools for LLMs to query and control the proxy

## 星数曲线

```mermaid
xychart-beta
    title "sailro/HttpProxyMcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `37d74bbdd6e5` · [字段定义](../../DATASET.md)*
