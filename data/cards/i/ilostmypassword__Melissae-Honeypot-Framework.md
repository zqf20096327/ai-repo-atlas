# ilostmypassword/Melissae-Honeypot-Framework

⭐ 14 · JavaScript · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/ilostmypassword/Melissae-Honeypot-Framework) · [官网](https://melissae-documentation.readthedocs.io) · 个人维护

**分布式蜜罐框架：容器化诱饵、规则评分与可选 AI 分析师**

Manager/agent 架构的分布式蜜罐框架：轻量 agent 部署各处，经 mTLS（ECDSA P-384、一次性令牌）与 Manager 通信。提供 7 种蜜罐模块（Web/SSH/FTP/Telnet/Modbus/MQTT 及 CVE 专项诱饵），14 条 YAML 规则对每个 IP 打 0-100 分并给出良性/可疑/恶意判定；实时仪表盘含拓扑、GeoIP 地图、杀伤链、日志搜索与 STIX 2.1 导出。AI 为可选功能：基于 AWS Bedrock + LangChain 的 Inspektor 威胁分析师，支持对话与 PDF 简报导出。经 git clone 后用 shell 脚本安装，依赖 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Manager/agent 架构，mTLS（ECDSA P-384）+ 一次性令牌接入
- 14 条 YAML 规则对 IP 进行 0-100 威胁评分
- 7 种蜜罐模块，含 Modbus/ICS、MQTT 与 CVE 专项诱饵
- 可选 Inspektor AI 分析师（AWS Bedrock + LangChain），导出 PDF 简报

## 适用场景

- 部署蜜罐诱饵并集中管理多个 agent 节点
- 对攻击 IP 进行规则评分并导出 STIX 2.1 情报
- 让 AI 分析师解读攻击事件并生成 PDF 简报

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L26: Most honeypots give you a wall of logs. **Melissae gives you a fleet of decoys, a verdict on every attacker, and an
> L31: - **Inspektor AI** : Optional threat analyst on AWS Bedrock + LangChain; chat with your hive, export PDF briefings.

## 星数曲线

```mermaid
xychart-beta
    title "ilostmypassword/Melissae-Honeypot-Framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c5b8a367cbc3` · [字段定义](../../DATASET.md)*
