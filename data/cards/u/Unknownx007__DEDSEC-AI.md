# Unknownx007/DEDSEC-AI

⭐ 11 · Python · 推送 2026-07-24 · [GitHub](https://github.com/Unknownx007/DEDSEC-AI) · 个人维护

**面向安全/渗透人员的终端 CLI 黑帽人格 AI 聊天工具**

基于 Python 的零依赖命令行 AI 终端，提供交互聊天、多行粘贴、上下文清除与速率限制遥测等功能。核心机制是 API 密钥池管理：可依次堆叠多个 OpenAI/Groq 密钥，遇到 HTTP 429 限流时自动热切换到下一密钥而不中断会话。系统提示词外置为可编辑的 DEDSEC 黑帽人格配置文件。需用户自行获取 OpenAI 或 Groq 的 API 密钥方可运行；README 声明仅用于授权的安全审计与教育用途，采用 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多密钥堆叠与 HTTP 429 自动故障切换，不中断会话
- /paste 多行输入协议，支持整段脚本/traceback 粘贴
- 外置系统宣言配置文件，支持热刷新同步
- 动态速率限制遥测条显示

## 适用场景

- 在终端中与无过滤人格的 AI 进行安全情报查询
- 管理多个 Groq/OpenAI 密钥自动轮换避免限流
- 粘贴完整脚本或报错代码块让 AI 分析

## 场景标签

`聊天机器人` `网络安全` · 领域:对话与助手

## 证据(README 行号)

> L6: **DEDSEC-AI** is a high-utility, zero-dependency Command Line Interface (CLI) neural terminal designed specifically 
> L20: - Allows users to stack multiple **OpenAI** and **GroqAI** developer authentication tokens sequentially into a pers

## 星数曲线

```mermaid
xychart-beta
    title "Unknownx007/DEDSEC-AI 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-15", "2026-11-19"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-11-02 10 → 2026-11-19 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `6c2fead7a9e9` · [字段定义](../../DATASET.md)*
