# hostealo-org/hostealo-terminal

⭐ 3 · TypeScript · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/hostealo-org/hostealo-terminal) · [官网](https://hostealo.es) · 组织维护

**面向服务器管理者的多协议桌面终端，内置需逐步审批的 AI agent**

基于 Tauri 与 Rust 构建的桌面应用，将 SSH/SFTP/FTP、RDP 远程桌面、Docker 容器管理、Proxmox/KVM 虚拟机管理整合进一个服务器列表。AI 部分为 agent 模式：读取终端输出、链式执行命令，每条命令等待用户批准，危险命令需二次确认；模型由用户自选（API key、Claude Code 订阅、本地 Ollama 或任意 OpenAI 兼容端点）。设备间同步走本地网络点对点加密，不经过云端，无账号无遥测。提供 macOS/Windows/Linux 安装包及源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSH、SFTP/FTPS、RDP、Docker、Proxmox/KVM 管理整合于单一应用
- agent 模式逐步执行命令，每步等待用户批准并检查结果
- 支持 Claude、OpenAI、Ollama 本地模型及任意 OpenAI 兼容端点
- 无云端设备同步：本地网络点对点，X25519+ChaCha20-Poly1305 加密

## 适用场景

- 用一个应用替代终端、SFTP 客户端、远程桌面与服务器面板
- 让 AI agent 在逐步审批下完成安装 nginx 等服务器操作
- 在无云服务的环境下多台设备同步服务器配置
- 通过 SSH 管理 Proxmox 集群与 KVM 虚拟机，无需 API token

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  SSH, SFTP, FTP and remote desktop in one app.
> L6:  With an AI agent that does the work on your servers, step by step and with your permission,
> L12:  License: FSL-1.1-ALv2
> L64: ### AI assistant and agent mode


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `45b68e32cf15` · [字段定义](../../DATASET.md)*
