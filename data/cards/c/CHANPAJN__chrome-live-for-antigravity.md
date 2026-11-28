# CHANPAJN/chrome-live-for-antigravity

⭐ 18 · JavaScript · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/CHANPAJN/chrome-live-for-antigravity) · 个人维护 · 中文 README

**让 Antigravity 操作日常已登录 Chrome/Edge 的 MCP 桥接工具**

由 Chrome MV3 扩展、本地桥接守护进程与 stdio MCP Server 组成的桥接层：通过 Alt+Shift+L 将已登录标签页交给 Antigravity，Agent 打开的页面收纳进自动折叠的后台标签组，不抢占窗口焦点；在聊天内嵌 0-token 实时预览卡片（MCP Apps ui:// 标准），支持多标签切换与拖选 DOM 提取；将 open/type/click/wait/snapshot 合并为单轮 batch 调用。守护进程仅绑定 127.0.0.1，使用 HMAC-SHA256 双向认证，内置支付/上传护栏与凭据读取脱敏。纯 Node.js >= 20 内置模块实现，零 npm 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键共享已登录标签页，免在沙箱浏览器重复登录与 2FA
- 0-token 聊天内实时预览（MCP Apps ui:// 标准）
- 单轮 batch 调用合并多步浏览器操作，降低 token 与耗时
- 回环隔离 + HMAC-SHA256 双向认证，支付/上传护栏与凭据脱敏

## 适用场景

- 让 Antigravity 直接操作已登录 GitHub、云控制台、内部看板等页面
- 在编辑器聊天窗口内实时预览并远程点击/滚动网页
- 需要保留手动 2FA/扫码登录时机时弹出页面人工接管

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L28: `chrome-live-for-antigravity` bridges Antigravity directly to your own Chrome or Edge browser:
> L131:   AG["Google Antigravity\nChat & Inline Monitor"] <-->|"stdio JSON-RPC\n+ MCP Apps ui://"| MCP["Local MCP Server"]
> L133:   MCP <-->|"127.0.0.1:28196\nMutual HMAC-SHA256"| DMN


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `2da417e843ef` · [字段定义](../../DATASET.md)*
