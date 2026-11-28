# debug-null/tunless

⭐ 3 · JavaScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/debug-null/tunless) · [官网](https://www.npmjs.com/package/tunless) · 个人维护 · 中文 README

**让 AI Agent 工具不开 TUN 也能联网的 macOS 本地转发代理**

面向只认 HTTPS_PROXY 环境变量、不读 macOS 系统代理的 Agent 工具（Antigravity、Cursor、各类 CLI Agent）：tunless 起一个本地 HTTP/SOCKS5 转发代理，把请求交给已运行的 Clash/mihomo 等内核，同时让内网域名走直连，避免开 TUN 后内网被代理接管。提供 TUI 五步向导与 CLI 子命令：上游代理自动探测（mihomo REST/系统代理/端口协议实测）、按工具实际域名实测连通、内网 DNS 分流配置写入（Clash Verge Rev merge 层或通用 mihomo 配置热重载）、写前备份与回滚。核心逻辑零运行时依赖，仅用 Node 内置模块；界面基于 ink + React，需 Node 运行。仅支持 macOS（launchd/scutil/open --env）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地转发代理（HTTP 8899 / SOCKS5 8898）接现有代理内核，无需 TUN
- 上游代理自动探测：mihomo REST → 系统代理 → 端口协议实测
- 内网域名分流：RFC1918 判定 + 手写 DNS UDP 报文，写入 nameserver-policy 与 fake-ip-filter
- 按各工具实际连接的域名做连通实测，配置写入前自动备份可回滚

## 适用场景

- 公司内网环境里让 Cursor/Antigravity 不开 TUN 也能连模型
- 给只认 HTTPS_PROXY 的 CLI Agent 提供本地代理口
- 修复内网域名被代理解析成假 IP 或公网地址的问题

## 场景标签

 · 领域:网络工具/开发者工具

## 证据(README 行号)

> L3: **让 AI Agent 不用开 TUN 也能联网。**
> L12:  把请求交给已运行的 Clash／mihomo 内核 —— Agent 只要认 `HTTPS_PROXY` 就能用，**不需要 TUN**；
> L33: 典型例子是 **Cursor**、**Antigravity**（VS Code 系 AI 编辑器）和各类 CLI Agent。它们要么只认 `HTTPS_PROXY`，


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `dd534193ebc7` · [字段定义](../../DATASET.md)*
