# electerm/electerm

⭐ 15,725 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/electerm/electerm) · [官网](https://electerm.org) · 个人维护 · 中文 README

**跨平台终端/SSH/SFTP/RDP/VNC 客户端，含 AI 助手与 MCP**

基于 Electron 的开源终端与远程连接客户端，支持 ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice 协议，覆盖 Linux/Mac/Windows/Android/HarmonyOS/iOS 及 UOS、Kylin、LoongArch、RISC-V 等平台。功能包括文件管理、多种认证方式、Zmodem/Trzsz 传输、隧道与连接跳板、代理、书签同步等。AI 部分：内置 AI 助手（支持 OpenAI Chat Completions/Responses 与 Anthropic Messages API 格式）用于命令建议、脚本编写、解释终端内容以及 agent 模式直接执行终端操作，并提供 MCP widget 供外部 AI 工具接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.9 天,年发版 95,50 位贡献者
- 涨星:近 1 天 **+8**(自 20261016 起算)
- 安装:npm 包 `electerm` 月下载 4,275
- 平台:WINDOWS / MACOS / LINUX / ANDROID / IOS / WEB · 协议:OPENAI-API / MCP

## 能力要点

- 多协议远程连接：ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice
- AI 助手支持 OpenAI 与 Anthropic API 格式，含 agent 模式执行终端操作
- MCP widget 供 AI 助手与外部工具集成
- 广泛平台支持：含 HarmonyOS、UOS/Kylin/LoongArch/RISC-V/ppc64le

## 适用场景

- 统一管理多台服务器的 SSH/SFTP 连接与文件传输
- 借助 AI 助手生成命令、编写脚本或解释终端输出
- 通过 MCP 让外部 AI 工具操作终端
- 在国产 Linux 发行版或老旧系统上使用终端客户端

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L13: Open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client(Linux, Mac, Windows, Android, HarmonyOS, 
> L52: - AI assistant integration (supporting multiple LLM API formats — OpenAI Chat Completions, OpenAI Responses, and An

## 星数曲线

```mermaid
xychart-beta
    title "electerm/electerm 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 15421 --> 15752
    line [15448, 15454, 15465, 15475, 15491, 15501, 15506, 15513, 15519, 15448, 15574, 15597, 15610, 15615, 15625, 15631, 15638, 15645, 15656, 15661, 15662, 15671, 15675, 15682, 15693, 15712, 15725]
```

2026-10-25 15,448 → 2026-11-27 15,725（+277）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `715b6995a802` · [字段定义](../../DATASET.md)*
