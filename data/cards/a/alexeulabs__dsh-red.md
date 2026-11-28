# alexeulabs/dsh-red

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/alexeulabs/dsh-red) · 组织维护 · 中文 README

**给渗透测试者的 DeepSeek Harness 定制发行版**

面向渗透测试场景重新组装的 DeepSeek agent harness 发行版，命令为 dshs，与官方 dsh 隔离安装（独立目录与端口）。在一个界面内提供交互式终端（PTY shell）、SSH 主机管理与 SFTP、逆向工程 MCP（对接 Ghidra/IDA/JADX 等引擎）、SQLite 演练台事实库与可视化插件市场。需自行准备 Linux 渗透机工具链（nmap/nuclei 等）与模型 API Key，README 给出 WSL+Kali 与 Windows 原生两条环境准备路线。

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

- 内置 REA 逆向 MCP，覆盖 ELF/PE/APK/WASM 等格式反编译分析
- SQLite 演练台事实库跨会话保留资产、凭据与战果记录
- 持久 PTY 终端与 SSH 插件（主机管理/SFTP/端口转发）
- 提供 dsh-purge-safe 提示词清洗与 danger-full-access 权限档

## 适用场景

- 在授权目标上完成侦察、打点、后渗透到报告导出的完整作业
- 拖入样本做反编译、脱壳与流量分析
- 通过 SSH 插件远程维持主机访问并挂持久会话

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: 面向渗透测试的 DeepSeek Harness 发行版，命令为 `dshs`。
> L9: 在一个界面里完成侦察、打点、后渗透与报告：交互式终端、SSH 运维、逆向工程引擎、演练台事实库、插件市场全部预置开箱可用。与官方 `dsh` **完全隔离**，可并排安装互不影响。
> L13: 官方 `dsh` 是通用 agent harness，执行受沙箱约束、工具偏保守。本版本按渗透场景重新组装：


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `d777bf9c51a4` · [字段定义](../../DATASET.md)*
