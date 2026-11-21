# jaskran0417/ai-termux-wadb-toolkit

⭐ 5 · Shell · Apache-2.0 · 推送 2026-11-07 · [GitHub](https://github.com/jaskran0417/ai-termux-wadb-toolkit) · 个人维护

**让手机上的云端 AI 助手经授权操作 Termux 文件与命令的工具集**

运行在 Termux 内部的工具集，通过 Desktop Commander Remote MCP 将手机端终端、文件系统与进程工具暴露给兼容的 AI 客户端，使 AI 可检查项目、执行 Termux 命令、编辑文件并保存结果，无需 PC 或本地模型。包含 Wireless ADB 管理、WADB Bridge 安卓伴侣应用、两个仅回环的本地认证 Shell（Termux UID 与 Android shell UID 2000）、ai-info 控制中心以及看门狗/恢复机制。推荐以 AI 辅助方式完成安装；Termux:API 与 GitHub CLI 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 Desktop Commander Remote MCP 向 AI 客户端暴露手机端终端与文件工具
- 双本地认证 Shell：Termux UID（47173）与 Android shell UID 2000（47174），仅回环监听
- Wireless ADB 管理：mDNS 发现、受信任密钥重连、配对状态保护
- 签名包校验、文件完整性检查与安装回滚

## 适用场景

- 在手机上让 AI 助手直接检查和修改 Android 项目文件并运行测试
- 免 PC 的手机端命令行开发工作流
- 通过 ai-info 检查与管理 Wireless ADB、WADB Bridge 与本地 Shell 状态

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: AI Termux WADB Toolkit connects a compatible AI assistant to an authorised Termux environment on Android. It gives t
> L67: - **AI-to-phone connection:** works with Desktop Commander Remote MCP so a compatible AI client can use authorised 
> L53: The AI model stays with its provider. Termux provides the local working environment. Desktop Commander is a separat

## 星数曲线

```mermaid
xychart-beta
    title "jaskran0417/ai-termux-wadb-toolkit 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-18", "2026-11-21"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-21 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `89f95128ac5f` · [字段定义](../../DATASET.md)*
