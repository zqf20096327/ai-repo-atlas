# MaximeRivest/sciencemadereadable

⭐ 9 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/MaximeRivest/sciencemadereadable) · [官网](https://sciencemadereadable.com) · 个人维护

**用自训练小模型把论文改写成平实语言的网站与流水线**

该项目提供 sciencemadereadable.com 网站：检索开放获取论文并输出逐段平实语言改写，与原文并排展示并保留原图表。改写由自训练的 Qwen3.5 9B/4B 模型完成，微调数据约 4,400 篇大模型改写样本。仓库包含语料采集、离线维基/词典术语表、改写评测 judge、训练代码与基于队列的应用服务；模型通过任意 OpenAI 兼容服务器（示例用 vLLM）部署，README 声明改写仍可能含事实错误。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自训练 qwen3.5-9b/4b-paper-rewriter 模型，单 GPU 即可运行
- 改写保持原文信息、不确定性与标题结构（翻译式而非摘要）
- 训练语料、术语表、benchmark judge 与 TypeScript 应用全链路代码
- 训练与生产使用逐字节相同的提示词（check_prompts.ts 校验）

## 适用场景

- 以平实语言阅读开放获取的科学论文
- 复现或研究论文改写的训练与评测流程
- 用自部署的 OpenAI 兼容服务器运行改写模型

## 场景标签

`模型评测` `微调` `AI 写作` · 领域:评测与运维

## 证据(README 行号)

> L3: **https://sciencemadereadable.com**: search open research papers and read them rewritten in plain
> L8: It is done by a small model we trained (Qwen3.5 9B, fine-tuned on about 4,400 papers rewritten by
> L9: large models), which runs on a single GPU.

## 星数曲线

```mermaid
xychart-beta
    title "MaximeRivest/sciencemadereadable 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 8 --> 10
    line [9, 9]
```

2026-10-18 9 → 2026-11-20 9（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `097e6a641ce4` · [字段定义](../../DATASET.md)*
