# owen-yue/SailTerm

⭐ 3 · Rust · MIT · 推送 2026-11-24 · [GitHub](https://github.com/owen-yue/SailTerm) · 个人维护 · 中文 README

**开发者保服务器用的 AI 辅助 SSH/SFTP/FTP 桌面终端，凭据不进模型**

基于 Tauri 2 + Rust 的跨平台桌面终端，整合 SSH/SFTP/FTP 连接、文件传输与 AI 助手。关键机制：凭据只存于 Rust 核心进程与 OS keychain（回退 AES-256-GCM 加密文件），AI 通过已建立会话的 session_id 句柄操作服务器，输出先做脱敏再送模型，写操作与高风险操作需人工审批，全程记录审计日志。macOS 有预构建包（自签名未公证），Windows/Linux 实验性需源码构建。项目为 0.x 早期预览，作者自述非专业运维，欢迎反馈。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 凭据隔离：存 OS keychain，仅 Rust 核心持有，前端无凭据无网络
- AI 经 session_id 在已建立 SSH 会话内执行，写/高风险操作需人工审批
- 终端输出送模型前做密码/token/私钥/内网 IP 脱敏
- 风险分级策略引擎（只读/写/高危）与完整审计日志

## 适用场景

- 日常维护多台服务器时在一个应用里完成终端、传文件与排错
- 希望用 AI 帮忙跑命令但不想暴露主机账号与私钥
- 用 AI 读懂报错并直接在已有会话中执行修复命令

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: > A cross-platform desktop SSH / SFTP / FTP terminal with AI built in — the AI works on your servers through the est
> L14: So I built SailTerm: one desktop app where the terminal, file transfer and AI live together — and where the AI can 
> L21: - The AI operates **through the already-established SSH session** via a `session_id` handle — it says *what* to do,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `6b378af8d9ec` · [字段定义](../../DATASET.md)*
