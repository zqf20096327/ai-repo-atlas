# gravion-ux/preference-data-doctor

⭐ 4 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/gravion-ux/preference-data-doctor) · 个人维护

**诊断并修复 LLM 个性化偏好数据集的 CLI 工具**

读取数据集目录，扫描 .json/.jsonl/.csv 记录，检测重复、矛盾对、类别失衡、格式漂移与隐私泄漏等 16 类缺陷，每条发现附脱敏摘录与修复建议；按严重度加权评分并给出 A+–F 等级，repair 子命令可写出修复副本。无运行时依赖，支持 CLI 与 Node.js 库两种用法，退出码可接入 CI 门禁。

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

- 16 条规则覆盖 quality/balance/format/privacy/leakage 五类缺陷
- 严重度加权评分并输出 A+–F 等级
- audit/repair/rules 三个子命令，支持 JSON 与 Markdown 报告输出
- 零运行时依赖，可用作 Node.js 库（createDoctor/toJson/repairDataset）

## 适用场景

- 在 CI 中对偏好数据集做质量门禁（--fail-on 阈值控制退出码）
- 发布前扫描数据集中泄漏的密钥与个人信息
- 修复 few-shot 示例库中的重复与矛盾记录

## 场景标签

 · 领域:LLM 数据工具/数据质量

## 证据(README 行号)

> L5: Preference Data Doctor diagnoses — and repairs — the preference datasets that personalise
> L6: LLM systems: few-shot examples, preference pairs, and user profile records.
> L18: Preference Data Doctor reads a dataset directory, reports every defect it finds with a


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `b27386ef7b42` · [字段定义](../../DATASET.md)*
