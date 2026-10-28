# zengury/manastone-diag

⭐ 22 · Python · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/zengury/manastone-diag) · [官网](https://pypi.org/project/manastone-diag/) · 个人维护 · 中文 README

**人形机器人离线日志故障诊断助手，LLM agent 三轮复核出报告**

面向 AgiBot X2 Ultra 与 Unitree G1 人形机器人的离线故障诊断工具：摄入 .log/.yaml/.json/.mcap/.atop 日志包（隐私剥离、GB 级安全），按机型故障规则与时间因果推断匹配症状，再由 LLM agent 走三轮复核（数据采集→分析→报告，每轮暂停确认）产出诊断报告；已验证案例回填经验库（分片存储、WAL 保护）。核心计算为确定性 Python，全程本地运行无需网络。PyPI 提供工具安装，完整仓库含样例与 agent 配置，agent 框架不绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摄入 .log/.yaml/.json/.mcap/.atop 五类日志格式，隐私剥离且 GB 级安全
- 机型故障规则匹配（中英）+ 事件时间线因果推断
- LLM agent 三轮复核流程，每轮暂停等用户确认
- 经验库分片存储 + WAL 保护，5,000 条实测 15ms 进程内检索

## 适用场景

- 机器人现场故障后拿到大体积日志包，离线定位故障原因
- 团队共享诊断经验库，让后续诊断复用已验证案例
- 为新型机器人按 schema 扩展故障知识包

## 场景标签

 · 领域:机器人/故障诊断

## 证据(README 行号)

> L26: 3. **Review** — an LLM agent walks you through a three-round review
> L33: The heavy lifting is deterministic Python — the LLM orchestrates and

## 星数曲线

```mermaid
xychart-beta
    title "zengury/manastone-diag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4f1be857c8ea` · [字段定义](../../DATASET.md)*
