# google-deepmind/personality_in_llms

⭐ 50 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-01 · [GitHub](https://github.com/google-deepmind/personality_in_llms) · 组织维护

**论文复现代码：LLM 大五人格特质的测量与分析**

DeepMind 论文《Personality Traits in Large Language Models》的官方复现代码库：以 Jupyter notebook 形式提供论文的心理测量与统计分析，推理脚本从 HuggingFace 与 OpenAI 模型收集心理测量测试及下游任务数据。依赖 PsyBORGS 心理测量测试管理框架（仓库内置副本，也可从 google-research 获取更新版本），其余依赖在 notebook 内 pip install。测试会话数据存于 admin_sessions/ 目录，其他数据托管在 Google GCP 开源仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Jupyter notebook 形式提供论文复现流程
- 推理脚本支持从 HuggingFace 与 OpenAI 模型采集心理测量数据
- 内置 PsyBORGS 心理测量测试管理框架副本
- 附测试会话数据与 GCP 托管的补充数据

## 适用场景

- 复现论文中 LLM 人格测量的统计结果
- 对 LLM 施测标准化心理测量问卷并采集数据
- 研究 LLM 人格特质与下游任务表现的关系

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3: This project contains all the code necessary to verify the results of the paper
> L15: downstream task data from HuggingFace and OpenAI models are located in

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/personality_in_llms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-27 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `eb34004c916f` · [字段定义](../../DATASET.md)*
