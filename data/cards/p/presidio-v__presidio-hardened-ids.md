# presidio-v/presidio-hardened-ids

⭐ 49 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/presidio-v/presidio-hardened-ids) · 个人维护

**教学用的 ML 入侵检测系统：含对抗逃逸攻击与加固实验**

计算机安全课程（PRES-EDU-SEC-101 实验4）配套仓库：用合成网络流量训练 Isolation Forest 异常检测器，通过 Streamlit 仪表盘实时展示异常分数；随后执行对抗逃逸攻击（evasion），再用对抗样本重训模型实现加固，并生成 JSON 报告。包结构包含流量生成、特征工程、检测器封装、对抗模块与安全日志（pip-audit）。以 Python 源码形式提供，git clone 后 pip 安装依赖运行，未见生产部署说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 合成流量生成（portscan/synflood/exfiltration 等攻击类型）
- Isolation Forest 异常检测器训练与实时 Streamlit 仪表盘
- 对抗逃逸攻击生成报告，并以对抗样本重训加固模型

## 适用场景

- 学习入侵检测与对抗机器学习加固流程
- 观察逃逸攻击对基线模型与加固模型的差异
- 课程实验复现与报告生成

## 场景标签

`网络安全` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: ML-based intrusion detection system with adversarial evasion and hardening.
> L25: ### Run 2 — Train Isolation Forest detector
> L45: ### Run 4 — Adversarial evasion attack

## 星数曲线

```mermaid
xychart-beta
    title "presidio-v/presidio-hardened-ids 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `16c025694798` · [字段定义](../../DATASET.md)*
