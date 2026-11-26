# hivepaas/shellwing

⭐ 192 · Rust · GPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/hivepaas/shellwing) · [官网](https://shellwing.app) · 组织维护

**面向 SSH 用户的客户端：让 AI 代理安全地操作服务器**

用 Rust 与 GPUI 构建的原生 SSH 客户端，覆盖 macOS/Windows/Linux，提供标签页、分屏、SFTP、端口转发、加密保管库与多设备同步，终端由 GPU 渲染并基于 libghostty-vt。AI 方面通过 Model Context Protocol 向 Claude Code、Codex CLI、Cursor 等客户端开放主机访问：代理只拿到主机不拿到凭据，按主机粒度授权操作范围，风险命令进入等待确认队列，AI 活动全程留痕并可回放。安装方式为 GitHub Releases 下载安装包，或用 Rust+Zig 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 MCP 向 AI 代理开放主机访问，代理不接触密钥与密码
- 按主机粒度授权（运行命令/读写文件/读笔记），可随时暂停或收回
- 风险命令（rm -rf 等）进入人工确认队列，AI 活动全程留痕
- 兼容 ~/.ssh/config 与 OpenSSH 行为，含 SFTP、端口转发、加密保管库与同步

## 适用场景

- 让 AI 代理代为登录服务器执行运维命令并修复故障
- 需要集中管理密钥、笔记、片段并多设备加密同步
- 日常 SSH 终端工作流：标签分屏、SFTP 传文件、端口转发

## 场景标签

 · 领域:开发者工具/SSH 终端

## 证据(README 行号)

> L7: Give Claude Code, Codex or any MCP agent the servers it needs, never your keys: it runs commands, reads your runbook
> L20: AI agents reach the hosts you give them through shellwing, over the Model Context Protocol: Claude Code, Claude Des
> L87: |`crates/core`|Sessions without a UI: connecting and reconnecting, prompts, saved secrets; AI access over MCP (`ai/


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8967e55aabf4` · [字段定义](../../DATASET.md)*
