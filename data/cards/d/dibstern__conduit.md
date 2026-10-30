# dibstern/conduit

⭐ 15 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/dibstern/conduit) · 个人维护

**OpenCode 的浏览器 UI：手机/平板远程查看会话并一键审批权限**

连接 `opencode serve` 的本地中继服务器，将 OpenCode 编码代理会话流式传输到任意设备的浏览器：聊天历史、diff 渲染、文件浏览器、xterm.js 终端、会话分叉等完整界面。核心机制是推送通知+一键 Allow/Deny 审批——OpenCode 暂停等待工具权限时，用户无需在电脑前。通过 npx 安装运行，PIN 认证，默认绑定 127.0.0.1，远程访问需 Tailscale 或 VPN；推送通知需 HTTPS（Tailscale Serve 或 mkcert）。限制：依赖 OpenCode 运行在 4096 端口。

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

- 工具权限请求的推送通知与手机一键审批
- 单端口多项目管理，PWA 可安装到主屏幕
- LCS diff 渲染、Mermaid 图表、180+ 语言语法高亮、xterm.js 终端标签
- QR 码扫码连接，会话与草稿跨重连持久化

## 适用场景

- 离开工位时用手机继续查看并审批 OpenCode 代理的权限请求
- 在平板/手机上操作 OpenCode 编码会话与终端
- 单台服务器统一管理多个项目的 OpenCode 会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: Conduit connects to `opencode serve` and streams your session to a browser.
> L245: No. Conduit connects to OpenCode's HTTP/SSE API directly. It doesn't scrape

## 星数曲线

```mermaid
xychart-beta
    title "dibstern/conduit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `25ae1d5d1873` · [字段定义](../../DATASET.md)*
