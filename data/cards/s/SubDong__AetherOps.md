# SubDong/AetherOps

⭐ 3 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/SubDong/AetherOps) · 个人维护 · 中文 README

**自托管 AI agent SSH 运维终端：审批门控执行、告警与事件回溯**

自托管的 SSH 运维终端，将 xterm.js 终端模拟器与自主 agent 结合：agent 通过 OpenAI function-calling 协议在真实终端执行命令、读取输出并迭代直至任务完成，危险命令黑名单与删除保护由锁定版本的 @cicctencent/agent-core 提供。连接时采集 OS/内核/CPU/内存等系统信息注入提示词，支持每分钟主机指标历史（保留 7 天）、命令审计与回放、多账号权限位控制、多 provider 模型配置与本地打分的自动路由及成本预算。提供 Web 应用、Electron 桌面客户端与 VSCode 扩展三种形态，README 提示将 agent 暴露到 localhost 之外前需阅读 SECURITY.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 在真实终端会话中执行命令并迭代，工具绑定所选会话
- 每分钟主机指标采样保留 7 天，query_metrics 支持趋势与阈值分钟数查询
- 10 个独立权限位的多账号访问控制，凭据 AES-256-GCM 加密存储
- 多 provider 配置与零额外 LLM 调用的自动成本分层路由

## 适用场景

- 通过自然语言让 agent 代为执行服务器巡检、日志分析等运维任务
- 团队共用一个部署并按权限位隔离各成员的连接与审计记录
- 回查主机过去数小时的 CPU/内存/磁盘指标与命令执行轨迹
- 在 VSCode 或桌面客户端中管理多标签 SSH 会话与 ZMODEM/SFTP 文件传输

## 场景标签

 · 领域:开发运维/服务器管理

## 证据(README 行号)

> L5: An AI-powered SSH operations terminal. It combines a full-featured terminal emulator with an
> L30: - **Autonomous loop.** The agent executes commands in a real terminal through tool calling
> L8: **Web app**, an **Electron desktop client**, and a **VSCode extension** that all run the exact same


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `68ee5524f53e` · [字段定义](../../DATASET.md)*
