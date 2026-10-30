# josephsteuerjr/praxis

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/josephsteuerjr/praxis) · [官网](https://github.com/josephsteuerjr/praxis/releases/latest) · 个人维护

**面向独立 agent 的桌面宿主：持久记忆、工具、Telegram 与可选本地语音**

Hélène 是一个桌面应用，为独立运行的 agent 提供住所：每个 agent 拥有独立人格、以可检查的 Markdown/JSONL 形式保存的持久记忆（配 SQLite 索引）、设置与工作文件。用户可在桌面窗口对话，接入 Telegram（bot 或 MTProto 账号），或在主机在线时经手机/网页访问。Agent 可搜索编辑文件、使用 shell 与已配置的计算机工具；Forge 模块协调工程任务、worker 结果与独立评审。自带打包好的 Python 运行时，下载解压即可运行；模型访问需自备凭证。Whisper 与 XTTS 为可选本地组件，XTTS 权重受 Coqui 非商业许可约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 记忆以 Markdown/JSONL 存储，SQLite 建索引，可检查
- 支持 Telegram bot 或 MTProto 账号接入，以及手机/网页配对访问
- Agent 可用 shell、文件编辑与已配置计算机工具；Forge 协调多 worker 任务与独立评审
- 打包自带 Python 运行时，解压即用，无需编译器或另装 Python

## 适用场景

- 想长期拥有带持久记忆与工作文件的私人桌面 agent
- 通过 Telegram 或手机远程与自己的 agent 对话
- 让 agent 在本机执行文件操作与 shell 任务并接受人工监督

## 场景标签

`Agent 记忆` `多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L20: Hélène is a desktop home for agents with their own character, lasting memory,
> L21: settings and working files. Talk in the desktop window, connect Telegram, or use

## 星数曲线

```mermaid
xychart-beta
    title "josephsteuerjr/praxis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ea75b91c304c` · [字段定义](../../DATASET.md)*
