# williamjsmail/piranha

⭐ 17 · JavaScript · 推送 2025-11-04 · [GitHub](https://github.com/williamjsmail/piranha) · [官网](https://zread.ai/williamjsmail/piranha) · 个人维护

**面向网络防御分析师的威胁分析与狩猎规划工具**

连接情报分析师与防御性网络操作的平台：选择 APT 组织后检索其关联的 MITRE ATT&CK 战术与技术，支持 IoM 图谱可视化、战术组合优化、雷达图展示威胁画像分布。可导入 Nessus XML 扫描提取 CVE 并映射到 ATT&CK 技术、生成热力图，支持威胁画像构建与 F1 匹配评分，并提供 AI 增强功能。以 Python 脚本形式通过源码安装运行，面向威胁情报团队与狩猎分析人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- APT 关联的 MITRE ATT&CK 战术/技术检索与重叠分析
- Nessus XML 导入：CVE 提取并通过 cve2capec 映射 ATT&CK 技术、生成热力图
- IoM 图谱可视化与战术组合优化引擎
- 威胁画像与扫描结果 F1 匹配评分

## 适用场景

- 把优先情报需求（PIR）转化为可执行的狩猎计划
- 评估威胁画像在数据采集类别上的覆盖分布
- 将 Nessus 漏洞扫描结果与 APT 威胁画像匹配以排优先级

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L39:  - AI Enrichment
> L51: - Add support for multiple GPTs

## 星数曲线

```mermaid
xychart-beta
    title "williamjsmail/piranha 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 low · 依据 README sha `52825f69d1a6` · [字段定义](../../DATASET.md)*
