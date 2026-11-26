# abdullahdmc/open-health-databases

⭐ 3 · JavaScript · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/abdullahdmc/open-health-databases) · [官网](https://healthdata.abdullahdmc.com) · 个人维护

**400 个免费健康/临床数据库的可检索编目站**

以 JSON 数据为单一事实来源、Node 脚本构建的可搜索目录，收录 17 个类别共 400 个免费健康与临床数据库（MIMIC-IV、eICU、NHANES、TCGA、PhysioNet 等），每条提供简介、原始描述论文链接、数据获取链接及 Open/Registration/Application/Credentialed 四级访问模式标注。构建产物包括站点、CSV、JSON 与 Markdown 全表；verify 脚本自动校验访问 URL、Crossref DOI 解析与 PhysioNet 访问策略。收费数据源被明确排除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 收录 400 个免费健康数据库，按 17 个类别组织
- 每条目标注四种访问模式（Open/Registration/Application/Credentialed）
- verify 脚本自动检查链接、DOI 与访问策略
- 无第三方依赖，仅需 Node 18+

## 适用场景

- 查找某研究领域可免费获取的临床/健康数据集
- 按访问门槛（注册/申请/认证）筛选数据源
- 为论文引用数据库时获取规范引文格式

## 场景标签

`科研工具` `精选清单` · 领域:学习与行业

## 证据(README 行号)

> L5: A curated, searchable catalogue of **400 freely available health and clinical databases** in 17 categories, such as 
> L25: ICU, perioperative and emergency care · EHR, cohorts, registries and synthetic data · population and public-health 

## 星数曲线

```mermaid
xychart-beta
    title "abdullahdmc/open-health-databases 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-25 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `437eaabe0dbb` · [字段定义](../../DATASET.md)*
