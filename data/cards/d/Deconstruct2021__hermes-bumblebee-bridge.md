# Deconstruct2021/hermes-bumblebee-bridge

⭐ 18 · Shell · NOASSERTION · 推送 2026-05-24 · [GitHub](https://github.com/Deconstruct2021/hermes-bumblebee-bridge) · 个人维护

**为 Hermes Agent 接入 Bumblebee 的供应链安全扫描桥**

把 Perplexity 的 Bumblebee 只读扫描器封装为 Hermes Agent 可调用的技能：一键安装脚本下载 Bumblebee 二进制与威胁情报目录，配置 systemd 用户定时器每日扫描 $HOME 下的 npm/PyPI/Go/RubyGems/Composer/MCP 配置/编辑器与浏览器扩展等已装包，按精确 (ecosystem, name, version) 元组匹配已知受污染版本。汇总器输出 JSON 摘要，供 Hermes 语音播报及 Telegram/Slack/Discord/webhook 推送新发现告警；告警默认关闭需手动开启，通知前对敏感路径与密钥模式做脱敏。支持 Linux/macOS，Windows 需 WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键安装：下载 sha256 校验的 Bumblebee 二进制 + 情报目录 + systemd 定时器 + Hermes 技能
- 按精确 (ecosystem, name, version) 匹配威胁情报目录，不执行包管理器、无 sudo
- 新发现触发 Telegram/Slack/Discord/webhook 推送，通知前对 .env/.ssh/密钥模式脱敏
- Hermes 原生技能：'is the system clean?' 由 Agent 自行运行扫描并播报

## 适用场景

- 让本地运行的 Hermes Agent 具备对宿主机的持续供应链安全监控
- 每日自动扫描已装包并匹配已知受污染版本，新发现即时推送
- 通过 Telegram 对话让 Agent 代为执行安全扫描并汇报

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L14: - **Hermes-native skill** — when you ask "is the system clean?" Hermes runs the scan himself and narrates the resul
> L62: He will load the `bumblebee-scan` skill, run a fresh scan via `systemctl --user start --wait bumblebee-scan.service

## 星数曲线

```mermaid
xychart-beta
    title "Deconstruct2021/hermes-bumblebee-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `183e029b2c97` · [字段定义](../../DATASET.md)*
