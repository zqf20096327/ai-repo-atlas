# QuesmaOrg/BinaryAudit

⭐ 106 · Shell · 推送 2026-10-22 · [GitHub](https://github.com/QuesmaOrg/BinaryAudit) · [官网](https://quesma.com/blog/introducing-binaryaudit/) · 组织维护

**评测 AI agent 在编译后二进制中检出后门的基准**

Quesma 维护的开源基准：在 lighttpd、dnsmasq、Dropbear、Sozu、Caddy 五个开源软件中人工注入后门并编译为 stripped 二进制，让 AI agent 在隔离 Docker 环境内使用 Ghidra、Radare2 等逆向工具判断是否存在后门或提取定时炸弹时间戳；另含干净二进制的阴性任务以测误报率与工具操作基线任务。任务经 Harbor 运行，默认 terminus-2 agent 经 OpenRouter 比较模型，也可换用 Claude Code 等其他 CLI agent。所有后门均为测试用途人工注入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个目标应用、多类任务：后门检测/阴性对照/定时炸弹时间戳提取/逆向工具操作基线
- agent 在隔离 Docker 中使用 Ghidra、Radare2 分析无源码二进制
- 经 Harbor 框架运行，支持 OpenRouter/Anthropic API 与多种 CLI agent
- 多架构交叉编译任务需 QEMU binfmt 模拟支持

## 适用场景

- 评测和比较不同模型/agent 的二进制后门检测能力
- 衡量逆向分析 agent 的误报率与工具操作能力
- 安全研究中复现基准结果并查看 agent 轨迹

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L5: An open-source benchmark for evaluating AI agents' ability to find backdoors hidden in compiled binaries of real ope
> L55: AI agents are given compiled binary executables (without source code) and reverse engineering tools (Ghidra, Radare

## 星数曲线

```mermaid
xychart-beta
    title "QuesmaOrg/BinaryAudit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 103 --> 107
    line [104, 106, 106]
```

2026-10-18 104 → 2026-10-28 106（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7d854a13ffa8` · [字段定义](../../DATASET.md)*
