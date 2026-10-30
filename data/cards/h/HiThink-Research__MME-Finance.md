# HiThink-Research/MME-Finance

⭐ 44 · Python · Apache-2.0 · 推送 2026-01-08 · [GitHub](https://github.com/HiThink-Research/MME-Finance) · [官网](https://hithink-research.github.io/MME-Finance/) · 组织维护 · 中文 README

**面向金融领域的双语多模态大模型评测基准**

MME-Finance 是一个双语（英文/中文）多模态金融评测基准，包含 1,171 道英文与 1,103 道中文开放式问题，覆盖 K 线图、技术指标图等金融图像类型与 OCR、实体识别、数值计算、风险提示、投资建议等多模态能力维度，另发布多轮问答（MT）与二分类（Binary）版本。评测已集成进 VLMEvalKit 框架，用户下载 TSV 数据与金融图像后通过 run.py 命令对 Qwen2-VL 等模型执行推理与评测；论文被 ACM MM 2025 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双语基准：1,171 英文 + 1,103 中文开放式问题
- 覆盖 K 线图、技术指标图、统计图表、文档等金融图像类型
- 提出考虑图像的评测策略，与人类判断一致性高
- 对 19 个 MLLM 进行评测并给出分任务与分图像类型结果

## 适用场景

- 评测多模态大模型在金融图表理解上的表现
- 比较开源与商用模型在金融分析任务中的能力
- 为金融大模型研发提供训练/评测参考数据

## 场景标签

`模型评测` `金融量化` · 领域:评测与运维

## 证据(README 行号)

> L30: Benchmarks from general fields often fail to measure the performance of multimodal models in the financial domain, 
> L40: - 🔥 Bilingual multimodal financial benchmark: MME-Finance is the first Bilingual multimodal financial benchmark whi
> L46: We have integrated MMfin into the VLMEvalKit framework. For the environment configuration and the use of API, pleas

## 星数曲线

```mermaid
xychart-beta
    title "HiThink-Research/MME-Finance 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1dadbcd94f90` · [字段定义](../../DATASET.md)*
