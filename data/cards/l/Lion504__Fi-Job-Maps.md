# Lion504/Fi-Job-Maps

⭐ 14 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Lion504/Fi-Job-Maps) · [官网](https://lion504.github.io/Fi-Job-Maps/) · 个人维护 · 中文 README

**芬兰职位市场交互可视化：StatFin 职业数据叠加 AI 暴露度评分**

从 Statistics Finland 的 PxWeb API 抓取职业分类（2010 分类，默认 459 个 Level 4 单元组）的就业、薪资、前景数据，生成按层级（Level 1-4）浏览的交互地图站点，部署于 GitHub Pages。AI 暴露度由 LLM 对每个职业打 0-10 分（默认 Claude，Gemini 可选，无 key 时回退规则估计），组级分数按就业加权平均，分数缓存于 scores.json。GitHub Actions 每周一自动刷新数据并通过 check_site_data.py 校验。未发布中位薪资的 97 个单元组由最近上级组估计并标注来源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 为 459 个职业单元组打 0-10 的 AI 暴露分（约 460 次调用，$0.10-0.20）
- Claude 默认、Vertex/AI Studio 可选、无 key 回退规则估计的三后端设计
- 每周一 GitHub Actions 自动抓取、评分、构建并校验发布
- 缺失中位薪资按最近上级组估计并记录 pay_source/pay_basis 可审计

## 适用场景

- 浏览芬兰各职业的就业、薪资与 AI 暴露度分布
- 按职业分类层级切换查看全国劳动力构成
- 追踪芬兰职位市场数据的每周自动更新

## 场景标签

 · 领域:劳动力市场/数据可视化

## 证据(README 行号)

> L3: Explore Finnish occupation data (StatFin PxWeb + Occupational Barometer) and color it by AI exposure.
> L28: - `finlandjobs infer` – add AI exposure estimates (optional)
> L44: `finlandjobs infer` scores each occupation with an LLM when a key is set in `.env`, and falls back to a rule-based 

## 星数曲线

```mermaid
xychart-beta
    title "Lion504/Fi-Job-Maps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3842b04968eb` · [字段定义](../../DATASET.md)*
