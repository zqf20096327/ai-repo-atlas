# dondai1234/goshawk

⭐ 29 · Go · MIT · 推送 2026-07-24 · [GitHub](https://github.com/dondai1234/goshawk) · 个人维护

**给 agent 用的浏览器 MCP 服务器：9 个工具、单 Go 二进制**

基于 Chrome DevTools Protocol 的 MCP 服务器，让 Claude Code、Cursor 等支持 MCP 的客户端驱动浏览器完成导航、读取、点击、填表、登录与抓取。提供 9 个工具（nav/see/act/js/find/tabs/history/session/login），每个动作返回带置信度标签的自诊断裁决（confirmed/likely/uncertain），失败时扫描页面错误并给出下一步建议，采用纯启发式、无 LLM 参与循环。支持意图式操作、批量填表、单次调用登录（处理 2FA/SSO/多步）、自愈 ref、命名配置文件与 Cookie 横幅自动关闭。限制：硬 CAPTCHA 仅报告为 CHALLENGE、跨域 iframe 不可访问、需本机已装 Chrome。

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

- 每个动作返回置信度标签的自诊断裁决，无 LLM 参与、纯启发式
- 单 Go 二进制（约 14MB），无 Node/Python/Docker 依赖，go install 即装
- 9 个工具约 3.4K tokens 的工具清单开销
- 单次调用登录支持多步表单、2FA 检测、SSO 重定向报告

## 适用场景

- 让 Claude Code/Cursor 等 MCP 客户端操作网页完成任务
- agent 表单批量填写与登录流程自动化
- 需要低 token 开销的浏览器抓取与自动化

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Navigate, read, click, fill, log in, scrape. Pure Go, single binary, no Node, no Python, no Docker.
> L6: Built on Chrome DevTools Protocol + MCP. Works with Claude Code, Cursor, OpenCode, Pi, anything that speaks MCP.

## 星数曲线

```mermaid
xychart-beta
    title "dondai1234/goshawk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b8efe331297b` · [字段定义](../../DATASET.md)*
