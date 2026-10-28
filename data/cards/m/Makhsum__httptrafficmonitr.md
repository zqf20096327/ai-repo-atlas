# Makhsum/httptrafficmonitr

⭐ 21 · C# · MIT · 推送 2026-10-06 · [GitHub](https://github.com/Makhsum/httptrafficmonitr) · 个人维护

**带 MCP 服务器的 Windows HTTP/HTTPS 抓包调试工具**

基于 WPF/.NET 8 的 Windows 桌面 MITM 代理：作为系统代理捕获整机 HTTP/HTTPS 流量（本地根 CA 解密），提供实时请求网格、多条件过滤、请求重发/构造、双请求对比、规则告警、Auto-Responder mock、图表与会话导出（CSV/HAR/JSON/cURL/Postman）。内置 MCP 服务器（stdio）把运行中的应用经本地 IPC REST API 暴露为 42 个 MCP 工具，供 Claude 等 AI 助手读取流量、管理告警与 mock 规则、重发请求；默认只读，需在应用内手动开启写权限。面向 Windows 开发者与测试者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 系统级捕获并显示发送请求的进程名
- 42 个 MCP 工具让 AI 助手检查/过滤/重发/mock 流量
- 默认只读模式与 Agent replay hosts 白名单限制
- 导出 CSV/HAR/JSON/cURL/Postman，.NET 运行时随发布包附带

## 适用场景

- 调试应用或服务实际发送的 HTTP/HTTPS 请求
- 让 AI 助手定位失败请求并自动重发验证
- 用 Auto-Responder 在开发期 mock 不稳定的后端 API

## 场景标签

 · 领域:开发者工具/网络监控

## 证据(README 行号)

> L5: For developers and testers on Windows who need to see what an app, a service or a browser really sends and receives:
> L101: `HttpTrafficMonitor.McpServer` exposes the running app to AI assistants over the Model Context Protocol (stdio tra

## 星数曲线

```mermaid
xychart-beta
    title "Makhsum/httptrafficmonitr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d3717e8178e3` · [字段定义](../../DATASET.md)*
