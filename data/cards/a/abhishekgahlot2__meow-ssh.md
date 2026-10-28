# abhishekgahlot2/meow-ssh

⭐ 28 · Rust · NOASSERTION · 推送 2026-03-22 · [GitHub](https://github.com/abhishekgahlot2/meow-ssh) · [官网](https://meow.gs) · 个人维护

**用浏览器 passkey（Touch ID/Face ID）做 SSH 认证的 Rust 服务器**

单个 Rust 二进制实现的 SSH 服务器：SSH 连接后给出短链 URL，用户在浏览器中通过 WebAuthn passkey（Touch ID / Face ID）完成验证，SSH 会话解锁；无密码、无 SSH 密钥。内含基于 xterm.js 的浏览器终端（/terminal）。SSH 层用 russh 0.57（含后量子密钥交换），状态存于本地 SQLite，注册需服务端 secret 验证。提供 Docker 与源码（cargo build）两种运行方式，另有托管版 meow.gs（内置 Claude Code、Codex 等云开发环境）。许可证为 BSL 1.1，4 年后转为 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSH 认证流程改为浏览器 WebAuthn passkey（Touch ID / Face ID）
- 单个 Rust 二进制，无需 Node.js/npm，内嵌浏览器终端（xterm.js）
- russh 0.57 支持后量子密钥交换（mlkem768x25519-sha256）
- 一次性认证令牌（6 位 hex，5 分钟过期）与服务端 secret 注册验证

## 适用场景

- 我不想管理 SSH 密钥，用指纹/面容完成服务器登录
- 在浏览器里直接获得同一容器的 SSH 与终端访问
- 为云开发环境（如 Claude Code、Codex）配置 passkey 登录

## 场景标签

 · 领域:开发工具/身份认证

## 证据(README 行号)

> L9: SSH authentication via browser passkeys (Touch ID / Face ID).
> L86: Don't want to self-host? meow.gs gives you a cloud dev environment with passkey auth — Claude Code, Codex, Gemini C

## 星数曲线

```mermaid
xychart-beta
    title "abhishekgahlot2/meow-ssh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9463a16cdb9b` · [字段定义](../../DATASET.md)*
