# justadityaraj/shim-mcp

⭐ 44 · PHP · GPL-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/justadityaraj/shim-mcp) · [官网](https://dev.adityarajsingh.com/shim-mcp/) · 组织维护

**把 WordPress 站点变成 MCP 服务器的插件，供 AI 编码客户端接入**

单插件自包含的 WordPress MCP 服务器：安装后站点通过 WordPress Abilities API 暴露 57 个能力，覆盖文章、页面、媒体、用户、插件、菜单、评论与系统管理，供 Claude Code、Cursor、Windsurf 等 MCP 客户端调用。提供两种连接方式：本地 stdio（经 WP-CLI 启动，无 HTTP、无令牌）和远程 Streamable HTTP（应用程序密码认证）。每个能力声明所需权限并对具体对象做二次权限校验；改写 wp-config.php 的能力默认关闭。要求 WordPress 6.9+ 与 PHP 8.0+，已上架 WordPress.org 插件目录，作者自述尚未在广泛的主机环境中运行过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 57 个 WordPress 能力经核心 Abilities API 注册，其他插件注册的能力也会自动暴露
- stdio（WP-CLI 本地）与 Streamable HTTP（远程）两种传输，MCP 多版本协议自动协商
- 逐对象权限校验（edit_post/delete_post 等），非仅整站授权
- 无云中继、无遥测、无厂商账户，数据不出服务器

## 适用场景

- 让 Claude Code 或 Cursor 像操作代码库一样操作本地 WordPress 站点
- 为生产 WordPress 站点提供经应用程序密码认证的远程 MCP 接入
- 通过 AI 客户端管理文章、媒体、插件与用户等站点资源

## 场景标签

 · 领域:Web/WordPress 工具与 MCP 基础设施

## 证据(README 行号)

> L9: A self-contained **Model Context Protocol (MCP) server for WordPress**, built for developers. Install one plugin and
> L41: That is exactly what this is. WordPress speaks the Abilities API. AI clients speak MCP. Shim translates between the

## 星数曲线

```mermaid
xychart-beta
    title "justadityaraj/shim-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-28 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8a80e686792a` · [字段定义](../../DATASET.md)*
