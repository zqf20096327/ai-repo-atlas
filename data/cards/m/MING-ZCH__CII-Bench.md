# MING-ZCH/CII-Bench

⭐ 26 · Python · 推送 2026-04-09 · [GitHub](https://github.com/MING-ZCH/CII-Bench) · [官网](https://aclanthology.org/2025.acl-long.700.pdf) · 组织维护 · 中文 README

**评测 MLLM 对中文图像深层寓意理解能力的基准数据集**

ACL 2025 论文配套的多模态大模型评测基准：698 张来自中文互联网与中国传统文化（如传统绘画）的图像，由 30 名本科生人工收集与标注，构成 800 道六选一选择题，覆盖隐喻、象征与细节理解，其中 765 题构成测试集、35 题用于 few-shot 开发验证集。提供基于 lmdeploy、vLLM 及自定义模型的推理脚本与评分脚本，另含中国传统文化子项评测（CTC_Evaluation）。论文报告 MLLM 最高准确率 64.4%，人类平均 78.2%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 698 张中文图像、800 道人工标注六选一选择题
- 涵盖隐喻、象征与图像细节理解，含中国传统文化子评测
- 支持 lmdeploy、vLLM API 服务及自定义模型接入的推理评测流程

## 适用场景

- 评测多模态大模型对中文图像深层含义的理解能力
- 分析模型在中国传统文化图像上的表现差异
- 研究加入图像情绪提示对模型准确率的影响

## 场景标签

`模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L15: To fill the gap, we introduce the **C**hinese **I**mage **I**mplication understanding **Bench**mark, **CII-Bench**,
> L29: CII-Bench contains a total of **698** various Chinese images. These images are manually collected and annotated by 
> L102: First, configure the environment required for vLLM link

## 星数曲线

```mermaid
xychart-beta
    title "MING-ZCH/CII-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `70e382326da3` · [字段定义](../../DATASET.md)*
