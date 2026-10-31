# Sensente/Security-Attacks-on-LCCTs

⭐ 23 · Python · 推送 2025-12-31 · [GitHub](https://github.com/Sensente/Security-Attacks-on-LCCTs) · 组织维护

**针对 LLM 代码补全工具的安全攻击研究代码（AAAI 2025）**

AAAI 2025 论文官方代码库，研究 GitHub Copilot 与 Amazon Q 等 LLM 代码补全工具的两类安全风险：越狱攻击与训练数据提取攻击。论文报告对 GitHub Copilot 越狱成功率 99.4%、Amazon Q 为 46.3%，并从 Copilot 提取到 54 个真实邮箱与 314 个物理地址；攻击方法同样适用于 GPT 等通用 LLM。代码仅供研究用途，实验数据集附于 data 文件夹，攻击需在 VSCode 中安装对应插件或持有 API key，无包依赖要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 LCCT 的越狱攻击与训练数据提取攻击方法
- 实验数据集（Forbidden Questions）附于 data 文件夹
- 攻击方法对 GPT 系列通用 LLM 亦有效

## 适用场景

- 复现论文中 LCCT 越狱与数据提取攻击实验
- 评估代码补全工具的安全风险
- 研究 LLM 处理代码时的安全错位问题

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L12: The rapid development of large language models (LLMs) has significantly advanced code completion capabilities, givi
> L17: ## Requirements

## 星数曲线

```mermaid
xychart-beta
    title "Sensente/Security-Attacks-on-LCCTs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `a46b7c705999` · [字段定义](../../DATASET.md)*
